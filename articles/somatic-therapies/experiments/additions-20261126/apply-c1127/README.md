# The somatic additions, live (2026-11-27, turn of 22:26 UTC)

His answers to the cards pages of 20:12 UTC (22:19 and 22:26 UTC; `../answers/ANSWERS-C1127-*.json`) gave his versions of
the texts whose tries were spent, each read Human High in his own check (`../pangram/HIS-CHECKS-C1127.json`). The texts
that read Human High in every window went into his two posts; A1 waits (below).

## What went in

| Post | What | Where | Its check |
|---|---|---|---|
| The somatic guide (post 201523223) | "Imagery Rescripting" (A2, his version: h2 and two paragraphs) | Layer 4, after EMDR, before "Hypnosis, the ancestral therapy" | Human High (checkpoint of 16:39) |
| The somatic guide | "Pain That Won't Quit?" (A3, his version: h1 and five paragraphs) | after Layer 5, before "Optional High-Intensity State-Shift and Release Practices" | [his section check: every window High but the heading (Medium)](https://www.pangram.com/history/52e2bc03-984c-418c-ad46-26a999df6526), which he isn't worried about |
| The inner child guide (post 189761959) | IC1, the pointer to Imagery Rescripting (approved as it stood) | the end of "Re-do Trauma Memories", after his J. paragraph and its picture, before "Discipline Done Right?" | [Human High](https://www.pangram.com/history/cfb9154d-4b26-4e87-ad84-b4112676c8f0) |
| The inner child guide | IC2, the pointer to the two pain therapies (his version, the link on "my somatic guide" kept) | the end of "Physical Pain?", after his advice not to stop the investigation, before "Compassionate Exit?" | [Human High (his)](https://www.pangram.com/history/81b522f7-4574-4678-87e9-9ea7f544d323) |

How: [make_plans.py](make_plans.py) → [PLAN-SOMATIC.json](PLAN-SOMATIC.json) and [PLAN-INNER.json](PLAN-INNER.json); then
[insert.js](insert.js) in each post's editor, in the desktop app's browser pane: one transaction a post, each new block
parsed with the editor's own schema, put in before its anchor heading (found once, by level and text; for the inner child
pointers the paragraph before the anchor checked too), every new block's text checked against the plan before dispatch;
the internal link to "How I Judge Whether Any of This Is Helping" given no target, as the guide's internal links have.
Then Update with `tools/humanization/substack_update.js`: the somatic guide's dialog had one box, "Schedule time to
publish", unticked; the inner child guide's had two, "Send via email and the Substack app" and "Schedule time to publish",
both unticked. No email went: `email_sent_at` is empty on both posts.

The date, as his rule says: the somatic guide's title "(Nov 21, 2026)" is now "(Nov 27, 2026)"; the inner child guide's
subtitle "Updated: Nov 26, 2026" is now "Updated: Nov 27, 2026". Neither post has a date in its social title (lesson
romance-2026-11-27d): the somatic guide has none, the inner child guide's has no date.

## The live posts after the update

Fetched through his laptop at 22:49 UTC ([LIVE-SOMATIC-POST-20261127.json](LIVE-SOMATIC-POST-20261127.json),
[LIVE-INNER-POST-20261127.json](LIVE-INNER-POST-20261127.json); as Markdown, [LIVE-SOMATIC-20261127.md](LIVE-SOMATIC-20261127.md)
and [LIVE-INNER-20261127.md](LIVE-INNER-20261127.md)):

- The somatic guide (updated on Substack 22:47:32 UTC): both sections in, in order (EMDR, Imagery Rescripting, Hypnosis;
  Layer 5, Pain That Won't Quit?, Optional High-Intensity), the internal link in; 36 sections
  (`articles/somatic-therapies/LIVE-SECTIONS.json`).
- The inner child guide (updated 22:46:28 UTC; its body changed on the API about two minutes later): both pointers in,
  in order, their links to the somatic guide's two new headings in; 154 sections (`articles/inner-child-therapy/LIVE-SECTIONS.json`).
- `tools/humanization/depends.py check` on both live texts: 0 changed (18 points and 34 points).
- `articles/BUILT-ON.json`: the Self-Hypnosis guide is built on both; neither change touches the sections it draws on
  (recorded under each edge's "source_changes"); put to him in the turn's report.

## Not in yet: A1, "Can't Stay With a Feeling?"

His two paragraphs are in; the section check reads [Human Written, 0% AI](https://www.pangram.com/history/089bbeb6-7fe6-4961-b18f-7d54fd474d5b)
with two Medium windows, one over his "The ISTDP therapist catches you each time ..." and one over the end of the AEDP
paragraph and his "All three keep steering you back ..." (each of his paragraphs read High by itself). Whether it goes in
as it reads is his to say (the turn's report asks).
