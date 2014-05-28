# Shrt.nr

Shorten strings by replacing combinations of letters with unicode characters that look similar. Great for maximizing your Twitter content when you need those extra 1 or two characters.

    python shrtnr.py "I'm going to aerobics tomorrow"
    IN  (32): I'm going to aerobics tomorrow
    OUT (30): I'm going to ærobѤs tomorrow

_Note:_ does not generally help due to the relative infrequency of these specific combinations of characters.

## Supported Replacements:
- ae -> \u00E6
- AE -> \u00C6
- 1/4 -> \u00BC
- 1/2 -> \u00BD
- 3/4 -> \u00BE
- ij -> \u0133
- OE -> \u0153
- ol -> \u01A3
- LJ -> \u01C8
- lj -> \u01C9
- dz -> \u01F3
- NJ -> \u01CA
- Nj -> \u01CB
- nj -> \u01CC
- bl -> \u044B
- ts -> \u02A6
- tf -> \u02A7
- tc -> \u02A8
- ia -> \u0468
- ic -> \u0464
- kk -> \u04DD