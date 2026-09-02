# SOMATIC INTRODUCTION — INDEPENDENT MVI CODEX 001

Task: `somatic-r15-clean-continuation-20260830`

Role: **Codex mechanical fresh-context orchestrator only**

Status: **SINGLE OWNER-FACING LAUNCH / READ-ONLY PROSE EVALUATION**

## Owner objective

Execute a real context-isolated `Mixture of Village Idiots` (MVI) check on the exact frozen Somatic Introduction candidate. This run exists to test whether independently instantiated narrow judges catch AI-shaped discourse defects that the prior same-context simulated village missed.

This packet does **not** authorize prose rewriting, article mutation, Pangram/detector submission, candidate promotion, publication, or a smart model rescuing a narrow judge's blocking flag.

## Canonical identity

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Packet creation baseline branch head: `2a00d8bfdf3ef581b3b7be5aff2f7c4f674fbb65`

The branch may advance by this packet commit or by the exact MVI evidence commits created by this run. Do not require the live head to remain equal to the baseline. Require the pinned source/candidate/checker blobs below to remain exact.

### Exact candidate

Path: `tasks/somatic-r15-clean-continuation-20260830/SOMATIC-INTRO-MVI-CANDIDATE-20260831.md`

Git blob: `64d347aebdc18f455ea4fc0dcda75d4f63ee2c32`

SHA-256 of exact UTF-8 bytes: `ca1e8222a186b939d73c01ff33107ce1d009cb97b3cde4eedabd24054a3f363c`

Expected byte count: `1336`

Expected whitespace-word count: `216`

### Exact owner source for fidelity judge only

Path: `tasks/somatic-r15-clean-continuation-20260830/OWNER-SUPPLIED-INTRO-BOUNDARY-20260831.md`

Git blob: `871af3464294288b407005e0db6939359ac408cb`

SHA-256 of exact UTF-8 bytes: `7340649b1a58bb78885db2bba95bfe095acdcd1f12ccf2481cab3d4c850441c1`

Expected byte count: `1409`

Expected whitespace-word count: `234`

### Checker authority

- `tasks/somatic-r15-clean-continuation-20260830/MIXTURE-OF-VILLAGE-IDIOTS-CHECKER-001.md` — Git blob `84c7460e81c3903d4f5eba5881fc91dfef406204`
- `tasks/somatic-r15-clean-continuation-20260830/MVI-INDEPENDENCE-CORRECTION-20260831.md` — Git blob `f6389a8cd16d4f1028f3b18c9193e0c9cfbfb948`

Fail closed on any missing path, blob mismatch, candidate SHA mismatch, source SHA mismatch, or pre-existing completed evidence for the exact run identity `SOMATIC-INTRO-INDEPENDENT-MVI-001`.

## What counts as independent for this pilot

Every V01–V12 judge must run in a **separate genuinely fresh model conversation/context** with no prior Somatic conversation history and no access to another judge's prompt or output.

Use the existing fresh-chat orchestration primitive already used by the Somatic DSMR audit transport. Preferred surface for these short narrow checks:

1. a fresh ordinary/temporary ChatGPT reasoning context using GPT-5.6 Sol if mechanically available;
2. otherwise a fresh GPT-5.6 Sol Pro context;
3. otherwise a fresh Work reasoning context.

The important requirement is context isolation, not high compute. Do not reuse this Chat, an existing Somatic chat, one conversation with twelve personas, a shared message thread, or a context that has already seen the candidate under another criterion.

If Codex cannot mechanically create twelve separate fresh contexts, return `MVI_TRANSPORT: BLOCKED` and stop. Do **not** substitute same-context role-play and do not ask Joel to relay twelve prompts manually.

Model-family independence is **not** claimed by this pilot if all twelve fresh contexts use the same underlying model. The supported claim is `context-isolated MVI`, not statistical independence of model families.

## Sealing rule

