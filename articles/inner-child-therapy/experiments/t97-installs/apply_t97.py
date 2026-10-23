#!/usr/bin/env python3
"""Turn 97: put in Joel's two rewrites of 2026-10-22 23:54 UTC word for word (experiments/t97-answers/JOEL-20261022-2354.md).

Before You Try to Go Deep: his P1 and P2 are the article's already (checked here); his P3 and P4 replace mine.
Your Body Might Need Some Love First: his P3, P4 and P5 replace the three paragraphs he quoted as the AI version
(round 4's text, with the gym line my turn-96 cut d01 had taken out). The only change to his text: the double space
in "difference.  You can" is one space, and trailing spaces are gone.
"""
import pathlib
import sys

ART = pathlib.Path(__file__).resolve().parents[2] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SRC = 'experiments/t97-answers/JOEL-20261022-2354.md'

HIS_BYT_P1 = ("How much of the grown-up you is actually here right now? Try looking around the room, pausing before you act, making a choice and following through on it. If you can't do that because you're basically the frightened kid, leave the deeper conversation until later. You may need somebody steady there with you, or to do whatever helps you come back a bit before you try to talk to the child.")
HIS_BYT_P2 = ("And if the grown-up you is there, and it's just how deep you're going that's too much, I'd go shallower. Like the flight attendants say, it's good to know where the exits are. 😅 So can you stop in the middle and come back to the room? If you can't, or going in at all keeps making it worse, I'd come all the way back out first. Some people try one technique after another instead, to prove to themselves they can take it. Your little one may have had to just take it back then, though. Now there's a grown-up around who can say, \"Okay, that's enough for today,\" and try something gentler, like saying hi to them with your eyes open.")

REPLACE = [
    # (old line, his new line, turn note)
    ("A full break from your little one is a last resort, unless something's actually unsafe. If you do need a break, I'd jot down why and how far you'd gotten, and come back there once that reason has changed.",
     "If you need a break from the communion, simply jot down the reason and the progress made so far. Then come back later, once that reason has changed and you feel comfortable.",
     "<!-- Turn 97 (his message of 2026-10-22 23:54 UTC, %s; his answer to question 87): his rewrite of Before You Try to Go Deep, word for word (\"i made some improvements and now it's dark green for the whole section\"). This paragraph is his; it replaces mine (turn 95's third reading after two cuts, still AI in round 4: Low 58). His P1 and P2 were the article's already. -->" % SRC),
    ("If being alone was a big part of what hurt, I'd call somebody now, mess and all, since reaching toward people is part of taking care of your little one too.",
     "If being alone was a big part of what hurt during your childhood, I'd call somebody now, mess and all, since reaching toward people is part of taking care of your little one too. Even if you don't have someone you know who wants to listen, there are warmlines for this.",
     "<!-- Turn 97 (his message of 2026-10-22 23:54 UTC, %s): his rewrite of Before You Try to Go Deep, word for word; this paragraph is his (\"during your childhood\" and the warmlines sentence are his additions). -->" % SRC),
    ("When your nervous system is flooded, your protective parts are busy with the flood, so they're not going to let your little one come out and talk much anyway. Some people go straight into EMDR on their worst memory before they can even stay in the room. Then they get flooded all over again and decide EMDR doesn't work. Here's a map of what to try when:",
     "When your nervous system is flooded, your protective parts are busy throwing buckets of water out of the boat, so they’re not going to let your little one come out and talk much anyway. Some people go straight into EMDR to work on desensitizing their worst memory before they can even stay in the room. Then they get predictably flooded all over again and, running low on buckets, they decide EMDR doesn’t work. Here’s a map of what to try when:",
     "<!-- Turn 97 (his message of 2026-10-22 23:54 UTC, %s; his answer to question 87): \"i will do one more for you tho, this is the ai section here\", then \"this is the all dark green version\". His three paragraphs, word for word, replace the three he quoted (this one, round 4's Low 31 on EMDR; my P4 with its gym line, Medium 53 and High 31; his P5's questions, High 18). -->" % SRC),
    ("Whatever you try from that map, I wouldn't go just by how pleasant a session felt to tell whether it was too much, or by whether you stayed present through it. Somatic work can bring up grief and fear, and sometimes hard dreams.",
     "Some somatic work can feel pleasant, and some can feel like a raging storm got unleashed. It can bring up grief and fear, and sometimes nightmares later on as the memories begin to unwind. It’s a bit like going to the gym. You want to make gains, and sore muscles the next day can be good, but proper range of (e)motion here is also key to avoid injury.",
     "<!-- Turn 97 (his message of 2026-10-22 23:54 UTC, %s): his paragraph, word for word. It replaces my P4 (my turn-96 cut d01, the gym line out, never checked) with his own gym comparison. -->" % SRC),
    ("So how were the next few days? How did you sleep, and could you get through your day okay? Do you want to go back toward what came up, or is some part of you saying no? (And was it hard but doable, or just too much?) If you honestly can't tell yet, I wouldn't rush to call it healing or harm. I'd just make the next one a bit easier (shorter, or shallower, at a better time of day, with your eyes open, a teddy bear standing in for your little one, or a friend in the next room), one change at a time, so you learn what made the difference.",
     "Keep track of how you feel over the next few days, like how refreshing your sleep is, and how easy it feels to get through your day. Do you want to go back toward what came up, or is some part of you saying no? If you can’t quite tell yet, I’d just make the next one a bit easier, one change at a time, like a science nerd, so you learn what made the difference. You can play around with variables like shorter session length, or shallower diving, time of day, keeping eyes open, having a friend around, or holding a teddy bear as a stand-in for your little one.",
     "<!-- Turn 97 (his message of 2026-10-22 23:54 UTC, %s): his paragraph, word for word, except one space for the two in \"difference.  You can\". It replaces his own P5 (its questions read High in round 4). -->" % SRC),
]


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')
    for want in (HIS_BYT_P1, HIS_BYT_P2):
        n = lines.count(want)
        if n != 1:
            sys.exit('his paragraph is not the article\'s exactly once (%d): %r' % (n, want[:70]))
    for old, new, note in REPLACE:
        n = lines.count(old)
        if n != 1:
            sys.exit('old paragraph found %d times: %r' % (n, old[:70]))
        i = lines.index(old)
        lines[i:i + 1] = [note, '', new]
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('installed %d paragraphs of his; his P1 and P2 of Before You Try were the article\'s already' % len(REPLACE))


if __name__ == '__main__':
    main()
