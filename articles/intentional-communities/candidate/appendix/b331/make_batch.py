"""Batch 331g (2026-10-17): screens (E175) of the appendix draft v3 (../make_v2.py: every entry rebuilt from Emulate round a
with the published meaning put back; ../make_v3.py: a break in each screened run). The entries are 8 to 40 words, two or three under each heading, so no entry can be read
alone or with one neighbor under its heading (Pangram reads 50 words or more). Each entry is screened inside the shortest
run around it that Pangram can read (tools/humanization/paragraphs_alone.py, minimal_runs: consecutive entries with the
headings between them, at least 50 words by spaces, and dropping the first or last entry, other than the one checked, takes
it under 50); a few runs cover every entry (a run is the shortest for each entry inside it when dropping either end takes it
under 50). Where two entries under one heading reach 50 words together (Liedloff and Doucleff), the pair is the test,
as for prose. The research paragraph, 50 words or more, goes alone; the whole appendix goes as a reader sees it.
The march is read per run, one paragraph per run (review-r1, two readings): a one-sentence entry can't hold a break of its
own, and the run is what Pangram reads. v2's march is review-r1, v3's review-r2, v4's changed runs review-r3; each
run takes the readings of its exact text.
Run from candidate/: python3 appendix/b331/make_batch.py [--march]   (--march writes the march prompt; the batch needs the
two readings in review-r1)"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
APX = HERE.parent
C = APX.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from ptext import plain  # noqa: E402
import paragraphs_alone as PA  # noqa: E402

V = 'v4'  # v2's march (review-r1) found a break in two of the twelve runs; v3 (../make_v3.py) adds one to each,
# v4 (../make_v4.py) to the two runs v3's march (review-r2) still read without one
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
    if ok:  # a pair under one heading that reaches 50 words is the test, as for prose (Liedloff and Doucleff)
        need[i] = ok[0]
        continue
    need[i] = 'run'
    for a, b, text, _ in PA.minimal_runs(md, i):
        runs.setdefault((a, b), {'text': text, 'for': set()})['for'].add(i)
# the fewest runs that cover every entry that needs one (greedy, the run that covers most first, then the shorter)
left = {i for i, k in need.items() if k == 'run'}
chosen = []
while left:
    best = max(runs.items(), key=lambda kv: (len(kv[1]['for'] & left), -len(kv[1]['text'].split()), -kv[0][0]))
    assert best[1]['for'] & left
    chosen.append(best[0])
    left -= best[1]['for']
chosen.sort()
ITEMS = {}
for a, b in chosen:
    ITEMS['APX%s-E%02d-%02d' % (V, a + 1, b + 1)] = runs[(a, b)]['text']
for i, k in need.items():
    if k == 'alone':
        ITEMS['APX%s-E%02d' % (V, i + 1)] = plain(paras[i][1])
    elif isinstance(k, tuple):
        ITEMS['APX%s-E%02d-%02d' % (V, k[0] + 1, k[1] + 1)] = plain(paras[k[0]][1]) + '\n\n' + plain(paras[k[1]][1])
whole = '\n\n'.join(plain(x.lstrip('#').strip()) if k == 'h' else plain(x) for k, x in PA.reader_blocks(md))
ITEMS['APX' + V] = whole

ROUNDS = ['review-r1', 'review-r2', 'review-r3']  # oldest first; a later round's reading of the same text wins
NEW_ROUND = APX / ROUNDS[-1]
MARCH_KEYS = [k for k in ITEMS if k != 'APX' + V]


def entries(key):
    m = re.match(r'APX\w+-E(\d+)(?:-(\d+))?$', key)
    a = int(m.group(1)) - 1
    b = int(m.group(2) or m.group(1)) - 1
    return [paras[j][1] for j in range(a, b + 1)]


def march_text(key):
    """One paragraph per item: its entries run together, without the headings (the march reads sentences)."""
    return ' '.join(entries(key))


def known():
    """march paragraph text -> its two readings, from every round that has them"""
    out = {}
    for rnd in ROUNDS:
        R = APX / rnd
        if not (R / 'MARCH-labels-b.txt').exists():
            continue
        ids = json.loads((R / 'march-ids.json').read_text())
        texts = [x.strip() for x in re.split(r'\n\s*\n', (R / 'march-in.md').read_text(encoding='utf-8')) if x.strip()]
        assert len(ids) == len(texts), rnd
        L = [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
              (R / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']
        for j, txt in enumerate(texts, start=1):
            out[txt] = [m[j] for m in L]
    return out


if '--march' in sys.argv:
    K = known()
    todo = [k for k in MARCH_KEYS if march_text(k) not in K]
    NEW_ROUND.mkdir(exist_ok=True)
    (NEW_ROUND / 'march-in.md').write_text('\n\n'.join(march_text(k) for k in todo) + '\n', encoding='utf-8')
    (NEW_ROUND / 'march-ids.json').write_text(json.dumps(todo) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py'), 'march',
                        str(NEW_ROUND / 'march-in.md'), str(NEW_ROUND / 'MARCH-PROMPT.txt'), '--about',
                        'the reading list at the end of a blog article about building intentional communities'],
                       capture_output=True, text=True)
    print(r.stdout[-300:], r.stderr[-800:])
    print(len(todo), 'march paragraphs to read, of', len(MARCH_KEYS), ';', {k: len(v.split()) for k, v in ITEMS.items()})
    sys.exit(0)

K = known()
missing = [k for k in MARCH_KEYS if march_text(k) not in K]
assert not missing, ('no march reading for', missing)
MARCH = {k: K[march_text(k)] for k in MARCH_KEYS}


def lint(text_md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(text_md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


def md_of(key):
    if key == 'APX' + V:
        return '\n\n'.join(x for k, x in PA.reader_blocks(md) if k == 'p')
    m = re.match(r'APX\w+-E(\d+)(?:-(\d+))?$', key)
    a, b = int(m.group(1)) - 1, int(m.group(2) or m.group(1)) - 1
    return '\n\n'.join(paras[j][1] for j in range(a, b + 1))


drafts, gate = {}, {}
for key, text in ITEMS.items():
    drafts[key] = text
    march = MARCH.get(key) or [' '.join(MARCH[k][x] for k in MARCH_KEYS) for x in range(2)]
    gate[key] = {'kind': 'screen', 'march': march, 'march_note': 'appendix/review-r1 to r3, one paragraph per run, by its exact text',
                 'lint': lint(md_of(key)), 'words': len(text.split())}
    assert gate[key]['words'] >= 50, (key, gate[key]['words'])
(HERE / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(HERE / 'drafts.json'),
                    str(HERE / 'GATE.json'), str(HERE / 'b331.js'), '--name', 'B331'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-800:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(HERE / 'b331-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
