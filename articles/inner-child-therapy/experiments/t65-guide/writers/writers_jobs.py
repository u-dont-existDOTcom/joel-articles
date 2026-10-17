"""Round z (turn 65): prompts for fresh writer agents, one per job, from reviewer/writer_draft.txt (E177: fresh
writers when my own drafts keep failing). Each brief is the guide passage's points as my best faithful draft and its
grounding carry them, with the grounding's MUST fixes; life facts from the guide's first person stay out (E159)."""
import json
import pathlib
import sys

REPO = pathlib.Path('/home/claude/joel-articles')
sys.path.insert(0, str(REPO / 'tools/humanization/reviewer'))
import reviewer  # noqa: E402

G = REPO / 'articles/inner-child-therapy/experiments/t65-guide'
OUT = G / 'writers'
txt = lambda n: (G / (n + '.txt')).read_text(encoding='utf-8').strip()
opens = lambda prev, heading: prev + '\n\n(Then the heading "' + heading + '" opens the section your text begins.)'

JOBS = {
 'sp4': dict(n=2, length='two paragraphs, 50 to 90 words each, blank line between them',
   before=opens(txt('sp3-p2-d2'), '## Journal With Each Hand'),
   after="## \"And So That's the Way It Happened!\" (the next practice)",
   brief='''Paragraph 1:
- what it's for: when talking to your little one, or picturing them, only gets you silence.
- the method: write the scared or hurting thoughts and feelings with your other hand, the one you don't write with (the clumsy one; its writing already looks like a child's, which is why it's your little one's hand), and answer with your usual writing hand, as the grown-up offering love, protection and guidance.
- MUST (a reader's question the review found unanswered, "If my little one stays silent, do I make up what they'd say?"): write only what's really there, what you actually feel; nothing invented.
- if the protective part shows up first, it gets the non-dominant hand first, until it's had its say.
Paragraph 2 (a queued guide change: memory support isn't the same as reflective journaling):
- if reflective journaling makes things more confusing, a simpler memory aid is fine: a short dated note of what happened, a note of what helped, a reminder, a next step, or a voice note.
- it keeps track of things without having to interpret them at the same time; looking for patterns can come later, if it's useful at all.
- a memory aid doesn't have to explain your life.'''),
 'sp5': dict(n=1, length='one paragraph, 60 to 95 words',
   before=txt('sp5-p1-e2'),
   after='## One Intention in the Morning, One Review at Night (the next practice)',
   brief='''This is the second paragraph of the practice; the first (above) gives the line and says to start with a memory you can handle.
- telling it as a story doesn't turn the memory into fiction, and it doesn't prove every detail is right.
- MUST: it ends the trial, not the accountability or the repair. If you're the one who did the harm, any repair that's owed is still owed; if someone hurt you, it doesn't say what they did was okay.
- the stop signs: if the narrator's voice turns sneering, if the shame gets bigger, or if you start to feel unreal, stop, instead of telling it from even further away (more distance won't help with those).
- if the line helps, keep it to the line; then you can ask what the younger you in that story needs from you now.'''),
 'sp6': dict(n=2, length='two paragraphs, 45 to 85 words each, blank line between them',
   before=opens(txt('sp5-p1-e2'), '## One Intention in the Morning, One Review at Night'),
   after='## Just Like Me (the next practice)',
   brief='''- in the morning, choose one modest intention: "Today I will notice one hook before I act from it" (any one hook, whichever shows up).
- at night, review the day without putting yourself on trial: where did you notice the hook? where did it run its whole sequence anyway? what small repair or protective act comes next? what moment of warmth, pleasure, courage or connection did you actually get?
- count noticing as progress, even when you only noticed afterward, in the review; if you interrupted the pattern somewhere, notice that too.
- repair what can be repaired, renew the intention, and go to sleep.
(The review questions can be asked as questions, but not as a run of three or more questions in a row; the author's linter flags that.)'''),
 'sp7': dict(n=1, length='one paragraph, 50 to 85 words',
   before=txt('sp7-p1-c'),
   after='## Use Childhood Photographs Without Interrogating Them (the next practice)',
   brief='''This is the second paragraph of the practice; the first (above) gives the wish, with yourself first.
- you breathe however you normally breathe (nothing special), and after yourself the wish takes in anyone else who comes to mind.
- it isn't asking you to forgive someone who hurt you, or to imagine their childhood.
- MUST: the wish asks for no contact with anyone. Whether you ever contact them is a separate decision, and never one to make while you're flooded.
- what it's for: you stop carrying a feeling this many people share as proof that you alone are defective.'''),
 'sp8p1': dict(n=1, length='one paragraph, 45 to 75 words',
   before=opens(txt('sp7-p1-c'), '## Use Childhood Photographs Without Interrogating Them'),
   after=txt('sp8-p2-c'),
   brief='''This opens the practice; the next paragraph (below) says what to notice while you look.
- if picturing your little one feels fake, like you're making it up, a real photo of you as a child can help: there's no face or posture to invent.
- look at it gently and notice what comes up, without deciding ahead of time what the picture is supposed to prove.'''),
 'sp8p4b': dict(n=1, length='one paragraph, 45 to 80 words',
   before=txt('sp8-p4a'), after=txt('sp8-p5-d'),
   brief='''- if a serious allegation starts to take shape (for example, the idea that someone abused you), don't confront or accuse anyone based only on what came up here.
- write down exactly what came up and how it came up.
- get grounded support from someone who won't lead you toward an answer.'''),
 'sp9': dict(n=1, length='one paragraph, 70 to 110 words',
   before=txt('sp8-p5-d'), after='# When Love Still Feels Missing (the next section)',
   brief='''The heading is "## Close the Session and Return to Life"; this is its only paragraph.
- give every session with your little one a definite ending.
- look around and name where you are; feel your feet, the chair, or another point of contact; relax your jaw and hands.
- name one ordinary thing you'll do next, and say something like "That's enough for today. We're returning to the life we're building."
- the session doesn't have to resolve every feeling before you make food, answer a message, take a walk or go to sleep; going back to your life is part of the healing, too.'''),
 'lm1': dict(n=3, length='three paragraphs, 50 to 95 words each, blank line between them',
   before=opens(txt('sp9-k2'), '# When Love Still Feels Missing'),
   after='## Notice the Part That Came Here (the next part)',
   brief='''Paragraph 1:
- if you weren't loved well as a child, "love your inner child" can sound like nonsense.
- you can sincerely want the best for your little one, hug them in your imagination or miss them, and still feel none of the warmth people mean by love; that doesn't close the door; it means starting smaller.
Paragraph 2:
- if even an imagined caring grown-up makes you feel more threatened, or lonelier, go smaller still: the least cruel response a decent adult could offer.
- it's scaffolding, not a test of whether you were loved enough.
Paragraph 3:
- taking the hostility out makes room for warmth.
- what people most often say helped is letting their defenses down. MUST: by choice, once the guarding part has been heard (not pushing past it).
- for someone who has never been safe being loved, the ego can act like a rigid security guard that won't let the feeling in, and vulnerability is the opening the feeling needs. MUST: this guard is about letting the feeling in, not about trusting people (people still earn trust).
- sometimes the warmth isn't absent: a cold part is standing in front of it, guarding something, and it tends to step aside once it's been heard (the article's section Hear the Protective Part First).'''),
 'lm2': dict(n=2, length='two paragraphs, 45 to 85 words each, blank line between them',
   before=opens(txt('lm1-p3-d'), '## Notice the Part That Came Here'),
   after='## Somatic Heart Opening (the next part)',
   brief='''Paragraph 1:
- some people hear all this about love and answer, "No. I hate myself."
- if that's what you find, it deserves an honest hearing, not an argument.
- but if you opened this article, came to therapy, asked someone for help, or tried again after deciding you were hopeless, something in you wanted things to be different.
Paragraph 2:
- what was it: hope, desperation, curiosity, fear, duty, refusing to keep suffering like this, maybe love; you don't need to decide which.
- ask that part what it hoped might happen when it brought you here, and follow that thread.'''),
 'lm3': dict(n=1, length='one paragraph, 70 to 110 words',
   before=opens(txt('lm2-p2-c'), '## Somatic Heart Opening'),
   after='## How Much Happiness Do You Know Is Possible? (the next part)',
   brief='''- Rumi says you have to keep breaking your heart until it stays open (the guide's words).
- some people find that deep grieving gives way to warmth, connection, or a feeling in the body of being held; that describes an experience, not proof of how the body produces it.
- love can open grief from the other side: being cared for can bring up sadness for the care that was missing, and that doesn't mean the love failed.
- MUST: stay with it while you're present and can still choose, and slow down when it's swamping you instead of opening you.'''),
 'lm4': dict(n=2, length='two paragraphs, 40 to 85 words each, blank line between them',
   before=txt('lm4-p2-a2'), after=txt('lm4-p5-c'),
   brief='''The section so far: love includes wanting someone to be well, and the happiness you know is possible shapes that wish; a big spiritual experience can enlarge it. The paragraph after yours says curiosity can be enough.
Paragraph 1:
- if you're curious about that bigger happiness, follow the curiosity instead of pretending to believe something.
- read people from different traditions, meet people whose lives make you wonder, and judge a path by its fruits.
Paragraph 2:
- sometimes care isn't what's missing: the whole horizon of life feels too small, and a meal, a boundary or a kind sentence can help without touching the question underneath, "Why should I want this life at all?"
- take that question seriously: what would have to be possible for being alive to feel worth discovering, not just enduring?'''),
 'ks12': dict(n=2, length='two paragraphs, 55 to 95 words each, blank line between them',
   before=opens(txt('lm4-p5-c'), '# If You Want to Kill Yourself'),
   after=txt('ks1-p3-a'),
   brief='''This section is for a reader who wants to die. Safety comes first and plainly.
Paragraph 1:
- if you're about to act, can't stop yourself, are badly disoriented or intoxicated, or have the means in front of you: first get another human being involved, and put distance between yourself and the means.
- MUST: a crisis line or an emergency number counts as another human being.
- MUST: if you can't tell whether you're about to act, treat it as if you are.
- that isn't the answer to whether life is worth living; it keeps the question open long enough to look into it.
Paragraph 2:
- before getting philosophical, make sure there's an adult in the room: if the part that wants to die feels like all of you, use the noticing from the article's section Noticing Counts (whoever is noticing is already more than the part that wants to die) or borrow an adult, as in Borrow the Adult Before You Can Be the Adult, and invite any part that can watch what's happening, protect the body, or put off a decision that can't be undone.
- if you can already watch the suicidal state without being completely caught up in it, skip this step.
- MUST: if no part of you can watch yet, the questions wait, and the person from the first step is the adult for now.'''),
 'ks4b': dict(n=1, length='one paragraph, 45 to 80 words',
   before=txt('ks1-p4-c'), after=txt('ks1-p5-b'),
   brief='''It follows the Buddhist view (above), which you don't have to believe.
- but if you're about to bet your life on the opposite claim (that death is simply nothing), look into it first.
- near-death experiences and seriously studied rebirth reports can't give reliable odds about what happens after death, but they can challenge the certainty that destroying the body guarantees nothingness.'''),
 'sh1': dict(n=1, length='one paragraph, 70 to 110 words',
   before=opens(txt('ks1-p6-d'), '# When the Practice Feels Real but Stays Shallow'),
   after='# How to Forgive Without Forgetting (the next section)',
   brief='''- some people have the opposite problem: it feels like they're connecting, but the contact is staying near the surface.
- meditating for a long time and then sleeping (especially a second sleep, after you've already slept once) can open up much more emotionally direct material.
- MUST: the sign of this case is the gap: if that night's dream carries far more feeling and need than the daytime session came anywhere near, the difference is information about the session (a good session that simply didn't carry into the day isn't this).
- ask what became available, and how you see it now.
- if repeated nightmares start wrecking your sleep, change the dose (earlier in the day, or shorter) before giving up on the whole thing.'''),
 'fg1': dict(n=4, length='four paragraphs, 55 to 95 words each, blank line between them',
   before=opens(txt('sh1-c'), '# How to Forgive Without Forgetting'),
   after="# When One Life Has Ended and the Next Hasn't Begun (the next section)",
   brief='''Paragraph 1:
- for many people, healing eventually includes some forgiveness, or at least getting out from under active resentment; it can't be put on a schedule, and you don't need it first in order to be safe, hold someone accountable, set boundaries, get justice or recover.
- active resentment can narrow what you see and keep your little one organized around the injury; pressure to forgive early produces an enlightened-looking performance while the wound goes underground.
Paragraph 2:
- what can help is seeing how a person's conditioning, history, pain and capacity shaped the harmful thing they did: given everything they had become by that moment, it was the only move they had available. Hurt people often pass on pain they never processed.
- when that becomes something you actually see, not a moral instruction, forgiveness may arise by itself, and the rage that held them uniquely to blame can soften into something more accurate.
(The guide says "the understanding that helps me": that's the guide's first person, not the author's own words, so don't write it as something the author does.)
Paragraph 3:
- that doesn't make what they did harmless, or mean no other option existed in theory; it means punishment can't go back and create the awareness, support or capacity they didn't have enough of. The useful work is repairing what can be repaired and making a different response more available now.
- accountability stays and the harm is real: boundaries, legal consequences, moral judgment, distance and permanent no-contact can all still be right. You can understand them, hold them responsible, never speak to them again, and forgive them. "I understand how you became this way" can sit beside "I now understand why I shouldn't rely on you for this."
Paragraph 4:
- forgiving yourself works the same way, and when it's hard, forgiving other people tends to be harder too.
- MUST: own what you did (and only what was yours), let the remorse register, repair what you can (apologize, make amends, change the behavior), and then you're allowed to stop holding yourself hostage; the responsibility stays.
- some harms take years: forgiving too soon is one trap, and living permanently inside resentment is the other. Don't push it; come back over time to the question of how they became capable of it, until the understanding is real enough to change how you feel.'''),
 'le1': dict(n=2, length='two paragraphs, 55 to 100 words each, blank line between them',
   before=txt('le1-p1-c'),
   after='# Borrowed Adulthood in Relationship (the next section)',
   brief='''The section's first paragraph (above) is done: the gap between one life and the next, and the bardo.
Paragraph 1:
- questions for the gap: what has actually ended? what are you still trying to keep going? what isn't known yet? what is your little one afraid will happen in the gap? what practical act or small ritual would mark the ending without pretending you know the next beginning? (The author's linter flags three or more questions in a row, so not all of them as a run of questions.)
- don't force a new identity because the uncertainty feels unbearable; the grown-up you can keep routines, protect the body, grieve what ended, and stay with your little one while the next life takes shape.
Paragraph 2:
- missing someone doesn't have to become another problem to solve; sometimes the ache itself can become a cue for love. Don't push the missing away.
- if love is there, let "I miss you" become "I love you," or offer a simple wish: "May you be safe. May you be held in love." Picture them, or just feel the direction of the care.
- it's about what happens in you: it doesn't require believing they receive anything, and it doesn't replace grief, contact, boundaries or practical action.
- if sending love makes you more compulsive or unreal, or you can't get back to your life, make it simpler: "I miss you, and I care." You can also offer some of the same care to the part of you that's still here.'''),
 'ba1': dict(n=2, length='two paragraphs, 55 to 95 words each, blank line between them',
   before=opens(txt('le1-p3-d'), '# Borrowed Adulthood in Relationship'),
   after='# Speak Toward What You Are Building (the next section)',
   brief='''Paragraph 1:
- reparenting is usually framed as something you do alone or with a therapist, but your little one was hurt in relationships, and a relational injury can only heal so far in isolation.
- sometimes one person ends up carrying a lot of the borrowed-grown-up jobs at once: food, planning, health decisions, rides, social life, reassurance, protection, company, or just the sense that somebody competent is beside you. Having someone who can care for you when you're struggling can be an enormous blessing.
Paragraph 2:
- over time, reparenting can help you take in and practice some of what that person has modeled for you, while other jobs can be shared with friends, community, professionals or services, routines and ordinary tools.
- three questions: which of these can become more yours? which are healthiest shared? which really belong inside that relationship?
- the aim is for your little one to feel reliable care through more than one way, while the relationship itself stays precious and important.'''),
 'st1a': dict(n=3, length='three paragraphs, 50 to 95 words each, blank line between them',
   before=opens(txt('ba1-p2-d'), '# Speak Toward What You Are Building'),
   after='(The section goes on to what a good peer can lend you, and to community.)',
   brief='''Paragraph 1:
- the words you use in this work direct attention: when a painful or negative frame isn't itself what needs naming, prefer words that point toward the capacity, relationship or action you want to strengthen.
- the guide's example: "Let's help you build more ways to feel cared for and supported" usually gives the mind a clearer direction than bringing in a label like "dependency" just to deny it or argue with it.
- in inner-child work and hypnosis especially, make the direction easy to imagine: warmth, protection, steadiness, rest, or whatever is actually needed.
Paragraph 2:
- this isn't forced positivity: grief is grief, and danger should be called danger; harm, anger, limits, accountability, consent and practical constraints still need accurate words.
- once reality has been named, spend most of the energy on what can be protected, practiced, repaired, chosen or grown, not on an unneeded picture of what the person shouldn't become.
Paragraph 3:
- before giving advice (to someone else, or to your little one), it can help to find out what kind of company they want: "Do you want me to mostly listen, help you untangle this, give you ideas, or some mix?"
- it isn't a ritual to ask every time: when it's obvious which they want, follow that; when it isn't, one sentence can keep advice from arriving where somebody needed to be heard, or plain listening where they were asking for help thinking.'''),
 'st1b': dict(n=3, length='three paragraphs, 50 to 95 words each, blank line between them',
   before="(The section so far: words that point toward what you're building, not forced positivity, and asking what kind of company someone wants before giving advice.)",
   after='# You Are Worthy of Love. Always. (the closing section)',
   brief='''Paragraph 1:
- the three grown-up jobs translate outward: a good peer (someone you take turns listening to, as equals) can lend you the Nurturer through presence and warmth, and the Protector through confidentiality, time boundaries and respect for "no".
- the peer doesn't supply your Guide or decide what your experience means; a carefully timed question can help your own Guide get heard, without interpretation, advice or authority over the answer; then the roles switch.
(The guide names its own peer-counseling framework here and calls it "my" framework: leave the name and the "my" out; that's for the author to add.)
Paragraph 2:
- this can be borrowed adulthood at its healthiest: the peer doesn't become your permanent parent; they show you a capacity, help you take part in it, and hand it back to you.
- therapy stays useful for what therapy does; community and disciplined peer support do something different, and a serious healing path can include both.
Paragraph 3:
- community can work in both directions: sometimes loving people give someone enough safety and belonging for a deeper opening to become possible; other times the opening comes first, and it changes what kinds of people and relationships they can "manifest"; then community helps make the opening practical, real and embodied.
- love moves from spiritual experience to your little one, from your little one into the grown-up relationship, from you into other people, and back again; the loop matters more than which door you came in through.'''),
 'wl1': dict(n=1, length='one paragraph, 50 to 80 words',
   before="(The section before: community and peers, and love moving in a loop from spiritual experience to your little one, to you, to other people, and back.)\n\n(Then the heading \"# You Are Worthy of Love. Always.\" opens the article's closing section, which your paragraph is.)",
   after='(the Appendix)',
   brief='''The article's last paragraph before its appendix. Almost everything the guide says here is already in the article (start with small acts of care; the role can start outside you; love can go before trust; your little one is still in there and finally has somebody reliable), so don't say those again.
- be patient with yourself, and gentle.
- you are more than your pain and your past.
- you aren't alone, and help exists.'''),
}


def prompt(job):
    w = reviewer.read('writer_draft.txt')
    w = w.replace('{brief}', job['brief']).replace('{before}', job['before']).replace('{after}', job['after'])
    if job['n'] > 1:
        w = w.replace("You're writing one short paragraph", "You're writing %d short paragraphs" % job['n'])
        w = w.replace('It goes between two paragraphs of his (below)', 'They go between two pieces of his (below)')
    i = w.index('Write the paragraph:')
    j = w.index('\n', i)
    what = 'the paragraph' if job['n'] == 1 else 'the %d paragraphs' % job['n']
    last = ('Write %s: %s, in the second person like the paragraphs around it. No heading. Output only %s.'
            % (what, job['length'], what))
    return w[:i] + reviewer.joel_fixes() + '\n\n' + last + w[j:]


if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    for k, job in JOBS.items():
        p = OUT / (k + '.prompt.txt')
        p.write_text(prompt(job), encoding='utf-8')
        print(k, len(p.read_text().split()), 'words')
