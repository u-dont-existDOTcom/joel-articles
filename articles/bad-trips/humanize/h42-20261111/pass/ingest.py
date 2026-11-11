#!/usr/bin/env python3
"""ingest.py - the h42a batch's results, read from Pangram's history as labels and character indexes
(RESULTS-h42a-idx.json, from the page's __readI), turned into the ledger's compact form (RESULTS-h42a.json) with each
window's words cut from the unit's own text, the way Pangram indexes it (blank lines counted as one newline). Each
window's words are checked against the first characters Pangram gives for it.

  python3 ingest.py
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
I = json.loads((HERE / 'RESULTS-h42a-idx.json').read_text(encoding='utf-8'))
out, bad = {}, 0
for k, (head, ai, words, uuid, ts, wins) in sorted(I.items()):
    text = (HERE / 'units' / (k + '.txt')).read_text(encoding='utf-8').rstrip('\n')
    n = re.sub(r'\n{2,}', '\n', text)
    flagged, below = [], []
    for label, conf, wc, a, b, head24 in wins:
        s = n[a:b].strip()
        if head24 and not s.startswith(head24[:20]):
            bad += 1
            print('%s: window at %d does not start with %r (got %r)' % (k, a, head24, s[:24]))
        if label != 'Human':
            flagged.append('%s (%d words): %s' % (label, wc, s))
        elif conf != 'High':
            below.append('Human %s (%d words): %s' % (conf, wc, s))
    out[k] = [head, ai, words, '; '.join('%s, %s, %d' % (l, c, w) for l, c, w, *_ in wins), ts[11:19], '/' + uuid, flagged, below]
(HERE / 'RESULTS-h42a.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(out), 'results;', bad, 'windows whose words did not match')
