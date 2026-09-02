# Writer–Critic Firewall — 2026-08-31

Status: ACTIVE supplement to the owner-directed Somatic Introduction live-composition experiment. This does not change article authority, preservation requirements, detector authorization, or the registered master.

## Failure that triggered this gate

Repeated `eval` cycles accumulated a large catalog of anti-patterns: semantic cards, matched pairs, concept extraction, rhetorical self-dialogue, source-card leakage, cumulative thesis gravity, truncation, aphoristic closure, and propositional mutation pools. Those diagnoses are useful for evaluation, but allowing the writer to carry all of them during composition creates a new failure mode: prose becomes cautious, compressed, self-monitoring, and visibly engineered around prohibitions.

The critic had colonized the writer.

## Architecture

Separate the live-composition pass from the accumulated failure detector.

### Writer packet

The writer receives only the minimum positive state needed to compose:

- current task: exploratory Somatic Introduction prose;
- no numerical length target, word count, countdown, expected sentence count, or stopping horizon;
- no invented autobiography, symptoms, chronology, evidence, or unauthorized factual specificity;
- one small live snag / pre-propositional seed rather than a semantic outline;
- permission to follow curiosity, association, irritation, or surprise word by word;
- no obligation to cover source units yet;
- no paragraph quota and no planned ending;
- source reconciliation happens later.

The writer does **not** consult the rejection catalog, source-unit coverage map, named AI patterns, detector history, prior candidate autopsies, or an explicit list of forbidden rhetorical structures while choosing the next word/sentence.

### Writer-blind length controller — 2026-09-01

Owner-directed `eval` found that the earlier floor-crossing stop still leaked the length horizon into generation. The writer packet itself contained `at least 50 words`, so the model could anticipate that a later sentence was likely to cross the floor and make that sentence function as a payoff. In the failed 57-word attempt, the final sentence (`processing` sounding like permission to continue) simultaneously crossed the minimum and supplied the clean rhetorical landing.

This is **horizon leakage**: the termination rule was external only after a sentence had been written, while the writer still knew the target during sentence selection.

Existing-work classification: **ADAPTATION / REUSE.** Length-controlled generation literature separates content generation from explicit length/EOS control, and work on EOS shows that termination cues can themselves create length-dependent internal behavior. This task uses a simple editorial analogue: keep the numerical floor in a controller rather than in the writer state.

Operational mechanism:

1. **Controller owns the floor.** The minimum word requirement exists in controller state only. The active writer packet does not state the number or say that a minimum exists.
2. **Writer emits without horizon knowledge.** Generate the next accepted sentence from literal text and local live pressure without estimating remaining words, sentence count, or likely stopping position.
3. **Controller checks only at accepted sentence boundaries.** It counts the frozen passage after the sentence is accepted.
4. **Controller returns only `CONTINUE` or `STOP`.** Never return the count, distance from threshold, whether the passage is close, or why continuation is required.
5. **`CONTINUE` carries no semantic instruction.** It authorizes another sentence but supplies no topic, transition, summary, ending, or completion pressure. The next sentence still comes from the writer's live local state.
6. **`STOP` terminates before another writing decision.** No landing, takeaway, aftercare, or polish sentence is generated after `STOP`.
7. **Do not infer the horizon from repeated controller calls.** A `CONTINUE` signal is not evidence that the writer is nearly done or that the next sentence should be broad, conclusive, or self-contained.
8. **Same-context limitation remains explicit.** Perfect information hiding is impossible in one Chat context. The operational approximation is role separation: during the writer phase, do not retrieve or reason from the numerical floor even though the larger conversation contains it. The controller alone performs counting.

### Microburst no-lookahead mode

Owner-directed `eval` on 2026-08-31 found that the first firewall attempt still compressed a snag into a clean abstraction (`Bodies don't know propositions`) and then resolved that abstraction inside the same paragraph. The writer was no longer carrying the blacklist, but it was still generating at sentence/paragraph scale with enough semantic lookahead to discover and finish a compact insight.

For the next exploratory passes, change the composition unit:

