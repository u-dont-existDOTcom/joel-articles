"""Section 16, a meaning-review round on a draft (2026-10-17): the meaning traces of the published paragraphs against their
rewrites (two pairs per trace run, each with the paragraph before and after for context, and a DEDUP NOTE where the dedup
left a point to another section, so the trace checks that claim instead of reporting it lost), one cold read of the section in
the article so far, and the stance check against the published essay with Joel's later positions. The published text is
v0.md. Run it for the paragraphs whose screens read Human (E175). Writes the prompts into the round's folder.
Run from the repo root: python3 articles/intentional-communities/candidate/s16/make_gate.py DRAFT ROUND [PID ...]"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
S16 = pathlib.Path(__file__).resolve().parent
DRAFT = S16 / (sys.argv[1] + '.md')
OUT = S16 / sys.argv[2]
OUT.mkdir(exist_ok=True)
SKIP = re.compile(r'^(#|\[image \d+\]|\[caption\])')
PUB_IDS = ['H1-P%d' % i for i in range(1, 4)] + ['H2-P%d' % i for i in range(1, 7)] + ['H3-P%d' % i for i in range(1, 12)]
REW_IDS = [p for p in PUB_IDS if p != 'H3-P1']   # H3-P1, the lead-in, went in the dedup (repeats r1 item 10)
HEAD = {'H1': 'Practice Comes Before Property', 'H2': 'If You Can’t Move', 'H3': 'What to Do This Month'}
H = '# Practice Comes Before Property'
py = sys.executable
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
ST = str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py')
DEDUP = {
 'H1-P3': 'The first stage (households that stop buying the basics among themselves while outside earners contribute a defined '
          'share) is not repeated here: section 4, "The container", says it in the author\'s own words ("First there will be no '
          'money exchanged between members for basic community functions ... they bring an agreed share of that income in"). '
          'Check that the rest of the published paragraph is here.',
 'H2-P4': '"already contains a real piece of community" is not repeated here: section 13 opens with it ("you are already a '
          'community, even if it\'s still an untested one"). Check that the rest of the published paragraph is here.',
 'H3-P2': 'The published H3-P1, the lead-in "Here is the first month without the heroic land purchase:", is cut: the section '
          'says land can wait four other times, and the heading already says "This Month". Trace only the published H3-P2.',
 'H3-P8': '"I\'m in Sénégal and expect to buy land, but I\'m not announcing a commune." is not repeated here: section 2 says it '
          '("I am not currently recruiting anyone or founding a community ... I do plan to buy land"). Check the rest.',
 'H3-P9': '"He made a film, founded a research organization, and carried me through communal experiments." is not repeated '
          'here: section 14 says it ("It shaped the foundation he started and the film he made. It shaped the places he took '
          'me"), and section 1 tells it in full. Check the rest.',
}


def prose(path, ids):
    bl = [b.strip() for b in re.split(r'\n\s*\n', path.read_text(encoding='utf-8')) if b.strip()]
    ps = [b for b in bl if not SKIP.match(b)]
    assert len(ps) == len(ids), (path, len(ps), len(ids))
    return dict(zip(ids, ps))


PUB, NEW = prose(S16 / 'v0.md', PUB_IDS), prose(DRAFT, REW_IDS)
want = sys.argv[3:] or REW_IDS
pairs = []
for pid in want:
    i = REW_IDS.index(pid)
    before = NEW[REW_IDS[i - 1]] if i > 0 and REW_IDS[i - 1][:2] == pid[:2] else '(the heading "%s" comes before)' % HEAD[pid[:2]]
    after = NEW[REW_IDS[i + 1]] if i + 1 < len(REW_IDS) and REW_IDS[i + 1][:2] == pid[:2] else '(the next heading follows)'
    pub = PUB[pid] if pid != 'H3-P2' else PUB['H3-P1'] + '\n\n' + PUB['H3-P2']
    pairs.append(dict(name='%s %s' % (HEAD[pid[:2]], pid), pid=pid, pub=pub, rew=NEW[pid], note=DEDUP.get(pid),
                      before=re.sub(r'\s+', ' ', before)[:400], after=re.sub(r'\s+', ' ', after)[:400]))
brief = re.sub(r'<!--.*?-->\n*', '', (REPO / 'tools' / 'humanization' / 'reviewer' / 'trace_brief.md').read_text(encoding='utf-8'),
               flags=re.S)
groups = [pairs[k:k + 2] for k in range(0, len(pairs), 2)]
index = {}
for n, g in enumerate(groups, start=1):
    inp = OUT / ('trace-in-T%d.md' % n)
    lines = ['# Section 16 pairs (T%d): published paragraph and rewrite' % n, '',
             'Section 16 is "Practice Comes Before Property", the article\'s last section before the appendix, with two '
             'subheadings ("If You Can’t Move", "What to Do This Month"). The author lives in Sénégal. The rewrite keeps the '
             'published order and headings, one rewrite paragraph per published paragraph. It is deliberately loose and spoken '
             '(short reactions, questions, run-on lists, "etc."); a short reaction or question that claims nothing about the '
             'world is there on purpose as the paragraph\'s pause, so report it as ADDED only if it states something new. The '
             'author asked for repeats across the article to be cut: where a pair has a DEDUP NOTE, check that the cut point is '
             'said where the note says instead of reporting it lost. Judge what the rewrite says, not its polish.', '']
    for p in g:
        lines += ['## ' + p['name'], '', 'CONTEXT BEFORE: ' + p['before'], '', 'PUBLISHED:', '', p['pub'], '', 'REWRITE:', '',
                  p['rew'], '', 'CONTEXT AFTER: ' + p['after'], '']
        if p['note']:
            lines += ['DEDUP NOTE: ' + p['note'], '']
    inp.write_text('\n'.join(lines), encoding='utf-8')
    (OUT / ('TRACE-PROMPT-T%d.txt' % n)).write_text(
        brief.replace('{what}', 'community section 16 ("Practice Comes Before Property"), pairs %d of %d' % (n, len(groups)))
             .replace('{input}', str(inp)).replace('{report}', str(OUT / ('trace-T%d.md' % n)))
             .replace('{words}', str(350 + 250 * len(g))), encoding='utf-8')
    index['T%d' % n] = [p['pid'] for p in g]
(OUT / 'traces.json').write_text(json.dumps(index) + '\n', encoding='utf-8')
subprocess.run([py, RV, '--article', str(CAND / 'HUMANIZED-SO-FAR.md'), 'sense-section', str(OUT / 'SENSE-PROMPT-a.txt'),
                '--section', H, '--draft', str(DRAFT), '--report', str(OUT / 'SENSE-a.md')], check=True)
subprocess.run([py, ST, '--essay', str(CAND.parent / 'original.md'), '--rewrite', str(DRAFT),
                '--out', str(OUT / 'STANCE-PROMPT-pub.txt'), '--scope', 'section 16 ("Practice Comes Before Property"), rewritten',
                '--topic', 'building intentional communities', '--report', str(OUT / 'STANCE-pub.md'),
                '--images', str(CAND / 'images.json'), '--positions', str(CAND / 's15' / 'positions.txt')], check=True)
print('prompts in', OUT, index)
