"""Section 15, a meaning-review round on a draft (2026-10-17): the meaning traces of published paragraphs against their
rewrites (two pairs per trace run, each with the paragraph before and after for context), one cold read of the section in the
article so far, the stance check against the published essay with Joel's later positions, and the repeats check of the
article with the draft in place (E172). Run it for the paragraphs whose screens read Human (E175). The published text is
v0.md (the section as it stands in the article). Writes the prompts into the round's folder.
Run from the repo root: python3 articles/intentional-communities/candidate/s15/make_gate.py DRAFT ROUND [PID ...]
e.g. make_gate.py v3 review-r4 H1-P4 H2-P1 ...   (no PIDs: every paragraph the draft changes)"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
S15 = pathlib.Path(__file__).resolve().parent
DRAFT = S15 / (sys.argv[1] + '.md')
OUT = S15 / sys.argv[2]
OUT.mkdir(exist_ok=True)
SKIP = re.compile(r'^(#|\[image \d+\]|\[caption\]|\[Professor Baby Sheep|Double click to interact with video)')
IDS = ['H1-P%d' % i for i in range(1, 6)] + ['H2-P%d' % i for i in range(1, 8)] + ['H3-P%d' % i for i in range(1, 9)]
HEAD = {'H1': 'What This Looks Like From Sénégal', 'H2': 'All is not well in paradise', 'H3': 'Lessons from the Black Tax'}
H = '# What This Looks Like From Sénégal'
py = sys.executable
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
ST = str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py')


def prose(path):
    bl = [b.strip() for b in re.split(r'\n\s*\n', path.read_text(encoding='utf-8')) if b.strip()]
    ps = [b for b in bl if not SKIP.match(b)]
    assert len(ps) == len(IDS), (path, len(ps))
    return dict(zip(IDS, ps))


PUB, NEW = prose(S15 / 'v0.md'), prose(DRAFT)
want = sys.argv[3:] or [p for p in IDS if PUB[p] != NEW[p]]
pairs = []
for pid in want:
    i = IDS.index(pid)
    before = NEW[IDS[i - 1]] if i > 0 and IDS[i - 1][:2] == pid[:2] else '(the heading "%s" comes before)' % HEAD[pid[:2]]
    after = NEW[IDS[i + 1]] if i + 1 < len(IDS) and IDS[i + 1][:2] == pid[:2] else '(the next heading follows)'
    pairs.append(dict(name='%s %s' % (HEAD[pid[:2]], pid), pid=pid, pub=PUB[pid], rew=NEW[pid],
                      before=re.sub(r'\s+', ' ', before)[:400], after=re.sub(r'\s+', ' ', after)[:400]))
brief = re.sub(r'<!--.*?-->\n*', '', (REPO / 'tools' / 'humanization' / 'reviewer' / 'trace_brief.md').read_text(encoding='utf-8'),
               flags=re.S)
groups = [pairs[k:k + 2] for k in range(0, len(pairs), 2)]
index = {}
for n, g in enumerate(groups, start=1):
    inp = OUT / ('trace-in-T%d.md' % n)
    lines = ['# Section 15 pairs (T%d): published paragraph and rewrite' % n, '',
             'Section 15 is "What This Looks Like From Sénégal", with two subheadings ("All is not well in paradise", "Lessons from '
             'the Black Tax"). The author lives in Sénégal and stays in a friend\'s family house. The rewrite keeps the published '
             'order and headings, one rewrite paragraph per published paragraph. It is deliberately loose and spoken (short '
             'reactions, questions, run-on lists, "etc."); a short reaction or question that claims nothing about the world is '
             'there on purpose as the paragraph\'s pause, so report it as ADDED only if it states something new. Judge what the '
             'rewrite says, not its polish.', '']
    for p in g:
        lines += ['## ' + p['name'], '', 'CONTEXT BEFORE: ' + p['before'], '', 'PUBLISHED:', '', p['pub'], '', 'REWRITE:', '',
                  p['rew'], '', 'CONTEXT AFTER: ' + p['after'], '']
    inp.write_text('\n'.join(lines), encoding='utf-8')
    words = 350 + 250 * len(g)
    (OUT / ('TRACE-PROMPT-T%d.txt' % n)).write_text(
        brief.replace('{what}', 'community section 15 ("What This Looks Like From Sénégal"), pairs %d of %d'
                      % (n, len(groups))).replace('{input}', str(inp)).replace('{report}', str(OUT / ('trace-T%d.md' % n)))
             .replace('{words}', str(words)), encoding='utf-8')
    index['T%d' % n] = [p['pid'] for p in g]
(OUT / 'traces.json').write_text(json.dumps(index) + '\n', encoding='utf-8')
subprocess.run([py, RV, '--article', str(CAND / 'HUMANIZED-SO-FAR.md'), 'sense-section', str(OUT / 'SENSE-PROMPT-a.txt'),
                '--section', H, '--draft', str(DRAFT), '--report', str(OUT / 'SENSE-a.md')], check=True)
subprocess.run([py, ST, '--essay', str(CAND.parent / 'original.md'), '--rewrite', str(DRAFT),
                '--out', str(OUT / 'STANCE-PROMPT-pub.txt'), '--scope', 'section 15 ("What This Looks Like From Sénégal"), rewritten',
                '--topic', 'building intentional communities', '--report', str(OUT / 'STANCE-pub.md'),
                '--images', str(CAND / 'images.json'), '--positions', str(S15 / 'positions.txt')], check=True)
art = (CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = art.index(H)
m = re.search(r'\n# ', art[a + 5:])
b = a + 5 + m.start() if m else len(art)
(OUT / ('article-with-%s.md' % sys.argv[1])).write_text(art[:a] + DRAFT.read_text(encoding='utf-8').strip() + '\n' + art[b:],
                                                       encoding='utf-8')
subprocess.run([py, RV, '--article', str(OUT / ('article-with-%s.md' % sys.argv[1])), 'repeats', str(OUT / 'REPEATS-PROMPT.txt'),
                '--focus', '"%s"' % H[2:], '--only', '--report', str(OUT / 'REPEATS.md')], check=True)
print('prompts in', OUT, index)
