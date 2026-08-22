# Somatic Therapies — Current State

Updated: 2026-08-22

## Goal

Humanize the owner-supplied Somatic Therapies Substack article while preserving its arguments, recommendations, links, native media, personal material, safety warnings, and evidence distinctions; then localize and repair remaining Pangram AI signal without sacrificing fidelity.

## Authority / Baseline

- Article id: `somatic-therapies`
- Status: `working`
- Registered working master: `articles/somatic-therapies/master.html`
- Revision: `r01-candidate`
- Master SHA-256: `1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202`
- Owner source baseline SHA-256: `0d7e03ccde3900277e7ee8e9a1f5aac3c4f780d5243396f9bb2a100ee57083f9`
- Reader-visible normalized SHA-256: `e79c3efe640dc87880e90aebaeae4eff0ad9a47cb11234a8a0144bd3eaa38677`
- Pangram-submitted reader-visible file SHA-256: `613c3514844097ee4bd31e227a4624bde37cca280e8a3a15b566c92a51b25c1e`
- Reader-visible word count: **3,412**
- Joel explicitly authorized public repository registration and public-by-default assigned work on 2026-08-22. This is working authority, not external publication approval.

## Completed

- P2S / D4 architecture-first reconstruction of the mostly AI-shaped source into r01.
- Three cold audits: AI-shape, unsupported-persona/fake-humanization, and fidelity/native-object integrity.
- 16/16 ordinary article links preserved as the same URL multiset.
- 8/8 native/editor objects preserved byte-for-byte in the same order.
- Complete required article authority family registered with exact hashes.
- Owner default-public rule promoted to repository operating guidance.
- Exact r01 Pangram 4 measurement recovered from durable cache: AI `0.9776151180`, Human `0.0223849081`, AI-assisted `0.0`.
- Pangram localized two High-confidence AI windows: indices `0–1529` and `2006–21309`, with only a short human segment between them around the Professor Baby Sheep/head-shaving material.
- Five intro repair probes (`r02`, `r03`, `r05`, `r06`, `r07`) were recovered; every one returned `1.0` AI.
- `r07` was provenance-audited and rejected for article use because its added first-person claims could not be traced to an owner source.
- A 270-word natural-owner research-conversational control from Joel's cancer article returned Pangram 4 Human `1.0`, High confidence. This falsifies the idea that the Somatic failure is simply the detector rejecting Joel's research-guide genre.

## Current checkpoint

`r01-candidate` remains the canonical working master because none of the detector probes is authorized article prose. The broad rewrite improved coherence but failed the detector goal: Pangram sees nearly the entire reader-visible article as AI-shaped.

The failed intro sequence shows that ordinary conversational paraphrasing, adding first person, reorganizing the framework, and approximating owner wording are insufficient. Do not continue that loop.

## Remaining

- Reconstruct from actual owner/source material and genuine practical thought movement rather than another generic paraphrase.
- Preserve the known Human owner material and all protected claims, links, media, recommendations, evidence distinctions, and safety warnings.
- Use the final remaining intro-audit call only for a materially different, source-grounded realization after editorial reconstruction; otherwise conserve it.
- After an accepted detector-driven prose change, re-run the article-wide architecture/fidelity gate before promoting a new master.
- Continue detector work section-by-section or at natural larger boundaries, never by random token edits.
- Claim-by-claim citation/health verification remains pending because it was not requested in this humanization pass.
- Owner-final review/publication export remains pending.

## Blockers / unresolved

- The registered r01 boundary is Pangram `AI Detected`, 97.76% AI fraction.
- No detector-tested replacement has passed for the opening.
- `r01-candidate` is not owner-final or published.
- Citation review remains pending.

## Evidence / artifacts

- `master.html` — registered working master and current raw-editor HTML authority
- `HUMANIZATION-REPORT.md` — reconstruction and preservation audit
- `SOURCE-EVIDENCE.json` — source/candidate provenance and exact baseline hashes
- `OWNER-LOCKS.json` — protected functions
- `ARCHITECTURE.md` — article-wide functional map
- `DETECTOR-EVIDENCE.json` — exact r01 result, failed intro probes, owner control, call accounting, and provenance disposition
- Pangram durable caches under `u-dont-existDOTcom/pangram-humanization-lab` branch `automation/pangram-fixed-batch`

## Next safe action

Do not spend the final intro call on another “more human” paraphrase. Build the next candidate from the owner-authored human material and the article's actual practical decisions, with no invented personal claims. Cold-audit the complete boundary first; only then use the remaining call if it represents a genuinely different realization.
