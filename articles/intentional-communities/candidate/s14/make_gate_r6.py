"""Section 14, gate round r6 on v6 (2026-10-17): v6 is v5 deduplicated at Joel's word (2026-10-16 23:38 UTC: "let's
merge/dedup section 14 without losing important things pls"; make_v6.py). One lean round (E177, E178): the march of the whole
section (two readings), the meaning trace of the two pairs v6 changes (P2's questions; P5 with the old last paragraph merged
into it), one cold read of the section in the article, and the repeats check of the assembled section with section 13 v32 in
place too. No stance check: v6 adds no claim, it cuts a repeated question and moves one clause. Run from the repo root:
python3 articles/intentional-communities/candidate/s14/make_gate_r6.py"""
import pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
CAND = REPO / 'articles' / 'intentional-communities' / 'candidate'
S14 = CAND / 's14'
OUT = S14 / 'review-r6'
OUT.mkdir(exist_ok=True)
DRAFT = S14 / 'v6.md'
HEAD = '# Dissolution and Exit'
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
py = sys.executable


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


orig = (CAND.parent / 'original.md').read_text(encoding='utf-8')
a = orig.index(HEAD); b = orig.index('\n# ', a + 5)
pub = [x for x in blocks(orig[a:b]) if not x.startswith(('#', '[image'))]
rew = [x for x in blocks(DRAFT.read_text(encoding='utf-8')) if not x.startswith(('#', '[image'))]
assert len(pub) == 7 and len(rew) == 6, (len(pub), len(rew))
pairs = [
    ('Dissolution and Exit P2 → P2', pub[1], rew[1], rew[0], rew[2],
     'The second question about food, housing and care is cut (the first two questions ask who keeps people housed, fed '
     'and cared for); the question keeps its own part, the outside cash or benefits.'),
    ('Dissolution and Exit P5+P7 → P5', pub[4] + '\n\n' + pub[6], rew[4], rew[3], rew[5],
     'The published last paragraph ("Even after the legal entity ends, some of what people learned to give one another may '
     'continue.") told P5\'s opening point again; its own part, what people learned to give one another, is now in P5\'s '
     'first sentence, and the section ends on the father paragraph (CONTEXT AFTER).'),
]
brief = re.sub(r'<!--.*?-->\n*', '', (REPO / 'tools' / 'humanization' / 'reviewer' / 'trace_brief.md').read_text(encoding='utf-8'),
               flags=re.S)
inp = OUT / 'trace-in-T1.md'
lines = ['# Section 14 pairs (T1): published paragraph and rewrite', '',
         'Section 14 is "Dissolution and Exit". The rewrite keeps the published order; a pair shows all the published '
         'paragraphs a rewrite paragraph carries. The rewrite is deliberately loose and spoken; judge what it says, not its '
         'polish. Each pair has a DEDUP NOTE: the author asked for repeats to be cut, so check that the cut point is said '
         'where the note says instead of reporting it lost.', '']
for name, p, r, before, after, note in pairs:
    lines += ['## ' + name, '', 'CONTEXT BEFORE: ' + re.sub(r'\s+', ' ', before)[:400], '', 'PUBLISHED:', '', p, '',
              'REWRITE:', '', r, '', 'CONTEXT AFTER: ' + re.sub(r'\s+', ' ', after)[:400], '', 'DEDUP NOTE: ' + note, '']
inp.write_text('\n'.join(lines), encoding='utf-8')
(OUT / 'TRACE-PROMPT-T1.txt').write_text(
    brief.replace('{what}', 'community section 14 ("Dissolution and Exit"), pairs 1 to 2 of 2').replace('{input}', str(inp))
         .replace('{report}', str(OUT / 'trace-T1.md')).replace('{words}', '550'), encoding='utf-8')
subprocess.run([py, RV, 'march', str(DRAFT), str(OUT / 'MARCH-PROMPT.txt'), '--about',
                'a blog article about building intentional communities'], check=True)
subprocess.run([py, RV, '--article', str(CAND / 'HUMANIZED-SO-FAR.md'), 'sense-section', str(OUT / 'SENSE-PROMPT-a.txt'),
                '--section', HEAD, '--draft', str(DRAFT), '--report', str(OUT / 'SENSE-a.md')], check=True)
art13 = (CAND / 's13' / 'review-r21' / 'article-with-v32.md').read_text(encoding='utf-8')
x = art13.index(HEAD); y = art13.index('\n# ', x + 5)
(OUT / 'article-with-s13v32-s14v6.md').write_text(art13[:x] + DRAFT.read_text(encoding='utf-8').strip() + '\n' + art13[y:],
                                                  encoding='utf-8')
subprocess.run([py, RV, '--article', str(OUT / 'article-with-s13v32-s14v6.md'), 'repeats', str(OUT / 'REPEATS-PROMPT.txt'),
                '--focus', '"%s"' % HEAD[2:], '--only', '--report', str(OUT / 'REPEATS.md')], check=True)
print('prompts in', OUT)
