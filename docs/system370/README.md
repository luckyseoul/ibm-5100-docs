# The System/370 question

> Did the IBM 5100 have a hidden ability to emulate an IBM System/370 mainframe?

**It had a documented ability to run the System/370 APL implementation, APLSV, on a
microcoded emulator. It did not emulate a System/370 computer.**

Everything else — "undocumented", "translate 370 machine code", "debug legacy mainframe
programs" — is either a distortion of that fact or comes from the John Titor hoax.

This directory separates the four claims that usually arrive bundled together.

---

## 1. What IBM says the machine does

From the **IBM 5100 Maintenance Information Manual** (SY31-0405-3, October 1979), section 4,
"Internal Operation of the 5100":

> "Because the 5100 controller cannot process an APL or BASIC user program directly, it must
> emulate the APL or BASIC program to the internal machine microcode by means of the APL (H4)
> or BASIC (H2) emulators on the executable ROS card."

> "Because the 5100 cannot operate directly from a user language, the system emulates or
> appears to have the attributes of the user's language, while each instruction is translated
> into language that the system can use."

*(MIM, p. 4-12. Full quotations in [evidence.md](evidence.md).)*

Note what "emulator" means here. It is IBM's word for **the microprogram that interprets the
language implementation** — not for a hardware-level System/370 simulator. APL and BASIC are
the two things being emulated.

## 2. Where the 370 enters — and how far it goes

IBM's 1977 account of the 5100's design, by A. J. Cubbon (GSD-Rochester), is the decisive
document. It records the design decision:

> "The last change made in the design plan was to go from the two 1130 implementations of APL
> already examined to the version used on the IBM System/370, known as APLSV."

*(Cubbon, "The IBM 5100 Portable Computer Design", APL ITL Symposium, January 1977, p. 52.)*

And then the implementation:

> "In late June 1974, the development team undertook the formal task of writing an emulator
> and the necessary higher-level code to interface the 370 APL interpreter with the 5100
> keyboard, display, tape and printer. To date, the finished emulator has remained error free
> and uses less than 10K of ROM."

> "The newest ROM is the dense, 48K bits per chip storage used for the APL and BASIC
> interpreters. This storage contains the intermediate language instructions. In the case of
> APL, these are **System/370-like instructions**. This storage is accessed by the emulators
> for each intermediate language…"

*(Cubbon, pp. 53–54.)*

So the concrete architecture is:

```
APLSV — the System/370 APL implementation
        │  implemented as
        ▼
intermediate-language instructions — in the case of APL, "System/370-like"  (language ROS)
        │  interpreted by
        ▼
PALM microcode emulator  (< 10 KB ROS)
        │  plus three interface routines
        ▼
5100 keyboard · 5" CRT · data cartridge · 5103 printer
```

The three interface routines, per Cubbon (p. 54):

1. **Supervisor** — makes the keyboard and display behave like a terminal; also allows the
   printer to serve as a hard copy of the display.
2. **Command processor** — supports the APL library commands, e.g. `)SAVE` and `)LOAD` to
   the tape cartridge.
3. **I/O processor** — lets the APL programmer use tape and printer as independent devices
   under program control.

And the boundary of the claim, stated by IBM:

> "The only differences between the 5100 version of APL and the APL on the System/370 were
> the portions dependent on the input/output devices, display vs typewriter, and tape vs
> direct access devices."

*(Cubbon, p. 54.)*

That is the whole of the "System/370 ability": **the same APL implementation, re-targeted to
a desktop's I/O, with a microcoded interpreter standing in for the mainframe.**

## 3. Language-level compatibility, in IBM's shipping manuals

The same two appendices appear in the customer documentation for each family:

| Manual | Appendix | Subject |
|---|---|---|
| IBM 5100 APL Reference Manual, SA21-9213-2 | Appendix D, p. 206 | "5100 APL Compatibility with IBM APLSV" |
| IBM 5100 BASIC Reference Manual, SA21-9217-3 | p. 143 | "5100 BASIC Compatibility With IBM 370/VS BASIC" |
| IBM 5110 APL Reference Manual, SA21-9303-0 | Appendix E, p. 229 | "5110 APL Compatibility with IBM APLSV" |
| IBM 5110 BASIC Reference Manual, SA21-9308-2 | p. 201 | "5110 BASIC Compatibility with IBM 370/VS BASIC" |

