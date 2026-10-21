"""fill_preds.py RESULTS.json PREDICTIONS.md - put each Pangram result (from the in-page reader, pangram_page_helpers.js's
__readC, compact form [headline, ai, words, windows, utc hh:mm:ss, link tail, flagged], or pangram_gate.py's reader's record per
key) into the PREDICTIONS table's empty
Pangram column, and print how many calls were right (2026-10-18: a scratch script of the community lane until then).

The table is "| text | mine | why | |" or "| text | mine | chance | why | |" (the chance, my chance of a 100% Human result,
stays where it is); a row is filled only when its last cell is empty and its key is in RESULTS.json. A result is Human
when Pangram's headline starts with "Human", AI when every window is AI, and Mixed otherwise.
"""
import json, re, sys
res = json.load(open(sys.argv[1], encoding='utf-8'))
p = sys.argv[2]
s = open(p, encoding='utf-8').read()
right = total = 0
def call(h, windows):
    if h.startswith('Human'):
        return 'Human'
    ws = [w.split(',')[0] for w in windows.split('; ')]
    if all(w.startswith('AI') for w in ws):
        return 'AI'
    return 'Mixed'
out = []
for line in s.split('\n'):
    m = re.match(r'\| (\S+) \| (Human|AI|Mixed) \| (.*) \| *\|$', line)
    if m and m.group(1) in res:
        k, mine, why = m.groups()
        r = res[k]
        if isinstance(r, dict):   # the gate's reader (pangram_gate.py's OUT-read.js) gives a record per key (2026-10-21)
            r = [r['headline'], r.get('avg_ai_likelihood') or 0, r['words'], '; '.join(r['windows']), r['utc'][11:19],
                 r['link'].split('/history', 1)[1], '; '.join(r.get('flagged', []))]
        h, ai, words, windows, t, tail, flagged = r
        got = call(h, windows)
        conf = windows.split(', ')[1] if len(windows.split('; ')) == 1 else None
        desc = '%s (%s%s, %s words, AI likelihood %.2f)' % (
            got, h, (', ' + conf.lower()) if conf else '; windows: ' + windows, words, ai)
        total += 1
        right += (mine == got)
        line = '| %s | %s | %s | **%s**, %s, [check](https://www.pangram.com/history%s) |' % (k, mine, why, desc.split(' (')[0], t, tail)
        line = line.replace('**%s**,' % got, '**%s** (%s),' % (got, desc.split(' (', 1)[1][:-1]))
    out.append(line)
open(p, 'w', encoding='utf-8').write('\n'.join(out))
print('predictions right: %d of %d' % (right, total))
