"""make_candidate.py - the sweep fixes of 2026-10-13 (SWEEP-RESULTS.md, 18) and the E172 repeat fixes in my words (3),
applied to a copy of HUMANIZED-SO-FAR.md as CANDIDATE.md, with FIXES.json recording each change. Run from fix-20261014/.

Each fix changes only the flagged words; the reason is the cold reads' flag (SWEEP-RESULTS.md) or the repeats check
(repeats/REPEATS-DISPOSITIONS.md). Facts added are sourced in SOURCES.md.
"""
import json, pathlib

H = pathlib.Path(__file__).resolve().parent
art = (H.parent / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')

FIXES = [
 # key, section, why, old, new
 ('S3P4f', 3, 'sweep: "they take turns talking about it ..." (3 reads: five "it"s, the seconding rule never named; published: "whether the motion requires a second")',
  'It can only make it so that they take turns talking about it, and that whoever raises it has to find somebody who agrees with him or her before they get to talk about it.',
  'It can only decide whose turn it is to talk about the hatred, and whether a motion about it needs somebody to second it.'),
 ('S3P10f', 3, 'sweep: "The deeper problem is that someone carries authority earned in one domain into the others." (5 reads: "the others" unnamed; published: "authority earned in one role can be spent in every other role")',
  'The deeper problem is that someone carries authority earned in one domain into the others. The founder who is a good teacher,',
  'The deeper problem is that somebody who\'s earned authority in one role can use it in all their other roles. The founder who is a gifted teacher,'),
 ('S6P8f', 6, 'sweep: "cultivating more human independence" (2 reads: from what?), "an exit" (3 reads: from what?), "technosphere" never explained (2 reads; his rule of 2026-10-09: explain at first mention). Source for the gloss: SOURCES.md',
  'it makes more sense to me to focus on cultivating more human independence than to wait for certainty. It\'s better to have community and find out I didn\'t need an exit than to need an exit after spending ten years',
  'it makes more sense to me to focus on cultivating more human independence from the technosphere, all the machines and systems modern life runs on, than to wait for certainty. It\'s better to have community and find out I didn\'t need a way out of the technosphere than to need one after spending ten years'),
 ('S7P6f', 7, 'sweep: "ZEGG and Tamera have spent decades ..." (2 reads: names never introduced). Sources: SOURCES.md',
  '[ZEGG](http://zegg.org/) and [Tamera](http://tamera.org/) have spent decades',
  '[ZEGG](http://zegg.org/), a community near Berlin, and [Tamera](http://tamera.org/), another in Portugal, have spent decades'),
 ('S8P10f', 8, 'sweep: "another promo video" (4 reads: "another" points back at the son\'s video; the article has no earlier promo video)',
  'What she said is more useful than another promo video showing kids smiling and carrying vegetables.',
  'What she said is more useful than the usual promo video showing kids smiling and carrying vegetables.'),
 ('S8P12f', 8, 'sweep: "the Ye\'kuana" (5 reads: never identified). Sources: SOURCES.md',
  'It\'s one outsider\'s interpretation of the Ye\'kuana, and she may have idealized',
  'It\'s one outsider\'s interpretation of the Ye\'kuana, an Indigenous people of the Venezuelan rainforest she lived with, and she may have idealized'),
 ('S8P20f', 8, 'sweep: "Fear like that can destroy that gift" (2 reads: "that gift" has no antecedent, "Fear like that" skips back; published: "Fear can destroy that gift"). People are the subject, not the fear (his F2, F5 and F8 answers: an abstract thing doing what a person does)',
  'Fear like that can destroy that gift, and it might not even prevent abuse.',
  'When adults panic like that, kids can lose all those grownups without the panic actually preventing abuse.'),
 ('S8P23f', 8, 'sweep: "at the end of a certain date it has to be told" (3 reads: needs a reread; mine; published: "Surprises have an ending date")',
  'A surprise isn\'t a secret, because at the end of a certain date it has to be told.',
  'A surprise has an end date.'),
 ('S8P26f', 8, 'sweep: "the Island Pond raid", "the state\'s blanket request" (5 reads: whose kids, why, what the state asked). Sources: SOURCES.md',
  'In 1984, Vermont authorities [seized 112 kids in the Island Pond raid](https://vtdigger.org/2024/06/21/40-years-later-island-pond-has-little-interest-in-revisiting-its-historic-raid/), but a court rejected the state\'s blanket request and returned them.',
  'In 1984, Vermont authorities [raided a religious community in Island Pond](https://vtdigger.org/2024/06/21/40-years-later-island-pond-has-little-interest-in-revisiting-its-historic-raid/) and took 112 kids into custody over suspected abuse. A judge turned down the state\'s blanket request to hold them, because it couldn\'t name any specific case, and the kids went home that same day.'),
 ('S8P27f', 8, 'cold reads (SENSE-s8.md and SENSE2-s8.md, 2 reads): "the research corpus" (which corpus?); published words ("I also searched the research corpus"), so a fix I propose under the rule for flags two reads raise',
  'I looked through [the research corpus](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) for a well-documented case',
  'I looked through [all the research I\'d gathered](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) for a well-documented case'),
 ('S9P2f', 9, 'sweep: "caracoles" (2 reads: unexplained). Source: SOURCES.md',
  'went down to Oventik, one of the Zapatista *caracoles* in Chiapas.',
  'went down to Oventik, one of the Zapatista *caracoles* ("snails"), the regional centers that tie their villages together in Chiapas.'),
 ('S9P18f', 9, 'E172 repeat (REPEATS-s2.md #37, s4 #35, s12 #37): "not claiming they already proved my whole model" repeats his P14 ("don\'t prove my whole money-free economy goal"); the paragraph already says the evidence wasn\'t found',
  'I\'m borrowing the Zapatistas\' teaching method and their ambition to replicate, not claiming they already proved my whole model.',
  'I\'m borrowing the Zapatistas\' teaching method and their ambition to replicate.'),
 ('S10P9f', 10, 'sweep: "a collision of two principles" (4 reads: none named, abrupt; published opens "And when two principles collide", after the solidarity limits)',
  'When you create or apply a rule to deal with a collision of two principles, don\'t only store the rule.',
  'Limits like those come from two principles colliding, solidarity and each community\'s claim on its own labor and stores. Whenever you create or apply a rule where principles collide, don\'t only store the rule.'),
 ('S11P2f', 11, 'sweep: "Founderism" (6 reads: the heading\'s word is never defined; his P13 says "founderism is a problem in every community")',
  'That person ends up with real influence, and pretending they don\'t just makes that influence harder to look at.',
  'That person ends up with real influence, and pretending they don\'t just makes that influence harder to look at. When that influence goes unchecked, I call it founderism.'),
 ('S11P4f', 11, 'sweep: "Can it correct a prediction that turned out wrong?" (11 reads: whose prediction?); E172 repeat (REPEATS-s2.md #39, s4 #37): "Can it replace the founder?" is asked again three blocks later in the four questions',
  'Can it correct a prediction that turned out wrong? Can it replace the founder? And if it\'s meant to spread',
  'When the method gets a prediction wrong, can the community say so and change course? And if the community is meant to spread'),
 ('S11P6f', 11, 'sweep: "Here are the four questions about the founder:" (3 reads: not set apart from the many questions above)',
  'Here are the four questions about the founder:',
  'The questions so far have been about the method. These four are about the founder:'),
 ('S11P8f', 11, 'sweep: "who picks the reviewers" (9 reads: reviewers of whom?; P9 says "the person to review the founder")',
  'Who decides who gets admitted, and who picks the reviewers?',
  'Who decides who gets admitted, and who picks the people who handle complaints?'),
 ('S11P9f', 11, 'sweep: "no matter how many circles it holds" (7 reads: circles never set up in this section)',
  'there\'s no way for the community to override the founder, no matter how many circles it holds.',
  'there\'s no real way for the community to override the founder, no matter how many meetings it holds.'),
 ('S11P10f', 11, 'sweep: "Also watch for the daily signs." (2 reads: signs of what?)',
  'Also watch for the daily signs.',
  'Also watch for the daily signs of founderism.'),
]

out = art
rec = []
for key, sec, why, old, new in FIXES:
    assert out.count(old) == 1, (key, out.count(old))
    out = out.replace(old, new)
    rec.append({'key': key, 'section': sec, 'why': why, 'old': old, 'new': new})
(H / 'CANDIDATE.md').write_text(out, encoding='utf-8')
json.dump(rec, open(H / 'FIXES.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rec), 'fixes ->', H / 'CANDIDATE.md')
