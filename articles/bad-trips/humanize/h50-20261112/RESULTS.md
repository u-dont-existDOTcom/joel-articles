# Turn 40 (2026-11-12): the rescue medicine and the evidence paragraph, after his fixes of 19:44 UTC

His fixes of 2026-11-12 19:44 UTC (`../../experiments/t38-answers/JOEL-VERSIONS-20261112-1944.md`), in whole
(`../../review/r38/apply_r38b.py`), with "we need to have a better sense check in general". The three lines he cut were
each true anyway of someone tripping or overdosing, or something a friend couldn't tell; every read I had passed them.
The fit read (`../../../../tools/humanization/fit_read_brief.md`, scored in `FIT-CALIBRATION.md`, gate
bad-trips-2026-11-12j) asks that of every line before a check.

Each draft went through the needed read, the read against his fixes and the fit read before any check (`reads/`,
`NEEDED.json`, `HIS-FIXES.json`, `FIT.json`, each mark changed or kept with its reason), with its receipt
(`make_receipts.py`), the fidelity check (`apply_h50.py --dry`, PASS with `../h01/FIDELITY-KEYS-R39.json`) and its
prediction (#467 to #472, `predict.py`).

Active Seizure's rescue medicine (B110): ten drafts. The reads moved it from "give it the way it's meant to be given" to
the label, from a bare risk at the end to what to watch, and from three ", since" clauses to varied ones; the read against
his fixes kept asking to cut "what doctors reach for first" (the guide's first-line evidence, with its link) and to say
when to give it (the label's job, not a time of mine).

| test | what | result | link |
|---|---|---|---|
| rescue-c8 | the section with the paragraph after eight drafts: the action first ("follow its label for when and how to give it"), what it is, its forms, what to watch after, in his call list's words ("slow and shallow") | AI Detected, 17%: his lists Human High and Medium; my action Human Low, then AI Low 44 over "These are benzodiazepines, the same first drugs doctors reach for ..." and "They come in forms you don't have to swallow ...", then Human Low | [ed4fe070](https://www.pangram.com/history/ed4fe070-ae91-4317-b946-a25cfd4bf60f) |
| rescuep-c9 | the paragraph by itself (the ledger's narrowing after a Mixed section), the class said of what they hold ("It's a benzodiazepine, which is what doctors reach for first ..."), the forms with their reason first | AI Generated, 100%: AI Medium 43, AI High 25, AI Low 32 | [9f5b6765](https://www.pangram.com/history/9f5b6765-c18b-4d59-9d64-036539a08f20) |
| rescuep-c10 | the paragraph by itself in his first person ("I'd give it when and how its label says", "I'd keep a close eye on their breathing") | AI Detected, 79%: AI Low 26, AI Low 18, Human Low 25 (the forms), AI High 37 (the breathing sentence) | [cdc63980](https://www.pangram.com/history/cdc63980-b7da-43a7-b684-819d7d4ac1c8) |
| rescue-c10 | rescuep-c10 back in its section | Human Written, 0%: his lists High and Medium; my four sentences Human Medium 26, Low 18, High 25, Low 37 | [8522369e](https://www.pangram.com/history/8522369e-b999-481a-84c0-3ab4c0518bef) |

rescue-c10 is in the guide (`apply_h50.py rescue-c10`). Its two Low windows ("It's a benzodiazepine, the kind of drug
doctors reach for first when a seizure won't stop." and the breathing sentence) are mine to fix; the section lineage has
used its two tries and the paragraph lineage has read AI twice, so the next try goes through the tell panel first.

My Brain Feels Damaged's evidence paragraph (B105):

| test | what | result | link |
|---|---|---|---|
| brainev-c1 | his belief first as it is; "That judgment is stronger than the clinical evidence, but the evidence is not empty" said plainly; one study a sentence in the reader's words; the animal study ending on "so it may still help if you start late" | AI Detected, 72%: heading and belief Human Low; AI Medium 15, Low 19, Low 19, High 30 (the animal study), Medium 19 | [a8a986e7](https://www.pangram.com/history/a8a986e7-f324-4e8a-9561-b542fa57b413) |
| brainev-c2 | rebuilt around the finding the reader can act on: the animal study first, the two findings in people in one sentence, the mechanism said plainly with its term in brackets (his shape) | AI Generated, 100%: AI Medium 32 (heading and belief), AI High 108 | [f7576565](https://www.pangram.com/history/f7576565-13c8-47d2-9ecb-02e2a092f284) |

It read AI built two ways, so it is round 39's teaching card (`../../review/r39/`, TEACH-EVID); B105 stays as it is
until his version.

What this round showed: by itself, every sentence of mine that explains in the guide's impersonal register read AI
(rescuep-c9); his first person moved one window of four (rescuep-c10), and beside his lists the same paragraph read
Human (rescue-c10). acute-c1 (97bf9589, Human High) was also mine in his first person. That is two carries, so it is a
note for the next ones, not yet a lesson. On his own Active Seizure lines the fit read kept marking "over 5 minutes" (an
epilepsy rule, it says, since a seizure from a drug is already an emergency) and "dangerously hot" (no thermometer);
both stay as he wrote them, told to him on round 39's page.
