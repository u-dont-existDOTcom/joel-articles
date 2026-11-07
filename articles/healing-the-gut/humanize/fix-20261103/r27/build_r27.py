#!/usr/bin/env python3
"""r27 = r26 with Phase 4's organ paragraph rewritten after the tell panel (E346; ../r26/panel/PANEL.md).

The paragraph by itself read AI Generated, 100%, High as r24 (#196) and r25 (#199). The panel's two fresh readers
(Sonnet and Haiku, from the prompt alone) agreed on both case sentences and on the build: each case runs symptom, name,
test, treatment, "a diagnostic menu" whose two halves mirror each other; "you'd test for that with ... and treat it with
..." is a stock frame; "called X" and "(X)" are the same lay-to-technical gloss twice; "may not" is a generic hedge. His
own diagnostic case elsewhere in the article reads Human: "if you get heartburn when your stomach is empty only, that's
usually H. pylori, and it's easily treated with berberine" (Parasites), and Phase 6 names its condition through its
author ("Hopper says the issue is Limbic System Impairment"). So:
- the first case keeps the reader's question, says "it's often your pancreas", where "may not be" hedged, and has people
  naming it ("which doctors call");
- its test and treatment get their own sentence and a detail the reader can use ("A Stool Elastase test will tell you, and
  if that's it, you take high-dose enzymes with every meal"; enzyme capsules go with every meal or snack, Healthline);
- the second case opens on what the reader would notice, has Brown name it as Hopper names hers, says what happens in
  plain words, and says what the binders do ("soak up the extra bile").
Writes r27.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r26' / 'r26.md').read_text(encoding='utf-8')
old = ('So check your organs (Brown). Do your stools look oily or greasy? Then your pancreas may not be making enough '
       'digestive enzymes, called Exocrine Pancreatic Insufficiency, and you\'d test for that with Stool Elastase and treat '
       'it with high-dose enzymes. If too much of your bile is reaching your colon and giving you diarrhea (Bile Acid '
       'Diarrhea), Brown has you tested with SeHCAT and put on bile binders.')
new = ('So check your organs (Brown). Do your stools look oily or greasy? Then it\'s often your pancreas not making enough '
       'digestive enzymes, which doctors call Exocrine Pancreatic Insufficiency. A Stool Elastase test will tell you, and if '
       'that\'s it, you take high-dose enzymes with every meal. If it\'s diarrhea that keeps coming back instead, Brown says '
       'the issue can be Bile Acid Diarrhea, where too much of your bile reaches your colon. He has you tested for that with '
       'SeHCAT, and bile binders soak up the extra bile.')
assert md.count(old) == 1
md = md.replace(old, new)
CHANGES = [{'old': old, 'new': new, 'kind': 'window',
            'why': 'the paragraph alone read AI High twice (#196, #199); the tell panel agreed on both cases and the build '
                   '(a two-case menu, a stock test-and-treat frame, the same gloss twice, a generic hedge): each case now '
                   'has its own shape, people name the conditions, the test and treatment carry a usable detail',
            'source': 'https://www.healthline.com/health/exocrine-pancreatic-insufficiency/treatment-options (enzyme '
                      'capsules at the beginning of every meal or snack); https://nice.org.uk/guidance/dg44/documents/'
                      'topic-description (bile acids not absorbed reach the colon and cause diarrhoea)'}]
(HERE / 'r27.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'change;', len(md.split()), 'words')
