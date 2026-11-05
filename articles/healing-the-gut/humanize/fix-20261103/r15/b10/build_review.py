#!/usr/bin/env python3
"""REVIEW.json for batch 10, marked on r12 (the text now in his post): what his batch-9 answers (2026-11-05 18:43 UTC,
../../../../experiments/t14-answers/) still need his OK for, as r15 words them, and the two terms I'm not sure readers
know. Gate E363 (gut): this page goes out the turn its cards are written. Gate E364: a new page with a new review id, not
batch 9's page rebuilt.

Applied in r15 without a card, by his rule ("make sure every term is introduced once at first ... you don't need to ask
me when making those obvious changes"): every term note, and the three repeats cut (../CHANGES.json, kinds "term" and
"repeat"); his own F9-1 version of glutamine's paragraph with card F9-2's clause. They're listed on REVIEW-CARDS.md.

Each card's new words have their making-sense receipt (gate E365), cut from the stretch receipts in ../checks/. No API
calls."""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R15 = HERE.parent
FIX = R15.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

MD = FIX / 'r12' / 'r12.md'
b12 = sr.blocks(MD.read_text(encoding='utf-8'))
b15 = sr.blocks((R15 / 'r15.md').read_text(encoding='utf-8'))
assert len(b12) == len(b15)
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-r07-20261104/articles/healing-the-gut/humanize/fix-20261103/'
PG = 'https://www.pangram.com/history/'
LIVE = 'https://www.pangram.com/feed/e3a65841-a626-4b34-aad7-62b9dfa48ada'
D_R15 = PG + '626fb9ca-c769-4775-bebc-2483576c71b5'      # the fuels stretch as r15 has it (#158)
H_TRY1 = PG + 'de89477f-ceb5-4762-b6d7-87601979e4d7'     # Phase 2 with only my FODMAP note (#162)
H_OPEN = PG + 'c7517cd3-0b56-4a28-b2d0-b8c2de287a48'     # Phase 2's two changed paragraphs (#169)
H_TRY2 = PG + '31e8d763-563d-4c55-aa5f-04218bf2a721'     # Phase 2 whole (#171)
REL = 'articles/healing-the-gut/humanize/fix-20261103/r15/b10/'


def b(start):
    i = [x['i'] for x in b12 if x['text'].startswith(start)]
    assert len(i) == 1, (start, i)
    return i[0]


def block_receipt(name, stretch_receipt, i):
    """The making-sense receipt for block I as r15 has it, cut from its stretch's receipt: the block's sentences with
    their payoffs, the stretch's reader, questions, placement and checks."""
    st = json.loads((R15 / 'checks' / stretch_receipt).read_text(encoding='utf-8'))
    text = b15[i]['text'].strip()
    by = {x['s']: x for x in st['sentences']}
    r = dict(st, text=text, text_sha256=S.sha256(text), sentences=[by[s] for s in S.sentences(text)])
    probs = S.check(text, r)
    assert not probs, (name, probs)
    (HERE / name).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return REL + name


def card(sid, typ, title, blocks, why, stays, whose, what, reading, tested, receipts, note=None):
    edits, spans = [], []
    for i in blocks:
        before, after = b12[i]['text'], b15[i]['text']
        assert before != after, (sid, i)
        edits.append({'block': i, 'before': before, 'after': after})
        spans.append({'block': i, 'start': 0, 'end': len(before)})
    return {'id': sid, 'type': typ, 'title': title, 'advice': 'approve', 'spans': spans, 'edits': edits,
            'reads': [{'text': b15[i]['text'], 'kind': 'p'} for i in blocks], 'reads_label': 'As it would read',
            'what': what, 'why': why, 'stays': stays, 'whose': whose, 'deciding': 'Whether it says what you meant.',
            'advice_note': note or 'Approve, Reject, or Revise with your own words.', 'reading': reading,
            'tested': tested, 'receipt': receipts}


P21, P22 = b('Take 5g a day as a baseline'), b('CAUTION: cancer cells')
PH2, DIET = b('This is Dr. Michael Ruscio'), b('Diet-wise, go Paleo-Low FODMAP')
HRP, INTRO, GEM = b('For the most research-backed'), b('Previously, I made some posts'), b('I have consolidated the top 9')
assert (P21, P22, PH2, DIET) == (28, 29, 45, 46)

