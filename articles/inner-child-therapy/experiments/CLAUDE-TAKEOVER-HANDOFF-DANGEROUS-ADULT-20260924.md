# Claude takeover handoff — Inner Child dangerous-present-adult H2

Date: 2026-09-24
Status: **ACTIVE WRITER HANDOFF / CLAUDE PRIMARY WRITER**

## Active gates for this lane (added 2026-09-26; read this first after any context summary)

The lane has moved past the dangerous-adult H2 and now humanizes the article section by section. Every section, before any Pangram call and before any prose goes to Joel, runs `tools/HUMANIZATION-GATE.md`:

- the repository's declared gates: the preservation proof, the architecture gate, the post-generation tell ledger, and the owner-delivery admission in `SKILL.md`;
- Joel's own corrections, in `experiments/DANGEROUS-ADULT-SELF-AUDIT-RULES-20260924.md`;
- the linter, `tools/tells_lint.py`.

Two lines below are superseded for this lane (Joel, 2026-09-25 and 2026-09-26):

- "Do not add another anti-pattern blacklist." Joel's list of tells is an owner-derived checklist and runs as a gate. It isn't a writer prompt: it's applied after drafting, as `SKILL.md` already says.
- "Follow its routing only as needed for this task." UDA's root `AGENTS.md` is re-read on every turn, and the gates above are never trimmed as "not needed".

## Owner outcome

Produce a faithful, genuinely human-sounding replacement for the new Inner Child Therapy H2:

`## When the Present-Day Adult Is Dangerous to the Child`

The exact H2 itself must pass unpaid editorial/preservation review before another Pangram call. Do not resume the old whole-section polishing loop.

Joel explicitly asked to hand primary generation/reasoning to Claude. Claude should use GPT/Codex only as a **fresh independent reviewer** at useful checkpoints, not as a co-writer and not as fake same-context independence.

## Writer lane

Work only on:

`handoff/claude-dangerous-adult-20260924-1631`

Base:
- parent progressive branch: `chat/inner-child-dangerous-progressive-20260924-1624`
- base SHA: `2ff49dd1668a585a3c2dc18f0291790028f99d01`

Do not mutate:
- `main`;
- `task/inner-child-therapy-intake-20260915`;
- any previous ChatGPT writer branch;
- Pangram evidence branches except through the approved runner when/if a paid call later becomes eligible.

If this branch moves unexpectedly from another writer, stop mutation, reconcile the diff, and create a new child branch before continuing.

## Mandatory bootstrap

Before substantive reasoning:

1. Read live default-branch `u-dont-existDOTcom/universal-dev-architecture/AGENTS.md`.
2. Follow its routing only as needed for this task.
3. Read live default-branch:
   - `u-dont-existDOTcom/joel-articles/SKILL.md`
   - `u-dont-existDOTcom/joel-articles/CANONICAL-REPO-MAP.md`
4. Then read the current registered Inner Child authority:
   - `articles/INDEX.json`
   - `articles/inner-child-therapy/CURRENT-STATE.md`
   - `articles/inner-child-therapy/OWNER-LOCKS.json`
   - `articles/inner-child-therapy/SOURCE-UPDATE-HUMANIZATION-RECONCILIATION-20260920.md`
5. For detector/humanization method, read fresh:
   - `u-dont-existDOTcom/pangram-humanization-lab/README.md`
   - `u-dont-existDOTcom/pangram-humanization-lab/state/WORKING-LESSONS.md`

GitHub is canonical. Do not infer current authority from chat summaries or filenames.

## Minimum task-specific files to read

On the handoff branch, read:

1. `articles/inner-child-therapy/experiments/DANGEROUS-ADULT-PRESERVATION-COMPRESSION-AMENDMENT-20260924.md`
2. `articles/inner-child-therapy/experiments/DANGEROUS-ADULT-CANDIDATE-I-CHAT0140B-20260924.md`
3. `articles/inner-child-therapy/experiments/DANGEROUS-ADULT-CANDIDATE-I-H2-PANGRAM-RESULT-20260924.md`
4. `articles/inner-child-therapy/experiments/DANGEROUS-ADULT-CANDIDATE-I-H2-POSTRESULT-DIAGNOSIS-20260924.md`
5. `articles/inner-child-therapy/experiments/DANGEROUS-ADULT-PROGRESSIVE-PREFIX-Y2-20260924.md`

Do **not** read every historical dangerous-adult candidate before writing. The old context is saturated and the task is to escape the same realization family.

## Exact detector evidence

Candidate I H2 alone was tested correctly after the boundary-selection bug was fixed.

