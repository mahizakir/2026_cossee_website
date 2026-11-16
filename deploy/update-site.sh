#!/usr/bin/env bash
# Build cossee.org from its GitHub repo and publish it on this server.
#
# Run every few minutes by the cossee-site.timer systemd user unit. It does
# nothing unless main has a new commit or the local date has changed. The daily
# rebuild is what publishes posts whose date has just arrived.
#
#   update-site.sh            build only if needed
#   update-site.sh --force    build now, whatever the state
#
# Layout under ~/cossee-site:
#   bin/        this script (installed copy; deploy/ in the repo is the source)
#   src/        clone of the repo. Never edit here, it is reset on every build.
#   releases/   one folder per build, newest few kept
#   current     symlink to the live release. Caddy serves this path.
#   state/      last built commit and day, lock file
#   cache/      Hugo's cache

set -euo pipefail
umask 022

REPO_URL="https://github.com/mahizakir/2026_cossee_website.git"
BRANCH="main"
BASE="${COSSEE_SITE_HOME:-$HOME/cossee-site}"
HUGO="${HUGO_BIN:-$HOME/.local/hugo/hugo}"
KEEP=3 # releases to keep, including the live one

SRC="$BASE/src"
STATE="$BASE/state"

log() { printf '%s\n' "$*"; }

read_state() { cat "$STATE/$1" 2>/dev/null || true; }

# Record a failed commit so it is retried once a day or when a fix lands,
# instead of on every timer tick.
fail() {
  local commit="$1" today="$2" release="$3" reason="$4"
  log "BUILD FAILED for ${commit:0:7}: $reason. The previous release stays live."
  rm -rf "$release"
  printf '%s\n' "$commit" >"$STATE/failed-commit"
  printf '%s\n' "$today" >"$STATE/failed-day"
  exit 1
}

main() {
  local force=0
  [[ "${1:-}" == "--force" ]] && force=1

  mkdir -p "$BASE/releases" "$STATE" "$BASE/cache"

  # One run at a time.
  exec 9>"$STATE/lock"
  if ! flock -n 9; then
    log "another build is running, skipping"
    return 0
  fi

  if [[ ! -d "$SRC/.git" ]]; then
    log "cloning $REPO_URL"
    git clone --quiet --branch "$BRANCH" "$REPO_URL" "$SRC"
  fi

  git -C "$SRC" fetch --quiet origin "$BRANCH"

  local new old today
  new="$(git -C "$SRC" rev-parse FETCH_HEAD)"
  old="$(read_state built-commit)"
  today="$(date +%F)"

  if ((!force)); then
    if [[ "$new" == "$old" && "$today" == "$(read_state built-day)" ]]; then
      return 0 # nothing new
    fi
    if [[ "$new" == "$(read_state failed-commit)" && "$today" == "$(read_state failed-day)" ]]; then
      return 0 # this commit already failed today; wait for a fix
    fi
  fi

  log "building ${new:0:7} (live: ${old:0:7})"
  git -C "$SRC" checkout --quiet --force --detach "$new"
  git -C "$SRC" submodule update --quiet --init --recursive --force

  local name release
  name="$(date -u +%Y%m%dT%H%M%SZ)-${new:0:7}"
  release="$BASE/releases/$name"

  # Same command as the old GitHub Actions build, in UTC like its runners.
  if ! TZ=UTC "$HUGO" --source "$SRC" --destination "$release" \
    --gc --minify --cacheDir "$BASE/cache"; then
    fail "$new" "$today" "$release" "hugo exited with an error"
  fi
  if [[ ! -s "$release/index.html" ]]; then
    fail "$new" "$today" "$release" "no index.html was produced"
  fi

  # Swap the live symlink in one atomic rename, so no request sees half a site.
  ln -sfn "releases/$name" "$BASE/current.new"
  mv -Tf "$BASE/current.new" "$BASE/current"

  printf '%s\n' "$new" >"$STATE/built-commit"
  printf '%s\n' "$today" >"$STATE/built-day"
  rm -f "$STATE/failed-commit" "$STATE/failed-day"
  log "published $name"

  # Drop old releases. Names start with a UTC timestamp, so they sort by age.
  local old_release
  while read -r old_release; do
    [[ "$old_release" == "$name" ]] && continue
    rm -rf "${BASE:?}/releases/${old_release:?}"
  done < <(ls -1 "$BASE/releases" | sort -r | tail -n +$((KEEP + 1)))
}

main "$@"
