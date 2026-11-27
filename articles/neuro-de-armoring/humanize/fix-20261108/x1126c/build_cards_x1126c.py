"""The cards page of 2026-11-27 (review x1126c): the one place the warnings section still reads below High after 72a, as a
teaching card (lesson bad-trips-2026-11-14b): the Cognitive Warning and the paragraph after it read Human High by
themselves, but in the section two windows over them read Human Medium, and the pair's tries are spent this turn.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1126c/build_cards_x1126c.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
H = FIX.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import suggestion_review as sr  # noqa: E402
import texts_x1126c as T  # noqa: E402

BRANCH = 'claude/community-joel-1018'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1126c/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
PG = 'https://www.pangram.com/history/'
SEC4 = PG + 'f2364b2b-f464-45de-a68a-f80f938b5ddc'
F1, F2, F3 = (PG + '69498d51-4485-47ad-b3be-c50dd04d2c7f', PG + '787fc317-0dc4-47a4-87e8-2c9ac3df278e',
              PG + '23fbc3f5-ab5b-4e90-bceb-08e3354afedf')


def main():
    bl = sr.blocks(MD, whole=True)

    def blk(start):
        (i,) = [b['i'] for b in bl if b['text'].startswith(start)]
        return i, (sr.block_text(bl, i) if hasattr(sr, 'block_text') else bl[i]['text'])
    cog_i, cog_now = blk('As you de-armor, you will feel naked and exposed.')
    faces_i, faces_now = blk('Your armored brain also projects')
    assert cog_now.count(T.COG_S12) == 1, 'the Cognitive Warning is not as this turn left it'
    joined = cog_now.replace(T.COG_S12, T.COG_S12B)   # the page's block text: links as their words
    card = {
        'id': 'W-COG-SEC', 'type': 'teach', 'advice': 'leave', 'approve_label': 'use the join',
        'title': 'The Cognitive Warning and the paragraph after it: High by themselves, two Medium windows in the section',
        'spans': [{'block': cog_i, 'start': 0, 'end': len(cog_now)}, {'block': faces_i, 'start': 0, 'end': len(faces_now)}],
        'edits': [{'block': cog_i, 'before': cog_now, 'after': joined}],
        'what': ('The Cognitive Warning (you will feel exposed and assume everyone sees your anxiety; Epley calls it the '
                 'Illusion of Transparency) and the paragraph after it (you will think people are judging you; don\'t '
                 'trust your read of a room until your heart rate is down). Your label is folded in, as 72a asked.'),
        'why': ('Checked as a section the warnings now read [Human Written, 0.0%% AI](%s): every window High but two, both '
                'here, "You will assume everyone can see your anxiety, which they mostly can\'t" (13 words) and "Your '
                'armored brain also projects the threat it feels onto neutral faces, so you will think people are judging '
                'you when they\'re mostly just thinking about themselves" (28 words), each Human Medium. By themselves the '
                'two read Human High ([with the label folded in](%s); [with your post\'s "projects ... onto" back in place '
                'of my "reads ... into"](%s)). My last try joined the Cognitive Warning\'s first two sentences and put the '
                'faces sentence\'s point first: [the join read High in its own window, the faces paragraph Human Medium]'
                '(%s). That was the pair\'s last try for this turn (its latest read worse, so the ledger stops it). I can\'t '
                'find more AI tells here that are mine; the short sentences split into small windows when the section is '
                'read whole. Can you show me what you\'d change?' % (SEC4, F1, F2, F3)),
        'reading': ('In the section: [Human Written, 0.0%% AI](%s), Human Medium over "You will assume everyone can see '
                    'your anxiety, which they mostly can\'t" and over the faces sentence; every other window High.' % SEC4),
        'tested': ('The join, in my last try of the two paragraphs: [its window read Human High, the faces paragraph after '
                   'it Human Medium](%s) (that try also moved the faces sentence\'s point first, which I would not keep). '
                   'As they stand they read [Human High by themselves](%s).' % (F3, F2)),
        'stays': ('Epley\'s credit, as your 68a has it; "naked and exposed"; the heart-rate test (back to your usual '
                  'resting rate, and under 90 BPM); the link to the Metabolic Red Line.'),
        'deciding': 'Your version of the two paragraphs, or the join of the first two sentences, or leaving them as they are.',
        'advice_note': ('Leave it as it is, unless you give your version: each paragraph reads Human High by itself, and the '
                        'join alone is untested in the section. If you write yours, the two short sentences of the '
                        'Cognitive Warning are where the section\'s windows split.'),
        'ask_because': ('downside: two windows of the warnings section stay Human Medium, and my tries for these two '
                        'paragraphs are spent this turn'),
        'found_by': 'The section\'s last check of 2026-11-27, after 72a; the checks in his Pangram account',
        'receipt': [REL + 'receipts/COG-J.receipt.json']}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261127-x1126c',
        'title': 'Neuro De-Armoring Cards, 27 November: the Cognitive Warning in the warnings section, for you to teach me',
        'intro': ['After 72a every warning at the top reads Human High by itself, and the section reads Human Written, '
                  '0.0% AI. Two windows still read Human Medium, both in the Cognitive Warning and the paragraph after '
                  'it. It\'s the whole article, so you can read them where they go.',
                  'One card. No compound, dose, unit or timing changes anywhere.'],
        'git_file': REL + 'REVIEW-X1126C.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'whole': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/trauma-and-addiction-why-neurological',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'REVIEW-X1126C.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A text of mine whose Pangram tries are spent below High: my best tested version, '
                                     'what each read, and room for yours.'}},
        'suggestions': [card],
    }
    bad = ['PROBLEM ' + x for x in sr.check(review, bl)]
    (HERE / 'REVIEW-X1126C.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, bl)
    (HERE / 'REVIEW-X1126C.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1126C.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    out += ['## %s: %s' % (card['id'], card['title']), '', '*At %s and the paragraph after it*' % sr.where(bl, cog_i), '',
            '**As they stand:**', '', '> %s' % cog_now, '>', '> %s' % faces_now, '',
            '**The join, as it would read:**', '', '> %s' % joined, '',
            '**What it says:** %s' % card['what'], '', '**Why I\'m asking:** %s' % card['why'], '',
            '**In the section:** %s' % card['reading'], '', '**The join:** %s' % card['tested'], '',
            '**What stays:** %s' % card['stays'], '', '**You\'re deciding:** %s' % card['deciding'], '',
            '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1126C.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', cog_i, faces_i)
    return 0


if __name__ == '__main__':
    sys.exit(main())
