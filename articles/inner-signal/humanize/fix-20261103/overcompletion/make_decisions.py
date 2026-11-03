"""The lead session's judgment of each overcompletion candidate (CANDIDATES.json), written to DECISIONS.json for apply_cuts.py.

Each candidate was read in place, with the paragraphs before it and its section (E328). The rule:
- "cut": a second explanation that loses nothing, in our words or in his published guide's words (his 2 November card
  W-685: "let's see what other redundancy remains in this article and cut that also"); his published words are marked so
  he can see them in CUTS.md and on the questions page.
- "ask": his own words (a paragraph he wrote or rewrote, or his inner child guide's): a question for him, never cut here.
- "keep": not a second explanation (it adds a claim, a case, a source, an instruction where it's needed, or his voice), with
  the reason.
A "join" the reader gave is used only after checking that it is the block with the cut taken out, plus only the words the
reason names.

  python3 articles/inner-signal/humanize/fix-20261103/overcompletion/make_decisions.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# id: (decision, why); the joins are the readers' unless JOINS below replaces one
D = {
    # part 1
    'P1-01': ('cut', 'a second gloss on "the guard mind" right after "childhood protector parts"'),
    'P1-02': ('cut', 'sums the paragraph up: its options already say any way is fine'),
    'P1-03': ('keep', 'a lead-in the next sentence fills in, not a second explanation; his published words'),
    'P1-04': ('keep', 'a second source is evidence, not a second explanation, and it is his published OECD citation'),
    'P1-05': ('cut', 'names the benefit the sentence before it already gives (training your own mind from the inside)'),
    'P1-06': ('cut', 'the sentence before it from the other side (with the correction / without it); his published sentence'),
    'P1-07': ('cut', 'the paragraph before it from the other side (a hypnotist can\'t get quick feedback / I can); the next sentence names the dialogue instead of "that"'),
    'P1-08': ('cut', 'the caveat before it said again as advice'),
    'P1-09': ('cut', 'the reason for "if it doesn\'t work for you, don\'t use it!", which the maps line earlier already gave'),
    'P1-10': ('cut', 'the two sentences before it already say you need to work on them'),
    'P1-11': ('cut', 'a "So…" that sums up the vantage-point picture and its warning'),
    'P1-12': ('cut', 'the paragraph\'s first sentence said again at its end'),
    'P1-13': ('cut', 'the sentence before it, said again'),
    'P1-14': ('keep', 'his inner child guide\'s words; it voices what the line says underneath, which is his move, not a second explanation'),
    'P1-15': ('cut', 'the same listening without hitting back, said earlier in the paragraph'),
    'P1-16': ('cut', 'one position doing both, asked again'),
    # part 4
    'P4-01': ('cut', 'the next sentence says it from the other side (you don\'t need to try all of them)'),
    'P4-02': ('keep', 'the section\'s instruction in its own words, which the request scripts after it carry out (ask, not bully); his published words'),
    'P4-03': ('keep', 'a list of areas a reader may recognize, not an explanation said twice; his published list'),
    'P4-04': ('cut', 'a "So…" conclusion of the two sentences before it; the line to get help stays'),
    'P4-05': ('cut', 'the first sentence\'s instruction said again as a picture'),
    'P4-06': ('cut', 'the same instruction said a third time'),
    'P4-07': ('keep', 'the stop rule for this case, where a reader in it reads it; not a second explanation in this section'),
    'P4-08': ('cut', 'the clause before it from the other side (love your thinking accepts / thinking that keeps love real), as in the pairs of minds he cut'),
    # part 6
    'P6-01': ('cut', 'the first half of the sentence said again as a rule of scale'),
    'P6-02': ('cut', 'the sentence before it said again as a rule of scale'),
    'P6-03': ('cut', 'the two sentences before it summed up, with their other side'),
    'P6-04': ('cut', 'the paragraph already says attention without interpretation and that peers aren\'t each other\'s Guide'),
    'P6-05': ('ask', 'his own paragraph\'s last line sums up the two sentences before it'),
    'P6-06': ('cut', '"In other words": the paragraph before it from the other side, and The General Rule says it again'),
    'P6-07': ('keep', 'a question that opens the section, not an explanation'),
    'P6-08': ('cut', 'said three times before it (it doesn\'t matter if they\'re demons; don\'t try to figure out what it is; the heading)'),
    'P6-09': ('cut', 'the section\'s recap: the heading and the paragraphs before it say it'),
    'P6-10': ('cut', 'two more cases after the point is made (fear gives it attention, hate a hook)'),
    'P6-11': ('cut', 'the paragraph before it and the heading say it (compassion present, door closed)'),
    'P6-12': ('cut', 'sums up his script before it and The General Rule; his published paragraph'),
    'P6-13': ('keep', 'his voice asking, not an explanation'),
    # part 2
    'P2a-01': ('keep', 'his own version of the paragraph, sent with his answers of 3 November, kept this line; "like a real conversation" is his picture'),
    'P2a-02': ('cut', '"Just sit back and enjoy their company", said again'),
    'P2a-03': ('cut', 'sums the paragraph up (enjoy them, not only make their feelings go away)'),
    'P2a-04': ('cut', 'the sentence before it from the other side (it fails when those things are skipped / works when they aren\'t)'),
    'P2a-05': ('keep', 'a list of what a guard may want, in its own section; a list, not an explanation said twice'),
    'P2a-06': ('cut', 'with P2a-07, the whole paragraph: it sums up the list before it (assess, ask, delay, stop scanning); from his published version, reworded'),
    'P2a-07': ('cut', 'with P2a-06, the whole paragraph (see P2a-06)'),
    'P2a-08': ('cut', '"a lot of connection", said again'),
    'P2a-09': ('cut', '"any vulnerable part of you", said again'),
    'P2a-10': ('cut', 'the step before it from the other side (do the smallest thing / don\'t fix it all)'),
    'P2a-11': ('cut', '"Give yourself some time", said again'),
    'P2a-12': ('cut', '"Reconnect with them", said again; "if they\'re willing" moves up'),
    'P2b-01': ('cut', 'a paragraph that only says its heading again'),
    'P2b-02': ('cut', 'the list\'s first sign is the paragraph before the list, said again'),
    'P2b-03': ('keep', 'adds why (attention went into avoiding pain and keeping the bond), which the first paragraph doesn\'t say; his published content'),
    'P2b-04': ('cut', 'a "That is why" ending to the point the sentence before it makes'),
    'P2b-05': ('cut', '"not directly telling the subject what to do", explained again'),
    'P2b-06': ('keep', 'a list of examples in his own "etc etc etc", not an explanation said twice'),
    # part 3
    'P3a-01': ('keep', 'his own words, in his voice; too small to ask about'),
    'P3a-02': ('keep', 'his own joke opening the section'),
    'P3a-03': ('keep', 'his own words; "soft, but to the point, easy to remember" adds what the script should be'),
    'P3a-04': ('cut', '"Read through the induction ... when you\'re awake", said again'),
    'P3a-05': ('cut', 'the no and silence rules said again; the paragraph before it already says you can say stop at any time'),
    'P3a-06': ('cut', '"Pick a place", said again'),
    'P3a-07': ('cut', 'sums the paragraph up'),
    'P3a-08': ('keep', 'his aside about his dad\'s driving, a joke in his voice, not an explanation'),
    'P3a-09': ('cut', '"Keeping it doesn\'t keep today\'s trance going", said again'),
    'P3b-01': ('keep', 'opens the section: what the induction is for and what comes after it, not a second explanation; his published content'),
    'P3b-02': ('cut', 'the first sentence said again; the example joins it with "For example"'),
    'P3b-03': ('cut', 'sums the paragraph up'),
    'P3b-04': ('cut', '"stop what you\'re doing and change it", said again'),
    'P3b-05': ('cut', 'sums the paragraph up'),
    'P3b-06': ('cut', '"or just imagine doing what you feel you need to do", from the other side'),
    'P3b-07': ('cut', 'the next sentence from the other side (welcome / don\'t have to get rid of them)'),
    'P3b-08': ('cut', 'the sentence before it from the other side'),
    'P3b-09': ('cut', 'sums the paragraph up ("That doesn\'t mean your love isn\'t working", "change it to something that is less")'),
    'P3b-10': ('cut', 'said in "Remember that whatever you find out is likely to be metaphorical" before it; the next sentence starts without its "And"'),
    'P3b-11': ('keep', 'adds a body release to the images'),
    # part 5
    'P5a-01': ('cut', 'the moves the paragraph before the example already lists, named again after it'),
    'P5a-02': ('ask', 'his own paragraph: it explains his Nimja example after it has made the point'),
    'P5a-03': ('ask', 'his own paragraph: it explains his salt example after it has made the point'),
    'P5a-04': ('keep', 'examples of the term, not an explanation said twice; his published words'),
    'P5a-05': ('cut', '"Feel a state you have really been in ... Do your anchor thing", said again'),
    'P5a-06': ('cut', 'a preview list of the paragraph after it, which says each step'),
    'P5a-07': ('cut', '"the highest state I can get into", said again in the same sentence'),
    'P5a-08': ('cut', 'the next sentence says it ("I choose at least one thing to do that is from a loving place")'),
    'P5a-09': ('cut', 'sums the paragraph before it up'),
    'P5a-10': ('cut', '"That isn\'t saying that noticing patterns is bad", said again'),
    'P5a-11': ('cut', 'the aim the next paragraph gives with its limit ("to break out of a prison of perception")'),
    'P5a-12': ('cut', 'the gloss the guide gave the first time ("an if...then... plan")'),
    'P5b-01': ('keep', 'his own words; it names what the move implies (that they are spiritually inferior), a new point'),
    'P5b-02': ('ask', 'his own paragraph: the good guide and the bad guide each said from both sides'),
    'P5b-03': ('cut', 'the heading and the next paragraph say it ("first your body")'),
    'P5b-04': ('cut', 'a "So" conclusion of "There isn\'t a ton of evidence"; the first-line therapies stay'),
    'P5b-05': ('cut', 'sums up the two-way check the sentences before it describe'),
    'P5b-06': ('cut', 'the heading, and the next sentence\'s "work directly with the body"'),
    'P5b-07': ('cut', 'the guide\'s order (body, inner child, inquiry, action) summed up again'),
}
# P2a-06 and P2a-07 together take the whole paragraph, so neither keeps the reader's join; P3b-10 drops the next
# sentence's "And" too.
JOINS = {'P2a-07': '', 'P3b-10': "Allow your analytical part to make comments and/or tell you that it doesn’t like what you are doing. Just tell it that you will check things out, and make any commitments etc, when you are back. If it says no to going deeper, or tells you to stop doing the exercise, I’d stop there. You can stop whenever you want to. Just because you see an image, or feel a body release, doesn’t mean you are right about what is going on."}


def main():
    cands = json.loads((HERE / 'CANDIDATES.json').read_text(encoding='utf-8'))
    out, missing = [], []
    for c in cands['candidates']:
        if c['id'] not in D:
            missing.append(c['id'])
            continue
        dec, why = D[c['id']]
        x = {k: c[k] for k in ('id', 'part', 'block', 'cut', 'kind', 'strength', 'already_said', 'adds', 'loses', 'whose', 'where')}
        x['join'] = JOINS.get(c['id'], c.get('join', ''))
        x['decision'], x['why'] = dec, why
        if dec == 'cut' and c['whose'].startswith('his') and 'published' not in c['whose']:
            raise SystemExit('%s: his own words are asked, never cut here' % c['id'])
        out.append(x)
    (HERE / 'DECISIONS.json').write_text(json.dumps({'guide_sha256': cands['guide_sha256'], 'decisions': out,
                                                     'undecided': missing}, ensure_ascii=False, indent=1) + '\n',
                                         encoding='utf-8')
    import collections
    print(collections.Counter(x['decision'] for x in out), 'undecided:', missing)


if __name__ == '__main__':
    main()
