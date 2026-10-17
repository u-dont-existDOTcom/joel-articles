"""Joel's message of 2026-10-17 23:10 UTC (joel-20261017/joel-20261017-2310-message.txt):
- 52 a: his section 2 opening as he wrote it ("this is human"): P1 ("Suddenly the longing to escape loneliness which inspired my
  father's movie ...") with the published link on "the U.S. Surgeon General" kept (his text is plain; the published article and
  every version since carry the link), and P2 with his 53 aside ("(it's literally listed in the UN Convention Against Torture)")
  and "Folks may disagree" for "They may disagree". The Google Trends paragraph after them is unchanged.
- 46 a stands (the anomie paragraph after his P2, with his screenshot and caption moved there from section 12, once section 2
  reads 100% Human with it), so section 2 is built three ways: v3.5 as he pasted it (no anomie paragraph; the screenshot stays in
  section 12), v3.5b with the anomie paragraph, v3.5c with the anomie paragraph and the screenshot and caption (section 12 v16).
- 54: section 8's truthfulness paragraph with his sentence after "Make sure kids understand what they say will be taken
  seriously if they are known to be honest.": "And those who are known to lie a lot are especially targeted by abusers who know
  their accusations won't be believed."
Writes fix-20261017d/s2-v35.md, s2-v35b.md, s2-v35c.md, s8-v32.md and article-with-2310.md (the article with v3.5c, section 12
v16 and section 8 v32, for the repeats checks). Run from candidate/: python3 fix-20261017d/make_2310.py"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H2 = '# Communes Are Hot Again 🔥'
H8 = '# The Grown Children Get the Final Review'
H12 = '# The Math of Absorption, and Who This Isn’t For'


def block(md, h1):
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return md[a:a + 3 + m.start()].strip() + '\n'


def swap(text, old, new, n=1):
    assert text.count(old) == n, (old[:70], text.count(old))
    return text.replace(old, new)


LINK = '[the U.S. Surgeon General](https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf)'
P1_OLD = ('Suddenly the longing behind my father’s movie is everywhere again, and in 2023 %s even put out an advisory about it. Or about '
          'the loneliness under it, at least. The advisory said roughly half of American adults experience loneliness, and it treated '
          'social connection as a public-health issue.' % LINK)
P1_NEW = ('Suddenly the longing to escape loneliness which inspired my father’s movie is everywhere again, and in 2023 %s even put out '
          'an advisory, saying roughly half of American adults experience loneliness, and it treated social connection as a public-health '
          'issue.' % LINK)
P2_OLD = ('Whether you want to call that loneliness an official “epidemic” or not, it’s obvious that a lot of people can’t tolerate '
          'modern life in isolation anymore. They may disagree about politics, food, God, sex, or whether shoes are oppressive, but '
          'they agree that something about the current arrangement is starvin’ them.')
P2_NEW = ('Whether you want to call that loneliness an official “epidemic” or not, it’s obvious that a lot of people can’t tolerate '
          'modern life in isolation anymore (it\'s literally listed in the UN Convention Against Torture). Folks may disagree about '
          'politics, food, God, sex, or whether shoes are oppressive, but they agree that something about the current arrangement is '
          'starving them.')
s2 = swap(swap(block(ART, H2), P1_OLD, P1_NEW), P2_OLD, P2_NEW)
(HERE / 's2-v35.md').write_text(s2, encoding='utf-8')
src = (HERE / 'make_2137.py').read_text(encoding='utf-8')
ns = {}
i = src.index('ANOMIE = ('); j = src.index(')\n', i)
exec(src[i:j + 1], ns)
ANOMIE = ns['ANOMIE']
(HERE / 's2-v35b.md').write_text(swap(s2, P2_NEW, P2_NEW + '\n\n' + ANOMIE), encoding='utf-8')
v34 = (HERE / 's2-v34.md').read_text(encoding='utf-8')
k = v34.index(ANOMIE) + len(ANOMIE)
img_block = v34[k:v34.index('<!-- CANDIDATE', k) if '<!-- CANDIDATE' in v34[k:] else v34.index('\n\nCheck out the Google Trends', k)]
assert 'psypost-relational-mobility.png' in img_block and '[caption]' in img_block, img_block[:200]
v35c = swap(s2, P2_NEW, P2_NEW + '\n\n' + ANOMIE + img_block.rstrip('\n'))
(HERE / 's2-v35c.md').write_text(v35c, encoding='utf-8')
S8_OLD = 'Make sure kids understand what they say will be taken seriously if they are known to be honest.'
S8_NEW = (S8_OLD + ' And those who are known to lie a lot are especially targeted by abusers who know their accusations won\'t be '
          'believed.')
s8 = swap(block(ART, H8), S8_OLD, S8_NEW)
(HERE / 's8-v32.md').write_text(s8, encoding='utf-8')
new = ART
for h1, text in ((H2, v35c), (H8, s8), (H12, (HERE / 's12-v16.md').read_text(encoding='utf-8'))):
    a = new.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', new[a + 3:])
    new = new[:a] + text.strip() + '\n' + new[a + 3 + m.start():]
(HERE / 'article-with-2310.md').write_text(new, encoding='utf-8')
print('written: s2-v35, s2-v35b, s2-v35c, s8-v32, article-with-2310')
