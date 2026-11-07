#!/usr/bin/env python3
"""r26 = r25 with Phase 4's first organ case opening on something the reader can recognize in their own case.

Phase 4's organ paragraph by itself read AI Generated, 100%, High twice: as r24 (#196) and as r25, with the second case
in its own shape (#199). The first case was the same in both, and it also read AI Low in both cuts of Phases 3 to 6
(#187, #192): one sentence that packs the condition, its name, the test and the treatment, with nothing the reader can
recognize in their own case. His own fix of the same kind of step, Phase 1, asks the reader first about what they would
notice ("Are your pupils dilated all the time?", "Do you burp extra ... after fatty meals?"), then says what that means
and what to do; the question form of this very case read High in Phase 4 (#164). So the case now opens on a sign the
reader can notice, oily or greasy stools, the fatty stools (steatorrhea) that are EPI's common sign (Healthline, reviewed
by Kevin Martinez, MD, 2023); then what that may mean, its name, the test and the treatment, with you acting. Not weight
loss: the article's warnings already list losing weight fast as a sign to see a doctor rather than try this, and a
question here shouldn't send that reader to their pancreas instead. The second case stays as r25 has it. Writes r26.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r25' / 'r25.md').read_text(encoding='utf-8')
old = ('So check your organs (Brown), starting with your pancreas: if it doesn\'t make enough digestive enzymes, called '
       'Exocrine Pancreatic Insufficiency, you\'d test for that with Stool Elastase, and treat it with high-dose enzymes.')
new = ('So check your organs (Brown). Do your stools look oily or greasy? Then your pancreas may not be making enough '
       'digestive enzymes, called Exocrine Pancreatic Insufficiency, and you\'d test for that with Stool Elastase and treat '
       'it with high-dose enzymes.')
assert md.count(old) == 1
md = md.replace(old, new)
CHANGES = [{'old': old, 'new': new, 'kind': 'window',
            'why': 'the organ paragraph alone read AI High twice (#196, #199), the first case the same in both and AI Low in '
                   'both cuts of Phases 3 to 6 (#187, #192): it now opens on a sign the reader can notice, as his Phase 1 '
                   'does, then what it may mean, its name, the test and the treatment',
            'source': 'https://www.healthline.com/health/exocrine-pancreatic-insufficiency/signs-and-symptoms (fatty, pale, '
                      'bulky stools, steatorrhea, a common symptom of severe EPI)'}]
(HERE / 'r26.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'change;', len(md.split()), 'words')
