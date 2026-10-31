#!/usr/bin/env python3
"""Check every URL in data/manuals.yaml and data/links.yaml.

Stdlib only. Politeness: one request at a time by default, short timeout, no retries beyond
one on connection errors.

Exit status:
  0  every URL resolved (blocked-but-expected entries are reported, not failures)
  1  at least one unexpected failure
"""

from __future__ import annotations

import argparse
import pathlib
import sys
import urllib.error
import urllib.request

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required (python3-yaml)")

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (X11; Linux x86_64) ibm5100-docs-linkcheck/1.0"

OK = range(200, 300)
BLOCKED = {401, 403, 429, 503}


def fetch(url: str, timeout: float):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            resp.read(1024)
            return resp.status, resp.geturl(), ""
    except urllib.error.HTTPError as exc:
        return exc.code, url, str(exc.reason)
    except Exception as exc:  # noqa: BLE001 - we want the message, whatever it is
        return 0, url, f"{type(exc).__name__}: {exc}"


def load_urls() -> list[dict]:
    entries: list[dict] = []
    manuals = yaml.safe_load((ROOT / "data" / "manuals.yaml").read_text())
    for m in manuals["manuals"]:
        entries.append(
            {
                "url": m["url"],
                "label": f"{m.get('part_number') or m['family']}: {m['title']}",
                "source": "manuals",
                "expected_blocked": False,
            }
        )
    links_path = ROOT / "data" / "links.yaml"
    if links_path.exists():
        links = yaml.safe_load(links_path.read_text())
        for link in links.get("links", []):
            entries.append(
                {
                    "url": link["url"],
                    "label": link.get("title", link["url"]),
                    "source": "links",
                    "expected_blocked": bool(link.get("known_blocked", False)),
                }
            )
    return entries


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--timeout", type=float, default=30.0)
    ap.add_argument("--only", choices=["manuals", "links"], help="check one source only")
    ap.add_argument("--quiet", action="store_true", help="only print problems and the summary")
    args = ap.parse_args()

    entries = load_urls()
    if args.only:
        entries = [e for e in entries if e["source"] == args.only]

    failures: list[tuple[dict, int, str]] = []
    blocked: list[dict] = []
    checked = 0

    for entry in entries:
        status, final, detail = fetch(entry["url"], args.timeout)
        checked += 1
        if status in OK:
            if not args.quiet:
                print(f"  ok   {status}  {entry['label'][:70]}")
        elif status in BLOCKED:
            if entry["expected_blocked"]:
                blocked.append(entry)
                if not args.quiet:
                    print(f"  blk  {status}  {entry['label'][:70]} (expected)")
            else:
                blocked.append(entry)
                print(f"  BLOCKED {status}  {entry['label']}\n         {entry['url']}\n         {detail}")
        else:
            failures.append((entry, status, detail))
            print(f"  FAIL {status or '---'}  {entry['label']}\n         {entry['url']}\n         {detail}")

    print()
    print(f"checked {checked} URL(s): {checked - len(failures) - len(blocked)} ok, "
          f"{len(blocked)} blocked, {len(failures)} failed")

    if blocked:
        print("\nblocked (bot protection; verify by hand if you need the content):")
        for entry in blocked:
            print(f"  - {entry['label']}  <{entry['url']}>")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