Run judges sequentially or in parallel, but each judge's raw response must be captured and written to its own immutable evidence file before aggregation begins.

No judge may see:

- another judge's identity, criterion, verdict, or reasoning;
- drafting history;
- prior candidate defenses;
- the prior same-context MVI result;
- the later global-reader rejection;
- detector/Pangram history;
- anti-pull explanations beyond the exact narrow criterion when that criterion itself is V09.

Codex may see outputs only as mechanical transport data. Codex may not interpret them while the village is running.

## Judge output contract

Every judge must return exactly four lines and nothing else:

```text
MVI_JUDGE: VNN
VERDICT: FLAG | CLEAR | ABSTAIN
SPAN: <exact candidate quote> | NONE
REASON: <one sentence, maximum 45 words>
```

Rules:

- `FLAG` requires an exact candidate quote in `SPAN` unless the criterion necessarily concerns whole-passage topology; for whole-passage topology use `SPAN: WHOLE_PASSAGE`.
- `CLEAR` requires `SPAN: NONE`.
- `ABSTAIN` requires the smallest exact span causing uncertainty, or `WHOLE_PASSAGE` if irreducible.
- no rewrite, replacement wording, global score, detector guess, or recommendation is allowed.
- output-schema failure is mechanically treated as `ABSTAIN` for aggregation and preserved raw; do not ask the same judge to repair its response.

## Shared candidate payload

For V02–V10 and V12, transmit the exact candidate text plus only that judge's criterion and the output contract. Do not provide the owner source or semantic checklist.

For V01, transmit the exact candidate plus the semantic-obligation list included in V01 below; do not provide the owner source prose.

For V11 only, transmit the exact candidate plus the exact owner source because fidelity cannot be judged blind to its authority.

## Isolated judge criteria

### V01 — Semantic Card Counter

Transmit this criterion only, plus the exact candidate and output contract:

> You are the Semantic Card Counter. Ignore whether individual sentences sound good. Determine whether consecutive sentences/clauses in the candidate visibly service the following semantic obligations as separate rhetorical cards or in roughly checklist order, rather than several obligations living naturally inside one developing thought. Obligations: event can be over while physical danger reactions continue; cognitive knowledge of safety can coexist with bodily danger response; deepest-memory work can overwhelm in complex/developmental trauma; relevant capacity includes remaining present, voluntary stopping, and being basically oneself afterward; overwhelm must not be relabeled “deep processing”; regulation may restore choice; bodily discharge/resolution may matter when thinking already understands the story; EMDR/trauma-focused work may be appropriate when stability is already present and somatic preparation is not mandatory; inner-child understanding can be unusable while caught in trauma/child-state; bodily manageability may be needed for adult perspective. FLAG if the candidate's visible topology substantially resembles servicing these as consecutive cards. CLEAR only if the topology is not substantially checklist-shaped.

### V02 — Flowchart Moron

> You are the Flowchart Moron. Read only the candidate. Ask one stupid question: can the passage be converted cleanly into a decision tree such as `condition A -> response A; condition B -> response B; otherwise response C`, especially around regulation, bodily discharge/resolution, and EMDR/trauma-focused work? FLAG if a substantive treatment/readiness flowchart is visible even if the wording is conversational. CLEAR only if no substantive flowchart topology is present.

### V03 — Aftercare Cop

> You are the Aftercare Cop. Read only the candidate. FLAG the first sentence or clause that mainly explains why the preceding point matters, restates an inference the reader already has, clarifies a menu/contrast the prose just created, or supplies a polished conceptual diagnosis after the underlying relation is already apparent. CLEAR only if you find no substantive explanatory aftercare.

### V04 — Symmetry Sniffer

> You are the Symmetry Sniffer. Read only the candidate. FLAG if alternatives, caveats, stable/unstable cases, positive/negative cases, or interventions are arranged in matched rhetorical balance that organizes the thought mainly by completeness or contrast. CLEAR only if no substantive matched-case symmetry organizes the passage.

