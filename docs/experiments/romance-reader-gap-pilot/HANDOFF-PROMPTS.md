# Romance blind reader pilot — handoff prompts

Status: **EXPERIMENT / DIAGNOSTIC ONLY.** These prompts operationalize `COLLECTION-PROTOCOL.md` and `FRESH-READER-BLIND-PROTOCOL.md`.

## Pass 1 — collector chat

Use a normal GitHub-capable execution context. Do not use this chat for editorial analysis.

```text
Use the live GitHub connection only for mechanical collection of the Romance blind-reader packet. Do not analyze, summarize, critique, or generate reader questions.

Repository: u-dont-existDOTcom/joel-articles
Experiment branch containing the collection instructions: experiment/obsidian-romance-gap-map
Protocol path: docs/experiments/romance-reader-gap-pilot/COLLECTION-PROTOCOL.md

Read that collection protocol completely and execute it exactly.

The canonical source itself must come only from main:
articles/romance/master.md
Expected SHA-256:
f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c

Your job is retrieval/verification/packaging only. No article interpretation. No gap analysis. No web research. Do not inspect the reader-gap register, Canvas, external benchmark, PR body, or previous audit conclusions.

Produce the sequential 90-line source windows and manifest required by the protocol. Package them as an ephemeral ZIP/file set for me to control manually. Do not publish or commit the generated windows back to the repository.

Return the collection receipt required by the protocol and the packet file(s). If exact SHA-256 verification is impossible with the available tool boundary, say so explicitly and mark the receipt lower-assurance rather than inferring success.
```

The human/controller keeps the complete packet. Do not upload the complete packet to the Pro reader conversation.

## Pass 2 — Pro reader startup

Start a genuinely fresh Pro/model conversation with no prior Romance context. Do not give it GitHub access for this task. Paste the following plus the **complete text of `FRESH-READER-BLIND-PROTOCOL.md`**. Do not attach any future window.

```text
You are the blinded reader in a sequential editorial diagnostic test.

For this test you must not access GitHub, the web, prior chats, memory, external files, or external relationship frameworks. The article has already been mechanically collected and verified in a separate pass.

I will reveal the canonical article to you one immutable source window at a time. Unrevealed windows are genuinely unavailable to you. Freeze each checkpoint before I provide the next window. Never revise an earlier checkpoint because of later text.

Follow the supplied Fresh-reader blind protocol exactly. Do not propose edits, fact-check, soften arguments, or compare against any prior audit.

Reply exactly:
READY FOR WINDOW 1
```

After it replies `READY FOR WINDOW 1`, paste **window 1 only**.

## Window 1 handoff

```text
WINDOW 1

[PASTE EXACT CONTENTS OF WINDOW 1 HERE]

Freeze the promise-first object and checkpoint 1 exactly as required by the protocol. Do not ask for or infer future content.
```

Save the response unchanged.

## Intermediate window handoff

For each later window except the last:

```text
WINDOW N

[PASTE EXACT CONTENTS OF WINDOW N HERE]

Freeze checkpoint N exactly as required by the protocol. Do not revise any earlier checkpoint and do not infer unrevealed content.
```

Save every response unchanged.

## Final window handoff

```text
FINAL WINDOW N

[PASTE EXACT CONTENTS OF FINAL WINDOW HERE]

This is the final source window. Freeze checkpoint N first. Then perform the protocol's final hindsight coverage pass using only the windows accumulated in this conversation.

Return exactly the three final top-level objects required by the protocol, in order:
1. promise_questions
2. checkpoints
3. surviving_questions

Reproduce all previously frozen promise/checkpoint records unchanged. No introduction, conclusion, rewrite, or comparison with another audit.
```

## Closeout

Copy the final Pro output **unchanged** into the supervising conversation. Only after that output is frozen may the supervisor inspect:

- `reader-gap-register.json`
- `romance-reader-gap.canvas`
- `EXTERNAL-BENCHMARK.md`
- PR #71 or prior audit conclusions

The comparison stage should distinguish:

- independently convergent questions;
- questions unique to the fresh reader;
- pilot candidates the fresh reader did not reproduce;
- existing questions correctly recognized as already answered;
- whether the Obsidian/question layer added information beyond Mermaid + multiscale audit.
