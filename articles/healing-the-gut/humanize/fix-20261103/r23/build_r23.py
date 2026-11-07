#!/usr/bin/env python3
"""r23 = r22 (the article with every answer in, batch 13 included) with Phase 4's second organ case and Phase 5 rewritten
so the stretch of Phases 3 to 6 tests Human (gate gut-2026-11-07a; Joel, 2026-11-06 23:59 UTC: "make sure you're fixing
any paras or sections that test ai before you ask for whole articel checks").

What tested AI, and on which words: the cut of Phases 3 to 6 read Phase 4's organ cases, Phase 5's opening, its first
three steps (his "Does anyone count their plants?" with them) and Phase 6's Hopper sentence AI, unchanged (#187); the cut
of Phases 4 and 5 read Phase 5's first three steps AI and Phase 4's second organ case Low (#186). Try 2's steps read AI in
the whole article too (#189), with three neighbours pulled down to Low.

The diagnosis, from the moves his own fixes make (the neuro lane's lessons of 23:01 and 23:50 UTC, neuro-2026-11-06b and
e, and his own Phase 1): these sentences have things as their subjects and purpose clauses where people act ("It contains
L. reuteri, to heal the lining ...", "the test is SeHCAT, and the treatment is bile binders"), they don't say in their own
words how each follows from the one before, and step 3 says again what Phase 2 says. So:
- people act: "you'd test for that with SeHCAT, and treat it with bile binders", as the first organ case already does;
  "which you ferment at home"; "He picked its bacteria for what they do";
- the tie in the words: "And if", "Cleared the infection? Then", "the way Bulsiewicz says";
- each term explained where it is first used: Bile Acid Diarrhea (bile spilling into the colon and giving you diarrhea;
  NICE DG44), oxytocin (the "love hormone"), bacteriocins (natural antibiotics);
- step 3's reason, the MMC's sweep, is Phase 2's; what only step 3 says is "forever" (bad-trips-2026-11-06a), so it keeps
  that and points to Phase 2;
- his aside, "Does anyone count their plants?", stays as he wrote it, after the number it jokes about.
Writes r23.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r22' / 'r22.md').read_text(encoding='utf-8')
CHANGES = []
NICE = 'https://nice.org.uk/guidance/dg44/documents/topic-description'


def ch(old, new, kind, why, source=None):
    global md
    assert md.count(old) == 1, (old[:60], md.count(old))
    md = md.replace(old, new)
    CHANGES.append(dict({'old': old, 'new': new, 'kind': kind, 'why': why}, **({'source': source} if source else {})))


ch('If it\'s Bile Acid Diarrhea, the test is SeHCAT, and the treatment is bile binders.',
   'And if bile is spilling into your colon and giving you diarrhea, called Bile Acid Diarrhea, you\'d test for that with '
   'SeHCAT, and treat it with bile binders.', 'window',
   'Low in the cut of Phases 4 and 5 (#186) and in draft C (#189), AI Low in the cut of Phases 3 to 6 (#187): the term '
   'explained where it is named, as the first organ case explains Exocrine Pancreatic Insufficiency, and you doing the test '
   'and the treatment where the test and the treatment were the subjects (neuro-2026-11-06e); "And if" ties it to the case '
   'before', NICE + ' (bile acids that aren\'t absorbed travel to the colon, and excess bile there causes diarrhoea)')
ch('Once you\'re clear of infection, you have to rebuild a diverse ecosystem to prevent relapse.',
   'Cleared the infection? Then it\'s time to rebuild a diverse ecosystem in your gut, so the overgrowth doesn\'t come back.',
   'window',
   'AI Low in the cut of Phases 3 to 6 (#187), Low in that of Phases 4 and 5 (#186): the reader\'s case as a question that '
   'asks them in first (neuro-2026-11-06b), "so the overgrowth doesn\'t come back" for "to prevent relapse"')
ch('1. Start by re-seeding with Davis\'s high-dose "SIBO Yogurt", fermented for 36 hours. It contains L. reuteri, to '
   'heal the lining and boost oxytocin, and L. gasseri, to produce bacteriocins that kill SIBO.',
   '1. Start by re-seeding your gut with Davis\'s high-dose "SIBO Yogurt", which you ferment at home for 36 hours. He '
   'picked its bacteria for what they do: L. reuteri heals your gut lining and boosts oxytocin (the "love hormone"), and '
   'L. gasseri makes bacteriocins, natural antibiotics that kill SIBO.', 'window',
   'AI in both cuts (#186, #187), Low in draft B (#183): you and Davis act where the yogurt was the subject with purpose '
   'clauses (neuro-2026-11-06e); oxytocin and bacteriocins explained where first used (E369)',
   'Davis chose the strains himself: "So I chose three in my original recipe for what I called SIBO yogurt", among them '
   'L. reuteri and L. gasseri (Defiant Health Radio, https://www.buzzsprout.com/1795054/episodes/17783323-here-s-a-microbe-'
   'you-should-know-about-bacillus-subtilis)')
ch('2. Then feed the new healthy bacteria. Bulsiewicz says to slowly titrate plant diversity back into your diet, '
   'aiming for 30+ different plants per week.',
   '2. Then feed the new healthy bacteria with plants, slowly, the way Bulsiewicz says: add a few new kinds at a time, '
   'until you eat 30+ different plants a week.', 'window',
   'AI in both cuts (#186, #187), Low in draft B (#183): the short sentence joined to how (E368), "the way Bulsiewicz says" '
   'ties the how to the act, and "add a few new kinds at a time" for "slowly titrate plant diversity back"; his "Does '
   'anyone count their plants?" stays right after the number')
ch('3. Continue Pimentel\'s strict meal spacing from Phase 2 (4+ hours), forever, to keep the MMC cleaning wave active.',
   '3. Keep spacing your meals 4+ hours apart, as in Phase 2, forever.', 'repeat',
   'AI High in both cuts (#186, #187): its reason, the MMC sweeping your gut clean between meals, is Phase 2\'s ("so the '
   'Migrating Motor Complex (MMC) gets to sweep your gut clean in between"), with Pimentel; what only this step says is to '
   'keep it up forever, so it keeps that and points to Phase 2 (bad-trips-2026-11-06a)')
(HERE / 'r23.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'changes;', len(md.split()), 'words')
