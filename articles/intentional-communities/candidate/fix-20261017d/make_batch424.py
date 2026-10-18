"""Batch 424g (2026-10-17 night, Joel's 51 a): section 15 v18 (make_s15_v18.py), v17 without "So which is it? Well, in a way,
it's both.", a cut, so it goes to Pangram whatever the march says (pangram_gate.py, "cut_of"). The changed paragraph with each
neighbor under its heading (it is under 50 words), and the section whole in its own batches' format. March: march-r4 (both
readers); cold read: SENSE-s15d.md. Run from candidate/: python3 fix-20261017d/make_batch424.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')


def own_whole(md):   # make_batch423.py's, copied (importing that script would rebuild its batch)
    out = []
    for blk in [x.strip() for x in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if x.strip()]:
        if SKIP.match(blk):
            continue
        if blk.startswith('[caption]'):
            blk = re.sub(r'^\[caption\]\s*', '', blk)
        out.append(plain(blk.lstrip('#').strip()))
    return '\n\n'.join(out)


def paras(md):
    out, h = [], 0
    for b in [x.strip() for x in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if x.strip()]:
        if b.startswith('#'):
            h += 1
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            out.append((h, plain(b)))
    return out


M = HERE / 'march-r4'
labels = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (M / ('MARCH-labels-%s.txt' % x)).read_text(), re.M)) for x in 'ab']
texts = [t.strip() for t in re.split(r'\n\s*\n', (M / 'march-in.md').read_text(encoding='utf-8')) if t.strip()]
cold_lines = (HERE / 'SENSE-s15d.md').read_text(encoding='utf-8')
PARA = re.compile(r'^\[?P(\d+)\]?:?\s*(.*)$')   # "[P3] OK" or "P3: OK"
lines = [PARA.match(l) for l in cold_lines.splitlines() if PARA.match(l)]
assert len(lines) >= 20, 'the cold read has a line per paragraph'
bad_cold = [m.group(0) for m in lines if not m.group(2).startswith('OK') and 'Double click to interact with video' not in m.group(2)]
cold = 'OK' if not bad_cold else '; '.join(bad_cold)
v17 = (C / 's15' / 'v17.md').read_text(encoding='utf-8')
v18 = (C / 's15' / 'v18.md').read_text(encoding='utf-8')
a, b = paras(v17), paras(v18)
pa, pb = [p for _, p in a], [p for _, p in b]
i = next(n for n, (x, y) in enumerate(zip(pa, pb)) if x != y)
assert pa[i] == texts[0] and pb[i] == texts[1]
rec = {'kind': 'edit', 'was': 'batch 423g: section 15 v17 100% Human', 'march_was': [l['1'] for l in labels],
       'march': [l['2'] for l in labels], 'march_note': 'fix-20261017d/march-r4 (s15-p3-was and s15-p3-new)', 'cold': cold,
       'cold_note': 'fix-20261017d/SENSE-s15d.md (section 15 v18 in the article)', 'grounding': 'OK',
       'grounding_note': 'no claim of mine: a cut; the next sentence says the "both" itself', 'stance': 0,
       'stance_note': 'a recap question out; no position added or taken away', 'missing': [],
       'joel_note': 'Joel, 2026-10-17 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt): 51 a ("make sure it reads well")'}
drafts, gate, parts = {}, {}, ['installed']
if len(pb[i].split()) >= 50:
    drafts['S15v18-p3'] = pb[i]; gate['S15v18-p3'] = dict(rec, cut_of=pa[i]); parts.append('S15v18-p3')
for j in (i - 1, i + 1):
    if 0 <= j < len(pb) and b[j][0] == b[i][0] and min(len(pb[i].split()), len(pb[j].split())) < 50:
        lo, hi = sorted((i, j))
        k = 'S15v18-p3+%s' % ('prev' if j < i else 'next')
        drafts[k] = pb[lo] + '\n\n' + pb[hi]; gate[k] = dict(rec, cut_of=pa[lo] + '\n\n' + pa[hi]); parts.append(k)
drafts['S15v18'] = own_whole(v18)
gate['S15v18'] = {'kind': 'section', 'parts': parts, 'repeats': 0, 'repeats_note': 'a cut of the recap the repeats check flagged '
                  '(REPEATS-s15.md); nothing added'}
for k in drafts:
    gate[k]['words'] = len(drafts[k].split())
    print(k, gate[k]['words'], gate[k]['kind'], gate[k].get('march_was'), gate[k].get('march'), '|', drafts[k][:70].replace('\n', ' / '))
print('cold:', cold)
out = HERE / 'b424'
out.mkdir(exist_ok=True)
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                    str(out / 'GATE.json'), str(out / 'b424.js'), '--name', 'B424', '--lint-article',
                    str(C / 'HUMANIZED-SO-FAR.md')] + list(drafts), capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-1500:])
if r.returncode == 0:
    items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
    (out / 'b424-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
