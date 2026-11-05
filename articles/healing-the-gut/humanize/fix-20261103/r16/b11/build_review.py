#!/usr/bin/env python3
"""REVIEW.json for batch 11, marked on r12 (the text now in his post): his F10-4 and F10-5 answers (2026-11-05 23:00 UTC,
../../../../experiments/t15-answers/) as r16 words them. F10-1 to F10-3 were approved and stay as r15 has them.
Gate E363 (gut): the page goes out the turn its cards are written. Gate E364: a new page with a new review id.

Each card's new words have their making-sense receipt (gate E365), cut from ../checks/RECEIPT-r16-*.json. The web-app
checks were predicted (#172 to #174) and wait for Pangram's sign-in in the desktop app's browser."""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R16 = HERE.parent
FIX = R16.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

MD = FIX / 'r12' / 'r12.md'
b12 = sr.blocks(MD.read_text(encoding='utf-8'))
b16 = sr.blocks((R16 / 'r16.md').read_text(encoding='utf-8'))
assert len(b12) == len(b16)
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-r16-20261105/articles/healing-the-gut/humanize/fix-20261103/'
LIVE = 'https://www.pangram.com/feed/e3a65841-a626-4b34-aad7-62b9dfa48ada'
REL = 'articles/healing-the-gut/humanize/fix-20261103/r16/b11/'
RESULTS = json.loads((R16 / 'checks' / 'RESULTS-r16.json').read_text(encoding='utf-8')) \
    if (R16 / 'checks' / 'RESULTS-r16.json').exists() else {}


def tested(key, pid, what):
    r = RESULTS.get(key)
    if not r:
        return ('Not checked yet: Pangram signed you out in the desktop app\'s browser before the check ran (my message). '
                'The prediction is frozen (%s); the check runs once you\'re signed in, and this card is updated.' % pid)
    below = [w for w in r['windows'] if w['confidence'] != 'High' or not w['label'].startswith('Human')]
    tail = 'one window, High' if len(r['windows']) == 1 and not below else (
        '%d window(s) below High: %s' % (len(below), '; '.join('"%s" %s %s' % (w['text'][:60], w['label'], w['confidence'])
                                                              for w in below)) if below else 'every window High')
    return '%s: [%s, AI %.0f%%](%s), %s (%s).' % (what, r['headline'], 100 * r['fraction_ai'], r['link'], tail, pid)


def block_receipt(name, stretch_receipt, i):
    st = json.loads((R16 / 'checks' / stretch_receipt).read_text(encoding='utf-8'))
    text = b16[i]['text'].strip()
    by = {x['s']: x for x in st['sentences']}
    r = dict(st, text=text, text_sha256=S.sha256(text), sentences=[by[s] for s in S.sentences(text)])
    probs = S.check(text, r)
    assert not probs, (name, probs)
    (HERE / name).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return REL + name


def b(start):
    i = [x['i'] for x in b12 if x['text'].startswith(start)]
    assert len(i) == 1, (start, i)
    return i[0]


def card(sid, title, blocks, why, stays, what, reading, tested_, receipts):
    edits, spans = [], []
    for i in blocks:
        before, after = b12[i]['text'], b16[i]['text']
        assert before != after, (sid, i)
        edits.append({'block': i, 'before': before, 'after': after})
        spans.append({'block': i, 'start': 0, 'end': len(before)})
    return {'id': sid, 'type': 'yours', 'title': title, 'advice': 'approve', 'spans': spans, 'edits': edits,
            'reads': [{'text': b16[i]['text'], 'kind': 'p'} for i in blocks], 'reads_label': 'As it would read',
            'what': what, 'why': why, 'stays': stays, 'whose': 'Your answer, worded.', 'deciding': 'Whether it says what '
            'you meant.', 'advice_note': 'Approve, Reject, or Revise with your own words.', 'reading': reading,
            'tested': tested_, 'receipt': receipts, 'found_by': 'your batch-10 answers'}


HRP, INTRO, GEM = b('For the most research-backed'), b('Previously, I made some posts'), b('I have consolidated the top 9')
assert (HRP, INTRO, GEM) == (17, 2, 35)
S_ = [
    card('F11-1', 'The deep research report, and where to re-check it', [HRP],
         'Your F10-4 answer: "yes it was an old version of askrigor basically, we can tell them to re-check it with '
         'askrigor.com for an up-to-date verification". "HRP" is out. AskRigor is explained where it is first named, '
         '"my research tool", since readers won\'t know it (your rule, E369), and your re-check is joined to the same '
         'sentence. Nothing says it isn\'t public yet. If "my research tool" isn\'t how you want it named, Revise.',
         'Your sentence\'s start, the link, and your glutamine sentence after it.',
         'HRP out; where the report came from and your re-check, in the same sentence',
         'Your post, through your extension: [Mostly Human 93%%](%s).' % LIVE,
         tested('r16-HRP', '#173', 'With the carnivore paragraph before it'),
         [block_receipt('RECEIPT-F11-1.json', 'RECEIPT-r16-HRP.json', HRP)]),
    card('F11-2', 'Gemini: free works, the highest thinking level is best', [INTRO, GEM],
         'Your F10-5 answer: "i just tested it with free gemini and it worked ... i\'d just tell people to use the highest '
         'thinking level they can for best answers as usual." The intro no longer names a mode ("(on Flash Extended '
         'mode)" out); the Gem section drops "Pro" and says your test and your advice after what the Gem is for, '
         'before your ask for books. The intro also has its term note from r15 ("the solvent DMSO").',
         'Both paragraphs as they were, apart from the mode.',
         'The mode named once, in the Gem section, as your answer gives it',
         'Your post, through your extension: [Mostly Human 93%%](%s).' % LIVE,
         tested('r16-A', '#172', 'The intro with the paragraphs around it') + ' ' +
         tested('r16-F', '#174', 'The Gem section with the note under it'),
         [block_receipt('RECEIPT-F11-2a.json', 'RECEIPT-r16-A.json', INTRO),
          block_receipt('RECEIPT-F11-2b.json', 'RECEIPT-r16-F.json', GEM)]),
]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b11-r16-20261105',
    'title': 'Gut Article, Your Batch-10 Answers (Batch 11)',
    'intro': ['Your three approvals (the dose, the caution, Phase 2) stay as they are. These two cards are your answers on '
              'HRP and the Gemini mode, worded. None of this is in your post yet.',
              'Once these are in, the next step is the whole article checked once (a temporary draft, never published), '
              'then your post updated with your OK and no email.'],
    'git_file': REL + 'REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r12/r12.md',
                'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-05',
    'links': {'guide': GH + 'r16/r16.md', 'review': GH + 'r16/b11/REVIEW-CARDS.md'},
    'types': {'yours': {'label': 'Your answer', 'about': 'What you answered, worded and checked'}},
    'suggestions': S_,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S_:
    out += ['## %s. %s' % (s['id'], s['title']), '', '*%s*' % s['whose'], '']
    for r in s['reads']:
        out += ['**%s:**' % s['reads_label'], '', '> ' + r['text'], '']
    out += ['**Why:** ' + s['why'], '', '**Pangram read:** ' + s['reading'], '',
            '**Pangram on the suggestion:** ' + s['tested'], '', '**What stays:** ' + s['stays'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(S_), 'cards')
