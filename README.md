# IBM 5100 — Documentation Dossier

A sourced, curated collection of the surviving public documentation for the **IBM 5100
Portable Computer** (1975) and the machines built on the same architecture — plus a
technical dossier on the question that refuses to die: **what could the 5100 actually do
with IBM System/370 code?**

This repo is an **index and a reading guide**, not a scan host. The manuals live at
bitsavers and the Internet Archive; every entry here links to them, records the IBM order
number, edition, date, byte size and (where fetched) a SHA-256 so a copy can be verified.

---

## The machine, in one screen

| | |
|---|---|
| **Announced** | 9 September 1975, IBM General Systems Division |
| **Withdrawn** | 31 March 1982 (per the IBM Hursley Museum hardware list) |
| **Price** | US$8,975 – US$19,975, twelve models |
| **CPU** | IBM **PALM** — a microcoded processor with a 16-bit data path |
| **Memory** | 16 / 32 / 48 / 64 KB read/write storage, plus ROM ("ROS") holding the interpreters and microcode |
| **Display** | 5-inch CRT, 16 lines × 64 characters |
| **Storage** | DC300 quarter-inch cartridge tape, 204 KB per cartridge |
| **Languages** | APL, BASIC, or both (front-panel toggle on dual-language models) |
| **Weight** | ~50 lb (≈25 kg) — "portable" in the luggable sense |
| **Successors** | IBM 5110 (1978), IBM 5120 (1980) |

The 5100 was the productised form of **SCAMP** (Special Computer APL Machine Portable),
built at IBM Los Gatos in 1973. Its trick was not new hardware but *microcode*: a small,
cheap machine that could run software written for far more expensive ones by emulating
the higher-level language implementation in firmware.

---

## The System/370 question — short answer

The 5100 genuinely runs a **System/370 APL implementation**, and IBM documented it. It does
**not** emulate a System/370 computer.

Three separate facts get collapsed into one myth:

1. **Language-level compatibility — real and documented.**
   The 5100's APL is IBM **APLSV**, the APL implementation used on System/370. Its reference
   manual contains *Appendix D: 5100 APL Compatibility with IBM APLSV*. The BASIC manual
   contains the same kind of appendix against **IBM 370/VS BASIC**.

2. **A microcoded 370-APL instruction interpreter — real and documented.**
   IBM's own 1977 account states that the language ROS holds intermediate-language
   instructions which "in the case of APL ... are System/370-like instructions", executed by
   an emulator written in PALM microcode — under 10 KB of ROS by IBM's own account, six
   months of work, error-free.

3. **"The 5100 emulates an IBM System/370 mainframe" — false.**
   There is no System/370 instruction set, no OS/VS, no JCL, no channel subsystem, no virtual
   storage, no multiprogramming. The machine is single-user, runs one language at a time, and
   its "emulator" is an interpreter for the APLSV intermediate language plus three interface
   routines (keyboard/display supervisor, command processor, I/O processor).

The "undocumented ability" framing comes from the **John Titor** internet hoax (2000–2001)
and was popularised by *Steins;Gate* as the "IBN 5100". The capability is obscure, not
undocumented: IBM described it in print in 1977 and the compatibility appendices shipped in
every APL and BASIC manual.

Full treatment with quotations and page references:
**[docs/system370/README.md](docs/system370/README.md)** ·
[evidence](docs/system370/evidence.md) ·
[the myth](docs/system370/myths.md) ·
[what it was not](docs/system370/what-it-was-not.md)

---

## What is in here

- **[docs/manuals.md](docs/manuals.md)** — the catalogue: 39 documents, with IBM order
  numbers, editions, dates, sizes and checksums. Generated from [data/manuals.yaml](data/manuals.yaml).
- **[docs/archives.md](docs/archives.md)** — where the scans actually live, and how to get
  them offline.
- **[docs/hardware/overview.md](docs/hardware/overview.md)** — models, memory, ROS cards,
  I/O devices, display, tape.
- **[docs/hardware/palm.md](docs/hardware/palm.md)** — the PALM processor, its instruction
  format, address spaces and interrupt model.
- **[docs/software/apl.md](docs/software/apl.md)** — APL 5100 as a dialect of APLSV.
- **[docs/software/basic.md](docs/software/basic.md)** — 5100 BASIC against 370/VS BASIC.
- **[docs/software/ros-and-tape.md](docs/software/ros-and-tape.md)** — how ROS banking,
  language selection and tape files work.
- **[docs/timeline.md](docs/timeline.md)** — 1972 to today.
- **[docs/guides.md](docs/guides.md)** — reading paths: learn APL, write PALM code, run an
  emulator, study the 370 question.
- **[docs/community.md](docs/community.md)** — emulators, talks, restoration threads,
  articles. Labelled by how well each is verified.
- **[docs/faq.md](docs/faq.md)** — short answers, including the myths.
- **[docs/sources.md](docs/sources.md)** — citation rules and confidence levels.

## Quick start

```bash
make manuals     # regenerate docs/manuals.md from data/manuals.yaml
make check       # link-check every URL in the manifest and link list
make fetch       # download the manual set into ./_archive (gitignored) and verify SHA-256
```

Requires Python 3.9+; no third-party packages.

## Coverage and honesty about gaps

**Included:** the complete IBM 5100 publication library as listed by IBM itself in the
Maintenance Information Manual (MIM, figure "IBM 5100 Computing System Publications"), the
5110 and 5120 families, the 5103 printer, the APLSV/APL-language references IBM cites as
related publications, System/3 references relevant to the BASIC lineage, and modern
emulation/community sources.

**Known missing from the manifest** (identified by IBM but not found digitised):

- `SA21-9264` — IBM 5100 Print Plot/APL User's Manual
- `SA21-9265` — IBM 5100 Print Plot/BASIC User's Manual
- `GX21-9214` — IBM 5100 APL Reference Card
- `GX21-9218` — IBM 5100 BASIC Reference Card
- `S131-0598` — IBM 5103 Printer Parts Catalog
- `S131-060x` — IBM 5106 Auxiliary Tape Unit Parts Catalog (number partially legible in the MIM)

If you have any of these, that is the single most useful contribution you can make.

**Not claimed:** that this list is exhaustive against IBM's internal publication register.
It is exhaustive against the sources that are publicly identifiable today, and it names the
holes rather than papering over them.

## Sourcing rules

1. **Primary beats secondary.** IBM manuals and IBM technical papers are quoted directly,
   with order number and page.
2. **Secondary sources are labelled.** Wikipedia, APL Wiki, Hackaday, forum posts: each is
   marked as secondary and none is used alone for a factual claim about hardware behaviour.
3. **Disagreements are recorded, not smoothed.** Where IBM's own documents conflict — the
   PALM acronym expansion, the BASIC lineage, the PALM chip count — the conflict is stated
   with both sources. See [docs/sources.md](docs/sources.md#known-conflicts).

## Copyright

IBM manuals are © International Business Machines Corporation. This repository **does not
redistribute scans**. It stores metadata and links; `make fetch` retrieves copies to a
gitignored local directory for personal research. Short quotations appear under fair use
with attribution. Prose here is CC BY-SA 4.0; scripts are MIT. See [LICENSE](LICENSE).
