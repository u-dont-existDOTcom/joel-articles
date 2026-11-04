#!/usr/bin/env python3
"""REVIEW.json for batch 3: the rest of the mitochondrial fuels under Leaky gut, marked on r03. Joel rewrote the first
paragraph and said "i didn't do all of it, you can finish" (2026-11-04 00:37 UTC). Built his way (gate E342), the dose and
the cancer caution read Human. Glutamine's mechanism, butyrate and the TCA intermediates still read AI after three tries
each, a blind meaning check on every try, and three fresh readers. These are stretches for him to edit, in his words (his
saved rule for help requests). No API calls."""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
R03 = HERE.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = R03 / 'r03.md'
md = MD.read_text(encoding='utf-8')
bl = sr.blocks(md)
RES = {}
for f in ('checks/RESULTS.json', 'try2/RESULTS.json', 'try3/RESULTS.json'):
    RES.update(json.loads((R03 / f).read_text(encoding='utf-8')))
TXT = {}
for d in ('checks', 'try2', 'try3'):
    TXT.update(json.loads((R03 / d / 'TEXTS-to-check.json').read_text(encoding='utf-8')))
BASE = json.loads((R03.parent / 'baseline' / 'RESULTS.json').read_text(encoding='utf-8'))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/r03/'
PANEL = GH + 'try2/panel/fuels-t2/PANEL.md'


def find(start):
    i = [b['i'] for b in bl if b['text'].startswith(start)]
    assert len(i) == 1, start
    return i[0]


def conf(r):
    return ', '.join('%s %s (%sw)' % ('Human' if w['label'].startswith('Human') else
                                      'AI-assisted' if w['label'].startswith('AI-Assisted') else 'AI', w['confidence'], w['words'])
                     for w in r['windows'])


def tries(keys):
    out = []
    for n, k in enumerate(keys, 1):
        r = RES[k]
        out.append('try %d: [%s, %d%% human](%s) (%s)' % (n, r['prediction_short'], round(100 * r['fraction_human']), r['link'], conf(r)))
    return '; '.join(out)


def reading():
    r = BASE['GH-12']
    return ('Your post as it was, the whole Leaky gut item: %s, %d%% human, your part High and this stretch AI. '
            '[Pangram result](%s)' % (r['prediction_short'], round(100 * r['fraction_human']), r['link']))


ASK = 'I can\'t find any more AI tells here, and I see some human tells, like these: %s. Can you help show me the tells I\'m missing? '
S = []
g = find('L-Glutamine (watch Dr. Rhonda vid)')
gk = ['r03-fuel-glutamine', 'r03-fuel-glutamine-t2', 'r03-fuel-glutamine-t3']
S.append({'id': 'F3-1', 'type': 'help', 'title': 'Glutamine: how it turns into energy, and what that does', 'advice': 'edit',
          'spans': [{'block': g, 'start': 0, 'end': len(bl[g]['text'])}],
          'why': ASK % '"(watch Dr. Rhonda vid)", "It doesn\'t have to go through the complicated digestive steps other nutrients do"' +
          'Its first sentence reads Human (High in try 3). The mechanism and the closing sentence read AI in all three tries: '
          'chained ("which feeds ..., where ..."), split into one step a sentence, and with only the closing sentence changed, '
          'which made that sentence read AI High. ' + tries(gk) + '. All three fresh readers named the closer ("So your cells '
          'get that energy right away", "and that keeps LPS from getting through") and the same fuel, then mechanism, then '
          'benefit order in every item ([panel](' + PANEL + ')).',
          'advice_note': 'Rewrite the last two or three sentences with Edit (from "Inside the mitochondria"), the way you did the first '
                         'paragraph, and I\'ll do butyrate and the TCA intermediates the way yours is built. It has to keep: it '
                         'skips the complicated digestive steps; it turns straight into alpha-ketoglutarate (α-KG) inside the '
                         'mitochondria; α-KG feeds the citric acid cycle; the cells get the energy right away; that drives the '
                         'repair of the gut lining and keeps LPS from getting through.\n\nMy try 2, the closest (40% human):\n' +
                         TXT['r03-fuel-glutamine-t2'],
          'reading': reading()})
