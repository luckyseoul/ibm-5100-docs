# What the 5100 was not

The 5100 has a real, documented System/370 lineage. The temptation is to let that lineage
imply capabilities the machine never had. This page draws the boundary.

---

## Not a System/370 computer

| System/370 capability | 5100 |
|---|---|
| S/370 instruction set executed by hardware | No. PALM executes PALM microinstructions. |
| Supervisor state / privileged instructions | No. No supervisor, no privileged mode. |
| Virtual storage / DAT | No. 64 KB physical address space, bank-switched. |
| Channel subsystem / I/O channels | No. Device-address I/O handled by microprograms. |
| OS/VS1, OS/VS2, VM/370, DOS/VS | No. No operating system at all in that sense. |
| JCL / job entry / batch | No. Single interactive user. |
| Multiprogramming / multi-terminal | No. Single user; APLSV's multi-terminal commands are explicitly unsupported. |
| 3270 data stream | No. (The 5110's BSC/2770 link is a communications feature, not a display protocol stack.) |
| Disk / DASD | No. IBM data cartridge (DC300) tape on the 5100; the 5110 adds diskette. |
| Card readers, line printers | No. 5103 matrix printer as an option. |

The 5100's "370" is a **language implementation and its intermediate code**, re-hosted on a
desktop with different I/O. That is why IBM's own comparison appendix spends its length on
display vs typewriter, tape vs direct access, single-user vs multi-terminal, and workspace
size — not on instruction-set differences.

## Not a 370 emulator in the XT/370 sense

IBM did later build a real System/370 emulator for a desktop. It looked nothing like this.

**IBM Personal Computer XT/370**, announced October 1983, was an IBM PC XT with three custom
8-bit cards:

- a processor card with two modified Motorola 68000 chips that emulate most S/370 fixed-point
  and non-floating-point instructions, plus a modified Intel 8087 for S/370 floating point;
- a 512 KiB memory card;
- a 3270 terminal-emulation card used to download system software from a host.

It booted DOS, then ran the **VM/PC** control program, supported up to 4 MB of virtual memory
using the hard disk for paging, and was claimed at 0.1 MIPS for about US$12,000. It was
discontinued in April 1987.

That machine executes S/370 instructions, runs a 370 operating system, and provides virtual
storage. The 5100 does none of those things. The correct analogy for the 5100 is not
"XT/370 in 1975" — it is "one mainframe *language implementation*, microcoded onto a
single-user desktop".

## Not a code translator

The Titor claim includes "translate between [System/370] machine code and more modern
languages". Nothing in the 5100 documentation describes translation of 370 machine code.
What exists is:

- an APL interpreter whose **intermediate** instruction stream is described by its designer as
  "System/370-like";
- a microcoded interpreter that executes that stream;
- three interface routines binding the interpreter to keyboard, display, tape and printer.

There is no 370 object-code input path, no 370 loader, no 370 executable format. APL
workspaces move on tape as APL workspaces.

## Not secret

The relevant facts appear in:

- the customer **APL Reference Manual** (Appendix D) and **BASIC Reference Manual** (p. 143);
- the **Maintenance Information Manual**, section 4 and Appendix C;
- an IBM internal symposium paper that was printed, distributed, and later scanned.

"Not widely known" is fair. "Undocumented" and "hidden" are not.

## Not a mainframe terminal, either — that was the 5110

If you want the 370 *connection* story, note that the 5110's communications features attach it
to a real System/370: the **Binary Synchronous Communications** feature (up to 4,800 bps,
EBCDIC or EBCDIC transparency, switched/nonswitched point-to-point, multipoint tributary) and
the **2770 data link control** mode, under which, per the 5110 *General Information Manual*,
"the 5110 can communicate with a System/370 equipped with the appropriate subfeatures."

That is terminal/BSC emulation over a wire — again not 370 instruction emulation, and again
documented in the customer manual.
