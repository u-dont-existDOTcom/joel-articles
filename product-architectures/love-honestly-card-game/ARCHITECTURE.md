# Love, Honestly v0.2.0 Game Architecture

Status: durable private product-architecture snapshot for the released standalone game.

This branch is intentionally not merged into the article-governance `main` branch. A future dedicated game repository should import this directory together with the full Git bundle. The map is an operational control surface, not authority to alter Joel's article.

## Core invariant

A deep answer is testimony, not proof. Preserve this sequence:

**Talk → identify evidence basis → preserve two private judgments → test openly in ordinary life → revisit privately → compare without scoring.**

Do not revert to v0.1's single negotiated outcome model.

## Player flow

```mermaid
flowchart TD
    W["Welcome: Talk · Test · Revisit"] --> S["Setup: route, depth, length, topics"]
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
    R -->|"2 days / 1 week / 1 month"| P["Store category-specific open experiment + due date"]
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
    J --> O["Overt ordinary-life observation"]
    O --> V["Delayed two-person revisit"]
    V --> M["Evidence map"]

    CLOSE["Felt closeness"] -. "may be real but is not equivalent to" .-> O
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
    PROMPTS["Card prompt / follow-up / why prose"] -. "not serialized" .-> STORE
    FREE["Free-text answer fields"] -. "do not exist" .-> STORE
    CLOUD["Network / analytics / accounts"] -. "do not exist" .-> STORE
```

## Selection architecture

```mermaid
flowchart LR
    FILTER["Route + depth + enabled topics"] --> POOL["Eligible cards"]
    WEIGHT["Category weights"] --> PICK["Deterministic weighted selection"]
    POOL --> PICK
    PICK --> VARIETY["Avoid consecutive same-category cards when alternatives exist"]
    VARIETY --> RHYTHM["Insert bounded rhythm cards"]
    RHYTHM --> SESSION["Alternating-speaker session"]

    ORD["Ordinary / clarity / conflict / community"] -->|"higher weight"| WEIGHT
    OPTIONAL["Polarity / altered states"] -->|"lower weight"| WEIGHT
```

## Article-to-product corrections encoded

- A successful card session can create real closeness without proving ordinary compatibility.
- Mutual triggering and unilateral coercion are not the same problem.
- Modern courtship often lacks a contained intermediate stage before sex and entanglement; the game explores the missing form without presenting historical bundling as a proven solution.
- Labels do not manufacture commitment, but naming an arrangement can expose incompatible assumptions.
- Consent cannot be negotiated on MDMA as though sober; altered-state intimacy still requires later sober evidence.

## Non-negotiable invariants

- Two private classifications and two private revisit records remain separate.
- A safety stop remains anonymous.
- Reality steps are overt, category-specific, and never secret tests.
- A scheduled reality plan becomes complete only after both people submit a revisit.
- No compatibility score may be added without an explicit product-authority change.
- Spoken answers and card prose remain outside serialized session data.
- Ordinary life, clarity, conflict, community, trust, promises, children, and life design carry more selection weight than optional polarity or altered-state material.
- Article-specific claims, autobiography, evidence, and rhetoric remain in the article rather than being silently generalized by the game.
