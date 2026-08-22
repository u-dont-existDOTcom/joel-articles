# Joel Articles Codex Current State

Updated: 2026-08-22

## Current posture

The Project-source recovery, GitHub migration, ChatGPT Project cutover, and article-authority system are active.

GitHub is the durable authority for governance, protocols, tooling, and registered article state. `articles/INDEX.json` registers **Romance** and **Somatic Therapies** as working canonical articles.

GitHub hosted readback on 2026-08-20 confirmed:

- repository visibility: **public**;
- default branch: `main`;
- `main` is **not protected** (`protected: false`; protection disabled).

Joel confirmed a standing public-working rule on 2026-08-22: his assigned work may be stored in public GitHub repositories by default unless he explicitly says private/confidential. This does not authorize external publication or licensing and does not override credentials, third-party privacy, or existing explicit-private repository boundaries. `u-dont-existDOTcom/AskRigor-lessons` remains an explicit private exception.

## Authority / baseline

- Repository: `u-dont-existDOTcom/joel-articles`
- Default branch: `main`
- Repository article registry: `articles/INDEX.json`
- Registered article: `romance`, status `working`
- Romance canonical master: `articles/romance/master.md`
- Romance master SHA-256: `af50b7b93662daf00d484ad83faa0453ff0a2a4fda2867ecfd467166b4c984fe`
- Romance reader-visible SHA-256: `10359ab2119ffbe9a8a7a4a52cd0c3216bb1a6a2c0bffbd7e66fca01287f17ce`
- Romance reader-visible word count: **20,496**
- Registered article: `somatic-therapies`, status `working`
- Somatic Therapies canonical master: `articles/somatic-therapies/master.html`
- Somatic Therapies master SHA-256: `1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202`
- Somatic Therapies normalized reader-visible SHA-256: `e79c3efe640dc87880e90aebaeae4eff0ad9a47cb11234a8a0144bd3eaa38677`
- Somatic Therapies Pangram-submitted reader-visible file SHA-256: `613c3514844097ee4bd31e227a4624bde37cca280e8a3a15b566c92a51b25c1e`
- Somatic Therapies reader-visible word count: **3,412**
- Owner ZIP SHA-256 for the historical 4.11.1 Project-source recovery: `c0b6b0ce4d95b303a00cc44d75fdf54e4433fa72e39e9e866c84b856fde965b1`

Current explicit Joel instructions outrank registered state and must then be reconciled back into the registered article family. Historical branches remain provenance/evidence after canonical import.

## Completed

- Archived the exact 4.11.1 ZIP and all 40 exact source members under `archive/project-source-snapshots/4.11.1/` with manifest, README, and checksums.
- Restored 31 absent baseline sources active and preserved all nine newer active successors byte-for-byte.
- Recovered optional `html_diff.py.txt` active and archived separately.
- Completed repository-local Project-source reference recovery with **0 unresolved references**.
- Merged Project-source recovery PR #11 at `eea01a44608fe39f7a472be2a5c7c7757dd22bad`.
- Completed public-visibility transition after credential/private-key audit.
- Replaced the ChatGPT Project instruction block with the GitHub-canonical minimal loader.
- Joel confirmed the redundant ChatGPT Project Source files are deleted.
- Resolved the Romance source branch `agent/romance-primal-crucible-gui-repair-20260817` at unchanged PR #36 head `8e0d70d0ea51fbcb12e307ed0629ed75ee35ce8c`.
- Verified Romance's deterministic 41-operation assembly and exact current Pangram halves manifest.
- Imported the exact Romance master with no prose edits and registered its complete authority family.
- Registered the exact August 20 Romance Pangram-4 current-half results and two paid GUI calls without claiming a whole-article score.
- Completed a P2S/D4 architecture-first humanization of the owner-supplied Somatic Therapies raw Substack editor HTML.
- Verified the Somatic r01 master after GitHub upload; master SHA-256 is `1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202`.
- Preserved all 16 ordinary links and all eight native/editor objects in the Somatic r01 candidate; native objects remain byte-identical and ordered.
- Registered the complete Somatic Therapies working article family and architecture map.
- Promoted Joel's public-GitHub-by-default owner rule into `SKILL.md` with explicit external-publication, licensing, secret, and third-party privacy boundaries.
- Recovered the exact Somatic r01 Pangram 4 result from the durable fixed-batch cache instead of repeating the paid request.
- Recorded five completed Somatic intro probes and a natural-owner control rather than repeating those paid measurements.

## Current checkpoint

Project-source / Project-UI work: **complete**.

Article authority:

- repository status: **active**;
- Romance status: **working**; citation `pending`; detector `recorded`; editorial `pending`;
- Somatic Therapies status: **working**; citation `pending`; detector `recorded`; editorial `pending`;
- neither article is `owner_final` or `published`;
- no competing registered master is unresolved for either article;
- publication exports: none registered.

Current Romance Pangram boundary:

