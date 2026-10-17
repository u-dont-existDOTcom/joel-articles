"""slide.py - screens (E175) of every run of three paragraphs in a draft of section 16, as Pangram reads them inside the whole
section (2026-10-17). Batch 347g showed that the whole section's AI windows are the AI reading of a stretch alone: v10's caption
and H2-P2 to H2-P4 read 0.92 alone, though every paragraph and pair read Human. Pangram's windows inside the whole section ran
116 to 222 words, about three paragraphs here, so a sliding run of three paragraphs (with the headings and the caption between
them) finds them for a few credits, and a draft goes to a whole-section screen when every run reads Human.
Usage (from candidate/): python3 s16/slide.py NNN NAME SCRIPT [ARG ...] --draft vNN.md --march MAP.json [--only H2,H3]
  [--changed H2-P3,H2-P4]   (only the runs that hold a changed paragraph)  [--pairs]  (and each changed paragraph alone
  and with each neighbor)  [--whole]  (and the whole section)  [--starts H3-P4,...]  (only the runs that start at these
  paragraphs, for a variant screened beside another: 2026-10-17, v16)
MAP.json: {"H2-P3": "H2-P3e", ...}, the march key of each paragraph that differs from the plain id (rounds r2 to r22).
Writes s16/bNNN/ (drafts.json, GATE.json, the in-page batch and bNNN-items.json)."""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

S16 = pathlib.Path(__file__).resolve().parent
C = S16.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

a = sys.argv[1:]
NNN, NAME, SCRIPT = a[0], a[1], a[2]
opt = lambda k: a[a.index(k) + 1] if k in a else None
ARGS = [x for x in a[3:a.index('--draft')]]
DRAFT = opt('--draft')
MAP = json.loads(pathlib.Path(opt('--march')).read_text()) if opt('--march') else {}
ONLY = opt('--only').split(',') if opt('--only') else None
CHANGED = opt('--changed').split(',') if opt('--changed') else None
STARTS = opt('--starts').split(',') if opt('--starts') else None
ROUNDS = ['review-r2', 'review-r3', 'review-r3b', 'review-r3c', 'review-r3d', 'review-r5', 'review-r6', 'review-r8', 'review-r9',
          'review-r10', 'review-r11', 'review-r12', 'review-r14', 'review-r15', 'review-r16', 'review-r17', 'review-r18',
          'review-r20', 'review-r21', 'review-r22'] + sorted(
    (p.name for p in S16.glob('review-r*') if re.fullmatch(r'review-r\d+', p.name) and int(p.name[8:]) >= 23
     and (p / 'march-ids.json').exists() and (p / 'MARCH-labels-b.txt').exists()), key=lambda n: int(n[8:]))
IDS = (['H1'] + ['H1-P%d' % i for i in range(1, 4)] + ['H2'] + ['H2-P%d' % i for i in range(1, 7)] + ['H3'] +
       ['H3-P%d' % i for i in range(2, 12)])
PARAS = [i for i in IDS if '-' in i]


def labels(folder):
    return [{int(k): v.strip() for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$',
             (folder / ('MARCH-labels-%s.txt' % x)).read_text(encoding='utf-8'), re.M)} for x in 'ab']


MARCH = {}
for rnd in ROUNDS:
    L = labels(S16 / rnd)
    for n, p in enumerate(json.loads((S16 / rnd / 'march-ids.json').read_text()), start=1):
        if p.startswith('s15-'):
            continue
        if rnd == 'review-r11' and p == 's16-H1-P2':
            p = 's16-H1-P2num'
        MARCH[p[4:] if p.startswith('s16-') else p] = [m[n] for m in L]
MARCH['H2-P3'] = MARCH['H2-P3a']
MARCH['H2-P5'] = MARCH['H2-P5d']
MARCH['H3-P4'] = MARCH['H3-P4x']
M = {p: MARCH[MAP.get(p, p)] for p in PARAS}

subprocess.run([sys.executable, str(S16 / SCRIPT)] + ARGS, check=True, capture_output=True)
blocks = [b.strip() for b in re.split(r'\n\s*\n', (S16 / DRAFT).read_text(encoding='utf-8')) if b.strip()]
reader = [b for b in blocks if not re.match(r'^\[image \d+\]', b)]
seq, pid = [], iter(IDS)
for b in reader:
    if b.startswith('[caption]'):
        seq.append(('c', None, re.sub(r'^\[caption\]\s*', '', b)))
    else:
        i = next(pid)
        seq.append(('h' if '-' not in i else 'p', i, b))
