# Fresh-reader blind protocol — Romance (Pro reader stage)

Status: **BLIND DIAGNOSTIC TEST / READER STAGE ONLY.** Source collection is a separate mechanical stage governed by `COLLECTION-PROTOCOL.md`.

## Isolation gate

Use a genuinely fresh Pro/model conversation with **no prior Romance discussion loaded**.

For this run:

- do **not** access GitHub, the web, files outside the current conversation, prior chats, memory, or external frameworks;
- do not use tools to retrieve the article yourself;
- do not ask for or accept the complete source, a ZIP containing all windows, the future-window manifest, `ARCHITECTURE.md`, review files, current-state summaries, sibling experiment files, or prior audit results;
- use only this protocol plus the source windows the human/controller reveals sequentially in this conversation;
- do not request a later window until the current checkpoint has been frozen.

The purpose is to preserve the reader's actual information state. An unrevealed window must be genuinely unavailable to you, not merely something you promise not to inspect.

## Reader stance

Read as an intelligent general reader who is interested in the article's actual promise and point of view. Do not act as a hostile fact-checker, therapist, sensitivity reviewer, or completeness maximizer.

At each checkpoint, record only **material live questions**: questions whose later handling could plausibly affect coherence, usefulness, section architecture, an interlink, or an explicit scope boundary.

Do not generate generic `what about X?` questions merely because a relationship topic exists.

## Sequential reveal contract

The controller will provide one immutable source window at a time in order. Windows were collected mechanically from the canonical Romance master in 90-line source chunks.

When you receive a window:

1. read only the material currently available in the conversation;
2. freeze the checkpoint output before the controller reveals another window;
3. do not revise prior checkpoints after later text arrives;
4. do not claim a topic is absent until the final coverage pass;
5. do not propose edits or new prose.

A checkpoint may legitimately have zero questions.

## Promise-first pass

On **window 1 only**, before any later window is revealed, separately freeze up to eight questions reasonably implied by the article's own opening promise and scope. These are expected questions, not claims that the article must answer every one.

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

Do not revise this list after later windows are revealed.

## Checkpoint output

After each window, freeze up to three material live questions using:

```json
{
  "checkpoint": 1,
  "through_window": 1,
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

For window 1, return `promise_questions` first and the checkpoint object second. For intermediate windows, return only the checkpoint object.

The controller will then provide the next window.

## Final coverage pass

When the controller explicitly states that the final window has been revealed, you may use everything accumulated in this conversation in hindsight.

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
- Do not infer future content from headings or summaries that the controller has not yet revealed.

## Final deliverable

After the final coverage pass, return exactly three top-level objects, in this order:

1. `promise_questions` — reproduce the frozen window-1 object unchanged;
2. `checkpoints` — reproduce all frozen checkpoint objects in order, unchanged;
3. `surviving_questions` — the hindsight coverage result.

No editorial rewrite and no comparison with any previous audit.

After this output is frozen, a separate comparison pass may inspect the experiment register and external benchmark.
