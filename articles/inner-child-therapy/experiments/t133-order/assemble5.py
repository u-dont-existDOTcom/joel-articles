#!/usr/bin/env python3
"""Turn 138, run 5 (PLAN.md, "Run 5"; written before its cards existed): the blind card sort with only the guide's own
words and his framework answers (questions 114 to 116) as its frame, scored, with each card's second home.

  python3 assemble5.py       # out/OUTLINE5-*.json and RESULTS-5.md
  python3 assemble5.py 5b    # run 5b, with his line on where divine love leads: out/OUTLINE5B-*.json and RESULTS-5B.md"""
import collections
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import assemble as A  # noqa: E402
import assemble2 as A2  # noqa: E402


def load(prefix):
    cards = {}
    for L in 'ABCD':
        for c in json.load(open(HERE / 'out' / ('%s-%s.json' % (prefix, L))))['cards']:
            cards[c['id']] = c
    return cards


def name(i):
    return A.CURRENT.get(i, A.HEADING.get(i, i))


def row(label, outline, moved=None):
    s = A.score_order.score(outline)
    return s, '| %s | %d | %d | %d | %d | %.3f | %d | %s |' % (
        label, s['reparented_same'], s['reparented_extra'], s['levels_same'], s['levels_extra'], s['tau_vs_his'],
        s['same_place'], '' if moved is None else len(moved))


RUN = (sys.argv[1] if len(sys.argv) > 1 else '5').upper()
TAG = {'5': '5', '5B': '5B'}[RUN]
SPIRITUAL = ['N035', 'N038', 'N040', 'N043', 'N044']
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-child-therapy/experiments/t133-order/'


def guide_side(cards):
    """Each spiritual section's chain of first homes (any confidence; the 4 November parent where a card says none):
    is the Guide (N045) above it?"""
    base = A.base_parents()
    par = {i: (cards.get(i, {}).get('sits_under') if cards.get(i, {}).get('sits_under') in A.LEVEL else base[i])
           for i in A.IDS}
    out = {}
    for u in SPIRITUAL:
        seen, i, chain = set(), u, []
        while par.get(i) and par[i] not in seen:
            seen.add(i)
            i = par[i]
            chain.append(i)
        out[u] = 'N045' in chain
    return out


