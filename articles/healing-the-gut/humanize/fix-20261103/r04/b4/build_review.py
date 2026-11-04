#!/usr/bin/env python3
"""REVIEW.json for batch 4: the TCA intermediates, the one fuels item left, marked on r04. Joel's F3-1 and F3-2 are in and
read Human through the API. The TCA item used the lineage's six tries (three before his answers; this turn the newcomer
draft, its causal version, and Codex's), each meaning-checked, and all read AI. It goes to him with the two questions the
newcomer read raised that only he can answer. No API calls."""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
R04 = HERE.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = R04 / 'r04.md'
bl = sr.blocks(MD.read_text(encoding='utf-8'))
RES = {}
for f in ('RESULTS.json', 'RESULTS-tca2.json', 'RESULTS-tca3.json'):
    RES.update(json.loads((R04 / 'checks' / f).read_text(encoding='utf-8')))
for f in ('try2/RESULTS.json', 'try3/RESULTS.json', 'checks/RESULTS.json'):
    RES.update(json.loads((R04.parent / 'r03' / f).read_text(encoding='utf-8')))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/'


def find(start):
    i = [b['i'] for b in bl if b['text'].startswith(start)]
    assert len(i) == 1, start
    return i[0]


def conf(r):
    return ', '.join('%s %s' % ('Human' if w['label'].startswith('Human') else
                                'AI-assisted' if w['label'].startswith('AI-Assisted') else 'AI', w['confidence']) for w in r['windows'])


def res(k, what):
    r = RES[k]
    return '%s: [%s, %d%% human](%s) (%s)' % (what, r['prediction_short'], round(100 * r['fraction_human']), r['link'], conf(r))


def span(block, words):
    t = bl[block]['text']
    i = t.index(words)
    return [{'block': block, 'start': i, 'end': i + len(words)}]


t = find('Malic and citric acid are what')
TXT = bl[t]['text']
tries = '; '.join([res('r03-fuel-tca', 'try 1'), res('r03-fuel-tca-t2', 'try 2'), res('r03-fuel-tca-t3', 'try 3'),
                   res('r04-fuel-tca', 'this turn, every newcomer gap answered'), res('r04-fuel-tca-2', 'the gaps as causes'),
                   res('r04-fuel-tca-3', "Codex's")])
S = [{'id': 'F4-1', 'type': 'help', 'title': 'The TCA intermediates: six versions read AI', 'advice': 'edit',
      'spans': [{'block': t, 'start': 0, 'end': len(TXT)}],
      'why': 'I can\'t find any more AI tells here, and I see some human tells, like these: "the one the glutamine ends up in", '
             '"They\'re the acids that make green apples and tart cherries sour", "clean sour stuff like that". Can you help '
             'show me the tells I\'m missing? I did what you taught: a reader who doesn\'t know the subject listed eleven links '
             'the paragraph leaves out ([the list](' + GH + 'r04/tca/links/LINKS.json)), and each version states them. '
             'Answered as definitions it read AI High; as causes, AI; Codex\'s, from the three readers\' notes, AI, with its '
             'bracketed "(TCA cycle intermediates)" at High. ' + tries + '. One difference I see: your two rewrites kept the '
             'sentences already there, two that had read AI Low among them, and changed only the stretch where the link was '
             'missing. All six of mine rewrote the whole paragraph.',
      'advice_note': 'Rewrite it with Edit, the way you did glutamine. It has to keep: malic and citric acid are TCA cycle '
                     'intermediates; they feed directly into the same energy pathway in the mitochondria as glutamine; clean '
                     'sour foods (organic malic acid, tart cherries, green apples) give the gut lining\'s cells a quick, '
                     'alternative fuel; that speeds up healing by a different biochemical route. The version on the page is '
                     'the causes one (it says each link a newcomer needs; the meaning check passed it).',
      'reading': res('r04-fuel-tca-2', 'The version in the article now')},
     {'id': 'F4-2', 'type': 'ask', 'title': 'What makes sour stuff "clean"?', 'advice': 'ask',
      'spans': span(t, 'clean sour stuff'),
      'question': 'What does "clean" leave out here: added sugar, something else, or nothing in particular? I\'d put your answer '
                  'in as a few words in the sentence.',
      'why': 'The newcomer reader asked "What makes sour stuff \'clean\', and what kind of sour stuff isn\'t clean?" Gemini\'s '
             'original says "clean, sour profiles" and no more, so I didn\'t guess.'},
     {'id': 'F4-3', 'type': 'ask', 'title': 'Along with glutamine, or instead of it?', 'advice': 'ask',
      'spans': span(t, 'another fuel'),
      'question': 'Should a reader have these sour foods along with glutamine, or are they an option for someone who doesn\'t '
                  'take glutamine? Or leave it unsaid?',
      'why': 'The newcomer reader asked "Why would my gut cells need another fuel if glutamine already does the job? ... should '
             'I have these along with glutamine or instead of it?" The original says "alternative fuel" and no more.'}]

review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b4-tca-20261104',
    'title': 'Gut Fuels, the Last One',
    'intro': ['Your glutamine and butyrate are in (r04), word for word, with the Dr. Rhonda link put back. Through the API: '
              + res('r04-fuel-glutamine-his', 'glutamine') + '; ' + res('r04-fuel-butyrate-his', 'butyrate') + '.',
              'The TCA intermediates are the only part of the fuels still reading AI. They\'ve used all six tries, three of them '
              'this turn with what you taught (gate E345: explain the links a newcomer can\'t see). One card asks your help with '
              'it, and two ask what only you know, from the newcomer read.'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r04/b4/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r04/r04.md', 'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-04',
    'links': {'guide': GH + 'r04/r04.md', 'review': GH + 'r04/b4/REVIEW-CARDS.md'},
    'types': {'help': {'label': 'Your help', 'about': 'Faithful rewrites still read AI'},
              'ask': {'label': 'A question', 'about': 'Only you know'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s['advice'] == 'ask':
        out += ['**Question:** ' + s['question'], '', s['why'], '']
    else:
        out += [s['why'], '', s['advice_note'], '', s['reading'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
