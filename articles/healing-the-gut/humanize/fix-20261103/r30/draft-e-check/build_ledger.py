#!/usr/bin/env python3
"""Draft E's whole-article check (his extension, 2026-11-07 01:11 UTC, the link he sent at 01:11 UTC), from RESULT.json
(substack_check_text.py result, which matched the page's SHA-256 to EXPECTED-TEXT-E.txt): writes LEDGER-RESULTS.json for
pangram_ledger.py results, key gut-r30-article (prediction #208), every window with its text so gate E354 can see what it
read (gut-2026-11-06c), and CONFIDENCE.md, the windows by confidence beside draft B's."""
import json, pathlib
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
r = json.loads((HERE / 'RESULT.json').read_text(encoding='utf-8'))
text = r['text']
lw = [{'label': w['label'], 'confidence': w['confidence'], 'words': w['word_count'],
       'calibrated': round(w['calibrated_confidence'], 4), 'text': text[w['start_index']:w['end_index']].strip()}
      for w in r['windows']]
ledger = {'gut-r30-article': {'headline': r['headline'], 'fraction_ai': r['fraction_ai'], 'words': r['word_count'],
                              'windows': lw, 'utc': '2026-11-07T01:11:49Z', 'link': r['link']}}
(HERE / 'LEDGER-RESULTS.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
c = Counter((w['label'], w['confidence']) for w in lw)
rows = ['| %s | %s | %d | %s |' % (w['label'], w['confidence'], w['words'],
                                    (w['text'][:90] + ' …') if len(w['text']) > 90 else w['text']) for w in lw]
md = ['# Draft E, the whole article (r30), read by his extension', '',
      '[Human Written](%s), %.0e AI, document confidence High; %d windows: %s. Draft B (r17) had 9 High, 8 Medium and 4 '
      'Low windows ([#183](https://www.pangram.com/feed/bb64a934-cf2c-47b3-ae93-af2a363a0644)).'
      % (r['link'], r['fraction_ai'], len(lw), ', '.join('%d %s %s' % (n, k[0], k[1]) for k, n in sorted(c.items()))), '',
      '| label | confidence | words | text |', '|---|---|---|---|'] + rows
(HERE / 'CONFIDENCE.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(c)
for w in lw:
    if w['confidence'] != 'High':
        print(w['confidence'], w['words'], repr(w['text']))
