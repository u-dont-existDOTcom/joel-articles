"""The cards page of 2026-11-23 (review x1123a): the Weeks 3-5 line for his answers 16a and 17, its six Pangram tries
spent below Human High in every window, as a teaching card (lesson bad-trips-2026-11-14b; gate bad-trips-2026-11-07c).
The text is texts_x1120a.W35R (try 6), the version that also fixes the reasoning gap the read of W35Q found; try 3
(W35J) read best but carries that gap.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1123a/build_x1123a.py
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
sys.path.insert(0, str(FIX / 'x1120a'))
import suggestion_review as sr  # noqa: E402
import texts_x1120a as T  # noqa: E402

BRANCH = 'claude/community-joel-1018'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1123a/'
X20 = LANE + 'fix-20261108/x1120a/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
PG = 'https://www.pangram.com/history/'
TRIES = [  # key, uuid, what Pangram read
    ('W35F', '236e28ea-f8e6-494c-a722-7f6f9cff7331', 'AI Detected, 76% AI'),
    ('W35H', 'e5176e60-7a61-4e7d-b207-2a59adff9392', 'Human Written; one Low and two Medium windows'),
    ('W35J', 'fefcb049-c5e8-46eb-9eca-fc4ffd645f98', 'Human Written; every window High but one Medium'),
    ('W35L', 'dac12965-24f9-4ad6-9595-652036780499', 'Human Written; every window High but one Medium'),
    ('W35N', '56c14834-60a8-45c3-a6bb-a3dceaf51bb9', 'Human Written; one Low and one Medium window'),
    ('W35R', '811ba601-3400-4e8e-a9ef-9b677089f177', 'Mostly Human Written, 3% AI; two Low and two Medium windows')]


def main():
    bl = sr.blocks(MD, whole=True)
    (head,) = [b['i'] for b in bl if b['text'].startswith('Weeks 3–5: The Dynorphin Void (Depression Phase)')]
    (prot,) = [b['i'] for b in bl if b['text'].startswith('Protocol:Reduce or stop phosphatidylserine here.')]
    assert prot == head + 1
    tries = '; '.join('try %d [%s](%s%s)' % (n, r, PG, u) for n, (k, u, r) in enumerate(TRIES, 1))
    card = {
        'id': 'W35',
        'type': 'teach',
        'title': 'The Weeks 3–5 line for your 16a and 17: six tries, not yet High',
        'advice': 'approve',
        'inserts': [{'before': prot, 'kind': 'p', 'text': T.W35R}],
        'card_after': head,
        'what': ('A new first line for Weeks 3–5, for your answers 16a and 17: start the phase\'s new things one at a time, '
                 'in the order listed; no 5-HTP at all while microdosing iboga or elliptica; for UMP with any microdose, '
                 'or 5-HTP with a mushroom microdose, there isn\'t enough data yet, so try each way and see how it feels; '
                 'if you\'re too numb to tell, compare sleep and dreams; and stop the 5-HTP at its stop signs.'),
        'why': ('I can\'t find any more AI tells here, and I see some human tells, like these: your own "there isn\'t '
                'enough data" and "to see how it feels", "don\'t take 5-HTP at all", "a day without" and "If you\'re too '
                'numb to tell". Can you help show me the tells I\'m missing? Six tries by itself: %s. Try 3 came closest '
                '(only "Until there is, you can try the one you want each way ..." read Medium), but a fresh reader then '
                'found its last sentence gives mushrooms the same reason as the iboga no ("Like iboga, mushrooms act on '
                'serotonin"), so the two rules looked contradictory; this version fixes that and reads worse. Three fresh '
                'readers marked the tells they saw ([the panel](%s%spanel-w35p/PANEL.md)).'
                % (tries, BLOB, X20)),
        'reading': ('The closest try, try 3, by itself: [Human Written](%sfefcb049-c5e8-46eb-9eca-fc4ffd645f98), every window '
                    'High but "Until there is, you can try the one you want each way, on days you microdose and on days '
                    'you don\'t, and see how you feel on each.", Medium.' % PG),
        'tested': ('This version by itself: [Mostly Human Written, 3%% AI](%s811ba601-3400-4e8e-a9ef-9b677089f177): the '
                   'first sentence Medium, the second High, the third and fourth together Low, the fifth Low, the last '
                   'Medium. Every try with each window\'s confidence: [the last check](%s%schecks-1123f/RESULTS.md) and '
                   'the five before it.' % (PG, BLOB, X20)),
        'stays': 'Everything else in Weeks 3–5, word for word.',
        'deciding': ('Your version of this line: it goes in as yours. Mine goes in only once it reads Human High in every '
                     'window by itself.'),
        'advice_note': ('Revise, with your version: the six tries are spent. Two points I changed from your answers, so '
                        'say if either is wrong: elliptica is in the iboga no (the article calls it healer iboga, with '
                        'many iboga alkaloids), and the reason given is that iboga acts on serotonin (it blocks the '
                        'serotonin transporter, as antidepressants do; psilocin works at serotonin receptors instead).'),
        'ask_because': ('downside: six Pangram tries read below Human High (try 6: two Low windows), and it extends your '
                        '"iboga with 5htp, no" to elliptica'),
        'approve_label': 'use mine anyway',
        'found_by': 'His answers 16a and 17 of 2026-11-20 17:05 UTC; six checks in his Pangram account, 2026-11-23',
        'receipt': [X20 + 'W35R.receipt.json'],
    }
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261123-x1123a',
        'title': 'Neuro De-Armoring Cards, 23 November: the Weeks 3–5 line, for you to teach me',
        'intro': ['The new line at the top of Weeks 3–5, for your answers 16a and 17 (one at a time, and microdose days), '
                  'after its six Pangram tries. It\'s the whole article, so you can read the line where it goes.',
                  'One card. No compound, dose, unit or timing changes anywhere.'],
        'git_file': REL + 'REVIEW-X1123A.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'whole': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/trauma-and-addiction-why-neurological',
                  'guide_label': 'your live post',
                  'review': BLOB + REL + 'REVIEW-X1123A.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A text of mine whose Pangram tries are spent below Human High: my best tested '
                                     'version, the tells I see, and room for yours.'}},
        'suggestions': [card],
    }
    bad = ['PROBLEM ' + x for x in sr.check(review, bl)]
    (HERE / 'REVIEW-X1123A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, bl)
    (HERE / 'REVIEW-X1123A.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1123A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    out += ['## %s: %s' % (card['id'], card['title']), '',
            '*New line after %s*' % sr.where(bl, card['card_after']), '', '**As it would read:**', '',
            '> %s' % T.W35R, '', '**What it says:** %s' % card['what'], '', '**Why I\'m asking:** %s' % card['why'], '',
            '**The closest try:** %s' % card['reading'], '', '**This version:** %s' % card['tested'], '', '**What stays:** %s' % card['stays'], '',
            '**You\'re deciding:** %s' % card['deciding'], '', '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1123A.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', head, prot)
    return 0


if __name__ == '__main__':
    sys.exit(main())
