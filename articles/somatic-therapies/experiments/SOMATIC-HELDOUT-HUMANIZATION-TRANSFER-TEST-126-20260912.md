# Somatic held-out humanization transfer test 126

Date: 2026-09-12
Status: **EXECUTED / ARCHITECTURE A FAIL / ARCHITECTURE B CLEANER BUT FAIL / CRITIC INDEPENDENCE DEGRADED / NO PANGRAM / NO ARTICLE INSTALL**

## Objective

Test whether the Stage-2 humanization method transfers to a different passage by measuring untouched first-pass generation quality. This is a generator-learning experiment, not article completion.

Controlling owner correction: `work/stage2-humanization-goal-correction-125.json`.
Source strategy: `articles/somatic-therapies/experiments/SOMATIC-STAGE2-FRESH-WRITER-SEMANTIC-CUSTODY-STRATEGY-094-20260911.md`.

## Frozen held-out source

Source artifact: `articles/somatic-therapies/WORKING-MERGED-READER-PROSE-20260905.md`.
Source Git blob: `4bf5535647af6c52d3daf27e296a7bbfe207eb6e`.
Boundary: start at `# Stage 3: Work With Trauma Feelings Before the Story Comes In`; include the Stage-3 opening and complete `## Brainspotting` subsection; end after the `Further reading` line; exclude `## After Brainspotting` and later material.

This source is working model-written prose, not owner-final wording. It has recoverable semantics and had not been through the Stage-2 fresh-writer/local-pressure process before this test.

## Architecture A — small positive method packet

Writer packet: `SOMATIC-HELDOUT-STAGE3-FRESH-WRITER-PACKET-127-20260912.md`.

Method exposed to writer:
1. recover the actual thought;
2. follow one live reader pressure;
3. use only semantic material needed for that pressure;
4. let the thought persist naturally;
5. stop when the thought stops.

The packet nevertheless contained several semantic relations at once: body-before-story, Brainspotting method relation, fit to diffuse/pre-verbal/body-held material, and a dose distinction.

Fresh writer: separate Replit document-agent context, not the supervising Chat context.
Replit app id: `7d273a30-c7ae-467d-a189-f6b23b332ed3`.
First-pass SHA-256: `930f732c26a449651cb782284a99ee73ccedc723480a3a5d314b2d021b678103`.
First-pass bytes: 1135.
First-pass words: 179.
Status: `UNTOUCHED_FIRST_PASS`.

Exact first pass:

> Brainspotting lets someone work with the felt material itself: the tightness, heaviness, heat, trembling, numbness, pressure, or emotional charge that is present even when its meaning is not yet clear. Rather than requiring a clean account of what happened, it uses gaze and bodily attention, held within the therapist’s attunement, to stay with what the system is already expressing.
>
> That can make it relevant for diffuse developmental, pre-verbal, or otherwise body-held material, where the response is more accessible than the memory or explanation. The person may know that something is happening without knowing what it belongs to, when it began, or how to put it into words. Here, the work is not to force that response into a story. It is to attend to the charged material at the level where it is available.
>
> The dose matters. Staying carefully resourced and approaching the material in small, tolerable amounts is different from deliberately entering highly charged developmental material. Both may involve what comes before a coherent story, but they ask very different things of the person’s capacity to remain present.

### Architecture A first-pass assessment

Architecture: **FAIL**.

Observed defects before preservation:
- preservation/semantic serialization reappeared as consecutive jobs: define felt material -> name fit/population -> add dose qualification;
- hidden enumeration in the opening sensation catalogue and secondary triads;
- complete mini-essay shape across three paragraphs;
- explanatory aftercare in the negative/positive clarification and final capacity sentence;
- false symmetry in `Both may involve ... but ...`;
- repeated conceptual job switching from phenomenology to method to fit to dosing to capacity;
- the central body-before-story point was restated several times rather than allowed to land once.

The writer's own post-freeze self-critique independently returned `FAIL` and identified the same main classes: completed explanatory mini-essay, hidden enumeration, aftercare, false symmetry, job switching, restatement, list-shaped compression, packaged contrast, and an over-resolved ending. This self-critique is useful but is **not independent critic evidence** because it came from the producing Replit context.

Estimated critic repair burden: **high**; at least three structural movements would require reconstruction rather than sentence polishing.

Preservation/reverse traceability: **NOT RUN** because architecture failed. No missing semantic material was appended.

## Architecture B — single-nucleus packet

Trigger: Architecture A reproduced the Stage-2 structural failure family. Per owner rule, do not add another prohibition; change generation architecture.

Writer packet: `SOMATIC-HELDOUT-STAGE3-SINGLE-NUCLEUS-PACKET-129-20260912.md`.

Structural change: withhold the fit categories and dose distinction entirely. Give the writer only one semantic nucleus: difficult material can be felt before coherent story, and Brainspotting can stay with that felt material through gaze, bodily attention, and therapist attunement without requiring clean narration first.

