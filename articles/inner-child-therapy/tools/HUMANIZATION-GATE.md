# Humanization gate — run for every section, before any Pangram check or owner delivery

Added 2026-09-25, revised 2026-09-26. Joel: "how is it possible you're still not following the basic instructions to check the list of tells? can we fix that or is it hopeless?" and "you should fix UDA since the inherited UDA rules must have allowed you to avoid doing the actual rule gates that were obviously required. i shouldn't have had to tell you to do that."

**Why the checks got skipped.** From the 2026-09-24 handoff on, no record in this lane shows the repository's own blocking gates being run: the preservation proof, the architecture gate, the post-generation tell ledger and the owner-delivery admission in `SKILL.md`. Joel's corrections were collected in a separate rules file that I read at the start of a section and then drafted from memory. After each context compaction the summary I worked from named some of those rules but carried no obligation to run them, and I didn't re-read the universal bootstrap either. Nothing enforced a gate at the moment a draft went to Pangram. Some universal (UDA) defaults also read as permission to skip a declared gate when they're loaded. The fix for those is UDA pull request #260 ("Declared gates and owner-stated checks can't be waived by universal defaults"), open with its checks passing and waiting for Joel to merge it (2026-09-26).

**The fix.** This file is the lane's checkpoint of what has to run. Part of it is mechanical and has to happen in the open. No Pangram check without a linter report and a written ledger in the drafts file, and no prose goes to Joel until every gate below has passed.

## 0. Activation

After every context summary, and at the start of each new section, reload this file and the gate documents below from the repo (E46). A summary that names a rule doesn't activate it.

## Declared gates this lane must run

These come from the repository's own authority (`AGENTS.md`, `SKILL.md`, `CANONICAL-REPO-MAP.md`). They're blocking.

