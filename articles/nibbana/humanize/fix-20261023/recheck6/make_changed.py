"""CHANGED.json for Nibbāna's sixth recheck (2026-10-23, after Joel's message of 20:35 UTC): the stretches his N4 answers
changed in the text Pangram reads (the moves, the split bullet, the nested item and the one cut; his headings aren't read)
and batch n5's splices (../n5/EDITS-n5.json), with my chance that each reads red, and the two red sentences of recheck 5
that stay his (the room's "Nothing observed them from behind. There was no cosmic knower celebrating its achievement.").
part_forecast.py adds each one's neighbours itself (gate E249) and the light green windows of recheck 5.

  python3 articles/nibbana/humanize/fix-20261023/recheck6/make_changed.py   (after make_recheck_nb.py)
"""
import json, pathlib, sys

R = pathlib.Path(__file__).resolve().parent
REPO = R.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

CHANCE = {
    'n5-practical': (0.30, "Emulate's sample bz, one word changed from his (\"leads to\" for \"creates\"); his sentence read AI, "
                           "Low, alone in recheck 5 and with the sentence before it in recheck 4"),
    'n5-dn3': (0.30, "Emulate's sample bz with four typo and spelling fixes, for his sentence that read AI, Medium, alone in "
                     "recheck 5 (Human before); Emulate's whole-stretch splices have read Human in place most times"),
    'n5-skip': (0.25, "Emulate's sample bx, for his question that read AI, Low, alone in recheck 5"),
    'n5-room': (0.30, "Emulate's sample bz for the first sentence of the red; the two sentences after it stay his, so the "
                      "window may still hold them"),
}
# his N4 answers that change the text Pangram reads: (name, the text as the draft shows it, chance, why)
N4 = [
    ('his N4 7: the Parinibbāna bullet, ended after its first Iti 44 sentence',
     'Iti 44 agrees on the difference between nibbāna & parinibbāna.', 0.05,
     'his words, in a Human, High, window of 876 words in recheck 5; the bullet now ends here'),
    ('his N4 7: the rest of the bullet, now a paragraph under the list',
     'Iti 44 also shows the limit of nibbāna while you’re alive:', 0.05, 'the same words, out of the list'),
    ('his N4 9: the SN 22.22 sentence without "(even an arahant feels the first dart)"',
     'are the burden of suffering, and craving is the process', 0.05, 'Human, High, in recheck 5 with the parenthetical'),
    ('his N4 14: the monk paragraph, after Frank\'s second paragraph and its video',
     'But the problem isn’t as surprising with a YouTube star', 0.05, 'Human, High, in a 436-word window in recheck 5'),
    ('his N4 15: the MN 89 question, its own line',
     'Are you more joyful and enjoyable to be around without becoming a people-pleaser, as in MN 89?', 0.05,
     'Human, High, in recheck 5 as one bullet with its note'),
    ('his N4 15: the note under the MN 89 question',
     'The standard isn’t the non-stop, 24/7 bliss that Soh claimed, which is false.', 0.05, 'the same words, nested'),
    ('his N4 16: "For me, nibbāna was really like waking up from a dream ..." moved up',
     'For me, nibbāna was really like waking up from a dream, except that nobody woke up.', 0.05,
     'Human, High, in a 350-word window in recheck 5'),
    ('his N4 17: the caution moved to the end of "Try a Tiny Bit of Nibbāna"',
     'The farther unification loosens, the less useful you become for normal tasks.', 0.05,
     'Human, High, in an 88-word window in recheck 5'),
]
KEPT = [{'name': 'kept red: his "Nothing observed them from behind. There was no cosmic knower celebrating its achievement."',
         'text': 'Nothing observed them from behind. There was no cosmic knower celebrating its achievement.',
         'chance_red': 0.30, 'why': 'in window 15 (AI, Low) of recheck 5; no sample keeps the knower\'s "achievement", so his '
                                    'words stay beside the new first sentence'}]


def main():
    text = (R / 'DRAFT-TEXT.txt').read_text(encoding='utf-8')
    out = []
    for e in json.loads((R.parent / 'n5' / 'EDITS-n5.json').read_text(encoding='utf-8')):
        chance, why = CHANCE[e['key']]
        s = C.smart(e['new'])
        assert text.count(s) == 1, (e['key'], s[:60], text.count(s))
        out.append({'name': '%s (batch n5)' % e['key'], 'text': s, 'chance_red': chance, 'why': why})
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
