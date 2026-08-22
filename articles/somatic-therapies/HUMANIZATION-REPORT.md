# Somatic Therapies — r01 humanization report

## Status

- Revision: `r01-candidate`
- Primary mode: P2S style-only reconstruction
- Edit dose: D4 article-wide reconstruction
- Baseline: owner-supplied raw Substack editor HTML
- Baseline SHA-256: `0d7e03ccde3900277e7ee8e9a1f5aac3c4f780d5243396f9bb2a100ee57083f9`
- Candidate SHA-256: `1e7e94717f40e7a4de77974a896f600a1bf2769d9c1846cbe84275e136ff5202`
- Candidate reader-text normalized SHA-256: `e79c3efe640dc87880e90aebaeae4eff0ad9a47cb11234a8a0144bd3eaa38677`
- Pangram-submitted reader-text file SHA-256: `613c3514844097ee4bd31e227a4624bde37cca280e8a3a15b566c92a51b25c1e`
- GitHub article authority: registered working article
- Owner approval: pending

## What the r01 pass changed

The supplied source's most obvious model shape was its repeated card architecture: `Goal → Best use → Not ideal → warning/caveat`, repeated across modality after modality. r01 reconstructed the article around the five current jobs rather than giving every therapy an identical miniature essay.

It also:
- removed repeated explanatory aftercare and conclusion-after-conclusion sentences;
- varied thought duration instead of giving every modality the same rhetorical space;
- kept practical lists where lists genuinely help navigation;
- moved from generic professional phrasing toward direct first-/second-person guide prose;
- preserved the article's supplied personality rather than adding fabricated quirks: Professor Baby Sheep, the head-shaving/loveyhuasca line, Louka, the heart-chakra loop, and the blunt yoga/shaking warnings remain;
- removed several initially generated metaphors and personalizations during cold audit because they were not source-derived.

## Fidelity and preservation checks

No substantive claim change was intended.

Preserved from the source:
- the five-job map and its explicitly provisional/author-developed status;
- the broad safety/regulation → discharge → processing → integration movement;
- the warning against turning capacity-building into indefinite avoidance;
- the inner-child overlap, Nurturer/Protector framing, borrowed adulthood, and heart-to-solar-plexus loop;
- all modality placements and distinctions for Somatic Experiencing, yoga, EFT, TRE/shaking, Shaking Qigong, Brainspotting, EMDR, cognitive integration, Sky Hypnosis, and Vagal Blitz;
- the 3–6 month Somatic Experiencing orientation range and the 10–45 minute shaking-practice range;
- the distinction between mainstream and qigong mechanism language;
- Louka's reported response to the linked shaking class;
- the Brainspotting vs EMDR distinctions;
- the neck/whiplash warning;
- post-session integration guidance;
- evidence-level distinctions between research, clinical practice, personal experience, community report, energetic explanation, and proposed mechanism;
- all high-intensity practice cautions.

Structural checks:
- Reader-visible word count: source 3,111; candidate 3,412 (+9.7%).
- Ordinary article links: 16/16 preserved as the same URL multiset (13 unique URLs).
- Exact native/editor objects: 8/8 preserved byte-for-byte and in the same order:
  1. top image
  2. Professor Baby Sheep digest-post embed
  3. Share button
  4. Somatic Experiencing YouTube embed
  5. TRE/shaking YouTube embed
  6. Brainspotting YouTube embed
  7. EMDR YouTube embed
  8. Sky Hypnosis digest-post embed
- No native object appears more or less than once.
- The source's playful line `therapy is not just work. It’s also play!` remains because it is supplied source language and part of the Professor Baby Sheep section, not a generated humanization device.

## Cold audits

### Pass 1 — architecture and prose shape

Found the repetitive modality-card skeleton and recursive mini-essay closure. Rebuilt the article around the five current jobs instead of polishing that skeleton.

### Pass 2 — unsupported persona / fake humanization

Removed generated flourishes and first-person claims that were not supplied by the source. Corrections included avoiding invented anecdotes when the source supplied only a duration range and backing out stronger judgments the source did not make.

### Pass 3 — fidelity / object integrity

