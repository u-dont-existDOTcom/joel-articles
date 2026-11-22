#!/usr/bin/env python3
"""ingest.py - this folder's Pangram results, read from the History by the page's __readI (RESULTS-<batch>-idx.json),
turned into the ledger's compact form (RESULTS-<batch>.json) with each window's words cut from the test's own text, the
way Pangram indexes it (blank lines counted as one newline), each checked against the first characters Pangram gives.

  python3 ingest.py BATCH      e.g. h43a
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent


FILES = {'ss-r1-fix2': 'TEST-ss-r1-fix2.txt', 'acute-r1-fix2': 'TEST-acute-r1-fix2.txt'}


def test_file(key):
    if key in FILES:
        return HERE / FILES[key]
    if '-fix' not in key:
        return HERE / ('TEST-%s.txt' % key)
    base, fix = key.rsplit('-fix', 1)
    return HERE / ('TEST-%s.txt' % base if fix == '1' else 'TEST-%s-fix%s.txt' % (base, fix))


batch = sys.argv[1]
I = json.loads((HERE / ('RESULTS-%s-idx.json' % batch)).read_text(encoding='utf-8'))
out, bad = {}, 0
for k, (head, ai, words, uuid, ts, wins) in sorted(I.items()):
    text = test_file(k).read_text(encoding='utf-8').rstrip('\n')
    n = re.sub(r'\n{2,}', '\n', text)
    flagged, below = [], []
    for label, conf, wc, a, b, head24 in wins:
        s = n[a:b].strip()
        if head24 and not s.startswith(head24[:20]):
            bad += 1
            print('%s: window at %d does not start with %r (got %r)' % (k, a, head24, s[:24]))
        if label != 'Human':
            flagged.append('%s %s (%d words): %s' % (label, conf, wc, s))
        elif conf != 'High':
            below.append('Human %s (%d words): %s' % (conf, wc, s))
    out[k] = [head, ai, words, '; '.join('%s, %s, %d' % (l, c, w) for l, c, w, *_ in wins), ts[11:19], '/' + uuid, flagged, below]
(HERE / ('RESULTS-%s.json' % batch)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(out), 'results;', bad, 'windows whose words did not match')
for k, r in out.items():
    print(k, r[0], r[1], r[3], 'https://www.pangram.com/history' + r[5])
    for f in r[6] + r[7]:
        print('   ', f[:200])
