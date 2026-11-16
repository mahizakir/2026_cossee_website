# How cossee.org is deployed

The site is served by the lab web server (`ssh cossee`, cossee.biology.ualberta.ca),
not by GitHub Pages. The server cannot be reached by SSH from outside campus, so
GitHub does not push to it. The server pulls instead.

## The loop

1. You push to `main` on GitHub (or the daily ORCID workflow commits new data).
2. Within about 5 minutes, `cossee-site.timer` on the server runs
   `~/cossee-site/bin/update-site.sh`.
3. The script fetches `main`. If there is a new commit, or the date has changed
   since the last build, it builds the site with Hugo into a fresh folder under
   `~/cossee-site/releases/` and repoints the `~/cossee-site/current` symlink.
4. Caddy serves `~/cossee-site/current` as https://cossee.org.

A failed build never replaces the live site. The previous release keeps serving
and the failure is in the log.

## Useful commands (on the server, no sudo needed)

    systemctl --user list-timers cossee-site.timer     # when it last ran, when next
    journalctl --user -u cossee-site -n 50             # build log
    ~/cossee-site/bin/update-site.sh --force           # rebuild right now
    cat ~/cossee-site/state/built-commit               # commit that is live
    ls ~/cossee-site/releases                          # the last few builds

Roll back to an earlier build:

    ln -sfn releases/<folder name> ~/cossee-site/current

That lasts until the next successful build, so also revert the bad commit.

## Files in this folder

| File | Lives on the server at |
| ---- | ---------------------- |
| `update-site.sh` | `~/cossee-site/bin/update-site.sh` |
| `cossee-site.service`, `cossee-site.timer` | `~/.config/systemd/user/` |
| `cossee.org.caddy` | `/etc/caddy/sites/` (needs sudo, then `caddy-reload`) |

The copies on the server are the ones that run. Editing a file here changes
nothing until it is copied over. That is deliberate: a push to the repo can
change the website but cannot run commands on the server.

## Hugo version

Hugo extended is at `~/.local/hugo/hugo` on the server. Keep it on the same
version as your local Hugo (0.157.0 when this was set up).
