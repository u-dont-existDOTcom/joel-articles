"""Section 13, gate round r22 on v32 (2026-10-17): the confirming traces of what changed after round r21's traces (its
marches, trace fixes, the stance check and the pause tally; review-r21/DISPOSITIONS-r21.md). Only the traces; the rest of
round r21 stands. Round r21's text follows.

Section 13, gate round r21 on v32 (2026-10-17): v32 is v31 with Joel's "if the community uses them" back, the short visit's
punchline fixed (the one paragraph that read AI alone, batch 312g), the book line no longer leaning on the book's order, and
the dedup he asked for (make_v32.py). One lean round (E177, E178), in parallel: the march of the whole section (two readings),
the meaning traces of the pairs v32 changed since v31 (the published text comes from original.md now that v31 is in the
article), one cold read of the section in the article, the stance check against the article so far (not against the
published essay: the book line departs from it on purpose, at Joel's word), and the repeats check of the assembled section.
Run from the repo root: python3 articles/intentional-communities/candidate/s13/make_gate_r21.py"""
import pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = CAND / 's13'
OUT = S13 / 'review-r22'
DRAFT = S13 / 'v32.md'
PREV = S13 / 'v31.md'
OUT.mkdir(exist_ok=True)
HEAD = '# Your Little Forming Group Already Is the Community'
py = sys.executable
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
ST = str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py')


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


orig = (CAND.parent / 'original.md').read_text(encoding='utf-8')
a = orig.index(HEAD)
b = orig.index('\n# ', a + 5)
pub = [x for x in blocks(orig[a:b]) if not x.startswith('<!--')]
so_far = (CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
sa = so_far.index(HEAD)
sb = so_far.index('\n# ', sa + 5)
before_section = [x for x in blocks(so_far[:sa]) if not x.startswith('<!--') and not x.startswith('#')][-1]
after_section = [x for x in blocks(so_far[sb:]) if not x.startswith('<!--') and not x.startswith('#')][:2]


def paras_by_heading(bs):
    out = []
    for x in bs:
        if x.startswith('#'):
            out.append((re.sub(r'^#+\s*', '', x), []))
        else:
            out[-1][1].append(x)
    return out


P = paras_by_heading(pub)
R = paras_by_heading(blocks(DRAFT.read_text(encoding='utf-8')))
assert [h for h, _ in P] == [h for h, _ in R]
MAP = [
    [([1], [1]), ([2, 3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6], [5])],
    [([1, 2], [1]), ([3], [2]), ([4, 5, 6], [3, 4]), ([7], [5])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6, 7], [5]), ([8], [6, 7]), ([9], [8]), ([10], [9])],
    [([1], [1]), ([2], [2]), ([3], [3]), ([4], [4])],
]
# what the dedup took out of a pair, and where the article says it (Joel, 2026-10-16 23:38 UTC: "let's merge/dedup ...
# without losing important things"); the tracer checks that the point is there, instead of reporting it lost
DEDUP = {
    'Your Little Forming Group Already Is the Community P6 → P4':
        'The failing well is cut here because section 12 ("The Math of Absorption, and Who This Isn\'t For") says it: "The '
        'water well doesn\'t care how beautiful the new member\'s heart is." The exhausted person stays here.',
    'Resources, Land, and Exit Terms P4+5+6 → P3+4':
        '"A money-free community still has scarce things" is cut here because section 4 ("The Four Parts That Have to '
        'Pl/ork Together", "4. The container") says it: "Even in a moneyless community, someone can control what\'s '
        'scarce." The exit resources moved from the first rewrite paragraph to the second, next to "That\'s coercive", so '
        'the paper right and the coercion are said once, side by side.',
    'From Visitor to Member—Slowly P1+2 → P1':
        '"Nobody benefits from joining a group that cannot support what it has promised" is cut here because section 5 '
        '("After the Psychedelic Calling") says a group can "recruit too quickly and promise too much", and section 12 '
        'asks "how many people can a group take in without hurting the existing members or the people they are taking in?"',
    'From Visitor to Member—Slowly P5 → P4':
        '"time gives you more evidence, not certainty" is cut here because two paragraphs later the same subsection says '
        '"Six months will give you more data, but there\'s still no "good person" detector."',
    'Resources, Land, and Exit Terms P7 → P5':
        'Joel asked (2026-10-16): "we should not lean on Christian\'s book order if it contradicts my own order". His order '
        'is in the section "Practice Comes Before Property": "Practice together. Process a real conflict. Clarify values. '
        'Test membership. Decide ownership and exit. Then consider land." The rewrite points to the book for the practical '
        'steps instead of its order; check that it no longer endorses the book\'s order and still recommends the book.',
}
flat_r = [(hi, j + 1) for hi, (_, ps) in enumerate(R) for j in range(len(ps))]
pairs = []
for hi, ((h, pps), (_, rps), m) in enumerate(zip(P, R, MAP)):
    assert sorted(x for pp, _ in m for x in pp) == list(range(1, len(pps) + 1)), h
    assert sorted(x for _, rr in m for x in rr) == list(range(1, len(rps) + 1)), h
    for pp, rr in m:
        first, last = flat_r.index((hi, rr[0])), flat_r.index((hi, rr[-1]))
        rtext = lambda k: R[flat_r[k][0]][1][flat_r[k][1] - 1]
        ctx_b = rtext(first - 1) if first > 0 else before_section
        ctx_a = rtext(last + 1) if last + 1 < len(flat_r) else after_section[0]
        if first > 0 and flat_r[first - 1][0] != hi:
            ctx_b = '(the heading "%s" comes between) ' % h + ctx_b
        elif first == 0:
            ctx_b = '(the end of the section before; this section starts with the heading "%s") ' % h + ctx_b
        name = '%s P%s → P%s' % (h, '+'.join(map(str, pp)), '+'.join(map(str, rr)))
        pairs.append(dict(name=name, pub='\n\n'.join(pps[k - 1] for k in pp), rew='\n\n'.join(R[hi][1][k - 1] for k in rr),
                          before=re.sub(r'\s+', ' ', ctx_b)[:400], after=re.sub(r'\s+', ' ', ctx_a)[:400]))
