#!/usr/bin/env python3
"""build_tests.py - the test texts of 2026-11-07's fourth pass: Joel's round-23 export of 22:38 UTC
(../../review/r23/ANSWERS-R23-20261107-2238.json; his words in ../../experiments/t25-answers/).

  DT   his No Rash Actions list, as he sent it (Pangram history e1537940, Human High alone), in the guide's place
  QF   Minimum Viable Integration cut as a repeat ("i also feel like this has been said at least twice already"), its one
       unique part (the facts to write down) merged into the questions paragraph, which gets his list moves
  AF3, SH3, AB3   his list moves carried to the other long don't lists, after a fresh reader's sense read:
       "maybe don't" for a flat don't (not where safety needs it firm), the list broken into sentences with their own
       verbs ("Think twice before ..."), concrete items ("giving away your BMW, buying a new BMW"), and an ending that
       gives the reader slack ("you can still change your mind the next day")

Each test is the Human base (Psychological First Aid to the reminder), then the section's heading and its part.

  python3 build_tests.py [NAME...]      writes TEST-base-NAME.txt
"""
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
spec = importlib.util.spec_from_file_location('h28', HERE.parent / 'h28-20261107/build_tests.py')
H28 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H28)
plain, BASE = H28.plain, H28.BASE
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text())
BY_ID = {b['id']: b for b in BLOCKS}

HIS_DT = ("Until you have slept and eaten, maybe don't drive, travel, break up, make up, quit your job, confess everything, "
          "confront or accuse that list of people you've been meaning to... Think twice before sending whatever ridiculous "
          "message you're planning on to Judge Amos, posting that revelation you'll forget tomorrow, giving away your BMW, buying "
          "a new BMW. After you decide that you are permanently enlightened or permanently damaged, and you explained the whole "
          "universe to your parents in 42 seconds, you can still change your mind the next day.")
NEW = {
    'B429': ("Then, once you're steadier, write down what happened while you still remember it: what you took and how much, if "
             "you know, where you were, what happened, what set it off, what helped and what made it worse. Some of it was "
             "probably medical or about the setting, some of it emotional, maybe some old trauma, maybe some fantasy. Notice "
             "which bits were useful, what's already changed in how you act, and what needs therapy, an apology, rest, or just "
             "some practical fixing."),
    'B428': ("While you're still wobbly, maybe hold off on more psychedelics, the joint, the ketamine and the heavy breathwork. "
             "The same goes for fasting, trying to force a kundalini awakening, staying up all night, or meditating or stretching "
             "for hours on end, and that ceremony you just found online that promises to fix it all can wait too. Keep to your "
             "routine and the ordinary world for a while, and deep practice will still be there once you've got your feet under "
             "you again."),
    'B415': ("During a trip, a shadow thought might show up looking like the truth about you. Maybe don't wrestle it down, "
             "announce it to everyone in the room, or decide it's your new permanent diagnosis. Just notice it: **\"A thought is "
             "here. A feeling is here. It is intense, but it is not the whole of me.\"** Then come back to the room, your body, "
             "whoever's with you, what time it is, and love."),
    'B408': ("If you see or remember abuse, betrayal, murder, past lives, hidden crimes or cosmic plots, write it down and get "
             "yourself somewhere safe. Don't fire off that 4 a.m. text to the person in the memory, or confront anyone else, while "
             "you're still high or shaky. After you've slept, take what you wrote to a therapist who knows trauma, an integration "
             "specialist (someone who helps people make sense of a trip afterward), or a grounded person you trust."),
}
TESTS = {
    'DT': (['B315', 'B317', 'B318'], {'B318': HIS_DT}),
    'QF': (['B419', 'B429', 'B430'], {'B429': NEW['B429']}),
    'AF3': (['B419', 'B427', 'B428'], {'B428': NEW['B428']}),
    'SH3': (['B410', 'B415'], {'B415': NEW['B415']}),
    'AB3': (['B405', 'B407', 'B408'], {'B408': NEW['B408']}),
}


def text(name):
    order, repl = TESTS[name]
    return BASE + '\n\n' + '\n\n'.join(plain(repl.get(k, BY_ID[k]['md'])) for k in order)


if __name__ == '__main__':
    for name in (sys.argv[1:] or TESTS):
        (HERE / ('TEST-base-%s.txt' % name)).write_text(text(name) + '\n')
        print(name, len(text(name).split()), 'words')
