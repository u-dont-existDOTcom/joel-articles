# The reviewer-writer loop

This is the method from 2026-09-28. The reviewer's validation is in `../REVIEWER-VALIDATION-20260928.md`. Its first use, which got Also Look Outward P1 past Pangram with sense intact, is in `articles/inner-child-therapy/experiments/REVIEWER-WRITER-LOOP-20260928.md`.

Paths here are from this folder (`tools/humanization/reviewer/`), except the ones that start with `articles/`, which are from the repo root. Run the commands from the repo root.

## Files

- `rubric.txt`: what the reviewer is told about Pangram and the march, in Joel's words.
- `output_verdicts.txt`: the verdict format for judging many passages (validation, the human-prose test).
- `tickets.txt`: what a reviewer does with one draft. A verdict, then one ticket per sentence: KEEP, or FIX with the problem, an instruction, and what the reader should get from it.
- `writer.txt`: the writer's instructions. Carry out the tickets literally and change nothing else.
- `writer_draft.txt`: a first draft from the brief, for a paragraph that has no draft yet. It carries what Pangram has shown about shape, as observations, not a checklist or sentence jobs. `reviewer.py draft` also adds Joel's own before/after fixes from `../JOEL-FIXES-CATALOGUE-20260928.md`, word for word.
- `owner_bans.txt`: Joel's standing bans and cautions (from 2026-09-28). `reviewer.py` puts the whole file where the writer, ticket and draft prompts say `{bans}` (since 2026-10-03; before that the prompts held copies that fell behind).
- `sense.txt`: the cold reader's instructions. Sense only, one line per sentence. With `"earlier": "section"` in the target, it also gets what the reader has already read: the whole section before, then this section up to the paragraph before (2026-09-30).
- `dedup.txt` and `repeats.txt`: the whole-article dedup checks (2026-10-08, E151; Joel, 2026-10-07 23:18: "did you make the dedup pass before trying to humanize?").
  - `reviewer.py dedup OUT TARGET [TARGET ...] [--draft TARGET=FILE ...] [--report PATH]`: every point of each target's guide passage, and each draft sentence, against the whole article and against the other targets (SAID, PARTLY, NEW), and what's left to add. Run it before drafting, with every new group at once, and again with the drafts. Give it to an opus subagent.
  - `reviewer.py repeats OUT --article A [--focus TEXT] [--report PATH]`: every point the installed article makes twice, and contradictions.
  - Both number the article's blocks [B#], with embedded posts as bracketed notes. First run: `articles/inner-child-therapy/experiments/dedup-20261008/`.
- `grounding.txt`: the guide-grounding and logic reviewer (2026-09-29).
  - It reads the whole guide and the article up to the new text, plus Joel's rulings.
  - It rebuilds each claim against the guide, checks examples, repeats, support, logic and headings, and gives one line per sentence.
  - Since 2026-09-30 it also tests every instruction, even a faithful carry of the guide, against different readers and the article's own model of people (flag MISFIRES; `grounding-validation/RESULTS-20260930.md`).
  - Since 2026-10-01 it also tests claims carried from the guide for a missing condition (MISFIRES), flags what the guide says Joel or his people did as INVENTED unless his own words say it, checks that anything it calls covered is covered in the same sense, and gives one good-to-great proposal (the GREAT line). Blind checks: `grounding-validation/RESULTS-20261001.md`.
  - Since 2026-10-01 (turn 9) it also asks whether an example is the case most readers are in, treats an extreme case in the author's rulings as explaining his point rather than as text, and flags MISFIRES on a line that could make an ordinary reader suspect they're the bad case (v5; caught the dark-empath line 2 of 2 blind, control clean, same file).
  - Build a prompt with `reviewer.py grounding DRAFT TARGET OUT`. The target needs `guide_passage`, and can have `next`, `rulings` and `article_upto`. It reads the article's source, and the article itself unless the target has `article_upto` (see `article` and `source` below).
  - `--blind` leaves out the worked examples, for validation.
  - `--push tight|default|wide` sets how hard it pushes on the reader's open questions, and how much a fix may add (default: the target's `"push"`, else `default`). See `grounding-validation/PUSH-KNOB-20260930.md`. Questions below the level go to the article's `PARKED-READER-QUESTIONS.md` (Inner Child: `articles/inner-child-therapy/PARKED-READER-QUESTIONS.md`).
  - Its validation cases are in `grounding-validation/`.
