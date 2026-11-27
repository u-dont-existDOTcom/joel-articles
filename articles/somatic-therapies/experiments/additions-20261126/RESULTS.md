# Somatic guide: three additions from ChatGPT's suggestions (26 November 2026)

Joel, 2026-11-26 22:44 UTC: "i also want to make an addition to the somatic.u-dont-exist.com article with the recs from gpt below (humanized)". The suggestions were ChatGPT's reply from the research lane ([PR 545](https://github.com/u-dont-existDOTcom/joel-articles/pull/545), [SOMATIC-INTEGRATION-PROPOSAL-20261126.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/research/somatic-edt-eaet-20261126/articles/somatic-therapies/experiments/SOMATIC-INTEGRATION-PROPOSAL-20261126.md)): experiential therapies after Brainspotting, imagery rescripting after EMDR, and a pain branch after Layer 5. His words to that lane: add only what fills a gap, say where it fits and who needs which.

**Where it stands:** on his marking page, [Somatic Guide, 26 November: three new sections](https://claude.ai/artifact/8w8DEeT9cS8T964HGSpz4M) (its cards on GitHub: [review/CARDS.md](review/CARDS.md)). Nothing is in the post yet.

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
