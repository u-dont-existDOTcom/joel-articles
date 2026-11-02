"""The windows of batch w1102 (the whole guide in two halves, ../whole/WINDOWS.md) that read AI or Human (Low), fixed.

Joel, 2026-11-02 19:11 UTC: "but you're saying we still ahve to fix some stretches" and "28a". Gate E306: fix every AI or
Human (Low) window; E321: what turned his own texts Human, in order: a specific, silly example for a general one; a tidy
closer cut or said plainly; a sentence that sums up, cut; an explanation folded into its sentence and short sentences
joined; a stock frame said the way people talk.

Whose words each window is (../whole/read_w1102.py, then read by the lead session against his published version and his
inner child guide, E314):
- OURS (fixed here, in place once their checks read Human): our rewrites of his published lines, and our own lines.
- CARDS: three are his inner child guide's lines, shortened or reworded when they came in (E314); the suggestion puts
  his lines back as he wrote them. One is his own text of 2 November (W-685, the forgiveness quote), which read Human
  (High) for him by itself and AI in the whole; the card offers a tested change and his own choice.
- KEPT, with the reason (no change offered): his own words that read Human (Low) only in the whole (his "Then put the
  screen away.", his opening of Don't rush the repair, his Reframing paragraph, his "Let yourself feel the remorse"), and
  the windows of one or two words in the countdowns ("4.", "1.", "3. Leave a little space. 2.").

  python3 articles/inner-signal/humanize/fix-20261102/w1102fix/fixes_w1102.py
Prints each edit; import it for EDITS and apply().
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

GUIDE_SHA = 'a789009c3777ede488fa8b3fce233874d42e88acc6f7adee186eb571eb2d0e00'

# (id, block, kind, old (exact, in the block's Markdown; its text without link targets is in the block's text), new, why)
EDITS = [
    ('F-11', 11, 'ours',
     "And mind you, the deeper mind is still running all of the programs it’s running: the inner child mind wanting to feel "
     "safe, the guard mind bracing for danger (childhood protector parts, the protective reactions learned as a child), the "
     "body mind remembering what your intellect explained away, the intuitive mind speaking up before you have the words, and "
     "the fantasy mind trying to become guidance mind, etc etc.",
     "And mind you, the deeper mind is running all of its programs the whole time. Your inner child still wants to feel safe. "
     "The guards are bracing for danger, because that’s how you learned to protect yourself as a kid. Meanwhile your body "
     "remembers what your intellect explained away. Intuition speaks up before you have the words, and your fantasy mind keeps "
     "applying for the job of guidance mind.",
     'Human (Low): one list of five minds, each "the X mind doing Y"; said one at a time, each with its own verb (his tries, '
     'SEQUENCES.md), and the fantasy mind applying for a job (E321, a silly specific)'),
    ('F-16', 16, 'ours',
     "I combine this with [inner child reparenting](http://innerchild.u-dont-exist.com/) (a clever suggestion won’t heal a "
     "hurt young part), and also aspects of "
     "prompt engineering (the shape of a question changes the kind of answer we can hear), as well as influence literacy, since "
     "hypnosis is hardly the only thing hypnotizing us.",
     "I combine this with [inner child reparenting](http://innerchild.u-dont-exist.com/), because a hurt young part isn’t "
     "going to be fixed by one clever suggestion. "
     "I also borrow from prompt engineering, since the way you word a question changes what answers you can hear, and from "
     "influence literacy, since hypnosis is hardly the only thing hypnotizing us.",
     'Human (Low): two asides in brackets that explain; folded into their sentences (E321)'),
    ('F-20', 20, 'ours',
     "You'll follow whatever you notice - sensation, image, phrase, feeling, objection, silence - and let it shape your next "
     "invite.",
     "Follow whatever shows up, even if it’s an objection or a long silence, and let it shape what you invite next.",
     'AI (Low): a list of six between dashes; "whatever shows up" carries the six, and the two a reader would not expect '
     'stay named'),
    ('F-42', 42, 'ours',
     "Legitimate influence can stand up to questions, sleep, boundaries and time.",
     "If it’s legit, it’ll still make sense after you’ve slept on it and asked all your annoying questions, and it can take a "
     "no and wait.",
     'Human (Low): a maxim that sums up (his published "Legitimate influence can survive questions, sleep, boundaries, and '
     'time."); the same four tests said as things you do'),
    ('F-140', 140, 'ours',
     " So before you decide where it's coming from, ask it. What is it trying to stop? What does it want from you?",
     "",
     'AI (Low) and AI (Medium): my C1 fix of this morning, Human in its section and AI in the whole; it sums up what the '
     'paragraph before says and asks what the next paragraph asks in his words ("What\'s going on?"), so it goes'),
    ('F-216', 216, 'ours',
     "Anyone worth following leaves your adult self more present. The more powerful the state you’re in, the stronger the "
     "boundaries you’ll need.",
     "Do I come away from them more present and grown up, or less? And the deeper the state you’re in, the more you need "
     "your boundaries, the way you need a seatbelt more on the highway than in a parking lot.",
     'AI (Low) and AI (Medium): two maxims (his published "A useful guide leaves the adult self more present. Powerful '
     'states need stronger boundaries."); the first asked as one more of the questions above it, the second with a '
     'specific picture (E321)'),
    ('F-218', 218, 'ours',
     "Be aware that even permissive language can still take away the subject’s choice.",
     None,
     'Human (Low): it says what its heading says ("Soft language can still take away choice"), a repeat (E320); the '
     'paragraph goes and the section starts with what follows'),
    ('F-251', 251, 'ours',
     "Either way, keep the instructions about how to stay safe and how to get out plain.",
     "Just don’t get poetic with the parts about how to stay safe and how to get out. Keep those as plain as a fire exit "
     "sign.",
     'AI (Medium): a closer (his published "Keep safety and exit instructions plain."); said the way people talk, with a '
     'picture'),
    ('F-253', 253, 'ours',
     "You can read this slowly into your recorder, or you can read it out loud or say it to yourself if you are good at that. "
     "Choose a sound, or a contact, or the two-hand practice (above) or something to anchor yourself, and choose a phrase you "
     "will say to open it up. Use the same anchor wherever the script mentions it. Don't read the directions out loud, just "
     "pause between paragraphs.",
     "Read this slowly into your phone’s voice recorder, or read it out loud. Saying it to yourself in your head works too, "
     "if you can keep your place. Pick one thing to anchor yourself with. It could be a sound in the room or the feel of the chair under you. "
     "The two-hand practice from above is another good one. Whichever you pick, use it every time the script mentions your anchor, and "
     "pick a phrase you’ll say to open things up. When you read it, skip the directions and just pause between paragraphs.",
     'AI (High), the strongest window: a list of anchors asked in one breath and four short instructions; the anchors '
     'split into two sentences, the steps joined, and a phone\'s voice recorder for "your recorder"'),
    ('F-255', 255, 'ours',
     "You can allow your eyes to rest on something in the room for a bit.",
     "Let your eyes rest on something in the room for a bit, maybe a doorknob or a spot on the wall.",
     'AI (Low): the script\'s first line in a stock permissive frame; a specific thing to look at (E321). His published '
     'line after it ("notice the difference between looking for something and letting what is already there come into '
     'view") stays'),
    ('F-265', 265, 'ours',
     "Bring to mind, if you want, the thing that you want to talk about, or just the wish to have inner contact. Just let it "
     "be there for now. You don't need to tell the whole story yet.",
     "Bring to mind, if you want, the thing that you want to talk about, or just the wish to have inner contact, and let it "
     "sit there without telling the whole story yet.",
     'Human (Low): a reassurance closer ("You don\'t need to tell the whole story yet."), folded into the sentence before'),
    ('F-527', 527, 'ours',
     "Milton Model language opens things up, and Meta Model questions ask what exactly someone means. If you want to be "
     "ethical with people, you need both.",
     "Milton Model language opens things up, and Meta Model questions pin it back down to what someone actually means, which "
     "is how you keep the first one honest.",
     'Human (Low), lineage HG1102-69-P10 (two tries read AI in their stretch, r1102b D1 and D2): new diagnosis from E321, the '
     'closer "If you want to be ethical with people, you need both." folded into the sentence, and a specific example '
     'below'),
    ('F-528', 528, 'ours',
     "When something sounds true but vague, ask:",
     "Say a workshop leader tells you, “Once you heal your inner child, everyone will love you.” Everyone? Your ex too? "
     "When something sounds true but vague like that, ask:",
     'Human (Low): the questions are the Meta Model itself and stay; a silly, specific vague claim goes in front of them '
     '(E321)'),
    ('C-141', 141, 'card',
     "Talk to the guard the way your Nurturer talks to your inner child: “I see you. I'm not going to force my way past you. "
     "What's going on?” Then wait and listen patiently. If nothing comes back, that's okay, you don't need to push for an "
     "answer.",
     "You can tell that part something like, “I see you. I'm not going to force my way past you. What's going on?” Or "
     "however you'd actually say that. Then wait and listen patiently. If nothing comes, that's fine for now. No need to answer "
     "for that part just because you'd set this up as a healing session.",
     'AI (Low) and two Human (Low): his inner child guide\'s lines, reworded when they came in (E314); the card puts his lines '
     'back as he wrote them'),
    ('C-384', 384, 'card',
     "If it says yes, that can sting, because there could be something to it. Maybe you've fooled yourself before, and that "
     "part of you remembers it. \"Tell me what you remember, I'm listening.\" works well here.",
     "If it says yes, that one can sting, because there could be something to it. Maybe you've fooled yourself before, and that "
     "part remembers. \"Tell me what you remember, I'm listening.\" works well here. It puts you into the role of the "
     "Nurturer, which alleviates the instinct to argue back.",
     'Human (Low): his inner child guide\'s lines, shortened when they came in (E314); the card puts his lines back, with his '
     'reason for the question'),
    ('C-626', 626, 'card',
     "If you can't genuinely say all that and feel it, then just rest your hands there and notice what you find.",
     "No warmth today? Then rest your hands there and notice what you find, no faking required.",
     'Human (Low): his inner child guide\'s line, reworded when it came in (E314); the card puts it back'),
    ('C-672', 672, 'card',
     "But I’m also not going to build our whole life around this wound forever.”",
     "We’re not moving into this wound for good, either.”",
     'AI (High) and AI (Low) in the whole: his own text of 2 November (W-685), Human (High) for him by itself; the AI pattern '
     'is the matched pair "I\'m not going to ... But I\'m also not going to ...", and the suggestion keeps its point with a '
     'picture and no matched "not going to"'),
]

KEPT = [
    (19, '"Then put the screen away." (Human (Low), 5 words)', 'his own words (a paragraph he rewrote); five words read Low '
     'only beside the line that follows, which is fixed (F-20)'),
    (160, 'his opening of Don\'t rush the repair (Human (Low), 24 words)', 'his own words; Human (High) by themselves in his '
     'check (https://www.pangram.com/history/14c44cec-57e0-4b80-b7bc-fbfed1a8c304), kept on 2 November'),
    (264, 'the countdown "4.", "3. Leave a little space. 2.", "1." (Human (Low), 1 to 6 words)', 'list numbers and a '
     'three-word step: nothing in them to change'),
    (560, 'his Reframing paragraph (Human (Low), 57 words, with its heading)', 'his own words; Low only in the whole, and the '
     'window is mostly his examples of questions'),
    (674, '"Let yourself feel the remorse by taking in the harm done." (Human (Low), 11 words)', 'his own words (W-685); '
     'read beside the card C-672 in its section'),
    (738, '"4." of "4. Unwinding object" (Human (Low), 1 word)', 'a heading\'s number'),
]


def apply(md, kinds=('ours', 'card'), only=None):
    """The guide with the edits of the given kinds (or only the edits named in ONLY); asserts each old text is in its block
    once."""
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == GUIDE_SHA, 'the guide changed since the fixes were written'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    bl = sr.blocks(md)
    assert len(raw) == len(bl)
    drop = set()
    for eid, i, kind, old, new, why in EDITS:
        if kind not in kinds or (only is not None and eid not in only):
            continue
        assert bl[i]['text'].count(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', old)) == 1, (eid, bl[i]['text'][:80])
        if new is None:
            assert bl[i]['text'] == old, eid
            drop.add(i)
            continue
        src = raw[i].replace('’', "'")
        o = old.replace('’', "'")
        if raw[i].count(old) == 1:
            raw[i] = raw[i].replace(old, new)
        elif src.count(o) == 1:
            k = src.index(o)
            raw[i] = raw[i][:k] + new + raw[i][k + len(o):]
        else:
            raise AssertionError('%s: the old text is not plain in the Markdown of block %d' % (eid, i))
    return '\n\n'.join(r for j, r in enumerate(raw) if j not in drop) + '\n'


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    for kinds in (('ours',), ('ours', 'card')):
        new = apply(md, kinds)
        print(kinds, hashlib.sha256(new.encode('utf-8')).hexdigest()[:12], len(sr.blocks(new)), 'blocks')
    for e in EDITS:
        print(e[0], e[2], '|', (e[4] or '(paragraph cut)')[:110])


if __name__ == '__main__':
    main()
