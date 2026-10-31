# Evidence: the primary sources, quoted

Every quotation below is from a document in [the catalogue](../manuals.md). Page numbers are
the printed page numbers, not PDF page indices. OCR has been corrected against the page
images where the scan is poor; corrections are limited to obvious character errors.

---

## 1. IBM 5100 Maintenance Information Manual, SY31-0405-3 (October 1979)

### 1.1 The machine emulates the language, not the mainframe

Section 4, "Internal Operation of the 5100", subsection **Microprogramming**, p. 4-12:

> "An internal machine program controls the 5100. This internal machine program consists of
> several microprograms, which the 5100 controller uses to accomplish given tasks. Because the
> 5100 controller cannot process an APL or BASIC user program directly, it must emulate the
> APL or BASIC program to the internal machine microcode by means of the APL (H4) or BASIC
> (H2) emulators on the executable ROS card."

> "When an APL or BASIC language statement is decoded by the 5100 computer, the machine
> microcode performs a series of microinstructions that accomplish the required emulation of
> the user language."

> "Note: Because the 5100 cannot operate directly from a user language, the system emulates or
> appears to have the attributes of the user's language, while each instruction is translated
> into language that the system can use."

Two paragraphs earlier, the manual lists what the microprograms are:

> "The various microprograms that are used on the 5100 are the emulators (APL and BASIC); the
> I/O controller interface (tape I/O, printer I/O, and keyboard I/O); the diagnostic control
> program (DCP); and the IPL and I/O supervisor microprograms."

### 1.2 Where the language interpreters physically live

Section 4, **ROS**, p. 4-20:

> "The microprograms stored in ROS are directly executed by the controller; they control the
> operation of the 5100. Executable ROS contains the bring up diagnostic, the I/O control
> microprograms for tape and printer, and the language emulator microprograms."

> "Language ROS (APL or BASIC) interpreter functions are accessed and placed into read/write
> storage when they are needed to control the APL or the BASIC microprogram executed by the
> controller."

> "BASIC ROS is located on the C4 card, common ROS is located on the E2 card, and APL ROS is
> located on the C2, D2 and D4 cards. APL, BASIC and common ROS share a common address bus. To
> select one of the three ROS spaces, the controller must execute a control instruction using
> device address 01."

### 1.3 The instruction format

Appendix C, **Microinstructions**, p. C-1:

> "I/O control and the high level languages (APL and BASIC) are implemented with
> microinstructions in read/write storage and executable ROS. All 5100 Portable Computer
> microinstructions are a halfword (2 bytes). The first 4 bits of the halfword is the op code.
> The meaning of the remaining 12 bits depends on the op code (refer to Formats). Some op
> codes have a modifier (bits 12-15) that expands the number of microinstructions beyond 16."

The appendix then classifies the op codes: I/O, fetch and store, register, arithmetic
register, logical register, and jump microinstructions.

### 1.4 The publication library