Fresh writer: second separate Replit document-agent context.
Replit app id: `aa31661f-3905-4e3c-bb87-6e7668b02002`.
First-pass SHA-256: `6ee61cc41b6ad9dd47e2ae3ddc9f34eacbb80bb9f1c5fda806f6a67abaf14da4`.
First-pass bytes: 834.
First-pass words: 140.
Status: `UNTOUCHED_FIRST_PASS`.

Exact first pass:

> Stage 3: Work With Trauma Feelings Before the Story Comes In
>
> Brainspotting can work with difficult material that is already being felt, even when it has not yet become a coherent story. A person may not have a clear sequence of events or language that neatly explains what is happening. What is present may instead be an emotionally charged feeling, a bodily sensation, or a sense that something difficult is there without a complete narrative around it.
>
> Here, the work does not have to wait for the person to tell the story clearly. Through gaze, bodily attention, and therapist attunement, Brainspotting can stay with the felt material as it is. The person does not have to organize it into a clean account before it can receive attention. It can be approached first as something experienced rather than something fully explained.

### Architecture B first-pass assessment

Architecture: **FAIL, but materially cleaner than A**.

Improvements relative to A:
- one conceptual job persists across the whole passage;
- fit/population and dosing obligations no longer become later paragraph jobs;
- no separate safety/capacity close;
- no two-case dose symmetry;
- lower repair burden.

Remaining defects:
- the same point is paraphrased repeatedly: not a coherent story -> no clear sequence/language -> no complete narrative -> need not tell story clearly -> need not organize clean account -> experienced rather than fully explained;
- a smaller hidden enumeration remains in `emotionally charged feeling, bodily sensation, or a sense...`;
- the second paragraph becomes explanatory aftercare rather than a new necessary movement;
- the final `experienced rather than fully explained` contrast neatly closes and interprets a distinction the reader already has.

Estimated critic repair burden: **moderate / one major stopping-point reconstruction**, substantially lower than A.

Preservation/reverse traceability: **NOT RUN** because architecture still failed.

## Critic independence status

The protocol called for a genuinely fresh architecture critic before preservation defense. A separate fresh critic launch was attempted after both candidates were frozen. The available separate Replit agent route hit its daily free quota and could not create the critic context. Therefore:

`CRITIC_INDEPENDENCE = DEGRADED`

No same-context review is represented as independent evidence. Architecture A has a producer self-critique plus supervising-context gate. Architecture B has the supervising-context gate; two attempts to obtain a producer self-critique timed out and produced no usable critic artifact.

This limitation does not change the first-pass texts or their frozen identities, but it lowers confidence in the critic layer. Owner review remains especially informative.

## Transfer judgment

The Stage-2 method **did not transfer successfully in its Architecture-A form**. Familiar failures recurred in a genuinely fresh writer despite not being named in the writer packet.

The comparison is informative:

- A exposed multiple semantically legitimate relations at once and the writer serialized them into a polished three-part explanation.
- B withheld all but one semantic nucleus. This substantially reduced conceptual job switching and closure burden.
- B still over-explained the one remaining thought through paraphrastic restatement and a tidy final contrast.

This supports a narrower causal lesson than `one live thought fixes humanization`:

> **Semantic packet breadth is itself a generative control variable. A packet can nominally describe one reader pressure while still carrying several independently completable relations, and the generator tends to realize those relations as prose jobs. Reducing the packet to one semantic nucleus materially improves first-pass architecture, but does not by itself remove the generator's tendency to restate and complete the nucleus after the reader already has it.**

Do not convert the remaining failure into another blacklist item. The next method comparison should alter the generation process itself—for example by separating ordinary spoken answer-generation from publication realization, or by using an independent stop-controller that decides whether the live thought still has unresolved content before another sentence is generated. Those are hypotheses, not promoted lessons.

## Progress against owner outcome

Owner outcome: learn and validate a generalizable humanization method.

Direct result of this held-out test: **STRATEGY LEARNING, not success**.

- transfer success demonstrated: **NO**;
- first-pass Architecture A: **FAIL**;
- structurally different Architecture B: **FAIL, materially improved**;
- known failure recurrence without writer-side warning: **YES**;
- critic repair burden reduced under B: **YES, high -> moderate**;
- owner correction burden measured: **PENDING OWNER READ**;
- preservation intact: **NOT YET TESTED because architecture never passed**;
- Pangram: **NOT RUN / NOT AUTHORIZED**;
- article authority changed: **NO**;
- publishing/citation/Stage-2 completion work resumed: **NO**.

## Durability / promotion disposition

This is one held-out comparison on one article boundary. Persist it in `joel-articles` as project-local experimental evidence. Do **not** yet promote the single-nucleus finding to `pangram-humanization-lab` as a general lesson. Promotion requires replication on another target or stronger cross-context evidence.
