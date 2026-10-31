# Hardware overview

The 5100 is a single integrated unit: keyboard, 5-inch CRT, tape drive, processor, ROS and
read/write storage in one case.

---

## Models and configuration

IBM Archives: twelve models, 16 / 32 / 48 / 64 KB of main storage, US$8,975–US$19,975,
available with APL, BASIC, or both. The MIM's model table gives the naming scheme:

| Model | Language | Storage |
|---|---|---|
| A1–A4 | APL | 16 / 32 / 48 / 64 KB |
| B1–B4 | BASIC | 16 / 32 / 48 / 64 KB |
| C1–C4 | APL and BASIC | 16 / 32 / 48 / 64 KB |

Dual-language machines (Model C) have a **BASIC-APL switch**; the MIM's operating procedure says
only "Set the BASIC-APL switch to BASIC/APL, press RESTART", and describes the switch as present
only on Model C. The frequently repeated detail that it is the third toggle from the left, up
for APL and down for BASIC, is **not** in the 5100 manual and is not verified here.

| Item | Value |
|---|---|
| Announcement | 9 September 1975 (GSD) |
| Withdrawal | 31 March 1982 (IBM Hursley Museum hardware list) |
| Main storage | 16, 32, 48 or 64 KB |
| ROS | APL or BASIC interpreter ROS plus executable ROS; the mix depends on the model |
| Display | 5-inch CRT, 16 lines × 64 characters |
| Tape | IBM data cartridge — 300 ft of ¼-inch tape, 512-byte records (commonly identified as the DC300) |
| Printer | IBM 5103 (dot matrix), optional |
| Second tape | IBM 5106 auxiliary tape unit, optional |
| Weight | ~50 lb (23 kg) quoted; measured closer to 55 lb (25 kg) |
| Price | US$8,975 – US$19,975 |

The display has a front-panel switch to show all 64 characters of a line, or only the left or
right 32 characters with spaces between. A second switch displays the first 512 bytes of main
memory in hexadecimal for diagnostics (MIM). The video output can also drive an external monitor via
a BNC connector (vertical scan fixed at 60 Hz), and the internal display can be switched
white-on-black or black-on-white.

## Memory and the ROS scheme

PALM can directly address 64 KB. Because some configurations hold more than 64 KB of
executable ROS plus RAM, the design uses bank switching, and the language interpreters live in
a **separate ROS address space that PALM treats as a peripheral** rather than as memory.

Per the MIM (p. 4-20):

- **Executable ROS** holds the bring-up diagnostic, the I/O control microprograms for tape and
  printer, the IPL supervisor, and the APL/BASIC **language emulator microprograms**.
- **Language ROS** — the APL and BASIC interpreters — is mapped in only when needed, selected
  through device address `01` and the card set:
  - BASIC ROS on the **C4** card;
  - common ROS on the **E2** card;
  - APL ROS on the **C2, D2 and D4** cards.
- The three ROS spaces share an address bus; the controller executes a control instruction to
  device address `01` and the data byte's bit 4 selects BASIC+common while bit 5 selects APL.

The MIM describes a 16-bit ROS address built from two "put" instructions to device address 01,
with the top six bits decoding 30 KB address ranges. MAME models the same structure with four
address spaces (program, read/write, I/O control, I/O data) and a memory view selected by the
`select_ros` line.

Most 5100 operations are microprogrammed in ROS. Some feature microprograms — the Serial I/O
Adapter is the example IBM gives — are **loaded into read/write storage from tape** rather than
living in ROS (MIM, Functional Units).

## I/O map

From the MIM's IOCB description (p. 4-13), which defines the device address in byte 0 of every
I/O control block:

| Device address | Device |
|---|---|
| `00` | Video display and processor |
| `01` | Common and language ROS |
| `02`–`03` | Not used |
| `04` | Keyboard |
| `05` | Printer |
| `06`–`09` | Not used |
| `0A` | Serial I/O |
| `0B` | Not used |
| `0C` | Print plot |
| `0D` | Not used |
| `0E` | Tape drive |
| `0F` | Not used |

Byte 1 selects a tape **subdevice**: `80` internal, `40` external, `20` RPQ (second external),
`10` subdevice 4, `08` subdevice 5, `04`–`01` subdevices 6–8 (not used). A footnote on the same
page records a real constraint: the 5100 may have two auxiliary tape units attached, *or* one
auxiliary tape unit and a printer — but **only two I/O devices total**.

