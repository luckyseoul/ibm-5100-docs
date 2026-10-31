# Community and modern sources

Modern material is uneven. This page labels every entry by **how it was verified**:

- **[read]** — fetched and read while compiling this dossier.
- **[snippet]** — only a search-result title/summary was available; the page itself was not
  read (bot protection, JavaScript rendering, or video content).
- **[blocked]** — the site refused automated access (Cloudflare); listed because it is a real
  resource, not because its content was checked here.

---

## Emulation

### MAME — the maintained emulator

- **[read]** `src/mame/ibm/ibm5100.cpp` — the 5100/5110 driver.
  <https://github.com/mamedev/mame/blob/master/src/mame/ibm/ibm5100.cpp>
  BSD-3-Clause, copyright Patrick Mackinlay. Implements ROS banking, RWS sizing, keyboard,
  display, beeper on the 5110, and declares `ibm5100` (1975) and `ibm5110` (1978).
- **[read]** `src/devices/cpu/palm/palm.cpp` and `palm.h` — the PALM CPU device: four address
  spaces, four register banks, interrupt levels, disassembler.
  <https://github.com/mamedev/mame/tree/master/src/devices/cpu/palm>

Driver TODOs (from the source, i.e. the honest gap list): display registers, device address F,
tape controller, disk controller, printer, communications cards, expansion feature, feature ROS
(K4). The character-generator ROM is `BAD_DUMP` — MAME reconstructs it from the documentation's
character map.

### Other

- **[snippet]** *IBM 5100 Side Scroller* — VCF forum thread on new PALM machine code.
  <https://forum.vcfed.org/index.php?threads/ibm-5100-side-scroller-presentation-new-palm-machine-code.1253061/>
- **[snippet]** Deskthority restoration thread, including video of PALM sample code attributed
  to Christian Corti. <https://deskthority.net/viewtopic.php?t=20163>

## Talks

- **[snippet]** *Exploring IBM 5100 P.A.L.M. with Steve Lewis* — a talk specifically on the
  PALM architecture and instruction set, by someone who reverse-engineered it.
  <https://www.youtube.com/watch?v=JIJNrBaTenM>

## Articles and write-ups

- **[snippet]** Bradford Morgan White, *The History of the IBM 5100*.
  <https://www.abortretry.fail/p/the-history-of-the-ibm-5100>
- **[snippet]** Hackaday, *Bringing APL To The Masses: The History Of The IBM 5100*
  (19 December 2023). <https://hackaday.com/2023/12/19/bringing-apl-to-the-masses-the-history-of-the-ibm-5100/>
- **[snippet]** voidstar, *IBM 5100 Personal Computer* — describes the executable ROS as
  written in PALM instructions that interpret the legacy systems' code.
  <https://voidstar.blog/ibm-5100-personal-computer/>
- **[snippet]** Retrocomputing Forum, *All about the IBM 5100 from 1975 (also IBM 5106 and
  IBM 5110)* — notes on the built-in DCP, PALM machine code, a modern assembler, and the
  "tin can" memory packages. <https://retrocomputingforum.com/t/all-about-the-ibm-5100-from-1975-also-ibm-5106-and-ibm-5110/2977>
- **[snippet]** oldcomputers.net — photographs and period advertising.
  <http://oldcomputers.net/ibm5100.html>
- **[snippet]** oldcomputermuseum.com — photographs and a short description.
  <https://www.oldcomputermuseum.com/ibm_5100.html>

## Reference and discussion

- **[blocked]** APL Wiki, *APL 5100* — states the APL interpreter was based on System/360's
  APL.SV and that PALM could run emulators for System/360 and System/3.
  <https://aplwiki.com/wiki/APL_5100>
- **[blocked]** Retrocomputing Stack Exchange, *Was the IBM 5100 ever used for codebreaking?* —
  includes notes on the PALM instruction set and Appendix C of the MIM.
  <https://retrocomputing.stackexchange.com/questions/7005/was-the-ibm-5100-ever-used-for-codebreaking>
- **[read]** Wikipedia, *IBM 5100* — the best single secondary summary; its "Emulator in
  microcode" section is the origin of many later claims.
  <https://en.wikipedia.org/wiki/IBM_5100>
- **[read]** Wikipedia, *IBM PALM processor* — thin, but preserves the "Program All Logic in
  Microcode" expansion and the board-level description.
  <https://en.wikipedia.org/wiki/IBM_PALM_processor>
- **[read]** Wikipedia, *John Titor* — the Titor claim, the 5110/5100 discrepancy, and the
  hoax-authorship investigations, all with citations.
  <https://en.wikipedia.org/wiki/John_Titor>

## How to treat community claims

Community work is where the PALM instruction set is actually being used, and several
contributors have done serious reverse engineering. It is also where the Titor framing leaks
into technical writing: phrases like "hidden 370 mode" or "System/370 emulation" often mean no
more than "the APL interpreter is APLSV". When a community source and an IBM manual disagree,
the manual wins; when two community sources disagree and no manual covers it, this repository
records the disagreement rather than picking a winner.
