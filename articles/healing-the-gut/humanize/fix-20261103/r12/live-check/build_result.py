#!/usr/bin/env python3
"""The live post's whole-article check (2026-11-04, Joel's extension on the published post at 22:17 UTC), rebuilt into a
RESULT.json like pangram_feed_read.js's full output, from the page's compact windows (WINDOWS.txt), its fields (META.json)
and the checked text (CHECKED-TEXT.txt). CHECKED-TEXT.txt is ../checks/texts/r12-article.txt without its 11 headings and
the paid-subscriber line, with the post's one line break inside the Parasites item; its SHA-256 is the page's own
(text_sha256), so the windows are cut from the very text the extension read. Also writes LEDGER-RESULTS.json for
pangram_ledger.py results (key gut-r12-live-article, prediction #142)."""
import hashlib, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
meta = json.loads((HERE / 'META.json').read_text(encoding='utf-8'))
text = (HERE / 'CHECKED-TEXT.txt').read_text(encoding='utf-8')
compact = (HERE / 'WINDOWS.txt').read_text(encoding='utf-8').strip()
sha = lambda s: hashlib.sha256(s.encode('utf-8')).hexdigest()
assert sha(text) == meta['text_sha256'], 'the text is not the page\'s'
assert sha(compact) == meta['compact_sha256'], 'the windows are not the page\'s'
assert len(text.encode('utf-16-le')) // 2 == meta['text_chars_js'] == len(text)
LABEL = {'H': 'Human', 'A': 'AI-Generated'}
CONF = {'H': 'High', 'M': 'Medium', 'L': 'Low'}
windows, pos = [], 0
for w in compact.split(';'):
    lab, conf, s, e, n, ai, hum, cal, unc = w.split(',')
    s, e = int(s), int(e)
    assert s == pos
    pos = e
    windows.append({'label': LABEL[lab], 'confidence': CONF[conf], 'ai_likelihood': float(ai), 'word_count': int(n),
                    'start_index': s, 'end_index': e, 'is_humanized': hum == '1', 'calibrated_confidence': float(cal),
                    'uncertainty_highlighting': unc == '1'})
assert pos == len(text)
assert sum(w['word_count'] for w in windows) == meta['windows_word_sum']
assert sum(w['label'].startswith('AI') for w in windows) == meta['windows_ai']
fields = {k: v for k, v in meta.items() if k not in ('text_sha256', 'text_chars_js', 'compact_sha256', 'compact_chars',
                                                       'windows_word_sum', 'windows_ai', 'windows_human', 'labels')}
result = dict(fields, windows=windows, text=text)
(HERE / 'RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
flagged = []
lw = []
for w in windows:
    item = {'label': w['label'], 'confidence': w['confidence'], 'words': w['word_count']}
    if not (w['label'] == 'Human' and w['confidence'] == 'High'):
        item['text'] = text[w['start_index']:w['end_index']].strip()
    lw.append(item)
ledger = {'gut-r12-live-article': {'headline': meta['headline'], 'fraction_ai': meta['fraction_ai'], 'words': meta['word_count'],
                                   'windows': lw, 'utc': '2026-11-04T22:17:14Z', 'link': meta['link']}}
(HERE / 'LEDGER-RESULTS.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
from collections import Counter
print(Counter((w['label'], w['confidence']) for w in windows))
