"""Round 1 of the bad-trips guide: the structure question and the repeats, as a marking page for Joel.

Every card works on his published words (original-page.md, the review-page form of original.md). Nothing here adds
words of mine to his text except where a card says so; the cuts and moves are proposals until he approves them. The
cards come from the three fresh readers' reports beside this folder (../../experiments/t01-repeats/READER-A.md,
READER-B.md, READER-C-SAFETY.md) and my own read, each checked against the article before it went in.

  python3 articles/bad-trips/review/r01/build_r01.py     (from the repo root)

writes REVIEW-R01.json, REVIEW-R01.html (the page), REVIEW-R01.artifact.html (what is published) and REVIEW-R01.md
(the cards as text, for GitHub) beside this file.
"""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
ART = HERE.parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402

MD_PATH = ART / 'original-page.md'
MD = MD_PATH.read_text(encoding='utf-8')
BL = SR.blocks(MD)
MAP = json.loads((ART / 'original-page-map.json').read_text(encoding='utf-8'))['map']


def P(bid, k=0):
    """The page index of the k-th page block of B id BID (a list B id has one page block per item)."""
    return MAP[bid][k]


def T(i):
    return BL[i]['text']


def whole(i):
    return {'block': i, 'start': 0, 'end': len(T(i))}


def span_of(i, quote):
    t = T(i)
    k = t.find(quote)
    if k < 0:
        raise SystemExit('quote not in block %d: %r\n  block: %r' % (i, quote, t[:300]))
    return {'block': i, 'start': k, 'end': k + len(quote)}


def cut_block(i):
    return {'block': i, 'before': T(i), 'after': ''}


def cut_words(i, quote):
    """Block i with QUOTE taken out, spacing tidied (a whole sentence, so no capital needs fixing)."""
    t = T(i)
    assert t.count(quote) == 1, (i, quote)
    after = t.replace(quote, '')
    after = re.sub(r'  +', ' ', after).strip()
    after = re.sub(r'\s+([.,;:])', r'\1', after)
    return {'block': i, 'before': t, 'after': after}


def replace_words(i, old, new):
    t = T(i)
    assert t.count(old) == 1, (i, old)
    return {'block': i, 'before': t, 'after': t.replace(old, new)}


TYPES = {
    'structure': {'label': 'Structure', 'about': 'how the quick version and the long version split the guide, and where '
                  'a part goes'},
    'repeat': {'label': 'Said twice', 'about': 'a point the guide already makes elsewhere: one copy goes, the other stays'},
    'safety': {'label': 'Safety in one place', 'about': 'a caution or call-for-help line said in several places, or one '
               'that changes nothing a reader does'},
    'question': {'label': 'Your call', 'about': 'something only you can decide or know'},
}

CARDS = []


def card(**kw):
    CARDS.append(kw)


exec((HERE / 'cards_r01.py').read_text(encoding='utf-8'))


BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261103/'


def marked(j, spans):
    t = T(j)
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


def cards_md(review):
    """The page's cards as text, for GitHub (he never gets sent to the JSON)."""
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide as published](%s) (its '
           'Markdown here: [original.md](%s)). To answer, use the page; or write your answer under a card\'s name in a '
           'message to me.' % (review['built'], review['links']['guide'], BLOB + 'articles/bad-trips/original.md'), '']
    for s in review['suggestions']:
        first = (s.get('spans') or [{}])[0].get('block')
        where = SR.where(BL, first) if first is not None else ''
        out += ['## %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '', '*%s*' % where, '']
        if s['advice'] == 'ask':
            out += ['**Question:** %s' % s['question'], '', '**Why:** %s' % s['why'], '']
            if s.get('stays'):
                out += ['**Until you answer:** %s' % s['stays'], '']
            out += ['**My pick:** %s' % s['advice_note'], '']
            continue
        out += ['**What changes:** %s' % s['what'], '']
        for e in s.get('edits', []):
            out += ['**Now** (the words it changes in bold):', '', '> %s' % marked(e['block'], s['spans']), '']
            out += (['**How it would read:**', '', '> %s' % e['after'], ''] if e['after'] else
                    ['**How it would read:** this paragraph goes.', ''])
        for mv in s.get('moves', []):
            out += ['**Moves** to just before "%s":' % SR.first_words(T(mv['before'])), '']
            out += ['> %s' % T(i) for i in mv['blocks']] + ['']
        for ins in s.get('inserts', []):
            out += ['**New heading** (%s, the words are yours, from the heading it replaces): %s' % (ins['kind'], ins['text']), '']
        out += ['**Why:** %s' % s['why'], '', '**What stays:** %s' % s['stays'], '',
                '**For you to weigh:** %s' % s['deciding'], '',
                '**My advice:** %s%s' % (s['advice_note'], ' (I\'d leave this one; it\'s here so you can overrule me.)'
                                         if s['advice'] == 'leave' else ''), '']
        if s.get('found_by'):
            out += ['*Found by: %s.*' % s['found_by'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'bad-trips-r01',
        'title': 'Bad Trips Guide, Round 1',
        'intro': INTRO,
        'git_file': 'articles/bad-trips/review/r01/REVIEW-R01.html',
        'article': {'file': 'articles/bad-trips/original-page.md',
                    'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': BUILT,
        'links': {'guide': 'https://ibogaqueen.substack.com/p/shadow-work-and-tripsitting-yourself',
                  'guide_label': 'the guide as published',
                  'review': BLOB + 'articles/bad-trips/review/r01/REVIEW-R01.md'},
        'types': TYPES,
        'suggestions': CARDS,
    }
    probs = SR.check(review, BL)
    if probs:
        raise SystemExit('\n'.join(probs))
    (HERE / 'REVIEW-R01.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    page = SR.page(review, MD, BL)
    (HERE / 'REVIEW-R01.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-R01.artifact.html').write_text(SR.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-R01.md').write_text(cards_md(review), encoding='utf-8')
    print(len(CARDS), 'cards')


if __name__ == '__main__':
    main()
