#!/usr/bin/env python3
"""build_tests.py - turn 37's carries (2026-11-12), after his round-36 answers and the read of his 112 fixes
(his-fixes/HOW-HE-FIXES.md): TEACH-SS's promise, "I test what it teaches on the sections above" (Chest Pain's warning
signs, the checks in My Brain Feels Damaged, the Call medics list). Written against the eight differences, then read by a
fresh reader against them (tools/humanization/his_fixes_brief.md) before any check.

- chest-c1: Chest Pain and Injury's branch paragraph (B124): his SS form, a lead-in and one line a sign, each line built
  differently, the plain words for the clinical ones; "is different from" and "does not prove" said as what to do.
- brain-c1: My Brain Feels Damaged's checks (B104): the fourteen checks said as what to look for, in lines built
  differently, W007's "checks", "recognized" and "warning" kept.

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
TESTS = {
    'chest-c1': ("Chest Pain and Injury\n\n"
                 "For chest pain that's mild and familiar, I'd just use DMSO, as long as it's holding steady and they're "
                 "fully alert. It's more serious if:\n"
                 "- The pain is new to them, or hasn't let up.\n"
                 "- It's severe, or keeps getting worse.\n"
                 "- Physical effort brought it on.\n"
                 "- It spreads out from the chest, like into an arm or the jaw.\n"
                 "- They're short of breath or sweating along with it.\n"
                 "- Any of the warning signs from the brain checks above show up.\n"
                 "- They feel faint, or collapse.\n\n"
                 "Then I'd still use DMSO, but call medics at the same time. When you're unsure which kind it is, treat it as "
                 "the serious kind. DMSO can also block pain signals, so if the pain fades, still let the medics check them."),
    'brain-c1': ("If Someone Says \"My Brain Feels Damaged\": DMSO + Humic Acid First\n\n"
                 "While the DMSO is working, check them over. Several of these checks are recognized stroke warning signs:\n"
                 "- First, are they awake and breathing normally, and how hot are they?\n"
                 "- Have them talk and smile: slurred speech, or one side of the face drooping, is a warning sign.\n"
                 "- Ask them to hold both arms out in front of them. If an arm drifts down, that's another.\n"
                 "- Watch them stand and walk, if that's safe. Losing their balance counts, and so does losing control of "
                 "their bladder or bowels.\n"
                 "- Keep an eye out for a seizure, or for vomiting again and again.\n"
                 "- Ask if they have a really bad headache or chest pain, and check whether their vision has changed.\n\n"
                 "When they're too out of it to answer you or do the checks, count that as a warning sign too, since nobody "
                 "can see what's happening in their brain. If everything checks out but the brain-damage feeling stays, keep "
                 "going with the DMSO and check them again soon."),
}
# Second drafts, after the read against his fixes (HIS-FIXES-READ.md): chest-c1's list lines built the same way (", or"
# three times) and "the warning signs from the brain checks above" not saying which; brain-c1's checks packed three to a
# line. Both read again before any check.
TESTS2 = {
    'chest-c2': ("Chest Pain and Injury\n\n"
                 "For chest pain that's mild and familiar, I'd just use DMSO, as long as it's holding steady and they're "
                 "fully alert. It's more serious if:\n"
                 "- It's severe, or a kind of pain they've never had before.\n"
                 "- It won't let up or keeps getting worse.\n"
                 "- Physical effort brought it on.\n"
                 "- It spreads out from the chest, like into an arm or the jaw.\n"
                 "- Shortness of breath or sweating comes with it.\n"
                 "- Any of the stroke signs from the brain checks above show up, like slurred speech or a drooping face.\n"
                 "- They feel faint, or they collapse.\n\n"
                 "Then I'd still use DMSO, but call medics at the same time. When you're unsure which kind it is, treat it as "
                 "the serious kind. DMSO can also block pain signals, so if the pain fades, still let the medics check them."),
    'brain-c2': ("If Someone Says \"My Brain Feels Damaged\": DMSO + Humic Acid First\n\n"
                 "While the DMSO is working, check them over. Several of these checks are recognized stroke warning signs:\n"
                 "- First, are they awake? Check their breathing, and feel whether they're very hot.\n"
                 "- Have them talk and smile: slurred speech, or one side of the face drooping, is a warning sign.\n"
                 "- Ask them to hold both arms out in front of them. If an arm drifts down, that's another.\n"
                 "- Watch them stand and walk, if that's safe. Losing their balance counts, and so does losing control of "
                 "their bladder or bowels.\n"
                 "- Look out for a seizure. Vomiting again and again is a sign as well.\n"
                 "- Ask whether they have a really bad headache, and whether their chest hurts.\n"
                 "- Check if their vision has changed.\n\n"
                 "For objective stroke-like signs, I would use DMSO immediately while someone calls medics. When they're too "
                 "out of it to answer you or do the checks, count that as a warning sign too, since nobody can see what's "
                 "happening in their brain. If everything checks out but the brain-damage feeling stays, keep going with the "
                 "DMSO and check them again soon."),
}

# Third drafts, after the second read against his fixes (HIS-FIXES-READ.md): chest-c2's lines opening "It" three times and
# "Physical effort" not saying what counts; brain-c2's "that's another", "counts" and "is a sign as well" not saying of
# what, two checks to a line, the moved sentence's "objective stroke-like signs", and an aside the reader can lose.
TESTS3 = {
    'chest-c3': ("Chest Pain and Injury\n\n"
                 "For chest pain that's mild and familiar, I'd just use DMSO, as long as it's holding steady and they're "
                 "fully alert. It's more serious if:\n"
                 "- The pain is severe, or new to them.\n"
                 "- It won't let up or keeps getting worse.\n"
                 "- Hard movement brought it on, like dancing or climbing stairs.\n"
                 "- From the chest it spreads into an arm or the jaw.\n"
                 "- Shortness of breath or sweating comes with it.\n"
                 "- Any of the stroke signs from the brain checks above show up, like slurred speech or a drooping face.\n"
                 "- They feel faint, or they collapse.\n\n"
                 "Then I'd still use DMSO, but call medics at the same time. When you're unsure which kind it is, treat it as "
                 "the serious kind. DMSO can also block pain signals, so if the pain fades, still let the medics check them."),
    'brain-c3': ("If Someone Says \"My Brain Feels Damaged\": DMSO + Humic Acid First\n\n"
                 "While the DMSO is working, check them over. Several of these checks look for recognized stroke warning "
                 "signs:\n"
                 "- First, are they awake and breathing normally?\n"
                 "- Feel whether they're very hot.\n"
                 "- Have them talk and smile. Is their speech slurred, or does one side of their face droop?\n"
                 "- Ask them to hold both arms out in front of them, and see if one drifts down.\n"
                 "- If it's safe, have them stand and walk a few steps to see if they keep their balance. Wetting or soiling "
                 "themselves is another sign to watch for.\n"
                 "- Watch for a seizure, and for vomiting that keeps coming back.\n"
                 "- Ask about a really bad headache or chest pain.\n"
                 "- Check if their vision has changed.\n\n"
                 "So if you see any of these signs, keep the DMSO going while someone calls medics. When they're too out of it "
                 "to answer you or do the checks, count that as a sign too. If everything checks out but the brain-damage "
                 "feeling stays, keep going DMSO-first and check them again soon."),
}

if __name__ == '__main__':
    for k, t in list(TESTS.items()) + list(TESTS2.items()) + list(TESTS3.items()):
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
