# titor370 — the machine the 5100 was rumoured to be

This dossier documents what the IBM 5100 actually did with System/370 code: it ran **APLSV**,
IBM's 370 APL implementation, on a microcoded interpreter. It did not emulate a System/370
computer, and it could never translate machine code into anything.

The companion project builds the thing the John Titor story described, so the gap between the
story and the hardware can be measured rather than argued about:

> **<https://github.com/luckyseoul/titor370>**

## What it is

A System/370 interpreter, an assembler, a disassembler, and a static binary translator from
S/370 machine code to C — where the translator's output is *proved* to match the interpreter,
register for register and byte for byte.

```
S/370 machine code ──interpreter──► registers, CC, storage
                   ╲──translator──► C ──gcc──► the same registers, CC, storage
```

Seven example programs each run both ways and agree. Arithmetic is additionally checked against
Python's own arithmetic across every edge-case operand pair, and 200 randomly generated
programs are compared through both paths.

## Why it belongs next to this dossier

The Titor claim had two halves, and this dossier only settles one:

| Claim | Verdict | Where |
|---|---|---|
| The 5100 could "emulate IBM System/370 mainframes" | **False**, in the sense that matters: no System/370 *system*. It ran APLSV on a microcoded interpreter whose intermediate stream Cubbon calls "System/370-like" — a language implementation, not a machine. | [system370/README.md](system370/README.md) |
| The 5100 could "translate [370] machine code and more modern languages" | **Never existed.** But it is *buildable*, and now it has been built. | [titor370](https://github.com/luckyseoul/titor370) |

Putting the two side by side is the point. The real machine had 64 KB of address space, a 200 KB
tape cartridge, and one language at a time. The thing the story described needs a general-purpose
CPU, a megabyte-scale store, and a compiler — which is why it is a laptop program now and could
never have been a 1975 desktop.

## What the review changed

`titor370` has since been reviewed against **Hercules**, a mature System/370 emulator, by an
independent reviewer. The review found a dozen genuine misreadings of the Principles of
Operation — `MR`'s multiplicand, `DR`'s quotient/remainder order, `MVN`/`MVZ`, `SLR`'s
condition code, `TRT`'s registers, `SLA`'s sign handling among them. All were re-checked
against the manual and fixed, and the response is recorded in
[titor370's REVIEW.md](https://github.com/luckyseoul/titor370/blob/main/REVIEW.md).

That episode is worth recording here for a reason that is not about emulation: the tests and
the implementation were wrong *together*, so a passing test suite proved nothing until an
outside oracle disagreed. The same discipline applies to this dossier — a claim repeated in
two of my own documents is not thereby corroborated.

One claim in this dossier was corrected as a result. "No System/370 instruction ever executed"
was too strong: the 5100's microcode did interpret an intermediate stream that its designer
calls "System/370-like". The accurate statement, now used throughout, is that the machine did
not emulate a System/370 *system*.

## Provenance

`titor370`'s opcodes are transcribed from IBM GA22-7000-4, *System/370 Principles of Operation*,
September 1975 — contemporary with the 5100's announcement. That manual is the other half of the
primary-source chain this dossier is built on:

- The 5100 side: the manual set catalogued in [manuals.md](manuals.md), notably Cubbon's 1977
  design paper and the MIM.
- The 370 side: GA22-7000-4, catalogued in `titor370`'s
  [SOURCES.md](https://github.com/luckyseoul/titor370/blob/main/SOURCES.md) with the exact pages
  each semantic rule was read from.

Both are scanned by bitsavers and cited by printed page rather than redistributed.