1. **Generate in short continuation bursts.** Advance by a few words or a short clause at a time rather than deciding the whole sentence or paragraph before realizing it.
2. **No destination variable.** The active writer state contains the literal text-so-far and the current local verbal pressure only. Do not privately decide what claim the paragraph will establish, where the sentence should land, or what the ending will mean.
3. **No semantic recap between bursts.** Do not summarize `what I am saying now` before choosing the next burst. Continue from wording, cadence, irritation, association, or unresolved local pressure instead of a conceptual paragraph plan.
4. **Permit ordinary connective tissue.** A burst need not contain an insight, novelty, aphorism, contrast, or argumentative move. Plain continuation is allowed. The writer does not have to make each sentence earn quotation value.
5. **Let wording detours survive provisionally.** If a phrase produces a side irritation or linguistic question, it may occupy several bursts without being converted immediately into the article thesis.
6. **Continuation is externally controlled.** The writer does not know the minimum length. After each accepted sentence, the controller supplies only `CONTINUE` or `STOP`; if `CONTINUE`, follow available local pressure or another already-live pre-propositional seed without treating continuation as evidence that an ending is approaching.
7. **Critic only after the controller stops the attempt.** The accumulated structural gates remain post-draft diagnostics. They do not steer individual bursts.

This is an operational approximation inside one model context; literal information hiding is impossible. The key test is whether the resulting prose appears to have known its payoff or stopping position several sentences in advance. If so, the no-lookahead / writer-blind controller failed even if the words are natural.

### Lexical-fixation attention reset

Owner-directed `eval` on 2026-08-31 found that microburst generation can still become a serial repair machine. In the failed attempt, `stop` was introduced, then questioned, disambiguated with shaking, redefined as changing one's mind, and finally restated twice. No individual burst required paragraph-level lookahead; the failure came from keeping attention locked on one lexical ambiguity until the ambiguity was fully closed.

This is **lexical fixation**: local uncertainty becomes repair debt, and each new burst is spent paying that debt rather than continuing to think.

Use the following positive routing inside the writer packet:

1. **Local roughness may remain.** If the literal meaning is intelligible enough to continue, a slightly loose word does not need immediate repair.
2. **One repair burst maximum before attention resets.** A real comprehension problem may receive one short clarification. After that, move attention back to another live pressure in the text rather than continuing to define the same word.
3. **Attention reset, not topic reset.** The next burst need not import a new source topic. It may pick up a different consequence, association, irritation, case, or unresolved piece already latent in the words on the page.
4. **Do not accumulate definition debt.** The writer does not maintain a private list of terms that must be made exact before the paragraph can proceed. Publication-level precision is a later revision concern unless current wording would materially misstate the thought.
5. **No serial self-edit narration.** `I mean`, `what I mean is`, `I'm using X too loosely`, and similar repair language may occur naturally, but the writer cannot use them repeatedly as the engine of continuation.
6. **Return is allowed later.** A loose term can be clarified later if another thought makes the distinction newly necessary. It does not have to be resolved at first contact.

The critic should reject a passage when several successive sentences exist mainly to clean up one prior word, even if the resulting distinction is correct.

### Critic packet

Only after the writer-blind controller returns `STOP` does the critic reopen the accumulated gates and inspect the literal passage for:

- card succession / source-card leakage;
- propositional seed packaging;
- local and cumulative completion;
- matched contrast / symmetry;
- concept harvesting;
- staged spontaneity or self-dialogue;
- bridge machinery;
- thesis gravity;
- aphoristic substitution;
- truncation / minimum-length failure;
- semantic or provenance violations;
- evidence that the prose knew its payoff or stopping position several sentences in advance;
- lexical fixation / serial repair of one term.

The critic diagnoses; it does not line-edit the rejected candidate into compliance.

## Retry rule

If the critic rejects a passage:

1. Name the strongest causal process failure.
2. Persist a reusable lesson when genuinely new.
3. Discard the rejected realization as generation context except for the smallest live fragment that independently survived the critique.
4. Build a new minimal writer packet that contains **positive generative affordances**, not the full rejection history and not the numerical length floor.
5. Generate sentence by sentence under the writer-blind `CONTINUE` / `STOP` controller.
6. Run the critic afterward.

Do not ask the writer to remember twenty things not to do. Do not make the next pass the inverse of the last defect. Do not treat critic awareness as the composition mechanism.

## Same-context limitation

Within one saturated Chat context, perfect informational isolation is impossible. The operational approximation is therefore strict role routing: anti-pattern history and the numerical floor may inform critic/controller decisions, but they are not used as the active next-token agenda during the writer pass. If the writer starts explicitly navigating the blacklist or length horizon, declare firewall failure and restart rather than adding another compositional prohibition.