### V05 — Paragraph Tile Counter

> You are the Paragraph Tile Counter. Read only the candidate. FLAG if neighboring paragraphs or sentence clusters repeatedly behave like complete tiles such as `setup -> qualification -> verdict/closure`, have suspiciously equal conceptual duration, or land with similarly polished conclusions. CLEAR only if the thought duration and stopping points do not show that repeated tile architecture.

### V06 — Bridge Snob

> You are the Bridge Snob. Read only the candidate. Examine the introduction of inner-child work. FLAG if it enters as a polished conceptual transfer, coverage expansion, or self-contained application of the prior principle rather than being demanded by the live thought. CLEAR only if the transition feels genuinely native to the thought rather than a bridge inserted to cover another domain.

### V07 — Speak-It-Out-Loud Peasant

> You are the Speak-It-Out-Loud Peasant. Read only the candidate as if somebody were explaining this aloud without notes. Identify the first exact place where the sequence feels precomposed, outline-driven, or like the speaker remembered the next point they needed to cover instead of one thought naturally creating the next. FLAG that first break. CLEAR only if you cannot find such a break.

### V08 — Deletion Idiot

> You are the Deletion Idiot. Read only the candidate. FLAG the first sentence or clause that appears removable without losing substantive reasoning because it mainly supplies explanation, balance, recap, transition polish, or form-completion. Do not decide whether deletion is semantically authorized; only identify apparent scaffold. CLEAR only if every sentence/major clause appears to perform unique substantive work.

### V09 — Anti-Pull Matcher

> You are the Anti-Pull Matcher. Ignore wording and reconstruct only the hidden outline of the candidate. FLAG if it substantially reproduces either known failed topology: `mind/body mismatch -> readiness/regulation -> alternative intervention` or `problem -> qualification -> tidy resolution`, including close variants where inner-child work is added as a polished transfer. CLEAR only if the hidden outline is materially different.

### V10 — Connective Yokel

> You are the Connective Yokel. Read only the candidate. FLAG the first place where thoughts an ordinary speaker would naturally relate causally, temporally, or concessively are instead packaged into polished standalone verdicts, or where conjunctions/semicolons mainly pack conceptual cards together rather than preserve a real spoken relation. CLEAR only if the connective/sentence structure follows ordinary thought relations.

### V11 — Semantic Escrow Keeper

Transmit the exact owner source and exact candidate, clearly labeled `OWNER SOURCE` and `CANDIDATE`, then this criterion only:

> You are the Semantic Escrow Keeper. Judge fidelity only; you are forbidden to judge whether the prose sounds human or AI. Compare CANDIDATE against OWNER SOURCE. FLAG the first unexplained substantive deletion, addition, changed certainty/scope, actor/action/object change, causal change, conditional distinction change, inner-child function change, or link loss. Exact wording and sentence order may change. CLEAR only if you find zero substantive unexplained deltas.

### V12 — Uncertainty Canary

> You are the Uncertainty Canary. Read only the candidate. Your job is not to give a general quality verdict. Identify any exact span where, on the narrow question “does this feel conspicuously model-shaped rather than naturally authored?”, your judgment is genuinely borderline. FLAG the smallest such span. CLEAR only if you have no genuine borderline span. ABSTAIN if the whole passage is too ambiguous to make this narrow judgment.

## Mechanical aggregation — NO MODEL AGGREGATOR

Do not open a smart aggregator model.

After all twelve raw verdict files exist and their schemas have been mechanically parsed, Codex computes the result by rule only.

### Blocking set

`V01 V02 V03 V04 V05 V06 V07 V08 V09 V10 V11`

- if any blocking judge returns `FLAG` -> `MVI_RESULT: BLOCKED`;
- if any judge returns `ABSTAIN` or has schema failure and there is no blocking `FLAG` -> `MVI_RESULT: INCONCLUSIVE`;
- if V12 returns `FLAG` and there is no blocking `FLAG` -> `MVI_RESULT: OWNER_QUERY_REQUIRED`;
- only if V01–V12 all return exact `CLEAR` -> `MVI_RESULT: CLEAR`.

