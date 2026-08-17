# Love, Honestly Card Game — Current State

Updated: 2026-08-17

## Repository status

This is a durable private architecture and recovery snapshot on branch:

`artifact/love-honestly-card-game-v0.2.1`

It is deliberately not merged into `joel-articles/main`, whose job is article governance. The connected GitHub interface used for this release did not expose repository creation, so a dedicated game repository remains pending. The complete project history is preserved in the release Git bundle.

## Exact release boundary

- Product version: `0.2.1`
- Release commit: `7f56a441b1ccb61520711c67dbb2ae6d46098ceb`
- Release tag: `v0.2.1`
- Annotated tag object: `dc7219576cc44ee203e7c90585ad70ce83fe7a83`
- Previous release tag: `v0.2.0`
- Previous release commit: `e9e0b48f5b4f9f20a1cbf70389bbfe89b1acca39`
- Article Edition tag: `v0.1.0`
- Article Edition commit: `884c2b241428e25180ae76e9ed9b10671992fcfd`
- Article reader-visible source SHA-256 used for the redesign: `fd47cad5825ab8f3bafd810c4c0b7e0a817edff40bd802edf66dac7247b6412e`
- Canonical operational map in this snapshot: `ARCHITECTURE.md`
- Release manifest in this snapshot: `RELEASE-MANIFEST.md`

## Product invariant

A deep answer is testimony, not proof. The application preserves:

**Talk → identify evidence basis → preserve two private judgments → test openly in ordinary life → revisit privately → compare without scoring.**

Do not revert to the v0.1 architecture in which a pair negotiated one shared outcome and the game ended after conversation.

## Source-credit invariant added in v0.2.1

The welcome screen visibly says exactly:

**Based on the U-Dont-Exist Romance Guide**

The complete phrase links to:

`https://romance.u-dont-exist.com`

The standalone verifier permits that exact navigational link while continuing to reject any other external runtime URL or dependency.

## Completed in v0.2.0

- Private two-person safety gate with anonymized stop.
- Private evidence-basis selection before either person hears the other's answer.
- Shared answer and corrected-mirroring phase.
- Two private classifications preserved independently.
- Anonymous `Not safe to resolve here` topic stop with no reality experiment.
- Weighted selection favoring ordinary life, clarity, conflict, and community over optional polarity and altered-state topics.
- Seventy-two substantive cards and eight rhythm cards.
- Twenty-eight overt reality experiments covering every substantive category.
- Scheduled revisits at two days, one week, or one month.
- Two private revisit records; a plan completes only after both people answer.
- Evidence map with no compatibility score.
- Minimal v2 serialization and conservative v1 migration.
- Complete normal, safety-stop, not-safe, storage-boundary, revisit, and demo browser paths.

## Completed in v0.2.1

- Added the exact visible source credit to the first screen.
- Linked the complete source-credit phrase to `https://romance.u-dont-exist.com`.
- Added focused regression coverage for the source text, URL, and standalone allowlist.
- Preserved the no-network runtime boundary except for user-initiated navigation through the visible guide link.
- Added a dedicated welcome-screen screenshot and retained the comparison-screen preview.

## Storage boundary

Allowed in local storage:

- setup metadata and local player names;
- card IDs;
- evidence labels;
- classification labels;
- reality-step text, date, and status;
- per-person revisit labels.

Disallowed:

- card prompt, follow-up, or rationale prose;
- spoken answers;
- free-text responses;
- network analytics or account data.

## Fresh release verification

The exact v0.2.1 release tree passed:

```text
npm run verify:release
24/24 Node tests passed
standalone build: 155,123 bytes
standalone source-credit text and URL: passed
normal browser flow: passed
private safety-stop flow: passed
anonymous not-safe flow: passed
storage-boundary flow: passed
two-person revisit flow: passed
demo/preview flow: passed
welcome-screen Chromium DOM verification: passed
git diff --check: passed
ZIP integrity: passed
Git bundle integrity and clone verification: passed
```

The browser verification harness uses a deterministic in-page local-storage shim because its environment blocks navigation to file and loopback URLs. The shipped standalone app uses native browser local storage.

## Recovery order

A fresh worker should:

1. recover the full source from `Love-Honestly-Card-Game-v0.2.1.bundle`;
2. verify its SHA-256 against `Love-Honestly-v0.2.1-SHA256.txt` and `RELEASE-MANIFEST.md`;
3. clone the bundle and confirm `main` and `v0.2.1^{}` resolve to release commit `7f56a441b1ccb61520711c67dbb2ae6d46098ceb`;
4. confirm `v0.1.0`, `v0.2.0`, and `v0.2.1` exist;
5. read the project `README.md`, `CURRENT-STATE.md`, `docs/GAME-FLOW.md`, and `docs/ARTICLE-MAPPING.md` contained in the bundle;
6. create an isolated branch before changing behavior;
7. update the operational Mermaid map in the same change as any consequential welcome attribution, phase, safety exit, serialized record, or setup-to-revisit dependency.

## Next safe action

Create a dedicated private repository for the game, push the complete Git bundle history, preserve all three tags, and make `v0.2.1` the default release boundary. Do not reconstruct the codebase from this architecture summary when the complete bundle is available.