The MIM's figure **"IBM 5100 Computing System Publications"** (p. 1-3 of the library section)
is the authoritative list of the 5100's own manual set, and is reproduced in
[../manuals.md](../manuals.md). It names: `1608314` (MAPs), `SY31-0405` (MIM),
`SY31-0414` (5103 MIM), `SY31-0429` (async comm / serial I/O MIM), `SA21-9239` (serial I/O
user's), `SA21-9215` (communications reference), `SA21-9216`/`SA21-9212` (BASIC/APL
introductions), `SA21-9217`/`SA21-9213` (BASIC/APL references), `SA21-9265`/`SA21-9264`
(print-plot BASIC/APL user's manuals), plus the parts catalogs.

### 1.5 On the name "PALM"

A negative finding worth recording: **the string "PALM" does not occur in the MIM's
extracted text at all.** The manual consistently calls the processor "the controller" and
the "microprocessor". This matches the secondary literature's note that IBM's maintenance
documentation referred to the PALM module as the controller. Anyone citing "PALM" to the MIM
is citing the literature around the manual, not the manual itself.

---

## 2. A. J. Cubbon, "The IBM 5100 Portable Computer Design"

APL ITL Symposium, Endicott, New York, 11–13 January 1977, Volume 2, pp. P51–P56. Marked
"IBM Internal Use Only". Scan: `bitsavers.org/pdf/ibm/apl/5100_Portable_Computer_Design_Jan77.pdf`.

This is the single most informative document on the 370 question. Cubbon was in
GSD-Rochester and also wrote the *IBM 5100 Shared Variable Primer* (Technical Report
07.607, April 1976).

### 2.1 The prototype ran 1130 APL under an emulator

> "The prototype supported the APL language and used an audio-type cassette tape as its
> permanent storage media. The APL used on the prototype was originally implemented on the
> IBM 1130 Computer. An 1130 emulator was written in the native microlanguage of the
> prototype."

*(p. 52.)*

### 2.2 The switch to the System/370 implementation

> "At this time, one of the team members introduced the idea of using the IBM System/370
> version of APL called APLSV. This version had a significant number of advantages over the
> 1130 APLs. It was the latest version with all the latest APL language features and
> functions. It had 15 digits of numerical precision vs six in the 1130 versions. It had an
> extensive input/output subsystem which was not available in the early APL systems. And most
> significantly, it was the most widely used and tested version of APL in IBM. The one
> drawback was the lack of a 370 emulator for which there was only 12K executable ROM left."

*(p. 53.)*

### 2.3 The emulator, and its size

> "In late June 1974, the development team undertook the formal task of writing an emulator
> and the necessary higher-level code to interface the 370 APL interpreter with the 5100
> keyboard, display, tape and printer. To date, the finished emulator has remained error free
> and uses less than 10K of ROM."

*(p. 54.)*

### 2.4 The three interface routines

> "There were three major interface routines:
>
> a. A supervisor that interfaced to the keyboard and displayed like a terminal. It also
> permitted using the printer as a hard copy of the display.
>
> b. A command processor that supported the APL program library commands like SAVE and LOAD
> for the tape cartridge.
>
> c. An input/output processor that allows the APL programmer to use the tape and printer as
> independent devices under program controls."

*(p. 54.)*

### 2.5 The scope limit, stated by IBM

> "The only differences between the 5100 version of APL and the APL on the System/370 were the
> portions dependent on the input/output devices, display vs typewriter, and tape vs direct
> access devices."

*(p. 54.)*

### 2.6 The intermediate code is "System/370-like"

> "The newest ROM is the dense, 48K bits per chip storage used for the APL and BASIC
> interpreters. This storage contains the intermediate language instructions. In the case of
> APL, these are System/370-like instructions. This storage is accessed by the emulators for
> each intermediate language as if it was a direct access storage device rather than like
> memory."

*(p. 54.)*

### 2.7 The processor, as described in 1977

> "The microprocessor is a fast two-chip 8-bit processor. It has 49 16-bit microinstructions
> and can operate on four interrupt levels. The levels are prioritized in this order:
> 1) Keyboard; 2) Tape and Printer; 3) Communications and Serial I/O; 4) Normal Operations."

*(p. 55.)*

