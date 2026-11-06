#!/usr/bin/env python3
"""r17 = r16 (every batch answer in) with the windows earlier checks left below High fixed, as Joel set the bar on
2026-11-06 20:13 UTC: "if it's "low" we should fix it, medium you could try to fix but if it's too difficult we can put
that as a later todo when we want to learn more, and some things are not worth fixing, pangram has some bugs, like
"Why?" often reads as medium". Under E373 these are the model's words he kept, so the fixes are mine, tested, on approve
cards. Writes r17.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r16' / 'r16.md').read_text(encoding='utf-8')
CHANGES = []


def ch(old, new, kind, why):
    global md
    assert md.count(old) == 1, (old[:60], md.count(old))
    md = md.replace(old, new)
    CHANGES.append({'old': old, 'new': new, 'kind': kind, 'why': why})


ch(') to feed the good bacteria in your gut, since your body can\'t digest it.',
   ') to feed the good bacteria in your gut: your body can\'t digest it, so it all goes to them.', 'window',
   'Low (#170): the point first as before, and the why as a plain clause joined with a colon instead of "since"')
ch('So check your organs (Brown). Is it Exocrine Pancreatic Insufficiency, where your pancreas doesn\'t make enough '
   'digestive enzymes? You\'d test for that with Stool Elastase, and treat it with high-dose enzymes. Or is it Bile Acid '
   'Diarrhea? That test is SeHCAT, and the treatment is bile binders.',
   'So check your organs (Brown). If your pancreas doesn\'t make enough digestive enzymes, called Exocrine Pancreatic '
   'Insufficiency, you\'d test for that with Stool Elastase, and treat it with high-dose enzymes. If it\'s Bile Acid '
   'Diarrhea, the test is SeHCAT, and the treatment is bile binders.', 'window',
   'Medium (#164): each case opens on what the reader would have, and the question-and-answer pairs are joined into one '
   'sentence each (E368, E371, E374 (neuro)); the tests and treatments word for word')
ch('And if you\'re pregnant, some herbs and supplements, like berberine, aren\'t safe.',
   'And if you\'re pregnant or breastfeeding, skip berberine, which can give a newborn jaundice, and ask your doctor about '
   'any other herb or supplement first.', 'window',
   'Medium (#166): the acts named exactly, with the reason (E371); NCCIH: people who are pregnant or breastfeeding '
   'should not use berberine, which can cause or worsen jaundice in newborns, https://www.nccih.nih.gov/health/in-the-news-berberine')
ch('Beta-glucans, a kind of fiber found in yeast extract.',
   'Beta-glucans, a kind of fiber found in yeast extract, to help your gut lining hold together under stress.', 'window',
   'Medium with the resistant starch item (#175): the item said what beta-glucans are but not what they are for, the '
   'reader\'s reason (E371); in gut tissue taken from people, a yeast beta-glucan kept the lining from leaking when it '
   'was stressed, https://pmc.ncbi.nlm.nih.gov/articles/PMC6166688')
(HERE / 'r17.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'changes;', len(md.split()), 'words')
