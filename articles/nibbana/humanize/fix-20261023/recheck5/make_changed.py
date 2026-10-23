"""CHANGED.json for Nibbāna's fifth recheck (2026-10-23, after Joel's message of 18:13 UTC): batch n4's stretches
(../n4/EDITS-n4.json) with my chance that each reads red, and the one red sentence of recheck 4 that stays his
("That creates a practical problem."). part_forecast.py adds each one's neighbours itself (gate E249) and the light
green windows of recheck 4.

  python3 articles/nibbana/humanize/fix-20261023/recheck5/make_changed.py   (after make_recheck_nb.py)
"""
import json, pathlib, sys

R = pathlib.Path(__file__).resolve().parent
REPO = R.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

CHANCE = {
    'n4-unification': (0.25, "Emulate's sample bu, with its first word cut; the paragraph read AI, High, alone in recheck 4, "
                             "and Emulate's whole-stretch splices have read Human in place most times (the guide's part A4: "
                             "all four)"),
    'n4-soh': (0.10, 'his published sentence back: Human, Medium, alone in recheck 3; next to the changed definition'),
    'n4-abstract': (0.25, "Emulate's sample bv for his red sentence, the rest of his paragraph unchanged"),
    'n4-preserve-1': (0.20, "Emulate's sample br, with his pronoun and the article's spelling back"),
    'n4-preserve-2': (0.20, "Emulate's sample bt, with its typo fixed; his puzzle image kept"),
}
KEPT = [{'name': 'kept red: his "That creates a practical problem."', 'text': 'That creates a practical problem.',
         'chance_red': 0.30, 'why': 'read AI, Low, in recheck 4 in one window with the puzzle sentence before it, which is '
                                   'new; his sentence stays (the one sample with a replacement turned his cause into a '
                                   'second problem)'}]


def main():
    text = (R / 'DRAFT-TEXT.txt').read_text(encoding='utf-8')
    out = []
    for e in json.loads((R.parent / 'n4' / 'EDITS-n4.json').read_text(encoding='utf-8')):
        chance, why = CHANCE[e['key']]
        s = C.smart(e['new'])
        if e['key'] == 'n4-soh':
            s = C.smart('I owe Soh a great deal, but one key difference remains: ' + e['new'] + ', which makes no sense to me.')
        assert text.count(s) == 1, (e['key'], s[:60], text.count(s))
        out.append({'name': '%s (batch n4)' % e['key'], 'text': s, 'chance_red': chance, 'why': why})
    for k in KEPT:
        assert text.count(k['text']) == 1
        out.append(k)
    (R / 'CHANGED.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d parts in CHANGED.json' % len(out))


if __name__ == '__main__':
    main()
