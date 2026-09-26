# Humanization gate — run for every draft, before any Pangram check

Added 2026-09-25. Joel asked: "how is it possible you're still not following the basic instructions to check the list of tells? can we fix that or is it hopeless?"

**Why the checks got skipped.** The self-audit rules are a long file that I read at the start of a section and then drafted from memory. When a draft felt fine, I went straight to Pangram. D8 already said a check done in my head is a check skipped; it didn't stop me, because nothing forced the check to happen. The list also lacked the tell that mattered most: a paraphrase of the source's skeleton.

**The fix.** Part of the audit is now mechanical and has to happen in the open. There is no Pangram check without a linter report and a written table in the drafts file.

## Steps

1. **Bird's-eye (D1).**
   - Reread the source beat and list its points.
   - Search the article for overlaps and callbacks.
   - Reread a stretch of Joel's own rewrite of AI prose (E43).
2. **Close the source (E42).** Write two or three lines of what I actually want to say, in what order, and why a reader would care. Draft from those lines, not from the source.
3. **Coverage check (D9).** Only now compare against the source's point list. Fold anything missing in as an aside or a single sentence, not a paragraph of its own.
4. **Linter.**

   ```
   python3 articles/inner-child-therapy/tools/tells_lint.py DRAFT.txt \
       --source SOURCE-SECTION.txt --failed EARLIER-FAILED-DRAFTS... [--owner OWNER-LINES.txt]
   ```

   A FAIL means rewrite the draft, not tweak it, then rerun. Never send a FAIL to Pangram.
5. **Manual table in the drafts file.**
   - Every REVIEW item from the linter, with a keep or fix decision and why.
   - The checks the linter can't do:
     - A1: meaning and safety kept;
     - A12: referents;
     - D2: where the draft departs from what an AI would say;
     - E1: naming (never "the kid");
     - E36: details that fit every reader;
     - E8 and E33: premises and terms not yet introduced;
     - E29: one owner practice per section.
6. **Pangram (E27, E37).**
   - At most about three checks per turn.
   - Test with and without the owner's lines.
   - Read results from the page text.
7. **Record** the linter report, the table and the Pangram results in the drafts file before showing Joel.

## What the linter checks

- **Hard FAIL:**
  - Joel's tics;
  - coach phrases above 2 per 100 of my words (E41);
  - half or more of the paragraphs ending on a short line (B7/B13);
  - two or more paragraphs that are strings of instructions (E23);
  - three or more paragraphs with the same opener (B13);
  - second person at 9 or more per 100 of my words (E36/E41);
  - with `--source`: 60% or more of the paragraphs mapping onto source points in the source's order (D9/E42 skeleton);
  - with `--failed`: 15 or more four-word runs reused from failed drafts (B10).
- **REVIEW** (flags for the table):
  - contrast constructions (B2);
  - finished principles (B1);
  - lines that announce a paragraph (B5);
  - individual coach phrases;
  - "kid";
  - packed or list sentences (B4/E15);
  - short knock-downs (B3);
  - short paragraph-final lines;
  - second person above 6 per 100.

## Calibration (2026-09-25)

Eleven texts with known Pangram 4.0 results. The files are in `tools/calibration/`.

| text | Pangram | linter | hard reasons |
|---|---|---|---|
| Borrow One Function r1 | 100% AI | FAIL | source skeleton |
| Borrow One Function r2 | 100% AI | FAIL | coach 3.3/100; landings 3/6 |
| Borrow One Function r3 | 100% AI | FAIL | coach 2.8/100; source skeleton |
| Borrow One Function r4 | 100% AI | FAIL | source skeleton (order 0.87) |
| Borrow One Function r5 | 100% AI, "paraphrased" | FAIL | landings 3/6; source skeleton |
| Music r2, my lines only | 100% AI | FAIL | second person 9.9/100 |
| Dangerous-adult H2 | 100% Human | REVIEW | — |
| Music r4 (installed) | 100% Human | CLEAR | — |
| Music r4, my lines only | 100% Human | REVIEW | — |
| Noticing Counts | 100% Human | REVIEW | — |
| Your Body Might Need Some Love First | 100% Human | REVIEW | — |

On these eleven, every AI text fails and every Human text clears or goes to review.

That's a small set, and the thresholds were set on it, so expect misses. A CLEAR or REVIEW only means the mechanical tells weren't found; it doesn't mean the draft reads human. The linter's job is to stop an obvious failure from reaching Pangram, and to make the check happen at all. Add every new Pangram result to the calibration set and retune the thresholds if they start letting AI through.
