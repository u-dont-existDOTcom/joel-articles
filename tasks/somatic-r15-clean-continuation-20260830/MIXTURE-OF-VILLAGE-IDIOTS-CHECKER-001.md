# Somatic Introduction — Mixture of Village Idiots checker

Updated: 2026-08-31
Status: **ACTIVE BOUNDED CHECKING METHOD / not article authority**

## Owner concept

Joel's `Mixture of Village Idiots` / `fussy moron filter` means a mixture-of-experts-like evaluator whose members are deliberately narrow and each fussy about a different failure. The purpose is to reduce smart-generalist rationalization: no individual checker gets enough scope to explain away a defect by balancing it against strengths elsewhere.

This method is for **checking/adjudication**, not generation. It does not replace source integrity, preservation, owner authority, or Pangram.

## Existing-work basis

This is an adaptation/composition rather than a claimed novel ensemble method. Relevant established precedents include:

- weak-supervision systems such as Snorkel, where multiple imperfect labeling functions contribute useful signal and correlated functions must not be double-counted;
- ensemble / jury approaches to LLM evaluation, where judge reliability differs and naive equal averaging can underperform judge-aware aggregation;
- multi-aspect evaluator panels, where separate judges handle distinct criteria rather than one monolithic global score.

The Somatic-specific novelty, if any, is only the application design: deliberately low-scope `idiot` checks against known AI-shaped discourse failures, with fail-closed promotion rules.

## Design principle

Each idiot receives only:

1. the literal candidate;
2. one narrow question;
3. permission to return `FLAG`, `CLEAR`, or `ABSTAIN`;
4. no other idiot's verdict;
5. no invitation to give a global quality assessment.

The idiot must cite an exact span when flagging. It may not compensate for its own detected defect by saying the passage is otherwise good.

## Village

### V1 — Semantic Card Counter
Question: Can the candidate's consecutive sentences/clauses be mapped mostly one-to-one onto the supplied semantic obligations in roughly their supplied order?
Blocking: yes.

### V2 — Flowchart Moron
Question: Can the prose be converted cleanly into `if condition A -> response A; if B -> response B; otherwise C`, especially regulation / bodily-resolution / trauma-focused-method branches?
Blocking: yes.

### V3 — Aftercare Cop
Question: Does any sentence mainly explain why the previous point matters, summarize an inference already available, clarify a menu the prose just created, or diagnose what the reader already saw?
Blocking when substantive.

### V4 — Symmetry Sniffer
Question: Are alternatives, caveats, positive/negative cases, or interventions arranged in matched rhetorical balance mainly to complete the form?
Blocking when it organizes the thought.

### V5 — Paragraph Tile Counter
Question: Do neighboring paragraphs or sentence clusters repeat `setup -> qualification -> verdict/closure`, receive similar conceptual bar-length, or land with similarly polished endings?
Blocking: yes.

### V6 — Bridge Snob
Question: Is a cross-domain relation such as inner-child work introduced through a polished explanatory bridge or self-contained transfer unit rather than arising from the live thought?
Blocking when present.

### V7 — Speak-It-Out-Loud Peasant
Question: If an ordinary thoughtful person were saying this aloud without notes, what is the first exact point where the sequence feels precomposed rather than like one thought leading to the next?
Output: exact first break or CLEAR. No theory.
Blocking if a concrete break is found.

### V8 — Deletion Idiot
Question: For each sentence, would deleting it preserve the substantive reasoning while merely removing explanation, balance, summary, or polish?
Flag those sentences as possible scaffold/aftercare.
Blocking only after semantic custodian confirms no protected function is lost.

### V9 — Anti-Pull Matcher
Question: Ignore wording. Does the hidden outline reproduce a known failed Somatic pull signature, especially `mind/body mismatch -> readiness/regulation -> alternative intervention`, or `problem -> qualification -> tidy resolution`?
Blocking: yes.

### V10 — Connective Yokel
Question: Are thoughts that an ordinary speaker would join causally/temporally/concessively split into polished standalone verdicts, or are semicolons/conjunctions being used to pack conceptual cards together rather than preserve real spoken relation?
Blocking when the syntax reveals imposed rhetorical meter.

### V11 — Semantic Escrow Keeper
Question: Did any claim, actor, certainty, causal relation, conditional distinction, inner-child function, or required link disappear or change?
This idiot judges fidelity only and is **not allowed to judge humanness**.
Blocking: any unexplained substantive delta.

### V12 — Uncertainty Canary
Question: Is there an exact span whose AI/human shape remains genuinely borderline after the other narrow checks?
Output only exact span + reason, or CLEAR.
Routing: any genuine borderline result goes to Joel under the owner uncertainty rule; it is not self-certified.

## Aggregation

Do **not** use majority vote.

Group correlated idiots so several versions of the same diagnosis do not create fake confidence:

- checklist/topology family: V1, V2, V9;
- overcompletion/rhythm family: V3, V4, V5, V10;
- transfer/speakability family: V6, V7;
- fidelity family: V8 + V11;
- uncertainty family: V12.

Promotion rule for an owner-facing candidate:

1. V11 must CLEAR.
2. No blocking idiot may return a credible FLAG.
3. A FLAG is defeated only by showing that the idiot's narrow premise is factually wrong about the literal text, not by balancing it against strengths elsewhere.
4. Correlated CLEARs count as one family clear, not multiple independent votes.
5. V12 must CLEAR; otherwise ask Joel about the exact span.
6. The normal two-consecutive-cold-clear rule still applies after the village check. MVI supplements rather than replaces it.

## Current-candidate diagnostic

Applied to the latest owner-facing Introduction candidate from the manual retry, the village rejects it without needing Pangram:

- V1: FLAG — successive units still closely service cognition/body mismatch, unresolved activation, inner-child state, deep-memory readiness, regulation, overwhelm, stable-case exception, EMDR.
- V2: FLAG — the second paragraph reduces cleanly to insufficient choice/stability -> regulation; sufficient stability -> trauma-focused method.
- V3: FLAG — `Regulation may be what makes that possible; without that much room, “deep processing” may just be a nicer name for overwhelm.` performs intervention-function explanation plus verdict.
- V4: FLAG — the final stable/unstable contrast organizes the ending.
- V5: FLAG — both paragraphs are compact explanatory units with strong conceptual closure.
- V6: FLAG — inner-child work still arrives as a self-contained transfer of the same mind/body principle.
- V7: FLAG — first clear precomposition point is the transition from the bodily-discharge sentence into the inner-child sentence; it feels like coverage expansion rather than pressure from the preceding thought.
- V8: FLAG candidate — the `cleaner treatment sequence` clause mainly services the anti-mandatory-sequence explanation; semantic review is needed before deletion/repair.
- V9: FLAG — hidden outline remains a close variant of the known failed Somatic package.
- V10: FLAG — semicolon packing repeatedly combines concept card + explanatory consequence.
- V11: CLEAR provisionally — no obvious substantive loss in the checked candidate relative to the supplied Introduction, but formal preservation remains required for any replacement.
- V12: CLEAR on the rejection decision — the passage is not borderline enough to require Joel adjudication; it is blocked.

Current MVI verdict: **BLOCKED**.

## Use on the next candidate

Run the village on the literal quarantined text before the two cold passes. A candidate does not advance merely because more idiots clear than flag. The goal is to expose a defect the smart generalist would otherwise rationalize away.
