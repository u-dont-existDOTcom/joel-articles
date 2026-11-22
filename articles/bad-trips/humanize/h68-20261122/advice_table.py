"""Join the four advice reads with their sentences and with the original guide.

For each flagged sentence: which questions the reader said yes to, the sentence,
and the closest sentence in his original guide (original.md) with a similarity
score, so each flag can be traced to whose words it is.
Writes advice/TABLE.json; prints a compact view.
"""
import json, re, difflib, pathlib, sys
H = pathlib.Path(__file__).resolve().parent
A = H / 'advice'
ROOT = H.parents[1]
orig = (ROOT / 'original.md').read_text(encoding='utf-8')
guide = (ROOT / 'GUIDE-SO-FAR.md').read_text(encoding='utf-8')

def sents(t):
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    out = []
    for line in t.split('\n'):
        line = line.strip().lstrip('-*0123456789. ').strip()
        if not line:
            continue
        out += [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"(])', line) if s.strip()]
    return out
OS = sents(orig)
def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower())
ON = [norm(s) for s in OS]
def closest(s):
    n = norm(s); best = (0, '')
    for o, on in zip(OS, ON):
        if abs(len(on) - len(n)) > max(60, len(n)):
            continue
        r = difflib.SequenceMatcher(None, n, on).ratio()
        if r > best[0]:
            best = (r, o)
    return best
Q = ['ANYWAY', "CAN'T TELL", 'FROM', 'RIGHT', 'MISREAD']
rows = []
for part in ['outside-help', 'brain-seizure', 'mdma-chest-swallowed', 'serotonin']:
    text = {}
    for line in (A / f'text-{part}.txt').read_text(encoding='utf-8').split('\n'):
        m = re.match(r'S(\d+): (.*)', line)
        if m:
            text[int(m.group(1))] = m.group(2)
    for line in (A / f'read-{part}.txt').read_text(encoding='utf-8').split('\n'):
        m = re.match(r'- S(\d+): (.*)', line)
        if not m:
            continue
        k = int(m.group(1)); body = m.group(2)
        parts = [p.strip() for p in body.split(' / ')]
        flags = {}
        for p in parts:
            for q in Q:
                if p.startswith(q + ' '):
                    v = p[len(q) + 1:].strip()
                    if v != '-':
                        flags[q] = v
        s = text.get(k, '')
        r, o = closest(s)
        rows.append({'part': part, 'S': k, 'sentence': s, 'flags': flags,
                     'orig_ratio': round(r, 2), 'orig': o,
                     'in_guide': norm(s)[:60] in norm(guide)})
(A / 'TABLE.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding='utf-8')
if __name__ == '__main__':
    for r in rows:
        print('%s S%d [%s] orig=%.2f guide=%s\n   %s' % (r['part'][:8], r['S'], ','.join(q[:3] for q in r['flags']), r['orig_ratio'], 'y' if r['in_guide'] else 'n', r['sentence'][:150]))
