# Bad Trips guide architecture

<!-- article-id: bad-trips -->

Indexes: `articles/bad-trips/CURRENT-STATE.md` + `articles/bad-trips/master.md`

This graph is a visual index over canonical article state. If it conflicts with registered authority, repair the graph.

## Overview

His guide as it stands in his post (2026-11-03): a quick checklist, a second, longer triage, the call-for-help lists,
the medical and neurological emergencies, his rescue remedies, then the tripsitting how-to and the shadow-work essays,
integration and resources. The same advice runs through several of these parts (the round-1 marking page,
`review/r01/`, maps the repeats); the structure question there decides how the quick and long parts split the work.

```mermaid
flowchart TD
    check["Quick Bad Trip Checklist — job: 15 steps in order, from medical danger to love"]
    app["Inner Signal App to the Rescue! — job: the app built from his guides"]
    triage["The Longer Triage — job: five questions on what kind of trouble this is"]
    help["When to Bring In Outside Help — job: when to call medics, when to get mental-health support"]
    acute["Acute Medical and Neurological Rescue — job: brain-damage feeling, seizure, MDMA, chest pain, oral toxic ingestion, serotonin syndrome"]
    remedies["My Acute Rescue Hierarchy — job: gut tools, nausea smoothers, stopping a trip, stabilizers, niacin, remedies needing caution"]
    sit["Shadow Work and Tripsitting — job: first five minutes, one human anchor, alone at 3 a.m., the person helping, grounding, no rash actions"]
    essays["The shadow-work essays — job: what a bad trip is, the two bypasses, the healing treadmill, sorrow, demons, memories, shadow thoughts"]
    after["After the Storm — job: integration and the kinds of aftermath"]
    res["Appendix: Additional Resources"]
    check --> app --> triage --> help --> acute --> remedies --> sit --> essays --> after --> res
    check -. "repeated in" .-> triage
    check -. "repeated in" .-> sit
    triage -. "repeated in" .-> acute
```

## Important dependencies

```mermaid
flowchart LR
    brain["Checklist: my brain feels damaged"] -. "full branch" .-> rescue["Acute rescue: DMSO first, then by drug"]
    rescue -. "steps listed again" .-> core["Rescue hierarchy: the Core Order list"]
    core -. "pes-caprae, magnesium" .-> rem["The pes-caprae and magnesium sections"]
    help["Outside help: the two lists"] -. "same thresholds" .-> peer["Tripsitting: When Peer Support Isn't Enough"]
    chk3am["Checklist: alone at 3 a.m."] -. "the long version refers back" .-> long3am["Tripsitting: Alone at 3 a.m."]
```

## Authority / placement notes

- Current topology: his post as of 2026-11-03 (`master.md`); nothing has moved yet.
- Unresolved placement questions: how the quick checklist and the long guide split the work, and where "Hello, Lovey Bunny!"
  sits (`OWNER-QUESTIONS.md`, questions 1 and 3; the round-1 page's cards ST-1 and Q-2).
- Protected functions: the remedies' fidelity (every remedy, dose, unit, timing and warning) and the call-for-help
  thresholds that stay inside each emergency (`OWNER-LOCKS.json`).

## Update rule

Update this file in the same substantive change whenever section order, protected-function placement, owner supersession
routing, setup/payoff dependencies, or the real stopping point changes. Cosmetic prose edits do not require graph churn.
