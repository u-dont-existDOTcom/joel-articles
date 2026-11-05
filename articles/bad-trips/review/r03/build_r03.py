"""Round 3 of the bad-trips guide: the guide's warnings checked against the research (gate E344, at Joel's request of
2026-11-03 22:05 UTC), as a marking page. Each card is a line the check would change: a warning with nothing behind it
(a cut, unless it's his experience), a line that says more than its studies, a new study bearing on one of his remedies,
and one place where the guide parts from standard advice. The check itself, with every line's verdict and sources, is
../../experiments/t05-warnings/WARNINGS-CHECK.md.

Every card works on the guide as it stands (PAGE-R03.md, the review-page form of ../../GUIDE-SO-FAR.md, made by
../../tools/page_md.py from GUIDE-SO-FAR-blocks.json, with PAGE-R03-map.json mapping its block ids to the page's blocks).
Nothing here adds words of mine to his text except where a card says so.

  python3 articles/bad-trips/review/r03/build_r03.py     (from the repo root)

writes REVIEW-R03.json, REVIEW-R03.html (the page), REVIEW-R03.artifact.html (what is published) and REVIEW-R03.md
(the cards as text, for GitHub) beside this file.
"""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
ART = HERE.parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402

MD_PATH = HERE / 'PAGE-R03.md'
MD = MD_PATH.read_text(encoding='utf-8')
BL = SR.blocks(MD)
MAP = json.loads((HERE / 'PAGE-R03-map.json').read_text(encoding='utf-8'))['map']


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


exec((HERE / 'cards_r03.py').read_text(encoding='utf-8'))


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
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide as it stands](%s), after round 2. '
           'The check behind them, every line with its verdict and sources: [the warnings check](%s). To answer, use the '
           'page; or write your answer under a card\'s name in a message to me.'
           % (review['built'], review['links']['guide'], review['links']['check']), '']
    def placed(s):  # where the page shows the card: after card_after, else after its first span's block
        at = s.get('card_after')
        return at if at is not None else (s.get('spans') or [{'block': 0}])[0]['block']
    for s in sorted(review['suggestions'], key=lambda s: (s['type'] != 'structure', placed(s))):
        where = SR.where(BL, placed(s))
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
            to = T(mv['before']).strip()
            out += [('**Moves** to the end of the section, just before its divider:' if to == '---' else
                     '**Moves** to just before "%s":' % SR.first_words(to)), '']
            out += ['> %s' % T(i) for i in mv['blocks']] + ['']
        for ins in s.get('inserts', []):
            if ins['kind'] == 'p':
                out += ['**New line**%s: %s' % (', linked to its section' if ins.get('href') else '',
                                                 '[%s](%s)' % (ins['text'], ins['href']) if ins.get('href') else ins['text']), '']
            else:
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
        'review_id': 'bad-trips-r03',
        'title': 'Bad Trips Guide, Round 3',
        'intro': INTRO,
        'git_file': 'articles/bad-trips/review/r03/REVIEW-R03.html',
        'article': {'file': 'articles/bad-trips/review/r03/PAGE-R03.md',
                    'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': BUILT,
        'links': {'guide': BLOB + 'articles/bad-trips/GUIDE-SO-FAR.md',
                  'guide_label': 'the guide as it stands',
                  'check': BLOB + 'articles/bad-trips/experiments/t05-warnings/WARNINGS-CHECK.md',
                  'review': BLOB + 'articles/bad-trips/review/r03/REVIEW-R03.md'},
        'types': TYPES,
        'suggestions': CARDS,
    }
    probs = SR.check(review, BL)
    if probs:
        raise SystemExit('\n'.join(probs))
    (HERE / 'REVIEW-R03.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    page = SR.page(review, MD, BL)
    (HERE / 'REVIEW-R03.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-R03.artifact.html').write_text(SR.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-R03.md').write_text(cards_md(review), encoding='utf-8')
    print(len(CARDS), 'cards')


if __name__ == '__main__':
    main()
