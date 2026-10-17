"""Section 15, gate round r3 on v2 (2026-10-17): the meaning traces of every published paragraph against its rewrite, two
pairs per trace run, each with the paragraph before and after for context. Run them for the screens that read Human in 322g
first (E175); the published text is v0.md (the section as it stood in the article). Writes review-r3/TRACE-PROMPT-TN.txt and
trace-in-TN.md. Run from the repo root: python3 articles/intentional-communities/candidate/s15/make_gate_r3.py [PID ...]"""
import pathlib, re, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
S15 = pathlib.Path(__file__).resolve().parent
OUT = S15 / 'review-r3'
SKIP = re.compile(r'^(#|\[image \d+\]|\[caption\]|\[Professor Baby Sheep|Double click to interact with video)')
IDS = ['H1-P%d' % i for i in range(1, 6)] + ['H2-P%d' % i for i in range(1, 8)] + ['H3-P%d' % i for i in range(1, 9)]
HEAD = {'H1': 'What This Looks Like From Sénégal', 'H2': 'All is not well in paradise', 'H3': 'Lessons from the Black Tax'}


def prose(path):
    bl = [b.strip() for b in re.split(r'\n\s*\n', path.read_text(encoding='utf-8')) if b.strip()]
    ps = [b for b in bl if not SKIP.match(b)]
    assert len(ps) == len(IDS)
    return dict(zip(IDS, ps))


PUB, NEW = prose(S15 / 'v0.md'), prose(S15 / 'v2.md')
want = sys.argv[1:] or IDS
pairs = []
for pid in want:
    i = IDS.index(pid)
    before = NEW[IDS[i - 1]] if i > 0 and IDS[i - 1][:2] == pid[:2] else '(the heading "%s" comes before)' % HEAD[pid[:2]]
    after = NEW[IDS[i + 1]] if i + 1 < len(IDS) and IDS[i + 1][:2] == pid[:2] else '(the next heading follows)'
    pairs.append(dict(name='%s ("%s") %s' % (HEAD[pid[:2]], HEAD[pid[:2]], pid), pid=pid, pub=PUB[pid], rew=NEW[pid],
                      before=re.sub(r'\s+', ' ', before)[:400], after=re.sub(r'\s+', ' ', after)[:400]))
brief = re.sub(r'<!--.*?-->\n*', '', (REPO / 'tools' / 'humanization' / 'reviewer' / 'trace_brief.md').read_text(encoding='utf-8'), flags=re.S)
groups = [pairs[k:k + 2] for k in range(0, len(pairs), 2)]
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
    prompt = (brief.replace('{what}', 'community section 15 ("What This Looks Like From Sénégal"), pairs %s' % ', '.join(p['pid'] for p in g))
                   .replace('{input}', str(inp)).replace('{report}', str(OUT / ('trace-T%d.md' % n)))
                   .replace('{words}', str(200 * len(g) + 150)))
    (OUT / ('TRACE-PROMPT-T%d.txt' % n)).write_text(prompt, encoding='utf-8')
print(len(pairs), 'pairs in', len(groups), 'runs:', [[p['pid'] for p in g] for g in groups])
