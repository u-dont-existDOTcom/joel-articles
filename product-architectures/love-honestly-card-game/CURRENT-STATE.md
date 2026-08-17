# Love, Honestly Card Game — Current State

Updated: 2026-08-17

## Repository status

This is the durable private architecture and recovery snapshot on branch:

`artifact/love-honestly-card-game-v0.3.0`

It is deliberately not merged into `joel-articles/main`, whose job is article governance. The complete project source and history are carried by the verified v0.3.0 Git bundle; this branch stores the architecture, disposition ledger, release identity, and recovery instructions.

## Exact release boundary

- Product version: `0.3.0`
- Release commit: `66dba59994e3fe67f7158aac940015057c252aaa`
- Annotated release tag: `v0.3.0`
- Annotated tag object: `31241f3b91b1a316076003da4c5b7fa44de7ee1a`
- Release closeout head in the Git bundle: `7e523e568fde8249645255f76fcbc7f54c976e54`
- Immediate predecessor tag: `v0.2.1`
- Immediate predecessor commit: `7f56a441b1ccb61520711c67dbb2ae6d46098ceb`
- Article Edition tag: `v0.1.0`
- Canonical operational map: `ARCHITECTURE.md`
- Card-function disposition ledger: `CARD-FUNCTION-MATRIX-v0.3.0.md`
- Release manifest: `RELEASE-MANIFEST.md`
- Fresh-conversation recovery packet: `FRESH-CONVERSATION-HANDOFF.md`

## Product invariant

A deep answer is testimony, not proof. Preserve:

**Talk → identify evidence basis → preserve two private judgments → test openly in ordinary life → revisit privately → compare without scoring.**

Do not revert to the v0.1 architecture or reduce the result to a compatibility score.

## Completed in v0.3.0

- Built a source-wide function matrix before editing; every supplied concept has an extend, add, replace, or omit disposition.
- Revised `love-03`, `love-04`, `sex-02`, `polarity-01`, and `inner-child-03` instead of adding near-duplicates.
- Added seven distinct cards: `love-aging-beauty`, `sex-affection-simmer`, `sex-barometer`, `sex-developed-compatibility`, `ordinary-listen-or-solve`, `polarity-insecurity-double-bind`, and `love-spiritual-practice`.
- Added twelve unique `articleUpdateFunction` values and twelve card-specific reality experiments.
- Added structured source metadata: `article-owner`, `doug-toft`, `kim-anami`, `buddhist-source`, and `relationship-research`.
- Added a compact first-screen source disclosure without adding another external URL or automatic request.
- Added optional, sensitive, low-weight Spiritual Practice; all optional categories begin disabled.
- Preserved all v0.2.1 card IDs and storage schema v2 so old sessions hydrate against the expanded deck.
- Preserved the v0.1.0 Article Edition byte-for-byte.

## New safety boundaries

- Affection and flirtation create no obligation to touch, continue, have sex, reciprocate, become aroused, or produce an orgasm.
- Sexual change is multicausal and not a diagnostic test.
- A bodily response is not evidence that anyone should stay.
- Listen-versus-solve does not reframe intimidation, false accusation, coercion, or retaliation as a style mismatch.
- Female success and lower male income are not pathologized; the operative defect is money or competence becoming rank, humiliation, domination, or enforced shrinking.
- Role-play remains chosen play; adult responsibility does not transfer.
- Sex is not required for awakening, and intensity is not durable integration.

## Storage and network boundary

Allowed local records remain setup metadata, names, card IDs, evidence labels, classification labels, reality-step text/date/status, and per-person revisit labels.

Spoken answers, card prose, source metadata, and free-text responses are not serialized. There are no accounts, analytics, cloud records, remote scripts, stylesheets, or fonts. The exact Romance Guide link is the sole external URL and is contacted only by deliberate player navigation.

## Fresh release verification

The exact v0.3.0 release tree passed:

```text
npm run verify:release
34/34 Node tests passed
standalone build: 169,987 bytes
normal browser flow: passed
private safety-stop flow: passed
anonymous not-safe flow: passed
storage-boundary flow: passed
two-person revisit flow: passed
source disclosure and exact link: passed
optional-topic defaults: passed
no automatic external requests: passed
welcome and comparison screenshots: passed
git diff --check: passed
ZIP integrity: passed
Git bundle integrity and clone verification: passed
v0.1.0, v0.2.0, v0.2.1, and v0.3.0 tag recovery: passed
```

## Recovery order

1. Recover full source from `Love-Honestly-Card-Game-v0.3.0.bundle`.
2. Verify it and the other artifacts against `Love-Honestly-v0.3.0-SHA256.txt`.
3. Clone the bundle and confirm `v0.3.0^{}` resolves to `66dba59994e3fe67f7158aac940015057c252aaa`.
4. Read the project `PRODUCT.md`, `DESIGN.md`, `surfaces/game.md`, `CURRENT-STATE.md`, and `README.md` in the bundle.
5. Read the operational map, card-function matrix, article mapping, v0.3.0 specification, implementation plan, and release notes.
6. Create an isolated branch before changing behavior.
7. Update the Mermaid architecture and disposition ledger in the same commit as any consequential phase, safety exit, serialized record, category default, source boundary, or setup-to-revisit change.

## Next safe action

A future dedicated game repository should import the verified Git bundle and preserve all four tags. Do not reconstruct source bytes from this architecture summary when the complete bundle is available.
