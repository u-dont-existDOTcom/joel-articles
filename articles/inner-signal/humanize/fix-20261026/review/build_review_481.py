"""The hypnosis guide's marking page for batches 479 to 481 (REVIEW-481.json, REVIEW-481.html), question 21.

Joel, 2026-10-26 12:43 UTC, with batch 480's recheck (part A https://www.pangram.com/feed/0f1902cd-df2a-4837-9879-69979188e5f1,
100% Human; part B https://www.pangram.com/feed/1a9e674f-113e-46ad-8a07-0fb6b71ad65e, one AI segment): "i also want you to
fix any segments that are not high confidence human if you can, and always we should be marking down the confidence if we
have it, because less than high confidence means it's likely next pangram version will mark it ai (that happened in
pangram 4.1 update)". So the page has, on his working copy (HUMANIZED-SO-FAR.md):
- the ten cards of batches 479 and 480 (build_review_480.py), each now with how it read in that check and at what
  confidence (E278);
- batch 481's 24 (../b481/make_b481.py): Emulate's versions of the stretches that read Human at Medium or Low confidence
  there, each through the owner-delivery gate (../b481/gate/), and in the two temporary drafts for his next check.
Every new sentence on the page is the gate's delivered text (<gate>/<NAME>/FOR-JOEL.txt), byte for byte, and every changed
paragraph, with all its cards applied, is the paragraph as the next check has it (../b481/CANDIDATE-MASTER.md).

  python3 articles/inner-signal/humanize/fix-20261026/review/build_review_481.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import build_review as br  # noqa: E402  (its helpers, and the working copy as it is now)

sr = br.sr
br.match_style = lambda new, para: new   # the gate delivered these exact words; the post curls quote marks anyway
GIT_FILE = 'articles/inner-signal/humanize/fix-20261026/review/REVIEW-481.html'
SPOTS = {
    'b479': json.loads((H / 'fix-20261025' / 'b479' / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots'],
    'b480': json.loads((H / 'fix-20261026' / 'b480' / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots'],
    'b481': json.loads((H / 'fix-20261026' / 'b481' / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots'],
}
MASTER = sr.blocks((H / 'fix-20261026' / 'b481' / 'CANDIDATE-MASTER.md').read_text(encoding='utf-8'))
GATES = {'b479': H / 'fix-20261026' / 'gate', 'b480': H / 'fix-20261026' / 'gate', 'b481': H / 'fix-20261026' / 'b481' / 'gate'}
A = 'https://www.pangram.com/feed/0f1902cd-df2a-4837-9879-69979188e5f1'
B = 'https://www.pangram.com/feed/1a9e674f-113e-46ad-8a07-0fb6b71ad65e'
TYPES = {
    'held': {'label': 'Read Human (High) in place',
             'about': 'Emulate\'s version of a stretch that read AI in an earlier check. In your last check of the whole guide it read Human, High confidence, where it stands.'},
    'notyet': {'label': 'Read Human, less than High',
               'about': 'Emulate\'s version of a stretch that read AI in an earlier check. In your last check it read Human where it stands, but at Medium or Low confidence.'},
    'confidence': {'label': 'Was Human at less than High',
                   'about': 'In your last check this read Human, but at Medium or Low confidence, which a later Pangram version is likeliest to read AI. Emulate\'s version is in the two temporary drafts, so your next check shows how it reads in place.'},
    'confidence-his': {'label': 'Your words, Human at Low',
                       'about': 'Your own words read Human at Low confidence in your last check. Emulate\'s version is in the two temporary drafts for your next check; Reject keeps your words.'},
}
FOUND = 'Pangram\'s check of the whole guide (your Substack drafts), then Emulate, the meaning reads and the gate\'s three reviewers'
FOUND_481 = ('Your last Pangram check of the whole guide, its windows at less than High confidence (window_confidence.py), then '
             'Emulate and the gate\'s three reviewers')

# id: (gate NAME, the working copy's words (batch, spot), the new words (batch, spot), type, title, why, note)
CARDS = [
    ('HG-S7', 'G-S7', ('b479', 'S1'), ('b480', 'S7'), 'held', 'One person, three jobs',
     'Your inner child guide\'s whole sentence, with the rent joke, read AI (High) two checks ago. Emulate\'s version, with your '
     '"keeps" put back, read Human checked alone and Human (High) where it stands in your last check (part A). "Grown-up" '
     'becomes "person"; the sentences around it say it\'s you.',
     'Approve: the rent joke stays, and it reads Human (High) in place.'),
    ('HG-S2', 'G-S2', ('b479', 'S2'), ('b479', 'S2'), 'held', 'Borrowed adulthood, the bridge',
     'This whole paragraph read AI (High) three checks ago. Emulate\'s version read Human where it stands in your last two '
     'checks, High in the last (part A). Your two published points are back in it: the practices are familiar ones, and you '
     'don\'t claim the whole sequence is proven as one treatment.',
     'Approve.'),
    ('HG-S3a', 'G-S3a', ('b479', 'S3a'), ('b480', 'S3a2'), 'held', 'Pointer to "Already open?"',
     'The end of this paragraph read AI (Low) three checks ago. Emulate\'s version, without "you can" (the gate\'s check counts '
     'it as coaching), read Human (High) where it stands in your last check (part A). The section\'s own heading is in it so '
     'a reader can find it, and your "not stable" stays.',
     'Approve.'),
    ('HG-S3b', 'G-S3b', ('b479', 'S3b'), ('b479', 'S3b'), 'notyet', 'The three stop words',
     'These two sentences read AI (four Low windows) three checks ago. Emulate\'s three short sentences read Human where they '
     'stand in both later checks, but in your last one (part A) at Medium (0.944), Low (0.879) and Medium (0.972) confidence. '
     'Emulate\'s new versions only moved commas or put "you can" back in, so these stay for now. Each of your words keeps what '
     'it does: "stop" ends the induction, "less" asks less of you, "quiet" stops the talking.',
     'Approve: it reads Human, and I have no better version yet.'),
    ('HG-S8', 'G-S8', ('b480', 'S8'), ('b480', 'S8'), 'held', 'Ask the guard what it wants first',
     'These two sentences (IC-A14, the inner child alignment card you approved) read AI (Medium and High) two checks ago, '
     'after the edits above them. Emulate\'s version read Human checked alone, and Human (High) where it stands in your last '
     'check (part A). It ends on your card\'s "or a bit of each". The guard prompt after it read Human again, two of its '
     'lines at Medium.',
     'Approve.'),
    ('HG-S9', 'G-S9', ('b480', 'S9'), ('b480', 'S9'), 'held', 'What the parent script is',
     'These two sentences read AI (Low and Medium) two checks ago, after the edits above them, though they hadn\'t changed. '
     'Emulate\'s three sentences read Human (High) where they stand in your last check (part A), and so did the paragraph\'s '
     'last two sentences. One word to know: "internalized" becomes "adopted", and the brackets still say it came from how '
     'you were treated.',
     'Approve.'),
    ('HG-S4', 'G-S4', ('b479', 'S4'), ('b479', 'S4'), 'held', 'Big or hard-to-undo things wait',
     'These are your own two sentences from your inner child guide, and here they read AI (Low and High) three checks ago. '
     'Emulate\'s one sentence read Human where it stands in both later checks, High in the last (part B). It keeps both '
     'points: it has to make sense to you, and anything big or hard to undo waits till you\'re calm and have checked it '
     'against what you know. One change in strength: your "can wait" becomes "wait".',
     'Approve if the firmer "wait" is fine with you. Reject keeps your two sentences, which read AI here.'),
    ('HG-S5', 'G-S5', ('b479', 'S5'), ('b480', 'S5b'), 'held', 'No warmth today',
     'This line, from your inner child guide (the inner child alignment added it), read AI (High) here three checks ago. '
     'Emulate\'s version, ending on your own three words from that guide, "no faking required", read Human (High) where it '
     'stands in your last check (part B). (The gate\'s check counts "you don\'t have to" as coaching, and a reviewer turned '
     'down "Don\'t fake it." because it makes your permission a rule.)',
     'Approve: Emulate\'s start, your ending.'),
    ('HG-S6', 'G-S6', ('b479', 'S6'), ('b479', 'S6'), 'held', 'The test for a response',
     'Your published test, word for word, read AI here (High, 17 words) three checks ago. Emulate\'s question read Human '
     'where it stands in both later checks, High in the last (part B). It asks the same test: whether this way of responding '
     'helps you get clearer, steadier and less hooked.',
     'Approve if a question is fine there. Reject keeps your sentence, which read AI here.'),
    ('HG-S10', 'G-S10', ('b480', 'S10'), ('b480', 'S10'), 'held', 'Borrowing Nurturer and Protector',
     'This sentence, from your inner child guide (the inner child alignment added it, IC-B19), read AI (Low) two checks ago. '
     'Emulate\'s version read Human (High) where it stands in your last check (part B). It keeps both conditions: someone '
     'stable, and not someone who will take over your trip.',
     'Approve.'),
    # batch 481: the windows at less than High confidence in that check (gate E278)
    ('HG-S11', 'G-S11', ('b481', 'S11'), ('b481', 'S11'), 'confidence', 'The daily and weekly sections',
     'Read Human (Medium, 0.989, just under High) in your last check (part A). Emulate\'s "read some of the stuff in" for "look '
     'at"; the sentence keeps its end, from your published "The daily and weekly sections help you make the practice your '
     'own". "You can also" became "Also": the gate\'s check counts "you can" as coaching.',
     'Approve.'),
    ('HG-S12', 'G-S12', ('b481', 'S12'), ('b481', 'S12'), 'confidence-his', 'The hidden menu',
     'Your own sentence read Human (Low, 0.649) in your last check (part A). Emulate\'s version keeps the point (the hidden '
     'table of contents helps because the guide is long), but not your "that little hidden menu is your friend".',
     'Your call: it trades your joke for a plainer line. Reject keeps your sentence.'),
    ('HG-S14', 'G-S14', ('b481', 'S14'), ('b481', 'S14'), 'confidence', 'Influence without the conscious mind',
     'Read Human (Medium, 0.982) with the paragraph before, 77 words, in your last check (part A). Emulate\'s first and third '
     'sentences go around your own second one, which stays: "Marketers and interface designers know this perfectly well." '
     'The FTC sentence keeps your "designs that trick or manipulate consumers" (a reviewer turned down Emulate\'s "their" and '
     '"used to trick and manipulate"), and "dark patterns" keeps the quote marks it had here.',
     'Approve.'),
    ('HG-S15', 'G-S15', ('b481', 'S15'), ('b481', 'S15'), 'confidence', 'Four kinds of agreement',
     'Its first line, the four kinds of agreement, read Human (Low, 0.848) in your last check (part A). Emulate joins it to '
     'the question with a dash, so the list leads into the question instead of standing alone.',
     'Approve.'),
    ('HG-S16', 'G-S16', ('b481', 'S16'), ('b481', 'S16'), 'confidence', 'Each can correct the other',
     'Read Human (Medium, 0.989) with the next line in your last check (part A). Emulate\'s "So each can correct the other." '
     'for "So these modes can correct each other."',
     'Approve.'),
    ('HG-S17', 'G-S17', ('b481', 'S17'), ('b481', 'S17'), 'confidence', 'It has to lead somewhere',
     'The same window as the card before. All three of Emulate\'s versions drop the "And".',
     'Approve.'),
    ('HG-S18', 'G-S18', ('b481', 'S18'), ('b481', 'S18'), 'confidence', 'Sober, and not suggestible',
     'These two sentences read Human (Medium, 0.944) and Human (Low, 0.531) in your last check (part A). Emulate\'s version '
     'keeps your points, and your published "trust and precision" ends it. Two fixes to Emulate\'s words: "One reason was" '
     'became "might have been" (your published "Maybe part of that"), and "wasn\'t that susceptible" became "didn\'t feel '
     'that susceptible", since you said how you felt.',
     'Approve.'),
    ('HG-S19', 'G-S19', ('b481', 'S19'), ('b481', 'S19'), 'confidence', 'The body\'s no',
     'Read Human (Low, 0.829) in your last check (part A). Emulate\'s "before my conscious mind can twist it around to a yes" '
     'is close to your published "before the conscious mind writes a persuasive little essay called yes".',
     'Approve.'),
    ('HG-S20', 'G-S20', ('b481', 'S20'), ('b481', 'S20'), 'confidence', 'Quiet little preferences',
     'This sentence and the two before it (your inner child guide\'s, which stay) read Human (Low, 0.722, 64 words) in your '
     'last check (part A). This is Emulate\'s version of the last one, with its quote marks around "social" taken off. One '
     'shift: "echoing your social group" becomes "going by what your social group would want you to do".',
     'Approve if that shift is fine with you.'),
    ('HG-S21', 'G-S21', ('b481', 'S21'), ('b481', 'S21'), 'confidence', 'Come back the other way',
     'Read Human (Medium, 0.987) with the bracket after it in your last check (part A). Emulate\'s "make sure to" makes the '
     'step a little firmer.',
     'Approve.'),
    ('HG-S22', 'G-S22', ('b481', 'S22'), ('b481', 'S22'), 'confidence', 'Read it out loud',
     'These three sentences read Human (Medium, 0.974) in your last check (part A). Emulate\'s version keeps the three points; '
     'one shift: "when you\'re being induced" becomes "when you\'re trying to induce", and "It\'s all soup to you at that '
     'point" puts it back on the person in the induction.',
     'Approve.'),
    ('HG-S23', 'G-S23', ('b481', 'S23'), ('b481', 'S23'), 'confidence', 'What you want to do today',
     'The paragraph read Human (Medium, 0.982, 58 words) up to its last sentence in your last check (part A). Emulate\'s first '
     'two sentences: "Think about what you want to do." for "Get clear on what it is you want to do during the induction", '
     'and a yes-or-no question for what you don\'t want to do today. The rest stays.',
     'Approve.'),
    ('HG-S24', 'G-S24', ('b481', 'S24'), ('b481', 'S24'), 'confidence', 'A safe place',
     'Read Human (Medium, 0.986) in your last check (part A). Two of Emulate\'s three versions gave this same sentence.',
     'Approve.'),
    ('HG-S25', 'G-S25', ('b481', 'S25'), ('b481', 'S25'), 'confidence', 'Deciding to do it',
     'The paragraph\'s first eight sentences read Human at Medium (0.949), Low (0.879, "Something else?") and Medium (0.957) '
     'in your last check (part A). Emulate\'s version: "Decide to do it.", "etc." for "Something else?", and "Preview what '
     'you are going to do." with the questions after it. The stop lines later in the paragraph are the card "The three stop '
     'words".',
     'Approve.'),
    ('HG-S26', 'G-S26', ('b481', 'S26'), ('b481', 'S26'), 'confidence', 'One next action',
     '"Give me one next action!" read Human (Low, 0.727) in your last check (part A). Emulate asks it as a question. The three '
     'BEFORE requests before it read Medium; Emulate put "Please" in front of each, and three new exclamations in a row fail '
     'the gate\'s check, so they stay as they are.',
     'Approve.'),
    ('HG-S27', 'G-S27', ('b481', 'S27'), ('b481', 'S27'), 'confidence', 'Treat it as an image',
     'The end of its first sentence and its last sentence read Human (Medium, 0.989 and 0.982) in your last check (part A). '
     'These are Emulate\'s; the middle sentence stays.',
     'Approve.'),
    ('HG-S28', 'G-S28', ('b481', 'S28'), ('b481', 'S28'), 'confidence', 'Try it smaller',
     'Read Human (Low, 0.618) in your last check (part A). Emulate\'s shorter question, with your "this".',
     'Approve.'),
    ('HG-S29', 'G-S29', ('b481', 'S29'), ('b481', 'S29'), 'confidence-his', 'The smaller asks',
     'Your three published requests read Human (Low, 0.575) with the next section\'s first sentence in your last check (part '
     'A). Emulate\'s version makes them a suggestion ("Maybe ask to be shown ...") instead of lines to say, and ends on your own '
     '"today is for listening or resting" (Emulate\'s "listening to something" made it something outside you).',
     'Your call: it loses the ready-to-say lines. Reject keeps them.'),
    ('HG-S30', 'G-S30', ('b481', 'S30'), ('b481', 'S30'), 'confidence', 'What feels fake',
     'Read Human (Low, 0.575) with the three requests before the heading in your last check (part A). This is Emulate\'s '
     'question.',
     'Approve.'),
    ('HG-S31', 'G-S31', ('b481', 'S31'), ('b481', 'S31'), 'confidence-his', 'The part that remembers',
     'This sentence from your inner child guide read Human (Low, 0.531) in your last check (part A). Emulate\'s start, "You may '
     'have fooled yourself in the past", ends on your own "and that part remembers", and your next line stays. (Emulate\'s '
     'whole version, "this part knows it. Try ...", lost your "remembers" and your "works well here", and a reviewer turned '
     'it down.)',
     'A small change: approve if you like it. Reject keeps your sentence.'),
    ('HG-S32', 'G-S32', ('b481', 'S32'), ('b481', 'S32'), 'confidence-his', 'The ethical double bind',
     'Your published sentence read Human (Low, 0.640) in your last check (part B). Emulate\'s version names the Ethical Double '
     'Bind Question instead of "one", with your "genuinely" put back (a reviewer turned down the version without it).',
     'Approve if the spelled-out name is fine with you. Reject keeps your sentence.'),
    ('HG-S33', 'G-S33', ('b481', 'S33'), ('b481', 'S33'), 'confidence', 'A little script',
     'Read Human (Medium, 0.984) with the script\'s first two questions in your last check (part B). Emulate\'s line drops '
     '"for anxiety", which the heading says.',
     'Approve.'),
    ('HG-S34', 'G-S34', ('b481', 'S34'), ('b481', 'S34'), 'confidence', 'Finding my body parts',
     'The same window as the card before. Emulate\'s "Let’s see if I can find my body parts." (its "Lets" typo fixed) for "Where '
     'are my body parts?": the script\'s first question becomes a gentler first step.',
     'Approve.'),
    ('HG-S36', 'G-S36', ('b481', 'S36'), ('b481', 'S36'), 'confidence', 'What is theirs, what is mine',
     'These two questions read Human (Medium, 0.963) with your "What does accountability require?" in your last check (part '
     'B). Emulate makes them one: "What’s theirs and what’s mine?" (Its "What boundaries do I need to set as a result?" for the '
     'question before them dropped your published "still", and a reviewer turned it down, so that one stays.)',
     'Approve.'),
]


def main():
    added = []
    for sid, name, old_ref, new_ref, typ, title, why, note in CARDS:
        d = GATES[new_ref[0]] / name
        delivered = (d / 'FOR-JOEL.txt').read_text(encoding='utf-8') if (d / 'FOR-JOEL.txt').exists() else None
        old_c, new_c = SPOTS[old_ref[0]][old_ref[1]], SPOTS[new_ref[0]][new_ref[1]]
        if delivered is None:
            print('SKIP', sid, '(not delivered by the gate)')
            continue
        assert delivered == new_c['new'], sid
        i = old_c['block']
        assert old_c['old'] in br.BL[i]['text'] or sr.norm_map(old_c['old'])[0] in sr.norm_map(br.BL[i]['text'])[0], sid
        br.add(sid, typ, title, 'approve', edits=[(i, old_c['old'], new_c['new'])], why=why, note=note,
               found_by=FOUND_481 if new_ref[0] == 'b481' else FOUND)
        added.append((sid, i, old_c['old'], new_c['new']))
    # every paragraph with all its cards applied is the paragraph the next check has
    by = {}
    for sid, i, old, new in added:
        by.setdefault(i, []).append((sid, old, new))
    for i, edits in by.items():
        t = br.BL[i]['text']
        for sid, old, new in edits:
            t = t.replace(br.locate(sid, t, old), new)
        assert t == MASTER[i]['text'], (i, [e[0] for e in edits], t[:80], MASTER[i]['text'][:80])
    br.S.sort(key=lambda s: (br.first_block(s), br.order_key(s['id'])))
    br.overlaps()
    n_new = sum(1 for s in br.S if s['type'].startswith('confidence'))
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-b481-20261026',
        'title': 'Hypnosis Guide Emulate Fixes',
        'intro': [
            'This is your hypnosis guide as it is in Git now, with everything you approved. Each card is a sentence or a few '
            'with Emulate\'s version in their place, and each new version passed the gate\'s three reviewers.',
            'The %d cards from before are the stretches that read AI in an earlier check; your last check (<a href="%s">part '
            'A</a>, <a href="%s">part B</a>) read all but one of them Human with High confidence, and each card now says so. '
            'The %d new ones are for stretches that read Human there but at Medium or Low confidence, which a later Pangram '
            'version is likeliest to read AI; they are in the two temporary drafts, so your next check shows how they read in '
            'place. Each card gives the confidence it read at.' % (len(br.S) - n_new, A, B, n_new),
            'Click <b>Approve</b>, <b>Reject</b> or <b>Revise</b> on each card, and add a comment if you want. If you leave '
            'cards unmarked, tell me whether to take my advice on them as you did last time. Your answers save as you click.',
        ],
        'git_file': GIT_FILE, 'article': {'file': br.ARTICLE, 'sha256': hashlib.sha256(br.MD.encode('utf-8')).hexdigest()},
        'links': {'guide': br.BLOB + br.ARTICLE, 'review': br.BLOB + 'articles/inner-signal/humanize/fix-20261026/review/REVIEW-481.json'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': br.S,
    }
    probs = sr.check(review, br.BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-481.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, br.MD, br.BL)
    (HERE / 'REVIEW-481.html').write_text(page, encoding='utf-8')
    print(len(br.S), 'cards (%d new);' % n_new, HERE / 'REVIEW-481.html', len(page), 'bytes')


if __name__ == '__main__':
    main()
