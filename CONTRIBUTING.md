# Contributing

The value of this repository is that every claim can be checked. Contributions are judged on
that basis, not on volume.

## The two ways to help

### 1. Fill a gap

The highest-value contribution is a scan of a document IBM itself lists but that is not in any
public archive. See the "Known IBM publications not located" table at the bottom of
[docs/manuals.md](docs/manuals.md).

If you have one:

1. Scan at 300–400 dpi, bitonal or grayscale, one page per image, no OCR required (OCR can be
   layered later, but never destructive).
2. Donate it to bitsavers (or the Internet Archive) so it has a permanent home — do not send it
   to this repository.
3. Add the entry to `data/manuals.yaml` with the new URL, order number, edition, date, byte
   count and SHA-256.

### 2. Correct or extend the dossier

Good corrections look like:

- "The MIM says X on page 4-19; the dossier says Y" — with the quotation.
- "This claim is sourced only to Wikipedia, here is the IBM document that settles it."
- "These two sources conflict; here is a third that explains why."

Bad corrections look like: a claim with no source, a link with no page reference, or a rewrite
that deletes an inconvenient conflicting source.

## Rules

1. **Primary sources win.** IBM manuals, IBM technical papers, IBM Archives. Secondary sources
   are allowed but must be labelled as such.
2. **Page numbers.** Cite the printed page (`4-19`, `C-1`, `p. 206`), not the PDF page index.
3. **Record conflicts.** If two sources disagree, add the disagreement to
   [docs/sources.md](docs/sources.md#known-conflicts) rather than choosing silently.
4. **No scans in the tree.** Link and checksum; do not commit PDFs.
5. **Label confidence.** If a statement rests on a forum post or a search snippet, say so.
6. **Do not launder the myth.** "Emulates a System/370" is not a shorthand for "runs APLSV";
   use the precise phrasing even when it is longer.

## Editing the manifest

`data/manuals.yaml` is the single source of truth for the catalogue. `docs/manuals.md` is
generated:

```bash
make manuals
```

Required fields per entry: `id`, `family`, `part_number` (or `null`), `title`, `date` (`YYYY-MM`),
`doc_type`, `publisher`, `url`, `filename`. Optional: `edition`, `bytes`, `sha256`,
`server_mtime`, `server_size`, `notes`.

Accepted `family` values: `ibm-5100`, `ibm-5110`, `ibm-5120`, `ibm-5103`, `supporting`.

Accepted `doc_type` values: `reference`, `introduction`, `user-guide`, `maintenance`,
`parts-catalog`, `communications`, `feature-manual`, `general-information`, `bibliography`,
`logic-manual`, `technical-report`, `conference-paper`.

## Checks before opening a PR

```bash
make manuals   # regenerate the catalogue
make check     # link-check manuals + links
make fetch     # optional: verify SHA-256 against a local archive
```

`make check` must pass, with the exception of links marked `known_blocked: true` in
`data/links.yaml` (Cloudflare-protected sites).

## Style

- Prose: plain, specific, no marketing adjectives.
- One idea per paragraph; short paragraphs win.
- Tables only where columns are short.
- Use the IBM order number the first time a manual is mentioned.
