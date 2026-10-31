# ROS, IPL and tape

The 5100 has no operating system in the modern sense. It has ROS (read-only storage), a
bring-up diagnostic, an IPL routine, a diagnostic control program, I/O microprograms and a
language emulator — all microcode, all in ROM, all documented in the MIM.

---

## The ROS spaces

| Space | Contents | Cards (5100) |
|---|---|---|
| Executable ROS | bring-up diagnostic, IPL, DCP, I/O control microprograms for tape and printer, APL and BASIC **emulator** microprograms | H2 (BASIC emulator), H4 (APL emulator) |
| Common non-executable ROS | shared tables and data | E2 |
| BASIC non-executable ROS | BASIC interpreter | C4 |
| APL non-executable ROS | APL interpreter | C2, D2, D4 |

MIM §4 (p. 4-19) describes the selection:

> "APL, BASIC and common ROS share a common address bus. To select one of the three ROS
> spaces, the controller must execute a control instruction using device address 01. The data
> byte of the control instruction is put on the bus out and stored in the bus out register on
> the E2 card. During control strobe, device address 01 and active data bit 4 will select BASIC
> and common ROS; address 01 and active data bit 5 will select APL ROS."

MAME models the same arrangement: `h2.ros` and `h4.ros` are the executable ROS halves, while a
memory view selects between `common`+`basic` (`c4.ros`, `e2.ros`), `apl` (`c2.ros`, `d2.ros`,
`d4.ros`), and read/write storage.

### Address formation

The MIM describes loading the 16-bit ROS address a byte at a time with two "put" instructions
to device address 01, and using the top six address bits (0–5) to decode 30 KB address
ranges. This is bank switching in the literal sense: the address space is built up by the
controller as it issues control instructions, not by a memory-management unit.

### Patching

Because the processor can fetch from either executable ROS or read/write storage, the design
supports patching:

> "This also makes possible the patch capability which allows changes to the logic flow by
> superceding portions of ROM instructions with instructions in read/write storage."
>
> — Cubbon 1977, p. 55

APL's `)PATCH` command loads "an IMF or Tape Recovery program" from an IBM-supplied tape (the
manual does not expand "IMF"); the same mechanism is what lets a field engineer alter
microcode behaviour without new ROS.

## Power-on sequence

From MIM §4:

1. Power-on reset activates ROS.
2. The processor begins executing at the address contained in location `0000`.
3. That is the bring-up diagnostic, ending with the IPL routine.
4. IPL brings up the selected language emulator; the language ROS interpreter is mapped in
   when needed.

## Tape

The DC300 quarter-inch cartridge is the 5100's only persistent storage: **204 KB**, written in
**512-byte records**. The 5106 adds a second drive in an external box.

APL sees tape through system commands added specifically for the device — `)MARK`, `)OUTSEL`,
`)REWIND`, `)MODE`, `)PATCH` — and through `)SAVE`/`)LOAD` with device/file numbers replacing
APLSV library numbers. A marked file's header needs 0.5 KB.

Cross-generation compatibility, from the 5110 APL Reference (SA21-9303-0, "5110 Compatibility
with the IBM 5100"):

- File types **2, 7 and 8** written by a 5100 can be read by a 5110, and vice versa.
- Only workspaces written by `)SAVE` on a 5100 can be loaded or copied into a 5110.
- 5100 continued workspaces (**type 6**) and 5110 continued workspaces (**type 26**) are not
  compatible.
- The 5110 needs 224 more bytes of user work area, so some 5100 programs can hit `WS FULL` on
  a 5110.

For anyone trying to read old cartridges or diskette images, those four rules are the useful
starting point.

## Machine code and maintenance mode

The DCP lives in executable ROS. A keyboard sequence documented in the MIM puts the machine
into a maintenance mode in which RAM, video memory, CPU registers, interrupt vectors and the
clock counter are exposed as hexadecimal, and PALM code can be entered directly. This is the
mechanism hobbyists use to run hand-assembled PALM programs on real hardware, and the reason
the MIM Appendix C instruction tables matter outside a museum.

## Preservation status

- **ROM images**: MAME's driver expects `h2.ros`, `h4.ros`, `c4.ros`, `e2.ros`, `c2.ros`,
  `d2.ros`, `d4.ros`, and `j2.ros`, with CRC/SHA-1 checks in the source. The character
  generator ROM `j2.ros` is explicitly marked **BAD_DUMP** — MAME's copy is "hand-made based on
  the character map in the documentation", with an assumption about the 8×8/4-row layout. That
  is the weakest link in the current emulation.
- **Tape images**: no standard public corpus has been identified for this repository. The file
  type table above is the map for anyone building one.
- **Documentation**: complete for the 5100 except the print-plot manuals and reference cards
  listed as gaps in the README.
