"""The cards page of 2026-11-27 (review x1127a), published from the account this turn ran in (his other account, which
owns the older cards page 9nENpt9AEJCB43a9Wy5jqn): two teaching cards (lesson bad-trips-2026-11-14b).

  - W-LMA-73A: his herbs warning with 73a and his line. Nine checks this turn (W-LMA-73a 4, W-LMA-his 5, past the
    budget's six per paragraph); my best reads Human Written, 0.0% AI, High over his first sentence and Medium over the
    second. The article keeps the fold until his answer.
  - W-COG-SEC: last turn's card, on the other account's page (06cda5c8), which this account can't read: the section check
    after 74b reads the same two Medium windows, so the card is here too, for an answer from either account.

Neither card asks for his experience (lesson somatic-2026-11-27a): each asks for his version of words of mine or his,
whose tries are spent.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127a/build_cards_x1127a.py
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
sys.path.insert(0, str(FIX / 'x1126c'))
import suggestion_review as sr  # noqa: E402
import texts_x1127a as T  # noqa: E402
import texts_x1126c as T6  # noqa: E402

BRANCH = 'claude/community-joel-1018'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1127a/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
PG = 'https://www.pangram.com/history/'
FOLD = PG + '0d102087-7015-4501-bf13-f8c40fec8d21'
S3, S4, S5 = (PG + '2cd62104-8545-4d8c-ad06-c468ec2e4786', PG + 'c785d020-2ff6-40d6-9ee7-669c1ca39a46',
              PG + 'fef78872-dac8-438a-8377-5f03bfed1bf7')
T1, T2, ST1, ST2 = (PG + '666f323c-0200-4f4f-a54e-be84150a350b', PG + 'f3417de9-5888-4720-adc1-66303c140dab',
                    PG + 'd2357d72-aa6f-4a8c-9ff1-ab3e53ac084b', PG + 'e48fb85c-ea18-48c5-b61a-7066b4069dec')
SEC5 = PG + '97ac98d1-e65d-4272-b9d7-426879391431'
SEC6 = PG + 'a9c8692c-d9af-4806-b4ee-87fe0389f77d'
F2, F3 = PG + '787fc317-0dc4-47a4-87e8-2c9ac3df278e', PG + '23fbc3f5-ab5b-4e90-bceb-08e3354afedf'


def main():
    bl = sr.blocks(MD, whole=True)

    def blk(start):
        (i,) = [b['i'] for b in bl if b['text'].startswith(start)]
        return i, (sr.block_text(bl, i) if hasattr(sr, 'block_text') else bl[i]['text'])
    lma_i, lma_now = blk('I\'m not advising lion\'s mane or ashwagandha')
    cog_i, cog_now = blk('As you de-armor, you will feel naked and exposed.')
    faces_i, faces_now = blk('Your armored brain also projects')
    assert lma_now == T.OLD['lma'], 'the herbs warning is not the fold'
    best = T.STEP['lma-s4']
    lma = {
        'id': 'W-LMA-73A', 'type': 'teach', 'advice': 'approve', 'approve_label': 'use my best try anyway',
        'title': 'Lion\'s mane and ashwagandha with 73a: nine tries, my best High then Medium',
        'spans': [{'block': lma_i, 'start': 0, 'end': len(lma_now)}],
        'edits': [{'block': lma_i, 'before': lma_now, 'after': best}],
        'what': ('Your herbs warning with your 73a in: the gloss with pleasure in it (here "(no joy or desire)", plainer '
                 'than "(little pleasure or desire)", which read worse), and a stop sign for the reader already on either '
                 'herb that points back at what your first sentence names ("any of that": both effects). Your line "i also '
                 'can\'t recommend starting them" is said by your own "I\'m not advising lion\'s mane or ashwagandha", '
                 'with the stop sign speaking to the reader already on one, which is what question 73\'s reader couldn\'t '
                 'tell.'),
        'why': ('As it stands (no 73a) it reads [Human High in one window](%s). Every way I put 73a and your line in read '
                'lower: with "I can\'t recommend starting" and a stop sign of mine, [AI 100%%](%s) and [AI 76%%](%s); with '
                '"anyone to start" and the gloss, [Human Low and AI Low](%s); with "anyone to start" alone, [Human Medium '
                'and Human Low](%s). Your "I\'m not advising lion\'s mane" (advising a thing, not a person) carries the '
                'paragraph, and any change to it weakens it. With your first sentence kept and only the gloss changed it '
                'stays High; the second sentence, with the stop sign in it, read Human Medium each time: [step 3](%s), '
                '[step 4, my best](%s), and in your own idiom from your agmatine paragraph ("so stop either herb right away '
                'if you notice any of that"), [one window, Medium](%s). I can\'t find any more AI tells here, and I see '
                'some human tells, like your "advising lion\'s mane", "Post-ashwa", and "it\'s the same kind of thing"... '
                'can you help show me the tells I\'m missing?' % (FOLD, T1, T2, ST1, ST2, S3, S4, S5)),
        'reading': ('My best (step 4): [Human Written, 0.0%% AI](%s), High over your first sentence with the gloss in, '
                    'Human Medium over the second.' % S4),
        'tested': ('My best, step 4: [Human Written, 0.0%% AI, High then Medium](%s). Of nine checks, the stop sign as its '
                   'own sentence after your "keep in mind" read [AI in three windows](%s); steps 3 and 4, with your '
                   'first sentence as you wrote it (step 4 with the gloss), read High there.' % (S4, PG + '35b9a7c1-f6cb-4de9-8424-82b918c1b4c9')),
        'whose': ('his own: his card version of the herbs warning (his answers of 2026-11-24 18:40 UTC, '
                  'x1123c/ANSWERS-X1123C-20261124-1840.json), and his answers 73a and "i also can\'t recommend starting '
                  'them" of 2026-11-27 15:45 UTC; the gloss\'s and the stop sign\'s words are mine'),
        'stays': ('Your "I\'m not advising lion\'s mane or ashwagandha", "Post-ashwa and post-lion\'s mane syndrome are '
                  'rare, but it\'s the same kind of thing SSRIs and finasteride can do", word for word.'),
        'deciding': ('Your version of the paragraph with 73a and your line, or my best try as it reads (one Medium window), '
                     'or leaving it as it is until one reads High.'),
        'advice_note': ('Your call: Revise with your version if you can, since the stop sign is where its window drops. '
                        'If not, I\'d leave it as it is for now (Reject) rather than put in a Medium window.'),
        'ask_because': ('downside: 73a and your line aren\'t in yet, and my tries for this paragraph are spent this turn '
                        '(nine checks, past the budget\'s six)'),
        'found_by': 'Your answers 73a and "i also can\'t recommend starting them"; the checks in your Pangram account',
        'receipt': [REL + 'receipts/LMA-S4.receipt.json']}
    joined = cog_now.replace(T6.COG_S12, T6.COG_S12B)
    cog = {
        'id': 'W-COG-SEC', 'type': 'teach', 'advice': 'approve', 'approve_label': 'use the join anyway',
        'title': 'The Cognitive Warning and the paragraph after it: High by themselves, one Medium window in the section',
        'spans': [{'block': cog_i, 'start': 0, 'end': len(cog_now)}, {'block': faces_i, 'start': 0, 'end': len(faces_now)}],
        'edits': [{'block': cog_i, 'before': cog_now, 'after': joined}],
        'what': ('The Cognitive Warning (you will feel exposed and assume everyone sees your anxiety; Epley calls it the '
                 'Illusion of Transparency) and the paragraph after it (you will think people are judging you; don\'t '
                 'trust your read of a room until your heart rate is down). The same card as on last turn\'s page in your '
                 'other account; answer it on either.'),
        'why': ('After your 76 the warnings section reads [Human Written, 0.0%% AI](%s), every window High but one: the '
                'faces sentence ("Your armored brain also projects the threat it feels onto neutral faces, so you will think '
                'people are judging you when they\'re mostly just thinking about themselves", 28 words), Human Medium. After '
                '74b there were two, this one and "You will assume everyone can see your anxiety, which they mostly can\'t" '
                '([check](%s)). By themselves the two paragraphs read [Human High](%s). My last try joined the Cognitive '
                'Warning\'s first two sentences: [its window read High, the faces paragraph Medium](%s). I can\'t find more AI '
                'tells here that are mine, and I see some human tells, like your post\'s "projects ... onto neutral faces"... '
                'can you help show me the tells I\'m missing?' % (SEC6, SEC5, F2, F3)),
        'reading': ('In the section after 76: [Human Written, 0.0%% AI](%s), Human Medium over the faces sentence; every '
                    'other window High.' % SEC6),
        'tested': ('The join: [its window High, the faces paragraph Medium](%s). As they stand: [Human High by themselves]'
                   '(%s).' % (F3, F2)),
        'stays': ('Epley\'s credit, as your 68a has it; "naked and exposed"; the heart-rate test (back to your usual '
                  'resting rate, and under 90 BPM); the link to the Metabolic Red Line.'),
        'deciding': 'Your version of the two paragraphs, or the join of the first two sentences, or leaving them as they are.',
        'advice_note': ('Your call: Revise with your version if you have one, since the two short sentences of the '
                        'Cognitive Warning are where the section\'s windows split; otherwise Reject, and they stay as they '
                        'are (each paragraph reads Human High by itself).'),
        'ask_because': ('downside: one window of the warnings section stays Human Medium, and my tries for these two '
                        'paragraphs are spent'),
        'found_by': 'The section\'s checks of 2026-11-27, after 72a and after 74b; the checks in his Pangram account',
        'receipt': ['articles/neuro-de-armoring/humanize/fix-20261108/x1126c/receipts/COG-J.receipt.json']}
    sha = hashlib.sha256(MD.encode('utf-8')).hexdigest()
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261127-x1127a',
        'title': 'Neuro De-Armoring Cards, 27 November (2): the herbs warning with 73a, and the Cognitive Warning, for you '
                 'to teach me',
        'intro': ['Your 74b and 76 are in, and the warnings section reads Human Written, 0.0% AI, every window High '
                  'but one, over the faces sentence. Your 73a and your line about not starting the herbs aren\'t in yet: nine tries of '
                  'mine read below High, so the herbs warning is a card. The two cards were hidden on this page before (built '
                  'as cards I\'d leave, which the page folds away); they show now. It\'s the whole article, so you can read '
                  'both where they go.',
                  'Two cards. Revise opens the paragraph for your version. No compound, dose, unit or timing changes anywhere.'],
        'git_file': REL + 'REVIEW-X1127A.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': sha},
        'whole': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': sha},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/trauma-and-addiction-why-neurological',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'REVIEW-X1127A.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A text whose Pangram tries are spent below High: my best tested version, what each '
                                     'read, and room for yours.'}},
        'suggestions': [lma, cog],
    }
    bad = ['PROBLEM ' + x for x in sr.check(review, bl)]
    (HERE / 'REVIEW-X1127A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, bl)
    (HERE / 'REVIEW-X1127A.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1127A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for c, now, after, where in ((lma, [lma_now], best, sr.where(bl, lma_i)),
                                 (cog, [cog_now, faces_now], joined, sr.where(bl, cog_i) + ' and the paragraph after it')):
        out += ['## %s: %s' % (c['id'], c['title']), '', '*At %s*' % where, '', '**As it stands:**', '']
        out += ['> %s\n>' % n for n in now][:-1] + ['> %s' % now[-1], ''] if len(now) > 1 else ['> %s' % now[0], '']
        out += ['**%s:**' % ('My best try, as it would read' if c is lma else 'The join, as it would read'), '',
                '> %s' % after, '', '**What it says:** %s' % c['what'], '', '**Why I\'m asking:** %s' % c['why'], '',
                '**Where it reads:** %s' % c['reading'], '', '**Tried:** %s' % c['tested'], '',
                '**What stays:** %s' % c['stays'], '', '**You\'re deciding:** %s' % c['deciding'], '',
                '**My advice:** %s' % c['advice_note'], '']
    (HERE / 'REVIEW-X1127A.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', lma_i, cog_i, faces_i)
    return 0


if __name__ == '__main__':
    sys.exit(main())
