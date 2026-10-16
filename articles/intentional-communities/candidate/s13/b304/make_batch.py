"""Batch 304g (2026-10-16): section 13 draft v26 (way A, v26.md; way B of H5-P2, v26b.md), the one more bounded fix-and-check
pass after Joel's message of 18:22 UTC. v21 read 56% AI as a whole (298g) though each part read Human alone, and 299g found the
land subsection and the stretch from H4-P9 through H5-P2 AI in every context; v22 to v26 rewrote those (Emulate round i, the
meaning put back over rounds r15 to r18) and made the fixes the rounds called for.

Stage 1 (this batch): every group of at least 50 words that holds a paragraph changed since v21, the land subsection, the
visitor subsection, the last subsection both ways, and the stretch from H4-P9 through H5-P2 both ways. Stage 2 (--section): the
whole section, the way that read better, once stage 1 is in.

Records: a paragraph unchanged since v21 keeps the record of the check that admitted it (b298/COVERAGE.md, b298/GATE.json). A
changed paragraph's record is its latest rounds': march r17 (r17b for H3-P3 to H3-P5, r18 for H2-P2), cold reads r17 (OK for
all 27 paragraphs of v24), traces r16 to r18 with their dispositions, stance r16 (its one conflict fixed in v24; v24 to v26 put
published words back and add no position), lint and keys on v26. H2-P2 goes as an edit (E173): its v21 version passed in 299g.
Run from candidate/: python3 s13/b304/make_batch.py [--section A|B]"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parents[1]
REPO = C.parents[2]
S13 = C / 's13'
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain  # noqa: E402

IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
HEADS = {0: 'H1', 5: 'H2', 11: 'H3', 17: 'H4', 27: 'H5'}


def blocks(f):
    return [b.strip() for b in re.split(r'\n\s*\n', (S13 / f).read_text(encoding='utf-8')) if b.strip()]


V21, VA, VB = blocks('v21.md'), blocks('v26.md'), blocks('v26b.md')
assert len(V21) == len(VA) == len(VB) == len(IDS)
TEXT = {'A': {}, 'B': {}}
for way, bl in (('A', VA), ('B', VB)):
    for i, (pid, b) in enumerate(zip(IDS, bl)):
        TEXT[way][pid or HEADS[i]] = b
OLD = {pid: b for pid, b in zip(IDS, V21) if pid}
CHANGED = {pid for pid in OLD if TEXT['A'][pid] != OLD[pid]}


def labels(path):
    out = {}
    for k, v in re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', path.read_text(encoding='utf-8'), re.M):
        out[int(k)] = v
    return out


R17 = [labels(S13 / 'review-r17' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
R17V = [labels(S13 / 'review-r17' / ('MARCH-labels-variants-%s.txt' % x)) for x in 'ab']
R17B = [labels(S13 / 'review-r17b' / ('MARCH-labels-%s.txt' % x)) for x in 'ab']
R18H2 = [labels(S13 / 'review-r18' / ('MARCH-labels-h2a-%s.txt' % x)) for x in 'ab']
T = {pid: n for n, pid in enumerate([p for p in IDS if p], start=1)}  # the T-number of each paragraph in a whole-section read
NEW_MARCH = {pid: [r[T[pid]] for r in R17] for pid in CHANGED}
NEW_MARCH.update({'H3-P3': [r[1] for r in R17B], 'H3-P4': [r[2] for r in R17B], 'H3-P5': [r[3] for r in R17B],
                  'H2-P2': [r[2] for r in R18H2], 'H5-P2b': [r[1] for r in R17V]})
R17D, R16D = 's13/review-r17/DISPOSITIONS-r17.md', 's13/review-r16/DISPOSITIONS-r16.md'
GROUNDING = {
 'H1-P1': 's13/review-r17/trace-T1.md (OK)',
 'H1-P4': 's13/review-r18/trace-T1.md (v25\'s "a budget of"); before it unchanged since v21 (b298: S13v9-1P4)',
 'H2-P2': 's13/review-r18/trace-T1.md (v26\'s break "Long list, huh?"); its v23 wording: s13/review-r16/trace-T1.md (OK)',
 'H3-P1': 's13/review-r16/trace-T2.md (OK)',
 'H3-P2': 's13/review-r16/trace-T2.md (OK); v24\'s "how inheritance works" is the published word (' + R16D + ')',
 'H3-P3': 's13/review-r17b/trace-T1.md (OK)',
 'H3-P4': 's13/review-r15/trace-T3.md (OK)',
 'H3-P5': 's13/review-r17b/trace-T1.md (two findings kept, ' + R17D + ')',
 'H4-P2': 's13/review-r17/trace-T3.md ("for a while" cut in v24, "(Not everyone does!)" kept, ' + R17D + ')',
 'H4-P6': 's13/review-r18/trace-T2.md (v25\'s "Six months"); s13/review-r17/trace-T4.md before it',
 'H4-P7': 's13/review-r18/trace-T2.md; the van-keys line kept (' + R17D + ')',
 'H4-P9': 's13/review-r18/trace-T2.md (v25\'s "All of them"); s13/review-r17/trace-T4.md (OK) before it',
 'H5-P1': 's13/review-r17/trace-T5.md ("Yeah, that\'s pretty tough ..." kept, ' + R17D + ')',
 'H5-P2': 's13/review-r16/trace-T6.md (OK)',
 'H5-P2b': 's13/review-r17/trace-T6.md (OK)',
}
assert set(GROUNDING) - {'H5-P2b'} == CHANGED, (sorted(CHANGED), sorted(GROUNDING))

g298 = json.loads((S13 / 'b298' / 'GATE.json').read_text(encoding='utf-8'))
cov = (S13 / 'b298' / 'COVERAGE.md').read_text(encoding='utf-8')
ADMIT = {}
for part, key in re.findall(r'^\| (H\d-P\d+b?)[^|]*\| (\S+) \(', cov, re.M):
    ADMIT[part] = key


def old_march(pid):
    """The march readings of the check that admitted an unchanged paragraph; a pair's record holds both paragraphs' readings."""
    key = ADMIT[pid]
    m = g298[key]['march']
    pair = re.search(r'-(\d)P(\d+)P(\d+)$', key)
    if pair and len(m) == 4:
        return m[:2] if pid.endswith('P' + pair.group(2)) else m[2:]
    return m


def march(pid, way):
    if pid == 'H5-P2' and way == 'B':
        return NEW_MARCH['H5-P2b']
    return NEW_MARCH[pid] if pid in CHANGED else old_march(pid)


def lint(md):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


SUB = {'H1': ['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], 'H2': ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       'H3': ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'],
       'H4': ['H4-P%d' % i for i in range(1, 10)], 'H5': ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']}
STAGE1 = {
 'S13v26-1hP1P2': ('A', ['H1', 'H1-P1', 'H1-P2']),
 'S13v26-1P3P4': ('A', ['H1-P3', 'H1-P4']),
 'S13v26-2P1P2': ('A', ['H2-P1', 'H2-P2']),
 'S13v26-3P1P2': ('A', ['H3-P1', 'H3-P2']),
 'S13v26-3P3': ('A', ['H3-P3']),
 'S13v26-3P4P5': ('A', ['H3-P4', 'H3-P5']),
 'S13v26-H3': ('A', ['H3'] + SUB['H3']),
 'S13v26-4P1P2': ('A', ['H4-P1', 'H4-P2']),
 'S13v26-4P6P7': ('A', ['H4-P6', 'H4-P7']),
 'S13v26-H4': ('A', ['H4'] + SUB['H4']),
 'S13v26-4P9h5P2': ('A', ['H4-P9', 'H5', 'H5-P1', 'H5-P2']),
 'S13v26b-4P9h5P2': ('B', ['H4-P9', 'H5', 'H5-P1', 'H5-P2']),
 'S13v26-H5': ('A', ['H5'] + SUB['H5']),
 'S13v26b-H5': ('B', ['H5'] + SUB['H5']),
}
COLD = 's13/review-r17/SENSE-a.md, SENSE-b.md: OK for all 27 paragraphs of v24 (v25 and v26 change a few words in four)'
STANCE = ('s13/review-r16/STANCE-pub.md, STANCE-sofar.md on v23: one conflict, fixed in v24 ("how inheritance works"); v24 to '
          'v26 put published words back and add no position')


def record(key, way, parts):
    ps = [p for p in parts if not p.startswith('H') or '-' in p]
    if 'H2-P2' in ps:
        # E173: v21's H2-P2 passed with H2-P1 in 299g; v23 took its break and v26 puts one back, so the edit has a break again.
        was = old_march('H2-P2')
        return {'kind': 'edit', 'was': 'batch 299g: S13v21-2P1P2 (H2-P1 with H2-P2), Human (medium); H2-P1 unchanged since',
                'march_was': was, 'march': NEW_MARCH['H2-P2'],
                'march_note': 'was: b298 S13v10-2P1P2 (H2-P2\'s readings); now: s13/review-r18/MARCH-labels-h2a-a.txt and -b.txt',
                'cold': 'OK', 'cold_note': COLD, 'grounding': 'OK', 'grounding_note': GROUNDING['H2-P2'],
                'stance': 0, 'stance_note': STANCE, 'missing': []}
    return {'kind': 'draft', 'march': [m for p in ps for m in march(p, way)],
            'march_note': '; '.join('%s: %s' % (p, ('r17/r17b/r18, ' if p in CHANGED else 'b298 ' + ADMIT[p] + ', ') + str(march(p, way)))
                                    for p in ps),
            'cold': 'OK', 'cold_note': COLD, 'grounding': 'OK',
            'grounding_note': '; '.join('%s: %s' % (p, GROUNDING['H5-P2b' if (p == 'H5-P2' and way == 'B') else p]
                                                    if p in CHANGED else 'unchanged since v21 (b298 %s)' % ADMIT[p]) for p in ps),
            'stance': 0, 'stance_note': STANCE, 'missing': []}


def build(items, name):
    drafts, gate = {}, {}
    for key, (way, parts) in items.items():
        md = [TEXT[way][p] for p in parts]
        drafts[key] = '\n\n'.join(plain(x) for x in md)
        if isinstance(parts, list) and parts and parts[0] == 'SECTION':
            continue
        gate[key] = record(key, way, parts)
        gate[key]['lint'] = lint('\n\n'.join(x for x in md if not x.startswith('#')))
        gate[key]['words'] = len(drafts[key].split())
        assert gate[key]['words'] >= 50, key
    return drafts, gate


if '--section' in sys.argv:
    way = sys.argv[sys.argv.index('--section') + 1]
    drafts, gate = build(STAGE1, 'B304')
    keyA = 'S13v26%s' % ('' if way == 'A' else 'b')
    order = [None] + [p for p in IDS]
    drafts[keyA] = '\n\n'.join(plain(TEXT[way][p or HEADS[i]]) for i, p in enumerate(IDS))
    gate[keyA] = {'kind': 'section', 'parts': [k for k, (w, _) in STAGE1.items() if w == way], 'repeats': 0,
                  'repeats_note': 's13/review-r15/REPEATS.md, answered in s13/review-r15/DISPOSITIONS-r15.md; v23 to v26 add breaks '
                                  'and no claim, and the two apologies ("Sorry!" in H3-P3, "(Sorry, hanging out doesn\'t count!" in '
                                  'H4-P8) are two subsections apart'}
    run = [keyA]
    out = 'b304s'
else:
    drafts, gate = build(STAGE1, 'B304')
    run = list(STAGE1)
    out = 'b304'
(HERE / ('drafts%s.json' % ('' if out == 'b304' else '-s'))).write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(HERE / ('GATE%s.json' % ('' if out == 'b304' else '-s'))).write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'),
                    str(HERE / ('drafts%s.json' % ('' if out == 'b304' else '-s'))),
                    str(HERE / ('GATE%s.json' % ('' if out == 'b304' else '-s'))), str(HERE / (out + '.js')),
                    '--name', out.upper()] + run, capture_output=True, text=True)
print(r.stdout[-2500:], r.stderr[-1500:])
print('changed since v21:', sorted(CHANGED))
