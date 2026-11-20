#!/usr/bin/env python3
"""Turn 133: the inner child post's first SECTION-LINKS.json, from what turn 132 put in the post (17:06 UTC).

  python3 build_catalog.py        # writes ../../SECTION-LINKS.json

Headings: turn 132's final list (publish/probe132.js, the "h" rows: id, old level, old heading, level, heading), which the
first account checked on the rendered page. Links: the 22 it added (publish/PLAN.json). The post's one older section
link and his changes after 17:06 UTC aren't in this build: read them from the post, then apply each heading change with
section_links.py rename, so every link to it is listed."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
T132 = HERE.parent / 't132-toc-links'
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
import section_links as sl  # noqa: E402

js = (T132 / 'publish' / 'probe132.js').read_text(encoding='utf-8')
data = json.loads(re.search(r'const c = (\{.*?\});\n', js, re.S).group(1))
plan = json.loads((T132 / 'publish' / 'PLAN.json').read_text(encoding='utf-8'))
BASE, POST = 'https://ibogaqueen.substack.com', '189761959'

headings = [{'id': i, 'level': lev, 'text': text, 'anchor': sl.slug(text)}
            for i, _old_lev, _old, lev, text in data['h'] if text]
links = [{'in': ln['in'], 'text': ln['text'], 'target': ln['target'], 'href': ln['href']} for ln in plan['links']]
cat = {'post': {'base': BASE, 'id': POST, 'title': "Joel's inner child guide"},
       'source': ('Built 2026-11-20 by experiments/t133-links/build_catalog.py from turn 132 as published at 17:06 UTC: its '
                  'headings (publish/probe132.js) and the 22 section links it added (publish/PLAN.json). Not yet in it: the '
                  "one section link the post had before turn 132, and Joel's changes after 17:06 UTC other than those "
                  'applied below with section_links.py rename.'),
       'headings': headings, 'links': links,
       'unlinked_on_purpose': [{'in': 'S013', 'text': 'Compassion Exit?', 'would_point_to': 'S084x',
                                'why': ('Claude declined to link the crisis paragraph to this section (turn 132); Joel kept '
                                        'the mention and can add the link himself.')}]}
out = HERE.parents[1] / 'SECTION-LINKS.json'
out.write_text(json.dumps(cat, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('%d headings, %d links -> %s' % (len(headings), len(links), out))
