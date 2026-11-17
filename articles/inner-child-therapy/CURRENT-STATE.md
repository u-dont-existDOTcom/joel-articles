# Inner Child Therapy current state

Updated: 2026-11-17 (turn 131). The checkpoint below is current; the sections after "History" are the 2026-09-21 state, kept as a record.

## Current checkpoint (2026-11-17, turn 131)

- **Work:** humanizing the guide section by section into `HUMANIZED-ARTICLE-SO-FAR.md`, through the gate in `docs/HUMANIZATION-GATE.md` (every paragraph, h3, h2 and h1 reads Human in Pangram's web app; meaning kept; nothing about Joel's life he didn't say, E159; and, his goal since 2026-10-24, reading as engagingly as a good public self-help book: "my goal is i want something that reads engagingly like i assume Lucia's book does").
- **Source:** his own reorganized guide, `experiments/t116-joel/JOEL-GUIDE-20261103.md` (his ODT of 2026-11-03 21:00 UTC as Markdown), with his answers of 23:32 UTC put in (turn 117); the published post is still `master.html`. Until turn 116 the source was `source/inner-child-guide-2026-10-04-r4.txt` with the queue in `GUIDE-UPDATE-QUEUE-20261006.md`.
- **Done through:** published: his live post is the whole guide as round 11 read it since 2026-11-04 18:25 UTC (turn 128; `experiments/t128-publish/UPDATED.json`: the text read back from the live post is round 11's word for word, with the post's own pictures, videos, audio and cards, his six new pictures, two new YouTube embeds, five pull quotes and a divider before each big section). Before that: the whole guide, as his reorganized version (turn 117), read whole for flow and pointers in turn 116 (`experiments/t116-joel/`, `experiments/t116-review/`); its last whole-guide Pangram read is round 11 (pasted in turn 126, read in turn 127), his guide as it will be published, with his sense-read answers of turn 125 and his two hyphens for its nine dashes: both halves Human Written, 0% AI, all 21 windows Human, 18 at High and the same 3 at Medium as round 10, each 1 to 5 of his own words where Pangram's sentence cut fell ("How do you check that?", "Debs.", "Just because Mr."; `experiments/t127-results/`; round 10, turn 124: `experiments/t124-results/`). Round 9 (turn 120) had one AI window at Low. The section-by-section record before it is in Git history (turn 114's `HUMANIZED-ARTICLE-SO-FAR.md`, commit b3a1f54c).
- **In progress:** Turn 131 (his message of 2026-11-17 18:07 UTC in the turn-130 chat, now set to Fable 5.2: "Check now with fable"): Fable's check of turn 130's contents work (`experiments/t131-toc-check/CHECK.md`). Opus's pick, read as a whole for the first time, holds: fresh readers picked the right section first on 53 to 55 of 68 situations (turn 130's 38 and 30 new ones written by an agent that saw only the guide's text), against 44 to 48 on his sidebar as it is, 52 to 54 on GPT's and 53 to 58 on three versions of Fable's. Fable's pick (`PROPOSAL-FABLE-FINAL.json`) is Opus's with 39 headings changed (12 only back to his lower case, most to keep more of his words, five answering what readers did) and one small heading to add (Ugly Thoughts Happen, under Healthy Mind, Not Perfect); his order stays, and one level changes as in Opus's pick. The options page https://claude.ai/artifact/RjHcYbik7oU9VdHcru1tB6 now starts on Fable's pick and keeps anything he had picked; it is question 111 on `OWNER-QUESTIONS.md`. Lessons inner-child-2026-11-17a to g are in `docs/lessons/2026-11-17-1807-inner-child.md`. His live post changed on 17 November 16:55 UTC in two paragraphs, its headings the same. Turn 129 (the article chat, 15 November) is pull request 438.
- **Next step (updated on every push, so another account can pick up here):** 1. His answer to question 111 (the page's store from the account that published it, or the JSON its Copy my answers button gives; `PROPOSAL-FABLE-FINAL.json` for any heading he leaves): build the headings from it, add the one new heading if he keeps it, change the words in the text that name a renamed heading (the page's list; four already point to the wrong place in the live post), and put them in his post as one checked editor transaction, with his OK, then read the live post back. The repository's article is behind his live post (`experiments/t130-toc/LIVE-VS-ARTICLE.json`, and two more paragraphs changed on 17 November): bring his live text into `HUMANIZED-ARTICLE-SO-FAR.md` first. 2. Then turn 128's next steps (his sketches; the Hearthwork article).
- **Waiting on Joel:** His answer to question 111 (the options page); pull request 438 (turn 129); his marks on the sketch page and his sketches; the two temporary drafts (deleting them is his).
- **His edits and rulings:** `OWNER-EDITS.json`, checked against the article on every render (`tools/humanization/check_owner_edits.py`).
- **Records:** `experiments/WHEN-THE-ADULT-VOICE-FEELS-FAKE-20261002.md` (turn log, newest at the bottom), `experiments/t42-rework/`, `tools/PREDICTIONS.md`, `tools/pangram-runs/`, `PARKED-READER-QUESTIONS.md`, `OPEN-OWNER-FLAGS.md`.
- **Lane:** branch `handoff/claude-dangerous-adult-20260924-1631`; pushes go through the laptop clone (`~/ai-work/claude-dangerous-lane/joel-articles`), pull requests to `main`, merged by Joel. Handoff note: `~/claude-acceptance-transfer/handoffs/inner-child-article.md` on his laptop.

