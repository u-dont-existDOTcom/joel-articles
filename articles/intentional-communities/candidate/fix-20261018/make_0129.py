"""Joel's message of 2026-10-18 01:29 UTC (joel-20261018/joel-20261018-0129-message.txt):
- 56 a: his first paragraph for section 2, as he wrote it ("i checked the section, it passes as human when first part is
  this"), with the published link on "the U.S. Surgeon General" kept (every version since the published one carries it) and
  his bold on "public-health".
- 55 b: his aside in P2 becomes "(the UN's rules for prisoners literally ban more than 15 days of it)".
- 46 a stands, so section 2 is built three ways from the 23:10 versions: v3.6 as he pasted it (the screenshot stays in section
  12), v3.6b with the anomie paragraph after his P2, v3.6c with the anomie paragraph, his screenshot and caption (then section
  12 v16, which 421g read 100% Human).
Writes fix-20261018/s2-v36.md, s2-v36b.md, s2-v36c.md. Run from candidate/: python3 fix-20261018/make_0129.py"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OLD = HERE.parent / 'fix-20261017d'
LINK = '[the U.S. Surgeon General](https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf)'
P1_2310 = ('Suddenly the longing to escape loneliness which inspired my father’s movie is everywhere again, and in 2023 ' + LINK +
           ' even put out an advisory, saying roughly half of American adults experience loneliness, and it treated social connection '
           'as a public-health issue.')
P1_0129 = ('Suddenly, the longing to escape loneliness which inspired my father’s movie, is everywhere again. Back in 2023, ironically, '
           'just the year after Covid lockdowns ended, ' + LINK + ' even put out an advisory, saying roughly half of American adults '
           'experience loneliness, and it treated social connection as a **public-health** issue.')
ASIDE_2310 = "(it's literally listed in the UN Convention Against Torture)"
ASIDE_0129 = "(the UN's rules for prisoners literally ban more than 15 days of it)"
for a, b in (('s2-v35.md', 's2-v36.md'), ('s2-v35b.md', 's2-v36b.md'), ('s2-v35c.md', 's2-v36c.md')):
    t = (OLD / a).read_text(encoding='utf-8')
    assert t.count(P1_2310) == 1 and t.count(ASIDE_2310) == 1, a
    t = t.replace(P1_2310, P1_0129).replace(ASIDE_2310, ASIDE_0129)
    (HERE / b).write_text(t, encoding='utf-8')
    print(b, len(t.split()), 'words')
