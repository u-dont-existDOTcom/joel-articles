# Fresh-conversation handoff: Love, Honestly v0.3.0

Continue from the durable v0.3.0 release rather than reconstructing the game from chat history.

## Authority

- Product: **Love, Honestly**
- Release: `v0.3.0`
- Release commit: `66dba59994e3fe67f7158aac940015057c252aaa`
- Annotated tag object: `31241f3b91b1a316076003da4c5b7fa44de7ee1a`
- Release closeout head: `7e523e568fde8249645255f76fcbc7f54c976e54`
- Immediate predecessor: `v0.2.1` at `7f56a441b1ccb61520711c67dbb2ae6d46098ceb`
- Primary product source: U-Dont-Exist Romance Guide
- Exact visible source line: `Based on the U-Dont-Exist Romance Guide`
- Exact href: `https://romance.u-dont-exist.com`

## Recovery order

1. Recover complete source from `Love-Honestly-Card-Game-v0.3.0.bundle`.
2. Verify every artifact against `Love-Honestly-v0.3.0-SHA256.txt`.
3. Clone the bundle and confirm `v0.3.0^{}` resolves to the release commit above.
4. Read `PRODUCT.md`, `DESIGN.md`, `surfaces/game.md`, `CURRENT-STATE.md`, and `README.md` inside the bundle.
5. Read `docs/GAME-FLOW.md`, `docs/CARD-FUNCTION-MATRIX-v0.3.0.md`, and `docs/ARTICLE-MAPPING.md`.
6. Read the v0.3.0 specification, implementation plan, release notes, and release manifest.
7. Create an isolated branch before changing behavior.

## Governing product loop

**Testimony → evidence basis → two private judgments → overt ordinary-life experiment → delayed private revisit.**

A good conversation is evidence that the pair can have a good conversation. It is not a compatibility verdict.

## v0.3.0 decisions not to rediscover

- Preserve every v0.2.1 card ID and storage schema v2.
- Revise an existing card when a new article concept sharpens the same function; do not add a near-duplicate.
- The v0.3.0 function matrix is the durable extend/add/omit record.
- Card-specific experiments override generic category experiments.
- Spiritual practice is an explicit sensitive opt-in category, not default Love content.
- The source panel is compact and semantic; citations do not appear on every playable card.
- Doug Toft, Kim Anami, Buddhist/lived spiritual-practice material, and relationship research are credited sources, not co-authors.
- Affection and flirtation create no sexual obligation.
- Sexual changes are multicausal and not diagnostic tests.
- Body response is not evidence that someone should stay.
- Money and competence are problematic when they become rank, not merely when a woman succeeds or a man earns less.
- Listen-or-solve never reframes intimidation, false accusation, coercion, or retaliation as a style mismatch.
- Role-play is not role capture.
- Sex is not required for awakening; intensity is not durable integration.

## Verification boundary

Run:

```bash
npm test
npm run build
npm run verify
npm run test:browser
npm run verify:release
git diff --check
```

The released tree passed 34 Node tests and all normal, safety-stop, not-safe, storage, revisit, source-disclosure, optional-topic, screenshot, and no-network browser paths.

## Architecture update rule

Any change to a consequential phase, safety exit, serialized record, category default, source boundary, card-function disposition, or setup-to-revisit dependency must update the relevant Mermaid map and durable ledger in the same commit.
