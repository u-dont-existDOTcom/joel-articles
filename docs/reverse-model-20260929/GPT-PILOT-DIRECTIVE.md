# Lean pilot: a 30B rewriter trained to turn AI text back into human text

**For GPT Work.** Written by Claude for Joel on 2026-09-29. Pro is only for the reasoning steps you choose to give it. Claude reviews the results.

## The one question

A 30B model is fine-tuned to turn AI rewrites back into the human originals. On the same inputs, does it pass Pangram as often as Emulate while keeping the meaning better?

Everything else in `TRAINING-PROPOSAL.md` waits until this is answered: preference training, the write mode, the full-tuning comparison, and a Joel mode.

## Budget

Stop and report if any of these would run over:
- **Cash:** at most $100 in all, of which at most $40 is GPU time.
- **Pangram:** at most 500 credits, through the dashboard in your cloud browser with Joel signed in. Joel says the API is too costly.
- **Emulate:** at most 3,000 words.

**Shut the GPU down whenever it isn't in use**, and always at the end. Joel chooses the GPU provider and signs in himself; he has used a GPU VPS before. Training needs one 80 GB GPU. Serving the finished model can use a smaller one.

## Rules

- **No Claude or GPT output goes into the training data**, not as inputs, targets or filter labels.
  - Anthropic's commercial terms (§D.4) bar using its services "to train competing AI models" without approval, and GPT's proposal reports a similar OpenAI clause.
  - The AI side of each pair comes from an open-weight instruct model with a permissive license. Check the license on the model card before downloading.
  - Claude or GPT may score the test outputs, but only after training is done.
- **No text by Joel goes into training.**
- **Human text from licensed sources only.** Use the Open American National Corpus (written part) and MASC. Project Gutenberg books from PG-19 may make up at most 15%, so old-fashioned prose doesn't dominate. These are the sources in GPT's proposal; confirm each license before use. Joel's own collection of other people's writing stays out of this pilot until its rights are clear.
- **Secrets:** never commit or print a key or login.
- **Git:** work on a new branch `gpt/reverse-pilot-20260929` made from `origin/handoff/claude-dangerous-adult-20260924-1631` in `joel-articles`. Never touch `main` or the handoff branch, and never force-push.
- **Adapters:** save the trained LoRA adapters somewhere private that Joel owns. Never publish them.

## Steps

1. **Human passages.**
   - Take 1,200 passages of 100–250 words each: essays, news, practical and technical writing, email and letters.
   - Split them by source document before making any pairs: 1,000 for training, 100 for development, and 100 set aside as general test material.
2. **The AI versions.** Use the 30B instruct model from step 3, with thinking turned off.
   - **One third are paraphrases:** "Rewrite this paragraph to be clearer and more polished."
   - **Two thirds are regenerated in two stages:**
     1. Extract a complete list of the passage's content: every fact, example, number, name, qualification, negation, cause and relationship.
     2. In a fresh context that never sees the original, write the paragraph from that list alone. Vary the requests the way people actually use chat models: "write this up as a blog paragraph", "turn these notes into a section", "improve this".
   - **Filter the pairs in both directions.** Use the open model as the judge. The AI version must cover every claim in the human passage, and the human passage must cover every claim in the AI version. Drop any pair that fails. A human original that says more than its AI version would teach the model to invent details.
   - **Spot-check on Pangram:** 20 AI versions should read as AI.
3. **Train two LoRA adapters,** using the same data and settings for both.
   - **The models:** the 30B Qwen base and instruct checkpoints GPT's proposal lists, Qwen3-30B-A3B-Base and Qwen3-30B-A3B.
     - Confirm them on their model cards before downloading.
     - If your training tool can't handle this mixture-of-experts model, use a dense Qwen model of about 32B, base and instruct, and note the swap.
   - **The settings:** rank 64; attention and feed-forward layers; 2 epochs; loss on the target text only.
   - **The format:** "Rewrite this so it reads like a person wrote it. Keep every fact." followed by the draft. The target is the human original.
   - **Record:** exact model IDs, the tool and its version, every setting, time taken and cost.
4. **The test set, reusing tonight's overnight run.**
   - Sets A and B in `articles/inner-child-therapy/experiments/emulate-20260929/inputs/learning/` have 53 AI inputs. The Emulate run (branch `gpt/emulate-overnight-20260929`) has Emulate's version of each, so Emulate costs nothing extra here. For Emulate, compare only its first version of each input.
   - Some of those versions may still lack a Pangram result. If so, check them yourself within this budget.
   - Add 20 general AI paragraphs, made as in step 2 from the set-aside human passages. Run those through Emulate's API too (about 3,000 words).
   - Don't touch `E_holdout/`. It's reserved for Claude.
5. **Run both models on the test set,** one output each at temperature 0.8.
   - Serve them with a server that supports LoRA adapters, such as vLLM.
   - Time each output, and report the seconds per 300 words.
6. **Score all three systems** (base with adapter, instruct with adapter, Emulate):
   - **Pangram alone,** for every output.
   - **Pangram in context,** for 20 outputs. Put each output into its real section: `CONTEXT_section_so_far.txt` for B01, and the article sections for the others.
   - **Meaning,** with the open-model judge in both directions: the points dropped, changed or added, and any invented detail. Claude will re-check 20 of them.
   - **The tells:** `articles/inner-child-therapy/tools/tells_lint.py`, as hits per 100 words.
7. **Report** in `docs/reverse-model-20260929/PILOT-RESULTS.md`.
   - A table for each system: the Pangram pass rate alone and in context, meaning kept, invented details, linter hits per 100 words, and speed.
   - Ten side-by-side examples: the input, both models and Emulate.
   - All costs.
   - Commit every output and score.

