"""Batch 422g (2026-10-17 night, Joel's 48 a and 51 a of 21:37 UTC): make_tighten.py's changes in sections 13 (v36), 15 (v16)
and 16 (v31). Each changed paragraph alone (50 words or more) and with each neighbor under its heading when one of the two is
under 50, and each section whole in the format its last check used (section 13: ptext's section(); 15 and 16: their own
batches' format). The edit records need the march (march-r1/MARCH-labels-a.txt and -b.txt), the tone check (TONE-tighten.md),
the cold reads (cold.json: SENSE-s13.md, SENSE-s15.md) and 421g's results for sections 15 and 16 (their installed versions).
Run from candidate/: python3 fix-20261017d/make_batch422.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
sys.path.insert(0, str(HERE))
from ptext import plain, section  # noqa: E402
from make_tighten import CHANGES, SRC  # noqa: E402


def own_whole(md):
    """Sections 15 and 16 as their own batches read them (make_batch421.py's own_whole, without importing that script)."""
    out = []
    for blk in [x.strip() for x in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if x.strip()]:
        if re.match(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)', blk):
            continue
        if blk.startswith('[caption]'):
            blk = re.sub(r'^\[caption\]\s*', '', blk)
        out.append(plain(blk.lstrip('#').strip()))
    return '\n\n'.join(out)


JOEL = 'Joel, 2026-10-17 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt): '
NEW = (HERE / 'article-with-tighten.md').read_text(encoding='utf-8')
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')
HEAD = {'s13': '# Your Little Forming Group Already Is the Community', 's15': '# What This Looks Like From Sénégal',
        's16': '# Practice Comes Before Property'}
KEYV = {'s13': 'S13v36', 's15': 'S15v16', 's16': 'S16v31'}
WAS = {'s13': 'batch 420g: section 13 v35 100% Human', 's15': 'batch 421g: section 15 v15 100% Human',
       's16': 'batch 421g: section 16 v30 100% Human'}


def labels(folder):
    if not (folder / 'MARCH-labels-a.txt').exists():
        return None
    ids = json.loads((folder / 'march-ids.json').read_text())
    L = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (folder / ('MARCH-labels-%s.txt' % x)).read_text(), re.M)) for x in 'ab']
    return {k: [m[str(i + 1)] for m in L] for i, k in enumerate(ids)}


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]


def paras(md):
    out, h = [], 0
    for b in blocks(md):
        if b.startswith('#'):
            h += 1
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            out.append((h, plain(b), b))
    return out


# each round's labels, by the exact plain text read: a changed paragraph takes the reading of its final text (the latest round that
# read it), and the reading of its installed text from the same round
ROUNDS = {}
for rnd in ('march-r1', 'march-r2', 'march-r3'):
    f = HERE / rnd
    lab = labels(f)
    if lab is None:
        continue
    texts = [t.strip() for t in re.split(r'\n\s*\n', (f / 'march-in.md').read_text(encoding='utf-8')) if t.strip()]
    ids = json.loads((f / 'march-ids.json').read_text())
    assert len(texts) == len(ids), rnd
    ROUNDS[rnd] = {ids[i]: (texts[i], lab[ids[i]]) for i in range(len(ids))}


def march_for(was, new):
    """(march_was, march, note) from the latest round whose '-new' text is NEW, or None."""
    for rnd in ('march-r3', 'march-r2', 'march-r1'):
        for mid, (t, lab) in ROUNDS.get(rnd, {}).items():
            if mid.endswith('-new') and t == new:
                w = ROUNDS[rnd][mid[:-4] + '-was']
                assert w[0] == was, (rnd, mid)
                return w[1], lab, 'fix-20261017d/%s (%s and %s)' % (rnd, mid[:-4] + '-was', mid)
    return None


