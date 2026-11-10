"""The romance post's third teaching page (2026-11-08): after his whole-article check of 16:47 UTC
(../../humanize/fix-20261107/r27/checks/RESULTS-whole-r27.json), every window it read AI or Low reads Human at Medium or
High in its section (r28) but one: "Slow & steady", whose list of what can go wrong reads AI in every wording of mine
(gate bad-trips-2026-11-07c). And one question on his own words: his new 369 tells the college friend with four
girlfriends that Labels already tells.

  python3 articles/romance/review/teach-20261107/build_t3.py     (from the repo root)

writes REVIEW-T3.json, REVIEW-T3.html, REVIEW-T3.artifact.html and REVIEW-T3.md beside this file.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402
import build_t2  # noqa: E402

MD = (HERE / 'PAGE-T3.md').read_text(encoding='utf-8')
BL = SR.blocks(MD)
build_t2.BL = BL
H = 'https://www.pangram.com/history/'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
BUILT = '2026-11-08'


def find_block(start):
    hits = [i for i, b in enumerate(BL) if b['text'].startswith(start)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


def whole(i):
    return {'block': i, 'start': 0, 'end': len(BL[i]['text'])}


def phrase(i, words):
    a = BL[i]['text'].index(words)
    return {'block': i, 'start': a, 'end': a + len(words)}


SLOW = find_block('You can know somebody for twenty years')
FRIEND_L = find_block('The person getting more of what they want')
FRIEND_J = find_block('Polyamory can also be a way of escaping deeper intimacy')

TYPES = {
    'teach': {'label': 'Teach me', 'about': 'a paragraph that reads AI in every wording I tried: how you would say it '
              'teaches me how to say the rest'},
    'question': {'label': 'Question', 'about': 'a choice about your own words'},
}
INTRO = [
    'Your whole-article check read both halves Human Written. Of the eight windows it read AI or Low, seven now read Human '
    'at Medium or High in their sections; my message has the links.',
    'This page has the one I can’t fix, a list of what can go wrong on a first night, and one question about your new '
    'jealousy paragraphs. Press Edit it on the first and write it the way you’d say it.',
]
CARDS = [
    dict(id='TEACH-SLOW-LIST', type='teach', advice='edit', whose=build_t2.ASKED, keep_label='skip this one',
         title='What twenty years of knowing someone can’t tell you about the first night',
         reading=('In your whole-article check (draft A, '
                  '[the result](https://www.pangram.com/feed/87029c8c-313d-436c-b885-e76466096da6)): Human Low on its two '
                  'list sentences, though the section read Human with no Low by itself ([#96](%sc71291d2-3fc7-444b-a538-44647109f8b8)).' % H),
         tested=('1. As your live post has it, one sentence with five items: the section read '
                 '[34%% AI](%sdb9d87a7-249e-44f8-a1e3-2facc9bc1b6c).\n\n'
                 '2. Split in two sentences (the version above): the section read [Human, no Low](%sc71291d2-3fc7-444b-a538-44647109f8b8), '
                 'and your whole check read it Low.\n\n'
                 '3. Particular things, two to a sentence ("Maybe their smell turns you off, or one of you wants it every day '
                 'while the other is happy with once a month. Your kinks might not line up either, or one person is sexually '
                 'shut down, or your bodies just don’t click."): [19.8%% AI](%s04f1b37e-4be3-45f7-b25e-4a8036f35803), AI '
                 'Medium on those two sentences.\n\n'
                 '4. Cut to two items, joined to the opener, with an ending that ties back ("... that the polarity isn’t '
                 'there: maybe their smell turns you off, or one of you wants it every day and the other once a month, and '
                 'twenty years of talking would never have told you that."): [25%% AI](%sc94b9077-c339-4424-bd97-11e0ff0c9cae).'
                 ) % (H, H, H, H),
         why=('A list of what can go wrong reads AI however I shape it: as one sentence, as two, cut to two items, or with '
              'particular things in it. Your fixes for lists (bad-trips-2026-11-07j, romance-2026-11-07a) lifted every '
              'other list in this post; this one I can’t get past Low.'),
         sense=('A fresh reader read my last two versions of it for what its reader needs (the r28 receipts): nothing '
                'unclear; they found the list\'s second sentence more of the same, which my fourth try cut, and that read '
                'worse.'),
         advice_note=('Edit it: write the paragraph the way you’d say it. What it says has to stay: you can know someone '
                      'for years and still find on the first night that the polarity isn’t there, for reasons no amount of '
                      'knowing them could have shown you (smell or touch, how often each of you wants sex, kinks, one person '
                      'shut down, bodies that don’t connect: as many of these as you want to keep).'),
         spans=[whole(SLOW)]),
    dict(id='ASK-FRIEND-TWICE', type='question', advice='ask', whose='his own words, in two places',
         title='Your college friend with four girlfriends is told twice',
         question=('Your new jealousy paragraph tells him ("like my one poly college friend who boasted about having 4 '
                   'girlfriends, but admitted to me that he felt deeply unhappy"), and Labels already does ("In college I '
                   'had a friend with four girlfriends ... “No, I’m miserable, dude. I feel empty inside.”"). Keep both, '
                   'cut one, or have the jealousy one point back ("like the college friend with four girlfriends I '
                   'mentioned earlier")?'),
         why=('A reader meets the same friend twice, about 330 paragraphs apart, each time as if for the first time. Both '
              'places use him for a different point (in Labels: the one getting more of what he wants isn’t happier; in '
              'Jealousy: polyamory as a way to escape intimacy), so I won’t cut either without you. My advice: keep '
              'Labels as it is and have the jealousy one point back.'),
         spans=[phrase(FRIEND_L, 'In college I had a friend with four girlfriends who boasted about it to girls while trying to get a fifth.'),
                phrase(FRIEND_J, 'like my one poly college friend who boasted about having 4 girlfriends, but admitted to me that he felt deeply unhappy')]),
]


def _cards_md(review):
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text. Built %s from the sections of [your live post](%s) they sit in, as the fixed '
           'version has them. To answer, use the page, or write under a card\'s name in a message to me.'
           % (review['built'], review['links']['guide']), '']
    out += [x for para in review.get('intro', []) for x in (para, '')]
    for s in review['suggestions']:
        blocks_ = sorted({sp['block'] for sp in s['spans']})
        out += ['## %s: %s' % (s['id'], s['title']), '', '*%s*' % SR.where(BL, blocks_[0]), '']
        if s['advice'] == 'ask':
            out += ['**The words:**', ''] + ['> %s\n' % BL[i]['text'] for i in blocks_]
            out += ['**My question:** %s' % s['question'], '', '**Why I ask:** %s' % s['why'], '']
            continue
        out += ['**The paragraph now:**', ''] + ['> %s\n' % BL[i]['text'] for i in blocks_]
        out += ['**What Pangram read:** %s' % s['reading'], '', '**My tries, with what Pangram read:**', '', s['tested'], '',
                '**Why it comes to you:** %s' % s['why'], '', '**What a fresh reader found:** %s' % s['sense'], '',
                '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'romance-teach-t3',
        'title': 'Romance Advice I Wish My Parents Taught Me: one list to teach me from, and a question',
        'intro': INTRO,
        'git_file': 'articles/romance/review/teach-20261107/REVIEW-T3.html',
        'article': {'file': 'articles/romance/review/teach-20261107/PAGE-T3.md',
                    'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': BUILT,
        'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents',
                  'guide_label': 'your live post',
                  'review': BLOB + 'articles/romance/review/teach-20261107/REVIEW-T3.md'},
        'types': TYPES,
        'suggestions': CARDS,
    }
    probs = SR.check(review, BL)
    if probs:
        raise SystemExit('\n'.join(probs))
    (HERE / 'REVIEW-T3.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    page = SR.page(review, MD, BL)
    (HERE / 'REVIEW-T3.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-T3.artifact.html').write_text(SR.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-T3.md').write_text(_cards_md(review), encoding='utf-8')
    print(len(CARDS), 'cards')


if __name__ == '__main__':
    main()
