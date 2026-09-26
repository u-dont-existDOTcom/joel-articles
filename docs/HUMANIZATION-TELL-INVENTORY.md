# Humanization tell inventory (numbered)

Status: **current inventory for the post-generation tell ledger and the fresh-context sweep** (2026-09-26).

`HUMANIZATION-FRESH-CRITIC-GATE.md` requires "the complete current tell inventory" with every tell ID answered exactly once. This is that inventory. Every applicable tell gets a PRESENT, ABSENT or UNCERTAIN disposition on the literal candidate. A PRESENT or UNCERTAIN row is resolved (repaired, or rejected with an exact editorial reason) before any Pangram call.

How it's used:
- Apply it after drafting, never as a writing checklist (`SKILL.md`, "Post-generation tell ledger and repair").
- The fresh-context sweep prompt is built from this file by `articles/inner-child-therapy/tools/build_sweep_prompt.py`.
- Joel's corrections that belong here get a new ID. IDs are never reused or renumbered.

Calibration:
- **Part A (T01–T12)** is copied verbatim from the Pangram lab's global tell prompt (`pangram-humanization-lab/state/generation/global-tell-model-comparison-20260923/global-tell-prompt.txt`). Its model calibration is recorded in `pangram-humanization-lab/state/generation/GLOBAL-TELL-CALIBRATION-COVERAGE-20260923.md`: T02 two-sided; T03–T09 positive-only; T01 and T10–T12 unscored.
- **Parts B and C** come from Joel's corrections and the repository catalogs. They're uncalibrated for model sweeps, so a model's PRESENT on them is a lead for editorial review, not proof.

General rules for every row:
- PRESENT means the operation is actually happening in this prose, not that a surface form associated with it appears.
- A list, first person, direct advice, a rhetorical question, a short sentence, a fragment, a colloquial word, a metaphor, a polished sentence, a joke or an organized structure is not a tell by itself.
- Organization is not a tell. An essay can follow the source's order and read human when it notices things along the way (Joel, 2026-09-26).
- Human-looking features don't cancel a tell that is present, and one tell doesn't force another.

## Part A — calibrated global tells (verbatim from the lab)

**T01 — fake personal stake / irrelevant first-person authority.** First person inserts the author's preference/want/care as pseudo-personal authority without a reader-relevant reason. Do not flag source-earned first person merely because it is first person.

**T02 — cumulative instruction-manual / compressed-listicle cadence.** At paragraph/section scale, consecutive compressed commands, verdicts, questions, conditions, distinctions, or lessons each do one clean teaching job and hand off to the next. A list, imperative, direct advice, or question alone is not this tell.

**T03 — abrupt complication without reader-visible setup.** A new concern/distinction appears because the requirements/source ledger needs it, but the previous visible thought does not generate why it matters now.

**T04 — scene-skinned semantic staircase.** A concrete/coherent scene merely skins the same source-function checklist: each scene beat maps one-for-one to a protected obligation in source-ledger order.

**T05 — synthetic/didactic prop continuity.** Concrete details are unusually convenient, mainly selected to carry the next teaching/source function, and are largely interchangeable rather than causally load-bearing.

**T06 — generic therapeutic abstraction.** Generic therapy-safe abstraction appears where the prose sounds concrete, e.g. vague grief/old thing/healing/process language that summarizes instead of carrying a specific lived relation.

**T07 — simulated spontaneity / fake filler as transition camouflage.** Hesitations, fragments, colloquial fillers, or self-talk function mainly as stage directions between engineered beats rather than arising from a real thought-turn.

**T08 — concrete image followed by explanatory aftercare / overcompletion.** A concrete beat already performs the function, then the next sentence immediately translates, explains, moralizes, or summarizes what it means.

**T09 — equalized / optimal semantic efficiency.** Nearly every sentence or fragment advances the assignment with similar efficiency; nothing receives disproportionate attention because it actually became interesting.

**T10 — generic permission syntax.** Generic therapeutic permission packaging such as 'you don't have to X before Y' carries a requirement as a reusable counseling formula rather than an earned local relation.

**T11 — generic bridge / connective tissue.** A transition mainly announces or connects document functions rather than being required by the live thought; polished bridge language could move between many topics.

**T12 — symmetry / balanced contrast / tidy taxonomy.** Matched A/B cases, balanced categories, or a closed taxonomy package the thought into neat coverage. Do not flag genuine open hypothesis enumeration or a naturally necessary contrast merely because it has multiple items.

