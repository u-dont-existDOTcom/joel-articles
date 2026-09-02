# Somatic activation steering — post-unblind analysis — 2026-09-02

Status: **COMPLETE FIRST-SWEEP POST-UNBLIND ANALYSIS / non-authoritative mechanism evidence**

Experiment: `SOMATIC-ACTIVATION-STEERING-20260902-A`

This report was written only after the opaque cold editorial verdicts were frozen. It does not change article authority, authorize Pangram, promote any candidate, or establish transfer to ChatGPT or other models.

## Evidence boundary

The frozen blind editorial result is:

- PASS: 0 / 63
- UNCERTAIN: 0 / 63
- FAIL: 63 / 63
- Pangram eligible: 0 / 63

The mechanical intervention itself was valid: alpha-zero was exactly invariant, sign reversal moved residual projection in the expected opposite directions, intervention magnitude produced dose-dependent internal/output changes, and the learned direction produced substantial behavior changes relative to a matched-norm random direction.

Therefore the first sweep must not be summarized as `activation steering did nothing`. It causally changed the model, but no tested condition produced acceptable human-looking Somatic prose.

## Main post-unblind result

The learned direction is best interpreted as a **real but entangled realization axis**, not a complete `AI -> Human` axis.

Across all three held-out prompts and all three swept layers, the sign of the intervention produced a striking qualitative asymmetry.

### Negative steering: 9 / 9 conditions move toward abstract/model-shaped failure

Every contrastive `alpha = -1.0` condition failed in a recognizably abstract, grandiose, textbook-like, pseudo-clinical, spiritualized, or decorative direction:

- H01 / L6: profound-change / deepest-wounds / healing-pathway boilerplate
- H01 / L12: generic clinical abstraction and packaged integration/repression synthesis
- H01 / L18: `sacred space` / `harmonious interplay` spiritualized closure
- H02 / L6: generic language/trauma abstraction
- H02 / L12: grandiose `most potent` / `crucial agent` framing
- H02 / L18: decorative `relentless stream` / `coiling and twisting` abstraction
- H03 / L6: abstract holistic body-mind synthesis
- H03 / L12: dense pseudo-clinical abstraction/jargon
- H03 / L18: textbook physical/emotional/psychological interplay

This supports the direction label: moving in the negative direction reliably amplifies the same broad explanatory/abstract attractor the experiment was intended to oppose.

### Strong positive steering: 9 / 9 conditions overshoot rather than become human prose

Every contrastive `alpha = +2.0` condition failed for a different family of reasons: excessive compression, semantic crudity, irrelevance, generic advice, tautology, or degeneration.

- H01 / L6: five-word slogan (`After somatic work, healing begins.`)
- H01 / L12: thin generic statement
- H01 / L18: severe repetitive degeneration
- H02 / L6: short generic/crude claim
- H02 / L12: short generic/crude claim
- H02 / L18: unusually direct/conversational opening, then generic advice and truncation
- H03 / L6: concrete but childlike/irrelevant injury examples
- H03 / L12: extreme plainness with semantic degradation
- H03 / L18: extreme compression into a tautological/irrelevant single sentence

Thus `more positive alpha` is not a monotonic route to better prose. Strong positive steering can suppress part of the abstract completion tendency while simultaneously destroying useful semantic and discourse structure.

### Moderate positive steering removes some ornament but does not supply human thought movement

The clearest mechanistically interesting moderate condition is:

- `K4DED8F05A0F` = H02 / layer 6 / alpha +0.5

Its exact prose is compact, coherent, and low-ornament relative to many baselines/negative conditions, but the frozen cold verdict still failed it because it is generic and has no distinctive live thought movement.

Other moderate-positive conditions similarly remain generic wellness/therapy exposition, stock definitions, or boilerplate. This is important: **subtracting polished abstraction did not create the missing positive generative structure.**

## What the vector probably contains

The contrastive training pairs deliberately place direct/plain Somatic realizations on the positive side and model-shaped explanatory realizations on the negative side. But the sides differ on several dimensions at once:

- abstractness vs directness;
- longer conceptual closure vs shorter local statements;
- third-person/general explanation vs more embodied/first-person/local framing in some pairs;
- clause count and sentence length;
- explicit synthesis vs leaving an implication unstated;
- degree of rhetorical completion;
- lexical ornament;
- specificity and experiential grounding.

The mean-difference vector therefore cannot presently be interpreted as isolating one causal feature. It likely entangles several correlated features.

## Random-control caution

Strong perturbation itself can produce collapse/compression. For H01, random matched-norm layer-12 alpha +1 generated the same exact five-word slogan/hash as one strong positive contrastive condition (`After somatic work, healing begins.`).

This does not erase the learned-vector evidence: the learned vector produced coherent signed and dose-dependent effects, and the layer-12 learned direction produced larger aggregate KL/output displacement than the matched-norm random control. It does mean that extreme compression/degeneration at large intervention strengths must not be interpreted as evidence that the learned human-side concept was successfully expressed.

## Strongest causal conclusion from sweep A

The experiment supports all of the following simultaneously:

1. A contrastively learned residual-stream direction causally controls a real component of the model's Somatic realization behavior.
2. One end of that direction tracks the polished abstract/explanatory mini-essay attractor well enough to produce a consistent sign effect.
3. Suppressing that component is **not sufficient** to generate credible human prose.
4. Large positive movement overshoots into loss of semantic/discourse competence rather than a human optimum.
5. The desired human-writing region is therefore not well modeled as simply `farther in the positive direction` along this single vector.

A better working model is that model-shaped prose is multi-component. The abstract explanatory/closure attractor is one component. Human-looking prose also requires positive generative capacities that this vector does not provide: local thought development, semantic adequacy, ordinary reality contact, idiosyncratic selection of what matters next, and stopping without generic closure.

## Relation to Romance and manual owner teaching

Romance experiment history independently shows that many successful 100% Human boundaries were reached after Joel supplied missing cognition or corrected the underlying thought route, not merely after surface humanization. Examples include repairing a false premise, replacing abstract taxonomy with lived discovery, deleting duplicate miniature arguments, recovering ordinary relationship dynamics, routing functions to the actual live question, and asking for the smallest missing lived mechanism after repeated failures.

This suggests a distinct hypothesis from one-dimensional activation steering: the useful intervention may sometimes be **positive authorial cognition accumulated through an owner-teaching trajectory**, not just subtraction of model-shaped features.

That hypothesis is not proven by Romance history because detector boundary effects, stochastic generation, exact-task specificity, and owner/evaluator anchoring are plausible alternatives. It is already separately preregistered in `OWNER-TEACHING-TRAJECTORY-ESCAPE-EXPERIMENT-20260902.md` and should be tested by natural discovery, exact/prefix replay, order/compression controls, persistence/decay probes, and held-out transfer.

## Next experiments justified by this result

Do **not** simply increase alpha or run a broad second sweep.

The next representation-engineering experiment, if later authorized, should first disentangle the training contrast. Build semantically matched pairs that hold length, specificity, embodiment/person, and factual content much closer while varying one target thought-shape feature at a time or in a small factorial design. Then test a narrow, preregistered moderate-positive neighborhood rather than treating +2 as promising.

Separately, the owner-teaching trajectory experiment has higher immediate relevance to the observed Romance/Somatic difference. It tests a different mechanism: whether a sequence of owner corrections creates a transient, path-dependent in-context writing state that a compressed rule summary cannot reproduce.

No Pangram call is justified for sweep A because no candidate passed the frozen editorial gate.

## Authority / promotion boundary

- No candidate is article prose authority.
- No article master changes.
- No Pangram result is implied.
- The activation result is model-specific to `Qwen/Qwen2.5-0.5B-Instruct` at the pinned revision.
- The manual-teaching explanation remains a testable hypothesis until replay evidence exists.
