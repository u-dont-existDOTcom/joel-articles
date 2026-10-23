"""CHANGED.json for Nibbāna's seventh recheck (2026-10-23, after Joel's message of 22:29 UTC): batch n6's splices
(../n6/EDITS-n6.json), with my chance that each reads red, and the red of recheck 6 that stays his ("So enlightenment
isn’t a simple bliss switch." and the first two sentences of "I used to attribute ..."). part_forecast.py adds each one's
neighbours itself (gate E249) and the light green windows of recheck 6.

  python3 articles/nibbana/humanize/fix-20261023/recheck7/make_changed.py   (after make_recheck_nb.py)
"""
import json, pathlib, sys

R = pathlib.Path(__file__).resolve().parent
REPO = R.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

CHANCE = {
    'n6-aware': (0.25, "Emulate's sample ca, his duality words kept; his sentence read AI, Low, alone in recheck 6"),
    'n6-mn75': (0.20, "Emulate's sample ca with 'remember' out; the reader found the meaning kept"),
    'n6-question': (0.20, "Emulate's sample cb with a typo and the spelling fixed; the reader found the meaning kept"),
    'n6-lucid': (0.30, "Emulate's sample cc with three of my fixes from the reader's check, more of my words than usual"),
}
N4 = []
KEPT = [{'name': 'kept red: his "So enlightenment isn’t a simple bliss switch."',
         'text': 'So enlightenment isn’t a simple bliss switch.', 'chance_red': 0.20,
         'why': 'in window 82 (AI, Low) of recheck 6 with the old question; no sample has it, and its neighbours are new'},
        {'name': 'kept red: his "I used to attribute ..." and "The early Pāli texts do give us ..."',
         'text': 'I used to attribute “life is like a dream” directly to the historical Buddha', 'chance_red': 0.35,
         'why': 'window 96 (AI, Low) of recheck 6, his 12:30 rewrite, next to his N4 16 move; no sample kept its meaning'}]


def main():
    text = (R / 'DRAFT-TEXT.txt').read_text(encoding='utf-8')
    out = []
    for e in json.loads((R.parent / 'n6' / 'EDITS-n6.json').read_text(encoding='utf-8')):
        chance, why = CHANCE[e['key']]
        s = C.smart(e['new'])
        assert text.count(s) == 1, (e['key'], s[:60], text.count(s))
        out.append({'name': '%s (batch n6)' % e['key'], 'text': s, 'chance_red': chance, 'why': why})
    for name, s, chance, why in N4:
        assert text.count(s) == 1, (name, s[:60], text.count(s))
        out.append({'name': name, 'text': s, 'chance_red': chance, 'why': why})
    for k in KEPT:
        assert text.count(k['text']) == 1
        out.append(k)
    (R / 'CHANGED.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d parts in CHANGED.json' % len(out))


if __name__ == '__main__':
    main()
