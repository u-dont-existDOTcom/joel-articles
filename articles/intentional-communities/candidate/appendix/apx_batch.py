"""apx_batch.py - a screening batch (E175) of appendix drafts, the way batch 331g's builder (b331/make_batch.py) made one,
for any number of drafts at once (2026-10-17).

Each entry is screened alone when it has 50 words, with its neighbor when two under one heading reach 50, and otherwise in
the shortest run around it that Pangram can read (tools/humanization/paragraphs_alone.py, minimal_runs; the fewest runs that
cover every entry); each draft also goes whole. A text already screened in an earlier appendix batch (its drafts.json) is
left out: paragraphs_alone.py matches results by exact text across batches. The march is read per item, one paragraph per
item (its entries run together, no headings), and an item takes the readings of its exact text from any review round
(appendix/review-r*/).
Usage (from candidate/):
  python3 appendix/apx_batch.py NNN V [V ...] --march review-rK   writes the march prompt for the texts with no readings
  python3 appendix/apx_batch.py NNN V [V ...]                     writes appendix/bNNN/ (drafts, gate, the in-page batch)"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

APX = pathlib.Path(__file__).resolve().parent
C = APX.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from ptext import plain  # noqa: E402
import paragraphs_alone as PA  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith('--')]
NNN, VERSIONS = args[0], [a for a in args[1:] if a not in (sys.argv[sys.argv.index('--march') + 1:sys.argv.index('--march') + 2]
                                                               if '--march' in sys.argv else [])]
MARCH_ROUND = sys.argv[sys.argv.index('--march') + 1] if '--march' in sys.argv else None


def plan(V):
    md = (APX / (V + '.md')).read_text(encoding='utf-8')
    paras = PA.paragraphs(md)
    n = len(paras)
    need, runs = {}, {}
    for i, (head, p) in enumerate(paras):
        t = plain(p)
        if len(t.split()) >= 50:
            need[i] = 'alone'
            continue
        same = lambda j: 0 <= j < n and paras[j][0] == head
        pairs = [(i - 1, i)] * same(i - 1) + [(i, i + 1)] * same(i + 1)
        ok = [x for x in pairs if len((plain(paras[x[0]][1]) + ' ' + plain(paras[x[1]][1])).split()) >= 50]
        if ok:
            need[i] = ok[0]
            continue
        need[i] = 'run'
        for a, b, text, _ in PA.minimal_runs(md, i):
            runs.setdefault((a, b), {'text': text, 'for': set()})['for'].add(i)
    left = {i for i, k in need.items() if k == 'run'}
    chosen = []
    while left:
        best = max(runs.items(), key=lambda kv: (len(kv[1]['for'] & left), -len(kv[1]['text'].split()), -kv[0][0]))
        chosen.append(best[0])
        left -= best[1]['for']
    items = {}  # key -> (text, march text, markdown for the linter)
    span = lambda a, b: ('\n\n'.join(plain(paras[j][1]) for j in range(a, b + 1)),
                         ' '.join(paras[j][1] for j in range(a, b + 1)), '\n\n'.join(paras[j][1] for j in range(a, b + 1)))
    for a, b in sorted(chosen):
        items['APX%s-E%02d-%02d' % (V, a + 1, b + 1)] = (runs[(a, b)]['text'],) + span(a, b)[1:]
    for i, k in need.items():
        if k == 'alone':
            items['APX%s-E%02d' % (V, i + 1)] = span(i, i)
        elif isinstance(k, tuple):
            items['APX%s-E%02d-%02d' % (V, k[0] + 1, k[1] + 1)] = span(*k)
    blocks = PA.reader_blocks(md)
    whole = '\n\n'.join(plain(x.lstrip('#').strip()) if k == 'h' else plain(x) for k, x in blocks)
    items['APX' + V] = (whole, None, '\n\n'.join(x for k, x in blocks if k == 'p'))
    return items


def screened():
    out = set()
    for d in sorted(APX.glob('b*/drafts.json')):
        if d.parent.name == 'b' + NNN:
            continue
        out |= set(json.loads(d.read_text(encoding='utf-8')).values())
    return out


def known():
    out = {}
    for R in sorted(APX.glob('review-r*'), key=lambda p: int(re.sub(r'\D', '', p.name) or 0)):
        if not (R / 'MARCH-labels-b.txt').exists():
            continue
        ids = json.loads((R / 'march-ids.json').read_text())
        texts = [x.strip() for x in re.split(r'\n\s*\n', (R / 'march-in.md').read_text(encoding='utf-8')) if x.strip()]
        assert len(ids) == len(texts), R
        L = [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
              (R / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']
        for j, txt in enumerate(texts, start=1):
            out[txt] = [m[j] for m in L]
    return out


ITEMS, done = {}, screened()
for V in VERSIONS:
    for k, v in plan(V).items():
        if v[0] not in done and v[0] not in [x[0] for x in ITEMS.values()]:
            ITEMS[k] = v
K = known()
todo = [k for k, v in ITEMS.items() if v[1] is not None and v[1] not in K]
if MARCH_ROUND:
    R = APX / MARCH_ROUND
    R.mkdir(exist_ok=True)
    (R / 'march-in.md').write_text('\n\n'.join(ITEMS[k][1] for k in todo) + '\n', encoding='utf-8')
    (R / 'march-ids.json').write_text(json.dumps(todo) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py'), 'march',
                        str(R / 'march-in.md'), str(R / 'MARCH-PROMPT.txt'), '--about',
                        'the reading list at the end of a blog article about building intentional communities'],
                       capture_output=True, text=True)
    print(r.stdout[-300:], r.stderr[-800:])
    print(len(todo), 'march paragraphs to read;', {k: len(v[0].split()) for k, v in ITEMS.items()})
    sys.exit(0)
assert not todo, ('no march reading for', todo)


def lint(text_md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(text_md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


OUT = APX / ('b' + NNN)
OUT.mkdir(exist_ok=True)
drafts, gate = {}, {}
for key, (text, mt, lmd) in ITEMS.items():
    drafts[key] = text
    if mt is not None:
        march = K[mt]
    else:  # a whole draft: the readings of every run in it, one string per reading
        V = key[3:]
        parts = [v[1] for v in plan(V).values() if v[1] is not None]
        march = [' '.join(K[p][x] for p in parts) for x in range(2)]
    gate[key] = {'kind': 'screen', 'march': march, 'march_note': 'appendix/review-r*, one paragraph per item, by its exact text',
                 'lint': lint(lmd), 'words': len(text.split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])
(OUT / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(OUT / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(OUT / 'drafts.json'),
                    str(OUT / 'GATE.json'), str(OUT / ('b%s.js' % NNN)), '--name', 'B' + NNN] + list(drafts),
                   capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(OUT / ('b%s-items.json' % NNN)).write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
