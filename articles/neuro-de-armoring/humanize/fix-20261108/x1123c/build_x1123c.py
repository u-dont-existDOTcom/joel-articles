"""The cards page of 2026-11-23, second round (review x1123c): his two warnings whose texts of mine read AI by
themselves in every try, as teaching cards (lesson bad-trips-2026-11-14b; gate bad-trips-2026-11-07c): the lion's mane
and ashwagandha item (W-LMA, five tries) and agmatine's stop signs with his lasting-anhedonia sentence (W-AGM, three
tries). The texts are x1123b/texts_x1123b.LMA8 and AGM7, the last tries.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1123c/build_x1123c.py
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
sys.path.insert(0, str(FIX / 'x1123b'))
import suggestion_review as sr  # noqa: E402
import texts_x1123b as T  # noqa: E402

BRANCH = 'claude/community-joel-1018'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1123c/'
XB = LANE + 'fix-20261108/x1123b/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
PG = 'https://www.pangram.com/history/'
LMA_TRIES = [('50622455-2e3a-482e-ac66-0ae461f68592', '93.5% AI'), ('e169798f-7c09-4000-befc-1ddd7642b40e', '98.1% AI'),
             ('f7a711fe-ad7c-40d4-be5a-5f2e3f60a684', '100% AI'), ('f39c1285-a963-4dc0-982b-ddfe3bc2dfff', '100% AI'),
             ('069a4bf5-d703-4126-8fe1-aa7542f70790', '100% AI')]
AGM_TRIES = [('1eea33ab-e9b9-4bd4-b32d-0489aec27358', '100% AI', 'the paragraph as the post has it, with the sentence for your warning added'),
             ('ce4e4e6a-64fb-467d-8750-2ed33891c429', '100% AI', 'my rewrite from the fresh reads'),
             ('4cc32d25-7fb2-41a2-a63f-21802c947517', '100% AI', 'my rewrite without the checklist the panel named')]


def main():
    bl = sr.blocks(MD, whole=True)
    (cog,) = [b['i'] for b in bl if b['text'].startswith('The armored brain projects')]
    (agw,) = [b['i'] for b in bl if b['text'].startswith('Agmatine Warning (The Voltage Governor):')]
    (stop,) = [b['i'] for b in bl if b['text'].startswith('Stop immediately if it causes flatness')]
    old = sr.block_text(bl, stop) if hasattr(sr, 'block_text') else bl[stop]['text']
    lt = '; '.join('try %d [%s](%s%s)' % (n, r, PG, u) for n, (u, r) in enumerate(LMA_TRIES, 1))
    at = '; '.join('%s [%s](%s%s)' % (w, r, PG, u) for u, r, w in AGM_TRIES)
    lma = {
        'id': 'W-LMA',
        'type': 'teach',
        'title': 'Lion\'s mane and ashwagandha: your warning, five tries, all AI',
        'advice': 'approve',
        'inserts': [{'before': agw, 'kind': 'p', 'text': T.LMA8}],
        'card_after': cog,
        'what': ('A new item in the warnings at the top, after the Cognitive Warning, for your message of 22 November: you '
                 'aren\'t advising either herb; some people report anhedonia and sexual dysfunction that last after they '
                 'stop taking them (post-ashwa or post-lion\'s mane syndrome); it\'s rare, and SSRIs and finasteride can '
                 'do the same.'),
        'why': ('I can\'t find any more AI tells here, and I see some human tells, like these: your own "not advising", '
                '"unfortunately" and "it\'s something to keep in mind", and the name people give it, with your "--". Can '
                'you help show me the tells I\'m missing? Five tries by itself, every one AI: %s. Three fresh readers '
                'marked the tells they saw in try 2 ([the panel](%s%spanel-lma3/PANEL.md)), and each later try took those '
                'out.' % (lt, BLOB, XB)),
        'reading': ('No try had a Human window: the first sentence read AI Low each time, the rest AI High (try 2, the one '
                    'the panel read: [98.1%% AI](%se169798f-7c09-4000-befc-1ddd7642b40e)).' % PG),
        'tested': ('This version (try 5) by itself: [AI Generated, 100%% AI](%s069a4bf5-d703-4126-8fe1-aa7542f70790): '
                   'its first sentence AI Low, the rest AI High. Every try with each window: [the checks](%s%schecks-1123k/'
                   'RESULTS.md) and the ones before it.' % (PG, BLOB, XB)),
        'stays': 'Everything else in the warnings, word for word.',
        'deciding': 'Your version of this item: it goes in as yours.',
        'advice_note': 'Revise, with your version: my tries read AI every time, whatever I changed.',
        'ask_because': 'downside: five Pangram tries read AI by themselves, so mine can\'t go in',
        'approve_label': 'use mine anyway',
        'found_by': 'His message of 2026-11-22 17:39 UTC; five checks in his Pangram account, 2026-11-23',
        'receipt': [XB + 'LMA8.receipt.json'],
    }
    agm = {
        'id': 'W-AGM',
        'type': 'teach',
        'title': 'Agmatine\'s stop signs with your lasting-anhedonia warning: three tries, all AI',
        'advice': 'approve',
        'spans': [{'block': stop, 'start': 0, 'end': len(old)}],
        'edits': [{'block': stop, 'before': old, 'after': T.AGM7}],
        'what': ('The agmatine warning\'s stop line, the one full list of its stop signs your 35a asked for, with your '
                 'warning that in rare reports the anhedonia lasted weeks after people stopped, so you don\'t push through '
                 'the numbness.'),
        'why': ('I can\'t find any more AI tells here, and I see some human tells, like these: "or you just stop caring", '
                '"Same if it winds you up instead", your "Unfortunately" and "hung on". Can you help show me the tells I\'m '
                'missing? Every version read AI by itself, one window, High: %s. Three fresh readers marked the tells they '
                'saw in a draft between them ([the panel](%s%spanel-agm6/PANEL.md)). This lane\'s record says a list of '
                'signs in my words reads AI however I frame it (your list fixes in the bad trips guide), so your version '
                'of this one would teach me the most.' % (at, BLOB, XB)),
        'reading': ('No try had a Human window: each read as one window, AI High (the first: [100%% AI](%s1eea33ab-e9b9-'
                    '4bd4-b32d-0489aec27358)).' % PG),
        'tested': ('This version (try 3) by itself: [AI Generated, 100%% AI](%s4cc32d25-7fb2-41a2-a63f-21802c947517), one '
                   'window, High.' % PG),
        'stays': ('The precautions before it, word for word; the cycle rule in the Glutamate Shield and Weeks 1–2 point to '
                  'this list (your 35a).'),
        'deciding': 'Your version of this paragraph: it goes in as yours, with the signs and the warning as you want them.',
        'advice_note': ('Revise, with your version. Two things my version changes in the list, so say if either should '
                        'stay: "diarrhea" is folded into "loose stools", and the old last line ("If agmatine makes the '
                        'world more gray, it is the wrong tool for that phase.") goes, since the Shield\'s "Poor fit" line '
                        'and Weeks 3–7 already say it.'),
        'ask_because': 'downside: three Pangram tries read AI by themselves, and it rewords the post\'s warning',
        'approve_label': 'use mine anyway',
        'found_by': 'His answer 35a and his message of 2026-11-22 17:39 UTC; three checks in his Pangram account, 2026-11-23',
        'receipt': [XB + 'AGM7.receipt.json'],
    }
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261123-x1123c',
        'title': 'Neuro De-Armoring Cards, 23 November (2): two of your warnings, for you to teach me',
        'intro': ['Your lion\'s mane and ashwagandha warning, and agmatine\'s stop signs with your lasting-anhedonia '
                  'sentence: every try of mine read AI by itself. It\'s the whole article, so you can read each where it '
                  'goes.', 'Two cards. No compound, dose, unit or timing changes anywhere.'],
        'git_file': REL + 'REVIEW-X1123C.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'whole': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/trauma-and-addiction-why-neurological',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'REVIEW-X1123C.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A text of mine whose Pangram tries read AI: my best tested version, the tells I see, '
                                     'and room for yours.'}},
        'suggestions': [lma, agm],
    }
    bad = ['PROBLEM ' + x for x in sr.check(review, bl)]
    (HERE / 'REVIEW-X1123C.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, bl)
    (HERE / 'REVIEW-X1123C.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1123C.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for card, text, where in ((lma, T.LMA8, 'New item after %s' % sr.where(bl, cog)),
                              (agm, T.AGM7, 'In place of %s' % sr.where(bl, stop))):
        out += ['## %s: %s' % (card['id'], card['title']), '', '*%s*' % where, '', '**As it would read:**', '',
                '> %s' % text, '', '**What it says:** %s' % card['what'], '', '**Why I\'m asking:** %s' % card['why'], '',
                '**The closest try:** %s' % card['reading'], '', '**This version:** %s' % card['tested'], '',
                '**What stays:** %s' % card['stays'], '', '**You\'re deciding:** %s' % card['deciding'], '',
                '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1123C.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', cog, agw, stop)
    return 0


if __name__ == '__main__':
    sys.exit(main())
