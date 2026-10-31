# Timeline

Dates in **bold** are documented in IBM publications or the IBM Archives. Other entries are
labelled with their source.

## Before the 5100

- **February 1969** — IBM announces the System/3, the small business computer whose BASIC
  dialect is sometimes claimed as the 5100's ancestor. *(IBM; see the lineage caveat in
  [software/basic.md](software/basic.md).)*
- **20 June 1972** — A. Hassitt and L. E. Lyon of the IBM Palo Alto Scientific Center date
  their paper *An APL Emulator*. Pre-5100 evidence that IBM was already thinking about APL
  implementations as things that could be emulated.
- **1973** — **SCAMP** (Special Computer APL Machine Portable) prototype built at IBM Los
  Gatos Scientific Center. It emulates an IBM 1130 to run APL\1130. *(Wikipedia, citing
  Friedl's 1983 PC Magazine account; the Smithsonian holds the prototype.)*

## Design and build

- **Late June 1974** — the GSD-Rochester team begins "the formal task of writing an emulator
  and the necessary higher-level code to interface the 370 APL interpreter with the 5100
  keyboard, display, tape and printer." *(Cubbon 1977, p. 54.)*
- **First half of 1974** — after rejecting two 1130 APL implementations, the team adopts APLSV,
  "the last change made in the design plan". Cubbon gives no month for this decision. *(Cubbon
  1977, pp. 52–53.)*
- **December 1974** — the APL system is running, after about six months and "three people's
  effort". Final testing and ROM manufacture take under a year. *(Cubbon 1977, p. 54.)*

## Product

- **9 September 1975** — IBM General Systems Division announces the 5100 Portable Computer;
  *The New York Times* reports it on 10 September as a "50-Pound Computer".
- **December 1975** — *BYTE* runs "Welcome, IBM, to personal computing"; the APL and BASIC
  *Introductions* are published (SA21-9212-1, SA21-9216-1).
- **April 1976** — 5100 "made available worldwide". The *Shared Variable Primer* (07.607) is
  published.
- **May 1976** — *IBM 5100 APL Reference Manual*, third edition (SA21-9213-2), including
  Appendix D against APLSV.
- **June 1976** — D. A. Roberson, "A microprocessor-based portable computer: The IBM 5100",
  *Proceedings of the IEEE* 64(6):994–999.
- **January 1977** — A. J. Cubbon presents "The IBM 5100 Portable Computer Design" at the APL
  ITL Symposium, Endicott, NY — the clearest account of the APLSV decision and the emulator.
- **July 1977** — *IBM 5100 BASIC Reference Manual*, fourth edition (SA21-9217-3), with the
  370/VS BASIC appendix.

## Family

- **January 1978** — IBM 5110 announced (diskette, lowercase, larger workspace).
- **October 1979** — *IBM 5100 Maintenance Information Manual*, fourth edition (SY31-0405-3) —
  the edition everyone cites for the hardware.
- **February 1980** — IBM 5120 announced.
- **September 1980** — *IBM 5110/5120 Computing Systems Bibliography* (GH30-0232-1).
- **31 March 1982** — the 5100 is withdrawn. *(IBM Hursley Museum hardware list, via
  Wikipedia.)*

## Afterlife

- **October 1983** — IBM announces the **XT/370**: a PC XT with three cards that execute
  S/370 instructions locally under VM/PC. This, not the 5100, is IBM's real desktop
  System/370 emulator. Discontinued April 1987.
- **1998–2001** — the **John Titor** persona posts on the Time Travel Institute forums and the
  Art Bell BBS, claiming the 5100 has an "undocumented ability to emulate IBM System/370
  mainframes". The first version of the story names the **5110** instead.
- **2009** — *Steins;Gate* visual novel uses the machine as the **"IBN 5100"**; the 2011 anime
  adaptation spreads the reference further.
- **2019–present** — MAME's `ibm5100` driver (Patrick Mackinlay, BSD-3-Clause) emulates the
  5100 and 5110 with a PALM CPU core and a disassembler; the character-generator ROM remains a
  reconstruction marked `BAD_DUMP`.
- **31 October 2026** — this dossier compiled.

## What the timeline does not show

There is no date on which the "370 emulator" was added as a secret feature, because it was not
one. It was a design decision taken in 1974, described at a symposium in 1977, and reflected in
customer manuals from 1975 onward.
