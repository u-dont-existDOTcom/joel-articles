#!/usr/bin/env python3
"""Turn 109: Joel's answers of 2026-10-25 14:20 UTC (experiments/t109-answers/JOEL-20261025-1420.md) into the article.

- 105.1: his own end of How This Relates to IFS, in place of its last paragraph, word for word but for an obvious typo
  ("expalined" is "explained") and a doubled space. His friend Pink's account is the reason the readers found missing.
- 105.2: his own start of Use Childhood Photographs Gently ("this is the part that reads ai and it's actually redundant
  also"): P1 is his one sentence, and P2's first sentence is his two. "Pema Chodron's" is "Pema Chödrön's", as the article
  spells her name in its four other places, and a doubled space is one.
- 104 A: Hear the Guard First in the shape of experiments/t108-shape/DEMO.md (the plain path first, then one situation a
  paragraph), every sentence kept and used once, with two changes from the page: "When it lets you, keep an eye on that
  part too, for any change at all." stays at the end of the paragraph about letting it keep watch, so "it lets you" still
  follows "let you peek out", and "It might say" is "That part might say", since the sentence now opens its paragraph.
Every replacement asserts that it finds its text exactly once.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
WHEN = 'Turn 109 (his answers of 2026-10-25 14:20 UTC, experiments/t109-answers/JOEL-20261025-1420.md)'
NOTE = '<!-- ' + WHEN + ': %s -->\n\n'

IFS_OLD = ("And the parts just keep coming: managers, firefighters, exiles, polarized parts, legacy burdens, Self-energy, guides, new "
           "subparts... At some point it's a maze, with a little one somewhere in the middle of it. Some practitioners are gentle about "
           "it and walk you through the maze just fine. Others seem to leave people more split up than when they started. I wouldn't "
           "trust a model more just because there's a big institute behind it handing out certificates.")
IFS_NEW = ("And the parts just keep coming: managers, firefighters, exiles, polarized parts, legacy burdens, Self-energy, guides, new "
           "subparts... At some point it’s a maze, and as my friend Pink, who has been healing her Dissociative Identity Disorder, "
           "explained, while it can be useful to have validation of the parts that one experiences, and ideas for how to work with "
           "them, it can also get overwhelming. People who are already overwhelmed can thus become more split up than before. I've "
           "seen many others echo this same evaluation, and it makes sense to me.")
PH1_OLD = ("If picturing your little one feels fake, like you're just making it up, a real photo of you as a child can help, since "
           "there's no face or posture to invent. Yes, yes, it might feel a bit strange, seeing your own face from back then. But look "
           "at it gently and just notice what comes up.")
PH1_NEW = ("If picturing your little one feels like you’re just making them up, a real photo of you as a child can help, since "
           "there’s no face or posture to invent.")
PH2_OLD = "While you look, notice what your body does and what feelings or urges show up."
PH2_NEW = ("While you look, notice any new feelings or urges, and any tightness or unusual feelings in your body, including the good "
           "ones. Use Pema Chödrön's \"feather touch\" approach to gently bring some light and love to the edges of any contracted "
           "feelings.")


def guard_new(paras):
    """Hear the Guard First's five paragraphs in their new order: [(paragraph, sentence) ...] per new paragraph, 1-based."""
    def sents(p):
        return [s for s in re.split(r'(?<=[.!?"”)])\s+(?=[A-Z"“(])', p) if s]
    S = [sents(p) for p in paras]
    assert [len(x) for x in S] == [6, 8, 6, 11, 5], [len(x) for x in S]
    shape = [[(1, 1), (1, 5), (2, 3), (2, 4), (2, 5), (2, 6)],
             [(1, 2), (1, 3), (1, 4)],
             [(1, 6), (2, 1), (2, 2), (2, 7), (2, 8)],
             [(4, k) for k in range(1, 8)],
             [(4, k) for k in range(8, 12)],
             [(3, k) for k in range(1, 7)],
             [(5, k) for k in range(1, 6)]]
    used = sorted(x for xs in shape for x in xs)
    assert used == sorted((p + 1, k + 1) for p in range(5) for k in range(len(S[p])))
    out = [' '.join(S[p - 1][k - 1] for p, k in xs) for xs in shape]
    first = 'It might say this will just be one more performance, and you\'ll fool yourself again.'
    assert out[2].startswith(first)
    out[2] = 'That part might say' + out[2][len('It might say'):]
    return out


def main():
    s = ART.read_text(encoding='utf-8')

    def once(old, new):
        nonlocal s
        n = s.count(old)
        assert n == 1, (n, old[:90])
        s = s.replace(old, new)

    once('\n' + IFS_OLD + '\n', '\n' + NOTE % '105.1, his own end of the paragraph, word for word but for "explained" (his "expalined") and a doubled space' + IFS_NEW + '\n')
    once('\n' + PH1_OLD + '\n', '\n' + NOTE % '105.2, his own first sentence ("this is the part that reads ai and it\'s actually redundant also"), and his two sentences for the start of P2, with "Pema Chödrön\'s" for his "Pema Chodron\'s", as the article spells her name elsewhere, and a doubled space as one' + PH1_NEW + '\n')
    once('\n' + PH2_OLD + ' ', '\n' + PH2_NEW + ' ')

    # Hear the Guard First: its section, comments and all, from its heading to the next h3
    i = s.index('### Hear the Guard First')
    j = s.index('\n### ', i + 10)
    sec = s[i:j]
    reader = re.sub(r'<!--.*?-->', '', sec, flags=re.S)
    paras = [p.strip() for p in reader.split('\n\n')[1:] if p.strip()]
    new = guard_new(paras)
    for p in paras:
        assert sec.count('\n' + p + '\n') == 1, p[:60]
    notes = re.findall(r'<!--.*?-->', sec, flags=re.S)
    body = ('### Hear the Guard First\n\n' + '\n\n'.join(notes) + '\n\n'
            + NOTE % '104 A ("yes this makes it much more of a readable guide, good"): the section in the shape of experiments/t108-shape/DEMO.md, the plain path first and then one situation a paragraph, every sentence kept word for word and used once (apply_t109.py checks it), with "That part might say" for "It might say" now that the sentence opens a paragraph. The notes above are the paragraphs\' history from before the move'
            + '\n\n'.join(new) + '\n')
    s = s[:i] + body + s[j:]
    ART.write_text(s, encoding='utf-8')
    print('ok')
    for p in new:
        print(len(p.split()), '|', p[:90])


if __name__ == '__main__':
    main()
