# Humanization gate — run for every section, before any Pangram check or owner delivery

Added 2026-09-25, revised 2026-09-26. Joel: "how is it possible you're still not following the basic instructions to check the list of tells? can we fix that or is it hopeless?" and "you should fix UDA since the inherited UDA rules must have allowed you to avoid doing the actual rule gates that were obviously required. i shouldn't have had to tell you to do that."

**Why the checks got skipped.** From the 2026-09-24 handoff on, no record in this lane shows the repository's own blocking gates being run: the preservation proof, the architecture gate, the post-generation tell ledger and the owner-delivery admission in `SKILL.md`. Joel's corrections were collected in a separate rules file that I read at the start of a section and then drafted from memory. After each context compaction the summary I worked from named some of those rules but carried no obligation to run them, and I didn't re-read the universal bootstrap either. Nothing enforced a gate at the moment a draft went to Pangram. Some universal (UDA) defaults also read as permission to skip a declared gate when they're loaded. The fix for those is UDA pull request #260 ("Declared gates and owner-stated checks can't be waived by universal defaults"), merged 2026-09-26 at Joel's direction (e6eb98e). It also says that an inherited rule that looks unhelpful gets flagged to Joel with a suggested change, and followed until he decides.

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
3. **Write inside the organization (Joel, 2026-09-26).** Keep the order the sense needs, which is usually the source's. Don't reorder, rank, cut or move material to get past the detector (inventory T14). Keep source sentences that already read right, and rewrite the ones that don't. The human part is what gets noticed while each piece is being said:
   - the reader's obvious counterexample;
   - why the thing is true, or hard;
   - an irony inside the article's own frame;
   - a callback.

   Joel's rewrite of the Borrow opening is the model. It keeps "A complete ideal parent may be impossible to imagine" and "Borrow one function at a time from a figure who embodies it" word for word, and adds The Brady Bunch, imagination getting stamped out early, and "the adult is actually a baby when it comes to power to imagine". That last one becomes the reason to start small. Organization that's "reducible to code" (T13) is the tell, not organization itself.
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
   - **Fresh-context sweep before Pangram.** Required for every section my sentences carry (SKILL.md's owner-calibrated fresh-context tell loop; the handoff's score-blind review). Build the prompt from the numbered inventory (`docs/HUMANIZATION-TELL-INVENTORY.md`, T01–T28 and C01–C04) with `tools/build_sweep_prompt.py`, give it the previous accepted prose (and any owner paragraphs) as context and my paragraphs as the target, and send it to a fresh subagent or another fresh route. Withhold the Pangram history and my reasons. On Borrow round 6 my own ledger kept everything, the fresh sweep found T02, T09 and T12, and Pangram said 100% AI.
     **Advisory until calibrated (2026-09-26).** The fresh-critic gate lets a model sweep gate only on axes that pass known controls. The numbered-inventory sweep on this route (a fresh Claude subagent) failed its negative control:
     - it reported 10 tells on the known-Human `When Healing Turns Into Checking`;
     - it reported 7 on the known-AI Borrow round 6;
     - T02 and T09 fired on both.
     So its rows are leads for my editorial read, not blockers. The blocking check is my own disposition of each flagged span: repair the real ones (a referent slip, a packed sentence I agree with), and record the reason for the rest. Rerun the controls whenever the prompt, the model or the route changes, and let the sweep gate again only for axes that separate them.
   - **Stop rule.** If fixing one tell produces another (round 7: removing landings created six packed sentences), stop polishing. Diagnose at the level of structure, and take any change that moves or cuts preservation units to Joel.
7. **Architecture.** Heading promise, entry and exit state, each paragraph's job, then one literal top-to-bottom read of the section in place.
8. **Pangram (E27, E37; SKILL.md owner-delivery admission).**
   - Check every paragraph I wrote on its own, and then the whole section. A section can pass while one of its paragraphs is AI, which is the cheating the per-paragraph rule exists to stop (Joel, 2026-09-26).
   - Run the checks side by side in separate browser tabs.
   - At most about three rounds per turn, where a round is one set of checks on one draft. Never recheck unchanged text.
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
- **REVIEW** (flags for the tell ledger):
  - contrast constructions (B2);
  - finished principles (B1);
  - lines that announce a paragraph (B5);
  - individual coach phrases;
  - "kid";
  - packed or list sentences (B4/E15);
  - short knock-downs (B3);
  - short paragraph-final lines;
  - second person above 6 per 100;
  - with `--source`: the draft follows the source's order (D9). That's a note, not a failure. Organization is fine when the prose notices things (T13); since 2026-09-26 this is no longer a hard fail.
- **Not checked, on purpose:** phrases shared with failed drafts. Reuse isn't a tell by itself (see B10).

The linter covers a handful of mechanical tells. It is not the tell ledger, and a CLEAR never skips step 6.

## Calibration (2026-09-25, rerun 2026-09-26 after the fixes)

Eleven texts with known Pangram 4.0 results. The files are in `tools/calibration/`.

| text | Pangram | linter | hard reasons |
|---|---|---|---|
| Borrow One Function r1 | 100% AI | REVIEW (miss since D9 became a note) | — |
| Borrow One Function r2 | 100% AI | FAIL | coach 3.3/100; landings 3/6 |
| Borrow One Function r3 | 100% AI | FAIL | coach 2.8/100 |
| Borrow One Function r4 | 100% AI | REVIEW (miss since D9 became a note) | — |
| Borrow One Function r5 | 100% AI, "paraphrased" | REVIEW (miss since the "Mr." splitter fix, 2026-09-26) | — |
| Borrow One Job r6 (full gate) | 100% AI | REVIEW (miss) | none; the fresh sweep found T02, T09, T12 |
| Borrow One Competency r8e (with Joel's opening) | 91% AI, "paraphrased"; my paragraphs 5 of 6 at 100% AI | REVIEW (miss) | none |
| Music r2, my lines only | 100% AI | FAIL | second person 9.9/100 |
| Dangerous-adult H2 | 100% Human | REVIEW | — |
| Music r4 (installed) | 100% Human | CLEAR | — |
| Music r4, my lines only | 100% Human | REVIEW | — |
| Noticing Counts | 100% Human | REVIEW | — |
| Your Body Might Need Some Love First | 100% Human | REVIEW | — |

Since D9 became a note and the sentence splitter stopped breaking "Mr. Rogers" in two, the linter hard-fails three of the eight AI texts (r2, r3, music r2) and none of the five Human ones. Rounds 1, 4 and 6 only reach REVIEW. What sank them (nothing noticed, equal weight, teaching cadence, a tidy taxonomy) isn't mechanical, which is why the fresh sweep with the numbered inventory is a required step. The linter is a guard against obvious failures, not a writing guide.

That's a small set, and the thresholds were set on it, so expect misses. A CLEAR or REVIEW only means the mechanical tells weren't found; it doesn't mean the draft reads human. Add every new Pangram result to the calibration set and retune the thresholds if they start letting AI through.
