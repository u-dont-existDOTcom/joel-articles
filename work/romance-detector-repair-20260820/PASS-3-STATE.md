# Romance detector repair — pass 3 state

Updated: 2026-08-20

Status: **candidate work only**. Canonical `main:articles/romance/master.md` remains unchanged.

## Pass-2 measured result

Exact pass-2 Part-2 boundary:

- SHA-256: `679daa77fb92ea71bb85716e6ece671e093b49412b149e2f5129079a204d24d2`
- Pangram 4.0 / `STAGE_SUCCESS`
- Human: `0.9114283323287964`
- AI: `0.08857167512178421`
- AI-assisted: `0.0`
- API task checkpoint/result is durable on `u-dont-existDOTcom/pangram-humanization-lab:evidence/romance-pass2-api-20260820`
- Part-2 paid submissions in this audit through pass 2: exactly 2 (pass 1 GUI + pass 2 API)
- Part 1 remained exactly restored to registered SHA `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`; no new Part-1 call occurred.

Pass 2 was slightly below pass 1 (`0.9137498736`) by `0.0023215412712036` Human fraction, but the two pass-2 edits were independently editorially justified: restoring owner-shaped `one-dimensionalizing them` and removing an unnecessary interpretive-aftercare sentence. They remain in the candidate unless later owner/editorial review says otherwise; a small detector regression does not override better prose.

## Corrected localization finding

The earlier pass-1 assessment incorrectly associated original Part-2 red windows 17/19/21 with `After leaving`. Re-reading the exact historical detector-boundary source against the raw/Pangram offset transform shows those late red windows are in the **Twin Flames → `Two Pillars Don't Hold The Roof Up` / community transition**.

This correction matters because it explains why pass-2 `After leaving` edits barely moved the full Part-2 score: they were not targeted at those late detector windows.

The historical original Part-2 localization had ten AI-labeled overall windows: 1, 3, 5, 7, 9, 11, 14, 17, 19, 21. Pass 1 edited regions corresponding to five of those clusters and the pass-2 API result reports exactly **5 AI segments**. This is not proof of one-to-one segment identity after resegmentation, but it is strong routing evidence that the likely residual regions are the two untouched Queen-of-Orgasms windows plus the three untouched Two-Pillars/community windows.

## Pass-3 semantic / architecture gate

### Queen of Orgasms

The two likely residual early windows contain independent prose weaknesses:

1. a generic `Many people are not even aware...` setup before the stronger lived sentence `Women have shown me...`;
2. a two-sentence taxonomy (`very differently... Instead...`) that states one thought in two steps;
3. `That laboratory evidence establishes the uniqueness of the phenomenon.`, which explicitly tells the reader what the immediately preceding laboratory result already demonstrated.

Pass 3 removes the generic setup, collapses the taxonomy into one spoken thought, and removes the explanatory aftercare sentence. The lived cervical-sex claim, the `life/work` joke, the Komisaruk/Whipple claim, and the Anami/Richardson claims remain.

### Two Pillars / community

The late cluster has a larger architecture defect. Earlier in the article, `Don’t make your partner your whole world` already establishes that romance can displace self-care/friends and explicitly promises to return to a stronger form of community: people who know both members over time. The current `Two Pillars` opening partly repeats the earlier burden argument before reaching that promised unique function.

Pass 3 therefore:

- makes the Twin-Flame → community bridge personal and direct while preserving the claim that polarity does not make a dyad sufficient;
- removes the duplicated friendship/family/therapy/spiritual-meaning burden list while preserving its unique practical-resilience point about housing, money, children, health, emotional crises, and backup;
- preserves the strong-couple/weak-couple caveat in a shorter asymmetric realization rather than a matched taxonomy;
- makes the unique section job explicit: the problem was not merely having friends on each side but lacking people who actually knew both partners and could reality-check the stories.

The personal Bee/community evidence immediately following remains unchanged.

## Protected-function / fidelity gate

- Part 1: unchanged exact registered hash; no detector call needed.
- Heading order: unchanged.
- Native object markers: unchanged.
- Markdown link destinations: unchanged.
- `community-around-dyad`: preserved and strengthened by routing the section to its unique shared-witness/reality-check job.
- `primal-owner-argument`: preserved; the cervical-sex lived claim and polarity context remain.
- Crucible safety, children obligations, Gandarussa, Hale/Heidi identity, father opening, Bear close: untouched.
- No actor, chronology, severe-claim agency, or source attribution is reassigned.

## Detector plan

If deterministic tests and branch CI pass, materialize pass 3 from the exact Git-durable pass-2 candidate, push it before detector work, and make exactly **one** new Pangram-4 Part-2 API measurement under the same audit/section identity. This will be paid Part-2 submission #3 of the six-call repair cap. No Part-1 call and no isolated probes.
