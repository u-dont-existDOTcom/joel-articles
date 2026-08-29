# Fresh-reader blind protocol — Romance

Status: **BLIND DIAGNOSTIC TEST.** This file intentionally contains no prior candidate questions or pilot conclusions.

## Isolation gate

Use a genuinely fresh chat/model context with **no prior Romance discussion loaded**.

For this run:

- use only this protocol and the exact canonical article chunks specified below;
- read from repository `u-dont-existDOTcom/joel-articles`, branch `main` only;
- canonical file: `articles/romance/master.md`;
- expected canonical SHA-256: `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`;
- do **not** read `ARCHITECTURE.md`, review files, current-state summaries, this experiment's sibling files, another branch, prior chat, or memory;
- stop on a master identity mismatch.

The purpose is to preserve the reader's actual information state. Do not browse ahead to answer a question before its turn.

## Reader stance

Read as an intelligent general reader who is interested in the article's actual promise and point of view. Do not act as a hostile fact-checker, therapist, sensitivity reviewer, or completeness maximizer.

At each checkpoint, record only **material live questions**: questions whose later handling could plausibly affect coherence, usefulness, section architecture, an interlink, or an explicit scope boundary.

Do not generate generic `what about X?` questions merely because a relationship topic exists.

## Sequential reveal

Fetch and read these exact line windows from `main`, **one at a time, in order**. Do not fetch a later window until you have frozen the current checkpoint output.

1. lines `1–90`
2. lines `91–180`
3. lines `181–270`
4. lines `271–360`
5. lines `361–450`
6. lines `451–540`
7. lines `541–630`
8. lines `631–720`
9. lines `721–810`
10. lines `811–900`
11. lines `901–990`

If the file has fewer than 990 lines, read through its actual end on the final available window.

## At each checkpoint

Before fetching the next chunk, freeze up to **three** questions in this schema:

```json
{
  "checkpoint": 1,
  "through_lines": "1-90",
  "questions": [
    {
      "question": "...",
      "why_live_now": "one sentence",
      "importance": "high|medium",
      "reader_mode": "curious-novice|practical-reader|personally-implicated|skeptic"
    }
  ]
}
```

A checkpoint may legitimately have zero questions.

Do not revise an earlier checkpoint because later text answers it. The point is to preserve what was live **at that moment**.

## Promise-first pass

At checkpoint 1, separately record up to eight questions reasonably implied by the article's own opening promise and scope. These are expected questions, not claims that the article must answer every one.

Use:

```json
{
  "promise_questions": [
    {
      "question": "...",
      "promise_basis": "short description of what in the opening creates the expectation",
      "importance": "high|medium"
    }
  ]
}
```

Freeze these before reading lines 91 onward.

## Final coverage pass

Only after all chunks have been read may you use the whole article in hindsight.

1. Merge semantically duplicate questions.
2. For each surviving material question, classify coverage:
   - `answered`
   - `answered-later`
   - `partial`
   - `thin`
   - `unanswered`
   - `intentionally-out-of-scope`
   - `question-rejected-by-article`
3. Name the section(s) that supply the answer or partial answer.
4. Distinguish **an unanswered question** from **an article defect**.
5. Do not propose prose yet.

Return final records as:

```json
{
  "surviving_questions": [
    {
      "question": "...",
      "origins": ["promise-first", "checkpoint-4"],
      "coverage": "partial",
      "answer_locations": ["section name"],
      "editorial_significance": "high|medium|low",
      "defect_status": "candidate|not-a-defect|unclear",
      "reason": "brief literal reason"
    }
  ]
}
```

## Anti-hallucination controls

- Do not claim a topic is absent until the final coverage pass.
- Do not infer that a question is important merely because an established relationship framework might discuss it; this test is intentionally article-internal.
- Do not recommend a new section merely because coverage is partial.
- Do not turn Joel's strong substantive positions into neutralized alternatives.
- Do not silently correct, soften, or fact-check claims.
- Do not use search-engine demand, Reddit, Gottman, PREPARE/ENRICH, RST, IBIS, or any other external framework during this blind run.

## Deliverable

Return exactly three top-level objects, in this order:

1. `promise_questions`
2. `checkpoints`
3. `surviving_questions`

No editorial rewrite and no comparison with any previous audit.

After this blind output is frozen, a separate comparison pass may inspect the experiment register and external benchmark.
