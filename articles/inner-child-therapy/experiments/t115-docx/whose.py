#!/usr/bin/env python3
"""Turn 115: whose words each round-8 window below High covers, for the docx comments (WHOSE.json: window id -> the
comment's last sentence). Read off the turn notes above each paragraph (experiments/t115-pass/CANDIDATES.md), the owner-edits
file and his published guide (source/inner-child-guide-substack-20261003.txt). A window not listed here is in my words and
the docx says why it was left. Where I see a tell in his words, the note names it and nothing more: a reworded suggestion of
his words would be new prose for him to approve, which goes through the owner-delivery gate first.

  whose.py      writes WHOSE.json beside this file"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
EXP = HERE.parent
C = json.loads((EXP / 't115-pass' / 'CANDIDATES.json').read_text(encoding='utf-8'))

YOURS = 'Your words: left for you.'
GUIDE = 'Your published guide\'s line: left for you.'
APPROVED = 'Your approved version of this section (GPT\'s dedup, word for word, turn 53): left for you.'
HIS_PIDS = {  # pid: note for every window in it (his own words, per the notes above the paragraph)
    'p01': YOURS, 'p25': YOURS, 'p31': YOURS, 'p33': YOURS, 'p35': YOURS, 'p39': YOURS, 'p45': YOURS, 'p48': YOURS,
    'p50': YOURS, 'p51': YOURS, 'p53': YOURS, 'p56': YOURS + ' (Hearthwork\'s premise, in your words.)', 'p57': YOURS,
    'p06': GUIDE, 'p41': APPROVED, 'p43': APPROVED, 'p34': 'Partly your words (the Nurturer voice is yours): left for you.',
    'p26': YOURS + ' The tell I see, if any: a topic sentence that announces the paragraph.',
    'p37': YOURS + ' The tell I see: a question answered right away ("And if none of them shows up yet? No problem, ..."), '
                   'the shape round 8 read AI in the paragraph before it; said as one plain sentence in your words, it may read High.',
}
BY_WINDOW = {
    'r8w029': 'Partly your words (your quoted "Tell me what feels unsafe."); the rest is mine, nearly High: I left it.',
    'r8w087': GUIDE,
    'r8w066': 'Mine, in a paragraph you approved as it is (your yes to C2): see the suggestion on these words.',
    'r8w067': 'Mine, in a paragraph you approved as it is; it holds the danger line, which stays.',
    'r8w059': APPROVED + ' The tell I see: "You don\'t have to ..." permission, then "The question is whether ...".',
    'r8w056': APPROVED + ' A short general line between two sets of examples; it may be fine.',
}


def main():
    out = {}
    for r in C:
        for w in r['windows']:
            if w['id'] in BY_WINDOW:
                out[w['id']] = BY_WINDOW[w['id']]
            elif r['pid'] in HIS_PIDS:
                out[w['id']] = HIS_PIDS[r['pid']]
    (HERE / 'WHOSE.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(out), 'windows with a note of whose words')


if __name__ == '__main__':
    main()
