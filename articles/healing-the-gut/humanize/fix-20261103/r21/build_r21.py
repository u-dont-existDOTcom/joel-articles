#!/usr/bin/env python3
"""r21 = r17 with the two clarity fixes that read Human, High in their stretch (r19-D, #185), and a third try at Phase 5's
first two steps, which read Low in the whole article (#183: calibrated 0.79, 0.58 and 0.63).

Why a third try, and why this one. Try 1 (../r19/, #184) joined each step to what it does and read worse than its control
(59% AI against 30%, #186). Try 2 (../r20/, #188) put the reader's situation first and read no better than its control in
the Phases 3-6 cut (28.3% against 27.8%, #187); that cut reads the steps AI even unchanged, where the whole article reads
them Human (Low), so it can't show a fix, and the whole article judges tries 2 and 3 (drafts C and D, his extension).
What neither try did is what his own fix of the model's Phase 1 did, after three of our versions of it read AI: he kept
its frames and glossed each term in a plain parenthesis or clause ("which in medical lingo is called", "not flowing well",
"an extract of beet greens", "the dying microbes release toxins you can't detoxify"), and in the whole article it reads
High. The steps still carry the model's compression: "high-dose" with nothing to say what makes it so, bare purpose
clauses ("to heal the lining and boost oxytocin", "to produce bacteriocins"), and "titrate plant diversity", a verb no
reader uses. So this try keeps each step's frame and words and adds a plain gloss where the reader would ask:
- what makes the yogurt high-dose: Davis ferments it for about 36 hours where a factory takes about 6 to 12, so it ends up
  with hundreds of times more microbes (Davis, Defiant Health Radio, "Will eating yogurt change your life?");
- what oxytocin and bacteriocins are (the "love hormone"; natural antibiotics), at their first use (E369);
- why slowly: the gut's microbes need time to adapt to a change of diet, and more fiber than they're used to brings gas
  and bloating (Bulsiewicz in Plant Based News, 27 April 2025);
- "bring more and more kinds of plants back into your diet, slowly" for "slowly titrate plant diversity back".
His aside, "Does anyone count their plants?", stays as he wrote it, after the number it jokes about. Writes r21.md and
CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r17' / 'r17.md').read_text(encoding='utf-8')
CHANGES = []
DAVIS = 'https://defianthealthradio.buzzsprout.com/1795054/episodes/16962045-will-eating-yogurt-change-your-life'
BULSIEWICZ = 'https://plantbasednews.org/lifestyle/health/gut-doctor-survival-guide-bloating-plant-based-diet/'


def ch(old, new, kind, why, source=None):
    global md
    assert md.count(old) == 1, (old[:60], md.count(old))
    md = md.replace(old, new)
    CHANGES.append(dict({'old': old, 'new': new, 'kind': kind, 'why': why}, **({'source': source} if source else {})))


ch('so come back down once it\'s over.', 'so come back down once the exposure or the stress is over.', 'clarity',
   'the compare read (F1.2): "it" could be the exposure, the stress or the training; r19-D read Human, High (#185)')
ch('like Crohn\'s or colitis, don\'t count on it.', 'like Crohn\'s or colitis, don\'t count on glutamine.', 'clarity',
   'the compare read (F1.4): "it" could be the higher dose or glutamine itself; r19-D read Human, High (#185)')
ch('1. Start by re-seeding with Davis\'s high-dose "SIBO Yogurt", fermented for 36 hours. It contains L. reuteri, to '
   'heal the lining and boost oxytocin, and L. gasseri, to produce bacteriocins that kill SIBO.',
   '1. Start by re-seeding with Davis\'s high-dose "SIBO Yogurt", fermented for 36 hours (store yogurt is fermented for 6 '
   'to 12, so this one ends up with hundreds of times more bacteria). It contains L. reuteri, to heal the lining and boost '
   'oxytocin (the "love hormone"), and L. gasseri, to produce bacteriocins (natural antibiotics) that kill SIBO.',
   'window',
   'Low in the whole article (#183): the frame and words kept, and a plain gloss where the reader would ask, as his own '
   'fix of Phase 1 does: what makes the yogurt high-dose, what oxytocin and bacteriocins are (E369)',
   DAVIS + ' ("So in a factory they ferment or process the yogurt for about 6 to 12 hours"; 36 hours lets the microbes '
   'double many more times, "hundreds of times greater numbers of microbes than you get in conventional yogurt")')
ch('2. Then feed the new healthy bacteria. Bulsiewicz says to slowly titrate plant diversity back into your diet, '
   'aiming for 30+ different plants per week.',
   '2. Then feed the new healthy bacteria. Bulsiewicz says to bring more and more kinds of plants back into your diet, '
   'slowly (go too fast and you can get gassy and bloated while your gut bacteria adapt), until you\'re eating 30+ '
   'different plants per week.',
   'window',
   'Low in the whole article (#183): "bring more and more kinds of plants back into your diet, slowly" for "slowly '
   'titrate plant diversity back", with why slowly in a plain parenthesis; "until you\'re eating 30+" keeps his number '
   'right before his "Does anyone count their plants?", which stays as he wrote it',
   BULSIEWICZ + ' (Plant Based News, 27 April 2025: switching to a high-fiber diet can bring gas and bloating because the '
   'gut microbiome has to adapt; "It\'s going to take time for your gut microbes to adapt")')
(HERE / 'r21.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'changes;', len(md.split()), 'words')
