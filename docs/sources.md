# Sources, confidence, and known conflicts

## Confidence levels

Every factual claim in this repo should be traceable to one of these tiers:

| Tier | Meaning | Examples |
|---|---|---|
| **A — primary, read** | IBM publication fetched and read, page cited | MIM SY31-0405-3; SA21-9213-2; Cubbon 1977 |
| **B — primary, metadata only** | IBM publication's existence and identity verified, contents not read | some 5110/5120 manuals |
| **C — secondary, read** | Fetched and read; not IBM | Wikipedia articles, MAME source |
| **D — secondary, unverified** | Search-result summary only, or site blocked | APL Wiki; YouTube talks; forum threads |
| **E — inference** | This repo's reasoning from A–D, labelled as such | e.g. the effective-clock discussion |

If a page states something without an obvious tier, treat it as E and check.

## Citation style

> IBM Corporation, *IBM 5100 APL Reference Manual*, SA21-9213-2, Third Edition, May 1976,
> Appendix D, p. 206.

Order number + edition + printed page. PDF page indices differ from printed pages and are not
used.

## Known conflicts

These are places where the sources genuinely disagree. They are recorded, not resolved.

### 1. What "PALM" stands for

- **"Program All Logic in Microcode"** — Wikipedia's *IBM PALM processor* article, citing
  D. A. Roberson, "A microprocessor-based portable computer: The IBM 5100", *Proceedings of the
  IEEE* 64(6), June 1976.
- **"Put All Logic in Microcode"** — common in hobbyist writing and in the header comment of
  MAME's PALM device source.

Neither expansion appears in the 5100 MIM's extracted text, and neither does the word
"microprocessor": the MIM says only "the controller". "Microprocessor" is Cubbon's usage.

### 2. What PALM physically is

- **A two-chip 8-bit processor with a 16-bit data path** — Cubbon 1977, p. 55 ("The
  microprocessor is a fast two-chip 8-bit processor").
- **A board of 13 bipolar gate arrays, 3 TTL DIPs and one round metal can** — Wikipedia,
  citing *PC Magazine*, November 1983.

Possibly different build stages, different family members (5110/5120), or imprecise language in
one source. Unresolved. The parts catalog and MIM card drawings would settle it.

### 3. System/360 vs System/370

- **System/370** — Cubbon 1977, p. 52: "the version used on the IBM System/370, known as
  APLSV".
- **System/360** — Wikipedia's *PALM* article and APL Wiki both say System/360 APL (APL.SV).

APLSV existed across the System/360–System/370 transition; the 5100 manuals compare against
"IBM APLSV" without naming a machine model. The strongest single statement is Cubbon's, because
he was describing the decision he took. Treat "System/360" as a secondary simplification.

### 4. The BASIC lineage

- **System/3** — Wikipedia: the 5100 used "the BASIC interpreter used on IBM's System/3", and
  the microcode emulates "most of the functionality of both a System/370 and a System/3".
- **370/VS BASIC** — IBM's own BASIC Reference Manual defines the dialect against **IBM 370/VS
  BASIC** (p. 143).

No primary source found for the System/3 claim. See [software/basic.md](software/basic.md).

### 5. APL numeric precision

- **16 significant digits** — SA21-9213-2, "Numeric Value Precision".
- **15 digits** — Cubbon 1977, p. 53, describing APLSV's advantage over the 1130 versions.

Likely different measurements (internal representation vs advertised decimal precision), but
recorded as a discrepancy.

### 6. Weight

- **~50 lb** — IBM Archives.
- **~55 lb (25 kg)** — Wikipedia, which notes measured weight was closer to 55 lb.

### 7. Announcement date

- **9 September 1975** — Wikipedia, citing the 10 September 1975 *New York Times* report of
  "yesterday's" announcement.
- The IBM Archives page says only "September 1975".

The 9 September date is a reasonable reading; the archival statement is the safer citation.

### 8. Tape capacity

- **200 KB** — MIM p. 4-30: "stores 200K bytes of formatted data".
- **204 KB** — MIM p. 3-91: "All tapes have 204K bytes storage capacity".

Both are IBM, in the same manual. Probably formatted capacity vs raw capacity, but the manual
never says which, so this dossier quotes both rather than picking one.

### 9. The "DC300" name

`DC300` appears in no source in this corpus — not the MIM, the MAPs, the parts catalog, or
Cubbon's paper — although it is the name used in most secondary writing and in the emulation
community. IBM's own term is "IBM data cartridge", 300 ft of ¼-inch tape in a keyed shell. The
identification is very probably right; it is nonetheless secondary, and is labelled as such.

## Verification log

Compiled 31 October 2026.

**Fetched with HTTP 200 and read:**

- bitsavers index pages for `5100`, `5110`, `5120`, `5103`, `apl`, `system3`
- All 12 IBM 5100 manuals listed in the manifest (SHA-256 recorded for 25 of 39 entries)
- `SA21-9213-2` Appendix D; `SA21-9217-3` p. 143; `SA21-9311`/5110 appendices; MIM §4 and
  Appendix C
- Cubbon 1977, all three pages, rendered as images and read
- `An_APL_Emulator` title page (Hassitt & Lyon, IBM Palo Alto Scientific Center, 20 June 1972)
- MAME `ibm5100.cpp`, `palm.cpp`, `palm.h` (master branch)
- Wikipedia raw wikitext: *IBM 5100*, *IBM PALM processor*, *John Titor*,
  *PC-based IBM mainframe-compatible systems* (XT/370 section)
- IBM Archives 5100 page via the Wayback Machine
- Crossref record for DOI `10.1109/PROC.1976.10253`

**Blocked or partial (tier D):**

- APL Wiki `APL_5100` — Cloudflare challenge (HTTP 403)
- Retrocomputing Stack Exchange question 7005 — Cloudflare challenge (HTTP 403)
- voidstar blog — page renders via JavaScript; only the summary was retrievable
- retrocomputingforum thread — only the link preview was retrievable
- YouTube talk — not transcribed

**Not verified here:**

- The IBM Hursley Museum PDF (withdrawal date) was not fetched; the date is taken from
  Wikipedia's citation of it.
- The *Telegraph* 2015 article on Titor was not fetched; the quotation is from Wikipedia's
  summary of it.
- Physical hardware behaviour (tape, printer, display timing) is documented, not tested on a
  real machine.

## Rules for contributors

1. Do not add a claim that rests only on a tier-D source without marking it.
2. Do not "fix" a conflict by deleting the losing source; add it to this page.
3. Every new manual entry needs: order number (if any), edition, date, URL, and a SHA-256 once
   fetched.
4. Never commit scans. Link, checksum, and let the archive serve the bytes.
