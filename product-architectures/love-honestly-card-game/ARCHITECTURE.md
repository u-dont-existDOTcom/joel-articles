# Love, Honestly v0.3.2 Game Architecture

This is the canonical operational map for the standalone game. Update it whenever a consequential phase, safety exit, serialized record, category default, source boundary, or setup-to-revisit dependency changes.

## Player flow

```mermaid
flowchart TD
    W["Welcome: guide link, source disclosure, spoken-answer privacy"] --> S["Setup: route, depth, length, topics"]
    S --> HA["Private safety handoff: person A"]
    HA --> SA["A: freely answer, skip, pause, stop?"]
    SA -->|"No or unsure"| STOP["Anonymous joint-game stop"]
    SA -->|"Yes"| HB["Private safety handoff: person B"]
    HB --> SB["B: freely answer, skip, pause, stop?"]
    SB -->|"No or unsure"| STOP
    SB -->|"Yes"| AA0["A privately forms the actual open-ended answer"]
    AA0 --> EA0["A labels what that answer is based on"]
    EA0 --> AA1["B privately forms the same actual answer"]
    AA1 --> EA1["B labels what that answer is based on"]
    EA1 --> D1["Both answer the main question aloud; listener mirrors and speaker corrects"]
    D1 --> D2["Both answer the follow-up aloud; listener mirrors and speaker corrects"]
    D2 --> CA["Private classification: A"]
    CA --> CB["Private classification: B"]
    CB --> U{"Either marked Not safe to resolve here?"}
    U -->|"Yes"| USTOP["Anonymous topic stop; no reality experiment"]
    U -->|"No"| C["Reveal two classifications without merging them"]
    C --> R{"Schedule overt reality step?"}
    R -->|"No"| N["Next card or evidence map"]
    R -->|"2 days / 1 week / 1 month"| P["Store card-specific experiment when present; otherwise deterministic category experiment"]
    P --> N
    N -->|"More cards"| AA0
    N -->|"Finish"| M["Evidence map: two perspectives, no score"]
    M --> HOME["Return later: show scheduled review + target date"]
    HOME --> ANY["Review now remains available before / on / after target date"]
    ANY --> RV["Open scheduled revisit"]
    RV --> RA["Private ordinary-life result + discrepancy: A"]
    RA --> RB["Private ordinary-life result + discrepancy: B"]
    RB --> RC["Reveal two revisit results"]
    RC --> M
```

## Answer and epistemic dependency

```mermaid
flowchart LR
    Q["Card prompt"] --> A["Actual answer formed in the player's own words"]
    A --> E["Evidence-basis label about that answer"]
    E --> S1["Primary answer spoken aloud"]
    S1 --> M1["Corrected mirror"]
    M1 --> F["Follow-up answer spoken aloud"]
    F --> M2["Corrected mirror"]
    M2 --> J["Two private judgments"]
    J --> O["Overt ordinary-life experiment"]
    O --> V["Delayed two-person revisit"]
    V --> MAP["Evidence map"]

    META["Epistemic metadata"] -. "describes how the answer is known; never replaces" .-> A
    CLOSE["Felt closeness"] -. "may be real but is not equivalent to" .-> O
    BODY["Arousal or body response"] -. "never proves someone should stay" .-> MAP
    INTENSITY["Spiritual or sexual intensity"] -. "is not durable integration" .-> O
    SCORE["Compatibility score"] -. "deliberately absent" .-> MAP
```

## Safety routing

```mermaid
flowchart TD
    FREE["Freedom to answer and stop"] -->|"Both yes"| JOINT["Joint card flow"]
    FREE -->|"Either no/unsure"| PRIVATE["Anonymous stop; independent support"]
    JOINT --> CLASS["Private card classification"]
    CLASS -->|"Either Not safe"| TOPICSTOP["Anonymous topic stop"]
    CLASS -->|"Neither Not safe"| COMPARE["Comparison + optional reality step"]

    SEX["Touch, flirtation, erotic time"] --> NONOB["No sexual act, arousal, continuation, or reciprocity obligation"]
    ROLE["Role-play"] --> ADULT["Adult responsibility remains with each person"]
    LISTEN["Listen-or-solve exercise"] --> ABUSE["Never reframes intimidation, false accusation, coercion, or retaliation as style mismatch"]

    PRIVATE -. "never identify selector" .-> SECRET["Private choice remains private"]
    TOPICSTOP -. "never identify selector" .-> SECRET
```

## Stored-data boundary

