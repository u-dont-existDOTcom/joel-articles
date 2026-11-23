#!/usr/bin/env python3
"""The Nirvāna post's section-link catalog (../../SECTION-LINKS.json; gate inner-child-2026-11-20g), from his picks as
published on 2026-11-23 at 18:01:47 UTC: every heading with its anchor as the live page has it (read from the page's
heading ids that day, LIVE-ANCHORS-20261123.json), the 13 links his picks added (PLAN.json), and the mentions left
unlinked on purpose with the reason. Also checks section_links.py's slug rule against every live anchor.

  python3 build_catalog.py
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import section_links as sl

plan = json.load(open(os.path.join(HERE, 'PLAN.json'), encoding='utf-8'))
live = json.load(open(os.path.join(HERE, 'LIVE-ANCHORS-20261123.json'), encoding='utf-8'))
heads = [e for e in plan['sections'] if e['heading']]
assert len(heads) == len(live['anchors']) == 58
cat = {'post': {'base': 'https://ibogaqueen.substack.com', 'id': '209400477', 'title': 'What If Everything Is Already Perfect? (v2.2)'},
       'source': 'Built 2026-11-23 by experiments/toc-20261123/build_catalog.py from his contents picks as published at '
                 '18:01:47 UTC: headings and anchors read from the live page, links from PLAN.json (all 13 checked on the '
                 'live page: each lands on a heading)',
       'headings': [], 'links': [], 'unlinked_on_purpose': []}
mismatch = []
for e, a in zip(heads, live['anchors']):
    cat['headings'].append({'id': e['id'], 'level': e['level'], 'text': e['heading'], 'anchor': a})
    if sl.slug(e['heading']) != a:
        mismatch.append((e['heading'], sl.slug(e['heading']), a))
for l in plan['links']:
    cat['links'].append({'in': l['in'], 'text': l['words'], 'target': l['target'], 'href': l['href']})
for u in plan['unlinked']:
    cat['unlinked_on_purpose'].append({'in': u['in'], 'text': u['words'], 'why': u['why']})
json.dump(cat, open(os.path.join(HERE, '..', '..', 'SECTION-LINKS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('SECTION-LINKS.json:', len(cat['headings']), 'headings,', len(cat['links']), 'links,', len(cat['unlinked_on_purpose']), 'left unlinked on purpose')
print('slug rule vs live anchors:', 'all agree' if not mismatch else mismatch)
