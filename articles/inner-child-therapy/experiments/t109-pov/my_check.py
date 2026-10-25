#!/usr/bin/env python3
"""Turn 109: my check of the 61 flags the eight point-of-view readers found (READER-1.md to READER-8.md, collected into
ITEMS.json by tools/humanization/clarity_read.py collect). Each reader saw an eighth of the article; each flag was checked
here against the whole article, the owner-edits record (whose words), his published guide (source/) and his answers.

A flag is offered to Joel when its cut passes the omission test, or when the point of view it lacks can be given from his
own words (in the article or in his answers), or when only he can give it. A flag is left, with the reason, when the line
is his own recent text or decision, when a cut would lose a claim, step or callback, or when the fix would break a
standing rule (no recipe for what to take). Nothing here changes the article: the article changes only on his decision.

  python3 my_check.py     writes CHECKED.json (ITEMS.json with my fields), puts the fields in ITEMS.json too, and prints
                          the counts; then clarity_read.py page . --out POV-READ.md lists them all"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

CUT = {
    '1.6': ("your published guide's line", "The section's heading, Don't Give the Inner Adult Away, already says it, and The Chicken-and-Egg Problem explains borrowing; without it the section ends on the joke that carries a request.", "Cut it."),
    '2.2': ("mine (turn 31), from the guide's gate", "The section says to wait three times before this ('clearly not the place to start', 'wait until you're calm and actually ready', 'before they bring their inner child anywhere near it'); without it, the paragraph ends on the question to ask.", "Cut it."),
    '2.3': ("not in your recorded texts", "The Buddha account and the Human Torch line already show what ill will does, and the question after it is the noticing. Round 6 read this sentence and the question as Human with Low confidence (w011 on the saved list).", "Cut it."),
    '2.7': ("mine or the guide's (not in your recorded texts)", "'A cheap trick for becoming the outsider to your own mess' already says what the trick gets you, and the Solomon's paradox sentence still follows from it.", "Cut it."),
    '3.1': ("mine (turn 9), in the paragraph you approved on 2026-10-01 (\"The P8 proposal was good.\")", "The paragraph opens with 'You can see the same move', so the scene already ties back to your bedtime story, and Mr. Rogers' own 'Thank you for that perspective' is the stronger last line.", "Cut it."),
    '3.8': ("not in your recorded texts; if it's your own wink, keep it", "Your 'Take a breath or three' already says to pause, and 'Maybe then you'll find' follows from the breath.", "Cut it, sentence and emoji, unless it's your joke."),
    '4.4': ("mine, from the guide's ending (turn 71)", "The heading and the line to your little one ('We're going back to the life we're building.') already say it; the section then ends on 'whatever you're still feeling can come along.'", "Cut it."),
    '6.3': ("mine (turn 87)", "'Most groups expect some conformity' already reads as normal, and the next sentence says when it becomes the bargain. 'Ordinary' is also one of the words the article rules mark as a model habit.", "Cut it."),
    '6.7': ("mine, after your tell cuts of 2026-10-22", "'People grow into who they are by trying things on and then changing their minds' already says it, and round 2 read this stretch as AI (Low 56).", "Cut it."),
    '7.5': ("mine (turn 65)", "'Maybe you're picturing them right now' already brings that person to mind, and the next paragraph says what they've been doing for you.", "Cut it."),
    '8.2': ("mine (turn 66), a quip", "'It can't be put on a schedule' says it, and it's the same kind of aside as '(nobody's taking attendance)', which you cut.", "Cut it."),
    '8.4': ("mine (turn 67), a quip", "'It doesn't matter whether they get any of it' says it; the same kind of aside as '(nobody's taking attendance)'.", "Cut it."),
    '8.8': ("mine (turn 65), from the guide's closing", "It explains the line before it. 'You are more than your pain and your past' stands on its own, and so does 'And you aren't alone.'", "Cut it."),
}
# 8.8's reader flagged the whole closing; the cut it proposes is this one sentence
NARROW = {'8.8': "That's easy to lose sight of when you've spent so long looking at them."}

POV = {
    '1.1': ("yours (your upload of 2026-10-19, word for word)",
            ["some people over-rely", "some people (like me) over-rely"],
            "As it stands it's 'some people', with nobody's case behind it. My Journey has your own: 'most people (like me) who chase spiritual freedom, as valid as that is, are, at least at first, trying to get away from something painful in themselves'. Reading that as this sentence's case is my inference, so it's yours to say.",
            "Add '(like me)', if it's you.", "Is it you, the way My Journey says?"),
    '1.4': ("mine (turn 72), from the guide's line", ["I'd keep whatever you feel around them", "Keep whatever you feel around them"],
            "It answers 'How do you check that?', so it's a step, and in your When to Change the Strategy you said a step plainly ('Before going with either of those paths, look for what exactly is in the way'); the questions after it carry the reasons.",
            "Say it plainly.", ""),
    '1.5': ("mine", ["I'd take a few days", "Take a few days"],
            "A step for someone who might be love-bombed, like the one above. If you'd rather tie it to you, My Journey's 'I kind of just assume I can trust everyone, and that gets me into trouble' is the reason, and your note can say so.",
            "Say it plainly.", ""),
    '3.2': ("mine (turn 12)", ["I'd ask these:", "ask these:"],
            "It hands over the six questions, and the two paragraphs before it give the reason.", "Say it plainly.", ""),
    '3.3': ("yours (2026-10-02)",
            ["with your own inner child.", "with your own inner child. My son did that for me, and I think that's very common for parents."],
            "Your answer of 2026-10-02 has the case this sentence needs: \"I actually used my son (i shouldn't say \"used\") to reconnect with my inner child, and I think that's very common for parents.\" The new sentence is that answer in article form, without \"used\".",
            "Add your line.", ""),
    '4.2': ("not in your recorded texts",
            ["I'd leave out forgiving them and picturing their childhood.", "I'd leave out forgiving them and picturing their childhood here; that has its own section, How to Forgive Without Forgetting."],
            "The reader isn't told why. The forgiveness section says it can't be put on a schedule and that pressure gets you an act, so pointing there gives the reason without saying it twice. Your own reason, if it's a different one, would be better.",
            "Point to the forgiveness section.", "Why do you leave it out here?"),
    '4.8': ("mine, from your queue item PGQ-004 (2026-10-07)",
            ["even when it sounds like a prediction.", "even when it sounds like a prediction. As What to Make of a Passing Feeling says, if you don't want to be touched, say no now and work out what it means later."],
            "The anxiety paragraph just before it says 'I'd go see', so the reader needs to know why a no about touch, sex or going deeper is different. Your own line in What to Make of a Passing Feeling is the reason.",
            "Point to your line.", ""),
    '5.1': ("mine", ["I'd still keep it the same.", "I'd still keep it the same, since a harder voice just starts the argument again."],
            "The reason is your line one paragraph up: 'It puts you into the role of the Nurturer, which alleviates the instinct to argue back.'",
            "Tie it to your line above.", ""),
    '5.4': ("yours (your upload of 2026-10-19, word for word)",
            ["Some people benefit more from solo therapy, while others benefit more from having a trained therapist guide the experience.",
             "If you haven't built much Nurturer and Protector yet, a trained therapist guiding the experience can lend you some; with more of your own, solo therapy can work."],
            "As it stands it's 'some people ... others', and the reader can't tell which they are. The sentence before it measures medicines by how much Nurturer and Protector you need, so this says who needs a guide in those terms. It's my reading of your point, so it's yours to say.",
            "Say who needs a guide.", "Is that who you'd tell to have a guide?"),
    '5.5': ("yours (turn 77)",
            ["or at least know that they are a double-edged sword.", "or at least know that they are a double-edged sword, and can start that cycle of taking more and more medicine."],
            "'Double-edged' names no edge. The paragraph above names one: 'which often leads into a cycle of taking more and more medicine over time.'",
            "Name the edge you already named.", ""),
}

ASK = {
    '2.4': ("the guide's line (it's in your published guide), as I humanized it",
            "Whose experience is 'what people most often say helped'? If it's yours (the watching meditator, a few paragraphs up), I'd say so in a clause; if it's what people have told you, who were they?",
            "Your words, in the note. Until then it stays as it is."),
    '5.8': ("your published guide's 'Many people find', as I humanized it",
            "What does the mantra do for you? Your 'I personally love this beautiful Om Mane Pemme Hum mantra' is right after it; one line of what it does would replace 'a lot of people find'.",
            "Your words, in the note. Until then it stays as it is."),
    '7.4': ("the guide's line (it's in your published guide), as I humanized it",
            "Has grief turned into warmth, or a held feeling, for you? One moment of yours would replace 'some people find'.",
            "Your words, in the note. Until then it stays as it is."),
}

LEFT = {
    '1.2': "It adds the other half of the goal: silly, and more self-aware at the same time.",
    '1.3': "Your own preference is the subject here (My Journey is your story), and the next paragraph says what it bought you.",
    '1.7': "Your own rewrite (2026-10-22, \"dark green for the whole section\"), and advice a reader needs: what to do when stopping.",
    '2.1': "Your own opener, from your rewrite of 2026-10-24.",
    '2.5': "Your own words (your opening of 2026-10-17), and it carries the car crash over to your sister's line.",
    '2.6': "You kept it on 2026-10-24 (the cut list's h9: \"b\").",
    '2.8': "Your own invitation to readers, and a real want of yours.",
    '3.4': "Your own sentence (2026-10-19), and the next sentence is its concrete case.",
    '3.5': "'Sovereign' calls back to the sovereignty line in When the Present-Day Adult Is Dangerous to the Child.",
    '3.6': "The lifelong-growth point of your correction of 2026-10-14, which keeps 'reduced need for the therapy' from reading as a finish line.",
    '3.7': "The next paragraph says what going at it harder turns into (a ritual you have to finish before you're allowed to live), and 'Take the parts that work, and innovate on the rest' invites the reader to adapt the guide.",
    '4.1': "Your own line, which you asked to have put back (2026-10-17).",
    '4.3': "Your own section (2026-10-18), and the line closes the night's review with the rest it's for.",
    '4.5': "Your own sentence, and its claim is your point of view.",
    '4.6': "The next sentence is its reason (how parts treat each other matters more than what they're called), and your new IFS paragraph gives another.",
    '4.7': "Your own line. In the new shape it opens the paragraph for when nothing comes, beside your 'Or if you do get an answer'.",
    '5.2': "Your own sentence (your rewrite of 2026-10-24, 'it makes sense to work on that blocker').",
    '5.3': "Your own section (2026-10-24).",
    '5.6': "Naming the healthiest medicines here would be a recipe for what to take, which stays out of the article.",
    '5.7': "Your own proverb, in your own story's paragraph.",
    '6.1': "Your own text (2026-10-19), and advice a reader in daily pain needs.",
    '6.2': "It follows from 'with no outside input' just before it.",
    '6.4': "A judgment with its reason in the same sentence: look at what they do before deciding it's envy.",
    '6.5': "The paragraph's one step, and 'see what actually happens' is the test the section sets up. If you have your own first small good thing, it could replace the meal.",
    '6.6': "Your own paragraph (2026-10-23, \"i fixed it, passes\"); it says the telling comes with practice.",
    '7.1': "Your own words (2026-10-23). One place or practice of your own could go here, if you have one.",
    '7.2': "Your own paragraph (2026-10-17), the march break you added.",
    '7.3': "Your own text (2026-10-17).",
    '7.6': "Your own P2 (2026-10-17), word for word.",
    '7.7': "It makes its own point, the tone after the words, which a cut would lose.",
    '8.1': "The paragraph's claim, with the guide's catch-all; trimming the list would be style, and the next paragraph says the love reaches other people.",
    '8.3': "The section's how-to, and 'the responsibility stays' right after it is the point of view.",
    '8.5': "Your own opener (2026-10-19).",
    '8.6': "Your own 'I'd', your judgment of what you'd want in a therapist.",
    '8.7': "Your own line (2026-10-19).",
}


def main():
    items = json.loads((HERE / 'ITEMS.json').read_text(encoding='utf-8'))
    keys = {x['key'] for x in items}
    mine = set(CUT) | set(POV) | set(ASK) | set(LEFT)
    assert keys == mine, ('unchecked: %s; unknown: %s' % (sorted(keys - mine), sorted(mine - keys)))
    assert not (set(CUT) & set(POV) or set(CUT) & set(ASK) or set(POV) & set(ASK) or (set(CUT) | set(POV) | set(ASK)) & set(LEFT))
    out = []
    for x in items:
        k = x['key']
        y = dict(x)
        if k in CUT:
            whose, note, pick = CUT[k]
            y.update(status='keep', group='cut', label='CUT', whose=whose, note=note, my_pick=pick)
            if k in NARROW:
                assert NARROW[k] in x['quote']
                y['quote'] = NARROW[k]
        elif k in POV:
            whose, edit, note, pick, q = POV[k]
            y.update(status='keep', group='pov', label='POV', whose=whose, edit=edit, note=note, my_pick=pick, question=q)
        elif k in ASK:
            whose, q, pick = ASK[k]
            y.update(status='keep', group='ask', label='POV', whose=whose, question=q, my_pick=pick, note='')
        else:
            y.update(status='drop', group='left', note=LEFT[k])
        out.append(y)
    (HERE / 'CHECKED.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    # the same fields in ITEMS.json, so that clarity_read.py page lists my check with the readers' notes (POV-READ.md)
    keep = ('status', 'note', 'my_pick', 'whose', 'question', 'label', 'quote')
    for x, y in zip(items, out):
        for k in keep:
            if k in y:
                x[k] = y[k]
        if y.get('edit'):
            x['my_pick'] = '%s (%s -> %s)' % (y['my_pick'], y['edit'][0], y['edit'][1])
    (HERE / 'ITEMS.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    from collections import Counter
    print(Counter(y['group'] for y in out))


if __name__ == '__main__':
    main()
