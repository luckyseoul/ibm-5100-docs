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

Dual-language machines have a front-panel toggle — on the 5100 it is the third toggle from the
left, up for APL, down for BASIC.

| Item | Value |
|---|---|
| Announcement | 9 September 1975 (GSD) |
| Withdrawal | 31 March 1982 (IBM Hursley Museum hardware list) |
| Main storage | 16, 32, 48 or 64 KB |
| ROS | APL or BASIC interpreter ROS plus executable ROS; the mix depends on the model |
| Display | 5-inch CRT, 16 lines × 64 characters |
| Tape | DC300 quarter-inch cartridge, 204 KB, 512-byte records |
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

From the MIM section 4 device-address table, as implemented in MAME's `cpu_ioc_map`:

| Device address | Function |
|---|---|
| `0` | Device address 0 control (base I/O card) |
| `1` | Non-executable ROS status / control (ROS select) |
| `2`–`3` | (5110: executable ROS status/control) |
| `4` | Keyboard status / control |
| `5` | Printer: read not used, write control |
| `6`–`7` | — |
| `8` | Expansion feature: read status, write control |
| `9`–`D` | — |
| `E` | Tape: read status, write control |
| `F` | Device address F control |

Interrupt levels are prioritised: **keyboard**, then **tape and printer**, then
**communications and serial I/O**, then normal operations (Cubbon 1977, p. 55).

## Tape

The DC300 cartridge holds 204 KB, written in 512-byte records. The MIM states it flatly — "All
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
