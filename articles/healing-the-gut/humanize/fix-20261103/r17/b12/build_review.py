#!/usr/bin/env python3
"""REVIEW.json for batch 12, marked on r12 (the text in his post): my fixes of the windows the stretch checks left below
High, tested (r17, ../checks/). Joel, 2026-11-06 20:13 UTC: "if it's "low" we should fix it, medium you could try to fix
but if it's too difficult we can put that as a later todo when we want to learn more, and some things are not worth
fixing, pangram has some bugs". Under E373 these are the model's words he kept, so the fixes are mine, on approve cards
he can Revise. Gate E363 (gut): the page goes out the turn its cards are written; E364: a new review id."""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R17 = HERE.parent
FIX = R17.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

MD = FIX / 'r12' / 'r12.md'
b12 = sr.blocks(MD.read_text(encoding='utf-8'))
b17 = sr.blocks((R17 / 'r17.md').read_text(encoding='utf-8'))
assert len(b12) == len(b17)
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-r16-20261105/articles/healing-the-gut/humanize/fix-20261103/'
PG = 'https://www.pangram.com/history/'
REL = 'articles/healing-the-gut/humanize/fix-20261103/r17/b12/'


def block_receipt(name, stretch_receipt, i, why_reading):
    st = json.loads((R17 / 'checks' / stretch_receipt).read_text(encoding='utf-8'))
    text = b17[i]['text'].strip()
    by = {x['s']: x for x in st['sentences']}
    sents = S.sentences(text)
    r = dict(st, text=text, text_sha256=S.sha256(text), sentences=[by[s] for s in sents],
             opens={'first_sentence': sents[0], 'why_reading': why_reading})
    probs = S.check(text, r)
    assert not probs, (name, probs)
    (HERE / name).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return REL + name


def card(sid, title, blocks, why, stays, what, reading, tested, receipts):
    edits, spans = [], []
    for i in blocks:
        before, after = b12[i]['text'], b17[i]['text']
        assert before != after, (sid, i)
        edits.append({'block': i, 'before': before, 'after': after})
        spans.append({'block': i, 'start': 0, 'end': len(before)})
    return {'id': sid, 'type': 'mine', 'title': title, 'advice': 'approve', 'spans': spans, 'edits': edits,
            'reads': [{'text': b17[i]['text'], 'kind': 'p'} for i in blocks], 'reads_label': 'As it would read',
            'what': what, 'why': why, 'stays': stays, 'whose': 'My fix of a window that read below High.',
            'deciding': 'Whether it says what you meant.', 'advice_note': 'Approve, Reject, or Revise.',
            'reading': reading, 'tested': tested, 'receipt': receipts, 'found_by': 'the web app, stretch by stretch'}


BG, RS, ORG, WARN = 23, 24, 59, 82
assert b17[BG]['text'].startswith('Beta-glucans') and b17[RS]['text'].startswith('Resistant starch')
assert b17[ORG]['text'].startswith('So check your organs') and b17[WARN]['text'].startswith('Some severe symptoms')
S_ = [
    card('F12-1', 'Beta-glucans and resistant starch say what they are for', [BG, RS],
         'The resistant starch item read Human Low on its own in the leaky gut list. With its reason as a plain clause, '
         '"your body can\'t digest it, so it all goes to them", the Low was gone, but the two short items still read '
         'Medium together. Beta-glucans was the one item in the list that never said why you\'d take it. Now it does: in '
         'gut tissue taken from people, a yeast beta-glucan kept the lining from leaking when it was stressed '
         '(https://pmc.ncbi.nlm.nih.gov/articles/PMC6166688). With both, the whole list reads Human, High.',
         'Both items, your link to your note on resistant starch, and the list around them.',
         'What each item is for, said in the item',
         'The leaky gut list as r16 has it: [Human Written, the resistant starch item Low](%s47069558-4b1d-4701-a3f6-'
         'c712041f1866); with only the resistant starch fix: [Human Written, the two items Medium](%s8c06b157-bd34-48c0-'
         'ba02-9b5c3d7b4b7c).' % (PG, PG),
         'The whole list with both fixes: [Human Written, AI 0%%](%sa87802e1-d404-4a91-b2d5-ec9caebeb2e4), one window, '
         'High, 502 words (#178).' % PG,
         [block_receipt('RECEIPT-F12-1a.json', 'RECEIPT-r17-C2.json', BG,
                        'The reader learns what beta-glucans are for before deciding to buy them.'),
          block_receipt('RECEIPT-F12-1b.json', 'RECEIPT-r17-C2.json', RS,
                        'The reader learns what resistant starch does for them before anything else.')]),
    card('F12-2', 'Phase 4 opens each organ case on what you\'d have', [ORG],
         'The two organ checks read Medium as questions answered in the next sentence ("Is it ...? You\'d test for that '
         '... Or is it ...? That test is ..."). Now each case opens on what the reader would have, with its name after, '
         'and each question and its answer are one sentence. The tests and treatments are word for word.',
         '"So check your organs (Brown).", Stool Elastase, high-dose enzymes, SeHCAT, bile binders.',
         'Each organ case as one sentence that opens on the reader\'s case',
         'Phase 4 as r16 has it: [Human Written, these sentences Medium](%sd22546ab-78b1-438d-8da3-19b18cf50712).' % PG,
         'Phase 4 with the fix: [Human Written, AI 0%%](%s83c128b0-42d2-4883-8aa1-efa9f8494306), one window, High, 127 '
         'words (#176).' % PG,
         [block_receipt('RECEIPT-F12-2.json', 'RECEIPT-r17-J.json', ORG,
                        'The reader knows the next step is checking their organs, and which two.')]),
    card('F12-3', 'If you\'re pregnant: skip berberine, and why', [WARN],
         '"And if you\'re pregnant, some herbs and supplements, like berberine, aren\'t safe." read Medium: a warning that '
         'doesn\'t say what to do. Now it says what to do and why: skip berberine, which can give a newborn jaundice, and '
         'ask your doctor about the rest. NCCIH says people who are pregnant or breastfeeding should not use berberine '
         '(https://www.nccih.nih.gov/health/in-the-news-berberine), so breastfeeding is in it too.',
         'The rest of the warnings paragraph, word for word.',
         'The pregnancy line names the act and the reason',
         'The stacks as r16 has them: [Human Written, the pregnancy line Medium](%sa75a3ea5-13d9-420c-937a-8178a5f455ce).'
         % PG,
         'The stacks with the fix: [Human Written, AI 0%%](%s8ff3fe60-b777-4eb0-b49a-01db1fbe7d6a), every window High '
         'but a one-word split at "Dr.", 407 words (#177).' % PG,
         [block_receipt('RECEIPT-F12-3.json', 'RECEIPT-r17-L.json', WARN,
                        'The reader knows some symptoms mean seeing a doctor, before trying any of this.')]),
]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b12-r17-20261106',
    'title': 'Gut Article, The Windows Left Below High (Batch 12)',
    'intro': ['Every window the stretch checks left at Low or Medium, fixed and tested: each card\'s stretch now reads '
              'Human, High. What\'s left below High is Pangram splitting text at "Dr." and other abbreviations, which '
              'isn\'t worth fixing; it\'s on the later list (LATER-WINDOWS.md).',
              'Once these are in, the whole article goes in a temporary draft for your extension.'],
    'git_file': REL + 'REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r12/r12.md',
                'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-06',
    'links': {'guide': GH + 'r17/r17.md', 'review': GH + 'r17/b12/REVIEW-CARDS.md'},
    'types': {'mine': {'label': 'My fix', 'about': 'A window below High in your post, fixed the way you fix them'}},
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
