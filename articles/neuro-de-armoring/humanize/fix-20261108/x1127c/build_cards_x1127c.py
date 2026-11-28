"""The cards page of the turn of his cards-page export of 2026-11-27 22:59 UTC (review x1127c): one teaching card, for
the Metabolic Red Line's second paragraph, whose six tries are spent this turn (lesson bad-trips-2026-11-14b). Its box
holds the paragraph as it stands (back to its text before this turn: the try that read High in one window changed the
meaning) and my best try that keeps the meaning.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127c/build_cards_x1127c.py
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
import texts_x1127c as T  # noqa: E402

BRANCH = 'claude/community-joel-1018'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1127c/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
PG = 'https://www.pangram.com/history/'
P33 = {'t1': PG + '58a89835-e138-4a23-b512-6369e1c9eda9', 't2': PG + 'f55e9c83-ee35-48be-973e-ace0616ee952',
       't3': PG + '7d009652-86c5-4ca7-a8d3-35ac5cbf28b3', 't4': PG + 'd9eb7768-b356-42f7-985c-ba0dc2911d16',
       't5': PG + '72ba33d4-6a70-4601-88a8-a249cc49dd1e', 't6': PG + 'a8485271-f241-43e8-8977-24921d310ab5'}
NO_TELLS = ('I can\'t find any more AI tells here that I know how to fix, and I can\'t point to a human tell in it (none '
            'of it is your own writing). Can you help show me the tells I\'m missing?')


def main():
    bl = sr.blocks(MD, whole=True)

    def blk(start):
        (i,) = [b['i'] for b in bl if b['text'].startswith(start)]
        return i, bl[i]['text']
    i33, now33 = blk("So if you try to process trauma while you're above this red line")
    best = T.NEW['p033']
    card = {
        'id': 'W-P033', 'type': 'teach', 'advice': 'approve', 'approve_label': 'use my best try anyway',
        'title': 'The Red Line\'s second paragraph: my tries that read High changed what it says',
        'spans': [{'block': i33, 'start': 0, 'end': len(now33)}],
        'edits': [{'block': i33, 'before': now33, 'after': best}],
        'what': ('Working on trauma above the red line adds armor; why (you can\'t think as well, and stress chemicals '
                 'build up DeltaFosB in a reward center, the protein the protocol treats as the armor, though that '
                 'isn\'t settled); and to work on trauma only under the line (the "window of tolerance", which your 39a '
                 'moved here). My best fixes what the three fresh reads found: catecholamines don\'t "transcribe" '
                 'proteins, "In that state" read as inside the window, DeltaFosB was both "the armor itself" and "the '
                 'master switch", and the advice came before its reason.'),
        'why': ('Six tries this turn. The one that read [Human High in one window](%s) said DeltaFosB "holds the armor in '
                'place", and the read beside your post found that changes what it says (your post: the new DeltaFosB '
                'proteins are the armor, and more of them get made), so it isn\'t in. Saying it the way your post means '
                'it reads [High, then Low over that sentence, then High](%s). Saying the doubt once took the sentence '
                'from [AI Low](%s) to [Human](%s); "switch on" for "set off the making of" and the label as an aside '
                'moved little ([3](%s), [4](%s)). %s' % (P33['t5'], P33['t6'], P33['t1'], P33['t2'], P33['t3'],
                                                           P33['t4'], NO_TELLS)),
        'reading': ('My best: [Human Written, 0.0%% AI](%s), High over the first sentence (24 words), Human Low over the '
                    'DeltaFosB sentence (47 words), High over the advice (19 words).' % P33['t6']),
        'tested': ('Six tries: [AI 26%%](%s), [Human, Low and Medium](%s), [Human, Low](%s), [Human, Low and Medium](%s), '
                   '[one window High, but the meaning changed](%s), [High, Low, High](%s).'
                   % (P33['t1'], P33['t2'], P33['t3'], P33['t4'], P33['t5'], P33['t6'])),
        'stays': ('The red line, the armor it adds, the IQ drop, the catecholamines and the Nucleus Accumbens, DeltaFosB '
                  'and your 39a caveat, and the window of tolerance.'),
        'deciding': ('Your version of the paragraph, or my best try as it reads (one Low window over the DeltaFosB '
                     'sentence), or leaving it as it stands until one reads High.'),
        'advice_note': ('Your call: Revise with your version if you can; only the DeltaFosB sentence is below High in my '
                        'best. If not, I\'d use my best anyway: it says what your post says, with the reads\' sense '
                        'fixes, and the text as it stands has the mix-ups they found.'),
        'ask_because': 'downside: the paragraph\'s tries are spent (six), and my best try still has one Low window',
        'found_by': 'The humanizing pass of Part 1, A. The Metabolic Red Line; the checks in your Pangram account',
        'receipt': [REL + 'receipts/P033-S1.receipt.json']}
    sha = hashlib.sha256(MD.encode('utf-8')).hexdigest()
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261127-x1127c',
        'title': 'Neuro De-Armoring Cards, 27 November (4): the Red Line\'s second paragraph, for you to teach me',
        'intro': ['Your two versions from the last cards are in. Part 1\'s intro and the Red Line\'s first paragraph went '
                  'in at Human High; the second paragraph used its tries, and the one that read High changed what it '
                  'says, so it stays as it was. It\'s the whole article, so you can read it where it goes.',
                  'One card. Revise opens the paragraph for your version. No compound, dose, unit or timing changes.'],
        'git_file': REL + 'REVIEW-X1127C.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': sha},
        'whole': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': sha},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/trauma-and-addiction-why-neurological',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'REVIEW-X1127C.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A text whose Pangram tries are spent below High: my best tested version, what each '
                                     'read, and room for yours.'}},
        'suggestions': [card],
    }
    bad = ['PROBLEM ' + x for x in sr.check(review, bl)]
    (HERE / 'REVIEW-X1127C.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, bl)
    (HERE / 'REVIEW-X1127C.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1127C.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    c = card
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    out += ['## %s: %s' % (c['id'], c['title']), '', '*At %s*' % sr.where(bl, i33), '', '**As it stands:**', '',
            '> ' + now33, '', '**My best try, as it would read:**', '', '> ' + best, '',
            '**What it says:** %s' % c['what'], '', '**Why I\'m asking:** %s' % c['why'], '',
            '**Where it reads:** %s' % c['reading'], '', '**Tried:** %s' % c['tested'], '',
            '**What stays:** %s' % c['stays'], '', '**You\'re deciding:** %s' % c['deciding'], '',
            '**My advice:** %s' % c['advice_note'], '']
    (HERE / 'REVIEW-X1127C.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', i33)
    return 0


if __name__ == '__main__':
    sys.exit(main())