## History (2026-09-21)

## Goal

Humanize Inner Child Therapy from the exact registered raw Substack source while preserving accepted/owner-final humanization work and incorporating later owner source edits without confusing the raw-source lineage with the unsynced humanization lineage.

## Authority / baseline

- Article id: `inner-child-therapy`
- Article status: **working**
- Raw-source master: `articles/inner-child-therapy/master.html`
- Raw-source master bytes: **150,330**
- Raw-source SHA-256: `372a43cb69b3f736ae2df4bcce1a627aa5a0318ec4ecf55ee7a2b4edafbf13bd`
- Active humanization assembly: `articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md`
- Whole-article owner-final status: **not claimed**
- Publication status: **not published by this repository action**

The raw master and humanization assembly are intentionally different lineages. The humanized prose has not yet been synced back to Substack. Therefore a raw-vs-humanized whole-document diff is not evidence that Joel changed or overwrote the humanized prose.

## Completed

- Registered and independently hash-verified the exact 2026-09-20 raw Substack editor body.
- Preserved the active humanization assembly and historical experiment/detector evidence separately from raw-source authority.
- Joel directly clarified on 2026-09-21 that the latest Substack revision contained **five targeted edits**, not a broad rewrite of the humanized frontier.
- Corrected the prior wrong-baseline diagnosis: the earlier `1/39 exact survivor` result measured cross-lineage difference, not source-update magnitude.
- Classified the five actual source edits against the current humanization frontier.
- Confirmed that only two current-frontier obligations are new: a protective-intent qualification in `The Chicken-and-Egg Problem`, and a new dangerous-present-adult H2 after `Before You Try to Go Deep`.
- Confirmed that the owner-final `Write It. Don't Send It Yet.` P1 remains current humanization authority and is unaffected by the five edits.
- Confirmed that the active checking-section humanization work is unaffected by the five edits.
- Preserved the three later edits as future humanization obligations: identity-development gate, vow gate, and harmful spiritual-authority exclusion.

## Current checkpoint

The current humanization branch remains valid.

### Existing humanized location requiring a local addition

After:

> So I stopped asking the child to heal itself. I started being the grown-up instead—the Nurturer, Protector, and Leader or Guide.

incorporate the new source function that the present-day adult must at least be willing to protect vulnerability rather than exploit it.

Do not replace the accepted paragraph merely because raw Substack uses a different realization.

### New section requiring humanization

Keep the accepted `Before You Try to Go Deep` readiness paragraph.

Immediately after it, before `You Don’t Need an Inner Monologue`, add and humanize:

`When the Present-Day Adult Is Dangerous to the Child`

with the protected functions recorded in `OWNER-LOCKS.json` and `SOURCE-UPDATE-HUMANIZATION-RECONCILIATION-20260920.md`.

