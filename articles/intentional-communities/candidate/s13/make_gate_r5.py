"""Section 13, gate round r5 on v7 (2026-10-15, Joel's 31 a): v7 rebuilt 21 of the 25 paragraphs from Emulate (rounds b,
c and d) with the published meaning put back word by word (make_v7.py, v7-sources.json). Traces go to the pairs whose
rewrite changed since v6; the march read, both cold reads and both stance checks cover the whole section, the stance
checks with the scope rule of 2026-10-15 (stance_check_prompt.py: read each rule within its section). Run from the repo
root:

  python3 articles/intentional-communities/candidate/s13/make_gate_r5.py

Writes s13/review-r5/. Pairs: each published paragraph (the published text with Joel's 2026-10-12 line, as in
HUMANIZED-SO-FAR.md) with the v7 paragraph(s) that carry it; four pairs at most per trace run (trace_brief.md). Joel's
own line ("So work out the process before it's about anyone in particular", his answer 13 of 2026-10-11) is marked as
his.
"""
import pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = CAND / 's13'
OUT = S13 / 'review-r5'
MARCH_ONLY = '--march-only' in sys.argv
DRAFT = S13 / 'v7.md'
PREV = S13 / 'v6.md'
OUT.mkdir(exist_ok=True)
HEAD = '# Your Little Forming Group Already Is the Community'
JOEL = "So work out the process before it's about anyone in particular."


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


so_far = (CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = so_far.index(HEAD)
b = so_far.index('\n# ', a + 5)
pub = [x for x in blocks(so_far[a:b]) if not x.startswith('<!--')]
before_section = [x for x in blocks(so_far[:a]) if not x.startswith('<!--') and not x.startswith('#')][-1]
after_section = [x for x in blocks(so_far[b:]) if not x.startswith('<!--')][:2]
v2 = blocks(DRAFT.read_text(encoding='utf-8'))


def paras_by_heading(bs):
    out, cur = [], None
    for x in bs:
        if x.startswith('#'):
            cur = re.sub(r'^#+\s*', '', x)
            out.append((cur, []))
        else:
            out[-1][1].append(x)
    return out


P = paras_by_heading(pub)
R = paras_by_heading(v2)
assert [h for h, _ in P] == [h for h, _ in R], ([h for h, _ in P], [h for h, _ in R])
# published paragraph numbers (1-based, under each heading) -> v2 paragraph numbers
MAP = [
    [([1], [1]), ([2, 3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5, 6, 7], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6, 7], [5]), ([8], [6, 7]), ([9], [8]), ([10], [9])],
    [([1], [1]), ([2], [2]), ([3], [3]), ([4], [4])],
]
flat_r = [(hi, j + 1) for hi, (_, ps) in enumerate(R) for j in range(len(ps))]
pairs = []
for hi, ((h, pps), (_, rps), m) in enumerate(zip(P, R, MAP)):
    assert sorted(x for pp, _ in m for x in pp) == list(range(1, len(pps) + 1)), h
    assert sorted(x for _, rr in m for x in rr) == list(range(1, len(rps) + 1)), h
    for pp, rr in m:
        first = flat_r.index((hi, rr[0]))
        last = flat_r.index((hi, rr[-1]))
        def rtext(k):
            hh, jj = flat_r[k]
            return R[hh][1][jj - 1]
        ctx_b = rtext(first - 1) if first > 0 else before_section
        ctx_a = rtext(last + 1) if last + 1 < len(flat_r) else after_section[0]
        if first > 0 and flat_r[first - 1][0] != hi:
            ctx_b = '(the heading "%s" comes between) ' % h + ctx_b
        elif first == 0:
            ctx_b = '(the end of the section before; this section starts with the heading "%s") ' % h + ctx_b
        rew = '\n\n'.join(R[hi][1][k - 1] for k in rr)
        if JOEL in rew:
            rew = rew.replace(JOEL, '⟦author⟧' + JOEL + '⟦/author⟧')
        name = '%s P%s → P%s' % (h, '+'.join(map(str, pp)), '+'.join(map(str, rr)))
        pairs.append(dict(name=name, head=h, pub='\n\n'.join(pps[k - 1] for k in pp), rew=rew,
                          before=re.sub(r'\s+', ' ', ctx_b)[:400], after=re.sub(r'\s+', ' ', ctx_a)[:400]))

