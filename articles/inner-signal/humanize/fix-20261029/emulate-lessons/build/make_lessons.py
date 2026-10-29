"""Builds LESSONS.md: hand-written text, with every quoted example and every count pulled from PAIRS.json and the writers' coding."""
import json, re, collections, statistics, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import writers
from data1 import L, O

OUT = pathlib.Path(__file__).resolve().parents[1]  # the emulate-lessons folder
P = json.loads((OUT / 'PAIRS.json').read_text())
R = {r['id']: r for r in P}
PFX = 'articles/inner-signal/humanize/'


def short(path):
    return path.replace(PFX, '')


def q(s):
    s = re.sub(r'\s*\n\s*', ' / ', s.strip())
    return '"' + s + '"'


def ex(pid, old_read, new_read, who='Emulate', who1='old', order='io'):
    r = R[pid]
    a = '  - %s, %s: %s (`%s`)' % (who1, old_read, q(r['input']), short(r['source_file']))
    b = '  - %s, %s: %s (`%s`)' % (who, new_read, q(r['emulate']), short(r['emulate_file']))
    if order == 'oi':
        a, b = b, a
    return '- `%s` (%s)\n%s\n%s' % (pid, r['detector'], a, b)


def wv(vid):
    e = next(x for x in W if x['id'] == vid)
    return '%s (`%s`, %s)' % (q(e['version']['text']), short(e['version']['file']), e['version']['key'])


SEL = collections.OrderedDict([
    ('4.1 passes', lambda r: r['detector'].startswith('Pangram 4.1') and r['kind'] in ('pass', 'pass-low', 'pass-alone-ai-in-place')),
    ('4.1 Low/Medium to High', lambda r: r['kind'] == 'weak-to-high'),
    ('4.0 passes', lambda r: r['detector'] == 'Pangram 4.0' and r['kind'] == 'pass'),
    ('failures', lambda r: r['kind'].startswith('fail') or r['kind'] == 'weak-stays-weak'),
    ('reverse', lambda r: r['kind'] == 'reverse'),
])
GROUP = {k: [r for r in P if f(r)] for k, f in SEL.items()}
W = writers.entries()


def pct(n, d):
    return '%d (%d%%)' % (n, round(100 * n / d)) if d else '0'


def label_table():
    labs = list(L.values()) + sorted({l for r in P for l in r['labels'] if l.startswith('other: ')} |
                                     {l for e in W for l in e['labels'] if l.startswith('other: ')})
    C = {k: collections.Counter(l for r in v for l in r['labels']) for k, v in GROUP.items()}
    CW = collections.Counter(l for e in W for l in e['labels'])
    head = '| shape change | ' + ' | '.join('%s (%d)' % (k, len(v)) for k, v in GROUP.items()) + ' | our writers, batch 482 (%d) |' % len(W)
    lines = [head, '|' + '---|' * (len(GROUP) + 2)]
    rows = []
    for l in labs:
        vals = [C[k][l] for k in GROUP]
        if not any(vals) and not CW[l]:
            continue
        rows.append((-(C['4.1 passes'][l] / len(GROUP['4.1 passes']) + C['4.1 Low/Medium to High'][l] / len(GROUP['4.1 Low/Medium to High']) + C['4.0 passes'][l] / len(GROUP['4.0 passes'])), l, vals, CW[l]))
    for _, l, vals, cw in sorted(rows):
        lines.append('| %s | %s | %s |' % (l, ' | '.join(pct(v, len(GROUP[k])) for v, k in zip(vals, GROUP)), pct(cw, len(W))))
    return '\n'.join(lines)


def kept_table():
    c = collections.Counter(k for r in GROUP['failures'] for k in r.get('kept_or_made', []))
    lines = ['| what the failing Emulate text still had | failures |', '|---|---|']
    for k, n in c.most_common():
        lines.append('| %s | %d |' % (k, n))
    return '\n'.join(lines)


def sent_lengths(t):
    t = re.sub(r'\s+', ' ', t).strip()
    return [len(s.split()) for s in re.split(r'(?<=[.!?])["”’)]?\s+', t) if s.strip()]


