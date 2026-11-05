#!/usr/bin/env python3
"""REVIEW.json for batch 9: the fuels stretch (Leaky gut, "Mitochondrial & Cellular Energy Starvation"), marked on r12 (the
text now in his post). Joel, 2026-11-05 15:18 UTC, on the four cards I'd held in r13/fuels/CARDS-DRAFT.md: "1agree with you
/ 2agree / 3.agree / 4. go ahead", and "why did you not give me the cards as the html file in context as the repo
requires?" (gate E363 (gut): this page goes out the turn its cards are written). Each wording here was read fresh by a
newcomer (hidden_links.py, E355), checked blind for meaning against its sources (../MEANING-VERDICTS-*.json) and checked
in the web app with the paragraph it leans on (E349). The record: ../README.md. No API calls."""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R14 = HERE.parent
FIX = R14.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = FIX / 'r12' / 'r12.md'
bl = sr.blocks(MD.read_text(encoding='utf-8'))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-r07-20261104/articles/healing-the-gut/humanize/fix-20261103/'
PG = 'https://www.pangram.com/history/'
LIVE = 'https://www.pangram.com/feed/e3a65841-a626-4b34-aad7-62b9dfa48ada'
STRETCH_R12 = PG + '2103ebd9-b274-4d8c-b32a-53819d5c740d'
STRETCH_R14 = PG + '01015713-1d9b-4b32-9bd0-1f1258a1cfee'
STRETCH_R14A = PG + '8d1686ec-5214-4648-abc2-cebbeb208ebb'


def draft(name):
    return (R14 / name).read_text(encoding='utf-8').strip()


def b(start):
    i = [x['i'] for x in bl if x['text'].startswith(start)]
    assert len(i) == 1, (start, i)
    return i[0]


def card(sid, typ, title, block, pairs, why, stays, whose, reading=None, tested=None, note=None, overlaps=None):
    """pairs: [(old, new), ...]: each old occurs once in the block."""
    before = bl[block]['text']
    after, spans = before, []
    for old, new in pairs:
        assert before.count(old) == 1, (sid, old)
        s = before.index(old)
        spans.append({'block': block, 'start': s, 'end': s + len(old)})
        after = after.replace(old, new)
    c = {'id': sid, 'type': typ, 'title': title, 'advice': 'approve', 'spans': spans,
         'edits': [{'block': block, 'before': before, 'after': after}],
         'reads': [{'text': after, 'kind': 'p'}], 'reads_label': 'As it would read',
         'what': '; '.join('"%s" for "%s"' % (new, old) for old, new in pairs),
         'why': why, 'stays': stays, 'whose': whose, 'deciding': 'Whether it says what you meant.',
         'advice_note': note or 'Approve, Reject, or Revise with your own words.'}
    if reading:
        c['reading'] = reading
    if tested:
        c['tested'] = tested
    if overlaps:
        c['overlaps'] = overlaps
    return c


P20, P21, P22 = b('L-Glutamine (watch Dr. Rhonda vid)'), b('Take 5g a day as a baseline'), b('CAUTION: cancer cells')
assert (P20, P21, P22) == (27, 28, 29)
P21_NOW, P22_NOW = bl[P21]['text'], bl[P22]['text']
P21_NEW, P22_NEW = draft('DRAFT-P21-v9.txt'), draft('DRAFT-P22-v11.txt')
P21_S12 = ('Take 5g a day as a baseline. The point of that baseline is to counter the breakdown of the gut lining that '
           'high-intensity or high-volume training causes, like CrossFit or intense cardio.')
assert P21_NOW.startswith(P21_S12) and P21_NEW.endswith(P21_NOW[len(P21_S12) + 1:])

