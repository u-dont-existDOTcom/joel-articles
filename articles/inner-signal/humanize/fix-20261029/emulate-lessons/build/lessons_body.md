# What Emulate's fixes teach, from the hypnosis guide's own data

Written 2026-10-29 from the lane's records only: no new Pangram or Emulate calls. It answers Joel's question of 2026-10-29
("i wonder if we really understood all the lessons from emulate's fixes or if we can learn enough from what we got that
we wouldn't need it anymore") with the step `docs/EMULATE-FALLBACK.md` section 5 asked for and nobody did: each loud
sentence beside Emulate's replacement, described by its shape. The pairs are in `PAIRS.json` beside this file, and the
scripts that cut, check and count them are in `build/`. Paths below are relative to `articles/inner-signal/humanize/`.
Every quote is cut from the file named by a script and checked against it; a line break inside a quote is shown as " / ".

## The short answer

- **Our brief already names most of what Emulate takes out** (quips, closers, textbook definitions, colon reveals,
  "not X but Y", lists of abstract nouns). What it leaves out is **how Emulate builds what it puts in**: fewer, longer
  sentences, steps chained in one spoken sentence, things said the long way, lists kept inside a sentence, and one plain
  question where the text had framed one. Our writers do the opposite: they split into tidy shorter sentences.
- **Batch 482's recheck (read at 19:27 UTC today) shows what that costs.** Where a writer kept the flagged stretch at the
  same number of sentences, 9 of 11 read Human; where the writer split it into more, 2 of 10 did. No writer joined.
- **Emulate fails on the same shapes our writers fail on:** runs of one-command sentences, runs of same-shape sentences,
  fragment lists, options strung on "or", and "you don't have to" lines. Where its input was built on those, its output
  often kept them and read AI.
- **Much of Emulate's passing came from dropping what reads AI.** It changed meaning in {N_ME} of the {N_PASSISH} pairs
  where its version read Human, most often by dropping a qualifier, a condition, a step, a definition or a list. When the comprehension pass of
  28 October put those points back in their published shape, 8 of the 17 restorations of 10 or more words read AI on
  2026-10-29, against 1 of 8 rewrites of that size and 1 of 36 small restorations. The content Emulate dropped
  (definitions, outcome lists, label-and-colon recipes) is still unsolved by anyone but Joel.
- **Under 4.1, raw Emulate output is no longer a sure pass.** 2 of 6 raw samples read Human in the screening post of
  2026-10-22, and the one sample installed without a screen (the induction section, `fix-20261018/emu-ba`) read AI in 48
  windows of check 41r3-a, 42 of them marked "humanized" (`fix-20261020/result41/WINDOWS-41r3-a.json`). Its strong 4.1
  record is for single sentences spliced into a guide that already read Human: batches 479 to 481, 34 spots, none AI in
  the next recheck, 28 at High.

## What the data is

{N_ROWS} rows in `PAIRS.json`, from {N_BATCH} batch groups (fix-20261018 to fix-20261029):

- **{N_PASS} passing pairs**: {N_41} under Pangram 4.1 (the screening post, batches 473 to 480), {N_41W} under 4.1 where the
  old words read Human at Low or Medium and Emulate's read High (batch 481), and {N_40} under 4.0 (batches 430 to 443).
  Under 4.0 the published guide read AI almost section by section (batch 429), so a 4.0 pair says what Emulate changed
  in an AI-written passage, not which sentence was loud. The 4.1 pairs mostly have a window of their own.
- **{N_FAIL} failures**: Emulate text that read AI (raw samples in the screening post; 4.0 samples whose sibling sample of
  the same input passed; 4.0 passes that read AI in 4.1; lines that flipped with their neighbours), each with what it
  kept (`kept_or_made`).
- **{N_REV} reverse pairs**: Emulate's words read Human (High) in batch 481's recheck; the comprehension fix of 28 October
  put the published point back, often in its published shape, and read AI on 2026-10-29.
- **Our writers**: batch 482's {N_W} versions (W1 to W4, fresh, with the current brief), coded with the same labels, and
  the 21 picked versions' readings in place (`fix-20261029/b482/recheck/read/SPOTS.json`); Claude's versions of the seam
  in batch 472 (all AI, High); the comprehension rewrites of 28 October; batches 470 and 471.

Readings are the window or windows the words sit in, with Pangram's confidence and calibrated value where the result has
it. A window under about 20 words at Low or Medium is noisy: "Could you try starting a bit smaller?" read Human (Medium)
on 2026-10-22 and AI (Low) on 2026-10-23 with nothing changed in it. The labels are one coder's judgment (mine), from the
task's list plus a fixed set of "other" labels so they can be counted.

## Tallies

Each cell is how many pairs in the group show the change (a pair can show several). "Failures" counts what Emulate
changed in text that still read AI, so a change that is common there is not enough on its own.

{LABEL_TABLE}

Measures that need no judgment, from the same pairs:

{LENGTH_TABLE}

Emulate's passing text has longer sentences than its input; its failing text keeps short ones; our writers add words but
keep the sentences the same length. Failures are often lists and scripts, which have short sentences anyway.

What the failing Emulate text still had (one failure can have two):

{KEPT_TABLE}

## Against the writers' brief

The brief is the BRIEF string in `fix-20261029/b482/make_targets.py`. Several of the missing items are already lessons in
`docs/HUMANIZATION-GATE.md` (E125, E208, E223, E223 (Inner Child), E229) or tells in `docs/HUMANIZATION-TELL-INVENTORY.md`
(T02, T09, T10); the brief the writers see doesn't carry them.

### Already in the brief, and the pairs agree

- **Quips, aphorisms and closing lines out.** Emulate dropped them in 30% of 4.0 passes and 15% of 4.1 pairs, and three
  reverse pairs (`reverse-X5.3`, `reverse-X9.10`, `reverse-X1.11`) read AI once the published aphorism, joke or list came
  back.
- **No textbook definitions, colon reveals or "not X but Y".** `reverse-X8.4` ("An embedded invitation places ...") and
  `reverse-X5.3` ("Fractionation means ...") read AI (High); `reverse-X1.5` brought back a semicolon and "not a checklist".
- **Lists of abstract nouns said as people doing things.** 33% of 4.0 passes, 15% of 4.1 pairs, 24% of the writers'
  versions. It isn't enough alone: `fail-41-emu-ba-ways` made the nouns things "You might just" do and read AI.
- **Don't copy the published phrasing.** The brief says it for the flagged sentences; the comprehension pass of 28
  October didn't follow it (the numbers above).
- **Casual register.** Common in Emulate's passes (46% of 4.1 pairs), but the writers already do it in 62% of versions
  and it is in 32% of the failures. It is background, not the difference.

### Missing from the brief

**1. Keep the sentence count, or join; don't split.** The writers split in 38% of versions and joined in 5%; Emulate
joined in 22% of 4.1 pairs and 37% of 4.0 passes. Batch 482's outcome is in the writers' section below (same count: 9 of
11 Human; split: 2 of 10). The best Emulate case is controlled: the same three steps as short commands read AI three
times, and as one comma run read High.

{EX:b475-reorient|AI (Low) in three windows, recheck A3|Human (High, 0.995), recheck A4}
{EX:b481-S36|Human (Medium, 0.963)|Human (High, 0.997)}

**2. Chain the steps; never one command per sentence.** The tell inventory's T02 (instruction-manual cadence), which the
brief doesn't carry. Emulate's passes chained steps with commas, "and", "then" or "however"; its failures kept the
commands apart.

{EX:b479-S4|AI (Low, 0.754) and AI (High, 0.997), and again on 2026-10-29 with these words back|Human (High, 0.999) in two rechecks}
{EX:b475-note|Human (Medium) and AI (Medium, 0.977), recheck A3|Human (High, 0.998), recheck A4}

Against it: `fail-41-emu-ax-look` (Emulate split "Look left, right, near, and far." into two commands: AI) and
`fail-41-screen-S6-commands` (each short command its own AI window, marked humanized).

**3. Let a sentence run long.** Emulate's passing sentences are longer than their inputs (4.1: 17.4 to 19.9 words on
average; 4.0: 13.4 to 23.9); the writers' stay near 15.6. {B482_LEN} A verdict line and the sentence before it often
became one:

