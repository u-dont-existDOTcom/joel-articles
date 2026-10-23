#!/usr/bin/env python3
"""Turn 98: Joel's message of 2026-10-23 02:29 UTC (experiments/t98-answers/JOEL-20261023-0229.md), put in word for word.

- 88.1: his How Much Happiness Do You Know Is Possible? (four paragraphs for the five, in his order: wishing well, the
  existential question, the spiritual experience, curiosity with the quote). His check: "human high conf 100%".
- 88.2: his When the Practice Feels Real but Stays Shallow (one paragraph). His check: "dark green".
- 88.3: his The Parent You Inherited (five paragraphs; the ST-CA reference cut). His check: "100% dark green". Two typos
  fixed, nothing else: "hanlde" to "handle", "pont" to "point".
- 89: A, my wording of his Related Clinical Work line (draft e06, 100% Human with its section in turn 97).
Each new paragraph takes its old paragraph's line, under the old notes, with a turn-98 note first.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SRC = 'experiments/t98-answers/JOEL-20261023-0229.md'

HAPPY = [
    "When you wish someone well, what do you have in mind? Probably something like, “I want them to have enough to eat, a safe place to sleep, some people who like them, etc.” Wanting this for someone is a form of love (this is the kind babies already understand). It’s a good and important thing, this practical love. But the horizon of your wishes may be partly determined by how much happiness/peace/freedom you know to be possible.",
    "Sometimes your little one already feels cared for in the normal ways, well fed, good boundaries at work, but will either of these actually deal with the existential issue? Maybe your life isn’t meant to be just something to put up with, something to slog through, a hamster wheel, a rat race. Maybe you could live it with a sense of zest and discovery. What would you need for that?",
    "Maybe you’ve had some big spiritual experiences, and for a while knew a kind of peace/love etc. that you hadn’t known before. Now when you wish someone well, your wishes may be bigger – perhaps much bigger – than they would have been before. This is one reason why loving-kindness meditation can seem kind of silly (who doesn’t want people to be happy!?) but actually be very powerful. Saying, “May you be happy,” over and over won’t necessarily zap you into a state of profound love for all beings, but it’s one way people discover that there is such a love and learn to expand it.",
    "If you’re curious about this bigger happiness, follow that curiosity. You don’t have to pretend to believe anything, but you might read a few people from different traditions (try a Sufi poet or a Zen teacher). If you know anyone who seems consistently happy in this bigger way, check out how they deal with people when things are going badly. And if they still pass that test, consider, \"I don’t know if I believe their explanation. But what if the experience is possible for me?”",
]
SHALLOW = "Some people have the opposite problem, where it feels like they’re connecting with their little boo, but then they find out somehow that it was still pretty superficial. Dreams can open up much more emotionally direct stuff, especially in the second half of the night's sleep, if you wake up in the middle to meditate, as I've discovered. That's a good point to ponder over what the dream let you feel that the session didn’t, and look at it again in the morning (but write it down so you remember!). And if nightmares start wrecking your sleep, shorten the practice or do it earlier."
PARENT = [
    "I’d look at the parent “script” you inherited: how you learned to treat yourself from how people treated you growing up. Maybe sometimes that script feels warm, but maybe too often it feels more like a critic, or a warden with rules. The rules can even sound totally reasonable, like “You can come back to the table when you’re done with your embarrassing crying fit.” If your childhood was like that, your little one learned bit by bit to hide that part of their authentic self which wasn’t allowed to show up, so they could keep belonging. And if so, do a double check: they might still be doing it!",
    "If the script is mostly critical, it means the parent you inherited is busy measuring whatever you show the world against an impossible ideal. Then you can feel attacked from both sides: not only are you not good enough, but if you do seem to be good enough, it's probably fake, so it's like nothing you do really counts. When a new grown-up voice shows up saying “Trust me,” with a background like that, well, of course your little one doesn’t answer.",
    "But with the borrowed adulthood trick, the new grown-up can start outside your head, as someone who likes you just the way you are, or as something you do to protect your little sweetie pie, like letting the phone ring when you know already how that call goes. You don’t have to pretend to feel anything to let a phone ring. It may take many such ignored calls before your inner child can start trusting you, and all the while, the parent you inherited calls your efforts fake.",
    "A good routine, like yoga in the morning and a proper bedtime, still feels like lockdown to your little one when it’s done in a disciplinarian style. One exercise you can do to handle this is to go back and rewrite your responses to that strict disciplinarian. First, remember who it was that drove you so hard as a child. Then start a little rap sheet of their provoking lines. Comfort your little one before you answer any of it. Your answers can be firm or funny, as long as they aren’t mean, since mean is the Critic’s department.",
    "The Critic's voice can often pile on, to the point where you can't even understand why or what you're really feeling anymore. You feel sad at first, then the Inner Critic calls your inner child pathetic for being sad, and now you’re ashamed and want to hide. You could probably have handled the sadness with some simple nurturing instead from the beginning, but now you have to peel back this other nonsense to get to it.",
]
RELATED_NEW = "This framework developed through the teachers and collaborators credited below and my own practice. Later revisions also compare notes with schema therapy, compassion-focused therapy, attachment repair, motivational interviewing, mentalizing, metacognitive therapy, behavioral activation, radically open DBT, emotion-focused therapy and spiritually integrated psychotherapy. I borrow particular ideas and practices from each of them, but the mix is mine, so please don't blame them for it."


def note(what):
    return '<!-- Turn 98 (his message of 2026-10-23 02:29 UTC, %s): %s -->' % (SRC, what)


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')

    def para_lines(head, stop):
        i = lines.index(head)
        out = []
        for k in range(i + 1, len(lines)):
            if lines[k].startswith(stop):
                break
            if lines[k].strip() and not lines[k].startswith('<!--'):
                out.append(k)
        return out

    edits = []  # (line index, new lines)
    hp = para_lines('# How Much Happiness Do You Know Is Possible?', '## ')
    assert len(hp) == 5, hp
    first = note('88.1, his rewrite of How Much Happiness Do You Know Is Possible?, word for word ("that was not very well written aside from being AI, this is better and human high conf 100%"). Four paragraphs for the five, in his order: wishing well, the existential question (his old P4), the spiritual experience, curiosity with the quote (my old P3 and P5). The notes under each paragraph below describe the old paragraph that held its place.')
    edits.append((hp[0], [first, '', HAPPY[0]]))
    for k, new in zip(hp[1:4], HAPPY[1:]):
        edits.append((k, [note('his rewrite of the h1, word for word (88.1).'), '', new]))
    edits.append((hp[4], [note('88.1: this paragraph is gone; its quote ends his last paragraph above.')]))
    sp = para_lines('## When the Practice Feels Real but Stays Shallow', '#')
    assert len(sp) == 1
    edits.append((sp[0], [note('88.2, his rewrite of the paragraph, word for word ("that was also a bad paragraph. i fixed it and it\'s also now dark green"). His night line and my sentences after it are gone.'), '', SHALLOW]))
    pp = para_lines('## The Parent You Inherited', '## ')
    assert len(pp) == 5
    for n, (k, new) in enumerate(zip(pp, PARENT)):
        what = ('88.3, his rewrite of The Parent You Inherited, word for word except two typos ("hanlde", "pont"): "that reference was too taxing for sucha small exercise, not necessary, i cut it. in general too much polish on this section, like a weird mix of overly efficient prose with actual lack of meaning." His check: "100% dark green on pangram". 90: A is covered by it.'
                if n == 0 else 'his rewrite of the section, word for word (88.3).')
        edits.append((k, [note(what), '', new]))
    rp = para_lines('## Related Clinical Work', '## ')
    assert len(rp) == 1
    edits.append((rp[0], [note('89: A, my wording of his last line goes in (draft e06, experiments/t97-tries/drafts/; 100% Human with its section in turn 97, check t97b_related_try).'), '', RELATED_NEW]))
    for k, new in sorted(edits, reverse=True):
        lines[k:k + 1] = new
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('installed: How Much Happiness (4 for 5), Stays Shallow, The Parent You Inherited (5), Related Clinical Work (89: A)')


if __name__ == '__main__':
    main()
