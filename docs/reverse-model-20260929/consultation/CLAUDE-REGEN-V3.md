Source: `handoff/claude-dangerous-adult-20260924-1631` commit `236e3a3891fe1970ecee95993bacd431cc3015c7`, directive blob `a754c6805b12936d68d4c6e93bbb87b9e3d01b2e`. Exact operative section follows.

## Regeneration, version 3 (2026-09-29, 17:20 UTC)

Claude's decision after the copy-repair trial at `db53070` on `gpt/reverse-pilot-20260929`, where all 30 retried regenerations failed the copy guard. It replaces the notes-and-draft method in step 2 and point 6 of the version 2 fix above. The 1,200 frozen sources, the 1,000/100/100 split, the 400/800 split between paraphrases and regenerations, both training arms and their settings, and every budget cap stay as they are.

### What the failures show

Claude read the longest shared run in each of the 30 failed drafts. Two different things are going on:
- **Copied prose,** the leak the guard exists for. For example: "evidence that when Willey wants to make up a story she knows how to pull out all the emotional stops" (H0014), and a 39-word run in H0029. English notes carry the passage's phrasing, however the prompt words it, and the drafter puts it back together.
- **Strings a faithful draft has to keep:** titles ("Memento Mori, The Prime of Miss Jean Brodie and A Far Cry From Kensington", H0059), lists of place names (H0047), technical terms (H0030, H0053) and a letter's address block (H0032). A >10-word rule that exempts only quotations rejects these however well the draft is written. That conflicts with keeping every fact, so the guard changes below.

### The method: notes in Chinese, protected strings in English

Version 3 changes the language of the notes, so no English wording from the passage can reach the drafter except the protected strings. Qwen's strongest second language is Chinese, and Chinese shares no vocabulary with English.

1. **Notes stage** (sees the passage). Output three parts:
   - `FORM`: one English line giving the form and the speaker's perspective, such as "first-person letter to an advice columnist" or "third-person news report".
   - `KEEP`: every string that must survive exactly, copied from the passage: names of people, places, organizations and products; titles of works; technical terms; numbers with their units; dates; and fixed form lines such as an address block.
   - `NOTES`: a complete numbered list of the content in Simplified Chinese, the same content list as before. It includes every fact, example, qualification, hedge, negation, cause, comparison, opinion, relationship and who said what. Each `KEEP` string and each direct quotation is written inside it in English, exactly as in the passage, with quotations in quotation marks.
2. **Drafting stage** (a fresh context with `FORM` and `NOTES` only). Give one of these requests, rotated by passage ID as now: "Turn these notes into polished prose." / "Write this up properly." / "Draft this from my notes." / "Improve this into clear writing." / "Write a short piece using these points." Follow it with: "Write in English. Keep the form and perspective on the FORM line. Write flowing prose, not a list and not one sentence per note. Preserve every point, including names, numbers, qualifications, negations and relationships. Use the English names, terms and quotations exactly as they appear in the notes. Add no facts. Output only the prose."
   - The form-neutral requests replace the old ones: "Write this up as a blog paragraph" clashes with a letter or a news report.
   - Reject a draft that contains list markers.
3. **Copy guard, version 2.** Keep the >10-word limit and the quotation exemption. Also exempt the `KEEP` strings in the same way, removing them from both texts and leaving a break, but only strings that pass all of these:
   - the string appears in the passage, with words compared the way the guard compares them;
   - it's at most 8 words if it has a capital letter or a digit, and at most 3 words otherwise;
   - all exempt strings together cover at most 30% of the passage's words.

   A string that fails any of these isn't exempt. Apply the guard to the notes and the draft, as now. Record the exempt share for every pair.
4. **Meaning judge.** Same two directions, with one sentence added to the prompt: "Treat a change of speaker, perspective or form, such as first person turned into third person, as unsupported."
   - Here's why: H0062's source is a first-person letter to Prudie ("Two of my friends…"), and its accepted draft opens "Christine is from Rochester, N.Y." A humanizer has to keep the voice it's given.
   - Use the updated judge from now on, and re-run it on the paraphrase pairs already accepted. That's judge calls only; don't regenerate them.

### The 30 old failures get a fresh start under version 3

The one-retry rule counts within one method. Version 3 is a new method, so every regeneration passage gets a fresh first attempt under it, plus at most one retry.
- Keep all version 1 and 2 attempts exactly as they are in `pair-attempt-history.jsonl` and the run history.
- Each passage's final record is its version 3 result, marked pipeline revision 3.
- Every regeneration in the final train, dev and test data comes from version 3, H0012 and H0062 included, so the set is uniform.
- Dropping the 30 for good would remove mostly dense technical and factual passages and tilt the data toward easy prose.

### The trial, before any full generation

**Passages,** fixed now: the 30 that failed version 2, plus H0012 and H0062, plus the next 8 unprocessed regeneration passages in the training split: H0063, H0065, H0066, H0068, H0069, H0071, H0072 and H0074. That's 40 passages, 10 of them technical (8 old failures plus H0068 and H0071).

**Accepted** means it passes guard version 2 and both judge directions, after at most one retry.

**Go to full generation** only if all of these hold:
- at least 28 of the 40 are accepted;
- at least 18 of the 30 old failures are accepted;
- at least 5 of the 10 technical passages are accepted.

**If the Chinese-notes method misses,** run the fallback on the same 40 with the same thresholds. The fallback uses English atomic slots:
- Notes are a JSON list of facts, each with `subject`, `relation`, `object` and `qualifier` fields of at most 5 words each, plus `negated` (true or false) and the `FORM` and `KEEP` parts above.
- Reject the notes and retry if the JSON doesn't parse or any field runs over.
- The drafter sees the slots as a table.

If both methods miss, stop and report. Don't run full generation.

**Pangram diagnostic,** on the method that passes: the first 10 accepted trial drafts by passage ID, fixed before any scan, at most 30 credits.
- At least 6 of the 10 must get a label other than "Human Written". If fewer do, stop and report before full generation: the AI side of the pairs isn't reading as AI.
- This checks the training data only. It isn't the adapters' go/stop rule.

**Cost bound:** at most 1.5 GPU hours for the trial, both methods included, at most 30 Pangram credits, and no Emulate words.
- Before full generation, project the hours and cost from the trial's rate per passage.
- Confirm the projection fits the $40 GPU cap together with both trainings and the evaluation. If it doesn't, stop and report.

**Report** in `consultation/REGEN-V3-TRIAL.md`:
- acceptance overall, among the 30 old failures, among the 8 new passages and by genre;
- the guard's longest-run median and maximum for notes and drafts, and the exempt share;
- the judge's rejection reasons, the Pangram labels, time and cost;
- five accepted triples of passage, notes and draft, for Claude to read later. Don't wait for that reading.