### Unaffected active work

The five targeted source edits do not modify the current humanization authority for:
- `You Don’t Need an Inner Monologue`;
- `Catch the Hook Before the Story Takes Over`;
- `Also Look Outward`;
- `Write It. Don't Send It Yet.`;
- the current checking-section lane.

### Checking lane — resolved and owner-accepted

Joel accepted the exact delivery-ready P3 on 2026-09-21.

Accepted P3:

> If you're feeling guilty because you didn't put your seat belt on, just put it on. If you still want to investigate it later, fine. Perhaps now and then you feel bad about that time you refused to put it on, broke your collar bone in a crash, and then got blamed for not wearing it. That's natural, but doesn't mean there's something new to look at. Then the background checker goes, “But are you really listening?” There it is. Seat belt's on. Where were we?

Exact P3 SHA-256:
8efe36e24e6ccfef0cd78393aff12a55942b7da313fa05b771935e027543584b

The complete five-paragraph checking section is now installed in HUMANIZED-ARTICLE-SO-FAR.md.

Quality/detector status:
- independent reader PASS;
- preservation forward/reverse PASS with zero unexplained substantive deltas;
- P3 Pangram Human 1.0 / AI 0.0;
- P1+P2+P3 Pangram Human 1.0 / AI 0.0;
- complete section Pangram Human 1.0 / AI 0.0.

Promotion receipt:
articles/inner-child-therapy/experiments/CHECKING-P3-OWNER-ACCEPTANCE-PROMOTION-20260921.json

Process lesson:
the successful production path was owner cognition -> owner-derived substrate -> post-generation tell ledger -> executed tell repairs -> preservation -> Pangram. This does not establish fresh autonomous Railway transfer.


## Remaining

- Humanize/incorporate the protective-intent qualification at the central reparenting premise.
- Humanize the new dangerous-present-adult H2 as a bounded section in full surrounding context.
- Keep Write-It on its current accepted state. The checking section is resolved and owner-accepted; do not reopen it absent new owner/source evidence.
- When later sections are reached, preserve the identity-development harm gate, vow harm gate, and harmful spiritual-authority exclusion.
- Run normal comprehension/preservation/architecture/humanization/Pangram gates only on boundaries actually changed by the humanization work.
- Citation/health claim review remains pending unless separately requested or materially required.

## Blockers / unresolved

- New dangerous-present-adult safety section is source-valid but not yet humanized.
- The central protective-intent qualification is not yet incorporated into the accepted humanized opening.
- Write-It remains open only on its preexisting unresolved continuation. The checking section has no remaining content blocker.
- No publication/export action is authorized by registration.

## Evidence / artifacts

- Current continuation handoff: `articles/inner-child-therapy/HUMANIZATION-HANDOFF-20260921.md`

- Raw working master: `articles/inner-child-therapy/master.html`
- Active humanization assembly: `articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md`
- Owner locks / protected functions: `articles/inner-child-therapy/OWNER-LOCKS.json`
- Corrected source-delta / humanization impact analysis: `articles/inner-child-therapy/SOURCE-UPDATE-HUMANIZATION-RECONCILIATION-20260920.md`
- Source/evidence index: `articles/inner-child-therapy/SOURCE-EVIDENCE.json`
- Current raw-source inventory: `articles/inner-child-therapy/SOURCE-STRUCTURE-INVENTORY-20260920.json`
- Citation state: `articles/inner-child-therapy/CITATIONS.json`
- Detector state: `articles/inner-child-therapy/DETECTOR-EVIDENCE.json`
- Editorial state: `articles/inner-child-therapy/EDITORIAL-STATUS.json`
- Unincorporated/future-source obligations: `articles/inner-child-therapy/UNINCORPORATED-IDEAS.md`

## Next safe action

Before continuing in a fresh chat, read `articles/inner-child-therapy/HUMANIZATION-HANDOFF-20260921.md` after the normal repository/article bootstrap. Continue humanization from the active humanization assembly. Preserve the two newly relevant source obligations at their exact locations and do not reopen unaffected accepted prose. The checking section is closed unless new owner/source evidence changes it. Write-It remains on its existing humanization authority.
