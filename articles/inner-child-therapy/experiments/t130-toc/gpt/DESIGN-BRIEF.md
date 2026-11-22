# Design brief: a contents for the inner child guide that works in Substack's narrow sidebar

The guide is Joel's Substack post "Inner Child Self-Love Reparenting Guide" (about 28,000 words). Its readers find their
way with Substack's contents sidebar: one line per heading, h1 to h4 (an h5 isn't listed), and every line is cut off
with "…" where the sidebar ends. Today 105 of its 147 listed headings are cut off. Joel, 2026-11-16: "we should be
optimizing substack posts specifrically for their very narrow toc sidebar so we might need to rethink some headings".

**The goal:** a reader who comes with a real situation can tell from the sidebar alone which heading to open.

## The files

- `GUIDE-BY-SECTION.md`: the guide's whole text as it is live now, each section under its heading with its id
  (`[S023]`), its level (number of #) and its word count. `[IMAGE]`, `[YOUTUBE]` and the like mark pictures and videos.
- `TOC-NOW.md`: the contents as it is, with what the sidebar shows for each heading.
- `tool/toc_sidebar.py`: measures a heading the way the sidebar does.
  `python3 tool/toc_sidebar.py --text "Your Heading" --level 2` says whether it fits; `python3 tool/toc_sidebar.py
  FILE.md` checks a whole contents written as Markdown headings.

## What you may change

- Rename a heading.
- Move a whole section, with its subsections.
- Change a heading's level.
- Drop a heading, so its text joins the section before it.

Nothing else: no new headings, no splitting a section, no changes to the text.

## The room

The sidebar leaves 217px for an h1, 205 for an h2, 193 for an h3 and 181 for an h4, at 15px. Aim for headings that fit
with 12px to spare (the tool says "fits"; "tight" may be cut for some readers): roughly 26 characters for an h1, 24 for
an h2, 22 for an h3 and 20 for an h4, fewer with wide letters. When a heading has to be longer, put the words that say
what's under it first, so what gets cut is only extra. A parent heading already tells the reader where they are, so its
children needn't repeat it (under "The Nurturer", a child needn't say "Nurturer").

## Joel's voice and his decisions

- He writes playfully on purpose: "Talk to the hand!✋🏿", "Ask God for a Loan 🫶🏿", "Write It. Don't Send It Yet.",
  "Listen To Your Body, Or Else!". Keep that voice. His own words are his coinages and the guide's terms: the little
  one, pl/ork, borrowed adulthood, the parent you inherited, belonging bargains, the Nurturer, the Protector, the Guide.
- Rename only when a reader can't tell what's under a heading, or the sidebar cuts off the part that says it. Take the
  new words from his own text in the section wherever you can.
- His order is his decision. He reorganized the guide himself on 3 November and again since. Building Your Inner Adult
  runs Borrow, then Protector, then Nurturer, then Guide, for the reason he wrote: "first he/she wants to feel safe
  (Protector), then, building on that safety, feel loved (Nurturer), and then building on the safety & love, trust
  allows the little one to be eager to take guidance". Move a section only when a reader would clearly look for it
  somewhere else, and say why.
- Lessons from earlier structure work on this guide: don't undo his moves; order carries meaning; a section stays with
  the image it extends.
- The text names some headings ("Noticing Counts", "Untangling the Belonging Bargains", "Ask God for a Loan",
  "Altered States Can Deepen Therapy or Escapism", "Use Hindsight to Re-do Traumatic Memories In A Healther Way"). If
  you rename or move one of those, list it, so the words that point to it can change too.

## What to hand back

1. `PROPOSAL.json`: the contents you propose, in reading order, one entry per section id of `TOC-NOW.md`, each exactly
   once: `{"id": "S023", "level": 2, "heading": "..."}`, or `{"id": "S041", "drop": true}` for a dropped heading.
2. `PROPOSAL-NOTES.md`: each change with its reason in one line, and the headings where you'd ask Joel before replacing
   his words.