S_ = [
 card('F10-1', 'yours', 'The glutamine dose, with the research you asked for', [P21],
      'Your F9-3 ("incorporate your research to make this more accurate and useful") and F9-5 answers. What changed, and '
      'why: "to keep your enterocytes fed" says what the 5g is for, whoever you are (your card 4). Away from meals, so '
      'the amino acids in your food don\'t compete with it (your F9-5; amino acids share the gut\'s transporters, '
      'https://www.consumerlab.com/answers/must-i-take-amino-acid-supplements-on-an-empty-stomach/how_to_take_amino_acid). '
      'For hard training, how it damages the gut (the blood goes to the muscles) and what was tested: glutamine two hours '
      'before an hour\'s run in the heat cut the leak even at the lowest dose, about 15g for a 70kg man, not 5g (Pugh '
      '2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5694515/). An acute exposure is to toxins or pathogens, and you '
      'raise it a gram a day (your F9-5). 14g a day is the long-term safe level found; higher doses were only tested '
      'briefly, so it says to come back down (Shao and Hathcock 2008, https://www.nutraingredients.com/Article/2008/04/18/'
      'crn-authors-risk-assessment-for-key-amino-acids/). Active IBD came off the list for raising it: the two small '
      'trials in active Crohn\'s found no benefit (Cochrane 2016, https://www.cochrane.org/CD007348). Your 10-30g stays '
      'for the cases you named.',
      'Your 5g baseline, CrossFit and intense cardio, your 10-30g and when to go there.',
      'Your F9-3 and F9-5 answers, with my research.',
      'The dose paragraph, reworded from your answers and the research (each change and its source under Why)',
      'Your post, through your extension: [Mostly Human 93%%](%s). Batch 9\'s two checks beside the caution read its '
      'first two sentences Human Low: [AI Detected, 36%%](%s8563cfe5-5f52-43ad-903c-f5e1fdae01ca), [AI Detected, '
      '26%%](%s84f98fca-d6d3-42b8-b14e-9b8e888e5601).' % (LIVE, PG, PG),
      'The whole fuels stretch as r15 has it, 744 words with your F9-1 version and the caution below: [Human Written, AI '
      '0%%](%s), one window, High.' % D_R15,
      [block_receipt('RECEIPT-F10-1.json', 'RECEIPT-D.json', P21)]),
 card('F10-2', 'yours', 'The caution, with what to do right after the warning', [P22],
      'Your F9-4 approval, with the fix your F9-1 note asks for everywhere: the payoff first. In the version you approved, '
      'what to do (check with your oncologist) came last, after two sentences on how glutamine gets to a cancer. Now it '
      'comes right after the warning, and the how follows it. Your own caution in your F9-1 version (intestinal or liver '
      'cancers, the portal vein) was your fix of the old paragraph in your post; your later F9-4 approval kept any active '
      'cancer and no portal vein (a tumor in the liver is fed mainly by the hepatic artery, '
      'https://pmc.ncbi.nlm.nih.gov/articles/PMC3036477), so this is that one. If you meant yours, Revise with it.',
      '"CAUTION:", the warning and its reasons, word for word as you approved them.',
      'Your F9-4 approval, in the order you fix payoffs to.',
      'The approved caution\'s last sentence, what to do, moved to second',
      'Your post, through your extension: [Mostly Human 93%%](%s); beside the dose, "So if you have an active colon or '
      'liver cancer, don\'t raise the dose that high." read AI Low: [AI Detected, 36%%](%s8563cfe5-5f52-43ad-903c-'
      'f5e1fdae01ca).' % (LIVE, PG),
      'In the whole fuels stretch as r15 has it: [Human Written, AI 0%%](%s), one window, High.' % D_R15,
      [block_receipt('RECEIPT-F10-2.json', 'RECEIPT-D.json', P22)]),
 card('F10-3', 'mine', 'Phase 2 opens with what it does', [PH2, DIET],
      'Phase 2 read AI Detected 65% on its own, and its opening read AI-Generated High in your post. It\'s the issue you '
      'always fix: the point came after two doctors and their books. Now it opens with what the phase does, then whose it '
      'is, the way Phases 1, 3 and 5 open; "no harsh chemicals" is said in full; and my FODMAP note joins your "Either '
      'way" with "since" instead of splitting your "go A or B". FODMAPs are the short-chain carbs that are poorly '
      'absorbed and quickly fermented (https://pubmed.ncbi.nlm.nih.gov/23588241/).',
      'Your diet sentence, your "Either way you stop feeding the bacteria in your small intestine", and the no-snacking '
      'paragraph.',
      'My fix of the AI window in your post.',
      'The opening reordered, and the FODMAP note after your "Either way"',
      'Your post, through your extension: [Mostly Human 93%%](%s), this opening and your diet sentence AI-Generated '
      'High. Phase 2 alone with my first FODMAP note inside your sentence: [AI Detected, 65%%](%s).' % (LIVE, H_TRY1),
      'The two paragraphs: [Human Written](%s), one window, High. Phase 2 whole: [Human Written, AI 0%%](%s), Human '
      'windows, three of them Medium where it splits at "Dr.".' % (H_OPEN, H_TRY2),
      [block_receipt('RECEIPT-F10-3a.json', 'RECEIPT-H2-open.json', PH2),
       block_receipt('RECEIPT-F10-3b.json', 'RECEIPT-H2-open.json', DIET)]),
 {'id': 'F10-4', 'type': 'ask', 'title': 'What HRP stands for', 'advice': 'ask',
  'question': 'What is "HRP" in "this HRP deep research report"? Your readers won\'t know the letters, and I don\'t '
              'either. The link is a ChatGPT project named askrigor.com: if it\'s AskRigor\'s health research protocol, '
              'should it say "this deep research report I made with AskRigor", or spell HRP out? Tell me the words.',
  'why': 'Your rule: every term a reader wouldn\'t know is introduced where it first comes up. This is the one I can\'t '
         'introduce without guessing.',
  'stays': 'Your sentence, as it is, until you answer.', 'advice_note': 'Answer in the box.',
  'spans': [{'block': HRP, 'start': b12[HRP]['text'].index('HRP deep research report'),
             'end': b12[HRP]['text'].index('HRP deep research report') + len('HRP deep research report')}]},
 {'id': 'F10-5', 'type': 'ask', 'title': 'Gemini Flash Extended, or Pro?', 'advice': 'ask',
  'question': 'Your intro says you consolidate the texts so readers can consult Gemini "on Flash Extended mode", and the '
              'Gem section calls it a "Gemini Pro" Gem. Which mode should readers use? I\'d name it once, in the Gem '
              'section where they open the Gem, and cut "(on Flash Extended mode)" from the intro, whose sentence is '
              'about what this article does. Say yes, or tell me the mode.',
  'why': 'You asked whether the article repeats itself. I read it through for that: the intro and the Gem section both '
         'say you consolidated the books for Gemini, which is fine as a promise and its delivery, but they name two '
         'different modes. The other repeats I found are cut (listed on the cards file).',
  'stays': 'Both sentences, as they are, until you answer.', 'advice_note': 'Answer in the box.',
  'spans': [{'block': INTRO, 'start': b12[INTRO]['text'].index('(on Flash Extended mode)'),
             'end': b12[INTRO]['text'].index('(on Flash Extended mode)') + len('(on Flash Extended mode)')},
            {'block': GEM, 'start': b12[GEM]['text'].index('Gemini Pro'),
             'end': b12[GEM]['text'].index('Gemini Pro') + len('Gemini Pro')}]},
]
for s in S_:
    s.setdefault('found_by', 'your batch-9 answers, the making-sense read, and the web app')
