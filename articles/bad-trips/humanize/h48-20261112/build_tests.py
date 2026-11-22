#!/usr/bin/env python3
"""build_tests.py - turn 38's carries (2026-11-12) of his round-37 Chest Pain fix: the action said before the list it
serves. His try 7 (../../experiments/t37-answers/JOEL-TRIES-TEACH-CHEST.md) changed my chest-c3 that one way, the lead-in
"For the following more serious signs (or if unsure), I'd also call medics:" with the two sentences after the list cut,
and it read Human Written where chest-c3 read AI Generated, 100%. My Brain Feels Damaged's checks (brain-c3, h46) and Acute
Medical's opening (acute-r1-fix2, h45) both said what to do only after their checks.

- brain-p1: brain-c3 with only that move, as his try 7 made it on chest-c3: the action and the can't-answer case in the
  lead-in, the two sentences after the list cut, the list and the last sentence as they were. Its first draft joined the
  stroke-signs sentence to the lead-in with "so"; the read against his fixes marked it packed, so they are two sentences.
- acute-c1: Acute Medical's opening (B100, B76) as one paragraph: what to do first, then why. Its six conditions are the
  Call medics list's own lines (trouble breathing, overheating, seizures, the brain checks, waking), so it points to the
  list instead of saying them again (his BODY-ONCE answer of round 35: "my paragraph should not say anything that should
  be going in that above list").

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
BRAIN_LIST = ("- First, are they awake and breathing normally?\n"
              "- Feel whether they're very hot.\n"
              "- Have them talk and smile. Is their speech slurred, or does one side of their face droop?\n"
              "- Ask them to hold both arms out in front of them, and see if one drifts down.\n"
              "- If it's safe, have them stand and walk a few steps to see if they keep their balance. Wetting or soiling "
              "themselves is another sign to watch for.\n"
              "- Watch for a seizure, and for vomiting that keeps coming back.\n"
              "- Ask about a really bad headache or chest pain.\n"
              "- Check if their vision has changed.")
TESTS = {
    'brain-p1': ("If Someone Says \"My Brain Feels Damaged\": DMSO + Humic Acid First\n\n"
                 "While the DMSO is working, check them over. Several of these checks look for recognized stroke warning "
                 "signs. If any check turns up a problem (or they're too out of it to answer you), keep the DMSO going "
                 "while someone calls medics:\n" + BRAIN_LIST + "\n\n"
                 "If everything checks out but the brain-damage feeling stays, keep going DMSO-first and check them again "
                 "soon."),
    'acute-c1': ("Acute Medical and Neurological Rescue\n\n"
                 "I'd calm and stabilize the trip right where they are, as long as none of the signs on the Call medics "
                 "list above show up and I can keep them from getting hurt. Even from a severe trip, they can come down "
                 "faster that way than after an ambulance ride and hours in an emergency room."),
}

if __name__ == '__main__':
    base = (HERE.parent / 'h46-20261112/TEST-brain-c3.txt').read_text(encoding='utf-8')
    assert BRAIN_LIST in base, 'brain-p1 must keep brain-c3\'s list as it was'
    for k, t in TESTS.items():
        p = HERE / ('TEST-%s.txt' % k)
        p.write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256((t + '\n').encode()).hexdigest()[:12])
