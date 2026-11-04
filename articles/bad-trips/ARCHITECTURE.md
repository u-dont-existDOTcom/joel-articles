# Bad Trips guide architecture

<!-- article-id: bad-trips -->

Indexes: `articles/bad-trips/CURRENT-STATE.md` + `articles/bad-trips/master.md` + `articles/bad-trips/GUIDE-SO-FAR.md`

This graph is a visual index over canonical article state. If it conflicts with registered authority, repair the graph.

## Overview

His guide after round 2 (`GUIDE-SO-FAR.md`; his post itself is `master.md`): a quick checklist whose 15 steps each
keep their heading and one or two of his lines and end with "More:" and a link to their section, the call-for-help
section (with When Peer Support Isn't Enough in it), the medical and neurological emergencies (the brain-damage section
ends with the Core Order list), his rescue remedies, then the tripsitting how-to and the shadow-work essays, integration
and resources. The Longer Triage is gone (his structure answer ST-1, A, 2026-11-03 18:59 UTC, carried out by round 2's
cards, all approved 2026-11-04 10:26 UTC); the four things only it said moved into the long part (LT-2 to LT-5).

```mermaid
flowchart TD
    check["Quick Bad Trip Checklist — job: 15 steps in order, from medical danger to love"]
    app["Inner Signal App to the Rescue! — job: the app built from his guides"]
    help["When to Bring In Outside Help — job: when to call medics, when to get mental-health support, when peer support isn't enough"]
    acute["Acute Medical and Neurological Rescue — job: brain-damage feeling, seizure, MDMA, chest pain, oral toxic ingestion, serotonin syndrome"]
    remedies["My Acute Rescue Hierarchy — job: gut tools, nausea smoothers, stopping a trip, stabilizers, niacin, remedies needing caution"]
    sit["Shadow Work and Tripsitting — job: first five minutes, one human anchor, who to contact, alone at 3 a.m., the person helping, grounding, no rash actions"]
    essays["The shadow-work essays — job: what a bad trip is, the two bypasses, the healing treadmill, sorrow, demons, memories, shadow thoughts"]
    after["After the Storm — job: integration and the kinds of aftermath"]
    res["Appendix: Additional Resources"]
    check --> app --> help --> acute --> remedies --> sit --> essays --> after --> res
    check -. "each step's More: link" .-> help
    check -. "each step's More: link" .-> acute
    check -. "each step's More: link" .-> remedies
    check -. "each step's More: link" .-> sit
```

## Important dependencies

```mermaid
flowchart LR
    brain["Checklist: my brain feels damaged"] -. "full branch" .-> rescue["Acute rescue: DMSO first, then by drug"]
    rescue -. "ends with" .-> core["The Core Order list (moved here in round 1)"]
    core -. "pes-caprae, magnesium" .-> rem["The pes-caprae and magnesium sections"]
    help["Outside help: the two lists"] -. "with, since round 1" .-> peer["When Peer Support Isn't Enough"]
    chk3am["Checklist: alone at 3 a.m."] -. "the long version refers back" .-> long3am["Tripsitting: Alone at 3 a.m."]
    stable["What counts as stable, and the ER's limits (from the Longer Triage, LT-3)"] -. "under the rescue section's first paragraph" .-> rescue
    emo["Real emotional material (LT-4)"] -. "before Do, in For the Person Helping" .-> sit2["For the Person Helping"]
    horror["The body writing the horror story (LT-5)"] -. "into the hierarchy, before the gut tools" .-> rem
```

## Authority / placement notes

- Current topology: the guide after round 2 (`review/r02/GUIDE-AFTER-R02.md`, made by `review/r02/apply_r02.py` from
  round 1's guide, `review/r01/GUIDE-AFTER-R01.md`, and his round-2 answers), with the standard typographic swap
  (`humanize/h01/swap.py`) as `GUIDE-SO-FAR.md`: the checklist's steps short, each with its More: link; the Longer Triage
  gone; its reassuring-screen line in the brain-damage checks, what counts as stable and the ER's limits under the rescue
  section's first paragraph, real emotional material before Do, and the body writing the horror story in the hierarchy.
  From round 1: When Peer Support Isn't Enough in When to Bring In Outside Help; the Core Order list in the brain-damage
  section; one appendix heading.
- Settled placements: "Hello, Lovey Bunny!" stays where it opens the shadow-work half (Q-2, a); the support lines stay
  in Get One Human Anchor (Q-8, a); the seizure threshold stays in both the medics list and Active Seizure (SF-2). All
  of them, with his words, are in `KEEP-AS-IS.json`.
- Protected functions: the remedies' fidelity (every remedy, dose, unit, timing and warning) and the call-for-help
  thresholds that stay inside each emergency (`OWNER-LOCKS.json`).

## Update rule

Update this file in the same substantive change whenever section order, protected-function placement, owner supersession
routing, setup/payoff dependencies, or the real stopping point changes. Cosmetic prose edits do not require graph churn.
