#!/usr/bin/env python3
"""REVIEW.json for batch 5, marked on r04 (the article before these changes), so each card shows its change in place.

Joel's card F4-3 (2026-11-04 11:32 UTC) let me redo the TCA item around glutamine if I agreed with Gemini's new point. I
checked it first (r05/research/ACIDS-CHECK.md, gate E348): glutamine holds; no study found showing dietary malic or
citric acid fuels the gut lining; iron absorption holds (Gillooly et al. 1983); "boost stomach acid" found nothing. So:
the acids paragraph says their real use, glutamine takes his two points from his TCA rewrite, and the fuels list loses
the TCA intermediates in two places. Each changed point is a card with its reason (E348). The acids paragraph's new
sentences still read AI in three versions, so that card asks his help. No API calls."""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
R05 = HERE.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = R05.parent / 'r04' / 'r04.md'
bl = sr.blocks(MD.read_text(encoding='utf-8'))
F = json.loads((R05 / 'FUELS-r05.json').read_text(encoding='utf-8'))
RES = {}
for f in ('RESULTS.json', 'RESULTS-acids2.json', 'RESULTS-acids3.json'):
    RES.update(json.loads((R05 / 'checks' / f).read_text(encoding='utf-8')))
RES.update(json.loads((R05.parent / 'r04' / 'checks' / 'RESULTS.json').read_text(encoding='utf-8')))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-r05-20261104/articles/healing-the-gut/humanize/fix-20261103/'
strip = lambda t: re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)


def find(start):
    i = [b['i'] for b in bl if b['text'].startswith(start)]
    assert len(i) == 1, start
    return i[0]


def conf(r):
    return ', '.join('%s %s' % ('Human' if w['label'].startswith('Human') else
                                'AI-assisted' if w['label'].startswith('AI-Assisted') else 'AI', w['confidence']) for w in r['windows'])


def res(k, what=''):
    r = RES[k]
    return '%s[%s, %d%% human](%s) (%s)' % (what, r['prediction_short'], round(100 * r['fraction_human']), r['link'], conf(r))


def card(sid, title, block, after, what, why, stays, deciding, tested, reading):
    before = bl[block]['text']
    return {'id': sid, 'type': 'point', 'title': title, 'advice': 'approve',
            'spans': [{'block': block, 'start': 0, 'end': len(before)}],
            'edits': [{'block': block, 'before': before, 'after': after}], 'reads': [{'text': after, 'kind': 'p'}],
            'reads_label': 'As it would read', 'what': what, 'why': why, 'stays': stays, 'deciding': deciding,
            'advice_note': 'Approve, or Revise.', 'tested': tested, 'reading': reading}


