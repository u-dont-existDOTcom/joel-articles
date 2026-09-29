Source: handoff commit `07ba4f137ee29ede64379be4550bdfc985562f5b`, directive blob `476a179cf97e93decc527ab3bbc2ac80b9d257ce`. Exact operative section follows.

## Regeneration, version 4: a round trip through Chinese (2026-09-29, 18:50 UTC)

Claude's decision after both version 3 trials missed. This is the pilot's last data-generation method. **If it misses, the pilot stops** (see "If it misses" below). The 1,200 frozen sources, the 1,000/100/100 split, the 400 paraphrase passages, both training arms and their settings, and every budget cap stay as they are. The 800 regeneration passages keep their assignment, now under this method.

### What version 3 showed

- **Chinese solved the copying.** Final drafts had a median longest shared run of 7 words and a maximum of 13, where version 2 had a median of 18. And 22 of the 30 passages that copied under version 2 were accepted.
- **The notes step caused most of what was left:**
  - compressing a passage into a list lost meaning (reverse judge 7, forward judge 4);
  - the notes format failed (not in Chinese 4, no draft 4);
  - drafts were truncated at 512 tokens (2).
- **Essays did worst,** at 5 of 17. They carry voice, irony and hedges, and those are what notes flatten.
- **The English slots** failed at the JSON boundary on all 40 passages, so they say nothing about meaning.

### The method

Version 4 drops the notes. The passage is translated whole into Chinese, and a fresh context turns the Chinese into polished English. Translation keeps voice, hedges, perspective and order far better than a content list, and there's no structured output to parse. It's a different pipeline, not a further refinement of the notes prompt.

1. **Translate** (sees the passage). Prompt: "Translate this passage into Simplified Chinese. Translate everything, including hedges, qualifications, tone and who is speaking. Keep names, titles, technical terms, numbers, units, links and direct quotations in English exactly as written, with quotations in quotation marks. Output only the translation." Allow 1,024 new tokens.
2. **Language check,** mechanical:
   - remove every Latin-script run in the translation that appears word for word in the passage;
   - at least 90% of the remaining letters must be Chinese characters.
3. **Write the English** (a fresh context with the Chinese text only). Rotate these requests by passage ID: "Here's a draft I wrote. Turn it into polished English." / "Write this up in English for my blog." / "Rewrite this in clear, natural English." / "Improve this and put it in English." / "Make this read well in English."

   Follow the request with: "Keep the form, the perspective and every point, including hedges, qualifications and who said what. Keep the English names, terms and quotations exactly as they are. Add nothing. Output only the English text." Allow 1,024 new tokens.
4. **Copy guard,** version 2 as now: more than 10 shared words fails, and quotations are exempt. The exempt strings are now found mechanically instead of from a `KEEP` list: the Latin-script runs in the translation that appear word for word in the passage, under the same limits as before:
   - at most 8 words if the run has a capital letter or a digit, at most 3 words otherwise;
   - all exempt runs together cover at most 30% of the passage's words.

   Apply the guard to the translation and to the English draft.
5. **Meaning judge:** the version 3 judge, in both directions, including the sentence on speaker, perspective and form.
6. **Retries:** any failure, whether language check, truncation, guard or judge, gets one retry: a fresh translation and a fresh draft. The interrupted-call rule still applies.
7. **Label:** record the method as `roundtrip_regeneration`, pipeline revision 4.

### The trial

- **Passages:** the same fixed 40 as the version 3 trial, each with a fresh first attempt under version 4. That makes the two methods directly comparable.
- **Go to full generation** only if:
  - at least 28 of the 40 are accepted; and
  - each genre with four or more passages gets at least half: essays/journal at least 9 of 17, technical 5 of 10, practical 4 of 8, letters 2 of 4.
- **Stop early** once a threshold can no longer be met, counting only final outcomes after the retry.
- **Time cap:** at most 1 billed GPU hour, model loading included, at batch 32 or as large as memory allows.
- **Pangram diagnostic,** only if the trial passes: the first 10 accepted drafts by passage ID, fixed before any scan, at most 30 credits.
  - At least 6 of the 10 must get a label other than "Human Written".
  - If fewer do, stop: the pairs' AI side isn't reading as AI.
- **Report** in `consultation/REGEN-V4-TRIAL.md`, with the same contents as the version 3 report, plus a table comparing version 3 and version 4 on the 40 passages.

### After a go

- **Trial results:** the 40 trial outcomes become those passages' final records. The trial set was fixed before the method ran, so this isn't cherry-picking.
- **Regenerations:** generate the remaining regeneration passages under version 4, in all three splits.
- **Paraphrases:** generate the remaining paraphrase passages with the unchanged paraphrase prompt and the version 3 judge.
- **Accepted paraphrases:** these must have been re-judged with the version 3 judge before training. If that hasn't happened yet, run it now; it's judge calls only.
- **Budget check before full generation:**
  - Project the hours and cost from the trial's rate per passage.
  - Confirm that generation, both trainings and the evaluation fit the $40 GPU cap. GPU spend so far is about $5.67.
  - If the Vast balance won't cover the projection, ask Joel once for the top-up, giving the amount and the projection. Cash stays under $100.
- **Then** continue from step 3 of this directive: train both adapters, evaluate, and report.

### What carries over, and what doesn't

**Reused:**
- the frozen sources, split and method assignment;
- accepted paraphrase pairs, once re-judged with the version 3 judge;
- the copy guard's code, the version 3 judge and the pinned weights;
- the GPU fit probe;
- the 48 cached first-Emulate Pangram results and the one cached context result;
- the 7 context cases;
- the general-case selection tool, run on test pairs from this pipeline;
- the 48-credit spot check, as the record of version 1.

**Not training data:** every regeneration made under versions 1, 2 and 3 and the slot fallback. That includes the 24 accepted version 3 pairs, because version 3 missed its go threshold. Keep all of them in the history as evidence.

### If it misses

Stop the pilot. Don't try another generation method, and don't train on what exists.
- Write `PILOT-RESULTS.md` as a data-generation report: each method, its acceptance by genre, its failure reasons, the costs, and what that says about making AI-side pairs from an open 30B model.
- Leave the instance stopped. Tell Joel it costs about $0.11 an hour ($2.64 a day) in storage, and recommend destroying it: every record is on the branch, and the weights can be downloaded again. Destroying can't be undone, so it's his call.