S = [
 card('F9-1', 'mine', 'Glutamine\'s three mechanism sentences', P20, [
      ("It doesn't have to go through the complicated digestive steps other nutrients do. Inside the mitochondria, it "
       "gets turned straight into alpha-ketoglutarate, or α-KG. The α-KG goes into the citric acid cycle, which is how "
       "the mitochondria make their energy.",
       "Most food has to be digested before your cells can use it, and for protein that means being broken down into "
       "amino acids. But glutamine already is an amino acid, so your enterocytes can take it in as soon as it reaches "
       "them. Their mitochondria (the part of a cell that makes its energy) turn it into alpha-ketoglutarate (a-KG). And "
       "a-KG is one of the acids in the citric acid cycle itself, the loop mitochondria make that energy with.")],
      'These three sentences were the AI windows in your post. A newcomer couldn\'t follow them: what the digestive steps '
      'are and why glutamine skips them, whose mitochondria, what alpha-ketoglutarate and the citric acid cycle are. This '
      'says each link in the order a reader asks. "Straight" goes, since it takes two steps (glutamine becomes glutamate, '
      'then a-KG: Frontiers in Medicine 2022, https://www.frontiersin.org/articles/10.3389/fmed.2022.1035335/full). '
      '"a-KG" is your own spelling. The blind meaning check passed it.',
      'Your first sentence (the video and the immune cells), and everything from "So that\'s why" on.',
      'My rewrite of the AI window (r13, last night).',
      reading='Your post, through your extension: [Mostly Human 93%%](%s), these three sentences AI Low. The stretch on '
              'its own: [AI Detected, 26%%](%s), the same three AI.' % (LIVE, STRETCH_R12),
      tested='With the paragraph it leans on: [Human Written, 100%%](%se28d97cb-50c2-4f13-89b9-ea19f2507a23), one '
             'window, High; with card F9-2\'s clause too: [Human Written, 100%%](%s7626ceb3-21e5-41b2-b9f1-53fce9a939aa).'
             % (PG, PG),
      overlaps=['F9-2']),
 card('F9-2', 'yours', '"Faster", and so "extra"', P20, [
      ('gives energy to those cells faster than eating food.',
       'gives energy to those cells faster than eating food, on top of what they get from their meals.')],
      'Your card 3 ("3.agree"): the paragraph before says the cells\' trouble is not getting enough, and "their extra '
      'energy" follows "faster", not "more". The clause ties the speed to the amount. Neither gap came up in the fresh read '
      'after it.',
      'Your sentence, and "They then use their extra energy" after it.', 'Your card 3, worded.',
      reading='The stretch in your post read Human here, inside the AI windows\' paragraph: [AI Detected, 26%%](%s).'
              % STRETCH_R12,
      tested='[Human Written, 100%%](%s7626ceb3-21e5-41b2-b9f1-53fce9a939aa), with the paragraph before it; the whole '
             'stretch: [Human Written](%s).' % (PG, STRETCH_R14),
      overlaps=['F9-1']),
 card('F9-3', 'yours', 'The 5g baseline: who it\'s for, and why training', P21, [
      (P21_S12, P21_NEW[:-(len(P21_NOW) - len(P21_S12))].rstrip())],
      'Your card 4 ("4. go ahead"). Three fresh readers asked whether the baseline is for them at all if they don\'t '
      'train, in a section about a leaky gut, and how training breaks the lining down ("I thought exercise was good"). My '
      'reading: the 5g is everyone\'s baseline, and covering hard training is its second job; your "raise it gradually" '
      'already treats the 5g as the starting point. If you meant the 5g only for people who train hard, Revise. Hard or '
      'long training sends blood away from the gut to the working muscles (van Wijck 2012, '
      'https://pubmed.ncbi.nlm.nih.gov/22517770/), while moderate exercise like walking and yoga helps the barrier '
      '(https://pmc.ncbi.nlm.nih.gov/articles/PMC12175863/). One thing I found: the trials where glutamine cut '
      'training\'s gut leak gave 0.25 to 0.9 g per kg of lean mass before a run, roughly 15 to 60g, not 5g a day '
      '(Pugh 2017, https://link.springer.com/article/10.1007/s00421-017-3744-4). Your claim stays as it is; that\'s yours '
      'to weigh.',
      'Your dose sentence ("If your immune system ... raise it gradually to 10-30g a day"), and CrossFit and intense '
      'cardio.', 'Your card 4: my fix, with its own check.',
      reading='Your post, through your extension: [Mostly Human 93%%](%s). Its first two sentences read Human Low beside '
              'the caution, twice: [AI Detected, 36%%](%s8563cfe5-5f52-43ad-903c-f5e1fdae01ca), [AI Detected, '
              '26%%](%s84f98fca-d6d3-42b8-b14e-9b8e888e5601).' % (LIVE, PG, PG),
      tested='With glutamine\'s paragraph: [Human Written, 100%%](%sa569bfb1-d815-4f9e-9498-d07fb0957a17), one '
             'window, High; the whole stretch: [Human Written, 100%%](%s), one window, High. A closing sentence of '
             'mine, "But the glutamine you swallow still gets to them, straight from inside your gut.", read Medium '
             '([Human Written](%scd90475f-4199-4cc0-b764-b3e88005929d)), so I cut it; one reader then asked how the 5g '
             'makes up for the blood, which "to keep your enterocytes fed" answers. If you want it said, Revise with '
             'that sentence back in.' % (PG, STRETCH_R14, PG),
      note='Approve, Reject, or Revise with your own words. Revise if the 5g is only for people who train hard.'),
 card('F9-4', 'yours', 'The glutamine caution, for any active cancer', P22, [(P22_NOW, P22_NEW)],
      'Your cards 1 and 2 ("1agree with you", "2agree"): any active cancer, your oncologist, the 5g too, and no '
      'portal vein (a tumor in the liver is fed mainly by the hepatic artery: '
      'https://pmc.ncbi.nlm.nih.gov/articles/PMC3036477). Fresh readers then asked how swallowed glutamine gets to a '
      'cancer when your enterocytes take it in, and why the bigger dose is worse, so it says both. Many tumors use '
      'glutamine avidly (Souba 1993, https://pubmed.ncbi.nlm.nih.gov/8257221/); the gut and liver take up 74% of a small '
      'swallowed dose on its first pass and 53% of a large one (Hankard 1995, https://pubmed.ncbi.nlm.nih.gov/7485479/); '
      'bigger oral doses raise blood glutamine more (Ziegler 1990, '
      'https://scilit.com/publications/3818c7c307b06a89e57d20b459c23ead). Three readers asked what an oncologist is; I '
      'kept the word, since the people this is for have one.',
      '"CAUTION:" and the warning itself.', 'Your cards 1 and 2, worded.',
      reading='Your post, through your extension: [Mostly Human 93%%](%s). Beside the dose: [AI Detected, '
              '36%%](%s8563cfe5-5f52-43ad-903c-f5e1fdae01ca), "So if you have an active colon or liver cancer, don\'t '
              'raise the dose that high." AI Low and the liver sentence AI Medium; my try with the liver kept: [AI '
              'Detected, 26%%](%s84f98fca-d6d3-42b8-b14e-9b8e888e5601).' % (LIVE, PG, PG),
      tested='Beside the dose paragraph (before its last sentence was cut): [Human Written]'
             '(%sb3f527c2-1d60-4d21-9135-2b53da1a9894), AI 0%%, the whole caution High; the whole stretch: [Human '
             'Written, 100%%](%s), one window, High.' % (PG, STRETCH_R14)),
 {'id': 'F9-5', 'type': 'ask', 'title': 'What readers asked about your dose sentence', 'advice': 'ask',
  'question': 'Want any of these said? Readers asked: whether pure glutamine is a powder or a pill, and with meals or '
              'apart; what an "acute exposure" is (a germ, a toxin?); which stress (illness, injury, worry?); how '
              'gradually to raise it, and how to pick between 10 and 30g. If yes, tell me the answers in your words.',
  'why': 'Six fresh readers asked these on your dose sentence. It reads Human High in every check, so I left it alone.',
  'stays': 'Your sentence, as it is.', 'advice_note': 'Answer in the box, or leave it.',
  'spans': [{'block': P21, 'start': P21_NOW.index('If your immune system'), 'end': len(P21_NOW)}]},
]
for s in S:
    s.setdefault('found_by', 'fresh newcomer reads, a blind meaning check, and the web app')
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b9-fuels-20261105',
    'title': 'Gut Article, the Fuels Stretch (Batch 9)',
    'intro': ['Your four cards, worded and checked, with my rewrite of glutamine\'s mechanism sentences from last night. '
              'All five are in the Leaky gut item, under "Mitochondrial & Cellular Energy Starvation". None is in your '
              'post yet.',
              'Each was read fresh by a newcomer, checked blind for meaning against its sources, and checked in the web '
              'app with the paragraph it leans on. The whole stretch, these four paragraphs together, now reads [Human '
              'Written, 100%%](%s), one window, High; in your post it read [AI Detected, 26%%](%s).' % (STRETCH_R14, STRETCH_R12),
              'Your answers go in as you write them. Then your post gets the update with your OK, without email. Draft A '
              '(the marks test) is still waiting for your extension\'s result; its link is in my message.'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r14/b9/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r12/r12.md',
                'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-05',
    'links': {'guide': GH + 'r12/r12.md', 'review': GH + 'r14/b9/REVIEW-CARDS.md'},
    'types': {'mine': {'label': 'My rewrite', 'about': 'An AI window, rewritten so a newcomer can follow it'},
              'yours': {'label': 'Your card', 'about': 'What you approved, worded and checked'},
              'ask': {'label': 'A question', 'about': 'Something readers asked, yours to answer'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
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
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