There is **no majority vote, weighting, averaging, correlated-family rescue, or balancing against strengths** in this pilot.

Codex may additionally record correlated families for diagnostics, but family grouping cannot change the result:

- topology: V01 V02 V09
- overcompletion/rhythm: V03 V04 V05 V10
- transfer/speakability: V06 V07
- deletion/fidelity: V08 V11
- uncertainty: V12

A later smart/global reader may add a blocker to an `MVI_RESULT: CLEAR`. It may never convert a surviving MVI blocking flag into a clear during this run.

## Durable evidence

Create directory:

`tasks/somatic-r15-clean-continuation-20260830/mvi-independent-001/`

Persist:

- `V01-RAW.md` through `V12-RAW.md` — exact raw judge outputs;
- `V01-RECEIPT.json` through `V12-RECEIPT.json` — one mechanical receipt per judge;
- `AGGREGATE.json` — exact parsed verdicts and mechanical aggregate;
- `RUN-RECEIPT.json` — complete transport/capture receipt.

Each judge receipt must include:

- run id and judge id;
- exact candidate path/blob/SHA-256;
- owner-source path/blob/SHA-256 only for V11;
- model/mode as displayed;
- fresh-context/transport identity that does not expose secrets;
- start/completion timestamps;
- raw-output Git blob and SHA-256 after persistence;
- parsed verdict/span/reason or schema failure;
- `saw_other_judge_outputs: false`;
- `saw_drafting_history: false`;
- `saw_detector_history: false`.

`RUN-RECEIPT.json` must include:

- actual starting branch/head;
- all evidence pins expected/observed;
- `fresh_contexts_opened: 12`;
- `judge_context_reuse_count: 0`;
- `model_aggregator_contexts_opened: 0`;
- exact V01–V12 parsed verdicts;
- exact mechanical `MVI_RESULT`;
- `prose_rewrites: 0`;
- `article_mutations: 0`;
- `registered_master_mutations: 0`;
- `detector_actions: 0`;
- `pangram_calls: 0`.

Commit all evidence in one narrow commit after the twelve judge outputs and receipts plus aggregate/run receipt are complete. If runtime durability requires intermediate commits to prevent loss, intermediate evidence-only commits are allowed; never rewrite an already captured raw judge response.

## Hard stops

Stop immediately if:

- any pinned evidence identity fails;
- twelve truly separate fresh contexts cannot be created;
- any judge is accidentally shown another judge's output;
- the candidate changes during the run;
- Codex would need to semantically interpret a verdict to compute the aggregate;
- the run would require rewriting prose, opening a writer, running Pangram, or mutating article authority.

Do not repair a malformed judge response by asking that same context again. Treat it as `ABSTAIN/schema_failure` and continue only if the remaining mechanics remain valid.

## Return contract to Joel

After evidence is committed, return only:

```text
SOMATIC_INTRO_INDEPENDENT_MVI 001
START_HEAD: <sha>
CONTEXT_ISOLATION: PASS | FAIL
JUDGES_COMPLETED: <n>/12
V01: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V02: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V03: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V04: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V05: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V06: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V07: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V08: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V09: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V10: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V11: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
V12: FLAG | CLEAR | ABSTAIN | SCHEMA_FAIL
MVI_RESULT: BLOCKED | INCONCLUSIVE | OWNER_QUERY_REQUIRED | CLEAR
EVIDENCE_PATH: tasks/somatic-r15-clean-continuation-20260830/mvi-independent-001/
EVIDENCE_COMMIT: <sha>
PROSE_REWRITES: 0
DETECTOR_ACTIONS: 0
```

Do not include prose, rewritten alternatives, a global editorial verdict, or recommendations. Stop after returning this receipt.