#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "orcid_publications.json"
DEFAULT_ORCID_ID = "0000-0002-7765-5182"
API_BASE = "https://pub.orcid.org/v3.0"
RECORD_BASE = "https://orcid.org"
USER_AGENT = "COSSEE Publications Updater/1.0 (+https://cossee.org/)"


def fetch_json(url: str, token: str | None = None) -> dict[str, Any]:
    headers = {
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=90) as response:
        return json.loads(response.read().decode("utf-8"))


def text_value(value: Any) -> str | None:
    if isinstance(value, dict):
        return value.get("value")
    return value


def normalize_doi(raw: str | None) -> str | None:
    if not raw:
        return None
    doi = raw.strip()
    doi = doi.removeprefix("https://doi.org/")
    doi = doi.removeprefix("http://doi.org/")
    doi = doi.removeprefix("doi:")
    doi = doi.strip()
    return doi.lower() if doi else None


def doi_url(raw: str | None) -> str | None:
    doi = normalize_doi(raw)
    if not doi:
        return None
    return f"https://doi.org/{doi}"


def best_link(work: dict[str, Any], doi_link: str | None) -> str | None:
    candidate = text_value(work.get("url"))
    if candidate:
        return candidate
    return doi_link


def publication_parts(publication_date: dict[str, Any] | None) -> tuple[str, str, str]:
    publication_date = publication_date or {}
    year = text_value(publication_date.get("year")) or "Unknown"
    month = (text_value(publication_date.get("month")) or "").zfill(2)
    day = (text_value(publication_date.get("day")) or "").zfill(2)
    return year, month, day


def display_date(year: str, month: str, day: str) -> str:
    if year == "Unknown":
        return "Date unavailable"
    if month and day:
        try:
            dt = datetime(int(year), int(month), int(day))
            return dt.strftime("%B %-d, %Y")
        except ValueError:
            pass
    if month:
        try:
            dt = datetime(int(year), int(month), 1)
            return dt.strftime("%B %Y")
        except ValueError:
            pass
    return year


def display_type(value: str | None) -> str:
    if not value:
        return "Other"
    return value.replace("-", " ").title()


def iso_date(year: str, month: str, day: str) -> str:
    safe_month = month if month else "00"
    safe_day = day if day else "00"
    if year == "Unknown":
        return "0000-00-00"
    return f"{year}-{safe_month}-{safe_day}"


def summary_score(summary: dict[str, Any]) -> tuple[int, int, int]:
    source_name = ((summary.get("source") or {}).get("source-name") or {}).get("value") or ""
    source_name = source_name.lower()
    year, month, day = publication_parts(summary.get("publication-date"))
    external_ids = ((summary.get("external-ids") or {}).get("external-id")) or []
    doi_present = any((item.get("external-id-type") or "").lower() == "doi" for item in external_ids)

    score = 0
    if doi_present:
        score += 8
    if text_value(summary.get("journal-title")):
        score += 4
    if text_value(summary.get("url")):
        score += 2
    if day:
        score += 2
    elif month:
        score += 1
    if source_name == "crossref":
        score += 4
    elif source_name == "datacite":
        score += 3
    elif source_name == "f1000":
        score -= 1
    if summary.get("type"):
        score += 1

    modified_value = ((summary.get("last-modified-date") or {}).get("value")) or 0
    put_code = summary.get("put-code") or 0
    return score, int(modified_value), int(put_code)


def authors_from_detail(detail: dict[str, Any]) -> list[str]:
    authors = []
    contributors = ((detail.get("contributors") or {}).get("contributor")) or []
    for contributor in contributors:
        name = text_value(contributor.get("credit-name"))
        if name:
            authors.append(name.strip())
    return authors


def format_authors(authors: list[str]) -> str | None:
    clean = [author for author in authors if author]
    if not clean:
        return None
    if len(clean) <= 12:
        return ", ".join(clean)
    return ", ".join(clean[:12]) + ", et al."


def extract_doi(work: dict[str, Any]) -> tuple[str | None, str | None]:
    external_ids = ((work.get("external-ids") or {}).get("external-id")) or []
    for item in external_ids:
        if (item.get("external-id-type") or "").lower() == "doi":
            raw = item.get("external-id-value")
            normalized = normalize_doi(raw)
            return normalized, doi_url(raw)
    return None, None