Rechecked claims, ordinary links, native-object byte identity, object order, safety warnings, ranges, examples, and evidence-plane distinctions.

## Detector results changed the assessment

The r01 prose/architecture pass did **not** achieve the detector objective.

Exact r01 Pangram 4 result:
- AI `0.9776151180267334`
- Human `0.02238490805029869`
- AI-assisted `0.0`
- two High-confidence AI windows: `0–1529` and `2006–21309`
- one short Human segment between them around Professor Baby Sheep/head-shaving material.

A genre-relevant natural-owner control from Joel's cancer writing returned Human `1.0`, High confidence. The r01 failure therefore cannot be dismissed as Pangram merely rejecting health/research-conversational prose.

### Intro audit

Six materially different intro candidates were tested under one fixed six-call audit. Every one returned AI `1.0`. One (`r07`) also failed provenance because it introduced first-person material for which no owner source could be recovered. The lane is closed.

A notable negative result came from `r08`: even surrounding the known Human-gap Professor Baby Sheep/head-shaving material with a different model-built realization produced a 100% AI boundary. A local Human span is therefore not composable evidence and must not be treated as a detector charm.

### Inner-child audit

The natural r01 inner-child section returned AI `1.0`. Four successive architecture/register repairs and one owner-source phrase restoration also returned AI `1.0`. The sixth and final call tested the exact owner-supplied source section itself; it also returned AI `1.0`, High confidence.

That last result changes the production decision. The inner-child source remains claim/meaning authority, but it supplies no Pangram-Human textual baseline. More model paraphrases would be an unjustified detector loop rather than evidence-based editing.

## Revised production strategy

The r01 D4 pass regenerated too much prose. Source-vs-r01 section comparison showed that the supplied Professor Baby Sheep/play section was preserved unchanged and overlaps the article's only Pangram-Human region, whereas some highly regenerated sections diverged sharply.

Therefore the current strategy is:
1. measure natural article sections before rewriting them;
2. restore higher-authority source language before generating new prose;
3. prefer movement, consolidation, and deletion of model aftercare over fresh paraphrase;
4. keep detector-Human owner/source spans intact when they already perform the needed function;
5. if the original source itself is detector-AI and no independent Human source exists, stop the model-only loop rather than inventing pseudo-owner language;
6. never promote a detector probe without separate fidelity, provenance, architecture, link, and native-object checks.

## Current active section

Shaking Qigong has an exact r01 natural-section measurement in progress:
- 249 words
- SHA-256 `0f21beb5d6c95c471a13d8b3ff2d373a4541cca61151043203c702286614a181`
- one paid call reserved in the durable Pangram ledger
- no durable result/cache at this report update.

A second candidate is already frozen but unsubmitted. It is a rollback/consolidation built around the exact Louka paragraph and the original discharge→settle sequence rather than another fresh rewrite. It should be submitted only if the r01 Shaking baseline is AI.

## Tooling incident found during this pass

The private Pangram executor originally used one GitHub Actions concurrency group with `cancel-in-progress: false`. A pending Shaking request was displaced by a newer pending run before it created a call ledger/cache entry. The executor was repaired to use `concurrency.queue: max`, and its README now records lossless pending-request and recovery-before-repeat behavior.

The dropped Shaking workflow was retriggered only after confirming that no paid reservation, task checkpoint, or cache existed for that exact measurement. The retrigger then created exactly one paid reservation.

## Idiolect status

A separate idiolect-retention metric was not used. The current protocol treats it as optional/non-blocking, and no validated, decision-useful genre-matched gate is available here. Semantic fidelity, source provenance, architecture, exact Pangram boundaries, and owner authority remain separate acceptance axes.

## Largest remaining weakness

The article still lacks enough independently human prose in several generic explanatory sections to support detector-guided restoration without fresh author input. Model-only rewriting has already failed repeatedly in the opening and inner-child section. The appropriate next move is section-by-section source restoration where a stronger owner anchor exists, not another article-wide regeneration.

## Next safe action

Recover the exact Shaking Qigong r01 result from its existing paid reservation. If it is AI, test the already-frozen source-rollback candidate once. Do not reopen the exhausted intro or inner-child detector lanes.
