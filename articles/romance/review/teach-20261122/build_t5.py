#!/usr/bin/env python3
"""The fifth marking page (2026-11-22): the whole fixed article (whole/FIXED.md, his Medium-page answers in), with the
questions only he can answer on his own words, under the paragraphs they are about. The first page built under lesson
romance-2026-11-22a: the whole article, every block in order, its pictures and videos as boxes with their links.

  python3 build_t5.py   ->  REVIEW-T5.json, REVIEW-T5.html, REVIEW-T5.artifact.html, REVIEW-T5.md
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as R  # noqa: E402

ART = 'articles/romance/humanize/fix-20261107/whole/FIXED.md'
md = (ROOT / ART).read_text(encoding='utf-8')
sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
bl = R.blocks(md, whole=True)


def span(words):
    hits = [(b['i'], b['text'].find(words)) for b in bl if b['kind'] not in ('embed', 'cut') and words in b['text']]
    assert len(hits) == 1, (words, hits)
    i, s = hits[0]
    return {'block': i, 'start': s, 'end': s + len(words)}


QUESTIONS = [
    {'id': 'Q-14', 'words': 'pressuring men into making it look like they know what they want',
     'title': 'Who is "they" here?',
     'question': 'In your new sentence "Women are kind of notorious for proudly not knowing what they want, and pressuring '
                 'men into making it look like they know what they want", the second "they" can be read as the men or as '
                 'the women. Which do you mean? My reading: the men are pushed to act as if they know what she wants. If '
                 'so, it could say "and pressuring men to act like they know what she wants." Your words go in as you '
                 'answer.',
     'why': 'A fresh reader could take the sentence two ways, and it is your own sentence (your answer M-14).',
     'advice_note': 'My pick: "and pressuring men to act like they know what she wants", if that is what you meant.'},
    {'id': 'Q-409', 'words': 'Non-strategic lying is literally diagnosed as',
     'title': '"Literally diagnosed": not quite',
     'question': 'Your new sentence says non-strategic lying "is literally diagnosed as \'pathological lying.\'" '
                 'Pathological lying is a real clinical term, but it is not a diagnosis in the DSM-5: psychiatrists '
                 'treat it as a feature of other conditions, and researchers have argued it should become one '
                 '(StatPearls, "Pseudologia Fantastica", 2026: https://pubmed.ncbi.nlm.nih.gov/39163430/ ; Curtis and '
                 'Hart, "Pathological Lying: Theoretical and Empirical Support for a Diagnostic Entity": '
                 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9176035/). It could say "Non-strategic lying is what '
                 'psychiatrists call \'pathological lying,\'" and keep your point. Which do you want?',
     'why': 'A point in your own words that a reader could check and find overstated (gate E348).',
     'advice_note': 'My pick: "Non-strategic lying is what psychiatrists call \'pathological lying,\'" (your point stays: '
                    'it is closer to an illness than a failure of virtue).'},
    {'id': 'Q-314', 'words': 'especially my first wife, Bee',
     'title': 'Bee or Ann as your first wife?',
     'question': 'This paragraph (as your live post has it) says "I’ve also had telepathy with some folks, especially my '
                 'first wife, Bee", but the article calls Ann your first wife twice ("like my first wife, Ann" in your '
                 'new Twin Flames paragraph, and "I took my first wife, Ann, to two counselors" further on). Which is it '
                 'here: Ann, or Bee as "my ex, Bee"?',
     'why': 'A fact about your life that the article says two ways; only you know which is right.',
     'advice_note': 'If Bee is meant: "especially my ex, Bee". If Ann: "especially my first wife, Ann".'},
    {'id': 'Q-392', 'words': 'like I had with H.D., where',
     'title': '"H.D." or "H."?',
     'question': 'Everywhere else she is "H.", and her story (the connection that kept deepening) is the one you tell '
                 'under Two Pillars. Here the live post has "H.D." Is that a slip for "H.", or a different person?',
     'why': 'A name, so I’m not changing it without you.',
     'advice_note': 'My guess: a slip, so "H." here too.'},
]

review = {
    'format': R.FORMAT, 'review_id': 'romance-t5', 'built': '2026-11-22',
    'title': 'Romance Advice I Wish My Parents Taught Me: the whole article with your answers in',
    'intro': ['The whole article as it reads now, with your 59 versions from the Medium page in (two of them with a '
              'question below, on your own words, and two questions on names in the live text). Every paragraph, picture and video is here in order: nothing is '
              'left out. Your other versions went in as you wrote them, with only obvious slips fixed (listed in the '
              'chat).'],
    'git_file': 'articles/romance/review/teach-20261122/REVIEW-T5.html',
    'article': {'file': ART, 'sha256': sha}, 'whole': {'file': ART, 'sha256': sha},
    'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents', 'guide_label': 'your live post',
              'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/romance-20261108/articles/romance/review/teach-20261122/REVIEW-T5.md'},
    'types': {'ask': {'label': 'Questions on your words', 'about': 'only you can answer: your own new sentences'}},
    'suggestions': [],
}
for q in QUESTIONS:
    review['suggestions'].append({'id': q['id'], 'type': 'ask', 'title': q['title'], 'advice': 'ask',
                                  'question': q['question'], 'why': q['why'], 'advice_note': q['advice_note'],
                                  'whose': 'his own: his answer on the Medium page, 2026-11-22',
                                  'spans': [span(q['words'])]})
probs = R.check(review, bl)
if probs:
    sys.exit('\n'.join(probs))
(HERE / 'REVIEW-T5.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
html = R.page(review, md, bl)
(HERE / 'REVIEW-T5.html').write_text(html, encoding='utf-8')
(HERE / 'REVIEW-T5.artifact.html').write_text(R.artifact_view(html), encoding='utf-8')
cards = ['# The whole article with your answers in: the questions (2026-11-22)', '',
         'The page shows the whole article ([FIXED.md](../../humanize/fix-20261107/whole/FIXED.md)); these are its cards.', '']
for s in review['suggestions']:
    b = bl[s['spans'][0]['block']]
    cards += ['## %s. %s' % (s['id'], s['title']), '', '> ' + b['text'], '', s['question'], '', '**' + s['advice_note'] + '**', '']
(HERE / 'REVIEW-T5.md').write_text('\n'.join(cards) + '\n', encoding='utf-8')
print('REVIEW-T5: %d blocks, %d cards, %d bytes' % (len(bl), len(review['suggestions']), len(html)))
