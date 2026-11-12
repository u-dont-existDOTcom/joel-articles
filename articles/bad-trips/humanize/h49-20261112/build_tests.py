#!/usr/bin/env python3
"""build_tests.py - turn 39's carries (2026-11-12) of his round-38 brain checks (../../experiments/t38-answers/
JOEL-TRIES-TEACH-BRAIN.md): each line of a list the kind of thing its lead-in says it holds (his one-line fix of my "First,
are they awake and breathing normally?", a sign of health in a list of warning signs, took eleven AI windows to seven
Human); "safe" said with how ("If you can safely hold them as they try"); a line that doesn't follow the one before on its
own line; the action in the lead-in; and the last line saying when to call for help. Round 38's card promised them to
Active Seizure's first aid; the section his version sits in opens on a paragraph of mine that reads AI (h42a) with the
action said fourth.

- brainopen-c1: My Brain Feels Damaged as it will read: the heading and his checks as he wrote them, and the paragraph
  before them (B103) with my opening said once and first ("Don't dismiss ..."), its two "It may be ..." sentences folded
  into the reason, and his remedy lines and his electrolytes reason after it as they are.
- seize-c1: Active Seizure's first aid (B109) as a lead-in that says what to do while it lasts and one step a line, "when
  practical" said as what to do and why ("Turn them gently onto their side, which helps them breathe."); and its call-medics line (B112) as his list
  form ("Call medics if any of these happen:"), moved to follow the first aid, before the rescue medicine (B110).
  "when practical" first became "as soon as you can do it without forcing them", which the linter fails ("X can ...
  without Y", E186); standard first aid turns the person gently onto their side to help them breathe, with no condition.

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
HIS_BRAIN = ("While the DMSO is working, check for stroke warning signs that would trigger a call to medics:\n"
             "- First, are they unconscious or breathing abnormally?\n"
             "- Feel whether they're very hot.\n"
             "- Have them talk and smile. Is their speech slurred, or does one side of their face droop?\n"
             "- Ask them to hold both arms out in front of them, and see if one drifts down.\n"
             "- If you can safely hold them as they try, have them stand and walk a few steps to see if they keep their "
             "balance.\n"
             "- Wetting or soiling themselves is another sign to watch for.\n"
             "- Watch for a seizure, and for vomiting that keeps coming back.\n"
             "- Ask about a really bad headache or chest pain.\n"
             "- Check if their vision has changed.\n\n"
             "When they're too out of it to help you do the checks, or if the brain-damage feeling stays despite sufficient "
             "treatment, then you've done what you can do, and it's time to call for help.")
HIS_B103 = ("DMSO is my first immediate remedy while I ask what the symptoms actually are. I usually know within about a "
            "minute whether it is helping. Smelling humic acid or tasting a tiny bit can also help a lot, in my experience, "
            "but I'm still collecting data from others. I add electrolytes too, because magnesium (and then potassium) can "
            "be depleted by some drugs, especially MDMA and iboga, although I don't think just electrolytes would be "
            "sufficient.")
OPEN = ("Don't dismiss someone who says their brain feels damaged just because they're high or can't explain what they feel "
        "in medical language, since something could really be going wrong in their brain.")
FIRST_AID = ("Time the seizure, and while it lasts:\n"
             "- Move anything hard or sharp away from them so they don't get hurt.\n"
             "- Loosen any tight clothing.\n"
             "- Turn them gently onto their side, which helps them breathe.\n"
             "- Don't restrain them, and don't put anything in their mouth while they're convulsing or not fully conscious.")
CALL = ("Call medics if any of these happen:\n"
        "- A convulsive seizure goes on for about five minutes.\n"
        "- Another seizure starts before they've recovered from the last one.\n"
        "- They have trouble breathing.\n"
        "- They get dangerously hot.\n"
        "- They're seriously hurt.\n"
        "- It's their first seizure, or it's substantially different from the ones they usually have.")
TESTS = {
    'brainopen-c1': ("If Someone Says \"My Brain Feels Damaged\": DMSO + Humic Acid + Electrolytes First\n\n" + OPEN + ' '
                     + HIS_B103 + "\n\n" + HIS_BRAIN),
    'seize-c1': "Active Seizure\n\n" + FIRST_AID + "\n\n" + CALL,
}

# seize-c2, after the read against his fixes (reads/his-seize-c1.txt) and the fidelity check: "dangerous" kept (W014's
# warning word, "clear dangerous objects"), the two don'ts one a line, and the call list's vague lines said with what the
# guide's own Call medics list says counts (its "Dangerous overheating (not just regular sweating)" is his aside).
FIRST_AID2 = ("Time the seizure, and while it lasts:\n"
              "- Move any dangerous objects away from them, especially anything hard or sharp.\n"
              "- Loosen any tight clothing.\n"
              "- Turn them gently onto their side, which helps them breathe.\n"
              "- Don't restrain them.\n"
              "- Keep everything out of their mouth while they're convulsing or not fully conscious.")
CALL2 = ("Call medics if any of these happen:\n"
         "- A convulsive seizure goes on for about five minutes.\n"
         "- Another seizure starts before they've recovered from the last one.\n"
         "- Their breathing gets slow and shallow.\n"
         "- Their lips turn blue or gray.\n"
         "- They get dangerously hot (not just regular sweating).\n"
         "- They're seriously hurt, like bleeding that won't stop or a possible head injury.\n"
         "- It's their first seizure, or one that's substantially different from their usual ones.")
TESTS['seize-c2'] = "Active Seizure\n\n" + FIRST_AID2 + "\n\n" + CALL2

# seize-c3, after the second read (reads/his-seize-c2.txt): the don't with its reason, and three signs in a row that
# opened the same way ("Their ...", "Their ...", "They ...") built differently.
FIRST_AID3 = FIRST_AID2.replace("- Don't restrain them.", "- Don't restrain them, since that can cause injuries.")
CALL3 = CALL2.replace("- Their lips turn blue or gray.", "- Blue or gray lips are another sign.")
TESTS['seize-c3'] = "Active Seizure\n\n" + FIRST_AID3 + "\n\n" + CALL3

# seize-c4, after seize-c3's check (36fbfa7d, Human Written, its one Low window "- Blue or gray lips are another sign.",
# the line the third read marked as saying a sign of nothing): the line says what it means.
CALL4 = CALL3.replace("- Blue or gray lips are another sign.", "- Lips turning blue or gray, which means they aren't getting enough air.")
TESTS['seize-c4'] = "Active Seizure\n\n" + FIRST_AID3 + "\n\n" + CALL4

# seize-c5, after seize-c4 read worse (AI Detected, 39%, c61ad5f7): the Low line said the plain way the second draft had it,
# "Their lips turn blue or gray." (read in reads/his-seize-c2.txt, marked only for opening like its neighbours).
CALL5 = CALL3.replace("- Blue or gray lips are another sign.", "- Their lips turn blue or gray.")
TESTS['seize-c5'] = "Active Seizure\n\n" + FIRST_AID3 + "\n\n" + CALL5

# er-c1: Acute Medical's emergency room paragraph (B77), after acute-c1 (h48, in): its opening ("The emergency room is not
# magic, and for a physiologically stable psychedelic or practice-induced crisis it may be a poor environment.") says again
# what acute-c1's last sentence says, so it goes; the drugs said plainly, the two sentences built differently.
ACUTE = ("Acute Medical and Neurological Rescue\n\n"
         "I'd calm and stabilize the trip right where they are, as long as none of the signs on the Call medics list above "
         "show up and I can keep them from getting hurt. Even from a severe trip, they can come down faster that way than "
         "after an ambulance ride and hours in an emergency room.")
ER = ("In an emergency room, a scared, psychotic-feeling person will often get a benzodiazepine. Those only sometimes help "
      "with psychosis, and in some people they bring on more agitation or fear instead, a paradoxical reaction. Antipsychotics "
      "may work better for psychosis, but they carry their own risks and interactions, and the staff giving them often don't "
      "know what was taken, if anything.")
TESTS['er-c1'] = ACUTE + "\n\n" + ER

# er-c2, after the reads of er-c1 (reads/his-er-c1.txt, reads/needed-er-c1.txt): "Those" named, the comma pair joined
# with "and", the term said where it is used, the antipsychotics sentence taken apart, and the paragraph ending on what
# the reader does with it (the needed read called the antipsychotics sentence unneeded: it ends on a worry with nothing to do).
ER2 = ("In an emergency room, a scared and psychotic-feeling person will often get a benzodiazepine. Don't count on it "
       "helping with psychosis, since in some people it does the opposite and brings on more agitation or fear, which is "
       "called a paradoxical reaction. Antipsychotics may work better for psychosis, but they carry their own risks and "
       "interactions. The staff also often have no idea what was taken, if anything, so if you do end up there, tell them.")
TESTS['er-c2'] = ACUTE + "\n\n" + ER2

# er-c3, after the read of er-c2 (reads/his-er-c2.txt): the drug's effect said as itself, with its term right there,
# instead of "it does the opposite ... which is called a paradoxical reaction".
ER3 = ER2.replace("since in some people it does the opposite and brings on more agitation or fear, which is called a "
                  "paradoxical reaction.", "since in some people it brings on a paradoxical reaction, with more agitation or "
                  "fear.")
assert ER3 != ER2
TESTS['er-c3'] = ACUTE + "\n\n" + ER3

if __name__ == '__main__':
    for k, t in TESTS.items():
        p = HERE / ('TEST-%s.txt' % k)
        p.write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest()[:12])
