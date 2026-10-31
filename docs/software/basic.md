# BASIC on the 5100

APL got the 5100 its charter; BASIC got it a market. The 5100 was available with APL, BASIC, or
both, and on dual-language machines a front-panel toggle selects the language.

---

## Which BASIC it is

IBM's customer manual compares it to **IBM 370/VS BASIC**:

> **5100 BASIC Compatibility With IBM 370/VS BASIC**
>
> "The BASIC language used in the 5100 differs from IBM 370/VS BASIC in the following areas:"
>
> — SA21-9217-3, p. 143

That appendix is a difference list, and it is the authoritative statement of what the dialect
is and is not. The documented deltas:

| Area | 5100 behaviour |
|---|---|
| Character set | No lowercase letters; no double quotation marks |
| Precision | One precision only — **13 digits** |
| Constants | Hexadecimal constants, `X'…'` |
| Output | `TAB(expression)` permitted inside `PRINT` |
| Output routing | Added `FLP` parameter on `PRINT`, `MAT PRINT`, `PRINT USING`, `MAT PRINT USING`; `FLO`–`FL9` direct output to the file in the corresponding `OPEN` |
| File description | 5100 supplies file description information that the operating system would supply under 370/VS |
| Chaining | `CHAIN` without initialising the data area reserved by `USE` variables |
| Data passing | `USE` may list data, including array dimensions, to pass data between programs on `CHAIN` |
| Missing VS BASIC functions | `CEN`, `CLK`, `CNT`, `CPU`, `DAT`, `DOT`, `FAH`, `IDX`, `JDY`, `KLN`, `KPS`, `LEN`, `MAX`, `MIN`, `NUM`, `PRD`, `RLN`, `SUM`, `TIM` |
| Missing array functions | `ASORT`, `DSORT` |
| Statement numbers | Up to 9999; user special functions assigned 9990–9999 |
| Missing statements | `DELETE FILE`, `EXIT`, `FORM`, `READ FILE`, `REREAD FILE`, `REWRITE FILE`, `WRITE FILE` |
| `MAT GET` / `MAT PUT` | No `EXIT`, `CONV`, `IOERR` parameters; `MAT PUT` lacks `EXIT`/`IOERR`; `OPEN` lacks `ALL` |
| Image statements | `!` not recognised (can be keyed by overstriking `'` and `.`) |

## The lineage question — unresolved

Two claims are in circulation:

- **Secondary (Wikipedia, uncited in the relevant paragraph):** the 5100's BASIC interpreter is
  "the BASIC interpreter used on IBM's System/3 minicomputer", and the microcode therefore
  emulates "most of the functionality of both a System/370 and a System/3".
- **Primary (IBM, SA21-9217-3, p. 143):** the dialect is defined by comparison with **IBM
  370/VS BASIC**, not System/3 BASIC.

IBM's own design account (Cubbon 1977, p. 52) says only that BASIC "was added because of its
popularity as an interactive computer language in the United States", and that the matrix
printer chosen was the one "already used on the IBM System/32 and the 3740 Data Entry System".
It does not state a System/3 interpreter lineage.

What to conclude: **the manual's 370/VS comparison is the defensible statement.** The System/3
lineage is plausible — IBM's BASIC dialects share ancestry — but this repository has not found
a primary source that establishes it, and the shipping manual points elsewhere. Treat
"System/3 BASIC" as unverified. See [../sources.md](../sources.md#known-conflicts).

## What BASIC on a 5100 looks like

- Single-user, interactive; programs and data on IBM data cartridge files opened with `OPEN`.
- Statement numbers up to four digits, with 9990–9999 reserved for user-defined special
  functions.
- 13-digit numeric precision, no lowercase, no double quotes — the keyboard is an APL-style
  IBM keyboard, and the character set is constrained accordingly.
- Printing via the 5103; plotting via the Print Plot/BASIC feature (`SA21-9265`, not yet
  located — see the README's gap list).

## Reading path

1. **SA21-9216-1**, *IBM 5100 BASIC Introduction* (December 1975) — tutorial.
2. **SA21-9217-3**, *IBM 5100 BASIC Reference Manual* (July 1977) — reference; the 370/VS
   appendix is at p. 143.
3. **GX21-9218**, *IBM 5100 BASIC Reference Card* — not yet located.
4. **S229-8032-1**, *IBM System/3 Reference Summary* — context if you are chasing the
   System/3 lineage claim.