```mermaid
flowchart LR
    STORE["Local v2 session"] --> IDS["Card IDs"]
    STORE --> SETUP["Names and setup choices"]
    STORE --> META["Evidence and classification labels"]
    STORE --> PLANS["Reality-step text, due dates, statuses"]
    STORE --> REVISITS["Per-person revisit labels"]

    PRIVATEANSWER["Private answer formation"] -. "no field and no serialization" .-> STORE
    SPOKEN["Spoken primary and follow-up answers"] -. "not stored" .-> STORE
    PROMPTS["Prompt / follow-up / why / source prose"] -. "not serialized" .-> STORE
    SOURCE["Structured source metadata"] -. "not serialized" .-> STORE
    FREE["Free-text answer fields"] -. "do not exist" .-> STORE
    CLOUD["Network / analytics / accounts"] -. "do not exist" .-> STORE
```

## Selection architecture

```mermaid
flowchart LR
    FILTER["Route + depth + explicitly enabled topics"] --> POOL["Eligible cards"]
    WEIGHT["Category weights"] --> PICK["Deterministic weighted selection"]
    POOL --> PICK
    PICK --> VARIETY["Avoid consecutive same-category cards when alternatives exist"]
    VARIETY --> RHYTHM["Insert bounded rhythm cards"]
    RHYTHM --> SESSION["Alternating-speaker session"]

    ORD["Ordinary / clarity / conflict / community"] -->|"higher weight"| WEIGHT
    OPTIONAL["Polarity / altered states / spiritual practice"] -->|"explicit opt-in and lower weight"| WEIGHT
    DEFAULTS["All optional categories off by default"] --> FILTER
```

## Card-function and experiment architecture

```mermaid
flowchart LR
    ARTICLE["Expanded Romance article concepts"] --> MATRIX["Card-function matrix"]
    MATRIX --> EXTEND["Extend existing card when function overlaps"]
    MATRIX --> ADD["Add card only for distinct function"]
    MATRIX --> OMIT["Omit when current deck already performs the job"]
    EXTEND --> UNIQUE["Unique articleUpdateFunction metadata"]
    ADD --> UNIQUE
    UNIQUE --> SPECIFIC{"Card-specific experiment present?"}
    SPECIFIC -->|"Yes"| CARDSTEP["Use exact card experiment"]
    SPECIFIC -->|"No"| CATSTEP["Use seeded category experiment"]
    CARDSTEP --> REVISIT["Schedule and revisit"]
    CATSTEP --> REVISIT
```

## Source and authority architecture

```mermaid
flowchart TD
    OWNER["U-Dont-Exist Romance Guide"] -->|"primary source and product authority"| GAME["Love, Honestly"]
    TOFT["Doug Toft"] -->|"specific long-marriage observations"| META["Structured source metadata"]
    ANAMI["Kim Anami"] -->|"simmer, receiving, sexual self-responsibility"| META
    BUDDHIST["Buddhist and lived spiritual-practice material"] --> META
    RESEARCH["Relationship research"] --> META
    META --> ABOUT["Compact About the sources disclosure"]
    META -. "not citations on each play card" .-> GAME
    ABOUT --> NOTE["Sources are not co-authors"]
```

## Backward recovery

- Legacy v0.3.0 `discuss` state renders as the new primary spoken-answer phase.
- Existing `private-evidence-*` phases remain readable rather than corrupting or discarding a saved session.
- New sessions always pass through `private-answer-*` before `private-evidence-*`.
- Card IDs and local-storage schema version 2 remain unchanged.

## Authority and invariants

- The exact first-screen link remains `Based on the U-Dont-Exist Romance Guide` → `https://romance.u-dont-exist.com`.
- Joel’s guide remains the product authority; additional credits do not imply joint authorship.
- The actual open-ended answer is a first-class phase and is spoken aloud; evidence labels are secondary metadata.
- The card-function matrix governs extend/add/omit decisions and blocks paragraph-by-paragraph deck inflation.
- Existing card IDs and storage schema v2 remain stable.
- Two private classifications and two private revisit records remain separate.
- A safety stop remains anonymous.
- Reality steps are overt. Card-specific experiments override category fallbacks; secret tests are prohibited.
- Sexual, flirtation, receiving, rank, role-play, and spiritual cards preserve the explicit non-obligation and abuse boundaries.
- A scheduled reality plan becomes complete only after both people submit a revisit.
- The target date is a reminder target, not an access lock. Pending reviews are surfaced on the welcome screen with the scheduled date and an explicit `Review now` action at all times.
- No compatibility score may be added without an explicit product-authority change.
- No answer field, spoken answer, card prose, or source metadata enters serialized session data.
- The application makes no automatic external request; the Romance Guide link is user-initiated navigation only.
