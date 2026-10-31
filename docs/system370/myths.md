# The myth: John Titor, the "IBN 5100", and how the claim mutated

This page is about the *story*, not the hardware. It is included because the story is now the
main reason people search for "IBM 5100 System/370", and because the story's version of the
fact is wrong in specific, correctable ways.

---

## What was claimed

The John Titor persona posted to the Time Travel Institute forums and the Art Bell
Post-2-Post BBS between 1998 and 2001, claiming to be an American soldier from 2036. The
relevant claim, as summarised by Wikipedia (citing *The Telegraph*, 2015):

> "Titor specifically claimed the IBM 5100 had an undocumented ability to emulate IBM
> System/370 mainframes and translate between their machine code and more modern languages —
> a capability needed to debug the legacy systems."

The same summary notes that the feature "was not widely known at the time of Titor's posts,
but had been confirmed by engineers who worked on the machine, leading some observers to
conclude that whoever was behind the posts had insider knowledge of the 5100's architecture."

That last inference is the engine of the legend: the claim was *specific enough to be
checkable*, and it checked out **partially** — which is exactly the mixture that makes a hoax
durable.

## Three errors in one sentence

| Titor phrasing | What the documents show |
|---|---|
| "undocumented ability" | Documented in IBM's 1977 symposium paper, in MIM §4 and Appendix C, and in the customer APL/BASIC manuals' compatibility appendices. Obscure ≠ undocumented. |
| "emulate IBM System/370 mainframes" | Emulates the **APLSV language implementation** (and a 370/VS-compatible BASIC dialect), not the machine. No 370 ISA, OS, channels or virtual storage. |
| "translate between their machine code and more modern languages" | No 370 machine-code translator exists in the design. The emulator interprets APL intermediate code described as "System/370-like". |

## The 5110 slip

Worth knowing before you cite the posts: the persona's **first** version of the story named
the wrong machine.

In an IRC conversation on 14 October 2000, the poster (then using "TimeTravel_0") said he had
been sent back to 1975 to retrieve an **IBM 5110**, and mentioned that model four times. The
5110 was released in 1978 — it did not exist in 1975. From 2 November 2000, the forum posts
switched to the **IBM 5100** and never acknowledged the change. The persona also sent a
correspondent a physical piece of an IBM 5110 label with an Orlando postmark.

(Source: Wikipedia's *John Titor* article, citing the archived IRC log and a 2017 account by
Michael Sauve.)

A story that is precise about microcode but sloppy about which machine existed in 1975 has a
readily identifiable shape.

## Steins;Gate and the "IBN 5100"

The 2009 visual novel *Steins;Gate* and its 2011 anime adaptation use the 5100 as a plot
device, renamed **"IBN 5100"**, able to decode legacy data. The fictional machine's abilities
are narrative devices, not documentation. Wikipedia's IBM 5100 article records the reference;
the anime's own wikis and fan material elaborate it considerably further.

This is the main vector by which the 5100's "hidden 370 mode" reached people who never read a
Titor thread.

## Why it persists

1. **There is a real kernel.** A 1975 desktop really does contain a microcoded interpreter for
   the intermediate code of a System/370 APL implementation. Denying the story outright is
   wrong; the correct move is to shrink it to its true size.
2. **The best source was hard to find.** Cubbon's 1977 paper is an internal symposium
   document, scanned on bitsavers under `apl/`, not under `5100/`. For decades the manuals were
   the only accessible evidence, and their compatibility appendices read like boilerplate
   unless you know what APLSV is.
3. **The machine looks like a prop.** A beige luggable with a 5-inch CRT, a tape cartridge and
   a switch labelled APL/BASIC invites conspiracy.
4. **The claim is unfalsifiable by construction.** The persona's many-worlds framing made
   wrong predictions non-disqualifying.

## Could it have worked?

The 5100 had 64 KB of address space and a 200 KB tape cartridge. Emulating a System/370 well
enough to debug mainframe programs needs a general-purpose CPU, a much larger store, and a
compiler. IBM's own later attempt — the 1983 XT/370 — needed three custom cards and 512 KiB on
top of a PC to reach 0.1 MIPS
([what-it-was-not.md](what-it-was-not.md)).

If you want to see what the claim *would* look like if it were true, the companion project
[titor370](https://github.com/luckyseoul/titor370) implements it: a System/370 interpreter and an
S/370-to-C translator whose output is verified against the interpreter. It runs on a laptop,
which is the honest measure of the distance between the myth and the machine.

## How to answer it, briefly

> The 5100 ran APLSV — IBM's System/370 APL implementation — on a microcoded emulator, and IBM
> documented that in 1977. It did not emulate a System/370 computer: no 370 instructions, no
> operating system, no channels, no virtual storage. The "undocumented 370 emulator" is a
> 2000-vintage internet story wrapped around a real, obscure, and fully documented design
> decision.

## A note on the hoax's authorship

Wikipedia records a 2009 investigation pointing to Larry Haber and his brothers John Rick
Haber and Morey Haber, all of whom denied it, and a 2018 claim by Joseph Matheny that he
consulted on the project as a literary experiment. No one has publicly claimed authorship.
This repository takes no position; the hardware claims are assessable without resolving it.
