#!/usr/bin/env python3
"""Convert a Project Gateway field-survey export (Survey123 CSV) into data/gateway/colonies.json.

Usage: python3 scripts/gateway_survey_to_json.py path/to/survey_export.csv

Each nest keeps the outcome of the survey's own field aggression trial. Nests collected for the
classroom trials also get their colony collection code ("code"). The results page joins that code
with data/gateway/colony_summary.json, because the classroom result is not known at collection time.

The output is embedded in a public page, so free-text notes and vial labels (which name landowners
and describe properties) are never written.
"""
from __future__ import annotations

import csv
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "gateway" / "colonies.json"

# The map covers Alberta; points outside its bounding box (e.g. a Northwest Territories survey) stay off it.
LAT_RANGE = (49.0, 60.0)
LNG_RANGE = (-120.0, -110.0)

# Survey records kept off the public map at the team's request (130: Sep 12, 2026 nest in the Jasper area).
EXCLUDED = {130}

TIME_FORMATS = ("%m/%d/%Y %H:%M", "%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S")  # July export, then Sep 2026 onward

# A record whose notes say it "replaces" another supersedes the nearest earlier record within this radius.
REPLACE_RADIUS_M = 30.0

# The newer survey has "What is the classroom outreach experimental colony collection code?";
# older records only mention the code in Notes ("This is colony EXP001").
CODE_COLUMN_HINT = "colony collection code"
CODE_RE = re.compile(r"\bEXP\s*-?\s*0*(\d+)\b", re.IGNORECASE)

# Survey123 choice names that don't read well with underscores swapped for spaces.
LABELS = {"Mixed_conifer_and_deciduous_for": "Mixed conifer and deciduous forest"}

OUTCOMES = {"The ants fought": "not-supercolony", "The ants did not fight": "supercolony"}


def norm(header: str) -> str:
    return " ".join(header.split()).lower()


def label(choice: str) -> str:
    if choice in LABELS:
        return LABELS[choice]
    text = choice.replace("_", " ").strip()
    return text[:1].upper() + text[1:]


def code_of(text: str) -> str | None:
    match = CODE_RE.search(text or "")
    return f"EXP{int(match.group(1)):03d}" if match else None


def parse_time(text: str) -> datetime:
    for fmt in TIME_FORMATS:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError(f"unrecognised survey time {text!r}")


def distance_m(a: tuple[float, float], b: tuple[float, float]) -> float:
    lat1, lng1, lat2, lng2 = map(math.radians, (*a, *b))
    h = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lng2 - lng1) / 2) ** 2
    return 6371000 * 2 * math.asin(math.sqrt(h))


def load_rows(path: Path) -> list[dict[str, str]]:
    """Rows keyed by normalised header. The export repeats 'Ant species'; the first column holds the answer."""
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        headers = [norm(h) for h in next(reader)]
        rows = []
        for values in reader:
            row: dict[str, str] = {}
            for header, value in zip(headers, values):
                row.setdefault(header, value.strip())
            rows.append(row)
    return rows


def convert(rows: list[dict[str, str]], *, link_codes: bool = True, drop_replaced: bool = True) -> list[dict[str, Any]]:
    code_column = next((h for h in rows[0] if CODE_COLUMN_HINT in h), None) if rows else None

    nests = []
    for row in rows:
        if row.get("objectid", "").isdigit() and int(row["objectid"]) in EXCLUDED:
            continue
        try:
            point = (float(row["y"]), float(row["x"]))
        except (KeyError, ValueError):
            print(f"skipped object {row.get('objectid')}: no coordinates", file=sys.stderr)
            continue
        if not (LAT_RANGE[0] <= point[0] <= LAT_RANGE[1] and LNG_RANGE[0] <= point[1] <= LNG_RANGE[1]):
            print(f"skipped object {row.get('objectid')}: {point} is outside Alberta", file=sys.stderr)
            continue
        nests.append((row, point, parse_time(row["date and time"])))

    superseded: set[int] = set()
    if drop_replaced:
        for i, (row, point, when) in enumerate(nests):
            if "replaces" not in row["notes"].lower():
                continue
            earlier = [j for j, (_, _, other_when) in enumerate(nests) if j != i and other_when < when]
            if not earlier:
                continue
            j = min(earlier, key=lambda k: distance_m(point, nests[k][1]))
            gap = distance_m(point, nests[j][1])
            if gap <= REPLACE_RADIUS_M:
                superseded.add(j)
                print(f"object {row['objectid']} replaces object {nests[j][0]['objectid']} ({gap:.0f} m away)", file=sys.stderr)

    out = []
    for i, (row, point, _) in enumerate(nests):
        if i in superseded:
            continue
        trialled = row["were aggression trials completed at this nest?"] == "Yes"
        nest: dict[str, Any] = {
            "lat": round(point[0], 6),
            "lng": round(point[1], 6),
            "outcome": OUTCOMES.get(row["did the ants attack the ant that was dropped onto the nest?"], "surveyed") if trialled else "surveyed",
        }
        code = (code_of(row.get(code_column, "")) if code_column else None) or code_of(row["notes"])
        if link_codes and code:
            nest["code"] = code
        nest.update({
            "date": row["date and time"].split()[0],
            "shape": label(row["nest shape"]),
            "environment": label(row["describe the environment where you found the nest"]),
            "species": label(row["ant species"]),
            "collected": row["were specimens collected at this site?"],
            "trial": row["were aggression trials completed at this nest?"],
        })
        out.append(nest)

    seen: dict[str, int] = {}
    for nest in out:
        if "code" in nest:
            seen[nest["code"]] = seen.get(nest["code"], 0) + 1
    for code, count in sorted(seen.items()):
        if count > 1:
            print(f"warning: {code} is on {count} nests; the map links to the last one", file=sys.stderr)
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    nests = convert(load_rows(Path(sys.argv[1])))
    DATA_PATH.write_text(json.dumps(nests, indent=1, ensure_ascii=False), encoding="utf-8")
    coded = sorted(n["code"] for n in nests if "code" in n)
    print(f"wrote {len(nests)} nests to {DATA_PATH.relative_to(ROOT)}; {len(coded)} with colony codes: {', '.join(coded)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
