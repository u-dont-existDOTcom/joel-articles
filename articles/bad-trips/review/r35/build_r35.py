"""Round 35 of the bad trips guide: after his round-34 answers (2026-11-11 23:57 UTC). His Risk of Harm version is in and its
reasons are said once; one place they overlap is his call, and his round-34 moves, carried in my words, read AI in a whole
section, so that section is the next teaching card.

Works on the guide as it stands (PAGE-R35.md, the review-page form of ../../GUIDE-SO-FAR.md after round 34, made by
../../tools/page_md.py, with PAGE-R35-map.json).

  python3 articles/bad-trips/review/r35/build_r35.py     (from the repo root)

writes REVIEW-R35.json, REVIEW-R35.html, REVIEW-R35.artifact.html and REVIEW-R35.md beside this file.
"""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
ART = HERE.parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as SR  # noqa: E402

MD_PATH = HERE / 'PAGE-R35.md'
MD = MD_PATH.read_text(encoding='utf-8')
BL = SR.blocks(MD)
MAP = json.loads((HERE / 'PAGE-R35-map.json').read_text(encoding='utf-8'))['map']


def P(bid, k=None):
    """The page index of B id BID's page block. A list B id has one page block per item, so for one of those, name the
    item (k) or use PALL. Round 23's card on Minimum Viable Integration spanned only its first item because this took the
    first by default (Joel, 2026-11-07 22:38 UTC: "i don't understand how you work, you want me to correct only that one
    line? ... why?")."""
    if k is None:
        if len(MAP[bid]) > 1:
            raise SystemExit('%s is a list of %d page blocks: name the item, P(%r, k), or take them all, PALL(%r)'
                             % (bid, len(MAP[bid]), bid, bid))
        k = 0
    return MAP[bid][k]


def PALL(bid):
    """Every page block of B id BID, in order (each item of a list)."""
    return list(MAP[bid])


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
    'plain': {'label': 'Said plainly', 'about': 'AI lines said plainly, each with its reason, the way he fixes his own windows'},
    'structure': {'label': 'Structure', 'about': 'how the quick version and the long version split the guide, and where '
                  'a part goes'},
    'repeat': {'label': 'Said twice', 'about': 'a point the guide already makes elsewhere: one copy goes, the other stays'},
    'safety': {'label': 'Safety in one place', 'about': 'a caution or call-for-help line said in several places, or one '
               'that changes nothing a reader does'},
    'question': {'label': 'Your call', 'about': 'something only you can decide or know'},
    'sense': {'label': 'Says what it means', 'about': 'a term explained where it is first used, or a word that says '
              'what to do'},
    'belief': {'label': 'Your belief back', 'about': 'a sentence of your post that said why, cut in an earlier '
                'round, put back where it bears on what the reader does'},
    'method': {'label': 'Your method where it is used', 'about': 'a line the guide already has, put where the reader uses '
               'it in trouble (your METHOD-WHERE answer, round 28)'},
    'notes': {'label': 'Your notes, placed', 'about': 'what you sent in a comment, put where it belongs in the guide, '
              'as you sent it'},
    'typo': {'label': 'Typo', 'about': 'a word in your own paragraph spelled differently from how you spell it '
             'elsewhere, with the fix in place'},
    'boilerplate': {'label': 'Boilerplate', 'about': 'standard advice a model added that carries none of your method '
                    'and no safety point a reader needs, shown as the section would read without it (your round-32 '
                    'note)'},
    'teach': {'label': 'Teach me', 'about': 'a paragraph that reads AI in every wording I tried, whose shape many stuck paragraphs '
              'share: how you would say it teaches me how to say them (you asked for these on 2026-11-07)'},
}

CARDS = []


def card(**kw):
    CARDS.append(kw)


BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/'
exec((HERE / 'cards_r35.py').read_text(encoding='utf-8'))




def marked(j, spans):
    t = T(j)
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


def cards_md(review):
    """The page's cards as text, for GitHub (he never gets sent to the JSON)."""
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide as it stands](%s), after every round answered so far. '
           'To answer, use the page; or write your answer under a card\'s name in a message to me.'
           % (review['built'], review['links']['guide']), '']
    out += [x for para in review.get('intro', []) for x in (para, '')]
    def placed(s):  # where the page shows the card: after card_after, else after its first span's block
        at = s.get('card_after')
        return at if at is not None else (s.get('spans') or [{'block': 0}])[0]['block']
    for s in sorted(review['suggestions'], key=lambda s: (s['type'] != 'structure', placed(s))):
        where = SR.where(BL, placed(s))
        out += ['## %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '', '*%s*' % where, '']
        if s['advice'] == 'edit':
            blocks_ = sorted({sp['block'] for sp in s['spans']})
            out += ['**The paragraph%s now:**' % ('s' if len(blocks_) > 1 else ''), '']
            out += ['> %s\n' % marked(i, []) for i in blocks_] + ['']
            if s.get('reading'):
                out += ['**What Pangram read:** %s' % s['reading'], '']
            if s.get('tested'):
                out += ['**My tries, with what Pangram read:**', '', s['tested'], '']
            if s.get('sense'):
                out += ['**What a fresh reader found:** %s' % s['sense'], '']
            out += ['**Why it comes to you:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
            continue
        if s['advice'] == 'ask':
            q = re.sub(r'(?<!\n)\n(?!\n)', '  \n', s['question'])   # a line break in it stays one on GitHub
            out += ['**Question:** %s' % q, '', '**Why:** %s' % s['why'], '']
            if s.get('stays'):
                out += ['**Until you answer:** %s' % s['stays'], '']
            out += ['**My pick:** %s' % s['advice_note'], '']
            continue
        if s.get('reading'):
            out += ['**What Pangram read:** %s' % s['reading'], '']
        if s.get('tested'):
            out += ['**Pangram on the suggestion:** %s' % s['tested'], '']
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
                out += ['**New heading** (%s, %s): %s' % (ins['kind'], ins.get('whose', 'the words are yours, from the heading it replaces'), ins['text']), '']
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
        'review_id': 'bad-trips-r35',
        'title': 'Bad Trips Guide, Round 35',
        'intro': INTRO,
        'git_file': 'articles/bad-trips/review/r35/REVIEW-R35.html',
        'article': {'file': 'articles/bad-trips/review/r35/PAGE-R35.md',
                    'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': BUILT,
        'links': {'guide': BLOB + 'articles/bad-trips/GUIDE-SO-FAR.md',
                  'guide_label': 'the guide as it stands',
                  'check': BLOB + 'articles/bad-trips/review/r35/REVIEW-R35.md',
                  'review': BLOB + 'articles/bad-trips/review/r35/REVIEW-R35.md'},
        'types': TYPES,
        'suggestions': CARDS,
    }
    probs = SR.check(review, BL)
    if probs:
        raise SystemExit('\n'.join(probs))
    (HERE / 'REVIEW-R35.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    page = SR.page(review, MD, BL)
    (HERE / 'REVIEW-R35.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-R35.artifact.html').write_text(SR.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-R35.md').write_text(cards_md(review), encoding='utf-8')
    print(len(CARDS), 'cards')


if __name__ == '__main__':
    main()