CH = json.loads((R15 / 'CHANGES.json').read_text(encoding='utf-8'))
carded = {e['block'] for s in S_ for e in s.get('edits', [])}
applied = [c for c in CH if c['kind'] in ('term', 'repeat', 'his') and c['block'] not in carded]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b10-r15-20261105',
    'title': 'Gut Article, Your Batch-9 Answers (Batch 10)',
    'intro': ['Your batch-9 answers are in. Your own version of glutamine\'s paragraph went in as you wrote it, with card '
              'F9-2\'s clause. Every term a reader wouldn\'t know is now explained where it first comes up (%d notes, '
              'listed on the cards file), and the three repeats I found are cut. None of this is in your post yet.'
              % len([c for c in applied if c['kind'] == 'term']),
              'These cards are what still needs your OK: the dose with the research you asked for, the caution with its '
              'payoff first, and Phase 2, which read AI. Two questions are terms I can\'t introduce without you.',
              'Every changed stretch was checked in the web app: all twelve read Human Written, the leaky gut list and '
              'Phase 2 after a second fix (links in my message).'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r15/b10/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r12/r12.md',
                'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-05',
    'links': {'guide': GH + 'r15/r15.md', 'review': GH + 'r15/b10/REVIEW-CARDS.md'},
    'types': {'mine': {'label': 'My fix', 'about': 'An AI window in your post, fixed the way you fix them'},
              'yours': {'label': 'Your answer', 'about': 'What you answered, worded and checked'},
              'ask': {'label': 'A question', 'about': 'A term I can\'t introduce without you'}},
    'suggestions': S_,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S_:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s.get('whose'):
        out += ['*%s*' % s['whose'], '']
    if s.get('advice') == 'ask':
        out += ['**Question:** ' + s['question'], '', '**Why:** ' + s['why'], '']
        continue
    for r in s['reads']:
        out += ['**%s:**' % s['reads_label'], '', '> ' + r['text'], '']
    out += ['**Why:** ' + s['why'], '', '**Pangram read:** ' + s['reading'], '',
            '**Pangram on the suggestion:** ' + s['tested'], '', '**What stays:** ' + s['stays'], '']
out += ['## Applied without a card', '', 'Your rule (2026-11-05 18:43 UTC): "make sure every term is introduced once at '
        'first ... you don\'t need to ask me when making those obvious changes". Each line is the new words, then why.', '']
for c in applied:
    out += ['- **%s** (%s): "%s"' % (c['kind'], c['why'], c['new'][:220] + ('...' if len(c['new']) > 220 else ''))]
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(S_), 'cards;', len(applied), 'applied without a card')
