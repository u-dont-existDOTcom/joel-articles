# Episode 008 — Pro Pass B2 failure diagnosis

Date: 2026-09-19
Status: **OWNER-REJECTED / PROMPT-SCAFFOLD CAUSALLY EXPOSED / B2 SAME-METHOD CONTINUATION STOPPED**

## Exact returned candidate

`experiments/EPISODE-008-PRO-PASS-B2-OWNER-RETURNED-CANDIDATE-20260919.md`

Owner judgment: **still trash**.

No Pangram call is warranted. Owner editorial rejection already determines production disposition.

## Strongest causal finding: B2 prewrote the first paragraph

The B2 writer payload contained this supposed scene/setup:

> They don't answer right away. They write the reply they actually want to send and leave it unsent. Later they read it again. A sentence that felt necessary at first may now look unfair or muddled; something they were tempted to soften may still be exactly what they mean. If an apology is genuinely theirs, it can stay without swallowing the complaint.

The returned candidate reproduced that paragraph verbatim as its opening paragraph.

Therefore B2 did not merely prime a style. It supplied publication-shaped prose that the writer treated as already-written article text.

The model then expanded the remaining prompt instructions in order:
- `Stay with the rereading...` -> second/third paragraph rereading analysis;
- `what, if anything, they want to say` -> explicit `what do I actually want this person to know?`;
- keepable later-answer promise -> final paragraph promise language;
- immediate protection -> final paragraph stop/protection language.

This is direct observable prompt-to-output topology, not speculative model psychology.

## Why the rest remained model-shaped

### 1. The “natural substrate” was still an outline in prose clothing

B2 removed bullets but converted the same functions into smooth declarative prose. The semantic topology survived:
private draft -> reread -> identify unfair/muddled -> preserve valid position -> retain apology -> decide what leaves page -> keepable promise -> immediate protection.

Replacing bullets with sentences did not remove the sequence. It made the sequence less visibly checklist-like to the supervisor while remaining fully legible to the generator.

### 2. The output remained a whole-subsection optimization problem

The writer was still asked to produce a finished practical subsection from abstract source functions. For this target, the model's default solution is a guide:
observe -> distinguish -> simplify -> decide -> safety/closure.

That produces the same predictable marching advancement even when the prompt is warmer or more scene-like.

### 3. The prompt supplied no uncontrolled human cognition

The scene contained no genuinely source-derived oddity, hesitation, social exchange, mistaken assumption, discovery, or owner reasoning route. Every supplied sentence existed because the supervisor needed it to encode a function.

The generator therefore had no human cognitive path to continue. It had a polished task representation.

### 4. “Fresh” context was not informationally clean

The launch required the mandatory Universal/Joel bootstrap before reading B2. That bootstrap activates current article/humanization guidance and critic knowledge.

The Episode-008 source firewall prevented extra file reads but did not make the writer informationally isolated from the project's active writing/humanization instruction environment.

Therefore B2 cannot establish that a truly sparse prose continuation prompt fails. It establishes that **B2 plus the mandatory project/bootstrap environment** fails.

### 5. Positive instructions are still being compiled back into critic rules

The generator-learning compiler already says the project is strong at diagnosing but has not demonstrated durable autonomous transfer. B2 confirms that converting a diagnosis into `stay with the rereading`, `let one moment carry more than one meaning`, or a naturalistic setup does not change the generator prior reliably.

## Method threshold

Pass A dense preservation prompt failed editorially.
B2 prose-substrate prompt failed editorially.
Earlier internal-cognition and exemplar/sentence-engineering broad-substrate experiments also failed on this target family.

Do **not** make B3 by rewriting the same semantic content into yet another nicer prompt.

## Next materially different experiment: pure continuation substrate

Test whether task semantics themselves are forcing the guide architecture.

A fresh writer should receive:
- only the strongest locally relevant accepted article tail;
- the target heading;
- a bare continuation request.

Do not tell the writer what the subsection must cover.
Do not provide the private-draft semantic ledger.
Do not provide a scene synopsis.
Do not provide humanization/detector rationale.
Do not ask for a complete preservation-clean article section.

This is deliberately **not** a production candidate request. It is a substrate experiment.

After generation:
1. judge whether the prose movement is materially more natural before checking semantic completeness;
2. map which required functions arose spontaneously;
3. if a genuinely Human-looking substrate exists, use localized residual engineering to add missing protected functions without rewriting the substrate;
4. if pure continuation is still globally model-shaped, stop treating prompt topology as the main bottleneck and change generation surface/architecture.

## Interpretation boundary

This experiment trades first-pass completeness for information about the causal bottleneck.

A semantically incomplete but materially natural continuation would be useful strategy evidence.
A complete but staircase-shaped continuation is another failure.

No detector spend until owner/editorial review says the substrate is plausible.
