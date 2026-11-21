You are naming the headings of a long harm-reduction guide on Substack so they work in Substack's narrow contents sidebar.

Read these files, in this order, and nothing else:
1. /home/claude/joel-articles/tools/humanization/headings_brief.md — the brief. Follow rules 1 to 10 and read its last
   section (where earlier writers missed the author's picks, and why).
2. /home/claude/joel-articles/articles/bad-trips/humanize/h64-20261121/toc/ARTICLE.md — the guide, section by section:
   each section's id, level (1 to 4), heading as it stands, and its text.

Measure every heading you propose with the sidebar tool, from the shell:
  python3 /home/claude/joel-articles/tools/humanization/toc_sidebar.py --text "Your Heading" --level N
It prints fits, tight or cut. A heading must print "fits" (rule 1). "tight" may be cut for some readers: avoid it.

What the author has asked for, besides the brief:
- Keep his order and levels: no section moves, merges or changes level. Name every one of the 62 sections.
- If his heading already fits and does its job, keep it exactly as it is (rule 1). Keep his words, his capitals where they
  are right under rule 7, and his playful ones ("Inner Signal App to the Rescue!", "Spiritual ≠ "Getting Your Ass
  Kicked"", "Metta NMT Sniffer Makes the Trip Chill & Lovey!") wherever a version that fits can keep their point.
- This is a guide people open in an emergency, for themselves or a friend who is tripping or has taken too much: a reader
  scanning the sidebar is looking for their situation ("my friend is seizing", "it won't stop", "I think my brain is
  damaged") or the thing to reach for. Rule 3 decides the words.
- The remedy sections (zeolite, activated charcoal, coffee cherry, the Metta NMT sniffer, humic acid, creatine, mango leaf
  tea, essential oils, DMSO, Syrian rue oil, ocean water, the shungite and charcoal waters, beach morning glory, niacin)
  will each get a short evidence tag on its own line under the heading, so the heading doesn't need to say what the
  remedy rests on. A remedy's own name is what a reader looks for: keep it in its heading.
- Some headings are links in the post (ZHoly3O, Coffee Cherry, DMSO); keep the linked name in the heading.
- Never bring back "The Longer Triage: What Kind of Trouble Is This?" (he cut it).

Write your answer to /home/claude/joel-articles/articles/bad-trips/humanize/h64-20261121/toc/PROPOSAL-FABLE.json as a JSON
list with one object per section, in the article's order:
  {"id": "...", "level": N, "heading": "the heading you propose", "from": "yours" if it is exactly his heading, else
   "fable", "kind": "situation" | "practice" | "point" | "name" (a remedy or a tool named), "why": "one line, for a
   changed heading: what the reader came for and what you kept of his words"}
Then reply with a short summary: how many you kept, how many changed, and any heading you could not make fit.