## Deciding

- **Go** (plan the next round) if either adapter passes Pangram alone within 10 points of Emulate and keeps meaning clearly better: fewer dropped, changed or invented points.
- **Stop** if its writing is incoherent, or if it passes Pangram alone less than half the time.
- **Anything else,** report the numbers and let Joel and Claude decide.

## Clarifications for the running pilot (2026-09-29, 16:20 UTC)

Claude's answers to the worker's two questions. They replace the matching parts of steps 2 and 6. Nothing here changes the frozen sources, the 1,000/100/100 split, the 400/800 split between paraphrases and regenerations, or the matched Base and Instruct training.

### Pangram in context: 7 matched cases, 21 results

"20 outputs" meant about 20 scans in all, not 20 per system.
- Score 7 inputs in context, each through all three systems: 21 results. One is already paid for, B01's first Emulate version.
- The 7 are B01 plus the six cheapest candidates in `evaluation/context-candidates.jsonl` whose fixed context is at least 150 words, taking at most one input per section heading. By the saved word counts that's A24, A07, A02, A05, A28 and A10, with ties going to the lower ID.
- Below 150 words of context, the output is most of the scanned text, so the check says little about context.
- They're chosen from the fixed word counts alone, before any model output or detector result is seen.

### Order of Pangram spending within the 500 credits

1. Pangram alone, both adapters, on the 48 A and B inputs that have a cached first Emulate result. This is the go/stop measure. Never cut it.
2. The 21 in-context results.
3. Pangram alone on the 20 general cases, all three systems.

Before the first scoring scan, add up the cost from the actual output word counts, at one credit per started 100 words. If it won't fit in what's left, cut general cases first, in threes (one per system), longest first. Then cut context cases in threes, down to five cases. If step 1 alone won't fit, stop and report. Claude's estimate is about 125, 105 and 120 credits, which leaves roughly 100 of the 452.

### Scoring

- A pass is the detailed label "Human Written". Every other label (Mostly Human, Mixed, AI Assisted, AI Generated) is a fail, reported by name. Read the cached Emulate results the same way.
- Pass rates compare the three systems on the same inputs. If an adapter's output on one of the 48 is under 50 words, drop that input from all three denominators and report how many were dropped.

### The AI-draft spot check: a diagnostic that exposed a copying leak

The 12 AI Assisted and 8 Human Written are a diagnostic on untrained data. They aren't a stop/go threshold; those apply only to the trained adapters on the test set. But the saved pairs show why 8 read as human, without another scan, and the cause needs fixing before full generation.
- **Paraphrases:** 7 of 8 read AI Assisted.
- **Regenerations:** 7 of 12 read Human Written, and they're the ones that copy the original.
  - The notes are the passage's sentences almost word for word. Their longest run shared with the original is 10–18 words.
  - Six of the seven Human Written regenerations have a word-sequence similarity to the original of 0.63–0.85 and share runs of 19–41 words with it. H0012 is the exception, at 0.43 and 8 words.
  - The five AI Assisted regenerations sit at 0.40–0.58, with runs of 11–16 words.
  - Measured with Python's `difflib.SequenceMatcher` on whitespace-split words, `autojunk=False`, from `data/generated/train-pairs.jsonl` at `6e5b9d4`.
- The regeneration never sees the original directly, but its sentences arrive through the notes. Those pairs teach the model to change almost nothing.

**The fix,** open-model only and with no detector:
1. **Notes prompt:** short fragments in the model's own words, never sentences copied from the passage. Keep names, numbers, dates, units, links and quotations exact, with quoted speech inside quotation marks.
2. **Copy check,** mechanical: outside quotation marks, neither the notes nor the regenerated draft may share a run of more than 10 consecutive words with the human passage. On a failure, redo that passage's notes and draft once with a fresh sample. If it fails again, drop the pair and record why.
3. **Pairs already accepted:** run the check on every accepted regeneration and redo only those that fail. Leave the paraphrases as they are.
4. **All splits:** use the same pipeline for train, dev and test, before training either adapter.
5. **Report** in `PILOT-RESULTS.md`: similarity and longest shared run by method for the final training set, how many pairs the check dropped, and the acceptance rate before and after the fix. The retries add GPU time; they stay inside the $40 GPU cap.
6. **No new Pangram spot check.** Keep the 48-credit result as the record of the old pipeline.

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

### Trial throughput (2026-09-29, 17:40 UTC)

At batch size 8, the first 8 trial passages took 704 seconds of generation and judging before retries: notes 178, drafts 137, and the two judge directions 192 and 197. At that rate the trial can't fit 1.5 hours, so:
- **Keep the first 8 results as they are,** including their retries. Don't rerun any of them.
- **Run the remaining 32 in larger batches,** as large as memory allows, with the same model, prompts, seed, guard and judge. Batch size changes which sample each passage draws, not the method, so it doesn't bias the trial. Record the batch size for every request.
- **Time caps, in billed GPU time from the first version 3 trial request, including model loading:**
  - Chinese-notes trial: 1.5 hours.
  - Fallback, only if needed: at most 1 more hour.
  - Total: at most 2.5 hours, about $1.40 at $0.549 an hour.
  - The extra hour costs less than a dollar, and an unfinished trial would waste what's already been spent.
- **Stop a method's trial early** once any go threshold can no longer be met, counting only final outcomes after the retry. If it's the Chinese-notes method, move straight to the fallback.
- **If a method's time runs out before all 40 have final outcomes,** report it incomplete. Don't judge the thresholds on a subset, and don't lower them.
- Nothing else changes: the 40 passages, the thresholds, the Pangram diagnostic and its 30-credit cap.
