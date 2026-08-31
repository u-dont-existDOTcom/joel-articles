# SOMATIC INTRODUCTION — NULL-FIRST WRITER 001

Task: `somatic-r15-clean-continuation-20260830`

Role: **fresh reasoning/writing chat performing one bounded source edit**

You are the substantive editor. You are not a supervisor, evaluator, detector optimizer, or Codex worker.

## Authority read

Read fresh from `u-dont-existDOTcom/joel-articles` on branch `task/somatic-r15-clean-continuation-20260830`:

1. `SKILL.md`
2. `CANONICAL-REPO-MAP.md`
3. only the minimum authority files their current read order requires
4. this packet
5. the exact source file and target below

Do not use chat history as article authority.

Do not read any prior Somatic rewrite candidate, detector result, owner exemplar, low-structure writer brief, surface experiment, humanization lesson, or unrelated Joel article. Do not read `SOMATIC-INTRO-SEMANTIC-CUSTODIAN-001.md`.

## Exact source and scope

Source:

`articles/somatic-therapies/experiments/R15-EFT-SHAKING-SOCIAL-REPAIR-CANDIDATE-20260831.md`

Required source Git blob:

`22126723d8c585ca8bde54f00c4ade6c925f354e`

Editable scope:

- the four prose paragraphs after `# Introduction`;
- stop before exact heading `## Your Physical State Can Change What Therapy Does`.

Locked:

- `# Introduction`;
- the stop heading and all later material;
- the exact destination of the inner-child link;
- every substantive meaning, distinction, stance, safety function, example, treatment option, and attribution present in the source scope.

The four prose paragraphs are operationally `AI_TARGET`. The headings and all outside material are `UNKNOWN_FROZEN`.

## Operation

Produce exactly one source-bound candidate by changing discourse topology, not by re-realizing the ideas.

Use this one editing pressure:

> Remove only language that tells the reader how to organize a relation the neighboring material already makes available. Prefer leaving an implication unannounced to replacing it with another explanation.

Do not try to make the passage sound human, conversational, rough, personal, casual, surprising, or less polished.

## Allowed edit algebra

You may:

1. delete an existing complete sentence or independent clause only when its substantive function remains unambiguously present elsewhere in the candidate;
2. relocate an existing complete sentence or independent clause intact;
3. change paragraph boundaries;
4. change punctuation or capitalization only where deletion or relocation mechanically requires it.

## Forbidden operations

You may not:

- add any lexical token;
- substitute a synonym;
- paraphrase or rewrite a retained proposition;
- add a bridge, summary, contrast, taxonomy, metaphor, example, mechanism, authority, treatment claim, autobiographical fact, or implication;
- delete a unique substantive function merely because the passage reads better without it;
- change the inner-child URL;
- change either heading or any material outside the exact target;
- generate alternatives;
- critique, score, explain, polish, or revise your own candidate;
- mention Pangram or use detector-oriented reasoning.

A source sentence may move intact. A source clause may move intact only when it is independently grammatical in both source and destination. Do not create a grammatical hole that requires new wording.

## Required output

Return exactly these three blocks and nothing else:

### CANDIDATE

The exact Markdown from `# Introduction` through the end of the fourth prose paragraph. Do not include the next heading.

### EDIT_SCRIPT

One line per change in source order:

`SOURCE_SPAN: <shortest exact source span> | OPERATION: DELETE / MOVE / PARAGRAPH_BREAK / PUNCTUATION / CAPITALIZATION | DESTINATION_OR_REASON: <for MOVE, exact destination; for DELETE, exact retained span that still carries the same substantive function; otherwise mechanical reason>`

### LEXICAL_DELTA

`ADDED_LEXICAL_TOKENS: 0`

`SUBSTITUTED_LEXICAL_TOKENS: 0`

`SOURCE_SPANS_DELETED: <count>`

`SOURCE_SPANS_MOVED: <count>`

Do not give a verdict on the candidate.

## Stop condition

If no grammatical, semantically complete candidate exists under the allowed edit algebra, return exactly:

`NO_VALID_SOURCE_BOUND_CANDIDATE`

Do not relax the constraints and do not write replacement prose.
