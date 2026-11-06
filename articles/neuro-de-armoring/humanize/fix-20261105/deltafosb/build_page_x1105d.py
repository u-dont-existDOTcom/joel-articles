"""Neuro De-Armoring Cards, 5 November (3): the four ΔFosB fixes from the deep pass of Joel's message of 2026-11-05
23:02 UTC ("neuro de-armoring ΔFosB deep pass"). Every claim and every source is in DELTAFOSB-CHECK.md beside this
script. Gate E348: a supporting point that doesn't hold is checked against a source, changed to what holds, and put to
him on a card with its reason and source; the larger argument it serves is his, so whether ΔFosB is the article's armor
at all is question 9 on the questions page, not a card here.

No Pangram reading on these four: the API has had no credits since 2026-11-04 (HTTP 402) and the web-app route needs his
browser, which this session can't reach. Predictions are in the ledger; the checks run the next turn that has a route.

  python3 articles/neuro-de-armoring/humanize/fix-20261105/deltafosb/build_page_x1105d.py
Writes REVIEW-X1105D.json, .html, .artifact.html and .md in cards/ here.
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
CARDS = HERE / 'cards'
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/neuro-deltafosb-20261105/'
LANE = 'articles/neuro-de-armoring/humanize/'
GIT_FILE = LANE + 'fix-20261105/deltafosb/cards/REVIEW-X1105D.html'
CHECK = BLOB + LANE + 'fix-20261105/deltafosb/DELTAFOSB-CHECK.md'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)

VIALOU = 'https://pubmed.ncbi.nlm.nih.gov/20473292/'
NESTLER08 = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC2607320'
NESTLER14 = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4380559'
ZACH = 'https://pubmed.ncbi.nlm.nih.gov/16415864/'
ROBISON = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8879420'
LOBO = 'https://www.nature.com/articles/npp201788'

TYPES = {
    'source': {'label': 'A point that doesn\'t match its source',
               'about': 'Something the article asserts that the research says differently, changed to what the sources '
                        'support, with the sources on the card. Keep the change, or edit the paragraph your way.'},
    'add': {'label': 'Something the section is missing',
            'about': 'A mechanism the section implies the other way round. Add it, or leave the section as it is.'},
}


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s, hits)
    return hits[0]


def main():
    i49 = block_with('The Hardening: Chronic cycles')
    t49 = sr.block_text(BL, i49)
    i46 = block_with('The Problem: To protect itself')
    t46 = sr.block_text(BL, i46)
    i33 = block_with('In this state, functional IQ')
    t33 = sr.block_text(BL, i33)
    i183 = block_with('Week 8+')
    t183 = sr.block_text(BL, i183)

    a49 = ('The Hardening: Chronic cycles lead to the accumulation of DeltaFosB, a protein switch that alters gene '
           'expression and holds the circuitry in place for weeks after the cycles stop '
           '([Nestler, 2008](%s)).' % NESTLER08)
    a46 = (t46 + ' The two aren\'t one mechanism, though: DeltaFosB accumulates inside the dynorphin neurons '
           'themselves, and what it does there is turn dynorphin down, not up ([Zachariou, et al, 2006](%s)).' % ZACH)
    a33 = t33.replace('with the exact cocktail of catecholamines that transcribes',
                      'with the catecholamines that transcribe')
    a183 = t183.replace('DeltaFosB degraded.', 'DeltaFosB degraded, if the animal timelines carry over.')
    assert a33 != t33 and a183 != t183

    def receipt(cid):
        return '%s%s' % (LANE + 'fix-20261105/deltafosb/receipts/', cid + '.json')

    S = [
        {'id': 'DFB-1', 'type': 'source',
         'title': '"a protein switch that permanently alters gene expression ... (Vialou, et al, 2010)"',
         'advice': 'approve', 'approve_label': 'use this wording',
         'spans': [{'block': i49, 'start': t49.index('a protein switch'), 'end': len(t49)}],
         'edits': [{'block': i49, 'before': t49, 'after': a49}],
         'what': 'Two changes in one sentence: "permanently" goes, and the citation changes.',
         'why': 'The paper cited here found close to the opposite. Vialou, et al, 2010 is about resilience: the mice '
                'that came through ten days of social defeat best were the ones with the most DeltaFosB in the nucleus '
                'accumbens, raising it there was both necessary and sufficient for that resilience, and fluoxetine '
                'needed it to work at all. In the human arm of the same paper, people who had been depressed had '
                'roughly half as much DeltaFosB in the accumbens as controls -- less, not more. '
                '([The paper](%s).) So it can\'t be the source for DeltaFosB cementing trauma circuitry. The '
                'accumulation claim itself does hold, from the addiction side, and that is what the new citation '
                'points to ([Nestler, 2008](%s)). "Permanently" is separately wrong, and your own Week 8+ line '
                'already says so: the measured half-life is up to about 8 days in living animals, and the protein '
                'persists for at least several weeks after the stimulus stops -- the longest anything ran was 28 days '
                '([review](%s)).' % (VIALOU, NESTLER08, ROBISON),
         'stays': 'The hardening, the accumulation, the protein-switch framing, and the sentence\'s place in section C.',
         'advice_note': 'Use this wording. Whether the opposite finding goes into the article as well is question 9 -- '
                        'that one changes what the section argues, so it\'s yours to call, not mine.',
         'receipt': receipt('DFB-1'),
         'deciding': "Whether to keep the hardening claim with a citation that supports it and no \"permanently\", or to say something different about DeltaFosB altogether (question 9).",
         'found_by': 'The DeltaFosB deep pass, 5 November ([every claim and source](%s))' % CHECK},
        {'id': 'DFB-2', 'type': 'add',
         'title': 'Dynorphin and DeltaFosB read as partners here, and they aren\'t',
         'advice': 'approve', 'approve_label': 'add it',
         'spans': [{'block': i46, 'start': 0, 'end': len(t46)}],
         'edits': [{'block': i46, 'before': t46, 'after': a46}],
         'what': 'One sentence at the end of the paragraph.',
         'why': 'The heading puts Dynorphin and DeltaFosB together and the section has them doing the same job -- '
                'dynorphin making the Void, DeltaFosB cementing it. In the animal work they pull against each other on '
                'that exact point: DeltaFosB in the accumbens produces its opiate-addiction phenotype partly by '
                'repressing dynorphin expression ([Zachariou, et al, 2006](%s)). What makes it easy to conflate is '
                'that the standard way of studying DeltaFosB puts it in the dynorphin-positive neurons, so the two are '
                'in the same cells -- in the same place, doing opposite things. A reader who takes them as allies will '
                'be wrong about why the Void lifts.' % ZACH,
         'stays': 'Everything you wrote about dynorphin, the chemical blanket, and the Void.',
         'advice_note': 'Your call. It makes section C more accurate and slightly more crowded. If you\'d rather keep '
                        'the section clean, the heading and the Void story still work -- it\'s the implied teamwork '
                        'that doesn\'t.',
         'receipt': receipt('DFB-2'),
         'deciding': "Whether section C tells the reader how dynorphin and DeltaFosB actually relate, or stays as it is.",
         'found_by': 'The DeltaFosB deep pass, 5 November ([every claim and source](%s))' % CHECK},
        {'id': 'DFB-3', 'type': 'source',
         'title': '"the exact cocktail of catecholamines that transcribes new DeltaFosB proteins"',
         'advice': 'approve', 'approve_label': 'use this wording',
         'spans': [{'block': i33, 'start': t33.index('with the exact cocktail'),
                    'end': t33.index('that transcribes') + len('that transcribes')}],
         'edits': [{'block': i33, 'before': t33, 'after': a33}],
         'what': '"the exact cocktail of catecholamines" becomes "the catecholamines".',
         'why': 'That chronic stress drives DeltaFosB up in the nucleus accumbens is well supported -- restraint '
                'stress, unpredictable stress and social defeat all do it ([review](%s)). "The exact cocktail" claims '
                'a precision none of the work gives: nobody has identified a specific catecholamine mixture that does '
                'the transcribing. Cutting two words fixes it and the sentence keeps its force.' % NESTLER14,
         'stays': 'The red line, the flooding, the armor label, and The Takeaway after it.',
         'advice_note': 'Use this wording. The "(the \'armor\')" label in the same sentence is the bigger question, '
                        'and it\'s question 9.',
         'receipt': receipt('DFB-3'),
         'deciding': "Whether the sentence claims a specific catecholamine mixture or just the catecholamines.",
         'found_by': 'The DeltaFosB deep pass, 5 November ([every claim and source](%s))' % CHECK},
        {'id': 'DFB-4', 'type': 'source',
         'title': '"Week 8+: The BaselineState: DeltaFosB degraded."',
         'advice': 'approve', 'approve_label': 'use this wording',
         'spans': [{'block': i183, 'start': t183.index('DeltaFosB degraded.'),
                    'end': t183.index('DeltaFosB degraded.') + len('DeltaFosB degraded.')}],
         'edits': [{'block': i183, 'before': t183, 'after': a183}],
         'what': 'Four words added, so the eight weeks reads as the protocol\'s estimate rather than a measurement.',
         'why': 'Week 8 is inside what the research supports, which is the good news: the protein persists for at '
                'least several weeks after the stimulus stops, with a half-life up to about 8 days in living animals, '
                'and the longest persistence measured was 28 days ([review](%s)). What doesn\'t exist is any human '
                'de-armoring timeline, or any measurement of DeltaFosB clearing in a person on this protocol. As it '
                'stands the line reads like a clock someone has checked.' % ROBISON,
         'stays': 'The week number, the phase name, and "Hardware reset complete."',
         'advice_note': 'Your call on the wording -- you may want it shorter, or the hedge somewhere else in the '
                        'timeline rather than in this line. The eight weeks itself I\'d keep: nothing contradicts it.',
         'receipt': receipt('DFB-4'),
         'deciding': "Whether the Week 8 line reads as a measured date or as the protocol's estimate.",
         'found_by': 'The DeltaFosB deep pass, 5 November ([every claim and source](%s))' % CHECK},
    ]

    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261105-x1105d',
        'title': 'Neuro De-Armoring Cards, 5 November (3): the DeltaFosB pass',
        'intro': [
            'Your "ΔFosB deep pass" of 23:02 UTC. I went through every place the article says something about '
            'DeltaFosB -- nine of them -- against the primary papers, including the one the article cites.',
            'Four cards here. The big one is DFB-1: the study cited for DeltaFosB cementing trauma circuitry found '
            'close to the opposite, that DeltaFosB in the nucleus accumbens goes with resilience and that depressed '
            'people have less of it. That one has a question behind it, question 9 on the questions page, because it '
            'touches what the article argues rather than how a sentence is worded, and that part is yours.',
            'Two things I checked and would leave exactly as they are: your "DeltaFosB may be the master switch, but '
            'the research isn\'t settled" -- of the nine places that is the one the evidence matches -- and the '
            'ketones step, since beta-hydroxybutyrate really is a class I HDAC inhibitor at the concentrations the '
            'protocol produces.',
            'No compound, dose, unit, timing or warning is touched by any of this. No Pangram reading on these four '
            'yet: the API has had no credits since yesterday and the web-app route needs your browser, so the '
            'predictions are recorded and the checks run next turn.',
        ],
        'git_file': GIT_FILE,
        'article': {'file': 'articles/neuro-de-armoring/humanize/HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + GIT_FILE},
        'types': TYPES,
        'suggestions': S,
    }
    CARDS.mkdir(parents=True, exist_ok=True)
    probs = sr.check(review, BL)
    for x in probs:
        print('PROBLEM', x)
    (CARDS / 'REVIEW-X1105D.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (CARDS / 'REVIEW-X1105D.html').write_text(page, encoding='utf-8')
    (CARDS / 'REVIEW-X1105D.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s: every card' % review['title'], '',
          'The page\'s cards as text. Built %s from [your post as it stands](%s), against the sources in '
          '[the DeltaFosB check](%s). To answer, use the page; or write your answer under a card\'s number in a '
          'message to me.' % (review['built'], review['links']['guide'], CHECK), '',
          'No Pangram reading on any of these yet: the API has had no credits since 2026-11-04 and the web-app route '
          'needs your browser, which this session can\'t reach. The predictions are in the ledger and the checks run '
          'the next turn that has a route.', '']
    for s in S:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '',
               '*%s*' % sr.where(BL, s['spans'][0]['block']), '']
        sp = s['spans'][0]
        md += ['> %s' % BL[sp['block']]['text'][sp['start']:sp['end']], '',
               '**What changes:** %s' % s['what'], '',
               '**As it would read:** %s' % s['edits'][0]['after'], '',
               '**Why:** %s' % s['why'], '',
               '**What stays:** %s' % s['stays'], '',
               '**You\'re deciding:** %s' % s['deciding'], '',
               '**My ask:** %s' % s['advice_note'], '']
    md += ['## Question 9, which is not a card', '',
           'Whether DeltaFosB is the article\'s armor at all. The three ways to go are on '
           '[the questions page](%s), with what each one costs.' % (BLOB + LANE + 'OWNER-QUESTIONS.md'), '']
    (CARDS / 'REVIEW-X1105D.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