- Targets (`*.json`): for each paragraph being worked on, the paragraph before, the paragraph after, and the meaning to keep. Each article keeps its own; Inner Child's are in `articles/inner-child-therapy/tools/targets/`. Write the meaning as bare points; writers reuse the brief's wording, and its order. Optional keys:
  - `article` and `source`: the humanized article (Markdown) and what it's made from (HTML, or Markdown or plain text), as paths from the repo root. `--article PATH` and `--source PATH` override them. Only `sense` (with `earlier`) and `grounding` read them;
  - `length`: the length line for the writers (for example "two or three sentences, 30 to 60 words");
  - `voice`: replaces "in the second person like the paragraphs around it" (for example "in Joel's first person, as his own memory");
  - `cut`: the text the article is cut after for the grounding prompt, when the paragraph before is the article's last so far; `append` adds text after the cut (a new h2);
  - `earlier`: `"section"` gives the cold reader the section before too (see `sense.txt`);
  - `push`, `rulings`, `guide_passage`, `next`: for the grounding review.
  - Write `rulings` as Joel's own words, dated and quoted. Never summarize what's his: on 2026-09-30 a P4 target said "The reflection is the guide's, in Joel's first person, about his own memory". In a blind rerun on 2026-10-01, both reviews took that as license to carry the guide's "She did not tell me I wasn't angry", which Joel says nobody knows.
- `human_items.manifest.json`: the human-prose test set, with sources and hashes. The texts go in `local/human_items.json`, which is kept out of git.
- `reviewer.py`: builds every prompt. Run `python3 tools/humanization/reviewer/reviewer.py -h`.

## The order (fastest first; Joel, 2026-09-28 16:29: "2hrs to humanize one paragraph is insane")

The reviewer is the slow step: 5 to 15 minutes a run. Writers, cold readers and Pangram each take 1 to 5 minutes. So the slow step runs only when a fast one fails:
1. Three fresh writers draft in parallel (`reviewer.py draft`). With an existing draft, skip this.
2. Run a cold sense read and a grounding review (`reviewer.py grounding`) on each draft, in parallel. The grounding review takes 5 to 10 minutes.
3. Pangram each draft that passes sense: alone if it's 50 words or more, then in the section.
4. Only if nothing passes, send the best draft to the reviewer for tickets, then the writer, then steps 2–3 again.

On the expectations paragraph this took about 20 minutes. Two of three first drafts passed sense and Pangram, and the section passed, with no reviewer run at all. Also Look Outward P1, done in the old order (reviewer rounds first, Pangram last), took about two hours.

## Running a round

```
R=tools/humanization/reviewer/reviewer.py
T=articles/inner-child-therapy/tools/targets   # the article's targets
python3 $R review DRAFT.txt $T/X.json runs/rK/review/prompt.txt
python3 $R writer DRAFT.txt TICKETS.txt $T/X.json runs/rK/writer/prompt.txt
python3 $R sense DRAFT.txt $T/X.json runs/rK/sense/prompt.txt
python3 $R review DRAFT.txt $T/X.json OUT --sense SENSE_NOTES.txt
```

The last form is for sense-only tickets.

Give each prompt its own folder, with nothing else in it. Send it to a fresh `general-purpose` subagent with model `opus`, using this wording: "Read the file … with the Read tool and do exactly what it says. That file is the only thing you may open. Don't list folders, search, run commands, open any other file, or use the web. Return only the output the file asks for." Keep answer keys out of any folder a subagent reads.

The steps:
1. Review with a fresh reviewer each round. Two in parallel is better: when their tickets differ, carry out both.
2. Write. A writer's output replaces the draft. Check only the meaning list and the facts (no invented facts about Joel, nothing extra about named people). Don't touch the style.
3. When a reviewer says HUMAN, run a cold sense read. Send its UNCLEAR notes back through `review --sense`, then write again.
4. Before a Pangram call, record the reviewer's prediction in the article's `PREDICTIONS.md` (Inner Child: `articles/inner-child-therapy/tools/PREDICTIONS.md`). Then check the paragraph alone, then the section.

## Reading the reviewer

- It's strict. Its HUMAN has been right every time so far. Its AI at 60–65, after it already calls the march broken, has twice been Pangram Human. That's the point to check Pangram, not to keep editing.
- Never tell a reviewer the Pangram result when its verdict matters. Told "100% Human", two reviewers said HUMAN 95.
- Use Opus. With the same prompt, Sonnet was near chance (32 of 53) and Fable was weaker (33 of 53).

## Re-validating

Revalidate after any change to the prompt, the examples or the model:

```
R=tools/humanization/reviewer/reviewer.py
python3 $R validation runs/val
python3 $R human-test runs/human
python3 $R score runs/val/key_testA.json ANSWERS_testA.txt
python3 $R score runs/val/key_testB.json ANSWERS_testB.txt
```

Two rules for the validation set:
- Keep versions of the same paragraph in one fold, so no reviewer is scored on a paragraph whose sibling it learned from.
- Add every newly Pangram-checked paragraph to `../calibration/`, so the examples grow.
- Not done yet: the five texts from the first loop (`PASS_outward_p1_loop_*`, `PASS_outward_section_loop_r6b`) are in `../calibration/` but not yet in `FAMILIES` in `reviewer.py`. Add them to the `outward` family at the next revalidation. They'd be that family's first Human examples.

- When the paragraphs before a draft aren't in the article yet, the reviews can't see them: the grounding reads the article up to `cut`, and the cold read gets only `before`. Give the grounding those paragraphs with `append` and put them in `before` for the cold read (2026-10-03: P5's first groundings flagged the guide's "If nothing speaks" as missing because they couldn't see P4, which carries it).
