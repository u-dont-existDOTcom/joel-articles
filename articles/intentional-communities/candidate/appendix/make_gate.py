"""The appendix, a meaning-review round on a draft (2026-10-17): the meaning traces of the published entries against their
rewrites (five pairs per trace run: the entries are one or two sentences each), one cold read of the appendix in the article
so far, and the stance check against the published essay with Joel's later positions. The published text is v0.md; three
changes since are authorized (v1: Joel's of 2026-10-16 23:38 UTC and two dedup cuts), and each pair that has one carries a
NOTE so the trace checks the rest instead of reporting it lost. Run it for the entries whose screens read Human (E175).
Run from the repo root: python3 articles/intentional-communities/candidate/appendix/make_gate.py DRAFT ROUND [N ...]
(N: entry numbers, 1 to 25; none: every entry)"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
APX = pathlib.Path(__file__).resolve().parent
DRAFT = APX / (sys.argv[1] + '.md')
OUT = APX / sys.argv[2]
OUT.mkdir(exist_ok=True)
H = '# Appendix: Watch These, Then Read These'
py = sys.executable
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
ST = str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py')
NOTE = {
 1: 'v1 cut "and now online" (a dedup: section 1 says the film is online, and the entry links it). Check the rest.',
 9: 'v1 cut "My father lived there for 17 years." (a dedup: sections 1 and 4 say it). Check the rest.',
 13: 'v1 cut "sequencing" from what the book is the place to start for, by the author\'s ruling of 2026-10-16 ("we should '
     'not lean on Christian\'s book order if it contradicts my own order"; his order is section 16\'s). Check the rest.',
}


def entries(path):
    """[(heading, entry)] in order: every block that isn't a heading"""
    out, head = [], None
    for b in re.split(r'\n\s*\n', path.read_text(encoding='utf-8')):
        b = b.strip()
        if not b:
            continue
        if b.startswith('#'):
            head = b.lstrip('#').strip()
            continue
        out.append((head, b))
    return out


PUB, NEW = entries(APX / 'v0.md'), entries(DRAFT)
assert len(PUB) == len(NEW) == 25, (len(PUB), len(NEW))
assert [h for h, _ in PUB] == [h for h, _ in NEW]
want = [int(x) for x in sys.argv[3:]] or list(range(1, 26))
pairs = []
for n in want:
    i = n - 1
    head = NEW[i][0]
    before = NEW[i - 1][1] if i > 0 and NEW[i - 1][0] == head else '(the heading "%s" comes before)' % head
    after = NEW[i + 1][1] if i + 1 < len(NEW) and NEW[i + 1][0] == head else '(the next heading follows)'
    pairs.append(dict(name='%s, entry %d' % (head, n), pub=PUB[i][1], rew=NEW[i][1], note=NOTE.get(n),
                      before=re.sub(r'\s+', ' ', before)[:400], after=re.sub(r'\s+', ' ', after)[:400]))
brief = re.sub(r'<!--.*?-->\n*', '', (REPO / 'tools' / 'humanization' / 'reviewer' / 'trace_brief.md').read_text(encoding='utf-8'),
               flags=re.S)
groups = [pairs[k:k + 5] for k in range(0, len(pairs), 5)]
index = {}
for g_n, g in enumerate(groups, start=1):
    inp = OUT / ('trace-in-T%d.md' % g_n)
    lines = ['# Appendix pairs (T%d): published entry and rewrite' % g_n, '',
             'The appendix, "Watch These, Then Read These", is the reading list at the end of the author\'s article on '
             'building intentional communities: films, then books and papers under headings. The rewrite keeps the headings, '
             'the order, every title, author, year and link, one rewrite entry per published entry; it is deliberately loose '
             'and spoken, and a short question or reaction that claims nothing about the work is there on purpose as a pause, '
             'so report it as ADDED only if it states something new about the work or the author. What each entry says about '
             'its work is the meaning to check: what kind of work it is, what it covers, and any judgment the author makes of '
             'it. Where a pair has a NOTE, a change was authorized; check the rest instead of reporting it lost. Judge what the '
             'rewrite says, not its polish.', '']
    for p in g:
        lines += ['## ' + p['name'], '', 'CONTEXT BEFORE: ' + p['before'], '', 'PUBLISHED:', '', p['pub'], '', 'REWRITE:', '',
                  p['rew'], '', 'CONTEXT AFTER: ' + p['after'], '']
        if p['note']:
            lines += ['NOTE: ' + p['note'], '']
    inp.write_text('\n'.join(lines), encoding='utf-8')
    (OUT / ('TRACE-PROMPT-T%d.txt' % g_n)).write_text(
        brief.replace('{what}', 'the appendix of the community article ("Watch These, Then Read These"), pairs %d of %d'
                      % (g_n, len(groups)))
             .replace('{input}', str(inp)).replace('{report}', str(OUT / ('trace-T%d.md' % g_n)))
             .replace('{words}', str(250 + 120 * len(g))), encoding='utf-8')
    index['T%d' % g_n] = [p['name'] for p in g]
(OUT / 'traces.json').write_text(json.dumps(index, ensure_ascii=False) + '\n', encoding='utf-8')
subprocess.run([py, RV, '--article', str(CAND / 'HUMANIZED-SO-FAR.md'), 'sense-section', str(OUT / 'SENSE-PROMPT-a.txt'),
                '--section', H, '--draft', str(DRAFT), '--report', str(OUT / 'SENSE-a.md')], check=True)
subprocess.run([py, ST, '--essay', str(CAND.parent / 'original.md'), '--rewrite', str(DRAFT),
                '--out', str(OUT / 'STANCE-PROMPT-pub.txt'), '--scope', 'the appendix ("Watch These, Then Read These"), rewritten',
                '--topic', 'building intentional communities', '--report', str(OUT / 'STANCE-pub.md'),
                '--images', str(CAND / 'images.json'), '--positions', str(CAND / 's15' / 'positions.txt')], check=True)
print('prompts in', OUT, index)
