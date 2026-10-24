"""CHANGED.json for Nibbāna's eighth recheck (2026-10-23, after Joel's message of 23:28 UTC): batch n7's splice
(../n7/EDITS-n7.json), with my chance that it reads red. part_forecast.py adds its neighbours itself (gate E249) and the
light green windows of recheck 7.

  python3 articles/nibbana/humanize/fix-20261023/recheck8/make_changed.py   (after make_recheck_nb.py)
"""
import json, pathlib, sys

R = pathlib.Path(__file__).resolve().parent
REPO = R.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

CHANCE = {
    'n7-drawers': (0.30, "Emulate's sample cf with four fixes of mine, two from the reader's check (its first sentence is "
                         "back to his flat opening, \"Part of the problem is that the Buddha\", which read AI, Low, in "
                         "recheck 7 and on 2026-10-20)"),
}


def main():
    text = (R / 'DRAFT-TEXT.txt').read_text(encoding='utf-8')
    out = []
    for e in json.loads((R.parent / 'n7' / 'EDITS-n7.json').read_text(encoding='utf-8')):
        chance, why = CHANCE[e['key']]
        s = C.smart(e['new'])
        assert text.count(s) == 1, (e['key'], s[:60], text.count(s))
        out.append({'name': '%s (batch n7)' % e['key'], 'text': s, 'chance_red': chance, 'why': why})
    (R / 'CHANGED.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d parts in CHANGED.json' % len(out))


if __name__ == '__main__':
    main()