These appendices are *difference lists*, in the ordinary vendor sense: "here is how our
implementation differs from the mainframe one." They are the strongest evidence that
compatibility with the System/370 **language implementations** was a designed, advertised
property — and also the strongest evidence that the 5100 was not the mainframe: the
differences are all about being a single-user machine with a screen and a tape drive.

### Other 370 touchpoints (none of which are emulation)

- **Components.** "The read/write memory is used in IBM System/370 and System/32" (Cubbon 1977,
  p. 53) — a parts-bin lineage, not an architectural one.
- **Terminal emulation.** The Communications Adapter makes the 5100 appear as an IBM 2741
  terminal to a remote system (SA21-9215-0).
- **Follow-on communications.** The 5110's Binary Synchronous Communications and 2770 data link
  control let it talk to a System/370 "equipped with the appropriate subfeatures"
  (GA21-9300-0).
- **Language references.** The 5100 manuals cite *APL Language* (GC26-3847) and *APL Shared
  Variables User's Guide* (SH20-1460-1), both System/370 documents.

Four different senses of "370" — language, components, terminal, communications — and none of
them is "the 5100 is a 370". Keeping them apart is most of the argument.

## 4. What the 5100 cannot do

No System/370 instruction set is executed at the hardware level; there is no 370 memory
model, no channel subsystem, no supervisor state, no virtual storage, no OS/VS, no JCL, no
job entry, no multiprogramming, no 3270 data stream, no card reader, no disk. The 5100 has
one user, one language at a time, 64 KB of address space, and a tape drive.

See [what-it-was-not.md](what-it-was-not.md) for the itemised list and for the contrast with
IBM's *actual* System/370-in-a-PC product, the 1983 XT/370.

## 5. Why the myth is sticky

Because the true version is strange enough. A 1975 desktop machine really does contain a
microcoded interpreter for the intermediate code of a System/370 APL implementation. If you
phrase that as "the 5100 can emulate a System/370", it is wrong but not *absurdly* wrong —
and that is exactly the sort of half-truth that a time-travel story can build on.

The John Titor posts (2000–2001) claimed:

> "the IBM 5100 had an undocumented ability to emulate IBM System/370 mainframes and
> translate between their machine code and more modern languages"

That sentence contains three errors: **undocumented** (IBM documented it in 1977 and shipped
compatibility appendices), **mainframes** (an APL implementation, not the machine), and
**translate machine code** (there is no 370 machine-code translator; the emulator interprets
APL intermediate code and re-targets I/O).

See [myths.md](myths.md) for the full provenance, including the detail that the same persona
first named the **5110**, not the 5100, and switched after the fact.

---

## Verdict table

| Claim | Verdict | Basis |
|---|---|---|
| The 5100 runs the System/370 APL implementation (APLSV) | **True** | Cubbon 1977; SA21-9213-2 App. D |
| The 5100's APL is source-compatible with APLSV, with listed exceptions | **True** | SA21-9213-2 App. D, pp. 206 ff. |
| The 5100's BASIC is compatible with IBM 370/VS BASIC, with listed exceptions | **True** | SA21-9217-3, p. 143 |
| APLSV was executed via a microcoded emulator over 370-like intermediate code | **True** | Cubbon 1977, pp. 53–54 |
| The emulator was written in under 10 KB of ROS | **True (IBM's own claim)** | Cubbon 1977, p. 54 |
| The 5100 emulates a System/370 mainframe | **False** | No 370 ISA, OS, channels or virtual storage |
| The 5100 runs System/370 machine code | **False** | Intermediate code is APL-specific, not 370 ISA |
| The ability was undocumented | **False** | Cubbon 1977; MIM §4; manual appendices |
| Non-executable 370 ROM code was shipped inside the 5100 | **Misleading** | ROS holds APL, BASIC and common ROS; the APL intermediate code is "System/370-like", not 370 object code |
| Titor is the origin of the "System/370 emulation" claim | **False** | IBM published it in 1977; the Titor posts popularised a distorted version in 2000 |

## Reading order

1. [evidence.md](evidence.md) — the primary quotations, with citations, so you can check them.
2. [README.md](README.md) — this page's architecture summary.
3. [what-it-was-not.md](what-it-was-not.md) — boundaries and the XT/370 contrast.
4. [myths.md](myths.md) — Titor, *Steins;Gate*, and how the claim mutated.
