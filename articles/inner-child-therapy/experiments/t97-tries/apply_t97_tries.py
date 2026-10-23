#!/usr/bin/env python3
"""Turn 97: my tries, with Joel's moves (E207, E216, E217), on the paragraphs of mine that still read AI in the turn's first
API checks (experiments/t97-api/API-RESULTS.md). His own paragraphs (How Much Happiness P4, Related Clinical Work's last
line) are not changed here: their tries are checked as texts first and go to him (drafts e04 and e06).
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
NOTE = ('<!-- Turn 97 (his message of 2026-10-22 23:54 UTC, experiments/t97-answers/JOEL-20261022-2354.md: 87, "you can learn '
        'and try"): %s Draft %s (experiments/t97-tries/drafts/). Not yet checked in Pangram. -->')
TRIES = [
    ("A good routine kept in the warden's tone still feels like punishment to your little one. If talking back to that voice feels disloyal, give it a name of its own, like the Critic. Write its lines down, with who said them and when. Comfort your little one first, then write a reply to each line, firm or funny but never mean (ST-CA has this as an exercise, section 18.12.2).",
     'e01-parent-P4.txt',
     "mine; the API read it AI, High, alone (t97_parentP4, my third try after two cuts), so this try uses his moves: the warden's metaphor carried on (lockdown, a rap sheet), named referents (the warden, the Critic), the reason as my opinion (\"since mean is the Critic's department\"), and the run of instructions broken up."),
    ("But what if you've had a big spiritual experience, and it showed you a kind of peace, or a love, you didn't know existed? Then \"I want you to be happy\" means something much bigger, almost overnight. Loving-kindness meditation can sound comically simple to someone who's never been near that, which makes sense, and so powerful to someone who has. Repeating \"may you be happy\" isn't some automatic shortcut to profound love, of course. It's one way to find that love and grow it.",
     'e02-happy-P2.txt',
     "mine; the API read it AI, Low, all of it, in the h1 (t97_happy). The \"isn't ..., of course. It's ...\" turn is gone; felt process (\"for a while you felt\"), a time anchor (\"After that\"), the reason as my opinion (\"That's why\") and a plain verb (\"won't zap you into\")."),
    ("Curious about that bigger happiness? Then follow the curiosity, and skip pretending to believe. Read people from different traditions. If you meet someone who's happy in a way that doesn't add up, see how they treat people when their own day is going badly.",
     'e03-happy-P3.txt',
     "mine; the API read it AI, Low and Medium, in the h1 (t97_happy). The question-then-order opener is gone; the advice is my opinion (\"I'd follow\"), with specific nouns (\"say a Sufi poet and a Zen teacher\") and a felt detail (\"on a day when everything's going wrong for them\")."),
    ("Some people have the opposite problem. It feels like you're connecting with your little one, but the contact is staying near the surface. Meditating for a long time and then sleeping can open up much more emotionally direct stuff, especially in a second sleep, after you've already slept once. What showed me that the daytime pl/ork had stayed shallow was the difference at night. So say you wake up from a dream with far more feeling and need in it than the session came anywhere near. That's the sign this is you (a session that was good and just didn't stick around is something else). Then ask what that dream let you feel that the session didn't, and how you understand it now. If nightmares start wrecking your sleep, do less of the practice, earlier in the day or for a shorter time.",
     'e05-shallow-P1.txt',
     "the API read AI, Low, from his night line to the end (t97_shallow); his line and the first three sentences are unchanged. My sentences after his line: the diagnosis line and its parenthesis are two plain sentences, the two-part prompt is my opinion with a felt detail (\"after your morning coffee\"), and the options closer is one instruction (\"dial the practice down\")."),
]


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')
    for old, draft, why in TRIES:
        new = (HERE / 'drafts' / draft).read_text(encoding='utf-8').strip()
        if lines.count(old) != 1:
            sys.exit('not exactly once (%d): %r' % (lines.count(old), old[:70]))
        i = lines.index(old)
        lines[i:i + 1] = [NOTE % (why, draft[:3]), '', new]
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('installed %d tries of mine' % len(TRIES))


if __name__ == '__main__':
    main()
