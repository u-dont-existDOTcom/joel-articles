# Contents order brief: proposing where a guide's sections go

Give this brief, with the article (each section's id, level, heading and text), to a model asked to propose a long
article's order and levels. Lesson inner-child-2026-11-20a. Joel, 2026-11-20 16:39 UTC: "which model could get closet (or
better) than my order with sufficient universal instructions that could apply to any article? i want to save those
instructions in joel-articles repo so that next time you can do most of the work for me."

**What it can and can't do.** In turn 132, 21 outlines of the inner child guide from five models (Opus, Sonnet, Fable,
Haiku, GPT), with no rules, with these rules and with a four-pass version of them, were scored against his own
reorganization of 4 to 14 November (`articles/inner-child-therapy/experiments/t132-toc-links/RESULTS.md`). None came near
it. Leaving his order alone scored about as well as the best outline, the GPT outlines with these rules made the most of
his moves (9 and 8 of his 20) and also the most he didn't make (16 and 23), and the four-pass version helped no model.
So a model's outline is a proposal that goes to him move by move (`docs/FIXING-AN-ARTICLE.md` section 3, item 8), never a
reorganization, and the moves of his that every model missed are the examples under rule 2.

**His view of the framework comes first (lesson inner-child-2026-11-20l).** Turn 133 tried three more ways: small
questions per section, a frame of what each role is for, and a blind card sort of the shuffled sections
(`articles/inner-child-therapy/experiments/t133-order/`). None came closer: every reader filed shame and forgiveness
under the part they were in, where he put them under the Nurturer. What he sees each role's work as including isn't in
the text. So before a model sorts, ask him for a few lines on what each role and part holds, in his words, and give
those lines to the model with this brief.

## 1. Find the reader's path first

Read the whole piece and write down, in a few words each, the path a reader takes through it: what they need to
understand first, what they need to be safe or ready, what they build or learn, how they practice it, what goes wrong and
how to handle it, special situations, how it carries into the rest of their life, and what closes the piece (summary,
appendix, sources). Not every piece has every stage. Each top-level part should do one job on that path. Keep the
author's parts where they already do this.

## 2. Put each section where its job is

A section belongs to the part whose job it serves, and under the heading whose question it answers. Judge by what the
section does for the reader (teaches a concept, gives a practice, handles a problem, tells a story), not by words it
happens to share with a heading.

- When the piece is built around roles, tools, steps or stages, a section that describes the work one of them does goes
  under that one, even if it was written somewhere else (an emotional-repair skill goes under the role that does
  emotional repair; a spiritual practice under the role that holds the spiritual side).
- Practice instructions go after the concepts they use, in the part about practice.
- A problem goes under the general problem it is a case of, or next to the practice where it comes up. Troubleshooting
  comes after what it troubleshoots.
- A story, example or aside stays with the point it illustrates. A section that only continues the one before it goes
  inside or under that one.
- Material about relationships with other people goes together; material about one kind of situation (for example a
  state of mind, a medium, a setting) goes together.

His moves that every model missed, all of this kind: the shame and forgiveness sections went under the Nurturer, the
role that does that repair; the spiritual sections under the Inner Guide; the sections about altered states under the
Altered States part; the vow under Practicing.

How he decides whose work it is (Joel, 2026-11-20 23:03 UTC, his answer to question 114; lesson inner-child-2026-11-20m):
- **Ask whom a person would go to for it.** "when you have shame or you need forgiveness, it is someone who feeling like a
  nurturer that you go to for that. you don't go to a policew officer (protector) for help with those [...] love accepts.
  protection blocks. guide directs. shame and forgiveness need acceptance."
- **A catch-all part is not the home for a primary obstacle.** "healing old patterns is just a catch all category which
  is not important enough to deal with such a primary obstacle."
- **A catch-all part holds the techniques that don't fit cleanly into one role.** (Joel, 2026-11-21 01:47 UTC, question
  116: "yes all 3 roles are for healing old patterns, that's true. this section is basically where we have decided to put
  techniques that don't seem to fit cleanly into just one role".) Once moves into the roles leave it nearly empty, ask
  the author whether it should go, and where each section left would land in the flow (question 117).
