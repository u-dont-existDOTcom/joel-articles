"""Section 13, gate round r19 on v29, the other meaning reviews (2026-10-16): two cold reads of v29 in the article, the stance
check against the published essay and against the article so far, and the repeats check of the assembled section (E172). Run
from the repo root: python3 articles/intentional-communities/candidate/s13/make_gate_r19b.py"""
import pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = CAND / 's13'
OUT = S13 / 'review-r19'
DRAFT = S13 / 'v29.md'
HEAD = '# Your Little Forming Group Already Is the Community'
py = sys.executable
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
ST = str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py')
art = str(CAND / 'HUMANIZED-SO-FAR.md')
owner = OUT / 'owner.md'
owner.write_text("So work out the process before it's about anyone in particular.\n\n"
                 "[My research](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) initially leaned too "
                 "far that way.\n\n(Hint: not the person who recruited them! 😜)\n", encoding='utf-8')
for x in 'ab':
    subprocess.run([py, RV, '--article', art, 'sense-section', str(OUT / ('SENSE-PROMPT-%s.txt' % x)), '--section', HEAD,
                    '--draft', str(DRAFT), '--report', str(OUT / ('SENSE-%s.md' % x))], check=True)
for tag, essay in (('pub', str(CAND.parent / 'original.md')), ('sofar', art)):
    subprocess.run([py, ST, '--essay', essay, '--rewrite', str(DRAFT), '--out', str(OUT / ('STANCE-PROMPT-%s.txt' % tag)),
                    '--scope', 'section 13 ("Your Little Forming Group Already Is the Community"), rewritten',
                    '--topic', 'building intentional communities', '--report', str(OUT / ('STANCE-%s.md' % tag)),
                    '--images', str(CAND / 'images.json'), '--positions', str(S13 / 'positions.txt'),
                    '--owner', str(owner)], check=True)
subprocess.run([py, str(S13 / 'article_with.py'), str(DRAFT), str(OUT / 'article-with-v29.md')], check=True)
subprocess.run([py, RV, '--article', str(OUT / 'article-with-v29.md'), 'repeats', str(OUT / 'REPEATS-PROMPT.txt'),
                '--focus', '"%s"' % HEAD[2:], '--only', '--report', str(OUT / 'REPEATS.md')], check=True)
print('prompts in', OUT)
