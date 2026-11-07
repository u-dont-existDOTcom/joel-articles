"""The romance post's two paragraphs to teach me from (gate bad-trips-2026-11-07c), 2026-11-07: S2, the monastic perks, and
S17, Kim Anami. Every wording I tried of each read AI, inside its own section too
(../../humanize/fix-20261107/r03 to r06).

The page shows the two sections they sit in (PAGE-T1.md, the live post's words, headings kept), not the whole post: the
live post isn't in the repository whole, and its 116,586 characters can't be carried over from the browser in this session.

  python3 articles/romance/review/teach-20261107/build_t1.py     (from the repo root)

writes REVIEW-T1.json, REVIEW-T1.html, REVIEW-T1.artifact.html and REVIEW-T1.md beside this file.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402

MD = (HERE / 'PAGE-T1.md').read_text(encoding='utf-8')
BL = SR.blocks(MD)
H = 'https://www.pangram.com/history/'
FEED = 'https://www.pangram.com/feed/9e40aa8f-317c-4490-893d-9e99c839de88'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/romance-20261107d/'
BUILT = '2026-11-07'
ASKED = ('he asked: Joel, 2026-11-07 12:08 UTC, in the bad trips lane (gate bad-trips-2026-11-07c makes it every '
         'lane\'s rule): "if you can\'t figure out how to humanize things, give me the top most important paragraphs '
         '(usually 1 or 2) that youu think i could teach you from that would help you humanize the rest, and give me your best '
         'tries on those to fix."')


def T(i):
    return BL[i]['text']


def whole(i):
    return {'block': i, 'start': 0, 'end': len(T(i))}


def find_block(start):
    hits = [i for i, b in enumerate(BL) if b['text'].startswith(start)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


S2A = find_block('There are practical reasons to become a monastic too.')
S2B = find_block('Of course, he may sincerely want liberation, too.')
S17A = find_block('Kim Anami goes further')
S17B = find_block('She has also collected a ton of stories')

TYPES = {
    'teach': {'label': 'Teach me', 'about': 'a paragraph that reads AI in every wording I tried, whose shape other stuck lines '
              'share: how you would say it teaches me how to say them'},
}

INTRO = [
    'These are the two paragraphs of the romance post I think you could teach me the most from. Every wording I\'ve tried '
    'of each is still flagged, even inside its own section, and each card names other lines with the same shape. Each card has my '
    'tries with what Pangram read. Press Edit it and write the paragraph the way you\'d say it. I\'ll carry what you did to '
    'the others and check them.',
    'The page shows only the two sections these paragraphs sit in, as your live post has them. 16 of the post\'s 21 AI spots '
    'already read Human with small fixes, which go into the post without cards; my message lists them.',
]

CARDS = [
    dict(id='TEACH-MONASTIC-PERKS', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
         title='The practical reasons to become a monk: a general claim, two cases with a list, a balanced close',
         reading=('In your live post ([your extension\'s check](%s)): AI Low on "There are practical reasons to become a '
                  'monastic too.", AI High on the poor-country and West sentences, and AI Low on each closing sentence.'
                  % FEED),
         tested=('1. "Some people become monks for practical reasons too. In a poor country, the robes come with free food, a '
                 'place to live, status, and a way out of ordinary responsibilities. Even in the West, where the free food '
                 'matters less, a guy who never got much respect as a layman becomes Venerable Somebody, and suddenly people '
                 'bow to him. Of course, he can sincerely want liberation and still enjoy the bowing." '
                 '[66%% AI](%sc2ef4f06-da74-439e-b714-d971e5a776f6).\n\n'
                 '2. "Some people become monks for practical reasons too. In a poor country, the robes get you free room and '
                 'board and status, and nobody expects you to earn a living or raise a family anymore. In the West the free '
                 'food probably isn\'t the draw, but a guy nobody respected much as a layman can shave his head, become '
                 'Venerable Somebody, and suddenly people are bowing to him. Of course, he may sincerely want liberation too. '
                 'Most of us have more than one reason for the big choices we make." [71%% AI](%s887feba1-bd01-4c9c-af80-376078a997a6).\n\n'
                 '3. My best: "Some people become monks for practical reasons too. In a poor country, it\'s free food, a roof '
                 'and respect, and nobody expects you to hold down a job or raise a family. And even where the food doesn\'t '
                 'matter, like in the West, a guy who was a nobody as a layman gets to be Venerable Somebody, and people bow to '
                 'him. Of course, he may sincerely want liberation, too. People can want several things at once." '
                 '[27%% AI](%s090fc1ae-7aca-49e3-ba70-f9e0a9857ea2) with the paragraph before it, and inside the whole section '
                 '[14%% AI](%s08aaaf98-6798-4b88-b334-de5c014dc274): AI Medium on the poor-country sentence, AI Low on the rest. '
                 'A tell panel (two other models reading for AI tells) agreed on the list of perks and the balanced closing pair.')
                % (H, H, H, H),
         why=('Five wordings of mine read AI, and in the section around it the best one still does. Its shape is a general '
              'claim, two contrasted cases, a list in one of them, and a balanced close. Some of the post\'s Low lines have the '
              'same shape: "If closeness was safe when you were little, maybe it does feel a bit like coming home. But if it '
              'came with neglect, abuse, or if people disappeared on you, ...", "Helping carry somebody through temporary '
              'incapacity is different from becoming the permanent support system for a man who won\'t take responsibility.", '
              'and "She should not have to perform softness, helplessness, or cuteness every minute to prove she is feminine."'),
         advice_note=('Edit it: write it the way you\'d say it. What it says has to stay: some people become monks for '
                      'practical reasons; in a poor country that means free food, a place to live, status and a way out of '
                      'ordinary responsibilities; in the West the free food matters less, but a nobody becomes Venerable '
                      'Somebody and people bow to him; and he may still sincerely want liberation, since people want several '
                      'things at once. I\'ll carry what you do to the lines above, test each, and put the ones that read Human '
                      'straight in.'),
         spans=[whole(S2A), whole(S2B)]),
    dict(id='TEACH-KIM-ANAMI', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
         title='Kim Anami\'s view: someone else\'s teaching summed up, with a list',
         reading=('In your live post ([your extension\'s check](%s)): AI Medium on "Kim Anami goes further and treats sexual '
                  'energy itself as a path into healing, creativity, worldly action, and spiritual awakening." and AI Low on '
                  'the students\' sentence. The jade-egg sentence read Human there.' % FEED),
         tested=('1. "Kim Anami goes further and treats sexual energy itself as a path to healing and spiritual awakening. '
                 'She\'s also collected a ton of stories from students who say the effects didn\'t stay in the bedroom and '
                 'spilled over into their health, work, money, creativity, and everything else." '
                 '[100%% AI](%s08dcbe93-bdb4-4fd2-af40-7eaa4add60ca).\n\n'
                 '2. "Kim Anami goes even further: she says sexual energy itself can heal you and wake you up spiritually. '
                 'She\'s also collected a ton of stories from students who say the effects spilled out of the bedroom into '
                 'their health, work, money, creativity, the rest of their lives." [100%% AI](%s930cbd06-1aaf-4af2-9f32-c1cf8d480561) '
                 'with the jade-egg sentence, and inside the whole section [15%% AI](%s5e02bd99-6014-48ff-be5d-b8e1694c6803): '
                 'both of her sentences AI, and three of the post\'s sentences around them AI Low.\n\n'
                 '3. "Kim Anami takes this a lot further than the suttas do: for her, sexual energy itself can heal you and '
                 'wake you up spiritually. She\'s also collected a ton of stories from students who say it changed their '
                 'health, their work, their creativity, even their money." [100%% AI](%sc89a704a-4c33-40e5-8a5b-e5beda918196). '
                 'This try fixed what a tell panel agreed on: "goes even further", the paired benefits, the list\'s catch-all.')
                % (H, H, H, H),
         why=('Three wordings of mine read AI at 100%%, and inside its section the best one ([15%% AI](%s5e02bd99-6014-48ff-'
              'be5d-b8e1694c6803)) pulls the post\'s sentences around it to AI Low. Its shape is a teacher\'s view summed up in a sentence, with a list. The post reports other teachers the '
              'same way: Toft and Perel read Human after small fixes, but "That laboratory evidence establishes the '
              'biological validity and uniqueness of the phenomenon." still reads Human Low. Her linked page also needed an '
              'approval to open from here, so I couldn\'t check her claims against it.') % H,
         advice_note=('Edit it: write it the way you\'d say it. What it says has to stay: Kim Anami goes further than the '
                      'suttas and treats sexual energy itself as a path into healing, creativity, worldly action and '
                      'spiritual awakening; she has collected a ton of stories from students who say the effects spill out '
                      'of sex into health, work, money and creativity; her jade-egg practice is training for the cervical O. '
                      'I\'ll carry what you do to the lines above, test each, and put the ones that read Human straight in.'),
         spans=[whole(S17A), whole(S17B)]),
]


def cards_md(review):
    """The page's cards as text, for GitHub (he never gets sent to the JSON)."""
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text. Built %s from the two sections of [your live post](%s) they sit in. To answer, use the '
           'page, or write your version under a card\'s name in a message to me.' % (review['built'], review['links']['guide']),
           '']
    out += [x for para in review.get('intro', []) for x in (para, '')]
    for s in review['suggestions']:
        blocks_ = sorted({sp['block'] for sp in s['spans']})
        out += ['## %s: %s' % (s['id'], s['title']), '', '*%s*' % SR.where(BL, blocks_[0]), '',
                '**The paragraph%s now:**' % ('s' if len(blocks_) > 1 else ''), '']
        out += ['> %s\n' % T(i) for i in blocks_]
        out += ['**What Pangram read:** %s' % s['reading'], '', '**My tries, with what Pangram read:**', '', s['tested'], '',
                '**Why it comes to you:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'romance-teach-t1',
        'title': 'Romance Advice I Wish My Parents Taught Me: two paragraphs to teach me from',
        'intro': INTRO,
        'git_file': 'articles/romance/review/teach-20261107/REVIEW-T1.html',
        'article': {'file': 'articles/romance/review/teach-20261107/PAGE-T1.md',
                    'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': BUILT,
        'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents',
                  'guide_label': 'your live post',
                  'review': BLOB + 'articles/romance/review/teach-20261107/REVIEW-T1.md'},
        'types': TYPES,
        'suggestions': CARDS,
    }
    probs = SR.check(review, BL)
    if probs:
        raise SystemExit('\n'.join(probs))
    (HERE / 'REVIEW-T1.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    page = SR.page(review, MD, BL)
    (HERE / 'REVIEW-T1.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-T1.artifact.html').write_text(SR.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-T1.md').write_text(cards_md(review), encoding='utf-8')
    print(len(CARDS), 'cards')


if __name__ == '__main__':
    main()
