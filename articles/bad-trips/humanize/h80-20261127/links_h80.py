"""links_h80.py - the guide's same-post links put back in step with their catalog (turn 72), from the repo root:

  python3 articles/bad-trips/humanize/h80-20261127/links_h80.py

- B154's "activated charcoal" link (#§activated-charcoal) went missing in turn 71, when his ferments answer replaced the
  paragraph's text (apply_h79.py took it from TEST-a3-b154.txt, which was written without links): put back on the same
  words, no word changed.
- Turn 70's four links (B141 twice, R59-GUT-DO, R59-GUT-COMMON) were in the guide but never catalogued: added to
  SECTION-LINKS.json, so a heading's rename finds them.
"""
import json
import pathlib
import re

ART = pathlib.Path(__file__).resolve().parents[2]
blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
by = {x['id']: x for x in blocks}
old = 'which then requires activated charcoal to reduce gut histamine.'
if old in by['B154']['md']:
    by['B154']['md'] = by['B154']['md'].replace(old, 'which then requires [activated charcoal](#§activated-charcoal) to reduce gut histamine.')
(ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
(ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

c = ART / 'SECTION-LINKS.json'
cat = json.loads(c.read_text(encoding='utf-8'))
have = {(x['block'], x['text'], x['href']) for x in cat['links']}
heading = None
for b in blocks:
    if b['md'].startswith('#'):
        heading = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', b['md'].lstrip('#').strip())
        continue
    for t, h in re.findall(r'\[([^\]]+)\]\((#§[^)]+)\)', b['md']):
        t = t.replace('*', '')
        if (b['id'], t, h) not in have:
            cat['links'].append({'in': heading, 'block': b['id'], 'text': t, 'href': h})
            have.add((b['id'], t, h))
            print('catalogued:', b['id'], t, h, 'in', heading)
c.write_text(json.dumps(cat, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(cat['links']), 'links in the catalog')