Exact H2:
- SHA-256: `097283751ace490138ceb9773c6d25b97abb0f400c1b9043813cf8ea7ff8f01d`
- local whitespace words: 444

Pangram 4.0:
- AI: **1.0**
- Human: **0.0**
- AI-assisted: **0.0**
- AI likelihood: **0.9992636442184448**
- one single high-confidence window covering the entire H2

This is not a neighbor-contamination result. Candidate I itself is detector-red.

No duplicate/repeat call is allowed on Candidate I.

## What the score-blind diagnosis found

A fresh Claude context that did **not** see Pangram found the key remaining defect:

### Section-scale coverage + closure

Candidate I still behaved like a safety specification:
- each paragraph covered a different complete requirement-set;
- lists were exhaustive/coverage-driven rather than incidental;
- every paragraph ended by closing a rule or boundary;
- semantic work was unusually equalized;
- polished significance/linking sentences announced what mattered;
- the source-function ledger remained visible through the prose.

The strongest line of reasoning to preserve from Candidate I:

> A frightened reaction only tells you the child is frightened, and if that fear is rewarding to the adult, using the child as a test has already become part of the harm.

Other useful human-facing properties:
- direct spoken register;
- `don't bring the child forward to find out what happens`;
- `Whatever brought you here is still there`;
- `theology fight`;
- the counterintuitive point that calm/present adult capacity does not equal safety.

Do **not** preserve Candidate I's paragraph topology merely because some sentences are good.

## Preservation authority

Use `DANGEROUS-ADULT-PRESERVATION-COMPRESSION-AMENDMENT-20260924.md` as the controlling realization contract.

Eight core claims must remain explicit:

1. Adult capacity/presence is not sufficient when present protective intent is absent.
2. Current endorsement/intent to frighten, humiliate, exploit, or harm vulnerability blocks child contact.
3. The child is not a diagnostic test of adult safety; fear/reaction cannot become gratification.
4. While harmful intent remains, work stays with the present-day adult rather than the child.
5. Beliefs/thoughts/history alone are not the gate; present endorsement and intent are.
6. A verbal promise alone does not establish safety; repeated non-harmful behavior matters.
7. Direct and indirect child-contact routes remain blocked while harmful intent remains.
8. Continued care is allowed without assisting exploitation, and some people may need sustained real-human care.

The following may be compressed/implicit-equivalent rather than inventoried:
- adult-focused inquiry into what the person wants changed and whether the stance serves the life they want, including effects on self/others;
- sovereignty as practical ability to disobey/reconsider/change course under urge/claimed authority;
- beliefs/religion, unwanted thoughts/feelings, and past wrongdoing as insufficient by themselves;
- care/listening without validating or assisting harm; beliefs do not have to be settled;
- proxy/imagined routes as indirect child contact.

Do not turn these back into one sentence per requirement.

## Current progressive prefix

Current best prefix Y2:

> ## When the Present-Day Adult Is Dangerous to the Child
>
> The last check was about whether enough of the adult is here. This one is about which side that adult is on. Maybe the heading makes you think of every ugly thought you've ever had; that's not what I mean. An unwanted thought or feeling, a belief, or something you did before can matter without being what you stand behind now. And if you honestly don't know which side you're on yet, the child is not how you find out.
>
> If you bring the child forward to see whether you're safe, a frightened child still only tells you the child is frightened. It can't tell you that you're safe. And if part of you wants that fear, the test isn't finding anything out; it's getting what it came for.

Y2 is **not owner-final**. It is a promising progressive prefix and may be kept, edited, or replaced if fresh reasoning finds something materially better.

## Recommended architecture

The best current architecture is a causal chain, not coverage.

The first live pressure:
> The reader may have passed the readiness/capacity test, but what side is that adult actually on?

The second live pressure:
> If the child cannot be used as the test, what would actually show that the adult has changed?

That second question should generate the remainder:
- inner contents do not answer it reliably;
- a promise does not answer it;
- behavior over time under the relevant temptation gives actual evidence;
- sovereignty becomes practical ability to refuse/change course;
- the child/proxy routes are excluded because they recreate the invalid test;
- care continues while the answer remains open;
- some people may need sustained real-human care.

Do not make each of those a separate policy beat. Each should arise because the previous answer fails or creates the next question.

## Method to use

Prefer **progressive forward construction** over another whole-section generation.

1. Start from Y2 or a better fresh prefix.
2. Generate/reason only the next natural beat.
3. Ask: what question does the current prose genuinely leave alive?
4. Add only the beat that answers/complicates that live question.
5. Freeze a prefix only if:
   - preservation remains recoverable;
   - the new beat does not visibly correspond to “the next source requirement”;
   - deleting the beat would make the following thought lose its reason to exist.
