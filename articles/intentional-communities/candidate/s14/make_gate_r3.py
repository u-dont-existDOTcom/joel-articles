"""Section 14, gate round r3 on v2 (2026-10-16): the meaning reviews for the screens that read Human in batch 301g (E175).
Traces on every pair (published paragraph -> v2 paragraph, one to one; P6 is Joel's father lines, nearly his published words);
two cold reads of v2 with the 2026-10-16 prompt (the opener rule and the "Paused:" line); both stance checks; and the repeats
check on the article with v2 in place (E172), section 14 first. The heading is the published one over the published claims,
so no grounding review. Run from the repo root:

  python3 articles/intentional-communities/candidate/s14/make_gate_r3.py

Writes s14/review-r3/."""
import pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
S14 = CAND / 's14'
OUT = S14 / 'review-r3'
OUT.mkdir(exist_ok=True)
DRAFT = S14 / 'v2.md'
HEAD = '# Dissolution and Exit'
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
ST = str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py')
py = sys.executable


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


so_far = (CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
a = so_far.index(HEAD)
b = so_far.index('\n# ', a + 5)
pub = [x for x in blocks(so_far[a:b]) if not x.startswith('<!--') and not x.startswith('#') and not x.startswith('[image')]
before = [x for x in blocks(so_far[:a]) if not x.startswith('<!--') and not x.startswith('#') and not x.startswith('[image')][-1]
after = [x for x in blocks(so_far[b:]) if not x.startswith('<!--') and not x.startswith('#') and not x.startswith('[image')][0]
rew = [x for x in blocks(DRAFT.read_text(encoding='utf-8')) if not x.startswith('#') and not x.startswith('[image')]
assert len(pub) == len(rew) == 7, (len(pub), len(rew))
brief = (REPO / 'tools' / 'humanization' / 'reviewer' / 'trace_brief.md').read_text(encoding='utf-8')
brief = re.sub(r'<!--.*?-->\n*', '', brief, flags=re.S)
groups = [[0, 1], [2, 3], [4, 5], [6]]
for n, g in enumerate(groups, start=1):
    lines = ['# Section 14 pairs (T%d): published paragraph and rewrite' % n, '',
             'Section 14 is "Dissolution and Exit", seven paragraphs. The rewrite keeps the published order, one rewrite '
             'paragraph for each published one. P6 is about the author\'s own father.', '']
    for k in g:
        cb = rew[k - 1] if k > 0 else '(the end of the section before; this section starts with the heading "Dissolution and Exit") ' + before
        ca = rew[k + 1] if k + 1 < len(rew) else '(the next section starts) ' + after
        lines += ['## P%d → P%d' % (k + 1, k + 1), '', 'CONTEXT BEFORE: ' + re.sub(r'\s+', ' ', cb)[:400], '', 'PUBLISHED:', '',
                  pub[k], '', 'REWRITE:', '', rew[k], '', 'CONTEXT AFTER: ' + re.sub(r'\s+', ' ', ca)[:400], '']
    inp = OUT / ('trace-in-T%d.md' % n)
    inp.write_text('\n'.join(lines), encoding='utf-8')
    prompt = (brief.replace('{what}', 'community section 14 ("Dissolution and Exit"), pairs %s' % ', '.join(str(k + 1) for k in g))
                   .replace('{input}', str(inp)).replace('{report}', str(OUT / ('trace-T%d.md' % n)))
                   .replace('{words}', str(200 * len(g) + 150)))
    (OUT / ('TRACE-PROMPT-T%d.txt' % n)).write_text(prompt, encoding='utf-8')
art = str(CAND / 'HUMANIZED-SO-FAR.md')
for x in 'ab':
    subprocess.run([py, RV, '--article', art, 'sense-section', str(OUT / ('SENSE-PROMPT-%s.txt' % x)), '--section', HEAD[2:],
                    '--draft', str(DRAFT), '--report', str(OUT / ('SENSE-%s.md' % x))], check=True)
for tag, essay in (('pub', str(CAND.parent / 'original.md')), ('sofar', art)):
    subprocess.run([py, ST, '--essay', essay, '--rewrite', str(DRAFT), '--out', str(OUT / ('STANCE-PROMPT-%s.txt' % tag)),
                    '--scope', 'section 14 ("Dissolution and Exit"), rewritten', '--topic', 'building intentional communities',
                    '--report', str(OUT / ('STANCE-%s.md' % tag)), '--images', str(CAND / 'images.json'),
                    '--positions', str(S14 / 'positions.txt')], check=True)
subprocess.run([py, str(S14 / 'article_with.py'), str(DRAFT), str(OUT / 'article-with-v2.md')], check=True)
subprocess.run([py, RV, '--article', str(OUT / 'article-with-v2.md'), 'repeats', str(OUT / 'REPEATS-PROMPT.txt'),
                '--focus', '"%s"' % HEAD[2:], '--only', '--report', str(OUT / 'REPEATS.md')], check=True)
print('prompts in', OUT)
