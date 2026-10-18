"""Batch 418g (2026-10-17 evening): section 16, one change at a time. 417g read section 16 AI (0.39) with its exclamations put
back, in the same two windows as 415g, so those windows weren't the periods: the first runs from "It would be better to get
together" to "a common purse" (installed text both sides of it), the second holds "It can still change how people survive",
and that sentence also read AI with the installed paragraph before it, "That's it!" and all (0.87). So "That's it!" wasn't
what 415g's 0.88 was about either. This batch reads section 16 as installed (v28, 413g 100% Human) with each remaining change
added on its own and together, and the "That's it!" cut with the installed next paragraph.
Run from candidate/: python3 fix-20261017b/make_batch418.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')


def own_whole(md):
    out = []
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if SKIP.match(b):
            continue
        if b.startswith('[caption]'):
            b = re.sub(r'^\[caption\]\s*', '', b)
        out.append(plain(b.lstrip('#').strip()))
    return '\n\n'.join(out)


v28 = (C / 's16' / 'v28.md').read_text(encoding='utf-8')
assert own_whole(v28) == json.loads((C / 'fix-20261017' / 'b413' / 'drafts.json').read_text())['S16v28']
DECL = ('rather than because "money is impure!"', 'rather than by declaring "money is impure!"')
MARKS = [('Or a sauna!', 'Or a sauna.'), ('And practice before you have an audience!', 'And practice before you have an audience.')]
CUT = (" That's it!", '')


def apply(md, changes):
    for old, new in changes:
        assert md.count(old) == 1, old
        md = md.replace(old, new)
    return md


V = {'S16-a': [DECL], 'S16-b': MARKS, 'S16-c': [DECL] + MARKS, 'S16-d': [DECL] + MARKS + [CUT]}
drafts, gate = {}, {}
G415 = json.loads((HERE / 'b415' / 'GATE.json').read_text(encoding='utf-8'))
G417 = json.loads((HERE / 'b417' / 'GATE.json').read_text(encoding='utf-8'))
parts = {'S16-a': ['S16v29b-H1P3', 'S16v29b-H1P3+prev'], 'S16-b': ['S16v29-H2P5', 'S16v29-H2P5+next', 'S16v29-H3P1+next'],
         'S16-c': ['S16v29b-H1P3', 'S16v29b-H1P3+prev', 'S16v29-H2P5', 'S16v29-H2P5+next', 'S16v29-H3P1+next'],
         'S16-d': ['S16v29b-H1P3', 'S16v29b-H1P3+prev', 'S16v29-H2P5', 'S16v29-H2P5+next', 'S16v29-H3P1+next',
                   'S16v29-H2P3+prev', 'S16-d-H2P3+next']}
for k, ch in V.items():
    md = apply(v28, ch)
    (HERE / 'b418').mkdir(exist_ok=True)
    (HERE / 'b418' / ('%s.md' % k)).write_text(md, encoding='utf-8')
    drafts[k] = own_whole(md)
    gate[k] = {'kind': 'section', 'parts': ['installed'] + parts[k], 'repeats': 0,
               'repeats_note': 'fix-20261017b/DISPOSITIONS.md', 'words': len(drafts[k].split())}
# the cut with the installed next paragraph
md = apply(v28, [CUT])
ps = [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]
i = next(n for n, b in enumerate(ps) if b.startswith('So your inner pl/ork'))
drafts['S16-d-H2P3+next'] = plain(ps[i]) + '\n\n' + plain(ps[i + 1])
gate['S16-d-H2P3+next'] = dict(G415['S16v29-H2P3+prev'], words=len(drafts['S16-d-H2P3+next'].split()))
for k in ('S16v29-H2P5', 'S16v29-H2P5+next', 'S16v29-H3P1+next', 'S16v29-H2P3+prev'):
    gate[k] = G415[k]
for k in ('S16v29b-H1P3', 'S16v29b-H1P3+prev'):
    gate[k] = G417[k]
out = HERE / 'b418'
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                    str(out / 'GATE.json'), str(out / 'b418.js'), '--name', 'B418'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(out / 'b418-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
for k in drafts:
    print(k, len(drafts[k].split()), gate[k]['kind'])