def main():
    cards = load('CARDS' + TAG)
    missing = [i for i in A.IDS if i not in cards]
    runs = [('guide\'s words and his answers, sits under (high)', 'high', A2.sits_under(cards)),
            ('guide\'s words and his answers, sits under (high or medium)', 'medium', A2.sits_under(cards, ('high', 'medium')))]
    base = A.score_order.score(A.score_order.BASE)
    if TAG == '5':
        title = '# Turn 138, run 5: the blind card sort with only the guide\'s own words and his answers'
        how = ('Made by [assemble5.py](%sassemble5.py) (method and predictions: [the plan](%sPLAN.md), "Run 5", written '
               'before the run). The frame, made by [make_frame5.py](%smake_frame5.py), is the 4 November text\'s own '
               'words for each part and role, and his answers to questions 114, 115 and 116; no model described any '
               'part.' % (GH, GH, GH))
    else:
        title = '# Turn 138, run 5b: run 5 with his line on where divine love leads'
        how = ('Made by [assemble5.py](%sassemble5.py) with "5b" (method and predictions: [the plan](%sPLAN.md), '
               '"Run 5b", written before the run). The frame, made by [make_frame5.py](%smake_frame5.py) with "--b", is '
               'run 5\'s with one line added, from his guide: under Divine Love: Bigger Door, "This is what the Inner '
               'Guide can bring you to".' % (GH, GH, GH))
    L = [title, '', how, '',
         '| Outline | His moves (of 20) | Other moves | His level changes (of 15) | Other level changes | Tau | In his place (of 148) | Sections moved |',
         '|---|---|---|---|---|---|---|---|',
         '| 4 November order, unchanged | 0 | 0 | 0 | 0 | %.3f | %d | 0 |' % (base['tau_vs_his'], base['same_place']),
         '| Turn 132 best on his moves: GPT with the rules, run 1 | 9 | 16 | 5 | 15 | 0.814 | 67 | |']
    for lv in ('high', 'medium'):
        o = json.load(open(HERE / 'out' / ('OUTLINE4-%s.json' % lv)))
        L.append(row('Run 4: frame written by a model, with his answer to 114 (%s)' % ('high' if lv == 'high' else 'high or medium'), o)[1])
    if TAG == '5B':
        for lv in ('high', 'medium'):
            o = json.load(open(HERE / 'out' / ('OUTLINE5-%s.json' % lv)))
            L.append(row('Run 5: the guide\'s words and his answers (%s)' % ('high' if lv == 'high' else 'high or medium'), o)[1])
    detail = {}
    for label, nm, (outline, moved) in runs:
        (HERE / 'out' / ('OUTLINE%s-%s.json' % (TAG, nm))).write_text(json.dumps(outline, indent=1) + '\n')
        s, r = row('Run %s: ' % TAG.lower() + label, outline, moved)
        detail[nm] = (s, moved)
        L.append(r)
    B, H = A.score_order.parse(A.score_order.BASE), A.score_order.parse(A.score_order.HIS)
    his = A2.his_moves()
    L += ['', 'Cards missing: %s.' % (', '.join(missing) or 'none'), '',
          '## His 20 moves: where the blind sort filed each', '',
          'Headings are his current ones (his picks of 20 November); "he put it under" is the heading he really put it '
          'under, headings he added included. "Counts as his" is the scorer\'s parent, which for a section under a '
          'heading he added is the nearest older heading; the sort can only name older headings.', '']
    first = second = 0
    for u in his:
        c = cards.get(u, {})
        t, t2 = c.get('sits_under'), c.get('second_home')
        mark = 'his' if t == H['par'][u] else ('where it was' if t == B['par'][u] else 'elsewhere')
        first += t == H['par'][u]
        second += t2 == H['par'][u] and t != H['par'][u]
        L.append('- "%s": %s; the sort, under "%s" (%s, %s); second home "%s"%s' % (
            name(u), A.his_place(u), name(t), c.get('sits_under_confidence'), mark, name(t2),
            ' (counts as his)' if t2 == H['par'][u] and t != H['par'][u] else ''))
    side = guide_side(cards)
    L += ['', '## The five spiritual sections he put on the Guide\'s side', '',
          'On the Guide\'s side (the Guide above it in the chain of first homes, at any confidence): %d of 5.' % sum(side.values()), '']
    for u in SPIRITUAL:
        c = cards.get(u, {})
        L.append('- "%s": under "%s" (%s), role %s; %s' % (name(u), name(c.get('sits_under')), c.get('sits_under_confidence'),
                 'none' if c.get('role') in (None, 'none') else '"%s"' % name(c['role']),
                 'on the Guide\'s side' if side[u] else 'not on the Guide\'s side'))
    unsure = [i for i in A.IDS if i in B['par'] and cards.get(i, {}).get('sits_under_confidence') != 'high']
    asked = [i for i in unsure if cards[i].get('second_home') not in (None, 'none', '')]
    pairs = collections.Counter()
    members = collections.defaultdict(list)
    for i in asked:
        k = tuple(sorted((cards[i]['sits_under'], cards[i]['second_home'])))
        pairs[k] += 1
        members[k].append(i)
    hits = [u for u in his if u in asked and H['par'][u] in (cards[u]['sits_under'], cards[u]['second_home'])]
    n_units = len([i for i in A.IDS if i in B['par']])
    L += ['', '## Second homes: do they show where to ask?', '',
          'His real heading (as the scorer counts it) was the sort\'s first home for %d of his 20 moves, and its second '
          'home for %d more. %d sections were unsure (medium or low) with a second home: asking him "first or second?" '
          'about each would be %d questions, and %d of them would have found his move (chance, for that many sections: '
          '%.1f of his 20 among them).' % (first, second, len(asked), len(asked), len(hits),
                                           len(asked) * len(his) / n_units), '',
          'The pairs of homes that unsure sections split between most often (one question each would cover them):', '']
    for k, n in pairs.most_common(8):
        if n < 2:
            break
        inside = [u for u in members[k] if u in his]
        L.append('- "%s" or "%s": %d sections%s' % (name(k[0]), name(k[1]), n,
                 ('; his moves among them: ' + ', '.join('"%s"' % name(u) for u in inside)) if inside else ''))
    s, moved = detail['high']
    L += ['', '## The high-confidence moves', '']
    for i in sorted(moved, key=A.POS.get):
        t = cards[i]['sits_under']
        L.append('- "%s" -> under "%s" (%s)' % (name(i), name(t), 'his move' if i in s['got'] else 'not his'))
    (HERE / ('RESULTS-%s.md' % TAG)).write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
