"""Neuro De-Armoring Cards, 4 November (second version, after his answers "3a 4a" of 2026-11-04 10:39 UTC).

The first version (build_page_x1104_v1.py) asked his help on the two uridine paragraphs after his "Who this is for", with no
tell panel behind the asks (E253). This one has the panel and what came after it (../panel/, ../checks/x1104e and x1104f):
- the evidence paragraph (block 82): try 5, after three fresh readers listed its tells, reads Human Written;
- Scott's paragraph (block 83): Codex's rewrite (E256, ../rewrite-b083/), after five of mine read AI, reads Human Written;
then the warnings cards: the changes the two warnings checks support (../warnings/WARNINGS-CHECK.md and the bad-trips
lane's agmatine check), and the three things his answer 4a keeps, said as experience (E344). The warnings cards change
what a warning says, not how it reads; his precautions paragraph, which already read Human, was checked again with the cuts
(../checks/x1104g).

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/build_page_x1104.py
Writes REVIEW-X1104.json, .html, .artifact.html and .md here.
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/neuro-de-armoring/humanize/'
GIT_FILE = LANE + 'fix-20261104/cards/REVIEW-X1104.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
B082 = {1: 'cccbd201-be29-4717-b177-f6e88225fa3d', 2: '7cf017d1-316d-4488-a25e-d1d30b2e0baa',
        3: '97296cac-f177-4661-b7c9-b05d2cdb6e18', 4: '3e7be4a8-0cbc-4ca0-8e2c-04289e790009',
        5: '036d5dff-88a6-4533-8023-989adbd74a3b', 6: 'e36c7366-cdce-4f67-a1bf-cd61514e9fd5'}
B083 = {1: '7a3942ef-bf69-4614-a5a6-4c227e661ef4', 2: '3d8a3585-50e0-4b8a-85aa-f5db6e46ca29',
        3: '44586ae5-999d-408a-b211-051da1e2348f', 4: '2d363d6b-c10b-4ee8-9a0b-a484a2db8c98',
        5: 'e17c623b-66d3-4f9b-8e23-d8f2444df0d5', 6: 'bdc81685-fdd0-420e-b74f-1a196b1ec606'}
ROUND2 = P + '3652a572-48a6-471a-9b10-180a37fabb34'
X15 = P + '0bc718b1-278a-40ce-a7dd-6af7d45268d5'
W015 = P + '2c74da86-1945-434c-a365-6d849c787b62'
BT = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261103/articles/bad-trips/experiments/'
      't02-warnings/AGMATINE-WARNINGS-CHECK.md')
WC = BLOB + LANE + 'fix-20261104/warnings/WARNINGS-CHECK.md'
PANEL82 = BLOB + LANE + 'fix-20261104/panel/b082/PANEL.md'
PANEL83 = BLOB + LANE + 'fix-20261104/panel/b083-try5/PANEL.md'
DOI = 'https://doi.org/'
TYPES = {
    'passes': {'label': 'My version reads Human',
               'about': 'A paragraph rewritten and checked by itself: it reads Human Written. Approve it, or revise it.'},
    'warning': {'label': 'A warning the research doesn\'t back',
                'about': 'What the warnings checks found, with the sources, and the change it supports. Approve it, revise '
                         'it, or keep the post\'s wording.'},
}


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s, hits)
    return hits[0]


def swap(i, old, new):
    t = BL[i]['text']
    assert t.count(old) == 1, (i, old)
    return t.replace(old, new)


def card(sid, i, title, after, **k):
    """A one-block card: the whole block highlighted, its after-text given."""
    c = {'id': sid, 'title': title, 'advice': 'approve',
         'spans': [{'block': i, 'start': 0, 'end': len(sr.block_text(BL, i))}],
         'edits': [{'block': i, 'before': sr.block_text(BL, i), 'after': after}]}
    c.update(k)
    return c


def main():
    i82 = block_with('The tool:Uridine monophosphate (UMP).')
    i83 = block_with("Scott's signal: Scott already had choline")
    mine82 = (F / 'r3' / 'blocks' / '082.md').read_text(encoding='utf-8').strip()
    codex83 = (F / 'r3' / 'blocks' / '083.md').read_text(encoding='utf-8').strip()
    assert codex83 == (F / 'rewrite-b083' / 'DRAFT.txt').read_text(encoding='utf-8').strip()
    i15 = block_with('Precautions/Side Effects: Do not use concurrently with opioids')
    i16 = block_with('Stop immediately if it causes flatness, anhedonia')
    i18 = block_with('Rule: do not take 5-HTP on the same day as psychedelics')
    i68 = block_with('Dose: 300–600 mg/day, taken earlier in the day.')
    i73 = block_with('Either one means PS is the wrong tool for you right now.')
    i85 = block_with('Side effects / stop signs: The most common problem is the "choline headache"')
    i111 = block_with('The Mandate: You must hit 4,700 mg of Potassium daily.')
    i112 = block_with('The Source: Food Only. (Supplements are dangerous and limited to 99mg).')
    i125 = block_with('Agmatine Sulfate (Optional Trial): Start with 250–500 mg')
    i154 = block_with('Warning: Direct D-Serine carries a higher renal (kidney) load')
    i172 = block_with('Phosphatidylserine 300–600 mg earlier in the day only if you fit the high-cortisol profile')
    found = 'The warnings checks, 4 November (the bad-trips lane\'s agmatine check, and the rest in WARNINGS-CHECK.md)'
    S = [
        card('Y-82', i82, '"The tool: Uridine monophosphate (UMP). There\'s no study showing ..."', mine82, type='passes',
             approve_label='use this wording',
             what='Your post\'s evidence paragraph, uncompressed the way your "Who this is for" is: each term after its plain '
                  'meaning, the study findings said plainly with their links kept.',
             why='One paragraph at a time it read 62.2%%, 30.9%%, 0.0%% (AI Assisted) and 2.6%% AI in my first four tries. Then '
                 'three fresh readers (Codex, Sonnet and Haiku) listed its tells ([their notes](%s)), and my fifth try, with '
                 'the tells they agreed on fixed, read Human Written.' % PANEL82,
             deciding='Whether my wording of the evidence paragraph goes in.',
             stays='Every compound, the three study links and the caveat ("plausible", "carefully extrapolating", "DAWS", '
                   '"anecdotes like Scott\'s"); "potassium" is back in the rat study.',
             reading='your post\'s uridine section, AI Generated, 100%%: [round 2](%s)' % ROUND2,
             tested='this version by itself, Human Written, 0.0%% AI: [try 5](%s%s). Its windows: High on the first three '
                    'sentences, Medium on the Wurtman sentence, Low on the rat study, Medium on the last sentence. When I '
                    'tried to raise those three it read 30.3%% AI ([try 6](%s%s)), and the paragraph has used its six tries, '
                    'so another try needs your OK (question 5). The first four: [1](%s%s), [2](%s%s), [3](%s%s), [4](%s%s)'
                    % (P, B082[5], P, B082[6], P, B082[1], P, B082[2], P, B082[3], P, B082[4]),
             found_by='Paragraph checks through the API, 4 November (batches x1104a to x1104f)'),
        card('Y-83', i83, '"Scott\'s signal: Scott already had choline from eggs ..."', codex83, type='passes',
             approve_label='use this wording',
             what='Scott\'s paragraph as Codex rewrote it after five of mine read AI: the craving result first, the eggs '
                  'and the fish oil after it, the dreams last. My one change put back your post\'s "in the right person". '
                  'The label "Scott\'s signal:" and "striking" are gone, and the "synaptic-membrane / '
                  'dopamine-receptor-recovery axis" is said in plain words.',
             why='My five tries read 100%%, 100%%, 100%%, 100%% and 99.9%% AI ([1](%s%s), [2](%s%s), [3](%s%s), [4](%s%s), '
                 '[5](%s%s)). The readers\' notes on my fifth ([their notes](%s)) went to Codex with the points the '
                 'paragraph has to keep, and its first draft read Human Written.'
                 % (P, B083[1], P, B083[2], P, B083[3], P, B083[4], P, B083[5], PANEL83),
             deciding='Whether Codex\'s wording of Scott\'s paragraph goes in.',
             stays='Every point of your post\'s paragraph: choline from eggs, DHA/EPA from fish oil, a standard dose of UMP, '
                   'within a day, the vivid dreams with real childhood memories in them, the tolerance, the ketamine/LSD '
                   'cravings falling hard, that it can\'t show his D3 receptors were rebuilt overnight, and what it '
                   'suggests in the right person.',
             reading='your post\'s uridine section, AI Generated, 100%%: [round 2](%s)' % ROUND2,
             tested='this version by itself, Human Written, 0.0%% AI: [try 6](%s%s). Its windows: High on the first two '
                    'sentences, Medium on "His psychedelic tolerance seemed to drop too.", Low on the last three. It has '
                    'used its six tries too (question 5).' % (P, B083[6]),
             found_by='Paragraph checks through the API, 4 November (batches x1104a to x1104f)'),
        card('W-15', i15, '"Precautions/Side Effects: Do not use concurrently with opioids and/or kratom ..."',
             (F / 'warnings' / 'cards' / 'W015-after.md').read_text(encoding='utf-8').strip(), type='warning',
             approve_label='make these cuts',
             what='Your agmatine precautions with the cuts the agmatine check supports: MAOIs, bipolar disorder, unstable '
                  'panic disorder and the relapse line go, and nitrates and PDE-5 inhibitors go inside "blood pressure '
                  'lowering medications", which already covers them.',
             why='The bad-trips lane\'s agmatine check ([its sources](%s)): MAO doesn\'t break agmatine down, and in '
                 'rodents agmatine reduced harmaline\'s tremor; in animals it eased withdrawal and cut opioid '
                 'self-administration, the opposite of a relapse risk; nothing supports bipolar disorder or unstable '
                 'panic. Opioids and kratom, clonidine, guanfacine, blood-pressure medication and lower-end blood pressure '
                 'stay.' % BT,
             deciding='Whether those cuts go in. Pregnancy and breast-feeding, kidney or liver issues and the "psych" '
                      'stacks have nothing behind them either, but they\'re the general caution a label carries, so they '
                      'stay unless you\'d cut them too.',
             stays='Your wording: "(will reduce tolerance)", "a physician competent to consider the likelihoods of '
                   'problematic interactions", "prior psychotic episode", "lower end blood pressure".',
             reading='your version by itself, Human Written, 0.3%%: [your X-15](%s)' % X15,
             tested='this version by itself, Human Written, 0.0%% AI, one window, High: [check](%s)' % W015,
             found_by=found),
        card('W-16', i16, '"Stop immediately if it causes flatness, anhedonia, emotional blunting ..."',
             swap(i16, 'or increased craving. Do not "push through" numbness.',
                  'or increased craving. Only the stomach problems showed up in the human trials, but the flatness '
                  'happens in practice, so do not "push through" numbness.'), type='warning',
             approve_label='use this wording',
             what='One sentence says where the flatness comes from (your answer 4a): only the stomach problems showed up '
                  'in the human trials, and the flatness is from experience. The other places agmatine\'s flatness comes '
                  'up (the poor-fit line, "without flattening mood", the Void phase) stay as they are, since this says it '
                  'once.',
             why='The agmatine check found only stomach side effects in the human trials, and in animals agmatine acted '
                 'against depression ([its sources](%s)). Your answer 4a: it stays, said as experience, not as a studied '
                 'effect.' % BT,
             deciding='Whether this is how the experience gets said.',
             stays='The whole stop list, and "If agmatine makes the world more gray, it is the wrong tool for that phase."',
             found_by=found),
        card('W-125', i125, '"Agmatine Sulfate (Optional Trial): Start with 250–500 mg ..."',
             swap(i125, 'cap at 1 g/day unless clinician-supervised.', 'cap at 1 g/day.'), type='warning',
             approve_label='cut it',
             what='"unless clinician-supervised" cut from the 1 g/day cap.',
             why='The studied doses were higher, 1.3 to 3.6 g a day for up to three weeks ([the agmatine check](%s)), so '
                 'the cap is the protocol\'s own choice, and the exception for a clinician is safety language a reader '
                 'doesn\'t need (your standing wish: cut it). The Timeline\'s cap already reads this way ("Cap at 1 g/day '
                 'in this protocol.").' % BT,
             deciding='Whether "unless clinician-supervised" goes.',
             stays='The doses, the 3-day start, "without flattening mood" and the 1 g/day cap.',
             found_by=found),
        card('W-18', i18, '"Rule: do not take 5-HTP on the same day as psychedelics ..."',
             swap(i18, 'craving, and psychedelic tolerance. Do not take UMP',
                  'craving, and psychedelic tolerance; that\'s from experience, like Scott\'s below, not from studies. '
                  'Do not take UMP'), type='warning',
             approve_label='use this wording',
             what='Says that uridine changing dreams, visual sensitivity, craving and psychedelic tolerance is from '
                  'experience (your answer 4a), and points to Scott\'s case.',
             why='No study of uridine and dreams, psychedelics or tolerance turned up ([the warnings check](%s), item '
                 '13); your answer 4a keeps it, said as experience.' % WC,
             deciding='Whether this is how the experience gets said.',
             stays='The 5-HTP rule and the UMP same-day rule, word for word.',
             found_by=found),
        card('W-85', i85, '"Side effects / stop signs: The most common problem is the "choline headache" ..."',
             swap(i85, 'Side effects / stop signs: The most common problem is the "choline headache" or spaced-out brain '
                       'fog: if UMP accelerates',
                  'Side effects / stop signs: In practice, the most common problem is the "choline headache" or '
                  'spaced-out brain fog. It isn\'t in the studies, but the likely reason is that if UMP accelerates'),
             type='warning', approve_label='use this wording',
             what='The choline headache said as experience (your answer 4a), and its reason as the likely one, since '
                  'it\'s the protocol\'s guess.',
             why='No study of a choline headache on uridine turned up, and the reason (UMP speeding up membrane building '
                 'while choline is short) is the protocol\'s guess ([the warnings check](%s), item 14).' % WC,
             deciding='Whether this is how the experience gets said.',
             stays='The rest of the stop signs, and "If it makes you wired, numb, or weirdly irritable, stop. Do not push '
                   'through."',
             found_by=found),
        {'id': 'W-68', 'type': 'warning', 'title': '"Dose: 300–600 mg/day, taken earlier in the day ..."',
         'advice': 'approve', 'approve_label': 'use this dose',
         'spans': [{'block': i68, 'start': 0, 'end': len(sr.block_text(BL, i68))},
                   {'block': i172, 'start': 0, 'end': len(sr.block_text(BL, i172))}],
         'edits': [{'block': i68, 'before': sr.block_text(BL, i68),
                    'after': 'Dose: about 400 mg/day, taken earlier in the day. In the stress studies, which used a PS '
                             'complex, 400 mg blunted the cortisol response, while 200 mg did nothing and 600 or 800 mg '
                             'didn\'t either.'},
                   {'block': i172, 'before': sr.block_text(BL, i172),
                    'after': swap(i172, 'Phosphatidylserine 300–600 mg earlier', 'Phosphatidylserine about 400 mg earlier')}],
         'what': 'The PS dose as about 400 mg, the dose that worked in the stress studies, here and in the Timeline.',
         'why': 'In [Hellhammer 2004](%s10.1080/10253890410001728379), 400 mg of a PS complex blunted the cortisol '
                'response to stress and 600 and 800 mg didn\'t; in [Hellhammer 2014](%s10.1186/1476-511X-13-121), 400 mg '
                'worked only in chronically stressed men with an over-reactive stress response, and 200 mg did nothing. '
                'Small studies. The post\'s "above ~800 mg adds nothing" doesn\'t fit them: 600 mg already didn\'t work.'
                % (DOI, DOI),
         'deciding': 'Whether the dose becomes about 400 mg, in both places.',
         'stays': 'Earlier in the day, and "only if you fit the high-cortisol profile".',
         'found_by': found},
        card('W-73', i73, '"Either one means PS is the wrong tool for you right now ..."',
             swap(i73, ' (A minority also report low blood pressure, water-weight gain, or restless legs – all consistent '
                       'with cortisol going too low.)', ''), type='warning', approve_label='cut it',
             what='The last sentence cut: "(A minority also report low blood pressure, water-weight gain, or restless legs '
                  '– all consistent with cortisol going too low.)"',
             why='Nothing behind it turned up ([the warnings check](%s), item 20). If it\'s something you\'ve seen, it '
                 'stays, said as experience.' % WC,
             deciding='Whether the sentence goes.',
             stays='The stop rule and the salivary cortisol test.',
             found_by=found),
        card('W-111', i111, '"The Mandate: You must hit 4,700 mg of Potassium daily."',
             'The Target: Aim for 4,700 mg of Potassium daily.', type='warning', approve_label='use this wording',
             what='"must hit" as "aim for", and "The Mandate" as "The Target".',
             why='4,700 mg is a target for healthy people, and falling short of it doesn\'t mean you\'re deficient '
                 '([Kumssa 2021](%s10.3390/nu13041369)). It\'s also the older US figure: since 2019 the adequate intake is '
                 '3,400 mg a day for men and 2,600 mg for women ([Tufts Health & Nutrition Letter]'
                 '(https://www.nutritionletter.tufts.edu/?p=2056)).' % DOI,
             deciding='Whether "must" becomes "aim for". The 4,700 mg stays unless you\'d rather use the 2019 figures.',
             stays='The number, and "The Source: Food Only."',
             found_by=found),
        card('W-112', i112, '"The Source: Food Only. (Supplements are dangerous and limited to 99mg)."',
             'The Source: Food Only. (Supplements are limited to 99mg, and bigger doses need a doctor\'s supervision.)',
             type='warning', approve_label='use this wording',
             what='"dangerous" said as what the evidence shows: bigger doses need supervision.',
             why='In a trial of 1,200 people with implanted defibrillators, supervised potassium supplements held their '
                 'potassium high-normal and cut the main risk outcome, about 23%% against 29%% ([Danielsen 2026]'
                 '(%s10.1093/europace/euag272)). So supplements aren\'t dangerous as such; that trial\'s were supervised.'
                 % DOI,
             deciding='Whether "dangerous" goes.',
             stays='Food only, and the 99mg.',
             found_by=found),
        card('W-154', i154, '"Warning: Direct D-Serine carries a higher renal (kidney) load than L-Serine ..."',
             'Warning: High doses of D-Serine damaged the kidneys in rat studies, so it carries a kidney caution, though '
             'kidney problems have been rare in human studies. Do not exceed 30mg/kg and ensure high water intake.',
             type='warning', approve_label='use this wording',
             what='The kidney warning said as what the studies found, and the keto and high-protein sentence cut.',
             why='In rats, D-serine damages the kidneys at high doses; across the human studies one person had abnormal '
                 'kidney values, which cleared in days, and nobody has compared it with L-serine in people '
                 '([Meftah 2021](%s10.3389/fpsyt.2021.726365)). Nothing supports keto or protein adding to it '
                 '([the warnings check](%s), item 24).' % (DOI, WC),
             deciding='Whether the warning reads this way and the keto sentence goes. The 30 mg/kg stays (the highest '
                      'dose tested in people was 120 mg/kg, so it\'s a cautious choice), and so does the water; both are '
                      'your call.',
             stays='The 30mg/kg cap and the water.',
             found_by=found),
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261104-x1104b',
        'title': 'Neuro De-Armoring Cards, 4 November',
        'intro': [
            'Both uridine paragraphs after your "Who this is for" now read <b>Human Written, 0.0% AI</b> by themselves: '
            'the evidence paragraph after three fresh readers listed its tells, and Scott\'s in a rewrite by Codex after '
            'five of mine read AI.',
            'Then ten warnings cards: the cuts and softer wordings the warnings checks support, and the three things your '
            'answer 4a keeps, said as experience. These change what a warning says, not how it reads; each paragraph\'s '
            'wording gets its own Pangram check when its turn comes. Your agmatine precautions, with the cuts, still read '
            'Human.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261104/cards/REVIEW-X1104.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-X1104.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1104.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1104.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s: every card' % review['title'], '',
          'The page\'s cards as text. Built %s from [your post with your versions in](%s). To answer, use the page; or write '
          'your version under a card\'s number in a message to me.' % (review['built'], review['links']['guide']), '']
    for s in S:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '',
               '*%s*' % sr.where(BL, s['spans'][0]['block']), '']
        if s.get('reading'):
            md += ['**Pangram read:** %s' % s['reading'], '']
        if s.get('tested'):
            md += ['**This version:** %s' % s['tested'], '']
        for e in s['edits']:
            md += ['> %s' % BL[e['block']]['text'], '', '**As it would read:**', '', '> %s' % sr.blocks(e['after'])[0]['text'], '']
        md += ['**What changes:** %s' % s['what'], '', '**Why:** %s' % s['why'], '', '**What stays:** %s' % s['stays'], '',
               '**You\'re deciding:** %s' % s['deciding'], '']
    (HERE / 'REVIEW-X1104.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
