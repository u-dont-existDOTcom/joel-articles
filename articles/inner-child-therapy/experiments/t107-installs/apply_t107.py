#!/usr/bin/env python3
"""Turn 107: Joel's answers of 2026-10-25 00:24 UTC (experiments/t107-answers/JOEL-20261025-0024.md) into the article.

- 103.1: his own My Journey, word for word ("here's the fixed, fully green section"). His bypassing paragraph is second now,
  after "I used to preach", and his chat answers I had put in close to word for word (turns 43, 45 and 79) are rewritten
  in his own article sentences.
- 103.2: his own first three paragraphs of Not Every Hero Wears A Cape, word for word ("i fixed the section, it's all dark
  green now"). Make It Intentional, its heading, P4 and d3 stay as they are.
- 103.3 A: his acacia sentence stays as he wrote it. Nothing changes.
- 103.4 A: "But do notice if it progress is stagnating." is "But do notice if progress is stagnating."

His paste is plain text, so it has no links or italics. Each link and the two italic words go back on the same words they
were on. His paste puts some paragraphs on single line breaks inside a group; each line is its own paragraph here, as
the article had them (docs/REVIEW-MOVE-INLINE-DIFF-GATE.md: a single newline can be a paragraph break). Trailing spaces
at the ends of his lines are dropped, as in turn 106. The paragraphs replace the old ones in order, so the notes between
them stay where they were. Every replacement asserts that it finds its text exactly once.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
OLD = json.loads((HERE / 'OLD-SECTIONS.json').read_text(encoding='utf-8'))
HIS = json.loads((HERE / 'HIS-SECTIONS.json').read_text(encoding='utf-8'))
WHEN = 'Turn 107 (his answers of 2026-10-25 00:24 UTC, experiments/t107-answers/JOEL-20261025-0024.md)'
NOTE = '<!-- ' + WHEN + ': %s -->\n\n'

# The formatting a plain-text paste drops: (paragraph index, his words, the article's markdown for them)
FORMAT = {
    'journey': [
        (0, 'Buddhist enlightenment', '[Buddhist enlightenment](http://mindset.u-dont-exist.com/)'),
        (1, 'spiritual bypassing', '[spiritual bypassing](https://goenka.u-dont-exist.com/)'),
        (1, 'Dalai Lama as one example', '[Dalai Lama as one example](https://substack.com/@udontexist/note/c-245314772?r=5vdc6m)'),
        (2, 'Understandable:', '*Understandable*:'),
        (2, 'Unforgivable.', '*Unforgivable.*'),
        (5, 'Loving-kindness (metta) meditation', '[Loving-kindness (metta) meditation](http://love.u-dont-exist.com/)'),
        (6, 'Buddhist teachings—which, it turns out, also include inner-child self-love!',
         '[Buddhist teachings—which, it turns out, also include inner-child self-love!](https://substack.com/profile/355021294-u-dont-existcom/note/c-297324975)'),
        (6, 'loveyhuasca', '[loveyhuasca](http://soma.u-dont-exist.com/)'),
        (7, 'self-directed inner-child therapy', '[self-directed inner-child therapy](https://youtu.be/yEWFjODXJbI?si=IXUqrhExojOm6Itm)'),
    ],
    'hero': [],
}


def formatted(key):
    paras = list(HIS[key])
    for k, plain, md in FORMAT[key]:
        assert paras[k].count(plain) == 1, (key, k, plain)
        paras[k] = paras[k].replace(plain, md)
    return paras


def article_paragraphs():
    """His paragraphs as they go into the article, with their links and italics (used by the owner-edits script too)."""
    return {key: formatted(key) for key in HIS}


if __name__ == '__main__':
    s = ART.read_text(encoding='utf-8')

    def once(old, new):
        global s
        n = s.count(old)
        assert n == 1, (n, old[:90])
        s = s.replace(old, new)

    # Every old link is still in the new text, on the same words
    for key in HIS:
        old_links = sorted(l for p in OLD[key] for l in __import__('re').findall(r'\]\((http[^)]+)\)', p))
        new_links = sorted(l for p in formatted(key) for l in __import__('re').findall(r'\]\((http[^)]+)\)', p))
        assert old_links == new_links, (key, old_links, new_links)

    labels = {
        'journey': '103.1, his own My Journey, word for word ("here\'s the fixed, fully green section"; "you put in some of my things too verbatim"). His bypassing paragraph is second now. The links and the two italic words are back on the same words, since his paste is plain text, and each of his lines is its own paragraph, as the article had them',
        'hero': '103.2, his own first three paragraphs, word for word ("i fixed the section, it\'s all dark green now"). Make It Intentional and its two paragraphs stay as they were',
    }
    for key in ('journey', 'hero'):
        olds, news = OLD[key], formatted(key)
        assert len(olds) == len(news), (key, len(olds), len(news))
        for k, (old, new) in enumerate(zip(olds, news)):
            once('\n' + old + '\n', '\n' + (NOTE % labels[key] if k == 0 else '') + new + '\n')

    # 103.4 A
    once('But do notice if it progress is stagnating.', 'But do notice if progress is stagnating.')
    once('<!-- P4\'s last three sentences are Joel\'s, word for word (2026-10-06 19:04 UTC)',
         NOTE % '103.4 A: "if it progress" is "if progress" in P4 below' + '<!-- P4\'s last three sentences are Joel\'s, word for word (2026-10-06 19:04 UTC)')

    ART.write_text(s, encoding='utf-8')
    print('ok')