prev = blocks(PREV.read_text(encoding='utf-8'))
CHANGED = {'Your Little Forming Group Already Is the Community P4+5 → P3', 'Resources, Land, and Exit Terms P4+5+6 → P3+4',
           'Resources, Land, and Exit Terms P7 → P5', 'From Visitor to Member—Slowly P4 → P3',
           'From Visitor to Member—Slowly P8 → P6+7', 'From Visitor to Member—Slowly P9 → P8', 'When Somebody Has to Go P4 → P4'}
pairs = [p for p in pairs if p['name'] in CHANGED]
assert len(pairs) == len(CHANGED), [p['name'] for p in pairs]
brief = re.sub(r'<!--.*?-->\n*', '', (REPO / 'tools' / 'humanization' / 'reviewer' / 'trace_brief.md').read_text(encoding='utf-8'),
               flags=re.S)
groups = [pairs[i:i + 2] for i in range(0, len(pairs), 2)]
for n, g in enumerate(groups, start=1):
    inp = OUT / ('trace-in-T%d.md' % n)
    lines = ['# Section 13 pairs (T%d): published paragraph and rewrite' % n, '',
             'Section 13 is "Your Little Forming Group Already Is the Community", with four subheadings. The rewrite keeps '
             'the published order and headings; a pair shows all the published paragraphs a rewrite paragraph carries. The '
             'rewrite is deliberately loose and spoken (short reactions, run-on lists, "etc."); judge what it says, not its '
             'polish. Where a pair has a DEDUP NOTE, the author asked for repeats to be cut: a point the note names is said '
             'where the note says, so check that claim instead of reporting the point as lost here.', '']
    for p in g:
        lines += ['## ' + p['name'], '', 'CONTEXT BEFORE: ' + p['before'], '', 'PUBLISHED:', '', p['pub'], '',
                  'REWRITE:', '', p['rew'], '', 'CONTEXT AFTER: ' + p['after'], '']
        if p['name'] in DEDUP:
            lines += ['DEDUP NOTE: ' + DEDUP[p['name']], '']
    inp.write_text('\n'.join(lines), encoding='utf-8')
    prompt = (brief.replace('{what}', 'community section 13 ("Your Little Forming Group Already Is the Community"), '
                                      'pairs %d to %d of %d' % (pairs.index(g[0]) + 1, pairs.index(g[-1]) + 1, len(pairs)))
                   .replace('{input}', str(inp)).replace('{report}', str(OUT / ('trace-T%d.md' % n)))
                   .replace('{words}', str(200 * len(g) + 150)))
    (OUT / ('TRACE-PROMPT-T%d.txt' % n)).write_text(prompt, encoding='utf-8')
print(len(pairs), 'pairs in', len(groups), 'trace runs:', [[p['name'] for p in g] for g in groups])
