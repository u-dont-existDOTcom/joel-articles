#!/usr/bin/env python3
"""Turn 109, after reshape_t109b.py: bus-h3 in OWNER-EDITS.json holds Hear the Guard First as it now reads (the second try:
his reply back after the remembering it answers), with a history note. His sentences stay required one by one in bus-p2-joel."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / 'OWNER-EDITS.json'
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
WHEN = 'Turn 109 (his answers of 2026-10-25 14:20 UTC, experiments/t109-answers/JOEL-20261025-1420.md)'
data = json.loads(P.read_text(encoding='utf-8'))
e = next(x for x in data['entries'] if x['id'] == 'bus-h3')
md = re.sub(r'<!--.*?-->', '', ART.read_text(encoding='utf-8'), flags=re.S)
i = md.index('### Hear the Guard First')
j = md.index('\n### ', i + 10)
guard = [p.strip() for p in md[i:j].split('\n\n')[1:] if p.strip()]
assert len(guard) == 7 and guard[2].startswith("That part might say") and "Tell me what you remember" in guard[2]
e['must_contain_exact'] = ['### Hear the Guard First'] + guard
e.setdefault('history', []).append(WHEN + ': reshape_t109b.py, the second try after P3 read 99.8% AI alone: his reply "Tell me what you remember, I\'m listening." and its reason are back after "and that part remembers", which they answer, and P1 is the plain path without them.')
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('bus-h3 updated')
