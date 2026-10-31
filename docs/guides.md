# Reading paths

Five audiences, five routes through the material. Each path lists only what you actually need,
in order.

---

## 1. "I want to understand the machine"

1. [hardware/overview.md](hardware/overview.md) — this repo's summary.
2. **MIM SY31-0405-3**, section 4, "Internal Operation of the 5100" — microprogramming, ROS,
   interrupts, I/O. The single most valuable chapter in the whole corpus.
3. **Cubbon 1977**, pp. 51–56 — why it was built this way, in the designer's words.
4. **MIM Appendix C** — instruction formats and opcode classes.
5. **Parts Catalog S131-0599-3** — if you care about cards, FRUs and what plugged where.

Skip for now: the MAPs (`1608314`), which are field-service flowcharts.

## 2. "I want to learn APL as it existed on the 5100"

1. **SA21-9212-1**, *APL Introduction* — a teaching text, not a reference. Work through it.
2. **SA21-9213-2**, *APL Reference Manual* — keep open for system commands and system variables.
3. **07.607**, *Shared Variable Primer* — the 5100-specific half: tape, printer, device I/O.
4. **GC26-3847**, *APL Language* — the System/370 language definition IBM points to.

Caveats: 125 symbols by default, `⎕IO`/`⎕PW`/`⎕PP` instead of `)ORIGIN`/`)WIDTH`/`)DIGITS`,
no `)OFF`/`)PORTS`/`)MSG*`, and a workspace small enough that `WS TOO BIG` is a normal error.

## 3. "I want to run one"

MAME is the maintained public emulator verified for this dossier. Its driver covers the
**5100 and 5110** (not the 5120), with a PALM CPU core and disassembler.

What you need:

- A MAME build containing `src/mame/ibm/ibm5100.cpp` and `src/devices/cpu/palm/`.
- ROM images named exactly as the driver expects, in `roms/ibm5100/`:

  | File | Region | Notes |
  |---|---|---|
  | `h2.ros` | executable ROS | BASIC emulator half |
  | `h4.ros` | executable ROS | APL emulator half |
  | `c4.ros` | BASIC ROS | |
  | `e2.ros` | common ROS | physically on E2, selected with BASIC |
  | `c2.ros`, `d2.ros`, `d4.ros` | APL ROS | |
  | `j2.ros` | character generator | **MAME's copy is a reconstruction, `BAD_DUMP`** |

- Check what MAME wants and what it found:

  ```bash
  mame -listroms ibm5100
  mame ibm5100 -verifyroms
  mame ibm5100
  ```

  *(Commands not executed while compiling this dossier — MAME was not installed on the
  machine used. The ROM names and hashes are taken from the driver source.)*

- Expect the machine to boot to APL or BASIC depending on the language switch, with the
  front-panel toggles exposed as MAME inputs. The driver's own TODO list is the honest
  statement of what is missing: display registers, device address F, **tape controller, disk
  controller, printer, communications cards, expansion feature, feature ROS (K4)**.

So: CPU, ROS banking, keyboard, display and the language emulators are emulated; the tape and
printer paths are not. You can run the machine, not yet round-trip a workspace cartridge.

## 4. "I want to write PALM machine code"

1. **MIM Appendix C** — the instruction formats and opcode classes.
2. **MIM section 4** — the memory map, device addresses, interrupt levels, and how ROS is
   banked. You need this before any non-trivial program.
3. **MIM maintenance mode** — the keyboard sequence that exposes registers and memory and lets
   you key in PALM code on real hardware.
4. **MAME's PALM core and disassembler** — `src/devices/cpu/palm/palm.cpp`, `palmd.cpp`. The
   practical development loop: assemble, run under MAME, inspect with the debugger.
5. Community work: Steve Lewis's talk on PALM internals, the voidstar thread on using the DCP
   and a modern assembler, and the VCF forum thread on a PALM side-scroller. See
   [community.md](community.md).

No IBM PALM assembler is known to this repository in the public corpus; the community
tooling is reverse-engineered.

## 5. "I want to settle the System/370 question myself"

Read in this order, and stop when you are convinced:

1. **Cubbon 1977, p. 52** — the decision to use the System/370 APL (APLSV).
2. **Cubbon 1977, pp. 53–54** — the emulator, its size, and the "System/370-like
   instructions" sentence.
3. **Cubbon 1977, p. 54** — the three interface routines and the "only differences" claim.
4. **SA21-9213-2 Appendix D, p. 206** — the shipped compatibility statement.
5. **MIM §4, pp. 4-12 and 4-20** — what "emulator" means to IBM.
6. **[system370/what-it-was-not.md](system370/what-it-was-not.md)** — the XT/370 contrast, for
   what a real desktop 370 emulator looks like.

If after that someone still tells you the 5100 "emulates a 370", ask them which 370
instruction is executed by which piece of hardware. There is no answer, and that is the point.

---

## How to read an IBM manual of this era

- **Order number**, not title, is the identity. `SA21-9213-2` is the third edition of the APL
  reference; `SA21-9213-0` is the first, and both are in the archive.
- **Editions and TNLs**: manuals were revised by Technical Newsletters (TNLs) and re-issued.
  The `-N` suffix is the edition. A later edition obsoletes earlier ones but earlier ones
  sometimes document removed features.
- **Page numbers restart per section**: `4-12` means section 4, page 12. Appendix pages are
  `C-1`, `D-1`.
- **Figures carry the value**: the publications library, the ROS card layout and the device
  address table are figures, not prose. OCR drops them; look at the page images.