if MARCH_ONLY:
    subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py'), 'march', str(DRAFT),
                    str(OUT / 'MARCH-PROMPT.txt')], check=True)
    sys.exit(0)
brief = (REPO / 'tools' / 'humanization' / 'reviewer' / 'trace_brief.md').read_text(encoding='utf-8')
brief = re.sub(r'<!--.*?-->\n*', '', brief, flags=re.S)
prev = blocks(PREV.read_text(encoding='utf-8'))
pairs = [p for p in pairs if any(x not in prev for x in p['rew'].replace('⟦author⟧', '').replace('⟦/author⟧', '').split('\n\n'))]
groups = [pairs[i:i + 4] for i in range(0, len(pairs), 4)]
for n, g in enumerate(groups, start=1):
    inp = OUT / ('trace-in-T%d.md' % n)
    lines = ['# Section 13 pairs (T%d): published paragraph and rewrite' % n, '',
             'Section 13 is "Your Little Forming Group Already Is the Community", with four subheadings. The rewrite keeps '
             'the published order and headings. Several short published paragraphs are joined in the rewrite, and one is '
             'split in two; a pair shows all the published paragraphs a rewrite paragraph carries, or both rewrite paragraphs. '
             'Text between ⟦author⟧ '
             'and ⟦/author⟧ is Joel\'s own wording (his answer of 2026-10-11).', '']
    for p in g:
        lines += ['## ' + p['name'], '', 'CONTEXT BEFORE: ' + p['before'], '', 'PUBLISHED:', '', p['pub'], '',
                  'REWRITE:', '', p['rew'], '', 'CONTEXT AFTER: ' + p['after'], '']
    inp.write_text('\n'.join(lines), encoding='utf-8')
    words = 750 if len(g) == 4 else 200 * len(g) + 150
    prompt = (brief.replace('{what}', 'community section 13 ("Your Little Forming Group Already Is the Community"), '
                                      'pairs %d to %d of %d' % (pairs.index(g[0]) + 1, pairs.index(g[-1]) + 1, len(pairs)))
                   .replace('{input}', str(inp)).replace('{report}', str(OUT / ('trace-T%d.md' % n)))
                   .replace('{words}', str(words)))
    (OUT / ('TRACE-PROMPT-T%d.txt' % n)).write_text(prompt, encoding='utf-8')
print(len(pairs), 'pairs in', len(groups), 'trace runs')

py = sys.executable
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
art = str(CAND / 'HUMANIZED-SO-FAR.md')
for x in 'ab':
    subprocess.run([py, RV, '--article', art, 'sense-section', str(OUT / ('SENSE-PROMPT-%s.txt' % x)),
                    '--section', HEAD[2:], '--draft', str(DRAFT),
                    '--report', str(OUT / ('SENSE-%s.md' % x))], check=True)
subprocess.run([py, RV, 'march', str(DRAFT), str(OUT / 'MARCH-PROMPT.txt')], check=True)
ST = str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py')
owner = OUT / 'owner.md'
owner.write_text(JOEL + '\n', encoding='utf-8')
for tag, essay in (('pub', str(CAND.parent / 'original.md')), ('sofar', art)):
    subprocess.run([py, ST, '--essay', essay, '--rewrite', str(DRAFT), '--out', str(OUT / ('STANCE-PROMPT-%s.txt' % tag)),
                    '--scope', 'section 13 ("Your Little Forming Group Already Is the Community"), rewritten',
                    '--topic', 'building intentional communities', '--report', str(OUT / ('STANCE-%s.md' % tag)),
                    '--images', str(CAND / 'images.json'), '--positions', str(S13 / 'positions.txt'),
                    '--owner', str(owner)], check=True)
print('prompts in', OUT)
