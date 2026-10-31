# APL on the 5100

APL was the reason the 5100 existed. The prototype, SCAMP, was built to put APL on a desk; the
product kept APL as its flagship language, and the choice of *which* APL is the root of the
whole System/370 story.

---

## Which APL it is

The 5100's APL is **APLSV** — IBM's APL implementation for System/370 — re-hosted on PALM with
a microcoded interpreter and new I/O. IBM states the comparison directly in the customer
manual:

> **Appendix D. 5100 APL Compatibility with IBM APLSV**
>
> "The 5100 APL system differs from the IBM APLSV system primarily because the 5100 is a single
> user system with different input/output devices and it has display screen output rather than
> typewriter output."
>
> — SA21-9213-2, p. 206

Appendix D is a *difference list*, which is the useful part: it tells you exactly where the
desktop machine departs from the mainframe implementation.

### Documented differences from APLSV

- **Single user.** Power-on signs you on; no sign-on or ID number.
- **Workspace** generally smaller than APLSV's, further reduced by the shared-variable
  processor's I/O buffers and work areas.
- **125 symbols by default** instead of 256.
- **Library numbers become device/file numbers**: a 1–5 digit number selecting device and file
  for `)SAVE` / `)LOAD`; fewer than four digits means file on device 1.
- `)LOAD`, `)COPY`, `)PCOPY` require library and workspace ID; `)DROP` requires the library
  number (plus workspace ID for stored workspaces).
- **Unsupported because multi-terminal/remote**: `)OFF`, `)OFF HOLD`, `)CONTINUE HOLD`,
  `)PORTS`, `)MSGN`, `)MSG`, `)OPRN`, `)OPR`, and all special system-operator commands.
- **Unsupported because the function is absent**: `)GROUP`, `)GRPS`, `)GRP`.
- **Unsupported, replaced by system variables**: `)ORIGIN`, `)WIDTH`, `)DIGITS` → `⎕IO`,
  `⎕PW`, `⎕PP`.
- **Added for the 5100's devices**: `)MARK` (format tape files), `)OUTSEL` (select printed
  transactions), `)REWIND`, `)MODE` (communications mode), `)PATCH` (load an IMF or Tape
  Recovery program from IBM tape).
- **Changed**: `)CONTINUE` saves workspaces with suspended functions; such a workspace cannot
  be `)COPY`ed or `)LOAD`ed into a 5100 with a smaller workspace.
- **New errors**: `LINE TOO LONG` (statements over 115 characters) and `WS TOO BIG`.

The absence of `RESEND` is noted because the 5100 "is not in a communications environment".

## Numeric behaviour

From the APL Reference Manual:

- range: **−7.237005577332262E75 to 7.237005577332262E75**
- smallest magnitude: **±5.397604346934028E−79**
- internal precision: **16 significant digits**

Cubbon's rationale for choosing APLSV over the 1130 implementations lists "15 digits of
numerical precision vs six in the 1130 versions" — a design-stage comparison, not a
contradiction of the shipped manual's internal precision figure.

## Shared variables

The 5100 supports APL shared variables, and IBM published a dedicated primer:

> Andrew J. Cubbon, **IBM 5100 Shared Variable Primer**, Technical Report 07.607, General
> Systems Division, Rochester, Minnesota, April 1976.

The primer is written as a supplement to Chapter 8 of SA21-9213 and starts from simple
exercises. It is the practical entry point for the 5100's shared-variable I/O model — which is
also how APL code reaches the tape, printer and (with the communications features) the outside
world. The 5110's manual later notes that its added system variables (`⎕AI`, `⎕DL`, `⎕TS`,
`⎕TT`, `⎕UL`) were introduced "to maintain syntactic compatibility between the 5110 and APLSV".

## What APL on a 5100 feels like

- 5-inch screen, 16 lines of 64 characters, with the option to view half a line at a time.
- The APL character set on a physical keyboard with APL legends; overstruck characters are
  part of the character-constant syntax.
- Workspaces saved to data cartridge rather than to a library on DASD.
- Printing via the 5103, or plotting via the Print Plot/APL feature (`SA21-9264`, not yet
  located — see the README's gap list).

## Reading path

1. **SA21-9212-1**, *IBM 5100 APL Introduction* (December 1975) — tutorial, assumes no APL.
2. **SA21-9213-2**, *IBM 5100 APL Reference Manual* (May 1976) — the reference; Appendix D is
   the APLSV comparison.
3. **07.607**, *Shared Variable Primer* (April 1976) — shared variables and device I/O.
4. **GC26-3847**, *APL Language* — the System/370 language reference IBM cites as related.
5. **SH20-1460-1**, *APL Shared Variables User's Guide* — the APLSV side of the same feature.

For the implementation story — why APLSV, how the emulator was written — read
[../system370/evidence.md](../system370/evidence.md).
