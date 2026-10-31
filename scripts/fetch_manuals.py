#!/usr/bin/env python3
"""Download the manual set into a local archive and verify SHA-256.

Scans are not redistributed by this repository; this script fetches them for personal
research into a gitignored directory. Sequential by default — bitsavers is a volunteer
archive, so do not parallelise it.

Usage:
    make fetch
    python3 scripts/fetch_manuals.py --dest _archive
    python3 scripts/fetch_manuals.py --verify-only
    python3 scripts/fetch_manuals.py --family ibm-5100
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import sys
import urllib.error
import urllib.request

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required (python3-yaml)")

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (X11; Linux x86_64) ibm5100-docs-fetch/1.0"


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(url: str, dest: pathlib.Path, timeout: float) -> tuple[str, int]:
    """Stream to a .part file, hashing as we go. Returns (sha256, bytes)."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    digest = hashlib.sha256()
    size = 0
    tmp = dest.with_suffix(dest.suffix + ".part")
    with urllib.request.urlopen(req, timeout=timeout) as resp, tmp.open("wb") as out:
        while True:
            chunk = resp.read(1 << 20)
            if not chunk:
                break
            digest.update(chunk)
            size += len(chunk)
            out.write(chunk)
    tmp.replace(dest)
    return digest.hexdigest(), size


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dest", default=str(ROOT / "_archive"), help="destination directory")
    ap.add_argument("--family", action="append", help="limit to one or more families (repeatable)")
    ap.add_argument("--verify-only", action="store_true", help="do not download; verify what exists")
    ap.add_argument("--timeout", type=float, default=300.0)
    ap.add_argument("--limit", type=int, help="stop after N documents (useful for testing)")
    args = ap.parse_args()

    dest_dir = pathlib.Path(args.dest)
    dest_dir.mkdir(parents=True, exist_ok=True)

    doc = yaml.safe_load((ROOT / "data" / "manuals.yaml").read_text())
    manuals = doc["manuals"]
    if args.family:
        manuals = [m for m in manuals if m["family"] in args.family]
    if args.limit:
        manuals = manuals[: args.limit]

    ok = skipped = mismatched = failed = missing = 0
    for entry in manuals:
        target = dest_dir / entry["filename"]
        expected = entry.get("sha256")
        label = f"{entry.get('part_number') or entry['family']}: {entry['title']}"

        if target.exists():
            actual = sha256_file(target)
            if expected and actual != expected:
                mismatched += 1
                print(f"  MISMATCH {label}\n           expected {expected}\n           actual   {actual}")
            else:
                skipped += 1
                print(f"  have     {label}")
            continue

        if args.verify_only:
            missing += 1
            print(f"  missing  {label}")
            continue

        try:
            actual, size = download(entry["url"], target, args.timeout)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            failed += 1
            if target.exists():
                target.unlink()
            print(f"  FAILED   {label}\n           {exc}")
            continue

        if expected and actual != expected:
            mismatched += 1
            print(f"  MISMATCH {label}\n           expected {expected}\n           actual   {actual}")
        else:
            ok += 1
            print(f"  fetched  {label}  ({size / 1e6:.1f} MB, sha256 {'verified' if expected else 'recorded'})")

    print()
    print(f"{len(manuals)} document(s): {ok} fetched, {skipped} already present, "
          f"{missing} missing, {mismatched} mismatched, {failed} failed")
    if mismatched or failed:
        return 1
    if args.verify_only and missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
