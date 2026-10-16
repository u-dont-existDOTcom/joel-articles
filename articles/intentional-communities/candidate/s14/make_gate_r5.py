"""Section 14, gate round r5 on v3 (2026-10-16): the meaning reviews for the words v3 changed, after batch 303g read the
endings W2 and W3 Human in every group (P6 with P7, P5 to P7, the whole section). Traces on the pairs v3 changed: P1 and P2
(T1), and P5, P6 and P7 with ending W2 (T2); ending W3's P6 and P7 (T3) in case W2's need a fix that loses its Human read.
Two cold reads of v3 with ending W2. The stance checks and the repeats check of round r3 stand: v3 puts published words back
and its endings make the same claims (review-r3/DISPOSITIONS-r3.md). Run from the repo root:

  python3 articles/intentional-communities/candidate/s14/make_gate_r5.py

Writes s14/review-r5/."""
import pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
S14 = CAND / 's14'
OUT = S14 / 'review-r5'
OUT.mkdir(exist_ok=True)
DRAFT = S14 / 'v3-W2.md'
DRAFT3 = S14 / 'v3-W3.md'
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
rew3 = [x for x in blocks(DRAFT3.read_text(encoding='utf-8')) if not x.startswith('#') and not x.startswith('[image')]
groups = [([0, 1], rew), ([4, 5, 6], rew), ([5, 6], rew3)]
for n, (g, rew) in enumerate(groups, start=1):
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
print('prompts in', OUT)