- **A practice goes under a role only when the role must do it; otherwise it goes where the flow lands.** "a practice is
  something that could be done by any of the roles [...] mantra practice, that's primary to the Guide, so it could go
  under the Guide, but the Guide does not need to give a mantra practice to be a good guide, so it doesn't need to go
  there if it fits better somewhere else [...] if the thing must go under a role then it goes there, but if it's optional
  there and the flow would have it come elsewhere then it would prob go elsewhere."

- **What lies beyond a role goes to the role that points there.** (Joel, 2026-11-20 23:22 UTC: "the nurturer doesn't
  give divine love, they give the love of the nurturer [...] divine love is beyond taking care of someone, or hugging
  them, or being with them or listening to them. it's infinite, it's unspeakable...") So divine love goes under the
  Guide, which directs toward it; his line under the Nurturer says so: "This is what the Inner Guide can bring you to."
- **A problem goes where the reader meets it.** How Distrust Reproduces went under Finding People and Building Trust.

With his answer to question 114 added to the frame, a blind card sort of the inner child guide put shame and forgiveness
under the Nurturer and gave the best order score of any outline so far (turn 133, run 4: `RESULTS-4.md`).

## Before the sort: ask the author about the framework (lesson inner-child-2026-11-20p)

In real work there is no author's outline to compare a model's with, so his view has to come before the sort, not after
a miss (Joel, 2026-11-20 23:22 UTC: "you need to ask the author for their view before the models miss... because what
are they even missing?"). These questions come from the guide's own structure, so they can be asked of any guide on day
one; ask them in one message, with the guide's roles and parts named.

**Start with the parts and roles the guide doesn't define (lesson inner-child-2026-11-20r).** `python3
tools/humanization/undefined_parts.py GUIDE.md` (or the post's HTML) lists every heading that has sections under it and
little or no text of its own. For each one, ask the author what it is for and what looks as if it belongs but doesn't,
and put the answer in the frame in place of a model's description. A model asked what such a part is for reads it off
what sits under it now, even when told not to. On 4 November the inner child guide's Nurturer and 7 of its 9 parts had no
text of their own, and the frame for the sorts gave the Nurturer "borrowing love from other people or from a spiritual
source ... and widening the sense of what happiness is possible", and Healing Old Patterns distrust, shame and
forgiveness: that sent 8 of his 20 moves back where they were. Joel, 2026-11-20 23:22 UTC: "is that really hard for ai
to understand the diff?" It wasn't: the text says it, and GPT, with no frame, put three of the five spiritual sections
under the Guide in turn 132. The list points to questions, not to sections: his moved sections sat under such headings
no more often than all the others did (`articles/inner-child-therapy/experiments/t133-order/DOUBT.md`).

**Send only what the guide and his answers leave open (lesson inner-child-2026-11-21a; Joel, 2026-11-21 01:08 UTC: "send
me any qeustions that you can't find answered in the article").** Look for each answer first: in the opening, any
overview of stages or parts, each part's first section, the names themselves, and what he has already answered. Keep a
table of where each is answered beside the questions, and send the rest. Of the 11 parts and roles his reorganized inner
child guide gives no text of their own, 10 were answered that way and one question went to him
(`articles/inner-child-therapy/experiments/t137-questions/ASKED.md`). When the sort will be scored against an outline of
his, ask only what a reader of the guide could ask without that outline, never about where he moved something, or the
score measures his answers and not the method.

The questions:

1. For each role (or figure, tool or stage the guide is built on): what belongs to it that a reader might not guess, and
   what looks as if it belongs but doesn't? Whom would a reader go to for it?
2. For each pair of roles that touch: what decides between them?
3. Which parts are catch-alls, and what should never be filed there?
4. Is there anything beyond the roles (as divine love is beyond the Nurturer's care), and which role points to it?
   Get both halves.
5. Where do practices go: under a role, or where the reader needs them?
6. What does a reader meet first, and what can wait?

**Every answer has to say where a thing goes, not only where it doesn't (lesson inner-child-2026-11-21b).** When an
answer only rules a place out, ask once more: "so where does it go?" In the inner child guide's run 5, the readers took
his "the nurturer doesn't give divine love": they gave the divine-love sections no role at all. With nothing naming where
divine love leads, they left all five where they were. Run 5b added one line of his, "This is what the Inner Guide can
bring you to", and all five went to the Guide's side (`articles/inner-child-therapy/experiments/t133-order/RESULTS-5B.md`).

The readers' own doubt is a weak guide to anything else worth asking (`articles/inner-child-therapy/experiments/t133-order/DOUBT.md`):
in the blind sort they were unsure about 14 of the 20 sections he moved, but also about 65 he left alone, and their
doubt came without his answer. Second homes didn't help either (lesson inner-child-2026-11-21c): in runs 5 and 5b, 84
and 94 unsure sections had a second home, with fewer of his moves among them than chance would give. And the guide's own
words alone are too thin a frame where most parts have none: the readers scatter sections more than with a model's
description of each part.

**The frame, since 2026-11-21 (run 6; lesson inner-child-2026-11-21e):** a model's description for each part and role the
guide describes in its own words, and the author's words for each one it doesn't (from the opening, any overview, and
his answers to the questions above), with his answers on how he sorts things
(`articles/inner-child-therapy/experiments/t133-order/make_frame6.py`). On the inner child guide it found as many of his
moves at high confidence as the best earlier frame (3 of 20), with about half the wrong ones (5 against 9) and twice his
level changes (6 against 3), and it put 4 of the 5 divine-love sections on the Guide's side
(`articles/inner-child-therapy/experiments/t133-order/RESULTS-6.md`). It still misses most of his moves: the sort is a
proposal, put to him move by move.

## After the sort: help the readers find their way (lesson inner-child-2026-11-21d)

Joel, 2026-11-21 13:07 UTC: "in that approach you should recommend how to improve the guide so the real readers will
also know where they would look for the sections". The gaps that mislead a model mislead a reader too, so the approach
ends with recommendations to the author, each a proposal with its evidence:

1. A line or two under each part and role with no text of its own (`tools/humanization/undefined_parts.py` lists them),
   drafted from the author's own words, with those words given beside it. One "how this guide is laid out" paragraph near
   the top can do the same job for a first-time reader.
2. A pointer, with a link, at each place where most readings of the sort would look for a section under another part or
   another role than the one it is in. A neighbouring heading inside the same part needs none: the sidebar shows them
   together.
3. After he picks, each line and pointer goes into his post only once it reads Human with High confidence in Pangram,
   in its place (lesson inner-child-2026-11-21f; Joel, 2026-11-21 13:31 UTC: "make sure you don't add anything that
   hasn't passed pangram with high conf"). A move or a heading's level changes no words and needs no check.
4. Then the contents test with fresh readers and real situations ("where would you look first?") runs again on the new
   contents, to see whether the lines and pointers changed where readers look.

The inner child guide's: `articles/inner-child-therapy/experiments/t139-readers/RECOMMENDATIONS.md`, made by
`where_readers_look.py` and `recommend.py` there.

## 3. Order inside each part

What a reader needs first comes first: readiness and foundations before techniques, the general before its special
cases, the common case before the rare one. Keep the author's order wherever these rules don't call for a change.

## 4. Levels

- A section that is a case, part, tool or example of another sits one level below it.
- Siblings are the same kind of thing at the same level of generality.
- A heading with only one section under it, or a heading over a single line or punchline, is a sign to merge it into
  its neighbour or parent.
- A grouping heading with no text of its own is fine when it has two or more sections under it; an empty heading with
  nothing under it should go.
- Only levels 1 to 4 show in the contents; use level 5 for a heading readers shouldn't see listed.

## 5. Change only what serves readers

Every move needs a reason a reader would recognize ("someone looking for X would look under Y"). Don't move things to
make the outline look tidy. Before you move a section, check what the text says around it: "above", "further on", "in
the next section", or the name of another section. A move can make such a pointer wrong; list those so they can be fixed.
