# Love, Honestly Card Game — Current State

Updated: 2026-08-27

## Repository status

This is the durable private architecture and recovery snapshot on branch:

`artifact/love-honestly-card-game-v0.4.0`

It is deliberately not merged into `joel-articles/main`, whose job is article governance. The complete project source and history are carried by the verified v0.4.0 Git bundle; this branch stores architecture, source reconciliation, release identity, checksums, and recovery instructions.

## Exact release boundary

- Product version: `0.4.0`
- Annotated release tag: `v0.4.0`
- Release commit: `ffb7c1ef7dca4585944d1acf78802ce4107658d6`
- Annotated tag object: `7a7b616c973b0f9908bf37b727b3339ec80df565`
- Final documentation/recovery bundle head: `1e5b0ef63177a9d411ce677990a2c2ee1494c111`
- Immediate predecessor: `v0.3.2` at `b76d18642df026c63fb75ccaa9d221d6b25cf165`
- Updated Romance Guide SHA-256: `e51bae5277c2e0f86b75ff11a304a7d99a56e39d36203eeff7d6f9cc5c8391c7`
- Canonical operational map: `ARCHITECTURE.md`
- Current guide-delta ledger: `CARD-FUNCTION-MATRIX-v0.4.0.md`
- Historical expansion ledger: `CARD-FUNCTION-MATRIX-v0.3.0.md`
- Release manifest: `RELEASE-MANIFEST.md`
- Fresh-conversation recovery packet: `FRESH-CONVERSATION-HANDOFF.md`

## Product invariant

A deep answer is testimony, not proof. Preserve:

**Private answer formation → evidence-basis label → spoken primary and follow-up answers with corrected mirroring → two private judgments → overt ordinary-life experiment → scheduled reminder target → review whenever the pair chooses → delayed private revisit → comparison without scoring.**

Scheduled dates remain reminder targets, never locks.

## Completed in v0.4.0

- Audited the complete 2026-08-27 Romance Guide against the current deck before changing cards.
- Added only two genuinely new substantive cards: `spiritual-bypass-intimacy` and `spiritual-relationship-spirit`.
- Extended `sex-01`, `sex-barometer`, `ordinary-05`, `clarity-06`, and `polarity-01` rather than duplicating their functions.
- Revised `altered-03` to match the guide's narrower warning about first-time sexual-consent decisions while high.
- Updated `promises-01` provenance to `Which marriage vows are honest?`.
- Added Sobonfu Somé as structured provenance for the spirit-of-relationship card.
- Preserved all preexisting card IDs and local-storage schema v2.
- Explicitly omitted incomplete or non-decision source material rather than inventing card doctrine from it.
- Deck total is now 81 substantive cards plus 8 rhythm cards across 15 substantive categories.

## Preserved boundary

- Pending reviews show their target date and remain reviewable before, on, or after it.
- Actual answers are spoken aloud and never stored.
- Evidence labels remain metadata, not answers.
- Two private classifications and two private revisit records remain separate.
- No compatibility score or secret tests.
- Anonymous safety exits remain intact.
- Exact Romance Guide credit remains unchanged.
- No automatic external request is introduced.
- Spiritual Practice remains sensitive, low-weight, opt-in, and disabled by default.

## Verification

```text
npm run verify:release
40/40 Node tests passed
standalone build: 185,817 bytes
normal browser flow: passed
legacy-resume flow: passed
private safety-stop flow: passed
anonymous not-safe flow: passed
storage-boundary flow: passed
two-person revisit flow: passed
source-provenance flow: passed
optional-topic defaults: passed
scheduled future review and early Review now path: passed
no automatic external requests: passed
source ZIP integrity: passed
Git bundle integrity and clone verification: passed
v0.1.0 through v0.4.0 tag recovery: passed
```

## Recovery order

1. Recover full source from `Love-Honestly-Card-Game-v0.4.0.bundle`.
2. Verify it and the other artifacts against `Love-Honestly-v0.4.0-SHA256.txt`.
3. Clone the bundle and confirm `main` resolves to `1e5b0ef63177a9d411ce677990a2c2ee1494c111` and `v0.4.0^{}` resolves to `ffb7c1ef7dca4585944d1acf78802ce4107658d6`.
4. Read `PRODUCT.md`, `DESIGN.md`, `surfaces/game.md`, `CURRENT-STATE.md`, and `README.md` inside the bundle.
5. Read `docs/GAME-FLOW.md`, both card-function matrices, `docs/ARTICLE-MAPPING.md`, the release notes, manifest, and fresh handoff.
6. Create an isolated branch before changing behavior.
7. Update the Mermaid architecture and disposition ledger in the same change as any consequential phase, safety exit, serialized record, category default, source boundary, or setup-to-revisit change.

## Next safe action

A future dedicated game repository should import the verified Git bundle and preserve all release tags. Do not reconstruct source bytes from this architecture summary when the complete bundle is available.