{EX:b481-S18|Human (Medium, 0.944) and Human (Low, 0.531); the old words read Low and AI (Medium) on 2026-10-29|Human (High, 0.998)}
{EX:b479-S2|AI (High, 0.995), and again on 2026-10-29 with these words back|Human (High, 0.999) with Human (Medium, 0.961)}

**4. Keep a list inside its sentence, and never string options on "or".** Emulate put lists in brackets or after a dash,
or made them things the reader "may want to" do, and ended an open list on a rough catch-all (the gate's E125 and E208;
the brief has neither). Two samples of one input: bd made the options things the reader may do and read Human; bc kept
the verbless "one ..., one ..., one ..." line, strung the options on "or ... or", and read AI
(`fail-41-screen-S1-metaphors`). Batch 482's two "or" chains (targets T2 and T5) both read AI (High).

{EX:screen-S2-metaphors|the published section, AI (High) in 4.0|Human (High, 0.999) in the 4.1 screening post}
{EX:40-HG04-h|AI (High), 4.0|Human (High), 4.0; its sibling emu-a kept two colon lists and read AI (fail-40-HG04-a)}

Against it: a list split into one- or two-word sentences read AI (`fail-41-screen-S6-fragments`, "Urgency. Secrecy.
Shame."), so did a list turned into ten fragment questions (`fail-41-byx`), and two examples added in brackets with
"such as" read AI (Low) (`reverse-X4.6`).

**5. Ask the question once, directly.** Where the text framed a test ("The useful question is whether ..."), Emulate asked
the reader that question. Our writers never added a question; for that sentence they wrote "It's more useful to ask
whether ..." and "Just keep an eye on whether ..." (target J4; the second read Human, High, as one long sentence).

{EX:b479-S6|AI (High, 0.996), and again on 2026-10-29 with these words back|Human (High, 0.999) in two rechecks}
{EX:b481-S26|Human (Low, 0.727), and again on 2026-10-29|Human (High, 0.999)}

Against it: a run of questions (`fail-41-byx`; the "Do you want it to be warm, or firm, ...?" pair in
`fail-41-screen-S1-metaphors`) and a question answered by the next sentence (`fail-41-emu-w-q`) read AI.

**6. Break runs, not only pairs.** The brief names "parallel pairs". The failures are runs of three or more sentences of
one shape ("If it's really X, it will Y" four times, `fail-41-screen-S5-ifrun`; "If you've X, make sure you Y",
`fail-41-emu-ax-if`). The passing versions made the members unequal or folded two into one.

{EX:40-HG29-i-daydream|AI (High), 4.0|Human (High), 4.0; its sibling emu-a kept the matched pair and read AI (fail-40-HG29-a)}

Against it: Emulate built a run of long "if" clauses inside one spoken sentence and it read High (`b474-shortcut-help`),
and `seam-bk-reverse` made a uniform run that passed in a pair check. Long, unequal clauses inside one sentence pass;
short same-size sentences don't.

**7. Don't give a "you don't have to" permission its own sentence or clause.** The tell inventory has it (T10); the brief
doesn't. Emulate's failures kept it (`fail-41-br-fix`, which read Human, AI, Human and AI in four rechecks;
`fail-41-screen-S3-active`; `fail-41-screen-S5-obey`), and so did two of batch 482's AI readings (T15, "You don't need to
fix it."; J3, "there's no need to fake it", both AI High). For the same input as `fail-41-screen-S3-active`, sample bf
turned the permission into the step:

{EX:screen-S4-active|AI, windows marked humanized, check 41r3-a|Human (High, 0.998), the screening post}

Against it: "You don't have to fake it!" read Human (High) in `b479-S5`.

**8. Say it the long way where a person would** (tentative). Most 4.1 Emulate pairs (73%) are looser than their input:
a repeated noun or verb where a pronoun would do, a filler clause, the condition said again. The writers did this in 12%
of versions; Claude's five versions of the seam in batch 472 tightened Emulate's loose input (140 words) to 110 to 124,
and all five read AI (High), while Emulate's re-run kept 143 words and read Human (High) alone. But looseness is in a third of the failures
too, and it is where most of Emulate's meaning errors came from, so it can't cost clarity (Joel's rule of 2026-10-29).

{EX:b474-shortcut-help|AI (Low, 0.879) and AI (Medium, 0.958), recheck of 2026-10-23|Human (High, 0.999), recheck A3}
{EX:b481-S20|Human (Low, 0.722)|Human (High, 0.999)}

### Where the brief and the data pull against each other

- **"Plain sentences of uneven length".** The writers read "plain" as short and neat: they split 38% of the time and
  kept the average length flat. Emulate's passes are longer and less tidy. "Uneven" is right; "plain" needs a guard.
- **"Add nothing: no new ... example".** Emulate sometimes spelled out an item already there ("without falling over" for
  "steady", `b474-stand`; "what you are expecting to get from this, a role you feel you have to play" for "what you are
  expecting, the role", `b474-trouble-fake`). Read strictly, the rule forbids that. Two cases; worth saying that saying
  an item in full is allowed.
- **"Parallel pairs"** as a blanket rule: see 6. The trigger is short, same-size members, not parallel grammar.
- **"Casual first-person asides ... where the paragraph already speaks that way".** Emulate added first person in 1 of
  41 4.1 pairs, and casual register doesn't separate passes from failures. The brief leans on surface register more than
  the data does.
- **Definitions said through what the reader does.** The brief points that way and the writers did it (T7, T9), and both
  still read AI (Low; High). Emulate passed these only by dropping the definition. No shape in this data carries a
  free-standing definition through 4.1.
- **The linter's coach-register rule (E41)** replaced two Emulate phrases that had read High (batch 480's S3a2 and S5b);
  both replacements kept reading Human, so no harm is shown.

## What Emulate's failures still had

The table above. Three to read:

{EX:fail-41-screen-S5-ifrun|the input (Claude's prose, batch 469), AI (High) as one 518-word window|AI (Medium and Low), screening post}
{EX:fail-41-screen-S6-fragments|as above|AI (Low and Medium, marked humanized), screening post}
{EX:fail-41-emu-ba-ways|published, AI (High) in 4.0|AI (Medium and High, marked humanized), check 41r3-a}

In the first, the input had already broken the parallel and Emulate rebuilt it. Joel's own Appendix C, written after this
screen, read Human (High); the gate's E223 lists what it did ("parallel tests with different verbs and lengths, the last
long and personal", "a how-to lead with its examples in brackets").

## Emulate's meaning errors

So the lessons don't carry them over. Counted on the raw samples, before the lane's fixes; ids are rows in `PAIRS.json`.

- **A qualifier, condition or step dropped** (the commonest, about 25 pairs): "only" (`seam-bj-keep`, `40-HG18-orient`),
  "automatically" (`40-HG19-believe`), "Even then" (`b479-S4`), "First" (`b474-trouble-fake`), "qualified"
  (`seam-bj-help`), "when the metaphor stops helping" (`screen-S2-metaphors`), "without forcing an answer"
  (`40-refix-HG19`), "repeating the count is not proof of a complete return" (`40-HG18-orient`), "Ask for capacity, not
  content" (`40-HG23-rule`), the five outcomes of a powerful state (`40-HG11-state`), the body's no (`40-HG12-essay`), a
  term's definition (`reverse-X5.3`, `reverse-X8.4`). Looser sentences shed exactly these small words.
- **Changed strength** (about 13): "believe none of it" with no "automatically" (`40-HG19-believe`); a warning softened
  to "sometimes the situation calls for more than that" (`40-HG26-relationship`); "things that I know work"
  (`b479-S2`); "Don't listen" for "Don't obey immediately" (`40-HG16-a`); a restriction made a permission
  (`seam-bj-keep`); "Maybe ask" for "Ask" (`b481-S29`); "of course" added (`b480-S8`).
- **Changed person, role or fact** (about 7): "the kid" became "her" (`40-HG27-kid`); the hypnotist became "he"
  (`40-HG12-outside`); "I was sober" became "I'm sober right now" (`40-HG12-sober`); sobriety stated as his reason and
  as a fact about him (`b481-S18`); his claim became his not knowing (`b479-S2`); being induced became inducing
  (`b481-S22`); requests to the inner process became requests to yourself (`b474-trouble-show`).
- **Changed or garbled point** (about 10): four separate kinds of agreement became "ways to gain someone's consent"
  (`40-HG06-consent`); the powerful-state point turned around (`40-HG11-state`); a condition attached to the wrong
  clause (`seam-bk-reverse`); "an urge to stop" lost in a garble (`40-HG19-response`).
- **Invented** (a few): "Most of these things will become easier" (`40-HG27-enemy`), "partially or fully" (`b479-S3a`).
- **Noise**: typos ("partally"), missing full stops, "in to", British spellings, slashes and ampersands. Never teach these.

The brief already says "every point, step, condition, contrast and example, with the same strength" and "Add nothing".
The data adds one warning: when a sentence is loosened or joined, carry its small qualifiers across one by one.

## Our writers beside Emulate

**What they already make**: Emulate's removals. Colon out (19% of versions), "not X" contrasts broken (21%),
definitions turned into what the reader does (17%), abstract nouns into people (24%), quips out (12%), casual register
(62%). Several versions land on Emulate's own shape for the same words, and Emulate's version of those had read High:
`b481-S32` and target T11 (Human, High), `b479-S4` and J2's v1 (the same join; v2, in the first person, was picked and
read Human, Medium), `b479-S2` and T4 (AI, High: see below).

**What they rarely make**: Emulate's constructions. Joining (5% against 22% and 37%), run-ons (2% against 15%),
loosening (12% against 73%), asides in brackets or dashes (2% against 12%; in T17 they took the brackets out), a direct
question (none), a softened instruction (none), an item spelled out (none). They split instead (38% against 20%).

**What they add that Emulate doesn't**: in batch 472, Claude's seam versions added idioms and similes ("floated up like a
balloon", "in the driver's seat", "erase it overnight") and a closing line ("Either way, today's trance ends when you come
back."). All five, and the two checked alone, read AI (High) (`fix-20261023/b472/API-CHECKS.md`); Emulate's re-run of the
same text read Human (High) alone (`seam-bj-help`).

**Batch 482 in place** (the picked version of each target, read in the candidate recheck of 2026-10-29; codes from
`build/writers.py`):

{B482_TABLE}

Two that kept one sentence and read High, and two that split and read AI:

{B482:T3|its earlier Emulate version (emu-a) dropped this sentence altogether (40-HG12-outside)}
{B482:J4|Emulate's version, a direct question, read High twice (b479-S6)}
{B482:T4|Emulate's version, two sentences with a dash aside, the examples in brackets and the disclaimer folded into the second with "even though", read High twice (b479-S2)}
{B482:T6|Emulate's version had no examples (reverse-X4.6)}

**Batches 470 and 471** were naming and clarity edits inside Emulate's text (Joel's answers 9 to 12), not humanizing
rewrites: all 23 that were scored read Human in place on 2026-10-22, a few with a Medium or Low window
(`fix-20261022/b470/batch/SCORE.md`, `fix-20261022/b471/batch/SCORE.md`). One of them, the parent-script definition ("This is the set of rules ..."), read AI (Low and
Medium, marked humanized) three days later, and Emulate's version replaced it (`b480-S9`).

**The comprehension rewrites of 28 October**: of 83 rewrites in the paragraph's own words, 70 read Human (High) and 2 AI
on 2026-10-29; 9 of the 11 AI readings among those fixes came from restoring published wording.

## A block for the writers' brief

Eleven lines, each a shape rule. Under "What reads human", after the current list:

- Keep the flagged stretch at the same number of sentences, or fewer: join it to its neighbour before you ever split it into shorter, tidier ones.
- Chain steps: put two or three steps in one spoken sentence joined by commas, "and" or "then"; a run of one-command sentences reads AI however plain each one is.
- Let at least one sentence run long, carrying the condition, the step and the reason together, beside a short one.
- Keep a list inside its sentence, as things the reader may do or in brackets or after a dash, ending an open list on a rough catch-all; never one- or two-word sentences, and never options strung on "or ... or".
- Where the text frames a test ("the useful question is whether ..."), ask the reader that question directly, once; no runs of questions, and no question the next sentence answers.
- A run of three or more sentences of one shape reads AI whatever words fill it: make the members unequal in length and build, or fold two into one.
- Don't give a "you don't have to" permission its own sentence or clause: fold it into the step it qualifies ("Instead of X, try Y").
- When a published point has to come back (a definition, a list, a caveat, a joke), add it in the paragraph's own shape, never as the published sentence or its colon, definition or closing line.
- Don't make a rewrite sound casual with new idioms, similes or a wrap-up line.
- When joining or loosening a sentence, carry its qualifiers across one by one (only, first, even then, automatically): they are what Emulate dropped.
- Where a person talking would repeat the noun or verb, repeat it rather than compress to the tightest clause, as long as it stays clear on a first read.

## How sure, and what is thin

- **Fairly sure** (several cases each way, some controlled): lines 1, 2, 6, 7 and 8. Line 1 rests on batch 482 (9 of 11
  against 2 of 10) and the reorientation lines (split: AI three times; joined: High); line 8 on 136 checked comprehension
  fixes; line 7 on five AI readings, two of them our writers', against one pass.
- **Moderately sure:** lines 3, 4, 5 and 9. Line 3's lengths are confounded with content (lists and scripts have short
  sentences); line 4 has a controlled pair, batch 482's two "or" chains and one counter-case (`reverse-X4.6`); line 5
  rests on two passes and three failing counter-shapes; line 9 on Claude's five versions of one stretch.
- **Tentative:** lines 10 and 11. Looseness is everywhere in Emulate's output, failures included, and it costs meaning.
- **Unsolved by these lessons:** free-standing definitions (T7, T9, `reverse-X5.3`, `reverse-X8.4`), outcome lists (T2,
  `reverse-X1.11`), label-and-colon recipe lines (T17, `reverse-X11.13`), the hypnosis audit he keeps as a list. Emulate
  passed these only by dropping them; Joel's own rewrite of Appendix C is the only passing model.
- **Thin data:** most 4.1 Emulate evidence is one or two sentences spliced into a guide that already read Human, a kind
  context; batch 482's targets were the hard residue, so the two sets aren't a fair race. Short windows flip with their
  neighbours (`fail-41-emu-bf-ones` read High three times, then AI when the sentences around it changed). 4.0 passes
  don't carry over to 4.1. One article, one coder, no blind second coding. The reverse pairs mix shape with content: a
  restored definition may read AI because definitions do, whatever shape carries them.

## For the question of re-upping Emulate

The data supports a narrower use, not none. Its raw output now fails 4.1 often, it bends meaning in most pairs, and much
of its passing came from dropping the content that reads AI, which Joel's clarity rule won't allow. What still worked in
4.1 was the re-run of text that read AI and the swap of single red sentences inside a section that already read Human.
The build lessons above (keep the sentence count, chain, keep lists inside sentences, one direct question) are what our
writers can copy now; batch 483 is the test of whether they close the gap. Emulate's balance was 0 words on 2026-10-29
(`fix-20261029/b482/make_targets.py`).
