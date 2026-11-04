#!/usr/bin/env python3
"""Turn 117: OWNER-EDITS.json after the article became Joel's own reorganized guide.

  python3 articles/inner-child-therapy/experiments/t117-apply/owner_edits_t117.py     (after apply_t117.py)

The article is now his guide of 2026-11-03 21:00 UTC with his answers of 23:32 UTC put in (apply_t117.py; every word
that differs from his file is listed in DECISIONS.md, each from a card or an answer). So an earlier record whose words
are no longer in the article was replaced by his own newer text: each one that fails now is marked superseded by the new
entry, joel-116-117-guide, which records this turn's changes with checks of its own. A record that fails only because of
the standard swap (E337 (gut): straight quote marks, a spaced en dash for each em dash) gets its strings swapped instead,
with a note. Records that still pass stay as they are. Run it once; a second run finds nothing more to do."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
import check_owner_edits  # noqa: E402
import typography_swap  # noqa: E402

sys.path.insert(0, str(HERE))
import apply_t117 as ap  # noqa: E402  (its texts; importing it applies nothing)

LEDGER = ART / 'OWNER-EDITS.json'
ARTICLE = ART / 'HUMANIZED-ARTICLE-SO-FAR.md'
NEW = 'joel-116-117-guide'
ENTRY = {
    'id': NEW,
    'status': 'applied',
    'what': ('His own reorganized guide (his ODT of 2026-11-03 21:00 UTC, experiments/t116-joel/JOEL-GUIDE-20261103.md) is the '
             'article now, with his answers on the turn-116 marking page put in by experiments/t117-apply/apply_t117.py: the '
             'cards he approved, his words for P13, Xandria as X (A1), "what year" (A5), the h5 (F6), English quote marks and no '
             'space before ! ? : (Q1), the links back (L1), and the live post\'s eleven pictures and videos with his own as notes '
             '(L2, L3). Each card\'s fate is checked in experiments/t117-apply/DECISIONS.md.'),
    'joel': ('2026-11-03 21:00 UTC (the ODT) and 23:32 UTC (experiments/t117-answers/ANSWERS-20261103-2332.json)'),
    'where': 'the whole guide',
    'must_contain_exact': [ap.P13, ap.DOG, typography_swap.swap_text(ap.CARDS['F4']['inserts'][0]['text'])[0]],
    'must_contain': ['My ex, X, taught me', 'another ex of mine (X)', 'like what year Pharaoh Tutankhamun',
                     'so “meet the protector first” would fit right in over there', 'I call it pl/ork (play + work)!',
                     'As Lao Tsu might have said (if I could ever have read that whole boring Art of War book)'],
    'must_have_line': ["##### Mo' Money, Mo' Problems", '## What to Make of a Passing Feeling', '## Finding People and Building Trust',
                       '## The Love Has to Move'],
    'must_not_contain': ['Xandria', 'therapeutic holding', '«', '»'],
}


def swapped(e):
    """The entry with every string it checks put through the standard swap."""
    S = lambda x: typography_swap.swap_text(x)[0]
    t = json.loads(json.dumps(e))
    for k in ('must_contain', 'must_contain_exact', 'must_have_line', 'must_not_have_line', 'must_not_contain', 'order'):
        if k in t:
            t[k] = [S(x) for x in t[k]]
    for l in t.get('must_link', []):
        l['text'] = S(l['text'])
    if 'span' in t:
        for k in ('from', 'to'):
            t['span'][k] = S(t['span'][k])
        for k in ('must_contain', 'must_not_contain'):
            if k in t['span']:
                t['span'][k] = [S(x) for x in t['span'][k]]
    return t


def main():
    led = json.loads(LEDGER.read_text(encoding='utf-8'))
    if any(e['id'] == NEW for e in led['entries']):
        print('already done:', NEW)
        return 0
    led['entries'].append(ENTRY)
    LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    res = check_owner_edits.run(ARTICLE, LEDGER)
    failed = {f['id'] for f in res['failed']}
    assert NEW not in failed, [f for f in res['failed'] if f['id'] == NEW]
    md = ARTICLE.read_text(encoding='utf-8')
    text, exact = check_owner_edits.visible(md), check_owner_edits.visible(md, quotes=False)
    raw = re.sub(r'<!--.*?-->', ' ', md, flags=re.S).translate(check_owner_edits.QUOTES)
    n, sw = 0, 0
    for e in led['entries']:
        if e['id'] not in failed or e.get('status') not in ('applied', 'claim'):
            continue
        t = swapped(e)
        if not check_owner_edits.check_entry(t, text, raw, exact):
            e.clear()
            e.update(t)
            e['what'] = (e.get('what') or '').rstrip() + (' Its strings swapped 2026-11-03 (turn 117) to the standard marks the '
                                                         'article now has (E337 (gut)).')
            sw += 1
            continue
        e['status'] = 'superseded'
        e['superseded_by'] = NEW
        e['what'] = (e.get('what') or '').rstrip() + (' Superseded 2026-11-03 (turn 117) by his own reorganized guide, which the '
                                                     'article now is (entry %s).' % NEW)
        n += 1
    LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    res = check_owner_edits.run(ARTICLE, LEDGER)
    print('swapped %d, superseded %d; now %d pass, %d failed, %d waiting' % (sw, n, res['passed'], len(res['failed']), len(res['waiting'])))
    return 1 if res['failed'] else 0


if __name__ == '__main__':
    sys.exit(main())