Byte 2 carries the command code, with separate code spaces for tape and printer. Tape commands:
`00` sense, `01` read, `02` write, `03` write last, `04` find, `05` mark, `06` initialize and
mark, `07` rewind, `08` forward space record, `09` backspace record, `0A` find next header,
`0B` write header. Printer commands: `00` sense, `02` print, `03` print, `FD` diagnostic.
Everything else in either space is invalid.

### What MAME implements

MAME's `cpu_ioc_map` is a subset and does not match the table above address for address:

| Address | MAME | MIM |
|---|---|---|
| `0` | `da0_ctl_w` | video display and processor |
| `1` | ROS status / control | common and language ROS |
| `2`–`3` | `noprw` | not used (on the 5110: executable ROS) |
| `4` | keyboard | keyboard |
| `5` | printer write only | printer |
| `6`–`7` | `noprw` | not used |
| `8` | commented "expansion", not mapped | not used |
| `9`–`D` | `noprw` | `0A` serial I/O, `0C` print plot |
| `E` | `noprw` | tape drive |
| `F` | `daf_ctl_w` | not used |

So: the keyboard, ROS selection and display paths are modelled; serial I/O, print/plot and the
tape drive are not, which is consistent with the driver's TODO list. Do not read MAME's map as
the hardware's map.

Interrupt levels are prioritised: **keyboard**, then **tape and printer**, then
**communications and serial I/O**, then normal operations (Cubbon 1977, p. 55).

## Tape

The IBM data cartridge is commonly identified as a DC300. It holds 204 KB, written in 512-byte
records, though the MIM also says "200K bytes of formatted data" elsewhere — see
[../sources.md](../sources.md#8-tape-capacity). The MIM states the capacity flatly — "All
tapes have 204K bytes storage" — and the tape I/O microprogram writes one 512-byte record block
at a time. APL system commands added for
the device — `)MARK`, `)OUTSEL`, `)REWIND`, `)MODE`, `)PATCH` — are listed in the APL
Reference Manual Appendix D. The file header for a marked file needs 0.5 KB.

The 5110's APL reference adds a useful compatibility note for preservation work: file types 2,
7 and 8 written on tape by a 5100 can be read by a 5110 and vice versa, but 5100 continued
workspaces (file type 6) and 5110 continued workspaces (file type 26) are **not** compatible.

## Communications and serial I/O

Two distinct options, often conflated:

- **Communications Adapter** (announced with the 5100, September 1975): makes the 5100 appear
  as an **IBM 2741** communications terminal, start-stop mode, using EBCD (Extended Binary
  Coded Decimal) notation — PTTC/EBCD in 2741 documentation. Documented in SA21-9215-0.
  It can only talk to 2741-compatible devices.
- **Serial I/O Adapter** (optional, not advertised): RS-232C-class serial port, with line
  rate, parity and code configurable to suit the attached device. Access to the port
  extensions requires loading support from tape for APL or BASIC. Documented in SA21-9239-1.

The 5110 adds Binary Synchronous Communications (up to 4,800 bps, EBCDIC or EBCDIC
transparency, switched/nonswitched point-to-point, multipoint tributary only) and 2770 data
link control, under which it can communicate with a System/370 with the appropriate
subfeatures (GA21-9300-0).

## Keyboard and maintenance mode

The keyboard is a standard IBM solid-state keyboard of the System/32 and 3740 type (Cubbon
1977, p. 53). A maintenance mode, entered by a keyboard sequence documented in the MIM, allows
direct reading and writing of RAM, video memory, CPU registers, interrupt vectors and the
clock counter using hexadecimal codes, and can be used to enter PALM machine code directly.

## Where to read the details

- **Memory map, device addresses, signals, card locations**: MIM SY31-0405-3, sections 2–4.
- **Card-level parts and FRUs**: Parts Catalog S131-0599-3.
- **Printer**: 5103 MIM SY31-0414-3.
- **Communications hardware**: SY31-0429-2.
- **Emulator implementation**: MAME `src/mame/ibm/ibm5100.cpp` and `src/devices/cpu/palm/`.