COLD = json.loads((HERE / 'cold.json').read_text()) if (HERE / 'cold.json').exists() else {}
drafts, gate = {}, {}
n = 0
for s, (src, dst) in SRC.items():
    a, b = blocks(src.read_text(encoding='utf-8')), blocks(dst.read_text(encoding='utf-8'))
    hp = paras(dst.read_text(encoding='utf-8'))
    ps = [p for _, p, _ in hp]
    for x, y in zip(a, b):
        if x == y:
            continue
        n += 1
        mid = '%s-c%d' % (s, n)
        whys = [w for sec, where, kind, old, new, w in CHANGES if sec == s and (new and new in y or old in x)]
        rec = {'kind': 'edit', 'was': WAS[s], 'grounding': 'OK',
               'grounding_note': 'no claim of mine: ' + '; '.join(whys) + ' (fix-20261017d/tighten-changes.json)',
               'stance': 0, 'stance_note': 'padding, a question-answer pair or capitals out, or a published anchor back; no position added',
               'missing': [], 'joel_note': JOEL + '48 a and 51 a ("make sure it reads well")'}
        m = march_for(plain(x), plain(y))
        if m:
            rec.update(march_was=m[0], march=m[1], march_note=m[2])
        if s in COLD:
            rec.update(cold=COLD[s][0], cold_note=COLD[s][1])
        i = next(k for k, (_, p, _) in enumerate(hp) if p == plain(y))
        key = '%s-c%d' % (KEYV[s], n)
        if len(ps[i].split()) >= 50:
            drafts[key] = ps[i]; gate[key] = dict(rec)
        for j in (i - 1, i + 1):
            if 0 <= j < len(ps) and hp[j][0] == hp[i][0] and min(len(ps[i].split()), len(ps[j].split())) < 50:
                lo, hi = sorted((i, j))
                k = '%s+%s' % (key, 'prev' if j < i else 'next')
                drafts[k] = ps[lo] + '\n\n' + ps[hi]; gate[k] = dict(rec)
drafts['S13v36'] = section(NEW, HEAD['s13'])
drafts['S15v16'] = own_whole((C / 's15' / 'v16.md').read_text(encoding='utf-8'))
drafts['S16v31'] = own_whole((C / 's16' / 'v31.md').read_text(encoding='utf-8'))
for s in ('s13', 's15', 's16'):
    k = KEYV[s]
    gate[k] = {'kind': 'section', 'parts': ['installed'] + sorted(x for x in gate if x.startswith(k + '-')), 'repeats': 0,
               'repeats_note': 'nothing added: padding, question-answer pairs and capitals out, the published bottlenecks anchor back '
                               '(fix-20261017d/tighten-changes.json)'}
for k in gate:
    gate[k]['words'] = len(drafts[k].split())
seen, aliases = {}, {}
for k in list(drafts):
    if drafts[k] in seen:
        aliases[k] = seen[drafts[k]]; del drafts[k]
    else:
        seen[drafts[k]] = k
for k in drafts:
    print(k, gate[k]['words'], gate[k]['kind'], '|', drafts[k][:70].replace('\n', ' / '))
print('aliases:', aliases)
print(len(drafts), 'items,', sum(gate[k]['words'] for k in drafts), 'words')
if all('march' in gate[k] for k in gate if gate[k]['kind'] == 'edit') and all(s in COLD for s in ('s13', 's15', 's16')):
    out = HERE / 'b422'
    out.mkdir(exist_ok=True)
    (out / 'aliases.json').write_text(json.dumps(aliases, indent=1) + '\n', encoding='utf-8')
    (out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                        str(out / 'GATE.json'), str(out / 'b422.js'), '--name', 'B422', '--lint-article',
                        str(C / 'HUMANIZED-SO-FAR.md')] + list(drafts), capture_output=True, text=True)
    print(r.stdout[-2000:], r.stderr[-2500:])
    items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
    (out / 'b422-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
else:
    print('waiting for: march', [k for k in gate if gate[k]['kind'] == 'edit' and 'march' not in gate[k]], 'cold',
          [s for s in ('s13', 's15', 's16') if s not in COLD])