Note the conflict with later descriptions of PALM as a board of 13 bipolar gate arrays (see
[../sources.md](../sources.md#known-conflicts)). Both can be true of different build stages
or different members of the family; the documents do not settle it.

---

## 3. IBM 5100 APL Reference Manual, SA21-9213-2 (May 1976)

**Appendix D, "5100 APL Compatibility with IBM APLSV", p. 206.** The appendix opens:

> "The 5100 APL system differs from the IBM APLSV system primarily because the 5100 is a
> single user system with different input/output devices and it has display screen output
> rather than typewriter output. The differences are as follows:"

It then lists the differences, including:

- Power-on signs the user on; no sign-on or ID number required.
- The 5100 active workspace is generally smaller than the APLSV active workspace, and is
  further limited by the shared-variable processor.
- The default number of symbols is 125 instead of 256.
- The library number in system commands is redefined as a device/file number.
- `)LOAD`, `)COPY`, `)PCOPY` require the library number and workspace ID; `)DROP` requires
  the library number (and workspace ID for stored workspaces).
- Not supported because they apply to multi-terminal or remote systems: `)OFF`, `)OFF HOLD`,
  `)CONTINUE HOLD`, `)PORTS`, `)MSGN`, `)MSG`, `)OPRN`, `)OPR`, and all special system
  operator commands.
- Not supported because the function is not supported: `)GROUP`, `)GRPS`, `)GRP`.
- Not supported: `)ORIGIN`, `)WIDTH`, `)DIGITS` (available as system variables `⎕IO`, `⎕PW`,
  `⎕PP`).
- Added for the 5100's devices: `)MARK`, `)OUTSEL`, `)REWIND`, `)MODE`, `)PATCH`.
- `)CONTINUE` changed to save workspaces with suspended functions.
- New error messages: `LINE TOO LONG` (statements over 115 characters) and `WS TOO BIG`.

The direction of the comparison matters: IBM documents the 5100 *against APLSV*, not against
some generic "APL". The mainframe implementation is the reference point.

---

## 4. IBM 5100 BASIC Reference Manual, SA21-9217-3 (July 1977)

**"5100 BASIC Compatibility With IBM 370/VS BASIC", p. 143:**

> "The BASIC language used in the 5100 differs from IBM 370/VS BASIC in the following areas:"

The list includes: no lowercase characters; no double quotation marks; one precision only
(13 digits); hexadecimal constants (`X'…'`); `TAB(expression)` inside `PRINT`; an added `FLP`
parameter on `PRINT`, `MAT PRINT`, `PRINT USING`, `MAT PRINT USING` to direct formatted output
to printer, screen or tape file; file description information that would otherwise be supplied
by the operating system; `CHAIN` without re-initialising `USE` data; `USE` with listed data
and array dimensions; `TAB(x)` but not VS BASIC functions `CEN`, `CLK`, `CNT`, `CPU`, `DAT`,
`DOT`, `FAH`, `IDX`, `JDY`, `KLN`, `KPS`, `LEN`, `MAX`, `MIN`, `NUM`, `PRD`, `RLN`, `SUM`,
`TIM`; no `ASORT`/`DSORT`; statement numbers up to 9999 with user functions assigned
9990–9999; no `DELETE FILE`, `EXIT`, `FORM`, `READ FILE`, `REREAD FILE`, `REWRITE FILE`,
`WRITE FILE`.

Again the comparison baseline is a System/370 implementation: **370/VS BASIC**.

---

## 5. IBM 5110 documentation — the same pattern, one generation later

- **SA21-9303-0**, *IBM 5110 APL Reference Manual* (December 1977), **Appendix E, p. 229**:
  "The 5110 APL system differs from the IBM APLSV system primarily because the 5110 is a
  single user system with different input/output devices and it has display screen output
  rather than typewriter output."
- **SA21-9308-2**, *IBM 5110 BASIC Reference Manual* (April 1979), **p. 201**:
  "5110 BASIC Compatibility with IBM 370/VS BASIC".

The 5110 adds diskette, lowercase, `)PROC`, `)LINK`, `)RESUME`, `)SORT`, and more shared
variable support — but keeps the same two reference implementations.

---

## 6. IBM Archives

The IBM Archives exhibit page for the 5100 (archived December 2018) states:

> "Weighing approximately 50 pounds and sized slightly larger than an IBM typewriter, the 5100
> Portable Computer was announced by the company's General Systems Division (GSD) in September
> 1975. … Available in 12 models providing 16K, 32K, 48K or 64K positions of main storage, the
> 5100 sold for between $8,975 and $19,975. The 5100 was available with either APL or BASIC —
> or both — programming languages."

---

## 7. What is *not* in any of these documents

For completeness, the negative evidence:

- No System/370 instruction set, opcode table, or 370 memory map appears in the MIM.
- No OS/VS, JCL, job control, channel program, or 3270 data stream appears anywhere in the
  5100 manual set.
- No claim of "translating machine code" appears. The emulator interprets APL intermediate
  code and interfaces APL to the 5100's devices.
- No mention of secrecy, concealment, or a hidden mode. The relevant material is in the
  customer reference manuals and an IBM internal symposium paper.
