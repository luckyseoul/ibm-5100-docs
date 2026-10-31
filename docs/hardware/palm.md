# PALM — the processor

"PALM" is the name used in the literature for the 5100's processor. IBM's own 5100
maintenance manual never uses the word: it calls the thing **the controller** or **the
microprocessor**. That single fact explains a lot of the confusion around the machine.

---

## The name

Two expansions circulate:

- **"Program All Logic in Microcode"** — the expansion given by Wikipedia, citing D. A.
  Roberson's 1976 *Proceedings of the IEEE* paper on the 5100.
- **"Put All Logic in Microcode"** — the expansion used widely in hobbyist writing and in
  MAME's PALM device source header.

Neither expansion appears in the 5100 MIM's extracted text. Treat the acronym's expansion as
unsettled and cite whichever source you use. See [../sources.md](../sources.md#known-conflicts).

## What it physically is

Two descriptions disagree, and the disagreement is unresolved:

| Source | Description |
|---|---|
| Cubbon 1977, p. 55 | "a fast two-chip 8-bit processor" with 49 16-bit microinstructions |
| Wikipedia (citing *PC Magazine*, 1983) | a circuit **board**: 13 bipolar gate arrays in square metal cans, 3 TTL ICs in DIPs, 1 round metal can part |

Possible readings: different build revisions, a two-chip ALU/control pair *within* the
13-array board, or loose language in one source. The 5100 MIM's card-level drawings and the
parts catalog are the place to settle it; until someone does, both descriptions are recorded
here.

## Architecture

| Property | Value | Source |
|---|---|---|
| Data path | 16-bit plus 2 parity bits | Cubbon 1977 p. 55; Wikipedia |
| Microinstruction width | 16 bits (halfword) | MIM Appendix C |
| Opcode | top 4 bits; remaining 12 bits operand | MIM Appendix C |
| Modifier | bits 12–15 extend the opcode beyond 16 | MIM Appendix C |
| Instruction count | 49 microinstructions | Cubbon 1977 p. 55 |
| Registers | four banks of sixteen 16-bit registers, one bank per interrupt level | Cubbon 1977 p. 55; MAME `m_r[4][16]` |
| Interrupt levels | 4, prioritised keyboard > tape/printer > comms/serial > normal | Cubbon 1977 p. 55 |
| Address space | 64 KB direct, bank-switched beyond | Wikipedia; MIM |
| Address spaces (MAME model) | program (16-bit), read/write (16-bit), I/O control (8-bit/4-bit), I/O data (8-bit/4-bit) | MAME `palm.h` |
| Clock (MAME) | 15,091,200 Hz machine clock | MAME `ibm5100.cpp` |
| Cycles per instruction (MAME) | 17–54 | MAME `palm.h` |

The commonly quoted "1.9 MHz" for the 5100 is best treated as an *effective* instruction rate
rather than a master clock. With a 15.0912 MHz machine clock and multi-cycle instructions
(17–54 in MAME), an effective rate in that region is consistent, but the manuals do not state
a headline MHz figure. This is an inference, not a documented number.

## Instruction set

MIM Appendix C classifies the microinstructions by function:

- I/O control
- fetch and store
- register
- arithmetic register
- logical register
- jump

Each is a 2-byte halfword with a 4-bit opcode; some opcodes take a modifier in bits 12–15,
which is how the design gets more than 16 operations out of a 4-bit field. Cubbon counts 49
16-bit microinstructions. Secondary sources describe "about 45 opcodes" documented in the MIM
appendix — consistent, since modifiers create variants of base opcodes.

## How it runs a language

The execution model, from MIM §4 and Cubbon 1977:

```
power on
  └─ power-on reset activates executable ROS
       └─ bring-up diagnostic at the address in location 0000
            └─ IPL routine
                 └─ I/O supervisor + language emulator microprograms
                      └─ language ROS (APL or BASIC interpreter) mapped in on demand
                           └─ interpreter emits intermediate instructions
                                └─ emulator interprets them on PALM
```

Two consequences worth internalising:

1. **The processor does not execute APL or BASIC.** It executes PALM microinstructions that
   implement an emulator; the emulator executes the language's intermediate code.
2. **The language interpreter is not "firmware" in the modern sense.** It is a separate ROS
   address space, banked in like a peripheral, and the emulator treats it "as if it was a
   direct access storage device rather than like memory" (Cubbon, p. 54).

## Diagnostic Control Program and maintenance mode

Executable ROS contains the **DCP** (Diagnostic Control Program) alongside the emulators and
I/O microprograms (MIM §4). Via a keyboard sequence documented in the MIM, the machine can be
put into a maintenance mode that exposes RAM, video memory, CPU registers, interrupt vectors
and the clock counter as hexadecimal, and permits entering PALM code directly. This is how
hobbyists have run hand-assembled PALM programs on real hardware.

## Where to read more

- **MIM Appendix C** — instruction formats and opcode classes.
- **MIM §4** — microprogramming, ROS, interrupts, I/O.
- **Cubbon 1977, pp. 53–55** — design rationale and processor description.
- **MAME `src/devices/cpu/palm/`** — a working, BSD-licensed implementation with a
  disassembler; the most practical way to study the instruction set today.
- Community reverse-engineering: see [../community.md](../community.md).
