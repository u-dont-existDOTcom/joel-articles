"""The repeats check for Joel's 01:29 texts in section 2 (56 a, 55 b): the article with section 2 v3.6c and section 12 v16
(article-with-0129.md), and a prompt that takes only what's new since the 23:10 report (REPEATS-s2b.md, answered in
fix-20261017d/DISPOSITIONS-2310.md) against the whole article: his new first paragraph and his new aside.
Run from candidate/: python3 fix-20261018/make_repeats_0129.py"""
import pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
H2, H12 = '# Communes Are Hot Again', '# The Math of Absorption, and Who This Isn’t For'


def put(md, h1, new):
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return md[:a] + new.strip() + '\n' + md[a + 3 + m.start():]


art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
art = put(art, H2, (HERE / 's2-v36c.md').read_text(encoding='utf-8'))
art = put(art, H12, (C / 'fix-20261017d' / 's12-v16.md').read_text(encoding='utf-8'))
(HERE / 'article-with-0129.md').write_text(art, encoding='utf-8')
out = HERE / 'REPEATS-PROMPT-s2c.txt'
subprocess.run([sys.executable, str(REPO / 'tools/humanization/reviewer/reviewer.py'), 'repeats', str(out), '--article',
                str(HERE / 'article-with-0129.md'), '--focus', '"Communes Are Hot Again 🔥"', '--only', '--report',
                'articles/intentional-communities/candidate/fix-20261018/REPEATS-s2c.md'], check=True, cwd=REPO)
t = out.read_text(encoding='utf-8')
a = t.index('WHERE TO LOOK HARDEST')
b = t.index('OUTPUT', a)
NEW = ('WHERE TO LOOK\n\n'
       'Only two things are new, both in section "Communes Are Hot Again 🔥": its first paragraph, "Suddenly, the longing to escape '
       'loneliness which inspired my father’s movie, is everywhere again. Back in 2023, ironically, just the year after Covid '
       'lockdowns ended, the U.S. Surgeon General even put out an advisory, saying roughly half of American adults experience '
       'loneliness, and it treated social connection as a public-health issue.", and the aside in its second paragraph, "(the '
       'UN\'s rules for prisoners literally ban more than 15 days of it)". The rest of the article was checked for repeats '
       'earlier, so check only these: does either make the same point as anything else in the article (in its own section or '
       'any other), and does either contradict anything? Search the whole article for loneliness, isolation, the Surgeon '
       'General, Covid, lockdowns, prison, solitary confinement and torture, and compare each hit with them.\n\n')
t = t[:a] + NEW + t[b:]
o = re.search(r'1\. A numbered list of repeats.*?\n\n', t, flags=re.S).group(0)
t = t.replace(o, '1. A numbered list of repeats that involve the new paragraph or the new aside, in article order. For each: the '
              'block numbers; a short exact quote from each instance (under 25 words each); the shared point in a few words; '
              'whether the later instance adds something the earlier one doesn\'t (say what) or a reader would feel told the same '
              'thing again; and which instance carries the point better or sits in the more natural place, with a one-line '
              'reason. If there are none, say so.\n'
              '2. Contradictions that involve them, the same way, or "none".\n'
              '3. The closest near-misses you rejected (up to three), each with its block number and a one-line reason it isn\'t a '
              'repeat.\n\n')
t = re.sub(r'3\. The five repeats a reader would most notice, by number\.\n\n', '', t)
t = t.replace('keep the whole report under 1,500 words', 'keep the whole report under 500 words')
t = t.replace('Find the repeats in a long article.', 'Check two new passages of a long article for repeats.', 1)
assert 'WHERE TO LOOK HARDEST' not in t and t.count('OUTPUT') == 1
out.write_text(t, encoding='utf-8')
print(out, len(t.split()), 'words')
