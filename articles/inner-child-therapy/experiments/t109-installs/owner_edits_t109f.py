#!/usr/bin/env python3
"""Turn 109, after reshape_t109e.py: bus-h3 in OWNER-EDITS.json holds Hear the Guard First as it now reads (the second
try's arrangement, seven paragraphs), with a history note and its paragraph order (applied once; it refuses to run again)."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / 'OWNER-EDITS.json'
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
NOTE = ('Turn 109 (his answers of 2026-10-25 14:20 UTC, experiments/t109-answers/JOEL-20261025-1420.md): reshape_t109e.py, back to '
        'the second try\'s arrangement after four tries, my pick on the review page: his reply and its reason together in P3, the '
        'plain path short in P1.')
data = json.loads(P.read_text(encoding='utf-8'))
e = next(x for x in data['entries'] if x['id'] == 'bus-h3')
assert NOTE not in e.get('history', []), 'already applied'
md = re.sub(r'<!--.*?-->', '', ART.read_text(encoding='utf-8'), flags=re.S)
i = md.index('### Hear the Guard First')
j = md.index('\n### ', i + 10)
guard = [p.strip() for p in md[i:j].split('\n\n')[1:] if p.strip()]
assert len(guard) == 7 and guard[1].startswith('A harder voice') and 'alleviates the instinct' in guard[2]
e['must_contain_exact'] = ['### Hear the Guard First'] + guard
e['order'] = ['Two Common Guarding Patterns', 'Hear the Guard First', 'Whichever protective part showed up', 'A harder voice can seem more fitting',
              'That part might say this will just be one more performance', "That part doesn't have to move out.",
              "If it's been calling all this stupid", "A new roommate doesn't win you over", 'Blaming yourself can be doing a job like that, too.']
e['history'].append(NOTE)
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('bus-h3 refreshed')