assert next(pid, None) is None
pidx = [n for n, (k, _, _) in enumerate(seq) if k == 'p']


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}
for w in range(len(pidx) - 2):
    s, e = pidx[w], pidx[w + 2]
    while s > 0 and seq[s - 1][0] in 'hc':
        s -= 1           # the heading or caption right before the run, as the whole section has it
    part = seq[s:e + 1]
    ps = [i for k, i, _ in part if k == 'p']
    if ONLY and not any(p.split('-')[0] in ONLY for p in ps):
        continue
    if CHANGED and not any(p in CHANGED for p in ps):
        continue      # a run with no changed paragraph has its screen already
    if STARTS and ps[0] not in STARTS:
        continue
    same = ps[0].split('-')[0] == ps[-1].split('-')[0]
    key = '%s-%s-%s' % (NAME, ps[0], ps[-1].split('-')[1] if same else ps[-1])
    drafts[key] = '\n\n'.join(plain(t.lstrip('#').strip()) if k == 'h' else plain(t) for k, _, t in part)
    # the linter's rates (short landings, openers) are a subsection's, so a run is linted as the subsections it touches
    subs = sorted({p.split('-')[0] for p in ps})
    gate[key] = {'kind': 'screen', 'march': [x for p in ps for x in M[p]], 'march_note': 'rounds r2 to r22, as in 346g',
                 'lint': lint('\n\n'.join(t for k, i, t in seq if k == 'p' and i.split('-')[0] in subs)),
                 'lint_note': 'the subsections the run touches: ' + ', '.join(subs), 'words': len(drafts[key].split())}
if CHANGED and '--pairs' in a:
    # each changed paragraph alone (50 words or more) and with each neighbor under its heading, for paragraphs_alone.py
    T = {i: t for k, i, t in seq if k == 'p'}
    for p in CHANGED:
        if len(plain(T[p]).split()) >= 50:
            key = '%s-%s' % (NAME, p)
            drafts[key] = plain(T[p])
            gate[key] = {'kind': 'screen', 'march': M[p], 'march_note': 'its own march', 'words': len(drafts[key].split()),
                         'lint': lint('\n\n'.join(t for k, i, t in seq if k == 'p' and i.split('-')[0] == p.split('-')[0]))}
        j = PARAS.index(p)
        for q in (PARAS[j - 1] if j else None, PARAS[j + 1] if j + 1 < len(PARAS) else None):
            if q and q.split('-')[0] == p.split('-')[0]:
                pr = sorted([p, q], key=PARAS.index)
                key = '%s-%s+%s' % (NAME, pr[0], pr[1].split('-')[1])
                if key in drafts:
                    continue
                drafts[key] = plain(T[pr[0]]) + '\n\n' + plain(T[pr[1]])
                gate[key] = {'kind': 'screen', 'march': M[pr[0]] + M[pr[1]], 'march_note': 'the pair', 'words': len(drafts[key].split()),
                             'lint': lint('\n\n'.join(t for k, i, t in seq if k == 'p' and i.split('-')[0] == p.split('-')[0]))}
if '--whole' in a:
    key = NAME
    drafts[key] = '\n\n'.join(plain(t.lstrip('#').strip()) if k == 'h' else plain(t) for k, _, t in seq)
    gate[key] = {'kind': 'screen', 'march': [x for p in PARAS for x in M[p]], 'march_note': 'every paragraph',
                 'lint': lint('\n\n'.join(t for k, _, t in seq if k == 'p')), 'words': len(drafts[key].split())}
out = S16 / ('b' + NNN)
out.mkdir(exist_ok=True)
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                    str(out / 'GATE.json'), str(out / ('b%s.js' % NNN)), '--name', 'B' + NNN] + list(drafts), capture_output=True,
                   text=True)
print(r.stdout[-300:], r.stderr[-1500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(out / ('b%s-items.json' % NNN)).write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
print(len(items), sum(g['words'] for g in gate.values()), {k: (g['words'], g['lint']) for k, g in gate.items()})