CHECK = '[the check](' + GH + 'r05/research/ACIDS-CHECK.md)'
top, glu, tca = find('Mitochondrial and cellular energy starvation'), find('L-Glutamine ('), find('Malic and citric acid are what')
step = find('And fuel the mitochondria')
S = [card('F5-1', 'Your opening paragraph: the TCA intermediates out of the fuels list', top, strip(F['top']),
          '"(glutamine and butyrate)" for "(glutamine, butyrate, TCA intermediates)". Nothing else changes.',
          'Once the acids aren\'t one of the gut\'s fuels (card F5-3), the list shouldn\'t name them.',
          'Every word of yours but the list.', 'Whether the list should change with F5-3.',
          res('r05-fuel-top'), 'Your version read [Possibly human, 100%](https://www.pangram.com/history/3ea11eae-a6bc-492a-9e07-57dd001ce44f?ucc=4rq5Ko7gBiW) in the web app.'),
     card('F5-2', 'Glutamine, with your two points from your TCA rewrite', glu, strip(F['glutamine']),
          'Your "by pulling the tight junctions together" goes into how the cells repair the lining, and your "Glutamine '
          'also provides nitrogen to help build new cells" becomes its last sentence. Both are from your rewrite of the TCA '
          'item.',
          'Your TCA rewrite isn\'t in as it was: its first sentence calls the acids "quick energy sources for the lining cells", '
          'which is what the check found no study for (' + CHECK + '). Its two points about glutamine belong here.',
          'Your glutamine paragraph word for word, the link included.', 'Whether your two points sit right here.',
          res('r05-fuel-glutamine'), res('r04-fuel-glutamine-his', 'Your version without them: ')),
     {'id': 'F5-3', 'type': 'help', 'title': 'The acids: their real use, and the sentences that still read AI', 'advice': 'edit',
      'spans': [{'block': tca, 'start': 0, 'end': len(bl[tca]['text'])}],
      'why': 'I agree with Gemini on two of its three points, and I checked each (' + CHECK + '). Glutamine is what matters for '
             'fuel: I found no study showing that eating malic or citric acid fuels the gut lining. They do help iron '
             'absorption (Gillooly et al. 1983: 1 g of citric acid added to a rice meal took iron absorption from 0.028 to '
             '0.085, 1 g of malic acid from 0.048 to 0.095). "Boost stomach acid" I found nothing for, and acid in the '
             'stomach holds back gastrin, the hormone that drives acid secretion, so I left it out. So the paragraph now says '
             'what they are, why they come up next to glutamine, that they add little as fuel, and their use for iron, in the '
             'order a newcomer asks. I checked it with the glutamine paragraph above, since it leans on that paragraph\'s '
             'cycle (your point of 11:32). I can\'t find any more AI tells here, and I see some human tells, like these: '
             '"(which make green apples and tart cherries sour)", "partway round that same cycle", "worth having anyway". Can '
             'you help show me the tells I\'m missing? Its first sentence reads Human (Medium, in a window with glutamine\'s '
             'end); everything after it reads AI in all three versions: ' +
             '; '.join([res('r05-fuel-acids-with-glutamine', 'version 1, with glutamine: '),
                        res('r05-fuel-acids-2', 'version 2, alone: '),
                        res('r05-fuel-acids-3-with-glutamine', 'version 3, with glutamine, after the tell panel: ')]) +
             '. Alone, even the first sentence read AI. The three readers agreed on the build: claim, caveat, payoff, study '
             '([panel](' + GH + 'r05/acids/panel/PANEL.md)).',
      'advice_note': 'Rewrite it from "But nobody has shown" with Edit, or tell me the point is wrong. It has to keep: in theory a '
                     'quick fuel, but nothing shows they add much next to glutamine; their use is iron absorption, with the '
                     'study; something sour with an iron-rich meal.\n\nVersion 3, now in r05:\n' + strip(F['acids']),
      'reading': res('r05-fuel-acids-3-with-glutamine', 'Version 3 with glutamine: ')},
     card('F5-4', 'Phase 5: the TCA intermediates out of step 4', step, bl[step]['text'].replace(
          '(glutamine, butyrate and TCA intermediates)', '(glutamine and butyrate)'),
          '"(glutamine and butyrate)" for "(glutamine, butyrate and TCA intermediates)".',
          'The same change as F5-1, where the protocol points back to the fuels.', 'The rest of the step.',
          'Whether it follows F5-1.', 'A one-line pointer; not checked alone. ' + res('r05-fuel-top', 'F5-1\'s paragraph: '),
          None)]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b5-acids-20261104',
    'title': 'Gut Fuels, the Acids',
    'intro': ['Your answers on the TCA item (card F4-3) and your note about testing with the explanation nearby, put in. '
              'Gemini\'s new point was checked before anything changed; three cards change points and say why, and one asks '
              'your help with the acids\' new sentences.',
              'Three rules came from your answers: answer a reader\'s questions in the order they come (E347), change a point '
              'that doesn\'t hold up and say why (E348), and test a paragraph with the explanation it leans on (E349).'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r05/b5/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r04/r04.md', 'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-04',
    'links': {'guide': GH + 'r05/r05.md', 'review': GH + 'r05/b5/REVIEW-CARDS.md'},
    'types': {'point': {'label': 'A changed point', 'about': 'Checked, with the reason'},
              'help': {'label': 'Your help', 'about': 'Faithful rewrites still read AI'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s['advice'] == 'edit':
        out += [s['why'], '', s['advice_note'].replace('\n', '\n\n'), '', s['reading'], '']
    else:
        out += ['**As it would read:**', '', '> ' + s['reads'][0]['text'], '', '**Pangram:** ' + s['tested'], '',
                '**What changed:** ' + s['what'], '', '**Why:** ' + s['why'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
