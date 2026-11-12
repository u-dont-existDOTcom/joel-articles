#!/usr/bin/env python3
"""build_tests.py - turn 36's tests (2026-11-12): his round-35 version carried (lesson bad-trips-2026-11-12e, the sixth
fix in SKILL.md: a diagnostic list as questions the reader asks of the body, each state with the signs that show it,
every state kept, "and" for a comma pair, what a difference means said instead of "is different from").

- ss-r1: Suspected Serotonin Syndrome's recognition part (B131 to B134): the Hunter criteria as the questions they ask,
  each criterion exactly as the guide has it, the term in brackets after its plain words; the 38 and 100.4 and W037's keys
  kept. h42a read the whole section AI Generated, 100% (4a5da2d5).
- acute-r1: Acute Medical and Neurological Rescue's first two paragraphs (B100, B76): the conditions for calming the trip
  in the field said as the questions the reader asks; B100's "It does not always mean that an ambulance is the first or
  only useful action" said as what can help instead, the ambulance pictured. h42a: AI Generated, 100% (0df121e8).
- ss-r1 also puts the point first ("Any one of the following patterns makes serotonin toxicity more likely", W-key "following" kept; the name, the
  Hunter criteria, went after a fresh reader found it a source label the reader doesn't act on, NEEDED-READ.md) and says B134's "rather than a command to wait for every criterion" as an instruction ("Don't wait")
  instead of a coach phrase (lint E41 on "You don't have to see every one"); ocular clonus pictured ("darting back and
  forth in a fast rhythm by themselves") instead of "they can't stop" (lint X1); the hypertonia question unpacked (B4).

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
TESTS = {
    'ss-r1': ("Recognizing serotonin toxicity\n\n"
              "Any one of the following patterns makes serotonin toxicity more likely. "
              "Are their muscles contracting and relaxing in a rhythm on their own, with nothing setting it off (spontaneous "
              "clonus)? Or does that rhythm start when a muscle is stretched, like when you flex their ankle up quickly "
              "(inducible clonus), and come with agitation or sweating? Do you see their eyes darting back and forth in a fast "
              "rhythm by themselves (ocular clonus), again with agitation or sweating? Are they shaking, and are their "
              "reflexes abnormally brisk (tremor and hyperreflexia)? Or are their muscles rigid, with a temperature above "
              "38°C (100.4°F) and eye or inducible clonus too (hypertonia and fever)?\n\n"
              "Don't wait to see every one of these before you act, though. Dangerous heat, rigidity, clonus, confusion, "
              "or rapid worsening deserves medical help."),
    'acute-r1': ("Acute Medical and Neurological Rescue\n\n"
                 "An emergency means act now, and sometimes the fastest help is right where they are. Someone who's severely "
                 "altered but physically stable may come down sooner with your help than after an ambulance ride and hours "
                 "in an emergency room.\n\n"
                 "So check the body first. Are they breathing normally, and is their temperature safe? Are they free of "
                 "seizures, with nothing suggesting a brain injury? Are they awake enough to work with you, and can you keep "
                 "them physically safe? If all of that's true, calming and stabilizing the trip may be enough."),
}
# Second tries (h45b), after both read AI Generated, 100% (02fb701a, eedc2eec). His five tries on the oral paragraph
# (experiments/t35-answers/JOEL-TRIES-TEACH-ORAL.md) flipped to Human without the question frame (his tries 3 and 4) and
# stayed AI with it gone and the tidy pairs kept (try 1): what changed was a working construction for a tidy parallel one,
# "Slow and shallow" for "Slow, shallow", a list left loose ("like seizure, dangerous overheating, tremor"), one clinical
# term in brackets for the whole list, not one per sign. Mine had a bracketed term closing every question (ss-r1) and
# three "Are they X, and Y?" pairs (acute-r1).
TESTS2 = {
    'ss-r1-fix2': ("Recognizing serotonin toxicity\n\n"
                   "Any one of the following patterns makes serotonin toxicity more likely. Are their muscles jerking in a "
                   "rhythm by themselves, with nothing setting it off (that's called clonus)? Does the jerking start when you "
                   "stretch a muscle, like flexing their foot up quickly, and are they also agitated or sweating? Do you see "
                   "their eyes darting back and forth in a rhythm, again with agitation or sweating? Are they shaking, with "
                   "reflexes that are way too brisk? Or are their muscles rigid, with a temperature above 38°C (100.4°F) and "
                   "that eye or stretch-triggered clonus too?\n\n"
                   "Don't wait to see every one of these before you act, though. Dangerous heat, rigidity, clonus, confusion, "
                   "or rapid worsening deserves medical help."),
    'acute-r1-fix2': ("Acute Medical and Neurological Rescue\n\n"
                      "An emergency means act now, and sometimes the fastest help is right where they are. If they're "
                      "severely altered but physically stable, you may bring them down faster yourself than an ambulance ride "
                      "and hours in an emergency room would.\n\n"
                      "So check the body first. Are they breathing normally, and is their temperature safe? No seizures, and "
                      "nothing that looks like a brain injury? Are they awake enough to work with you, and can you keep them "
                      "from getting hurt? If all that checks out, calming and stabilizing the trip may be enough."),
}

if __name__ == '__main__':
    for k, t in list(TESTS.items()) + list(TESTS2.items()):
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
