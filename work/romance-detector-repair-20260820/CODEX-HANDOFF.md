# Codex handoff — Romance detector repair

Updated: 2026-08-23 after r20 aggregate, Joel's patient acceptance, and Affection owner-language routing.

## Authority

Canonical `main:articles/romance/master.md` remains unchanged at SHA-256:

`af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`

PR #29 / `task/romance-detector-repair-20260820` is experimental working state only. **Never merge PR #29 wholesale.** Current Joel wording/acceptance outranks task candidates; preservation proof, semantic/editorial quality, architecture, source provenance, and fidelity outrank Pangram.

Semantic-r9 remains the loss-recovery baseline: 44/44 headings aligned and ten discovered unsuperseded argumentative losses restored. Father provenance remains separate: the only exact remembered father sentence is `Sex is what you do when you are older and you find a friend you want to have children with.` Joel's later readiness/co-parenting questions are his interpretation.

## Settled current task choices

- **Talk:** r19 owner-final Talk tail is settled and outside current AI windows. Preserve exact owner wording in `recovery-20260822/OWNER-TALK-FINAL-TAIL-20260822.md`.
- **Slow Steady:** retain exact local-green minimum-dose repair SHA `2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4`.
- **Casual:** r20 is settled. Joel approved two deletions only: remove `Oxytocin, vasopressin, and the rest can start attaching you anyway.` and remove `You can both mean it when you say this is only sex and still have one of you get attached afterward.` Preserve `If you’re both really numb or robotic about sex, maybe not.`
- **Stable Part 2:** SHA `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`, 9,892 words, Pangram 4.0 exact Human `1.0`. Do not rerun unless bytes change.

Local section caps: Talk 6/6, Affection 6/6, Casual 6/6, Primal 6/6. No seventh local calls or invented identities. Maturity/patient cross-split is 4/6 after the r4 diagnostic probe, but no further local call is currently needed.

## r20 exact candidate / aggregate

Final preservation receipt:
`work/romance-detector-repair-20260820/recovery-20260823/preservation-proof-r20-casual-two-deletions-final.json`

Materialized Markdown:
`work/romance-detector-repair-20260820/materialized-preservation-r20-casual-two-deletions/candidate-master.md`

- master SHA `8b60f2916a4c050c6295b858889c3a7e3e80c87e18307a2c3e2cf9e276e8637d`;
- 20,343 words;
- native objects 11→11;
- Markdown links 22→22;
- zero unexplained deltas.

Part 1:
- SHA `04ea13442d4044ee56733b75771cb62c5cd44ba1b5da1bbb57d637c4f2ec4316`;
- 10,300 words.

Pangram 4.0 Part 1:
- Human `0.9639888405799866`;
- AI `0.03601117804646492`;
- assisted `0.0`;
- three AI windows.

Casual is completely outside all r20 AI windows. r20 detector closeout is merged into Pangram main at `7e8b15540ff7d6ed2f5b6a3237f3d7495ce70486`.

## Patient/helping — OWNER ACCEPTED for next candidate

Joel accepted this exact replacement on 2026-08-23:

> All three women told me at some point that they felt like my patient, and I couldn't exactly argue with them. They asked me about almost every medical, mental-health, and practical problem:
>
> “I’m sick. What should I take?”
>
> “I’m sad. What should I do?”
>
> I usually had some idea, so of course I answered. But enough moments become a pattern.

Durable owner acceptance:
`work/romance-detector-repair-20260820/recovery-20260823/OWNER-ACCEPTED-PATIENT-R21.md`

Pre-materialization preservation whitelist:
`work/romance-detector-repair-20260820/recovery-20260823/preservation-proof-r21-owner-patient-pre.json`

Joel also manually reports this small snippet tests Human at low confidence and suspects the confidence ceiling is due to snippet size. Treat that only as short-boundary evidence; current lab doctrine already says short passages are less reliable.

### Patient r4 API probe

Historical 273-word known-green boundary plus restored `But enough moments become a pattern.` was tested once through the API:
- candidate SHA `45d79fa428a737131113e0eb75e65d8d326e270196f01fbf5cb0165f3cf732f4`;
- Human `0.8113083243370056` overall;
- first 223 words, including the complete accepted patient realization, Key guru anecdote, and condescension/accountability paragraph: High-confidence Human;
- only AI window moved downstream into unchanged `I know what can happen on my side. Helping feels good...` paragraph.

Closeout merged to Pangram main at `59d09ca910d89c5f35fd1112b96f5b91414d7cf7`.

Interpretation: the accepted patient realization is locally compatible with Human classification; downstream detector redistribution is contextual and is not edit authority.

### Materialization state

A hash-gated one-shot materializer was added at:
`.github/workflows/materialize-romance-r21-owner-patient.yml`

As of this handoff update it has **not emitted** the r21 Markdown artifact. Do not infer that the prose failed; this is orchestration state. Do not manually reconstruct the article from detector text. The exact authorized transform is frozen in the owner-acceptance file and preservation pre-proof above.

## Remaining r20 detector windows before patient materialization

1. **Affection and the simmer — 205 words, High-confidence AI.** Entirely registered-main prose. Affection local loop is 6/6; no assistant-only seventh repair.
2. **Idealization/dependability — 97 words, Medium-confidence AI.** This exact remote area has appeared/disappeared across aggregates without edits. Treat as composition-sensitive and do not edit unless independently localized.
3. **Patient/helping — 53 words, High-confidence AI in r20.** Now owner-accepted replacement above; pending exact r21 materialization + aggregate certification.

## Affection — current owner-language request

The next independent owner-language target is frozen at:

`work/romance-detector-repair-20260820/recovery-20260823/OWNER-LANGUAGE-REQUEST-R21-AFFECTION.md`

It gives Joel the full section, marks the 205-word r20 AI span, preserves the Toft/Anami attribution and links, lists nine current functions, and includes the following Casual context.

Working research hypothesis from Joel's Casual controls: Pangram may react more to polished balanced/therapeutic/explainer discourse than to situated, committed, opinionated prose. This remains provisional and article-specific, not a phrase blacklist or universal rule.

## Immediate next actions

1. Obtain Joel's natural Affection wording from the fully contextualized request. Do not generate an assistant-only seventh local Affection rewrite.
2. In parallel, complete deterministic r21 patient materialization from the exact frozen transform, run final preservation proof, and aggregate-certify Part 1 once; reuse Part 2 exactly.
3. Do not edit the remote idealization window merely because its aggregate label moves.
4. After r21/next aggregate, localize remaining windows. If Affection owner language is accepted, freeze it verbatim and incorporate it through the preservation gate.
5. Canonical `main` remains unchanged until deliberate Joel reconciliation/acceptance. Do not publish/export.
