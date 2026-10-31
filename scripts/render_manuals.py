#!/usr/bin/env python3
"""Render docs/manuals.md from data/manuals.yaml.

Stdlib only. Run from the repo root or via `make manuals`.
"""

from __future__ import annotations

import datetime as dt
import pathlib
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml (or use the distro package python3-yaml)")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "manuals.yaml"
OUT = ROOT / "docs" / "manuals.md"

FAMILY_ORDER = ["ibm-5100", "ibm-5110", "ibm-5120", "ibm-5103", "supporting"]

FAMILY_TITLES = {
    "ibm-5100": ("IBM 5100", "The complete 5100 publication library as listed by IBM in the MIM, plus two non-manual documents."),
    "ibm-5110": ("IBM 5110 and 5114", "The follow-on family. Same architectural pattern, one generation later."),
    "ibm-5120": ("IBM 5120", "The larger follow-on system."),
    "ibm-5103": ("IBM 5103 printer", "The 5100's optional dot-matrix printer."),
    "supporting": ("Supporting IBM references", "Documents IBM cites as related publications, and the APL/System-3 context material."),
}

TYPE_LABELS = {
    "reference": "Reference manual",
    "introduction": "Introduction / tutorial",
    "user-guide": "User's guide",
    "maintenance": "Maintenance (MIM/MAP)",
    "parts-catalog": "Parts catalog",
    "communications": "Communications",
    "feature-manual": "Feature manual",
    "general-information": "General information",
    "bibliography": "Bibliography",
    "logic-manual": "Logic manual",
    "technical-report": "Technical report",
    "conference-paper": "Conference paper",
}


def human_size(n: int | None, server_size: str | None) -> str:
    if not n:
        if server_size:
            for suffix, word in (("K", " KB"), ("M", " MB"), ("G", " GB")):
                if server_size.endswith(suffix):
                    return server_size[: -len(suffix)] + word
            return server_size
        return "—"
    units = ["B", "KB", "MB", "GB"]
    value = float(n)
    index = 0
    while value >= 1024 and index < len(units) - 1:
        value /= 1024
        index += 1
    return f"{value:.0f} B" if index == 0 else f"{value:.1f} {units[index]}"


def esc(text: str) -> str:
    return text.replace("|", "\\|")


def entry_row(e: dict) -> str:
    part = e.get("part_number") or "—"
    title = esc(e["title"])
    edition = e.get("edition") or ""
    date = e.get("date", "")
    if edition:
        date = f"{date} ({edition})"
    kind = TYPE_LABELS.get(e.get("doc_type", ""), e.get("doc_type", ""))
    size = human_size(e.get("bytes"), e.get("server_size"))
    short = (e.get("sha256") or "")[:12]
    link = f"[PDF]({e['url']})"
    row = f"| `{part}` | {title} | {date} | {kind} | {size} | `{short or '—'}` | {link} |"
    if e.get("notes"):
        row += f"\n| | *{esc(e['notes'])}* | | | | | |"
    return row


def main() -> int:
    if not DATA.exists():
        return f"missing {DATA}"
    doc = yaml.safe_load(DATA.read_text())
    manuals = doc["manuals"]

    lines: list[str] = []
    lines.append("# Manual catalogue")
    lines.append("")
    lines.append(
        "Generated from [`data/manuals.yaml`](../data/manuals.yaml) by "
        "[`scripts/render_manuals.py`](../scripts/render_manuals.py). Do not edit by hand — "
        "edit the YAML and run `make manuals`."
    )
    lines.append("")
    lines.append(
        f"**{len(manuals)} documents.** Every link points at bitsavers (or, for the supporting "
        "set, the relevant IBM directory on bitsavers). Sizes are the actual file sizes where a "
        "copy was fetched; SHA-256 is recorded where computed, so `make fetch` can verify a "
        "local archive byte-for-byte."
    )
    lines.append("")

    counts = {f: sum(1 for m in manuals if m["family"] == f) for f in FAMILY_ORDER}
    lines.append("| Family | Documents |")
    lines.append("|---|---|")
    for f in FAMILY_ORDER:
        lines.append(f"| {FAMILY_TITLES[f][0]} | {counts[f]} |")
    lines.append("")

    for family in FAMILY_ORDER:
        group = [m for m in manuals if m["family"] == family]
        if not group:
            continue
        group.sort(key=lambda m: (m.get("date", ""), m.get("part_number") or ""))
        title, blurb = FAMILY_TITLES[family]
        lines.append(f"## {title}")
        lines.append("")
        lines.append(blurb)
        lines.append("")
        lines.append("| Part no. | Title | Date (ed.) | Type | Size | SHA-256 | Link |")
        lines.append("|---|---|---|---|---|---|---|")
        for e in group:
            lines.append(entry_row(e))
        lines.append("")

    missing = doc.get("missing") or []
    if missing:
        lines.append("## Known IBM publications not located")
        lines.append("")
        lines.append(
            "Identified from IBM's own publication lists but not found in any public archive. "
            "These are the highest-value gaps."
        )
        lines.append("")
        lines.append("| Part no. | Title | Where it is referenced |")
        lines.append("|---|---|---|")
        for m in missing:
            lines.append(
                f"| `{m['part_number']}` | {esc(m['title'])} | {esc(m.get('reference', ''))} |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "IBM manuals are © International Business Machines Corporation and are not "
        "redistributed here. Runs of the manuals are image-only scans; OCR text exists for "
        "most but not all, and figure content (device address tables, card layouts) is lost in "
        "text extraction. Always check the page image."
    )
    lines.append("")

    OUT.write_text("\n".join(lines))
    print(f"wrote {OUT.relative_to(ROOT)} ({len(manuals)} documents, {len(missing)} gaps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
