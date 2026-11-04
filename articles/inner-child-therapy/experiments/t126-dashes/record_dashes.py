#!/usr/bin/env python3
"""Turn 126: the guide's nine dashes made his two hyphens by the new standard swap (tools/humanization/typography_swap.py,
E353 (Inner Child); his answer of 2026-11-04 16:30 UTC, experiments/t126-answers/JOEL-20261104-1630.md). The swap itself was
run on HUMANIZED-ARTICLE-SO-FAR.md (`typography_swap.py FILE --write`: 9 characters); this records each change (DASHES.json,
from the copy of the article just before it) and adds OWNER-EDITS.json joel-126-dashes, which keeps the article free of an
em dash or a spaced en dash.
  python3 articles/inner-child-therapy/experiments/t126-dashes/record_dashes.py BEFORE.md"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART_DIR = HERE.parents[1]
before = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
after = (ART_DIR / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
from typography_swap import swap_text  # noqa: E402
assert swap_text(before)[0] == after, 'the article changed in more than the swap'
changes = []
for m in re.finditer(r'[  ]*[–—][  ]*', before):
    a, b = before[max(0, m.start() - 40):m.start()], before[m.end():m.end() + 25]
    changes.append({'before': a + m.group(0) + b, 'after': a + '--' + b})
(HERE / 'DASHES.json').write_text(json.dumps({'answer': 'experiments/t126-answers/JOEL-20261104-1630.md', 'changes': changes},
                                             ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
led = json.loads((ART_DIR / 'OWNER-EDITS.json').read_text(encoding='utf-8'))
assert 'joel-126-dashes' not in {e['id'] for e in led['entries']}
led['entries'].append({
    'id': 'joel-126-dashes', 'status': 'applied',
    'what': ('His two hyphens, "--", with no spaces, for each of the guide\'s nine dashes (seven em dashes in his ODT that the '
             'standard swap had made spaced en dashes, and two spaced en dashes he typed), by the standard swap as it is now '
             '(tools/humanization/typography_swap.py, E353 (Inner Child)).'),
    'joel': ('2026-11-04 16:04 UTC, on card SR-11 of the sense-read marking page: "no everything should be the 2 dashes not '
             'em-dash, em-dash is ai"; 16:30 UTC, asked whether that meant all nine and the swap for every article: "1 yes to '
             'both" (experiments/t126-answers/JOEL-20261104-1630.md)'),
    'where': 'The Chicken-and-Egg Problem, P1; Five Stages of Reparenting (stages 2 to 5); and three more paragraphs',
    'must_contain': ['On ne change pas--"we don\'t change."', 'Begin to borrow adulthood--remember', 'bigger--perhaps much bigger--than'],
    'must_not_contain': [' – ', '—']})
(ART_DIR / 'OWNER-EDITS.json').write_text(json.dumps(led, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(changes), 'dashes recorded; joel-126-dashes added')