def length_table():
    def row(name, pairs):
        a = [statistics.mean(sent_lengths(x)) for x, _ in pairs]
        b = [statistics.mean(sent_lengths(y)) for _, y in pairs]
        am = [max(sent_lengths(x)) for x, _ in pairs]
        bm = [max(sent_lengths(y)) for _, y in pairs]
        wr = [len(y.split()) / max(1, len(x.split())) for x, y in pairs]
        return '| %s | %d | %.1f → %.1f | %.1f → %.1f | %.2f |' % (name, len(pairs), statistics.mean(a), statistics.mean(b), statistics.mean(am), statistics.mean(bm), statistics.median(wr))
    lines = ['| texts | n | mean sentence, words: before → after | longest sentence: before → after | words after / before (median) |', '|---|---|---|---|---|']
    lines.append(row('Emulate, 4.1 passes and Low/Medium to High', [(r['input'], r['emulate']) for r in GROUP['4.1 passes'] + GROUP['4.1 Low/Medium to High']]))
    lines.append(row('Emulate, 4.0 passes', [(r['input'], r['emulate']) for r in GROUP['4.0 passes']]))
    lines.append(row('Emulate, failures', [(r['input'], r['emulate']) for r in GROUP['failures']]))
    lines.append(row('our writers, batch 482, all versions', [(e['flagged']['text'], e['version']['text']) for e in W]))
    lines.append(row('our writers, batch 482, picked versions', [(e['flagged']['text'], e['version']['text']) for e in W if e['picked']]))
    return '\n'.join(lines)


def counts():
    k = collections.Counter(r['kind'] for r in P)
    d = collections.Counter(r['detector'].split(' (')[0] for r in P)
    return k, d


K, D = counts()
N_PASS = len(GROUP['4.1 passes']) + len(GROUP['4.1 Low/Medium to High']) + len(GROUP['4.0 passes'])
N_ME = sum(1 for r in P if r['meaning_error'] and r['kind'] in ('pass', 'pass-low', 'pass-alone-ai-in-place', 'weak-to-high', 'weak-stays-weak'))
N_PASSISH = sum(1 for r in P if r['kind'] in ('pass', 'pass-low', 'pass-alone-ai-in-place', 'weak-to-high', 'weak-stays-weak'))
BATCHES = sorted({r['batch'].split(' ')[0] for r in P})



B482 = 'fix-20261029/b482/'
B482_C = json.loads((OUT.parents[1] / 'fix-20261029/b482/CANDIDATES.json').read_text())['spots']
B482_S = {x['id']: x for x in json.loads((OUT.parents[1] / 'fix-20261029/b482/recheck/read/SPOTS.json').read_text())['spots']}
B482_T = {x['id']: x for x in json.loads((OUT.parents[1] / 'fix-20261029/b482/TARGETS.json').read_text())['items']}
WCODE = {c[0]: c for c in writers.CODES}


def n_sent(t):
    t = re.sub(r'\s+', ' ', t).strip()
    return len([x for x in re.split(r'(?<=[.!])["”’)]?\s+', t) if x.strip()])


def b482_rows():
    out = []
    for i, c in enumerate(B482_C):
        sid = c['id']
        flagged = B482_T[sid]['flagged_stretch'] if sid in B482_T else c['old']
        a, b = n_sent(flagged), n_sent(c['new'])
        code = WCODE.get(sid)
        labs = (code[2] if c['pick'] == 'v1' else code[3]) if code else []
        out.append(dict(id=sid, i=i, where=c['where'], whose=c['whose'], pick=c['pick'], a=a, b=b, now=B482_S[sid]['now'],
                        labels=labs, emu=(code[4] if code else '') or ''))
    return out


def b482_table():
    rows = b482_rows()
    lines = ['| target | whose | sentences: flagged → new | read in place | the writer\'s main changes |', '|---|---|---|---|---|']
    for r in sorted(rows, key=lambda r: (r['b'] > r['a'], not r['now'].startswith('Human'), r['id'])):
        labs = '; '.join(l.replace('other: ', '') for l in r['labels'][:4])
        lines.append('| %s (%s) | %s | %d → %d | %s | %s |' % (r['id'], r['pick'], r['whose'], r['a'], r['b'], r['now'], labs))
    same = [r for r in rows if r['b'] == r['a']]
    more = [r for r in rows if r['b'] > r['a']]
    fewer = [r for r in rows if r['b'] < r['a']]
    hs = sum(1 for r in same if r['now'].startswith('Human'))
    hm = sum(1 for r in more if r['now'].startswith('Human'))
    lines.append('')
    lines.append('Same number of sentences: %d of %d read Human (%d at High). More sentences: %d of %d read Human (%d at High). Fewer: %d.' % (
        hs, len(same), sum(1 for r in same if r['now'] == 'Human (High)'), hm, len(more), sum(1 for r in more if r['now'] == 'Human (High)'), len(fewer)))
    return '\n'.join(lines)