- **Preservation proof:** `docs/HUMANIZATION-PRESERVATION-GATE.md`. Freeze the preservation units and the change whitelist before drafting; afterwards, trace both ways with zero unexplained substantive deltas. No Pangram call before it passes.
- **Architecture:** `docs/HUMANIZATION-ARCHITECTURE-GATE.md`. Heading promise, entry and exit state, one job per paragraph, and a literal top-to-bottom proofread. Before the first Pangram call and after every detector-driven edit.
- **Post-generation tell ledger:** `SKILL.md`, "Post-generation tell ledger and repair". Every applicable tell gets a disposition on the literal candidate, covering both local wording and paragraph-level function topology (a scene that just skins the source's order still fails). The catalog is `project-sources/BANNED-PATTERNS.md`, `project-sources/STRUCTURAL-HUMANITY.md`, the `SKILL.md` sections, and Joel's corrections in `experiments/DANGEROUS-ADULT-SELF-AUDIT-RULES-20260924.md`.
- **Owner-delivery admission:** `SKILL.md`, "Humanization owner-delivery admission". Joel isn't an intermediate QA surface. Failed candidate prose stays internal unless he asks to see it, and AI-shaped wording is never a reason to ask him for his own experience.
- **Fresh-context review:** `docs/HUMANIZATION-FRESH-CRITIC-GATE.md`, whenever fresh-model evidence is used before Pangram. It never replaces the full tell ledger.

## Steps

1. **Bird's-eye (D1).**
   - Reread the source beat and list its points.
   - Search the article for overlaps and callbacks.
   - Reread a stretch of Joel's own rewrite of AI prose (E43).
   - Read only the parts of the article and the rules the section needs (E47).
2. **Preservation freeze.** Write the preservation units (what has to survive, one unit per inseparable meaning, not per sentence) and the change whitelist (what Joel has authorized: cuts, moves, research relocation). Anything not whitelisted is presumed invariant.
3. **Close the source (E42).** Write two or three lines of what I actually want to say, in what order, and why a reader would care. Draft from those lines, not from the source.
4. **Preservation trace.** Forward: every unit is in the draft, or has its authorized disposition. Reverse: every substantive thing in the draft maps to the source, an owner statement or the whitelist. Zero unexplained deltas. Fold a missing unit in as an aside or a single sentence, not a paragraph of its own.
5. **Linter.**

   ```
   python3 articles/inner-child-therapy/tools/tells_lint.py DRAFT.txt \
       --source SOURCE-SECTION.txt [--owner OWNER-LINES.txt]
   ```

   A FAIL means rewrite the draft, not tweak it, then rerun. Never send a FAIL to Pangram.
6. **Tell ledger in the drafts file.**
   - Every REVIEW item from the linter, with a disposition (KEEP, DELETE, REWRITE, MERGE, SUBORDINATE or MOVE) and why.
   - The full catalog above, including the checks the linter can't do: A1 meaning and safety, A12 referents, D2 where the draft departs from what an AI would say, E1 naming (never "the kid"), E36 details that fit every reader, E8 and E33 premises and terms not yet introduced, E29 one owner practice per section.
   - Execute the repairs, then rerun steps 4–6 on the changed text.
7. **Architecture.** Heading promise, entry and exit state, each paragraph's job, then one literal top-to-bottom read of the section in place.
8. **Pangram (E27, E37).**
   - At most about three checks per turn.
   - Test with and without the owner's lines.
   - Read results from the page text.
9. **Record and deliver.** Put the preservation ledger, the linter report, the tell ledger and the Pangram results in the drafts file. Show Joel the prose only if every gate passed; otherwise report gate status and keep working.

**Repairing a failed draft (B10, Joel 2026-09-26).** Don't fix it by swapping its phrases for less likely ones. Rewording while the structure and the other tells stay is what humanizer bots do, and it's what Pangram's "paraphrased or rewritten" flag describes. A phrase from a failed draft is judged like any other phrase, on whether it looks AI. The repair has to change what the draft says and how it's built.

## What the linter checks

- **Hard FAIL:**
  - Joel's tics;
  - coach phrases above 2 per 100 of my words (E41);
  - half or more of the paragraphs ending on a short line (B7/B13);
  - two or more paragraphs that are strings of instructions (E23);
  - three or more paragraphs with the same opener (B13);
  - second person at 9 or more per 100 of my words (E36/E41);
  - with `--source`: the AI marching order (D9), meaning 60% or more of the paragraphs follow the source's points in the source's order.
- **REVIEW** (flags for the tell ledger):
  - contrast constructions (B2);
  - finished principles (B1);
  - lines that announce a paragraph (B5);
  - individual coach phrases;
  - "kid";
  - packed or list sentences (B4/E15);
  - short knock-downs (B3);
  - short paragraph-final lines;
  - second person above 6 per 100.
- **Not checked, on purpose:** phrases shared with failed drafts. Reuse isn't a tell by itself (see B10).

The linter covers a handful of mechanical tells. It is not the tell ledger, and a CLEAR never skips step 6.

## Calibration (2026-09-25, rerun 2026-09-26 after the fixes)

Eleven texts with known Pangram 4.0 results. The files are in `tools/calibration/`.

| text | Pangram | linter | hard reasons |
|---|---|---|---|
| Borrow One Function r1 | 100% AI | FAIL | AI marching order |
| Borrow One Function r2 | 100% AI | FAIL | coach 3.3/100; landings 3/6 |
| Borrow One Function r3 | 100% AI | FAIL | coach 2.8/100; AI marching order |
| Borrow One Function r4 | 100% AI | FAIL | AI marching order (order 0.87) |
| Borrow One Function r5 | 100% AI, "paraphrased" | FAIL | landings 3/6; AI marching order |
| Music r2, my lines only | 100% AI | FAIL | second person 9.9/100 |
| Dangerous-adult H2 | 100% Human | REVIEW | — |
| Music r4 (installed) | 100% Human | CLEAR | — |
| Music r4, my lines only | 100% Human | REVIEW | — |
| Noticing Counts | 100% Human | REVIEW | — |
| Your Body Might Need Some Love First | 100% Human | REVIEW | — |

On these eleven, every AI text fails and every Human text clears or goes to review.

That's a small set, and the thresholds were set on it, so expect misses. A CLEAR or REVIEW only means the mechanical tells weren't found; it doesn't mean the draft reads human. Add every new Pangram result to the calibration set and retune the thresholds if they start letting AI through.
