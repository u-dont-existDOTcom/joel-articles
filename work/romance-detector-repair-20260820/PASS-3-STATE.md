# Romance detector repair — pass 3 state

Updated: 2026-08-20

Status: **candidate work only**. Canonical `main:articles/romance/master.md` remains unchanged.

## Measured progression

Registered Part 2 baseline:

- SHA-256 `2df878093bc05fefa98ca30e9a97bdd52e212370f432bf0408e90f1b60c54bb0`
- Human `0.8983033895`

Pass 1:

- SHA-256 `30f61fb0c490ec1275f3c39c834a38a956041865b63e5592c270d51cc22d5498`
- Human `0.9137498736`
- AI `0.0862501487`
- AI-assisted `0.0`

Pass 2:

- SHA-256 `679daa77fb92ea71bb85716e6ece671e093b49412b149e2f5129079a204d24d2`
- Human `0.9114283323287964`
- AI `0.08857167512178421`
- AI-assisted `0.0`

Pass 3:

- SHA-256 `c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c`
- words `10,043`
- Pangram 4.0 / `STAGE_SUCCESS`
- Human `0.9153165817`
- AI `0.0846834108`
- AI-assisted `0.0`
- exact stored-text match `exact_utf8`
- transport `local_playwright`
- durable evidence branch `u-dont-existDOTcom/pangram-humanization-lab:evidence/romance-pass3-gui-20260820`
- result path `state/gui-runs/pangram-4/c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c/result.json`

Pass 3 is therefore the best measured Part-2 candidate so far: `+0.0015667081` Human fraction over pass 1 and `+0.0170131922` over the registered baseline. The gain over pass 1 is small, so it does not prove that all seven pass-3 local operations helped.

The pass-3 API attempt was rejected with HTTP 402 `Insufficient credits` before Pangram created a task ID. It was non-ambiguous and produced no detector result, so it is recorded as a rejected pre-task attempt rather than a paid measurement. The GUI fallback is paid Part-2 measurement #3 under the same audit/section identity.

Part 1 remains exactly restored to registered SHA `ae88df0f4156537239cb984337196703b88629c3588a5e58ee50c0888d3b39f8`; no further Part-1 call occurred.

## Corrected localization finding

The earlier pass-1 assessment incorrectly associated original Part-2 red windows 17/19/21 with `After leaving`. Re-reading the exact historical detector-boundary source against the raw/Pangram offset transform shows those late red windows are in the **Twin Flames → `Two Pillars Don't Hold The Roof Up` / community transition**.

This correction explains why pass-2 `After leaving` edits barely moved the full Part-2 score: they were not targeted at those late detector windows.

The historical original Part-2 localization had ten AI-labeled overall windows: 1, 3, 5, 7, 9, 11, 14, 17, 19, 21. Pass 1 edited several of those regions, and pass 2 reported five AI segments, but neither that count nor the old window positions can establish the exact surviving pass-3 windows after resegmentation.

## Pass-3 semantic / architecture gate

### Queen of Orgasms

Pass 3 removed a generic setup before the lived cervical-sex claim, collapsed a two-sentence taxonomy into one spoken thought, and removed an explanatory sentence that merely stated what the immediately preceding laboratory result established. The lived cervical-sex claim, the `life/work` joke, the Komisaruk/Whipple claim, and the Anami/Richardson claims remain.

### Two Pillars / community

Earlier in the article, `Don’t make your partner your whole world` already establishes that romance can displace self-care/friends and explicitly promises to return to a stronger form of community: people who know both members over time. The old `Two Pillars` opening partly repeated the earlier burden argument before reaching that promised unique function.

Pass 3 therefore:

- makes the Twin-Flame → community bridge personal and direct while preserving the claim that polarity does not make a dyad sufficient;
- removes the duplicated friendship/family/therapy/spiritual-meaning burden list while preserving its unique practical-resilience point about housing, money, children, health, emotional crises, and backup;
- preserves the strong-couple/weak-couple caveat in a shorter asymmetric realization;
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

## Next detector step — read-only, no paid call

Do **not** draft pass 4 yet.

The pass-3 result receipt contains only the aggregate score; it does not persist window spans. Before another detector-driven prose change, use `pangram-local localize` read-only against the exact already-paid pass-3 History report and exact SHA `c6ef42419a3db2e82b1ff4f9370fc85bca4fa8c061c61dd6a1b5d28171d9908c`.

This localization must make no detector submission. Its purpose is to recover the current pass-3 AI windows after resegmentation so the next edit is targeted at actual residual failures rather than inferred old windows.

Paid Part-2 measurements used: **3 of 6**. Exact History localization/recovery is read-only and does not count against the cap.
