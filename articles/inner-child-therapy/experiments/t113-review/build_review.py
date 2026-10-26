#!/usr/bin/env python3
"""Turn 113: Joel's review sheet with every edit proposed this turn, each in place in the whole guide, for him and then
GPT (his message of 2026-10-25 22:38 UTC: "do the major edits as you suggested and then i can see what GPT thinks of all
the changes"), built with tools/humanization/suggestion_review.py (REVIEW.json, REVIEW.html, REVIEW-artifact.html).

One card per section (experiments/t113-shape/proposals.py, SECTIONS.json): its case headings, the first words a heading
now says, dropped, any long paragraph split, and the one sentence moved (Start With Whatever Showed Up), shown as the
whole section would read. One card for his 109 A sentence,
and one question. Every heading or sentence with new words on the sheet is the exact text the owner-delivery gate
admitted (experiments/t113-gate/<NAME>/FOR-JOEL.txt); the build stops if one isn't.

  python3 articles/inner-child-therapy/experiments/t113-review/build_review.py"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

ARTICLE = 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/'
EXP = BLOB + 'articles/inner-child-therapy/experiments/'
MD = (ROOT / ARTICLE).read_text(encoding='utf-8')
BL = sr.blocks(MD)
SEC = json.loads((HERE.parent / 't113-shape' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']
GATE = HERE.parent / 't113-gate'
NAMES = {(k.split('|')[0], k.split('|')[1]): v for k, v in json.loads((GATE / 'NAMES.json').read_text(encoding='utf-8')).items()}
EXTRA = json.loads((HERE / 'CARDS.json').read_text(encoding='utf-8'))   # titles, notes and checks per section

TYPES = {
    'heads': {'label': 'Case headings', 'about': 'A heading over each paragraph that is its own case, so a reader can skip to theirs.'},
    'split': {'label': 'Splits', 'about': 'A long paragraph in two or more, every sentence kept.'},
    'reread': {'label': 'Wording', 'about': 'A few words changed in a sentence.'},
    'ask': {'label': 'Questions', 'about': 'A question about a line: no change until you answer.'},
}
S = []


def norm(t):
    t = re.sub(r'^>\s?', '', t.strip())
    return re.sub(r'\s+', ' ', sr.LINK.sub(r'\1', t)).strip()


def section_blocks(heading_line):
    level = len(heading_line.split(' ')[0])
    text = heading_line[level + 1:].strip()
    hits = [b['i'] for b in BL if b['level'] == level and b['text'] == text]
    assert len(hits) == 1, heading_line
    out = []
    for b in BL[hits[0] + 1:]:
        if b['level']:
            break
        out.append(b['i'])
    return hits[0], out


def admitted(sid, words):
    """The gate's delivered bytes for a new-word item; stops the build when the item isn't admitted."""
    name = NAMES[(sid, words)]
    p = GATE / name / 'FOR-JOEL.txt'
    assert p.exists(), 'not admitted by the gate: %s (%s)' % (name, words)
    return p.read_text(encoding='utf-8'), name


def card(r):
    sid = r['id']
    h, blocks = section_blocks(r['heading'])
    old = [norm(t) for t in r['old']]
    assert [norm(BL[i]['text']) for i in blocks] == old, sid
    gated = {w['new']: admitted(sid, w['new']) for w in r['new_words'] if w['kind'] == 'heading'}
    for words, (text, name) in gated.items():
        assert text == words, (name, text, words)
    # each new paragraph comes from one old one: whole, with its lead dropped, a part of a split, or with the swap
    src = []
    for x in r['new']:
        if x['kind'] != 'p':
            src.append(None)
            continue
        t = norm(x['text'])
        k = next((n for n, o in enumerate(old) if t == o or o.endswith(t[1:]) or t[1:] in o), None)
        if k is None and sid == 'W-solomon':
            k = next(n for n, o in enumerate(old) if o[:60] == t[:60])
        if k is None:   # a paragraph that a moved sentence joined (Start With Whatever Showed Up): its first sentence's own
            first = re.split(r'(?<=[.!?])\s+', t)[0]
            k = next((n for n, o in enumerate(old) if first[1:] in o), None)
        assert k is not None, (sid, t[:60])
        src.append(k)
    inserts, edits, notes = [], [], EXTRA[sid].get('notes', {})
    parts = {}
    for n, x in enumerate(r['new']):
        if x['kind'] == 'p':
            parts.setdefault(src[n], []).append(n)
    seq = 0
    for n, x in enumerate(r['new']):
        if x['kind'] == 'p':
            continue
        nxt = next(m for m in range(n + 1, len(r['new'])) if r['new'][m]['kind'] == 'p')
        k = src[nxt]
        if parts[k][0] == nxt:     # the heading stands before the old paragraph itself
            inserts.append({'before': blocks[k], 'kind': x['kind'], 'text': x['text'], 'seq': seq})
            seq += 1
    for k, ns in parts.items():
        pieces = []
        for m in range(ns[0], ns[-1] + 1):
            y = r['new'][m]
            pieces.append(('#' * int(y['kind'][1]) + ' ' + y['text']) if y['kind'] != 'p' else norm(y['text']))
        after = '\n\n'.join(pieces)
        if after != norm(BL[blocks[k]]['text']):
            edits.append({'block': blocks[k], 'before': BL[blocks[k]]['text'], 'after': after})
    reads = []
    for n, x in enumerate(r['new']):
        item = {'text': norm(x['text'])}
        if x['kind'] != 'p':
            item['kind'] = x['kind']
            if x['text'] in gated:
                item['new'] = [x['text']]
                item['note'] = 'New words (through the owner-delivery gate).'
            else:
                item['note'] = 'Your own words, from the paragraph under it.'
        elif src[n] is not None and sid != 'W-solomon':
            o, t, k = old[src[n]], norm(x['text']), src[n]
            if len(parts[k]) > 1 and n != parts[k][0]:
                item['note'] = 'Split from the paragraph before it.'
            elif t != o and o.endswith(t[1:]):
                dropped = o[:len(o) - len(t)].strip().rstrip(',.')
                item['note'] = 'Starts after "%s", which its heading now says.' % dropped
        if str(n) in notes:
            item['note'] = notes[str(n)]
        reads.append(item)
    for w in r['new_words']:
        if w['kind'] == 'sentence':
            text, name = admitted(sid, w['new'])
            k = next(n for n, x in enumerate(reads) if text in x['text'])
            reads[k]['new'] = [['and ', 'the blind spot behind it']]
    e = EXTRA[sid]
    s = {'id': sid, 'type': e['type'], 'title': e['title'], 'advice': 'approve',
         'spans': [{'block': i, 'start': 0, 'end': len(BL[i]['text'])} for i in blocks], 'card_after': blocks[-1],
         'edits': edits, 'inserts': inserts, 'moves': [], 'reads': reads,
         'reads_label': 'How %s would read' % BL[h]['text'],
         'what': e['what'], 'why': r['why'], 'stays': e['stays'], 'deciding': e['deciding'],
         'advice_note': e['advice_note'], 'found_by': e['found_by'], 'approve_label': e.get('approve_label', 'use this')}
    if e.get('warning'):
        s['warning'] = e['warning']
    S.append(s)


for r in SEC:
    card(r)

ask = EXTRA['Q-me']
i, a, z = sr.find_quote(BL, ask['quote'])
S.append({'id': 'Q-me', 'type': 'ask', 'title': ask['title'], 'advice': 'ask', 'question': ask['question'], 'why': ask['why'],
          'stays': ask['stays'], 'advice_note': ask['advice_note'], 'spans': [{'block': i, 'start': a, 'end': z}]})

review = {
    'format': sr.FORMAT, 'review_id': 'inner-child-t113', 'title': 'Inner Child Review Sheet',
    'intro': EXTRA['_intro'], 'git_file': 'articles/inner-child-therapy/experiments/t113-review/REVIEW.html',
    'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
    'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'links': {'guide': BLOB + ARTICLE, 'review': EXP + 't113-review/REVIEW.html'},
    'types': TYPES, 'suggestions': S,
}
probs = sr.check(review, BL)
for p in probs:
    print('PROBLEM', p)
assert not probs
(HERE / 'REVIEW.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
page = sr.page(review, MD, BL)
(HERE / 'REVIEW.html').write_text(page, encoding='utf-8')
(HERE / 'REVIEW-artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
print('%d cards: %s' % (len(S), ', '.join('%s (%d headings)' % (s['id'], sum(1 for x in s.get('reads', []) if x.get('kind'))) for s in S)))