6. Continue until the thought naturally stops.
7. Only then run whole-H2 preservation and score-blind editorial review.

Do not allocate sentence jobs from the source ledger.

## Claude's role

Claude is the **primary writer and reasoning engine** for this lane.

Use Claude's own context for:
- architecture;
- next-beat reasoning;
- drafting;
- preservation-aware revision.

But do not treat Claude's same-context self-critique as independent evidence.

## GPT/Codex review loop

At meaningful checkpoints, use a genuinely fresh GPT/Codex CLI session if the local authenticated subscription CLI is available.

Use GPT/Codex for **review only**:
- literal preservation check;
- score-blind coverage/closure check;
- reader-purpose/why-now/referent review;
- final fresh-reader diagnosis.

Give the reviewer:
- literal candidate;
- minimum surrounding article context;
- preservation contract;
- exact review question.

Withhold:
- Pangram score unless the review task specifically requires detector-result interpretation;
- Claude's defenses/rationale;
- rejected alternatives;
- hidden target labels.

Do not tell GPT/Codex to pretend it has not seen material already in its context. Independence requires a genuinely fresh CLI session.

If GPT/Codex CLI is unavailable, do not fake independence. Joel can bring the exact candidate back to the ChatGPT thread for review.

Reviewer output is diagnostic evidence, not edit authority. Claude decides what to change subject to preservation and owner authority.

## Required score-blind review before Pangram

A complete candidate must survive a fresh reviewer that does **not** know Pangram.

Ask specifically whether the H2 still shows:
- closed coverage taxonomies;
- paragraph-by-paragraph requirement coverage;
- repeated rule-closing endings;
- equalized semantic efficiency;
- specification/policy topology;
- generic therapeutic abstraction;
- polished significance/bridge statements;
- source requirements visible through the prose.

Also require the reviewer to identify at least some functional Human-facing properties.

If the reviewer can still name a section-scale blocking defect, **do not call Pangram**.

## Detector boundary rule

The workflow bug has been fixed canonically on `main`:

- editorial/fresh-reader review may use natural surrounding context;
- first Pangram certification tests the **smallest complete changed model-written unit itself**;
- for this task that means **H2 alone**;
- known-bad neighboring prose must not contaminate the first certification call.

Do not Pangram the readiness + H2 + next-section boundary as the first test.

## Pangram discipline

Do not call Pangram until:
- preservation PASS, zero unexplained substantive deltas;
- whole-H2 score-blind editorial review has no blocking defect Claude/GPT actually endorses;
- the H2 has at least some genuine Human-facing properties;
- exact H2 SHA is frozen;
- cache/History check is clear.

Then:
- run exactly one guarded Pangram GUI call on H2 alone;
- preserve exact model/version/SHA/result/history identity;
- if AI/Mixed, do not immediately repeat;
- first run a score-blind diagnosis of the exact failed H2, then change architecture only if a concrete defect is found.

## Do not do

- Do not keep rewriting Candidate I sentence-by-sentence.
- Do not add another anti-pattern blacklist.
- Do not make prose intentionally sloppy just to imitate a person.
- Do not invent anecdotes, fake specificity, memories, dialogue, chronology, diagnoses, motives, or factual claims.
- Do not drop meaning to satisfy Pangram.
- Do not let preservation become a sentence checklist.
- Do not use Jev ABSENT as clearance.
- Do not treat Pangram as authorship or quality authority.
- Do not ask Joel for rough cognition merely because wording remains model-shaped; the source already represents his cognition and he approves the thought.
- Do not spend Pangram on knowingly incomplete probes.

## Current stop condition

The owner outcome is still OPEN.

Claude should continue autonomously until one of these is true:

1. A complete H2 passes preservation + score-blind editorial/fresh-review gates and is ready for one H2-only Pangram call; then run the authorized guarded call.
2. A Pangram result is obtained and preserved; continue according to the production protocol.
3. A genuine owner-only tradeoff is reached about meaning, not execution mechanics.
4. A real access/authentication/spending/platform gate blocks the next action.

Do not stop merely because one candidate failed or because a local method stalled.

## Reporting back to Joel

Keep progress concise. Report:
- current candidate/prefix identity;
- preservation status;
- strongest remaining defect, if any;
- independent GPT/Codex review result when used;
- Pangram only after eligible and actually run;
- what changed in GitHub.

Do not show failed candidate prose unless Joel asks.
