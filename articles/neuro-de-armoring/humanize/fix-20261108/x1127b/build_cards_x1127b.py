"""The cards page of the turn of his message of 2026-11-27 20:08 UTC (review x1127b): two teaching cards, for the two
paragraphs of "Psychology is the Software; Biology is the Hardware." whose tries are spent below High this turn (lesson
bad-trips-2026-11-14b). Each card's box holds every paragraph it marks (suggestion_review.py 1.14, lesson
neuro-2026-11-27l), and names no human tell it can't say a model wouldn't write (lesson neuro-2026-11-27g).

  - W-SW19: the one-sixteenth paragraph. Nine tries in all (two last turn, seven this turn); from step 6 every window
    High but its last sentence, Human Medium.
  - W-SW23: the practice paragraph after the Anti-Breakthrough. Six tries; my best reads High over the Anti-Breakthrough's
    first two sentences and Medium over its last with the practice sentence.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127b/build_cards_x1127b.py
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
import texts_x1127b as T  # noqa: E402

BRANCH = 'claude/community-joel-1018'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1127b/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
PG = 'https://www.pangram.com/history/'
SW19 = {'post': PG + '17283e5a-247e-44c0-b2c8-e8f6a90d845f', 't2': PG + 'cd2c9d6b-ada6-44c9-b29c-67292c104927',
        's2': PG + 'bee687c2-f818-435b-8f5f-ae3d4b9a4630', 's4': PG + '22a255ee-3d48-4afd-8b51-6d3ac3251feb',
        's5': PG + '84d12e88-4359-49bd-a3e8-ed6306e429f3', 's6': PG + 'de8a85ed-e939-4b92-808f-ee2e527176e6',
        's7': PG + '9f18c4aa-12e3-4806-a13d-57c8ebe5b439', 's8': PG + '9d20e313-4158-4abe-a581-1921a281f0ef'}
SW23 = {'post': PG + '3ad85ece-63b0-4c1a-bad6-df492b74835b', 't3': PG + '70b05e3c-4aaf-419d-91dd-e97b043c50ed',
        's1': PG + '17aa8876-097f-43dd-a2f2-654c38d0bb89', 's2': PG + 'beae5fbb-2ab5-4cda-a264-cf5017db761c',
        's3': PG + '1b4480e7-f060-4462-89bb-7be42ead2f3a', 'sw22': PG + '31905039-057d-4b64-9c9e-5dbde18dadef'}
NO_TELLS = ('I can\'t find any more AI tells here that I know how to fix, and I can\'t point to a human tell in it (none '
            'of it is your own writing). Can you help show me the tells I\'m missing?')


def main():
    bl = sr.blocks(MD, whole=True)

    def blk(start):
        (i,) = [b['i'] for b in bl if b['text'].startswith(start)]
        return i, bl[i]['text']
    s19_i, s19_now = blk('We are operating on about one-sixteenth')
    s22_i, s22_now = blk('The Anti-Breakthrough (Micro-Dosing):')
    s23_i, s23_now = blk('Your goal is Micro-Dosing Safety')
    best19 = T.STEP['sw19-s7']
    best23 = T.NEW['sw23-s3']
    sw19 = {
        'id': 'W-SW19', 'type': 'teach', 'advice': 'approve', 'approve_label': 'use my best try anyway',
        'title': 'The one-sixteenth paragraph: every window High but its last sentence',
        'spans': [{'block': s19_i, 'start': 0, 'end': len(s19_now)}],
        'edits': [{'block': s19_i, 'before': s19_now, 'after': best19}],
        'what': ('How far short of the company our brains evolved with we fall (about a sixteenth of the grown-ups per '
                 'child, from Perry\'s ratio just before), that the emptiness the reader may feel (the "Void") is that, '
                 'that a lonely life feels worse once the armor is off, and to gather a tribe of people they\'re close to '
                 'and see most days. My best says the post\'s "just to survive the cold" as "just to get through the '
                 'loneliness" and "reach for the armor again" as "put the armor back on", the plain words.'),
        'why': ('As it stands it reads [AI High](%s). Of my nine tries, the ones that moved it were: the Void sentence '
                'said as the reader\'s own feeling with its name in brackets ([its window from AI High to AI Low](%s)), '
                '"the cold" said as "the loneliness" ([the first Human High window](%s)), and your "you\'ll tend to" from '
                'the Cognitive Warning, which took the before-and-after sentence up ([Human Written](%s)). Then "So" '
                'before the last sentence took the first three sentences to High ([High, then Medium over the last](%s)); '
                'neither the plainer image ([step 7](%s)) nor "start gathering" ([step 8](%s)) moved the last one. %s'
                % (SW19['post'], SW19['s2'], SW19['s4'], SW19['s5'], SW19['s6'], SW19['s7'], SW19['s8'], NO_TELLS)),
        'reading': ('My best (step 7): [Human Written, 0.0%% AI](%s), High over the first three sentences (61 words), '
                    'Human Medium over the last (29 words): "So gather a tribe of people you\'re close to and see most '
                    'days, or you\'ll eventually put the armor back on just to get through the loneliness."' % SW19['s7']),
        'tested': ('Nine tries, the last seven this turn: [try 2](%s), [AI 75%%](%s), [AI 55%%, the first High window](%s), '
                   '[Human Written](%s), and three at High then Medium ([step 6](%s), [step 7](%s), [step 8](%s)).'
                   % (SW19['t2'], SW19['s2'], SW19['s4'], SW19['s5'], SW19['s6'], SW19['s7'], SW19['s8'])),
        'stays': ('The one-sixteenth and its source (Perry, 2023, your approved card SC-24), the "Void", a lonely life '
                  'feeling worse once the armor is off, and the tribe of people you\'re close to and see most days.'),
        'deciding': ('Your version of the paragraph, or my best try as it reads (one Medium window over its last '
                     'sentence), or leaving the post\'s version (AI High) until one reads High.'),
        'advice_note': ('Your call: Revise with your version if you can, since only its last sentence is below High. If '
                        'not, I\'d use my best try anyway: one Medium window is better than the post\'s AI High.'),
        'ask_because': ('downside: the paragraph\'s tries are spent (nine checks, past the budget\'s six), and my best try '
                        'still has one Medium window'),
        'found_by': 'The humanizing pass of "Psychology is the Software; Biology is the Hardware."; the checks in your '
                    'Pangram account',
        'receipt': [REL + 'receipts/SW19-S7-CARD.receipt.json', REL + 'receipts/SW19-S7.receipt.json']}
    sw23 = {
        'id': 'W-SW23', 'type': 'teach', 'advice': 'approve', 'approve_label': 'use my best try anyway',
        'title': 'The practice after the Anti-Breakthrough: High but for its last two sentences',
        'spans': [{'block': s22_i, 'start': 0, 'end': len(s22_now)}, {'block': s23_i, 'start': 0, 'end': len(s23_now)}],
        'edits': [{'block': s23_i, 'before': s23_now, 'after': best23}],
        'what': ('The daily practice the Anti-Breakthrough\'s doses of a few seconds come to: 30 seconds of slow breathing '
                 '(the post\'s "regulated breathing"), twenty times a day. The post\'s "We are not running a marathon; we '
                 'are doing physical therapy for a broken nervous system. Frequency beats intensity." goes: the paragraph '
                 'before already says why short and often.'),
        'why': ('The Anti-Breakthrough reads [Human High by itself](%s). As it stands, the practice paragraph after it '
                'reads [AI](%s). With it as one plain sentence, the pair reads [High over the first two sentences and '
                'Medium over the last two](%s), "which is what I mean by micro-dosing here." with the practice sentence. '
                'Every word I added to that sentence read worse: saying what a dose is ([AI 66%%](%s)), saying what it\'s '
                'a dose of ([Mostly Human, two Low windows](%s)); my last, "I\'d do" for "that means", read the same as '
                'the first ([High, then Medium](%s)). %s' % (SW23['sw22'], SW23['post'], SW23['t3'], SW23['s1'],
                                                              SW23['s2'], SW23['s3'], NO_TELLS)),
        'reading': ('My best: [Human Written, 0.0%% AI](%s), High over the Anti-Breakthrough\'s first two sentences (62 '
                    'words), Human Medium over its last with the practice sentence (33 words).' % SW23['s3']),
        'tested': ('Six tries: last turn\'s two read AI; this turn [High then Medium](%s), [AI 66%%](%s), [Mostly Human](%s), '
                   '[High then Medium](%s).' % (SW23['t3'], SW23['s1'], SW23['s2'], SW23['s3'])),
        'stays': 'The Anti-Breakthrough as it went in; 30 seconds of breathing, twenty times a day.',
        'deciding': ('Your version of the practice (with the Anti-Breakthrough\'s last sentence, if it helps), or my best '
                     'try as it reads, or leaving the post\'s practice paragraph (AI) until one reads High.'),
        'advice_note': ('Your call: Revise with your version if you can; the box holds both paragraphs, since the Medium '
                        'window spans the Anti-Breakthrough\'s last sentence and the practice. If not, I\'d use my best '
                        'try anyway: one Medium window is better than the post\'s AI.'),
        'ask_because': 'downside: the pair\'s tries are spent (six), and my best try still has one Medium window',
        'found_by': 'The humanizing pass of "Psychology is the Software; Biology is the Hardware."; the checks in your '
                    'Pangram account',
        'receipt': [REL + 'receipts/SW23-S3-CARD.receipt.json', REL + 'receipts/SW22-23-6.receipt.json']}
    sha = hashlib.sha256(MD.encode('utf-8')).hexdigest()
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261127-x1127b',
        'title': 'Neuro De-Armoring Cards, 27 November (3): the one-sixteenth paragraph and the daily practice, for you '
                 'to teach me',
        'intro': ['Your two versions from the last cards are in. In "Psychology is the Software; Biology is the '
                  'Hardware." two paragraphs used their tries this turn, each with one Medium window left: the '
                  'one-sixteenth paragraph (its last sentence) and the daily practice after the Anti-Breakthrough. It\'s '
                  'the whole article, so you can read both where they go.',
                  'Two cards. Revise opens the paragraphs for your version; each box holds every paragraph its card marks. '
                  'No compound, dose, unit or timing changes anywhere.'],
        'git_file': REL + 'REVIEW-X1127B.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': sha},
        'whole': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': sha},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/trauma-and-addiction-why-neurological',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'REVIEW-X1127B.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A text whose Pangram tries are spent below High: my best tested version, what each '
                                     'read, and room for yours.'}},
        'suggestions': [sw19, sw23],
    }
    bad = ['PROBLEM ' + x for x in sr.check(review, bl)]
    (HERE / 'REVIEW-X1127B.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, bl)
    (HERE / 'REVIEW-X1127B.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1127B.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for c, now, after in ((sw19, [s19_now], best19), (sw23, [s22_now, s23_now], s22_now + '\n\n' + best23)):
        out += ['## %s: %s' % (c['id'], c['title']), '', '*At %s*' % sr.where(bl, c['spans'][0]['block']), '',
                '**As it stands:**', '']
        out += sum((['> ' + n, '>'] for n in now), [])[:-1] + ['']
        out += ['**My best try, as it would read:**', ''] + sum((['> ' + n, '>'] for n in after.split('\n\n')), [])[:-1]
        out += ['', '**What it says:** %s' % c['what'], '', '**Why I\'m asking:** %s' % c['why'], '',
                '**Where it reads:** %s' % c['reading'], '', '**Tried:** %s' % c['tested'], '',
                '**What stays:** %s' % c['stays'], '', '**You\'re deciding:** %s' % c['deciding'], '',
                '**My advice:** %s' % c['advice_note'], '']
    (HERE / 'REVIEW-X1127B.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', s19_i, s22_i, s23_i)
    return 0


if __name__ == '__main__':
    sys.exit(main())
