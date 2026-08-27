# Love, Honestly Card Game — Current State

Updated: 2026-08-27

## Repository status

This is the durable private architecture and recovery snapshot on branch:

`artifact/love-honestly-card-game-v0.5.0`

It is deliberately not merged into `joel-articles/main`, whose job is article governance. The complete project source and history are carried by the verified v0.5.0 Git bundle; this branch stores architecture, source reconciliation, release identity, checksums, and recovery instructions.

## Exact release boundary

- Product version: `0.5.0`
- Annotated release tag: `v0.5.0`
- Verified application release commit: `400f64f0c8acc815bd9b12a075ab324de76d4cff`
- Annotated tag object: `6807866e938582a7588e05e9bee021d9a1959dc8`
- Final documentation/recovery bundle head: `46f7e616779377d49e2b3d5d8df1786b0ab38d25`
- Immediate predecessor: `v0.4.0` at `ffb7c1ef7dca4585944d1acf78802ce4107658d6`
- Current Romance Guide SHA-256: `e51bae5277c2e0f86b75ff11a304a7d99a56e39d36203eeff7d6f9cc5c8391c7`
- Additional owner source: `Long distance` section supplied in the 2026-08-27 card-review conversation
- Canonical operational map: `ARCHITECTURE.md`
- Current owner-gap ledger: `CARD-FUNCTION-MATRIX-v0.5.0.md`
- Prior guide-delta ledger: `CARD-FUNCTION-MATRIX-v0.4.0.md`
- Release manifest: `RELEASE-MANIFEST.md`
- Fresh-conversation recovery packet: `FRESH-CONVERSATION-HANDOFF.md`

The annotated `v0.5.0` tag is the exact verified application source boundary. The later bundle head contains documentation/recovery closure without changing the tagged application bytes.

## Product invariant

A deep answer is testimony, not proof. Preserve:

**Private answer formation → evidence-basis label → spoken primary and follow-up answers with corrected mirroring → two private judgments → overt ordinary-life experiment → scheduled reminder target → review whenever the pair chooses → delayed private revisit → comparison without scoring.**

Scheduled dates remain reminder targets, never locks.

## Completed in v0.5.0

- Preserved the owner-approved v0.4.0 cards except where the owner identified a specific missing function.
- Added `community-06`: intentional-community/commune living as an explicit shared-life question.
- Added `community-07`: community exploration/visits, prior best fit, and next visit planning.
- Revised `sex-03`: making love versus having sex, preferred modes/depth, and eventual cervical-sex interest.
- Added `life-design-long-distance-01`: desire/tolerance for long distance and maximum comfortable duration/frequency.
- Added `life-design-long-distance-02`: opportunity versus physical togetherness, reunion/relocation condition, and indefinite-distance prevention.
- Added `ordinary-long-distance-evidence`: what distance leaves unknown about ordinary in-person compatibility.
- Added `spiritual-twin-flame-model`: one destined person versus repeatable sacred/archetypal connection versus another meaning or non-belief, plus practical consequences.
- Rechecked the remaining guide sections and added no other cards where existing functions already cover the decision or the source material is evidence/history/memoir rather than a new couple decision.
- Preserved every prior card ID and local-storage schema v2.

## Deck boundary

- 87 substantive cards.
- 8 rhythm cards.
- 15 substantive categories.
- 25 card-specific article/owner-update experiments plus 30 category-level fallback experiments.
- All v0.5.0 additions and revised `sex-03` are available in `discover`, `build`, `repair`, and `full`.
- Spiritual Practice remains sensitive, optional, low-weight, and off by default; the direct Twin Flame card therefore appears only by explicit topic opt-in.

## Preserved boundaries

- Pending reviews show their target date and remain reviewable before, on, or after it.
- Actual answers are spoken aloud and never stored.
- Evidence labels remain metadata, not answers.
- Two private classifications and two private revisit records remain separate.
- No compatibility score or secret tests.
- Anonymous safety exits remain intact.
- Exact Romance Guide credit remains unchanged.
- No automatic external request is introduced.
- The cervical-sex question creates no obligation to attempt any sexual act.
- Long distance is asked as a preference/tolerance question rather than diagnosing every distant couple as intimacy-avoidant.

## Verification

```text
npm run verify:release
46/46 Node tests passed
standalone build: 194,288 bytes
normal browser flow: passed
legacy-resume flow: passed
private safety-stop flow: passed
anonymous not-safe flow: passed
storage-boundary flow: passed
two-person revisit flow: passed
source-provenance flow: passed
optional-topic defaults: passed
scheduled reminder target and early Review now path: passed
no automatic external requests: passed
git diff --check: passed
source ZIP integrity: passed
Git bundle integrity and clone verification: passed
v0.1.0 through v0.5.0 tag recovery: passed
```

## Recovery order

1. Recover full source from `Love-Honestly-Card-Game-v0.5.0.bundle`.
2. Verify it and the other artifacts against `Love-Honestly-v0.5.0-SHA256.txt`.
3. Clone the bundle and confirm `main` resolves to `46f7e616779377d49e2b3d5d8df1786b0ab38d25` and `v0.5.0^{}` resolves to `400f64f0c8acc815bd9b12a075ab324de76d4cff`.
4. Read `PRODUCT.md`, `DESIGN.md`, `surfaces/game.md`, `CURRENT-STATE.md`, and `README.md` inside the bundle.
5. Read `docs/GAME-FLOW.md`, `docs/CARD-FUNCTION-MATRIX-v0.5.0.md`, `docs/ARTICLE-MAPPING.md`, `DECISION-LOG.md`, the release notes, and manifest.
6. Create an isolated branch before changing behavior.
7. Update the Mermaid architecture and disposition ledger in the same change as any consequential phase, safety exit, serialized record, category default, source boundary, or setup-to-revisit change.

## Next safe action

A future dedicated game repository should import the verified Git bundle and preserve all release tags. Do not reconstruct source bytes from this architecture summary when the complete bundle is available.
