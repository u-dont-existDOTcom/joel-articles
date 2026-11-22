"""Find advice the guide says more than once (Joel, round 49: "make sure we are
not repeating the same stuff over and over").

Sentence pairs in different blocks whose content words overlap a lot, and
remedy mentions (with amounts) spread across sections. Writes REPEATS.json.
"""
import json, re, pathlib, itertools, difflib
H = pathlib.Path(__file__).resolve().parent
ROOT = H.parents[1]
blocks = json.load(open(ROOT / 'GUIDE-SO-FAR-blocks.json', encoding='utf-8'))
STOP = set('''a an the and or but if so of to in on at for with by from as is are was were be been being it its this that
these those they them their there then than i i'd i'm you your we our he she his her not no do does did done can could
would should will may might must just also even more most less very much many some any each one two all only like into out
up down over under again once while when what which who how why where about after before because until other such own same
too s t don't it's that's they're you're isn't doesn't wouldn't won't can't'''.split())
def words(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    return [w for w in re.findall(r"[a-z][a-z'-]+", s.lower()) if w not in STOP and len(w) > 2]
sec = ''
sents = []
for b in blocks:
    md = b.get('md') or ''
    if b['kind'] in ('h1', 'h2', 'h3', 'h4') or md.startswith('#'):
        sec = md.lstrip('#').strip()
        continue
    if b['kind'] in ('image', 'hr'):
        continue
    for line in md.split('\n'):
        line = re.sub(r'^\s*(\d+\.|[-*])\s+', '', line).strip()
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"(*])', line):
            if len(words(s)) >= 5:
                sents.append({'id': b['id'], 'sec': sec, 's': s.strip(), 'w': set(words(s))})
pairs = []
for a, c in itertools.combinations(sents, 2):
    if a['id'] == c['id']:
        continue
    inter = a['w'] & c['w']
    j = len(inter) / len(a['w'] | c['w'])
    r = difflib.SequenceMatcher(None, a['s'].lower(), c['s'].lower()).ratio()
    if (j >= 0.42 and len(inter) >= 5) or r >= 0.72:
        pairs.append({'j': round(j, 2), 'r': round(r, 2), 'a': [a['id'], a['sec'], a['s']], 'b': [c['id'], c['sec'], c['s']], 'shared': sorted(inter)})
pairs.sort(key=lambda p: -(p['j'] + p['r']))
# remedy mentions by section
REM = {'magnesium chloride': r'magnesium chloride|mgcl', 'electrolyte drink': r'electrolyte', 'DMSO': r'\bDMSO\b', 'cyproheptadine': r'cyproheptadine', 'cool / ice / cold bath': r'\bice\b|cold bath|cool(ing)? them|somewhere cool', 'poison control': r'poison control', 'niacin': r'niacin', 'humic': r'humic', 'Ipomoea': r'Ipomoea', 'activated charcoal': r'charcoal', 'recovery position / on their side': r'recovery position|on their side'}
spread = {}
sec = ''
for b in blocks:
    md = b.get('md') or ''
    if md.startswith('#'):
        sec = md.lstrip('#').strip(); continue
    for k, p in REM.items():
        n = len(re.findall(p, md, re.I))
        if n:
            spread.setdefault(k, {}).setdefault(sec, 0)
            spread[k][sec] += n
out = {'pairs': pairs, 'spread': spread}
(H / 'REPEATS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding='utf-8')
if __name__ == '__main__':
    print(len(sents), 'sentences;', len(pairs), 'close pairs')
    for p in pairs[:45]:
        print('\nj=%.2f r=%.2f  %s [%s]\n   A: %s\n   B: %s [%s] %s' % (p['j'], p['r'], p['a'][0], p['a'][1][:40], p['a'][2][:230], p['b'][0], p['b'][1][:40], p['b'][2][:230]))
    print()
    for k, v in spread.items():
        print(k, '->', v)
