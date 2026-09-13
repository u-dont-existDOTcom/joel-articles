# Romance patient r4 probe — result and owner decision

Status: current task-edge supplement after r20. This does not change canonical `main` or authorize article promotion by itself.

## Context

Article section: **When you and your partner are at different levels of maturity**.

Current r20 registered-main patient wording contains the High-confidence AI 53-word block:

> All three women told me at some point that they felt like my patient. Which is true, I really was the one they asked about almost every medical, mental-health, and practical problem:
>
> “I’m sick. What should I take?”
>
> “I’m sad. What should I do?”
>
> Of course I helped. Saying, “I’m not your doctor or therapist,” every time would have been cold. But enough moments become a pattern.

The current thought functions that must survive are:
- the women had a real basis for describing the relationship as patient-like;
- they routinely brought medical, mental-health, and practical problems to Joel;
- the sick/sad examples;
- helping was natural, not inherently wrong;
- repeated helping can accumulate into a default caregiver/patient pattern.

## Prior known-green control

Historical `MATURITY_PATIENT_R2B`, exact 273-word natural boundary, SHA `b52861615ae49e1059b7b035e70e6f0b624240b70b5486c51523e4a34048695d`, Pangram 4.0 exact Human `1.0`, High confidence.

Its patient realization was:

> All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them. They asked me about almost every medical, mental-health, and practical problem:
>
> “I’m sick. What should I take?”
>
> “I’m sad. What should I do?”
>
> I usually had some idea, so of course I answered.

That prior green wording did not explicitly preserve the current `But enough moments become a pattern.` function, so it was not article-eligible as a rollback.

## 2026-08-23 API probe

Diagnostic candidate: exact 273-word known-green boundary plus only the current six-word sentence:

> But enough moments become a pattern.

Candidate SHA `45d79fa428a737131113e0eb75e65d8d326e270196f01fbf5cb0165f3cf732f4`, 279 words.

Pangram 4.0 result:
- Human `0.8113083243370056`;
- AI `0.188691645860672`;
- AI-assisted `0.0`.

Crucial localization:
- first **223 words**, including the complete patient realization, restored pattern sentence, Key guru anecdote, and Joel's condescension/accountability paragraph: **High-confidence Human**;
- only AI window: the unchanged later 56-word paragraph beginning `I know what can happen on my side. Helping feels good...`.

Interpretation: restoring `But enough moments become a pattern.` does **not** make the patient realization itself detector-red. The detector signal redistributed downstream, consistent with the already-established context-sensitivity findings.

Evidence:
- public result: `pangram-humanization-lab:automation/pangram-fixed-batch/state/experiments/romance-detector-repair-20260820-patient-known-green-plus-pattern-r4-20260823-results.json`;
- exact result source ref `7ce540b23e16a0087ac329d2c008c821a24a7aa3`;
- result source SHA-256 `dc705274f9633074ea9dd807d90f5298a425b043d22310d43e5e2af9bcf5fc8c`;
- closeout merged to Pangram `main` as `59d09ca910d89c5f35fd1112b96f5b91414d7cf7`.

## Exact proposed patient replacement for Joel to accept/edit

Replace only the current patient block with:

> All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them. They asked me about almost every medical, mental-health, and practical problem:
>
> “I’m sick. What should I take?”
>
> “I’m sad. What should I do?”
>
> I usually had some idea, so of course I answered. But enough moments become a pattern.

Everything before and after this block remains unchanged. In particular, the following Key guru anecdote and Joel's condescension/accountability paragraphs are not part of this proposed edit.

## Owner decision required

This wording is assistant/task-history provenance, not direct owner prose. It must not be materialized as article authority merely because it tests well locally.

Joel can:
1. accept it as written;
2. edit it in his own words; or
3. reject it and supply a different realization.

Only after owner acceptance should it be materialized into r20 and aggregate-certified as the next candidate.