## Part B — tells from Joel's corrections and the catalogs (uncalibrated)

**T13 — nothing noticed inside the organization.** The order makes sense, but each sentence only fills its slot. No counterexample, reason, irony, aside or callback comes up out of the material while it's being said, so the section could be regenerated from its outline. Source: Joel, 2026-09-26 ("your organization needs to be not reducible to code ... it needs to notice things naturally in the midst of the organization"). Not the same as T09, which is about equal weight.

**T14 — organization chosen to dodge the detector.** Material is reordered, ranked, cut or moved to another section because the draft read AI, not because the new order reads better. Visible as an order the sense doesn't need, or a point that has gone missing. Source: Joel, 2026-09-26 ("you can't just move stuff around willy nilly to humanize it if it needs to be in a certain order to make it read right").

**T15 — humanizer rewording.** Words and phrases swapped for less likely ones while the structure and the other tells stay, including between repair rounds. Pangram flags this as "paraphrased or rewritten". Reusing a phrase from a failed draft is not this tell. Source: self-audit rule B10 as rewritten 2026-09-26.

**T16 — reflex negative reveal.** "That's not X. It's Y.", "not X — it's Y", or "isn't X, it's Y" used as a default move. A contrast that answers a real dismissal the reader has isn't this tell. Source: canonical bans; Joel's saved preferences.

**T17 — finished principle.** A compressed thesis line hands the reader a completed principle ("X can be Y and still Z"), including first-person aphorisms. Source: self-audit B1 and E24.

**T18 — premise and knock-down.** A premise followed by a short sentence that just flips it. Source: self-audit B3.

**T19 — announcing setup.** A sentence whose only job is to announce what comes next, including list announcements. Source: self-audit B5; banned patterns.

**T20 — engineered landing.** A paragraph built to land on a clever closer, or several paragraphs in a row ending on short polished lines, antitheses or quote-card phrasing. Source: self-audit B7 and B13; banned patterns ("successive paragraph-ending aphorisms").

**T21 — condensed function list.** One sentence does several argumentative jobs in coordinated clauses. Source: self-audit E15.

**T22 — coach register.** A calm, validating voice that only reassures, instructs or anticipates feelings ("you can start by", "at some point you'll want", "that's fine", "the next step is"), with no stance, reason, argument or humor coming out of a thought. Source: self-audit E41.

**T23 — generic-specific scenery.** Details that sound concrete but fit every reader (the song you skip in the car, your face is still wet), used in advice as if they were someone's specifics. Source: self-audit E36.

**T24 — faux-insight setup or self-answered question.** "Here's the thing", "what nobody tells you", or a question answered straight away to manufacture suspense. A real reader's question answered flatly isn't this tell. Source: banned patterns.

**T25 — colon reveal.** A noun phrase plus colon used for fake drama instead of a real list, label, quotation or grammatical relation. Source: banned patterns.

**T26 — unearned repetition.** A distinctive word, idea or phrase repeated within three paragraphs, or reused elsewhere in the piece, without the repetition doing anything. Source: banned patterns; self-audit D5.

**T27 — Joel's tic words.** "doing some work", "load-bearing", "tells on itself", "digest" or "metabolize" as metaphors, "clean" as praise, vague "work" or "does its work", "corollary", "to be clear", repeated "honestly". Source: canonical bans; Joel's saved preferences.

**T28 — forced closure or uplift.** The section ends on healing, a lesson, reassurance or a summary of what the reader learned, instead of where the material actually stops. Source: `project-sources/STRUCTURAL-HUMANITY.md` section 13; banned patterns.

## Part C — editorial checks the sweep also answers (uncalibrated)

**C01 — naming.** The inner child is called "the kid". Warm names are required ("your little one", "the inner child"). Source: self-audit E1.

**C02 — referent.** A pronoun, name or example points at the wrong person or thing, or at something the reader hasn't seen yet. Source: self-audit A12, E8, E33.

**C03 — invented first-person fact.** A first-person claim about Joel's life, feelings or practices that he didn't supply. Source: `STRUCTURAL-HUMANITY.md` section 22; Joel's saved preferences.

**C04 — unsupported named-entity claim.** A claim about a study, person, product or fact that isn't sourced, or that says more than the source does. Source: Joel's saved preferences; citation rules.