b = find('Butyrate and the other short-chain')
bk = ['r03-fuel-butyrate', 'r03-fuel-butyrate-t2', 'r03-fuel-butyrate-t3']
S.append({'id': 'F3-2', 'type': 'help', 'title': 'Butyrate: the colon\'s fuel', 'advice': 'edit',
          'spans': [{'block': b, 'start': 0, 'end': len(bl[b]['text'])}],
          'why': ASK % '"your home-brewed SIBO yogurt", "raw resistant starch", and your own "the colonocytes lining your large '
                       'intestine"' +
          'All three tries read AI: the "the way your small intestine runs on glutamine" comparison, then a plain "but", then '
          'a trailing "while"; the effects packed into one sentence, then split, then folded into one "Besides ..." sentence. ' +
          tries(bk) + '.',
          'advice_note': 'Rewrite it with Edit if you like; otherwise I\'ll redo it the way your glutamine rewrite is built. It has '
                         'to keep: the small intestine runs on glutamine and the large intestine on SCFAs like butyrate; you get '
                         'them from your gut bacteria fermenting raw resistant starch, or from your home-brewed SIBO yogurt; they '
                         'fuel the colonocytes, lock down the lower gut barrier and keep suppressing inflammatory signals.\n\nMy '
                         'try 3:\n' + TXT['r03-fuel-butyrate-t3'],
          'reading': reading()})
t = find('TCA cycle intermediates, like malic')
tk = ['r03-fuel-tca', 'r03-fuel-tca-t2', 'r03-fuel-tca-t3']
S.append({'id': 'F3-3', 'type': 'help', 'title': 'The TCA cycle intermediates: sour foods as fuel', 'advice': 'edit',
          'spans': [{'block': t, 'start': 0, 'end': len(bl[t]['text'])}],
          'why': ASK % '"clean sour stuff", "The TCA cycle is another name for the citric acid cycle"' +
          'Opening with that plain definition (your first move) read Human in try 2; the rest read AI, and in try 3, which '
          'began with the foods ("The point of eating clean sour stuff ..."), the whole item read AI High. ' + tries(tk) + '.',
          'advice_note': 'Rewrite it with Edit if you like; otherwise I\'ll redo it the way your glutamine rewrite is built. It has '
                         'to keep: malic and citric acid are TCA cycle intermediates and feed directly into the same mitochondrial '
                         'energy pathways as glutamine; clean sour foods (organic malic acid, tart cherries, green apples) give the '
                         'gut lining\'s cells a quick, alternative fuel; that speeds up healing by a different biochemical route.'
                         '\n\nMy try 2, the closest (17% human):\n' + TXT['r03-fuel-tca-t2'],
          'reading': reading()})

dose = RES['r03-fuel-dose-caution']
his = RES['r03-st2-his']
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b3-fuels-20261104',
    'title': 'Gut Fuels, the Rest',
    'intro': ['Your batch-2 answers are in (r03): S2-1, S2-3, S2-4 and S2-5 as you approved them, your S2-2, and your first fuels '
              'paragraph word for word. Your S2-2 reads [Human, %d%%](%s) (%s).' % (round(100 * his['fraction_human']), his['link'], conf(his)),
              'I built the rest of the fuels the way your paragraph is built (a plain definition first, one step a sentence, each '
              'gloss in the sentence, plain verbs; gate E342), each part checked blind for meaning. The glutamine dose and the '
              'cancer caution read [Human, %d%%](%s) (%s). Its last sentence, on the liver, is at Low.' % (
                  round(100 * dose['fraction_human']), dose['link'], conf(dose)),
              'Three parts still read AI after three tries each and three fresh readers: glutamine\'s mechanism, butyrate, and the '
              'TCA intermediates. In every try, the sentence that names the thing in plain words reads Human, and the sentences '
              'that explain the mechanism or state the benefit read AI. Rewriting glutamine\'s last sentences would show me how you '
              'do those.'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r03/b3/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r03/r03.md', 'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-04',
    'links': {'guide': GH + 'r03.md', 'review': GH + 'b3/REVIEW-CARDS.md'},
    'types': {'help': {'label': 'Your help', 'about': 'Faithful rewrites still read AI'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '', s['why'], '', s['advice_note'].replace('\n', '\n\n'), '', s['reading'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
