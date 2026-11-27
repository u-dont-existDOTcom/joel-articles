# Somatic guide: three additions from ChatGPT's suggestions (26 November 2026)

Joel, 2026-11-26 22:44 UTC: "i also want to make an addition to the somatic.u-dont-exist.com article with the recs from gpt below (humanized)". The suggestions were ChatGPT's reply from the research lane ([PR 545](https://github.com/u-dont-existDOTcom/joel-articles/pull/545), [SOMATIC-INTEGRATION-PROPOSAL-20261126.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/research/somatic-edt-eaet-20261126/articles/somatic-therapies/experiments/SOMATIC-INTEGRATION-PROPOSAL-20261126.md)): experiential therapies after Brainspotting, imagery rescripting after EMDR, and a pain branch after Layer 5. His words to that lane: add only what fills a gap, say where it fits and who needs which.

**Where it stands:** on his two cards pages of 27 November, [Somatic Guide: two new sections for you to teach me](https://claude.ai/artifact/PWWhtf4EjbExfr9j4fTwKu) (cards on GitHub: [review-c1127/CARDS-SOMATIC.md](review-c1127/CARDS-SOMATIC.md)) and [Inner Child Guide: two pointers to the somatic guide's new sections](https://claude.ai/artifact/AtSe7jXfLmsQ4cyqcRBwpS) (cards: [review-c1127/CARDS-INNER.md](review-c1127/CARDS-INNER.md)). The first page of 26 November, answered: [Somatic Guide, 26 November: three new sections](https://claude.ai/artifact/8w8DEeT9cS8T964HGSpz4M). Nothing is in the post yet.

| | Section | Words | Pangram on the card's version |
|---|---|---|---|
| A1 | "Can't Stay With a Feeling?" (h2, end of Layer 3, after Brainspotting) | 291 | paragraph 1 [AI 100% High](https://www.pangram.com/history/d24b51d4-8c68-4f97-8939-ce63f875dc7d); 2 [AI 100%](https://www.pangram.com/history/c84530df-1666-4b49-85c4-4aa829b57c9d); 3 [Mixed 55%, the Affect Phobia sentence Human High](https://www.pangram.com/history/b4f0fea6-06e1-4076-a6a6-a0589c7d82e1); 4 is 49 words, under the web app's 50 |
| A2 | "Imagery Rescripting" (h2, Layer 4, after EMDR) | 158 | paragraph 1 [Mixed 77%, the sentence on his Re-do Trauma Memories Human Medium](https://www.pangram.com/history/f61d3830-0297-4178-9a50-dabb63f671e9); 2 [AI 100%](https://www.pangram.com/history/70cf11e3-b851-4db9-8560-701196caba33) |
| A3 | "Pain That Won't Quit?" (h1, after Layer 5) | 315 | [Mostly Human, 3% AI](https://www.pangram.com/history/2ead9bf4-482d-487d-bb34-b40ceb60f1e3), windows Human: Medium, Low, High, Low, Medium, Low, Medium, High |

## What the readings say

- What reads AI is general explaining of a therapy: what it is, what the therapist does, what a trial found. A1 and A2 read AI 100% as whole sections in their fifth drafts ([A1](https://www.pangram.com/history/7f76bad0-ee08-4a1c-b586-8c119afa80ad), [A2](https://www.pangram.com/history/b9255b37-4f32-4681-a0c7-72672ab039c9)) and mostly AI as paragraphs in their seventh.
- The one sentence tied to Joel's own work (A2: "Rescripting is a lot like the way I re-do trauma memories in my inner child reparenting guide") read Human Medium inside an AI paragraph. So the cards ask him for a line of his own experience for A1 and A2 (his preference: ask targeted questions before drafting lived-experience stretches; never invent his experience).
- A3 read Mostly Human in its first check. Seven small clarity fixes the sixth reads asked for, made in one try, turned it to [AI 61%](https://www.pangram.com/history/af6615cb-06d4-4f41-a73f-e4a9340d86fb). The near-miss rule (one or two words a check) was right; the card keeps the Human version and offers the two fixes that matter for meaning ("though real" after "false alarm"; naming the two therapies) one at a time.

## Sources checked

[DRAFT-2.md](DRAFT-2.md), "Sources checked", and on each card. Added since: the anxiety signs ISTDP watches (tense muscles, sighing, foggy thinking) from [Abbass 2021](https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and); "0 or 1 out of 10" as the trial's pain-free-or-nearly line from [Ashar 2022, Figure 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC8482298/figure/yoi210060f2); the trial was in mild or moderate back pain, [NIH Research Matters](https://www.nih.gov/news-events/nih-research-matters/retraining-brain-treat-chronic-pain).

## How it was made

1. The live post fetched (LIVE-BODY-20261126.html, [WHOLE-LIVE-20261126.md](WHOLE-LIVE-20261126.md) by [live_markdown.py](live_markdown.py)).
2. Seven drafts. Fresh readers read drafts 1, 3, 4 and 6 against his fixes ([reads/](reads/READ-HIS-FIXES-6.md)) and for need, fit and contradictions with the guide ([READ-NEEDED-FIT-6.md](reads/READ-NEEDED-FIT-6.md)). Fable's limit ran out at the sixth read (until 1 December), so the last two reads were Sonnet's; Sonnet marks far more than it should (22 of 30 sentences in round 4), so marks that conflicted with each other or with the near-miss rule are kept with a reason in the receipts.
3. Making-sense receipts for every new paragraph and heading ([fill_receipts.py](fill_receipts.py) for A1 and A2, [fill_receipts_v5.py](fill_receipts_v5.py) for A3; [receipts/](receipts/)).
4. Pangram in the web app (his account, desktop app's browser pane); predictions and results in [the somatic ledger](../../humanize/pangram-ledger.jsonl): 6 right, 3 misses (A1 predicted Human and read AI; A3's first try predicted AI and read Human; its second predicted Human and read AI 61%).
5. The page: [build_review.py](build_review.py) → [review/REVIEW.json](review/REVIEW.json), [review/CARDS.md](review/CARDS.md), published as the artifact above.

## Next

1. His answers to the three cards. For A1 and A2, a line of his own if he has one; with it, rebuild each section's opening on it and check again. Without one, the next try ties A1 to what the guide already says (Hâle's worry that the feeling can outrun the therapist) and keeps A2's description to one sentence, saying the rest through his Re-do Trauma Memories section.
2. A3's three Low windows, one small fix a check, and the two clarity fixes he chooses.
3. Once approved and Human High: apply in the editor (the Self-Hypnosis pattern: apply script, `tools/humanization/substack_update.js`), update the title's date, fetch the live post, run `tools/humanization/live_sections.py` and the depends check.

## Checkpoint, 2026-11-27 01:00 UTC (his answers in; saved mid-turn at his word: "save your work so i can continue on other acct")

His answers ([answers/ANSWERS-20261127.json](answers/ANSWERS-20261127.json)):
- **A1 approved.** "why are you suddenly thinking you need a human experience, that's not true ... but certainly if you find stuff in the article already like you said that you could echo that might make sense". It still reads AI, so it is mine to fix before it goes in.
- **A2: his own version** goes in (117 words, [Human Written, Human High](https://www.pangram.com/history/36d19d5d-dd1c-453f-850a-5d41835bf330), checked: its text matches his version). He also asked: "add a mention in the inner child guide that what i'm talking about is an actual clinical therapy called Imagery Rescripting and link to info on it".
- **A3 approved.** He asked: "briefly mention these in the secftion on pain that won't go away in inner child guide and link to this section of the somatic guide for more on them (just like a sentence or so maybe)".
- His rule, now in the repo: Pangram never needs his experience; the tries come first ([lesson somatic-2026-11-27a and b](../../../../docs/lessons/2026-11-27-0055-somatic.md); AGENTS.md; his_fixes_brief.md way 28; romance-2026-11-24a's last step marked superseded).

Where each piece stands:
- [ADDITIONS-9.json](ADDITIONS-9.json): A1 rewritten (draft 9, 235 words: opens on what the reader knows from Layer 3, the way his A2 rewrite opens on his own guide); A2 his version; A3 the approved text with two one-word fixes aimed at its Low windows ("the feelings" for "those feelings"; "A 30% drop is a lower bar" for "That's a lower bar"). Not yet checked in Pangram.
- [INNER-CHILD-ADDS-1.json](INNER-CHILD-ADDS-1.json): the two inner child sentences (IC1 after "Once you've got your cast ... relive them in a better way."; IC2 after "I'd ask for a chronic pain specialist ..."). Their links point to the somatic sections' anchors, which exist only once the somatic edit is live (check the slugs then: imagery-rescripting, pain-that-wont-quit).
- Fresh reads of draft 9 are in, not yet acted on: [READ-HIS-FIXES-9.md](reads/READ-HIS-FIXES-9.md) (12 marks) and [READ-NEEDED-FIT-9.md](reads/READ-NEEDED-FIT-9.md) (17 findings). The ones that matter most: IC1's "at first" and its place (the next paragraph's "For example" would read as an example of the therapy, so it may go after that story or end the section); IC2's "have done well in trials" needs the trials' limits (mild to moderate back pain; veterans 60 and up) and "so far" after "no injury or disease found"; A1-S5's "Most people who go" names no therapy (say it: "Most people who go to it" or "There's a slower version"); A3-S13's "the second" and "the first" (approved as is; a one-word change at most, one per check, since A3 is a near miss). Sonnet over-marks: act on what a reader would hit, keep the rest with a reason in the receipt.
- The lesson's blind test: [replay/BRIEF.md](replay/BRIEF.md) written, not yet run (a fresh writer rewrites my A2 draft 7 from the lesson alone, then each paragraph in Pangram; Fable's limit is out until 1 December, so use Opus told to answer briefly).

Next, in order:
1. Act on the draft-9 reads; receipts (fill_receipts.py pattern, texts with their links); predictions in [the somatic ledger](../../humanize/pangram-ledger.jsonl); Pangram in the web app (his account; desktop app's browser pane, tab "seed"): A1 each paragraph by itself (the last one with the one before it, being under 50 words) and as a section; A3 as a section; IC1 and IC2 each in its paragraph and section. Keep trying up to the budget the way his fixes show; never ask him for experience.
2. Run the replay and write replay/RESULTS.md.
3. Apply in Substack once every window reads High: the somatic guide (A1, A2 his version, A3, in the places in ADDITIONS-9.json), then the inner child guide (IC1, IC2) with the live anchors; guarded Update (tools/humanization/substack_update.js); fetch both live posts; live_sections; depends check; BUILT-ON (the Self-Hypnosis guide is built on the somatic guide: these are therapist-led therapies, so likely nothing to carry, but say so in articles/BUILT-ON.json).

## Checkpoint, 2026-11-27 16:39 UTC (the draft-9 reads acted on through draft 17; four rounds of Pangram; the replay run)

Drafts 10 to 17 ([ADDITIONS-17.json](ADDITIONS-17.json), [INNER-CHILD-ADDS-7.json](INNER-CHILD-ADDS-7.json); each made by a script in [scripts/](scripts/make_draft17.py)) act on the draft-9 reads and on five more rounds of fresh Fable reads ([READ-HIS-FIXES-10](reads/READ-HIS-FIXES-10.md), [READ-NEEDED-FIT-10](reads/READ-NEEDED-FIT-10.md), the same for 11, then [READ-12](reads/READ-12.md), [READ-14](reads/READ-14.md), [READ-16](reads/READ-16.md)), with a tell panel twice on A1's opening ([panel/A1-P1-15](panel/A1-P1-15/PANEL.md), [panel/A1-P1-16](panel/A1-P1-16/PANEL.md)). Receipts: [fill_receipts_v17.py](fill_receipts_v17.py) (receipts/v17/); predictions and results in [the somatic ledger](../../humanize/pangram-ledger.jsonl), batch add1127.

Each paragraph checked by itself (with its neighbour when under 50 words), Pangram web app, his account:

| Piece | Latest check | Where it stands |
|---|---|---|
| A1 P1, the opening | [AI 97%: AI (Low) 11, AI (Medium) 32, AI (Low) 29](https://www.pangram.com/history/4e4d68a4-4cff-491a-aae3-74c536c89085) | try 3 of 6; the panel agreed on every sentence twice |
| A1 P2, how ISTDP stays bearable | [Human (High) 78](https://www.pangram.com/history/63dc89df-a178-4ad6-94ea-0c9865645849) | done |
| A1 P3, Affect Phobia (38 words, word for word the draft-7 near miss) | [Human (High) 39, beside the AEDP paragraph](https://www.pangram.com/history/6ab21c6b-4c4a-4ed4-8a39-09248c3bbe75) | done |
| A1 P4, AEDP | [Human (High) 62 by itself](https://www.pangram.com/history/da780877-d112-467b-93fc-fc02004fbc76) | done by itself; beside either neighbour its sentences read AI (same link as P3; [3ee74597](https://www.pangram.com/history/3ee74597-b3e5-40ff-9164-5f5474ac0ae3)) |
| A1 P5, what to ask before booking | [Human (Low) 69](https://www.pangram.com/history/7de1f32a-42f2-469c-9184-a2e9fa8ddc81) | near miss: a word or two a check |
| A2 (his version) | [Human (High)](https://www.pangram.com/history/36d19d5d-dd1c-453f-850a-5d41835bf330) | done |
| A3 P1, the opening (36 words, with P2) | [opening line Human (Medium) 12; the second sentence High](https://www.pangram.com/history/0615933a-a6eb-4722-8e6b-8222bfea1f27) | the opening line read Medium in three one-word tries ("in the first place", "here", "physical") |
| A3 P2, what you do in PRT | [Human (High) 71](https://www.pangram.com/history/82740d43-acd9-45b0-a942-1cd761d66698) | done |
| A3 P3, PRT's evidence | [Human (High) 55](https://www.pangram.com/history/1f690117-8ab6-47c9-beaf-2e9eaa4ea8c3) | done |
| A3 P4, EAET | [Human (High) 62](https://www.pangram.com/history/625ebf0c-6a40-42f5-8429-a9f8feffdbbc) | done |
| A3 P5, EAET's evidence | [Human (High) 57](https://www.pangram.com/history/76768c4b-1a89-46e8-b37d-befaf314177b) | done |
| A3 P6, how to choose | [Human (High) 72](https://www.pangram.com/history/0320a0bc-3f6d-4eb1-80c2-5d8b7639c6e9) | done |
| IC1, Imagery Rescripting (inner child guide) | [Human (High) 33, Human (Medium) 25](https://www.pangram.com/history/e2f5b150-fe52-40ff-8109-61804c63bd87) | near miss: the Medium window is its second sentence |
| IC2, the pain therapies (inner child guide) | [AI, with his paragraph before it (his paragraph read AI in the same window)](https://www.pangram.com/history/5416d638-45ef-4b18-871f-cfbaba2ced81) | needs a new try with a named cause |

Changes for his eye (they touch meaning; on the marking page when the texts are final):
- A3, the false alarm: "you learn to treat the pain, though real, as a false alarm, your brain signaling danger where the doctors haven't found any. Part of how you learn that is by paying close attention to how the pain feels in your body without fearing it." The approved wording could read as "your pain isn't real", stated the cause as fact against his inner child guide's "a treatment that helps doesn't explain what's causing it", and read as dwelling on the pain (READ-NEEDED-FIT-9, READ-12).
- A1, the booking question: "or if you say I'm dodging a feeling and I don't think I am?" keeps the approved freedom to disagree, tied to what the ISTDP therapist does (READ-16).
- IC1 uses his own aside from his card answer: "which I only found out about after I wrote this section".
- IC2 dropped the trials' summary: the somatic section it links to has them and their limits, and he asked for "just like a sentence or so".

The blind replay of lesson somatic-2026-11-27b: [replay/RESULTS.md](replay/RESULTS.md), 1 of 3 parts; what it missed is [lesson somatic-2026-11-27c](../../../../docs/lessons/2026-11-27-1615-somatic.md).

Next, in order:
1. A1 P5 and IC1's second sentence: a word or two a check, on the window below High.
2. A3's opening line: join it to the sentence after (his way 18), or, if two more tries leave it Medium, the later list with its checks.
3. A1's opening: try 4 of 6 from the second panel's agreed points; if it reads AI, the next draft comes from a writer of another family (tools/humanization/tell_panel.py rewrite-prompt), then a teaching card.
4. IC2: a new try with a named cause; pairing it with his paragraph gave no lift.
5. The sections: A1 (predict with --narrowed, the paragraph lineages), A3 (--after-fix and --narrowed).
6. Cards for the four changes above, on the marking page the turn they are written.
7. Apply in Substack once every window reads High: the somatic guide, then the inner child guide (anchors imagery-rescripting, pain-that-wont-quit); BUILT-ON.

## Checkpoint, turn of 2026-11-27 19:25 UTC (drafts 18 to 24; the cards pages published 20:12 UTC)

Joel, 19:25 UTC: "why did you stop". The turn went on with the checkpoint's Next until each text read Human High or its
tries were spent, and ends on two cards pages for what is spent (lesson bad-trips-2026-11-14b). 19 checks in his Pangram
account from 19:29 to 20:05 UTC (batch add1127, [pangram/RESULTS-add1127-5.json](pangram/RESULTS-add1127-5.json) to
[-10](pangram/RESULTS-add1127-10.json)): 11 predictions right, 8 misses, each explained in the ledger.

| Text | Where it is | Best check |
|---|---|---|
| A1, first paragraph (who the section is for; ISTDP) | spent: six tries, all AI; the sixth, joined into the anxiety paragraph, pulled that one to AI too (lesson somatic-2026-11-27d) | [AI 91%, two Low windows](https://www.pangram.com/history/6e616723-4be9-418f-b508-0ae4f56f3bca) (try 18); his card A1-TEACH |
| A1, the anxiety paragraph | done | [Human High](https://www.pangram.com/history/63dc89df-a178-4ad6-94ea-0c9865645849) |
| A1, Affect Phobia Therapy (under 50 words, with its neighbour) | done | [Human High over it](https://www.pangram.com/history/b4f0fea6-06e1-4076-a6a6-a0589c7d82e1) |
| A1, AEDP | done | [Human High](https://www.pangram.com/history/da780877-d112-467b-93fc-fc02004fbc76) |
| A1, the booking paragraph | spent: six tries | [Human Low](https://www.pangram.com/history/7de1f32a-42f2-469c-9184-a2e9fa8ddc81) (try 17) and [again with the question in quotes](https://www.pangram.com/history/ef39ee2f-d0d5-4cf2-9a26-b2b2726e57de) (try 20); his card A1-TEACH |
| A2 (his version) | done | Human High (checkpoint of 16:39) |
| A3, first paragraph (merged with the PRT paragraph) | seven tries; stopped, the last no better than the one before | [High 88, Medium 18](https://www.pangram.com/history/382a6e6b-372e-4f94-a8ec-a454d44492c0); the join of its last sentence (draft 23, read and passed) waits on the section's near-miss gate (lesson somatic-2026-11-27f); his card A3-TEACH |
| A3, paragraphs 2 to 5 | done | [trial](https://www.pangram.com/history/1f690117-8ab6-47c9-beaf-2e9eaa4ea8c3), [second therapy](https://www.pangram.com/history/625ebf0c-6a40-42f5-8429-a9f8feffdbbc), [its trial](https://www.pangram.com/history/76768c4b-1a89-46e8-b37d-befaf314177b), [how to choose](https://www.pangram.com/history/0320a0bc-3f6d-4eb1-80c2-5d8b7639c6e9), each Human High |
| IC1 (inner child guide, Re-do Trauma Memories) | done | [Human High](https://www.pangram.com/history/cfb9154d-4b26-4e87-ad84-b4112676c8f0); his card IC1, for his eye (his aside in it) |
| IC2 (inner child guide, Physical Pain?) | spent: six tries | [High 38, Medium 20](https://www.pangram.com/history/0f422892-5de8-43b0-8cb2-bfe4b5045d27) (ic2-9); his card IC2-TEACH (lesson somatic-2026-11-27e) |

What this turn made: drafts 18 to 24 ([scripts/make_draft20.py](scripts/make_draft20.py) to
[make_draft24.py](scripts/make_draft24.py); [ADDITIONS-20.json](ADDITIONS-20.json) to [ADDITIONS-23.json](ADDITIONS-23.json),
[INNER-CHILD-ADDS-10.json](INNER-CHILD-ADDS-10.json) to [-14](INNER-CHILD-ADDS-14.json)); fresh reads against his fixes and
for need, fit and contradictions before every check ([reads/READ-20.md](reads/READ-20.md), [READ-20b](reads/READ-20b.md),
[READ-21](reads/READ-21.md), [READ-22](reads/READ-22.md), [READ-23](reads/READ-23.md), [READ-24](reads/READ-24.md)), every
mark acted on; tell panels on A3's opening ([panel/A3-P1-20/PANEL.md](panel/A3-P1-20/PANEL.md)) and IC2
([panel/IC2-23/PANEL.md](panel/IC2-23/PANEL.md)); receipts ([fill_receipts_v20.py](fill_receipts_v20.py) to
[v24](fill_receipts_v24.py)) and predictions ([predict_v20.py](predict_v20.py) to [v24](predict_v24.py)); the inner child
guide as live, fetched through his laptop at 20:11 UTC ([IC-WHOLE-LIVE-20261127.md](IC-WHOLE-LIVE-20261127.md)); the cards
([build_cards_c1127.py](build_cards_c1127.py), [review-c1127/CARDS-SOMATIC.md](review-c1127/CARDS-SOMATIC.md),
[review-c1127/CARDS-INNER.md](review-c1127/CARDS-INNER.md)).

Changes of meaning for his eye, on the cards: A3's false alarm ("your brain is making real pain, signaling danger where the
doctors haven't found any injury"), "there are two therapies I'd look into" for "two therapies are worth knowing about";
A1's booking question in quotes ("What happens if I get overwhelmed, or if you say I'm dodging a feeling and I don't think I
am?"); IC1's aside, his own line.

A stray scheduled task: one of the tell panel's readers (Haiku, on IC2) scheduled a one-minute reminder nobody asked for
(trigger trig_018tSxx2uvui6MSbM584iYBP, placeholder text, due about 20:04 UTC) and couldn't delete it; it is his to delete
from his scheduled tasks, if it still shows.

### Next, in order

1. His answers to the two cards pages: record each fate with a script (Approve, Reject, Revise with his version).
2. A1: his versions of the first and the booking paragraphs, each checked by itself, then A1 as a section (`--narrowed`).
3. A3: his answer to A3-TEACH; then the section check (`--after-fix`, `--narrowed`), after the two small section tries the
   ledger asks for, or with his version.
4. IC2: his version of the second sentence, checked by itself.
5. Once every window reads High: apply in Substack, the somatic guide (A1, A2 his version, A3) then the inner child guide
   (IC1, IC2) with the live anchors imagery-rescripting and pain-that-wont-quit; guarded Update
   (tools/humanization/substack_update.js); the posts' "Updated" dates; fetch both live posts; live_sections; the depends
   check; BUILT-ON.
