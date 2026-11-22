#!/usr/bin/env python3
"""build_tests.py - turn 41's tests (2026-11-12, after his round-39 answer and message of 22:34 UTC):

- his message: "you're right about over 5 minutes that's an epilepsy rule. altho we should also keep in mind that if
  someone does have epilepsy, they are more likely to have seizures on psychedelics so explain that they can lower seizure
  threshold even with a normal dose and people with already low seizure thresholds might have seizures which are most
  likely less dangerous than an actual drug overdose seizure", and "as for dangerously hot, you can tell by touching
  someone's forehead how hot it is. i'm very often sweating a lot on psychedelics but my forehead is not hot."
- So Active Seizure's call list (his) says an overdose seizure as its own line and keeps "over 5 minutes" for any other
  seizure, its heat line says how to tell (the forehead), and a paragraph after the list says why, in his words.

Each goes in only when a check of it by itself reads Human High in every window (apply_gate.py, gate
bad-trips-2026-11-12l).

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
HEAD = "Active Seizure"
FIRST = ("Time the seizure, and while it lasts:\n"
         "- Move any dangerous objects away from them, especially anything hard or sharp.\n"
         "- Don't restrain them, since that can cause injuries, but do put pillows where appropriate, especially under the head.\n"
         "- Loosen any tight clothing.\n"
         "- Turn them gently onto their side, which helps them breathe.\n"
         "- Keep everything out of their mouth while they're convulsing or not fully conscious.")
CALL1 = ("Call medics if any of these happen:\n"
         "- They have a seizure after taking too much.\n"
         "- Any other seizure goes on for over 5 minutes.\n"
         "- Their breathing gets slow and shallow.\n"
         "- Their lips turn blue or gray.\n"
         "- Their forehead feels very hot to the touch, not just sweaty.\n"
         "- They injure their head, break a bone, or bleeding won't stop.")
EXPL1 = ("Even a normal dose of a psychedelic can lower the seizure threshold, making seizures easier to set off, so a person "
         "whose threshold is already low, like someone with epilepsy, might have a seizure. That's most likely less "
         "dangerous than a seizure from an actual overdose.")
RESCUE = ("If they have a rescue medicine for epilepsy seizures with them, give it as the label instructs. These medicines are "
          "benzodiazepines in nasal spray or rectal gel, or sometimes an intramuscular shot (pills can't be swallowed). After "
          "giving it, keep a close eye on their breathing, since a benzodiazepine adds to the risk of it getting slow and "
          "shallow, especially if they've also taken other respiratory depressants like opioids or alcohol.")
TESTS = {
    'callp-c1': CALL1,
    'explp-c1': CALL1 + "\n\n" + EXPL1,
    'seize-c6': "\n\n".join([HEAD, FIRST, CALL1, EXPL1, RESCUE]),
}

# c2, after the reads of seize-c6 (reads/): the overdose line says what to do when you can't tell ("or you don't know how
# much they took", his "(or if unsure)" from Chest Pain), the heat line in his bracket shape with how to tell, and the
# paragraph said from the reader's question (is this an overdose?), naming who and which seizure, so it bears on the call.
CALL2 = ("Call medics if any of these happen:\n"
         "- They have a seizure after taking too much, or you don't know how much they took.\n"
         "- Any other seizure goes on for over 5 minutes.\n"
         "- Their breathing gets slow and shallow.\n"
         "- Their lips turn blue or gray.\n"
         "- Their forehead feels very hot (not just sweaty).\n"
         "- They injure their head, break a bone, or bleeding won't stop.")
EXPL2 = ("If they have epilepsy or are otherwise prone to seizures, a seizure doesn't have to mean they took too much, since "
         "psychedelics can lower the seizure threshold even at a normal dose. That kind of seizure is most likely less "
         "dangerous than one from an actual overdose.")
TESTS['callp-c2'] = CALL2
TESTS['explp-c2'] = CALL2 + "\n\n" + EXPL2
TESTS['seize-c7'] = "\n\n".join([HEAD, FIRST, CALL2, EXPL2, RESCUE])

# c3, after the reads of seize-c7: the paragraph's second sentence, his point ("most likely less dangerous than an actual
# drug overdose seizure", his words), said with what the reader does with it ("which is why you give it 5 minutes before
# calling"), and its first sentence the reason first, then who, then what it means.
EXPL3 = ("Psychedelics can lower the seizure threshold even at a normal dose, so someone with epilepsy or who's otherwise prone "
         "to seizures might have a seizure without taking too much. That's most likely less dangerous than an actual drug "
         "overdose seizure, which is why you give it 5 minutes before calling.")
TESTS['explp-c3'] = CALL2 + "\n\n" + EXPL3
TESTS['seize-c8'] = "\n\n".join([HEAD, FIRST, CALL2, EXPL3, RESCUE])

# c4, after the reads of seize-c8 (all three marked "That's ... which is why you give it 5 minutes before calling": "That"
# unclear, and the 5 minutes read as a rule for every seizure): the call line says which seizure gets the 5 minutes ("A
# seizure on a normal dose"), and the paragraph opens on that scope, then his reason and his comparison.
CALL3 = ("Call medics if any of these happen:\n"
         "- They have a seizure after taking too much, or you don't know how much they took.\n"
         "- A seizure on a normal dose goes on for over 5 minutes.\n"
         "- Their breathing gets slow and shallow.\n"
         "- Their lips turn blue or gray.\n"
         "- Their forehead feels very hot (not just sweaty).\n"
         "- They injure their head, break a bone, or bleeding won't stop.")
EXPL4 = ("Waiting the 5 minutes is only for a seizure on a normal dose. Psychedelics can lower the seizure threshold even then, "
         "so someone with epilepsy or who's otherwise prone to seizures might have a seizure, and it's most likely less "
         "dangerous than an actual drug overdose seizure.")
TESTS['callp-c3'] = CALL3
TESTS['explp-c4'] = CALL3 + "\n\n" + EXPL4
TESTS['seize-c9'] = "\n\n".join([HEAD, FIRST, CALL3, EXPL4, RESCUE])

# c5, after the reads of seize-c9: "even then" said ("even at a normal dose"), and the long second sentence made two, the
# reason and his comparison, each naming whose seizure it is.
EXPL5 = ("Waiting the 5 minutes is only for a seizure on a normal dose. Psychedelics can lower the seizure threshold even at a "
         "normal dose, so someone with epilepsy or who's otherwise prone to seizures can have a seizure without taking too much. "
         "Their seizure is most likely less dangerous than an actual drug overdose seizure.")
TESTS['explp-c5'] = CALL3 + "\n\n" + EXPL5
TESTS['seize-c10'] = "\n\n".join([HEAD, FIRST, CALL3, EXPL5, RESCUE])

# Checked by themselves for the gate (apply_gate.py): the call list with its lead-in, and the paragraph (over 50 words).
TESTS['explone-c5'] = EXPL5

# callp-c4, after callp-c3 read Human with a Medium window (4d0a5d11) over its last four lines, where my forehead line made
# three "Their ..." lines in a row: his heat line kept as he wrote it ("They get dangerously hot ... (not just regular
# sweating)") with only how to tell added ("which you can feel on their forehead", 22:34 UTC).
CALL4 = CALL3.replace("- Their forehead feels very hot (not just sweaty).",
                      "- They get dangerously hot, which you can feel on their forehead (not just regular sweating).")
assert CALL4 != CALL3
TESTS['callp-c4'] = CALL4
TESTS['seize-c11'] = "\n\n".join([HEAD, FIRST, CALL4, EXPL5, RESCUE])

# callp-c5, after callp-c4 read AI (14de8a4b) and callp-c3 Human with a Medium window over its last four lines (4d0a5d11):
# the heat line short again, and said as what the reader does and finds ("When you touch their forehead, it's very hot"),
# so it no longer opens like the lines around it ("Their breathing ...", "Their lips ...").
CALL5 = CALL3.replace("- Their forehead feels very hot (not just sweaty).",
                      "- When you touch their forehead, it's very hot, not just sweaty.")
assert CALL5 != CALL3
TESTS['callp-c5'] = CALL5
TESTS['seize-c12'] = "\n\n".join([HEAD, FIRST, CALL5, EXPL5, RESCUE])

# callp-c6, after callp-c3 and callp-c5 read Human with the same Medium window over the list's last four lines, three of
# them his, whatever my heat line said (and callp-c4 AI): his heat line as he wrote it ("They get dangerously hot (not just
# regular sweating)."), which his message of 22:34 UTC answers the fit read on ("you can tell by touching someone's forehead
# how hot it is"), with only my two new lines above it.
CALL6 = CALL3.replace("- Their forehead feels very hot (not just sweaty).", "- They get dangerously hot (not just regular sweating).")
assert CALL6 != CALL3
TESTS['callp-c6'] = CALL6
TESTS['seize-c13'] = "\n\n".join([HEAD, FIRST, CALL6, EXPL5, RESCUE])

if __name__ == '__main__':
    for k, t in TESTS.items():
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest()[:12])
