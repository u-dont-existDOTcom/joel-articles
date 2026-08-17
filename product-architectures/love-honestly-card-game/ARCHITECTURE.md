# Love, Honestly v0.3.0 Game Architecture

Status: durable private product-architecture snapshot for the released standalone game. This branch is intentionally not merged into the article-governance `main` branch. The complete project history is carried by the verified Git bundle.

This is the canonical operational map. Update it whenever a consequential phase, safety exit, serialized record, category default, source boundary, or setup-to-revisit dependency changes.

## Player flow

```mermaid
flowchart TD
    W["Welcome: title, exact Romance Guide link, compact source disclosure"] --> S["Setup: route, depth, length, topics"]
    S --> HA["Private safety handoff: person A"]
    HA --> SA["A: freely answer, skip, pause, stop?"]
    SA -->|"No or unsure"| STOP["Anonymous joint-game stop"]
    SA -->|"Yes"| HB["Private safety handoff: person B"]
    HB --> SB["B: freely answer, skip, pause, stop?"]
    SB -->|"No or unsure"| STOP
    SB -->|"Yes"| EA0["Private card + evidence basis: A"]
    EA0 --> EA1["Private same card + evidence basis: B"]
    EA1 --> D["Share answers; listener mirrors before arguing"]
    D --> CA["Private classification: A"]
    CA --> CB["Private classification: B"]
    CB --> U{"Either marked Not safe to resolve here?"}
    U -->|"Yes"| USTOP["Anonymous topic stop; no reality experiment"]
    U -->|"No"| C["Reveal two classifications without merging them"]
    C --> R{"Schedule overt reality step?"}
    R -->|"No"| N["Next card or evidence map"]
    R -->|"2 days / 1 week / 1 month"| P["Store card-specific experiment when present; otherwise deterministic category experiment"]
    P --> N
    N -->|"More cards"| EA0
    N -->|"Finish"| M["Evidence map: two perspectives, no score"]
    M --> RV["Open scheduled revisit"]
    RV --> RA["Private ordinary-life result + discrepancy: A"]
    RA --> RB["Private ordinary-life result + discrepancy: B"]
    RB --> RC["Reveal two revisit results"]
    RC --> M
```

## Epistemic dependency

```mermaid
flowchart LR
    Q["Card prompt"] --> T["Independent testimony"]
    T --> E["Evidence-basis label"]
    E --> X["Shared conversation + corrected mirror"]
    X --> J["Two private judgments"]
    J --> O["Overt ordinary-life experiment"]
    O --> V["Delayed two-person revisit"]
    V --> M["Evidence map"]

    CLOSE["Felt closeness"] -. "may be real but is not equivalent to" .-> O
    BODY["Arousal or body response"] -. "never proves someone should stay" .-> M
    INTENSITY["Spiritual or sexual intensity"] -. "is not durable integration" .-> O
    SCORE["Compatibility score"] -. "deliberately absent" .-> M
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

    SPOKEN["Spoken answers"] -. "not stored" .-> STORE
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

## Non-negotiable invariants

- The exact first-screen link remains `Based on the U-Dont-Exist Romance Guide` → `https://romance.u-dont-exist.com`.
- Joel’s guide remains the product authority; additional credits do not imply joint authorship.
- The card-function matrix governs extend/add/omit decisions and blocks paragraph-by-paragraph deck inflation.
- Existing v0.2.1 card IDs and storage schema v2 remain stable.
- Two private classifications and two private revisit records remain separate.
- A safety stop remains anonymous.
- Reality steps are overt. Card-specific experiments override category fallbacks; secret tests are prohibited.
- Sexual, flirtation, receiving, rank, role-play, and spiritual cards preserve the explicit non-obligation and abuse boundaries.
- A scheduled reality plan becomes complete only after both people submit a revisit.
- No compatibility score may be added without an explicit product-authority change.
- Spoken answers, card prose, and source metadata remain outside serialized session data.
- The application makes no automatic external request; the Romance Guide link is user-initiated navigation only.