- total: 20,496 reader-visible words; SHA-256 `10359ab2119ffbe9a8a7a4a52cd0c3216bb1a6a2c0bffbd7e66fca01287f17ce`;
- Part 1: 10,236 words; SHA-256 `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`; Human `0.9205247164`;
- Part 2: 10,260 words; SHA-256 `2df878093bc05fefa98ca30e9a97bdd52e212370f432bf0408e90f1b60c54bb0`; Human `0.8983033895`;
- total paid GUI calls for that registered half measurement: exactly 2, one per half.

These half results are not a measured whole-article score and do not satisfy Romance's standing 100% Human acceptance target.

Current Somatic Therapies detector boundary:

- registered r01 boundary: 3,412 reader-visible words; normalized SHA-256 `e79c3efe640dc87880e90aebaeae4eff0ad9a47cb11234a8a0144bd3eaa38677`; submitted file SHA-256 `613c3514844097ee4bd31e227a4624bde37cca280e8a3a15b566c92a51b25c1e`;
- Pangram 4.0 / `STAGE_SUCCESS`: AI `0.9776151180`, Human `0.0223849081`, AI-assisted `0.0`;
- two High-confidence AI windows: indices `0–1529` and `2006–21309`; the short human segment between them contains the Professor Baby Sheep/head-shaving material;
- five intro repair probes (`r02`, `r03`, `r05`, `r06`, `r07`) each returned AI `1.0`;
- `r07` is invalid for article promotion because its added first-person claims have no recovered owner provenance;
- a 270-word natural-owner research-conversational control from Joel's cancer article returned Human `1.0`, High confidence;
- intro audit accounting: 5/6 new paid calls used; one remains and must not be spent on another ordinary conversational paraphrase.

## Remaining

Future work is article/task-driven:

- Romance editing/humanization starts from `articles/romance/` authority.
- Somatic Therapies remains on registered `r01-candidate`; none of the failed intro probes is article authority.
- Somatic humanization must stop the generic paraphrase loop and reconstruct from actual owner/source material and genuine practical thought movement.
- Preserve the known Human owner material, protected claims, recommendations, evidence distinctions, links, media, and safety warnings.
- Use the final remaining intro-audit call only for a materially different, source-grounded realization after cold editorial review; otherwise conserve it.
- After detector-driven prose changes, re-run article-wide semantic, architecture, fidelity, native-object, and link checks before changing the registered master.
- Citation verification remains pending for both articles until factual/source review is requested or materially required.
- Publication/export work should use registered source-format authority and native-object rules.

Hosted GitHub settings such as branch protection, secret scanning, Actions defaults, Dependabot alerts, and code scanning are optional operational hardening. They are not required for the article system to function.

## Blockers / unresolved

- Romance and Somatic Therapies are `working`, not `owner_final` or `published`.
- Citation review remains pending for both.
- Romance's current exact Pangram halves remain below its standing detector target; no whole-article detector result is claimed.
- Somatic r01 is Pangram `AI Detected` at 97.76% AI fraction, and no tested opening replacement has passed.
- Copyright/license posture remains an owner policy decision. Public repository visibility does not imply a license.
- No external publication action is authorized or implied by registration or by the public-working default.

None of these prevents normal work on either registered working article.

## Evidence / artifacts

- Article registry: `articles/INDEX.json`
- Repository meta-map: `ARTICLE-META-MAP.md`
- Romance current state: `articles/romance/CURRENT-STATE.md`
- Romance master: `articles/romance/master.md`
- Romance architecture: `articles/romance/ARCHITECTURE.md`
- Romance detector evidence: `articles/romance/DETECTOR-EVIDENCE.json`
- Somatic Therapies current state: `articles/somatic-therapies/CURRENT-STATE.md`
- Somatic Therapies master: `articles/somatic-therapies/master.html`
- Somatic Therapies architecture: `articles/somatic-therapies/ARCHITECTURE.md`
- Somatic Therapies source evidence: `articles/somatic-therapies/SOURCE-EVIDENCE.json`
- Somatic Therapies detector evidence: `articles/somatic-therapies/DETECTOR-EVIDENCE.json`
- Somatic Therapies humanization report: `articles/somatic-therapies/HUMANIZATION-REPORT.md`
- Somatic raw detector evidence: `u-dont-existDOTcom/pangram-humanization-lab` branch `automation/pangram-fixed-batch`
- Historical Project retirement archive: `archive/chatgpt-project-retirement-2026-08-17/`

## Next safe action

For the active Somatic Therapies task, keep `r01-candidate` canonical while constructing a source-grounded replacement boundary outside authority. Do not repeat the r01 full call or any completed intro probe. Cold-audit a genuinely different realization, use the one remaining intro slot only if warranted, and promote prose only after fidelity and architecture checks pass.

## Recovery rule

After interruption, read `SKILL.md`, `CANONICAL-REPO-MAP.md`, this state file, `articles/INDEX.json`, then the target article's registered current state/master/locks/evidence required by the task. Treat historical branches and detector probes as provenance unless current registered state explicitly promotes them.
