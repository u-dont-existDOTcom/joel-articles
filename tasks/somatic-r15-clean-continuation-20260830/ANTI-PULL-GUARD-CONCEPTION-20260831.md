# Anti-Pull Guard — conception and bounded prior-art scan

Updated: 2026-08-31
Status: CURRENT OWNER-PROPOSED PROCESS HYPOTHESIS / experimental

## Independent conception snapshot

Owner insight: the humanization failure may be usefully understood as a latent-tendency problem. The model knows the rule against its familiar explanatory architecture and can still be pulled toward that architecture when generating and again when judging its own output. Joel analogized this to a spiritual discipline sometimes summarized as not simply doing what one wants to do: the point is not that the opposite impulse is automatically correct, but that the first impulse should not automatically govern behavior.

Applied to writing, the proposed mechanism is an **anti-pull guard**:

- treat the writer's first/default realization as evidence of the model's current latent pull, not as a candidate to polish;
- do not mechanically invert the first realization;
- externally prevent the default structural trajectory from becoming the accepted trajectory merely because it is fluent, easy, or locally plausible;
- make the next search operation depart at the level of discourse movement/topology rather than vocabulary;
- keep semantic preservation external so the writer is not pulled back into checklist servicing;
- dynamically identify the pull again after each material change rather than creating a permanent opposite-style template.

The key distinction is **non-obedience to the default trajectory**, not opposition for its own sake.

## Bounded existing-work scan

Strong analogues already exist at the model-control level:

1. **Unlikelihood training** (Welleck et al., ICLR 2020) explicitly lowers probability assigned to designated undesirable candidates rather than only rewarding desired output. This supports the general concept of negative pressure against known degeneration modes.
2. **GeDi** (Krause et al., 2020) uses a generative discriminator to steer decoding away from an undesired attribute distribution and toward a desired one.
3. **DExperts** (Liu et al., ACL 2021, DOI 10.18653/v1/2021.acl-long.522) combines an expert and anti-expert at decoding time so likely base-model tokens can be downweighted when the anti-expert favors them.
4. **Self-Refine** (Madaan et al., 2023) shows that iterative self-feedback can improve outputs, but the current Somatic evidence shows the limitation relevant here: correlated generator/judge priors can allow repeated self-certification of the same structural defect.

These methods do not directly solve Joel-byline prose architecture in the current Chat runtime because Chat has no direct token-logit anti-expert interface. They do establish that suppressing an undesirable distribution/trajectory is an established control idea rather than a novel principle.

## Decision

**ADAPT + EXPERIMENT**, not invent-from-scratch.

Use an inference/workflow-level approximation of anti-expert steering:

1. **Sacrificial pull sample:** the first realization after a semantic reset is disposable. Its function is to reveal the easiest/default discourse topology.
2. **Pull signature:** record only the structural pattern to avoid (for example: premise → readiness checklist → conditional modality menu → polished transfer), never preserve the rejected sentences as a template.
3. **Departure requirement:** the next realization must differ in governing movement, paragraph jobs, and information release—not merely diction, sentence length, or order of the same semantic cards.
4. **External guard:** admission review explicitly compares the new topology with the pull signature. Material structural recurrence blocks promotion.
5. **No inverse-style trap:** the guard never says the opposite structure is good. A new route still has to arise from the live thought and preserve all semantics.
6. **Dynamic reset:** after a material owner correction or newly exposed latent pattern, recalculate the pull signature. Do not accumulate a giant permanent blacklist.
7. **Self-judge limitation:** two same-context cold clears remain provisional; if literal reread reactivates the pull diagnosis, the candidate is blocked regardless of prior receipts.

## Hindu analogy boundary

Do not encode the spiritual analogy as a factual claim that Hinduism universally teaches `do not do what you want`. The Bhagavad Gita's better-established analogy is action without attachment to desire/results rather than mechanically doing the opposite of desire. For process design, this maps well to: **notice the pull; do not let the pull choose the action; choose according to the governing objective.**

## Current Somatic application

For the active Introduction retry, the known pull signature is:

`body/mind mismatch premise → complex-trauma qualification → readiness criteria → regulation verdict → EMDR exception → bodily-discharge exception → polished inner-child transfer/closure`

A candidate following substantially this topology is blocked even if its sentences are individually natural. The next realization must not be produced by shuffling or softening those cards.
