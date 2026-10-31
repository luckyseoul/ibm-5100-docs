# Archives: where the scans live

The 5100 corpus survives mainly because of **bitsavers**, a volunteer archive that has
been scanning IBM General Systems Division manuals for decades. Knowing the directory
layout is most of the battle: the most important document about the System/370 question is not
filed under `5100/` at all.

---

## bitsavers — the primary mirror

Base: <https://bitsavers.org/pdf/ibm/>

| Directory | Contents | Files |
|---|---|---|
| [`5100/`](https://bitsavers.org/pdf/ibm/5100/) | the 5100 manual set: APL/BASIC introductions and references, MIM, MAPs, parts catalog, communications, serial I/O, shared-variable primer | 12 |
| [`5110/`](https://bitsavers.org/pdf/ibm/5110/) | 5110 and 5114: general information, APL/BASIC manuals, MIM, maintenance analysis, async comms, bibliography | 16 |
| [`5120/`](https://bitsavers.org/pdf/ibm/5120/) | 5120 maintenance and logic manuals | 2 |
| [`5103/`](https://bitsavers.org/pdf/ibm/5103/) | 5103 printer maintenance | 1 |
| [`apl/`](https://bitsavers.org/pdf/ibm/apl/) | **the 1977 Cubbon design paper**, APL\360 and APLSV language references, the APL shared-variables guide, "An APL Emulator" (1972), "Microcoding APL: The 370/135 APL Assist" | many |
| [`system3/`](https://bitsavers.org/pdf/ibm/system3/) | System/3 bibliography and reference summary, for the BASIC lineage question | many |

### The one that matters most

> <https://bitsavers.org/pdf/ibm/apl/5100_Portable_Computer_Design_Jan77.pdf>

Cubbon's 1977 symposium paper. If you read one document about the "370 ability", read this one.
It is 3 scanned pages (P51–P56 of the proceedings), image-only, and marked *IBM Internal Use
Only*.

## Internet Archive

bitsavers is mirrored into the Internet Archive as individual items, which gives a second path
when bitsavers is unavailable:

- Search: <https://archive.org/search?query=bitsavers+ibm+5100>
- Example items seen while compiling this dossier:
  `bitsavers_ibm5100SY39_14148603` (MIM), `bitsavers_ibm5100SA2erenceManualMay1976_12076027`
  (APL Reference, May 1976), `bitsavers_ibm5100SA2roductionDec1975_7126203` (APL
  Introduction), `bitsavers_ibm5100SA2IOAdapterFeatureUsersManualJan1977_5611868` (Serial
  I/O), `bitsavers_ibm5100160nceAnalysisProceduresMar1976_9827346` (MAPs).

The identifiers are generated and ugly; search, don't guess.

## IBM's own archive

- IBM Archives exhibit page for the 5100 (archived 25 December 2018):
  <https://web.archive.org/web/20181225172459/https://www.ibm.com/ibm/history/exhibits/pc/pc_2.html>
  Gives the announcement month, the twelve models, memory sizes, price range and language
  options.
- IBM Hursley Museum, *IBM Hardware Announcements to 1987* (PDF) — the withdrawal date of
  31 March 1982 comes from here. The museum's own site currently fails TLS negotiation, so use
  the Wayback capture:
  <https://web.archive.org/web/20241014115210/https://ibmhursleymuseum.info/docs/hardware_list_to_1987.pdf>

## Museum catalogues

- Computer History Museum collection catalog: <https://www.computerhistory.org/collections/catalog/>
  (search "IBM 5100"; the CHM also holds scanned IBM documents that are not on bitsavers).
- Smithsonian National Museum of American History holds the SCAMP prototype (si.edu blocks
  automated clients; Wayback copy):
  <https://web.archive.org/web/20240201185534/https://www.si.edu/object/nmah_334628>

## Downloading reliably

bitsavers runs a plain Apache directory listing and rejects some automated requests:

```bash
# works: GET with a normal user agent
curl -sS -A 'Mozilla/5.0 (X11; Linux x86_64)' \
  -O https://bitsavers.org/pdf/ibm/5100/SY31-0405-3_IBM_5100_Maintenance_Information_Manual_Oct1979.pdf

# may fail: HTTP HEAD without a user agent returns 403
```

This repository's `scripts/fetch_manuals.py` does exactly that, then verifies SHA-256 against
[data/manuals.yaml](../data/manuals.yaml). Please be a good citizen: one connection at a time,
no recursive mirroring, and don't re-host the scans.

## What is still missing

22 IBM publications are identified but not in the public corpus; the full table is at the end
of [manuals.md](manuals.md#known-ibm-publications-not-located). The 5100-specific six:

- `SA21-9264` — IBM 5100 Print Plot/APL User's Manual
- `SA21-9265` — IBM 5100 Print Plot/BASIC User's Manual
- `GX21-9214` — IBM 5100 APL Reference Card
- `GX21-9218` — IBM 5100 BASIC Reference Card
- `S131-0598` — IBM 5103 Printer Parts Catalog
- `S131-060x` — IBM 5106 Auxiliary Tape Unit Parts Catalog

If you own any of these, a scan donated to bitsavers is worth more than any code in this repo.

## Citing scans

Cite the IBM order number and edition first, the scan second:

> IBM Corporation, *IBM 5100 Maintenance Information Manual*, SY31-0405-3, Fourth Edition,
> October 1979, p. 4-20. Scan: bitsavers.org/pdf/ibm/5100/.

That survives link rot and lets a reader find the same page in a different scan.
