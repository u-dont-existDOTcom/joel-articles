# Bad Trips guide architecture

<!-- article-id: bad-trips -->

Indexes: `articles/bad-trips/CURRENT-STATE.md` + `articles/bad-trips/master.md` + `articles/bad-trips/GUIDE-SO-FAR.md`

This graph is a visual index over canonical article state. If it conflicts with registered authority, repair the graph.

## Overview

His guide after round 1 (`GUIDE-SO-FAR.md`; his post itself is `master.md`): a quick checklist, a second, longer
triage, the call-for-help section (now with When Peer Support Isn't Enough in it), the medical and neurological
emergencies (the brain-damage section now ends with the Core Order list), his rescue remedies, then the tripsitting how-to
and the shadow-work essays, integration and resources. His structure answer (ST-1, A, 2026-11-03 18:59 UTC): the
checklist keeps each step's heading and one or two of his lines with a link to its section, and the Longer Triage goes,
its few unique paragraphs moving into the long part; round 2's page (`review/r02/`) proposes each step and move.

```mermaid
flowchart TD
    check["Quick Bad Trip Checklist — job: 15 steps in order, from medical danger to love"]
    app["Inner Signal App to the Rescue! — job: the app built from his guides"]
    triage["The Longer Triage — job: five questions on what kind of trouble this is"]
    help["When to Bring In Outside Help — job: when to call medics, when to get mental-health support, when peer support isn't enough"]
    acute["Acute Medical and Neurological Rescue — job: brain-damage feeling, seizure, MDMA, chest pain, oral toxic ingestion, serotonin syndrome"]
    remedies["My Acute Rescue Hierarchy — job: gut tools, nausea smoothers, stopping a trip, stabilizers, niacin, remedies needing caution"]
    sit["Shadow Work and Tripsitting — job: first five minutes, one human anchor, who to contact, alone at 3 a.m., the person helping, grounding, no rash actions"]
    essays["The shadow-work essays — job: what a bad trip is, the two bypasses, the healing treadmill, sorrow, demons, memories, shadow thoughts"]
    after["After the Storm — job: integration and the kinds of aftermath"]
    res["Appendix: Additional Resources"]
    check --> app --> triage --> help --> acute --> remedies --> sit --> essays --> after --> res
    check -. "repeated in (round 2: each step links to its section)" .-> sit
    triage -. "goes in round 2; its unique paragraphs move" .-> acute
```

## Important dependencies

```mermaid
flowchart LR
    brain["Checklist: my brain feels damaged"] -. "full branch" .-> rescue["Acute rescue: DMSO first, then by drug"]
    rescue -. "ends with" .-> core["The Core Order list (moved here in round 1)"]
    core -. "pes-caprae, magnesium" .-> rem["The pes-caprae and magnesium sections"]
    help["Outside help: the two lists"] -. "with, since round 1" .-> peer["When Peer Support Isn't Enough"]
    chk3am["Checklist: alone at 3 a.m."] -. "the long version refers back" .-> long3am["Tripsitting: Alone at 3 a.m."]
```

## Authority / placement notes

- Current topology: the guide after round 1 (`GUIDE-SO-FAR.md`, made by `review/r01/apply_r01.py` from his post and his
  round-1 answers): When Peer Support Isn't Enough moved into When to Bring In Outside Help; the Core Order list moved
  into the brain-damage section; the appendix has one heading.
- Settled placements: "Hello, Lovey Bunny!" stays where it opens the shadow-work half (Q-2, a); the support lines stay
  in Get One Human Anchor (Q-8, a). Open: round 2's cards (`review/r02/`).
- Protected functions: the remedies' fidelity (every remedy, dose, unit, timing and warning) and the call-for-help
  thresholds that stay inside each emergency (`OWNER-LOCKS.json`).

## Update rule

Update this file in the same substantive change whenever section order, protected-function placement, owner supersession
routing, setup/payoff dependencies, or the real stopping point changes. Cosmetic prose edits do not require graph churn.