def work_record(orcid_id: str, detail: dict[str, Any]) -> dict[str, Any]:
    doi, doi_link = extract_doi(detail)
    year, month, day = publication_parts(detail.get("publication-date"))
    authors = authors_from_detail(detail)
    title = text_value((detail.get("title") or {}).get("title")) or "Untitled work"
    journal = text_value(detail.get("journal-title"))
    source = ((detail.get("source") or {}).get("source-name") or {}).get("value")
    link = best_link(detail, doi_link)
    put_code = detail.get("put-code")

    return {
        "put_code": put_code,
        "title": title,
        "authors": authors,
        "authors_display": format_authors(authors),
        "journal_title": journal,
        "type": detail.get("type") or "other",
        "type_display": display_type(detail.get("type")),
        "publication_year": year,
        "publication_month": month or None,
        "publication_day": day or None,
        "publication_date_display": display_date(year, month, day),
        "publication_date_iso": iso_date(year, month, day),
        "doi": doi,
        "doi_url": doi_link,
        "best_url": link,
        "source_name": source,
        "orcid_work_url": f"{RECORD_BASE}/{orcid_id}/work/{put_code}" if put_code else None,
    }


def build_payload(orcid_id: str, token: str | None) -> dict[str, Any]:
    works_url = f"{API_BASE}/{orcid_id}/works"
    works_response = fetch_json(works_url, token=token)
    groups = works_response.get("group") or []

    selected_summaries = []
    for group in groups:
        summaries = group.get("work-summary") or []
        if not summaries:
            continue
        best = max(summaries, key=summary_score)
        selected_summaries.append(best)

    details = []
    for summary in selected_summaries:
        put_code = summary.get("put-code")
        if not put_code:
            continue
        detail_url = f"{API_BASE}/{orcid_id}/work/{put_code}"
        detail = fetch_json(detail_url, token=token)
        details.append(work_record(orcid_id, detail))

    details.sort(
        key=lambda item: (
            item["publication_date_iso"],
            item["title"].lower(),
        ),
        reverse=True,
    )

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    type_counts: dict[str, int] = defaultdict(int)
    for item in details:
        grouped[item["publication_year"]].append(item)
        type_counts[item["type"]] += 1

    year_keys = sorted(
        grouped.keys(),
        key=lambda value: (value != "Unknown", value if value != "Unknown" else ""),
        reverse=True,
    )
    years = [
        {
            "year": year,
            "count": len(grouped[year]),
            "items": grouped[year],
        }
        for year in year_keys
    ]

    latest = details[:6]
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    payload = {
        "orcid_id": orcid_id,
        "record_url": f"{RECORD_BASE}/{orcid_id}",
        "works_api_url": works_url,
        "generated_at": generated_at,
        "generated_at_display": datetime.now(timezone.utc).strftime("%B %d, %Y at %H:%M UTC"),
        "works_count": len(details),
        "latest": latest,
        "years": years,
        "type_counts": dict(sorted(type_counts.items())),
    }
    return payload


def payload_without_timestamp(payload: dict[str, Any]) -> dict[str, Any]:
    copy = json.loads(json.dumps(payload))
    copy.pop("generated_at", None)
    return copy


def main() -> int:
    orcid_id = os.environ.get("ORCID_ID", DEFAULT_ORCID_ID)
    token = os.environ.get("ORCID_ACCESS_TOKEN")

    try:
        payload = build_payload(orcid_id, token)
    except urllib.error.HTTPError as exc:
        print(f"Failed to fetch ORCID data: HTTP {exc.code} {exc.reason}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"Failed to fetch ORCID data: {exc.reason}", file=sys.stderr)
        return 1

    if DATA_PATH.exists():
        existing = json.loads(DATA_PATH.read_text())
        if payload_without_timestamp(existing) == payload_without_timestamp(payload):
            payload["generated_at"] = existing.get("generated_at", payload["generated_at"])

    DATA_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {payload['works_count']} ORCID publications to {DATA_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
