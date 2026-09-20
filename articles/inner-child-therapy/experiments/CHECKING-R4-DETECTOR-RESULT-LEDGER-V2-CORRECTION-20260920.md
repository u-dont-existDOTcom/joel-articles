# Checking R4 — ledger-pass detector result and ledger failure analysis

Date: 2026-09-20
Status: **R4 LEDGER FALSE POSITIVE / ALL THREE EXACT INPUTS PANGRAM AI 1.0**

R4 source:
`CHECKING-SENTENCE-TELL-LEDGER-FOUR-REALIZATIONS-20260920.md`.

The v1 ledger classified R4 as:
- strong A: 0
- strong H: 6
- E: 9

That editorial gate was too permissive.

## Exact Pangram 4.0 results

Model-only section, excluding owner P4:
- 207 words
- SHA-256 `a1d9a45787230aa23b612fbf7256973b81773f4d08ee728cc96cb4d6c46a14af`
- AI 1.0 / Human 0.0
- exact_utf8 History binding
- captured 2026-09-20T03:00:32.386862Z
- prediction probability 0.9990961552.

P2:
- 103 words
- SHA-256 `b2ef911e99c35a5b6fb16c3079bb7c32982ed68a77b89ca75f1cbd7969e46783`
- AI 1.0 / Human 0.0
- exact_utf8
- captured 2026-09-20T03:01:10.756526Z
- prediction probability 0.9917814136.

P3:
- 58 words
- SHA-256 `2a72c1c05ace6b110088b51fc815085089a86bfc029cebaab65ed17e50b23f8c`
- AI 1.0 / Human 0.0
- exact_utf8
- captured 2026-09-20T03:01:34.995020Z
- prediction probability 0.9945873022.

Transport: local Playwright GUI. No detector API. No owner/donor text, heading, padding or repeated exact input.

Evidence branch:
`u-dont-existDOTcom/pangram-humanization-lab@evidence/checking-r4-ledger-pass-20260920`.

## Why the v1 ledger failed

It credited **performative humanizers** as Human signals even though the model inserted them to satisfy the ledger:
- `Then—actually...` self-correction;
- `I've got no problem with that`;
- `What worries me...`;
- `If the thought follows you, it follows you`.

These markers changed surface texture without changing the underlying semantic staircase.

The passage-level plan still marched:
hook/qualification -> practical-first -> retrospective check -> useful branch -> author reaction -> checking branch -> grief caveat/new-request conclusion -> leave thought -> return to life -> meeting metaphor -> ritual stop.

Thus every protected unit still received a cleanly identifiable destination, even when individual sentences looked less polished.

## Ledger v2 correction

A Human-facing signal only counts positive if it is **functionally earned by the target/source**. A self-correction, aside, colloquial reaction, repetition, fragment, question or first-person stance added mainly to humanize the surface is a **synthetic humanizer**, not H.

The ledger must score two levels:

### Sentence/local signals
- A-local: known model-shaped realization;
- H-earned: source/argument requires the irregularity, stance, social act or unresolved relation;
- S: synthetic humanizer / decorative irregularity;
- E: weak/either.

### Passage/topology signals
Strong A-topology includes:
- preservation ledger visible as prose order;
- every sentence/paragraph has one obvious next function;
- symmetric useful/unhelpful branches;
- conclusion sentences that close each local distinction;
- repeated instruction -> explanation -> conclusion cycles;
- paragraph lengths different on paper but semantic units still equally complete.

Strong H-topology includes:
- one thought genuinely occupies several clauses/sentences because its internal problem requires it;
- another source function is compressed or delayed because it is subordinate;
- a real complication interrupts/revises the route;
- unresolved material survives into the next paragraph without an explanatory closure;
- short paragraph roles are explained by the larger map, not by uniform brevity.

### Gate

Before detector eligibility:
- zero unexplained substantive deltas;
- zero strong A-topology;
- zero synthetic-humanizer dependencies;
- no strong A-local that can be repaired without harming fidelity;
- at least two H-earned local/topological signals where the source actually affords them.

This gate is still heuristic; passing it does not predict Pangram or owner acceptance. R4 is the counterexample that keeps the gate honest.