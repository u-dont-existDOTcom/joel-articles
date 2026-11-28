#!/usr/bin/env python3
"""make_plan_a1.py - the insertion plan for A1, "Can't Stay With a Feeling?", in the somatic guide (turn of 2026-11-28
09:44 UTC): his version from card A1-TEACH-2 with the three links back (ADDITIONS-31.json), as HTML blocks, before the h1
"Layer 4: Unstick the Memories You Can Actually Point To" with the Brainspotting section's further-reading line before it,
and the title's date moved to today's. Built with the last apply's inline() (../apply-c1127/make_plans.py).
  python3 articles/somatic-therapies/experiments/additions-20261126/apply-c1128/make_plan_a1.py
Writes PLAN-A1.json beside this file."""
import html, importlib.util, json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('mp', HERE.parent / 'apply-c1127' / 'make_plans.py')
mp = importlib.util.module_from_spec(spec); spec.loader.exec_module(mp)
a = {x['id']: x for x in json.loads((HERE.parent / 'ADDITIONS-31.json').read_text(encoding='utf-8'))}['A1']
assert a['draft'] == 31 and a['before_heading'] == 'Layer 4: Unstick the Memories You Can Actually Point To'
blocks = ['<h%d>%s</h%d>' % (a['level'], html.escape(a['heading'], quote=False), a['level'])]
blocks += ['<p>%s</p>' % mp.inline(p) for p in a['paragraphs']]
T = 'Somatic Therapy Modalities Map & Free Intro Sessions! Save $50k! \U0001faf6\U0001f3ff\U0001f486\U0001f3ff‍♀️'
plan = {'post': '201523223',
        'inserts': [{'id': 'A1', 'heading': a['heading'], 'before': [1, a['before_heading']],
                     'after_text': 'Comparative study of EMDR, Brainspotting, and related methods',
                     'html': ''.join(blocks),
                     'texts': [a['heading']] + [re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', p) for p in a['paragraphs']]}],
        'title': {'from': T + '(Nov 27, 2026)', 'to': T + '(Nov 28, 2026)'}}
(HERE / 'PLAN-A1.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(plan['inserts'][0]['texts']), 'blocks;', plan['inserts'][0]['html'][:160])
