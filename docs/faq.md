# FAQ

Short answers, with pointers. Where a claim is contested, it says so.

**Was the 5100 the first portable computer?**
It is one of the first, and the first IBM product of its kind. The title is contested — the
MCM/70, the Wang 2200 and the HP 9830 are all in the argument — and the 5100 was not battery
powered: "portable" meant luggable, about 50 lb. Its direct ancestor, SCAMP (1973), is called
"the world's first personal computer" by *PC Magazine* in 1983.

**How much did it cost?**
US$8,975 to US$19,975 across twelve models, depending on memory (16/32/48/64 KB) and language
(APL, BASIC, or both). IBM Archives.

**What languages did it run?**
APL, BASIC, or both. Dual-language machines have a front-panel toggle: up for APL, down for
BASIC.

**Could it emulate a System/370?**
It ran **APLSV**, IBM's System/370 APL implementation, on a microcoded emulator, and IBM
documented that. It did **not** emulate a System/370 computer. See
[system370/README.md](system370/README.md).

**So the "hidden 370 emulator" story is false?**
The *hidden* part is false. The *370* part is a distortion of something real: the APL
implementation came from the System/370, its intermediate code was "System/370-like", and a
sub-10 KB emulator executed it. The story comes from the John Titor posts (2000–2001) and was
popularised by *Steins;Gate* as the "IBN 5100". See [system370/myths.md](system370/myths.md).

**Did IBM keep it secret?**
No. It is in the customer APL Reference Manual (Appendix D, p. 206), the customer BASIC
Reference Manual (p. 143), MIM section 4 and Appendix C, and a 1977 IBM symposium paper. It was
obscure, not concealed.

**What is PALM?**
The 5100's microcoded processor. The expansion of the acronym is unsettled: "Program All Logic
in Microcode" (Wikipedia, citing Roberson's 1976 IEEE paper) and "Put All Logic in Microcode"
(hobbyist usage, MAME's source header) both circulate. IBM's own MIM never uses the word —
it says "controller". See [hardware/palm.md](hardware/palm.md).

**Why does a 64 KB machine have 32–64 KB of ROM on top?**
PALM addresses 64 KB directly, so the design bank-switches. Language interpreters live in a
separate ROS address space selected through device address `01`, which PALM treats as a
peripheral rather than as memory. See [software/ros-and-tape.md](software/ros-and-tape.md).

**Can I run one today?**
Yes — MAME's `ibm5100` driver covers the 5100 and 5110. You need ROM images; the driver declares
the exact filenames and hashes. Tape and printer are still TODO in the driver, so you can run
the machine but not yet mount a workspace cartridge. See [guides.md](guides.md#3-i-want-to-run-one).

**Are the ROMs legally available?**
They are not distributed by this repo, and IBM has not published them. Whether a given dump is
redistributable is a jurisdiction- and provenance-specific question this repo does not answer.
MAME requires you to supply them.

**What is the difference between the 5100, 5110 and 5120?**
The 5100 (1975) is the original. The 5110 (1978) adds diskette storage, lowercase characters,
new APL system commands (`)PROC`, `)LINK`, `)RESUME`, `)SORT`) and more shared-variable
support. The 5120 (1980) is the larger follow-on system. The 5100's APL and the 5110's APL are
both documented against APLSV; their BASICs are both documented against 370/VS BASIC.

**What is the "IBN 5100"?**
A fictionalised 5100 from the 2009 visual novel and 2011 anime *Steins;Gate*, used as a plot
device that can decode legacy data. "IBN" is the show's stand-in for "IBM". Its abilities are
story, not documentation.

**Was the 5100 used for codebreaking?**
No primary evidence has been found, and this repository does not assert it. The relevant
question — whether its programmable microcode could implement custom operations — is separate
from whether it was ever used that way. The community discussion is linked in
[community.md](community.md).

**Where do the manuals live?**
bitsavers, mostly. Start at [archives.md](archives.md); the catalogue is
[manuals.md](manuals.md).
