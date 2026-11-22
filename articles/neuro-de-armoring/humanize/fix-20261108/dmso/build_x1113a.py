"""Neuro De-Armoring Cards, 13 November: DMSO again, with his 1967 paper (SC-DMSOb, in place of SC-DMSO), and the ketone
strategies (SC-95, unchanged). After the paper he sent on 2026-11-13 (14:05 UTC): Ramírez & Luza 1967 gave DMSO to nine
people with severe anxiety or obsessive-compulsive disorder, so SC-DMSO's "No trial has tested it for anxiety or PTSD" was
wrong. Texts in texts_x1113a.py, sources in DMSO-PTSD.md ("His 1967 paper"); the fresh reads are needed/spdmsob,
his-fixes/spdmsob and fit/spdmsob2, each READ.md with what I did about it.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/dmso/build_x1113a.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'sci-cde'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402
import texts_x1113a as T  # noqa: E402
from build_x1108b import Q_ANS  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/dmso/'
KEY = 'SPDMSOB'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
READER = ('someone with trauma whose glutamate storms bring anxiety, rage and racing thoughts, going through the '
          'protocol\'s glutamate tools and wanting to know what each does and whether it is safe for them')
HUANG = 'https://pubmed.ncbi.nlm.nih.gov/42939788/'
TEXT = T.plain(T.NEW)
P = [T.plain(x) for x in (T.S1, T.S2, T.S3, T.S4, T.S5, T.S6, T.S7, T.S8, T.S9, T.S10)]

CARD = dict(
    id='SC-DMSOb', title='DMSO in the Glutamate Shield, with your 1967 paper',
    what='The DMSO item as before (smell it, as the Fog table says; your study\'s finding in a dish; the second dish study '
         'and young mice, so not in pregnancy or around children), now with your 1967 paper: nine people with severe '
         'anxiety or obsessive-compulsive disorder among 42 inpatients grew calmer within days on DMSO injections, with '
         'the study\'s limits. "No trial has tested it for anxiety or PTSD" becomes PTSD only.',
    why='You were right to send it: my last card said no trial had tested DMSO for anxiety, and this one did, in 1967. '
        'Read in full: in Lima, 42 psychiatric inpatients (25 with schizophrenia, four in mania, four with alcoholic '
        'psychoses, four with obsessive-compulsive disorder and five with severe anxiety) got 50 to 80%% DMSO injected '
        'into the muscle, one to five 5 ml vials a day. Agitation eased from the first doses, the anxious patients said '
        'they felt calm, and the acute cases left the hospital sooner than 16 patients with similar diagnoses on '
        'electroshock, insulin comas and the drugs of the day, about half as long for schizophrenia and the anxiety '
        'states in the paper\'s chart ([Ramírez & Luza, 1967](%s)). Its limits go '
        'in with it: no placebo (they say its smell made blinding impossible), a comparison group not picked at random, '
        'barbiturates for the most agitated in the first days, and injections, not smelling. My search had asked for '
        '"psychiatric" with DMSO and read the newest hits, and a 1967 title says "mental patients"; that\'s the lesson '
        'this time. The rest of the item is as on the last card ([Lu & Mattson, 2001](%s); [Hanslick, et al, '
        '2009](%s); and in people, IV DMSO after head injury, [Huang & Wang, 2026](%s)).'
        % (T.RAMIREZ, T.LU, T.HANSLICK, HUANG),
    stays='Your safety note at the top, the Fog table and the timeline\'s "Inhale DMSO", as they are.',
    deciding='Whether DMSO goes into the Glutamate Shield with your study, your 1967 paper and the cautions.',
    advice='Approve. I put it with the glutamate tools because that\'s what your study is about; if you\'d rather it sat '
           'by the Fog table, say so in your comment and I\'ll move it. Once you approve, I check it in Pangram before it '
           'goes in, as the new rule asks of every paragraph of mine.',
    ask='meaning: new text in the protocol: what DMSO does to glutamate and what it did for anxious patients in 1967, with '
        'a caution for pregnancy and children')

SPEC = dict(
    pays=['they learn how the protocol has them take DMSO, and at what purity',
          'they learn what DMSO did to the glutamate signals that drive their storms, and where that was shown',
          'they learn it also protected the cells from glutamate, the damage this protocol\'s glutamate tools are for',
          'they learn it has been given to people with anxiety like theirs, and when, where and how',
          'they learn what happened to those people, against what they were compared with',
          'they learn how far that study can be trusted',
          'they learn that at similar strengths it harmed brain cells too, and young brains',
          'they learn who should not use it',
          'they learn nobody knows how much reaches the brain by smelling it',
          'they learn it hasn\'t been tested for PTSD and rests on reports, which many give'],
    follows=['it opens the item, after Magnesium, the last glutamate tool',
             'it says what the dish study found',
             'it adds the dish study\'s second finding',
             'it turns from the dish to people',
             'it says what the 1967 study found',
             'it gives that study\'s limits',
             'it gives the other side',
             'it turns the other side into what to do',
             'it says how far the findings carry to smelling it',
             'it ends on what is known for PTSD'],
    links=[None, 'In rat brain cells', 'It also kept', 'Back in 1967', 'Within days they grew calmer',
           'There was no placebo', 'In a second dish study', 'So if you\'re pregnant', 'when you smell it',
           'And no trial has tested it for PTSD'],
    checked=[('DMSO suppresses NMDA- and AMPA-mediated excitotoxicity (his study)',
              'in cultured rat hippocampal neurons, DMSO at 0.5 to 1.5% reversibly suppressed glutamate, NMDA and AMPA '
              'currents and calcium influx and prevented excitotoxic death (Lu and Mattson 2001)',
              'yes: they learn what DMSO did to the glutamate signals, in a dish', 'kept'),
             ('DMSO calmed mental patients (his 1967 paper)',
              '42 inpatients in Lima, nine with severe anxiety or obsessive-compulsive neurosis, got 50 to 80% DMSO into '
              'the muscle; calmer within days, shorter hospital stays than 16 non-randomized controls; no placebo '
              '(Ramirez and Luza 1967, read in full)', 'yes: they learn what was seen in anxious people, with its limits',
              'kept'),
             ('DMSO is safe for the brain',
              'DMSO at 0.5% and 1% killed cultured rat neurons, and injections caused widespread apoptosis in the '
              'developing mouse brain (Hanslick et al. 2009); rare seizures and strokes in people given it into a vein '
              'with stem cells (PMID 17353475, 28121745)', 'yes: they learn who should not use it', 'changed'),
             ('DMSO works wonders for many people',
              'no trial of DMSO for PTSD found; his firsthand point', 'yes: they learn it rests on reports, which many '
              'give', 'kept')])


def receipt(before):
    where = sr.where(BL, before - 1).rsplit(',', 1)[0]
    r = S.make(TEXT, where, READER)
    sents = r['sentences']
    assert [x['s'] for x in sents] == P, [x['s'][:30] for x in sents]
    for x, p, f, k in zip(sents, SPEC['pays'], SPEC['follows'], SPEC['links']):
        x['payoff'] = p
        x['follows'] = f
        if 'link' in x:
            assert k and k in x['s'], (k, x['s'][:40])
            x['link'] = k
    r['opens'] = {'first_sentence': sents[0]['s'],
                  'why_reading': 'they learn the protocol has them smell DMSO, and that the item says why, among the '
                                 'glutamate tools for their storms'}
    r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in SPEC['checked']]
    r['needed'] = {'reader': 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this paragraph '
                             '(needed/spdmsob/READ.md), of the version before the read against his fixes was acted on',
                   'unneeded': [P[2], T.READ[8]],
                   'kept': {P[2]: 'they learn it protected brain cells from glutamate\'s damage, the excitotoxicity his '
                                  'study is about and this protocol\'s glutamate tools are for'}}
    r['his_fixes'] = {
        'reader': 'a fresh reader (Haiku) given tools/humanization/his_fixes_brief.md and the paragraph, one sentence a '
                  'line (his-fixes/spdmsob/READ.md)',
        'marked': [{'s': P[2], 'difference': '2'}, {'s': T.READ[4], 'difference': '1, 2'},
                   {'s': T.READ[5], 'difference': '2, 4'}, {'s': T.READ[7], 'difference': '1, 2'},
                   {'s': T.READ[8], 'difference': '4'}, {'s': T.READ[9], 'difference': '1'}],
        'kept': {P[2]: 'its citation sits at the end of the sentence, as every citation in the article does, his own '
                       'paragraphs included'}}
    r['fit'] = {'reader': 'a fresh reader (Haiku) given tools/humanization/fit_read_brief.md (the universal version) and '
                          'the text, one sentence a line (fit/spdmsob2/READ.md)',
                'marked': [{'s': P[0], 'found': 'CAN\'T TELL: the Fog table isn\'t in the excerpt'},
                           {'s': P[1], 'found': 'FROM: a dish finding, not smelling'},
                           {'s': P[2], 'found': 'FROM: a dish finding, not smelling'},
                           {'s': P[3], 'found': 'FROM: injections in 1967 inpatients, not smelling'},
                           {'s': P[4], 'found': 'FROM: compared with 1960s hospital treatments'},
                           {'s': P[6], 'found': 'FROM: dish cells and injected mice, not smelling'},
                           {'s': P[9], 'found': 'MISREAD: "many say it helps" could reassure'}],
                'kept': {P[0]: 'the Fog table is in the article, under Scenario B, where the reader sees it',
                         P[1]: 'a finding that says where it comes from, a dish, which is how far it goes; S9 says no one '
                               'has measured smelling it',
                         P[2]: 'the same dish finding, said as one; S9 names the gap to smelling it',
                         P[3]: 'says its route, injections into the muscle, and S9 names the gap to smelling it',
                         P[4]: 'the comparison is the study\'s own, named so the reader can weigh it, with its limits next',
                         P[6]: 'the harms say where they come from, and S8 turns them into what to do',
                         P[9]: 'his point, said as what people report, after the line saying no trial has tested it'}}
    r['same_point'] = ('none: read the section from its heading to the next for what DMSO does; the section names no '
                       'DMSO. The safety note at the top (block 7) covers its purity and cleanliness, and the Fog table '
                       'and the timeline (block 179) say when to smell it; this item says what it does and who should '
                       'not use it')
    r['placement'] = ('a new item after Magnesium (block %d), the last of the glutamate tools, before the Dynorphin Bridge '
                      'that turns to the Void' % (before - 1))
    r['questions'] = dict(Q_ANS)
    probs = S.check(TEXT, r)
    (HERE / ('%s.receipt.json' % KEY)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return probs


def main():
    (before,) = [x['i'] for x in BL if x['text'].startswith(T.BEFORE)]
    assert sr.block_text(BL, before - 1).startswith(T.AFTER)
    (HERE / ('%s.md' % KEY)).write_text(T.NEW + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % KEY)).write_text(TEXT + '\n', encoding='utf-8')
    bad = ['%s: %s' % (KEY, x) for x in receipt(before)]
    c = CARD
    card = {'id': c['id'], 'type': 'add', 'title': c['title'], 'advice': 'approve',
            'inserts': [{'before': before, 'kind': 'p', 'text': TEXT, 'seq': 1}], 'card_after': before - 1,
            'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'deciding': c['deciding'],
            'advice_note': c['advice'], 'ask_because': c['ask'], 'approve_label': 'add it',
            'found_by': 'The 1967 paper he sent on 2026-11-13, read in full, on top of the DMSO card of 2026-11-12',
            'receipt': [REL + '%s.receipt.json' % KEY]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261113-x1113a',
        'title': 'Neuro De-Armoring Cards, 13 November: DMSO with your 1967 paper, and the ketone strategies',
        'intro': ['The DMSO card again, now with the 1967 paper you sent: it replaces yesterday\'s DMSO card.',
                  'The ketone-strategy card is here too, unchanged, since you haven\'t answered it yet.',
                  'No compound, dose, unit or timing changes in either.'],
        'git_file': REL + 'REVIEW-X1113A.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1113A.md'},
        'types': {'add': {'label': 'Something added', 'about': 'New text you asked for, with its sources.'},
                  'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [],
    }
    prev = json.loads((HERE.parent / 'coherence' / 'ketone' / 'REVIEW-X1112B.json').read_text(encoding='utf-8'))
    assert prev['article']['sha256'] == review['article']['sha256'], 'the article changed since SC-95 was built'
    review['suggestions'] = prev['suggestions'] + [card]
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1113A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1113A.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1113A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    out += ['The ketone-strategy card, SC-95, is in [its own page](../coherence/ketone/REVIEW-X1112B.md).', '',
            '## %s: %s' % (card['id'], card['title']), '',
            '*New item after %s*' % sr.where(BL, before - 1), '', '**As it would read:**', '', '> %s' % TEXT, '',
            '**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '',
            '**What stays:** %s' % card['stays'], '', '**You\'re deciding:** %s' % card['deciding'], '',
            '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1113A.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', card['id'], 'before block', before)
    return 0


if __name__ == '__main__':
    sys.exit(main())