def b482_ex(sid, note=''):
    r = next(x for x in b482_rows() if x['id'] == sid)
    c = B482_C[r['i']]
    flagged_src = 'fix-20261029/b482/TARGETS.json' if sid in B482_T else 'fix-20261029/b482/CANDIDATES.json'
    flagged = B482_T[sid]['flagged_stretch'] if sid in B482_T else c['old']
    return '- `%s` (%s, %s)\n  - flagged, %s: %s (`%s`)\n  - the writer\'s %s, read %s in place: %s (`fix-20261029/b482/CANDIDATES.json`)%s' % (
        sid, r['where'], r['whose'], '; '.join(B482_T[sid]['readings']) if sid in B482_T else 'AI', q(flagged), flagged_src,
        r['pick'], r['now'], q(c['new']), ('\n  - ' + note) if note else '')




def b482_len():
    rows = b482_rows()
    def sl(t):
        t = re.sub(r'\s+', ' ', t).strip()
        return [len(x.split()) for x in re.split(r'(?<=[.!?])["”’)]?\s+', t) if x.strip()]
    H = [B482_C[r['i']]['new'] for r in rows if r['now'].startswith('Human')]
    A = [B482_C[r['i']]['new'] for r in rows if r['now'].startswith('AI')]
    f = lambda G: (statistics.mean(statistics.mean(sl(t)) for t in G), statistics.mean(len(sl(t)) for t in G))
    (hm, hn), (am, an) = f(H), f(A)
    return ('In batch 482 the %d versions that read Human averaged %.1f words a sentence and %.1f sentences; the %d that read AI, '
            '%.1f words and %.1f sentences.' % (len(H), hm, hn, len(A), am, an))


TEXT = open(pathlib.Path(__file__).parent / 'lessons_body.md').read()


def fill(t):
    def rep(m):
        a = m.group(1).split('|')
        return ex(a[0], a[1], a[2], *(a[3:] or []))
    t = re.sub(r'\{EX:([^}]*)\}', rep, t)
    t = re.sub(r'\{WV:([^}]*)\}', lambda m: wv(m.group(1)), t)
    t = re.sub(r'\{Q:([^}]*)\}', lambda m: '%s (`%s`)' % (q(R[m.group(1).split('|')[0]][m.group(1).split('|')[1]]), short(R[m.group(1).split('|')[0]]['source_file' if m.group(1).split('|')[1] == 'input' else 'emulate_file'])), t)
    t = re.sub(r'\{B482:([^}|]*)\|?([^}]*)\}', lambda m: b482_ex(m.group(1), m.group(2)), t)
    t = t.replace('{B482_TABLE}', b482_table()).replace('{B482_LEN}', b482_len())
    t = t.replace('{LABEL_TABLE}', label_table()).replace('{KEPT_TABLE}', kept_table()).replace('{LENGTH_TABLE}', length_table())
    t = t.replace('{N_ROWS}', str(len(P))).replace('{N_PASS}', str(N_PASS)).replace('{N_FAIL}', str(len(GROUP['failures']))).replace('{N_REV}', str(len(GROUP['reverse'])))
    t = t.replace('{N_41}', str(len(GROUP['4.1 passes']))).replace('{N_41W}', str(len(GROUP['4.1 Low/Medium to High']))).replace('{N_40}', str(len(GROUP['4.0 passes'])))
    t = t.replace('{N_ME}', str(N_ME)).replace('{N_PASSISH}', str(N_PASSISH)).replace('{N_BATCH}', str(len(BATCHES))).replace('{N_W}', str(len(W)))
    return t


(OUT / 'LESSONS.md').write_text(fill(TEXT), encoding='utf-8')
print('LESSONS.md written,', len(fill(TEXT).splitlines()), 'lines')
