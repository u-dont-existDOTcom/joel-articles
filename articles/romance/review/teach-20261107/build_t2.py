"""The romance post's last stretch to teach me from (gate bad-trips-2026-11-07c), 2026-11-07 23:35 UTC: Jealousy 367 to
369. After his S2 and S17 versions (ANSWERS-T1.json) I carried his fixes to the three stretches with S2's pattern. Romance
285 to 287 and Idealization 148 now read Human in their sections (../../humanize/fix-20261107/r21 to r24); these three
paragraphs each read Human by themselves and still read AI together and in their section (r21 to r25).

  python3 articles/romance/review/teach-20261107/build_t2.py     (from the repo root)

writes REVIEW-T2.json, REVIEW-T2.html, REVIEW-T2.artifact.html and REVIEW-T2.md beside this file.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402

MD = (HERE / 'PAGE-T2.md').read_text(encoding='utf-8')
BL = SR.blocks(MD)
H = 'https://www.pangram.com/history/'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/romance-20261107n/'
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


J367 = find_block('I would rather make every attraction possible')
J368 = find_block('A foundational, permanent, exclusive romantic partnership')
J369 = find_block('That’s not to say that polyamory is automatically better')

TYPES = {
    'teach': {'label': 'Teach me', 'about': 'paragraphs that read AI in every wording I tried, in their section: how you '
              'would say them teaches me how to say the rest'},
}

INTRO = [
    'Your two versions taught me a lot, and I used them on the three other stretches with the same problem. Two of them '
    'now read Human inside their sections: Romance ("play the damsel ... pretending she can’t open a jar") and Idealization '
    '("she can go from worshipping me to hating me, first in private and then in front of everybody"). My message has '
    'the links.',
    'These three jealousy paragraphs are the last ones still flagged. Each of my newest versions reads Human by itself, '
    'but together, and inside the section, they read AI, the way S2 did before your version. Press Edit it and write them '
    'the way you’d say them; the page shows the section as your live post has it.',
]

CARDS = [
    dict(id='TEACH-JEALOUSY-POLY', type='teach', advice='edit', whose=ASKED, keep_label='skip this one',
         title='Mentioning attractions, promises of exclusivity, and how polyamory can be dishonest too',
         reading=('In the section as your live post has it: [28%% AI](%s184babff-d20a-4383-8e5d-c125b55aa48b), AI Low and '
                  'Medium on all three paragraphs, and his 366 and 370 Low around them.' % H),
         tested=('1. Idioms in place of the abstract words ("a whole sit-down talk", "each other’s one and only forever", '
                 '"can’t keep it in their pants"): the three with 366 and 370 read [95%% AI](%s613a0e10-1633-4eed-8792-1c5e763740fe), '
                 'worse than the live words.\n\n'
                 '2. A particular scene in each, your plain words back: 367 "I’d rather be able to say “she’s cute” about a '
                 'woman at the next table, and have my girlfriend say the same about some guy, without it turning into a '
                 'fight. If only the serious crushes get mentioned, every mention turns into a confession, so people end up '
                 'hiding all of them." read [Human, Medium then Low](%s2a7438bb-34a3-43db-865e-8ea8126efeec) by itself; 368 '
                 'with 369 read [100%% AI](%s5a483771-c3cd-4cdd-89bc-07f2ba9838aa).\n\n'
                 '3. My best: 369 told as what people do, the way your S2 told the monks’ reasons: "Lots of couples promise '
                 'forever and nobody else. Look around at how many actually live that way. In a polyamorous relationship the '
                 'boundaries might be more negotiable, but then somebody has to sit down and negotiate them, down to who '
                 'gets to stay the night." and "Polyamory can be dishonest too, like when someone who can’t get close to any '
                 'one person dates four at once and calls it polyamory. Or when someone keeps cheating until they finally '
                 'announce they’re poly, without necessarily doing the work on themselves that would make it ethical. If '
                 'you can’t do monogamy, say so, since pretending can do more damage than an affair would have." Together '
                 'they read [Human, Medium and High](%s96386c46-ec98-45ad-bd35-41e0f5dddde8), and 369 alone [Human, '
                 'High](%s4b7466bb-9691-42f1-ab09-546c3fc28664). With 367 and with 366 and 370 around them, '
                 '[94.8%% AI](%s4d8ad356-99b1-48ed-824d-5d20731b67a8); in the whole section, '
                 '[26%% AI](%sf6838232-0d06-4160-b614-171df927ee32): AI Medium on 367’s second sentence, AI High on 368, AI '
                 'Low on 369 with 370.\n\n'
                 '4. The links a fresh reader found missing put in words ("For that to stay honest, I’d rather we could both '
                 'mention attractions to other people casually, ...", "... so a lot of them end up pretending. Polyamory '
                 'leaves those rules open, ...", "Or when someone who can’t stop cheating just renames it polyamory, ..."): '
                 'the section read [31.7%% AI](%s8d1b8eb6-deb9-4a95-a0d9-707cb70ac464), worse.') % (H, H, H, H, H, H, H, H),
         why=('Every version of mine reads Human by itself and AI once the three sit together, which is what happened to S2 '
              'until your version. Your fixes I carried (concrete things in place of lists, a reason with since, what '
              'people do in place of what an idea does) fixed Romance and Idealization, and fixed each of these alone, but '
              'not the three together. Something about how they follow one another is still mine.'),
         sense=('A fresh reader read your live three for sense (SENSE-T2.md beside this page) and found the links between '
                'them missing: "I would rather" has no alternative and never says to whom; the step from "only the serious '
                'ones" to "a major event" isn’t said; 368 jumps from mentioning attractions to promises to polyamory; '
                '"negotiable" doesn’t mean "negotiating is required"; 369 answers a claim nobody made, its "too" points at a '
                'dishonesty only implied, and "a way to admit a lack of self-control" sits oddly beside "dishonest", since '
                'admitting is honest. My fourth try put each link in words and read worse, so I don’t trust my reading of '
                'how these three should follow one another.'),
         advice_note=('Edit it: write the three the way you’d say them. What they say has to stay: you’d rather any '
                      'attraction, even a small one, could be mentioned casually, since if only serious ones get mentioned '
                      'each becomes a big event and people stop saying anything; exclusive lifelong partnership is promised '
                      'far more often than lived; polyamory’s boundaries are more negotiable, so they have to be '
                      'negotiated; polyamory isn’t automatically better, since it can be a way to cope with not connecting '
                      'deeply with one person, or to admit a lack of self-control without the work that would make it '
                      'ethical; and if you can’t do monogamy, saying so is more honest than pretending, which can do more '
                      'damage than an outside connection would have.'),
         spans=[whole(J367), whole(J368), whole(J369)]),
]


def cards_md(review):
    """The page's cards as text, for GitHub (he never gets sent to the JSON)."""
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text. Built %s from the section of [your live post](%s) they sit in. To answer, use the '
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
        'review_id': 'romance-teach-t2',
        'title': 'Romance Advice I Wish My Parents Taught Me: the jealousy paragraphs to teach me from',
        'intro': INTRO,
        'git_file': 'articles/romance/review/teach-20261107/REVIEW-T2.html',
        'article': {'file': 'articles/romance/review/teach-20261107/PAGE-T2.md',
                    'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': BUILT,
        'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents',
                  'guide_label': 'your live post',
                  'review': BLOB + 'articles/romance/review/teach-20261107/REVIEW-T2.md'},
        'types': TYPES,
        'suggestions': CARDS,
    }
    probs = SR.check(review, BL)
    if probs:
        raise SystemExit('\n'.join(probs))
    (HERE / 'REVIEW-T2.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    page = SR.page(review, MD, BL)
    (HERE / 'REVIEW-T2.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-T2.artifact.html').write_text(SR.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-T2.md').write_text(cards_md(review), encoding='utf-8')
    print(len(CARDS), 'cards')


if __name__ == '__main__':
    main()
