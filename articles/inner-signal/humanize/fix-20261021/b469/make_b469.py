"""Batch 469g (2026-10-21): Joel's answers of 17:56 UTC put into the guide.

- Question 2, c: Appendix C keeps its hypnosis-specific audit (seven questions) as a list, and the rest before it becomes
  prose: the general list of fourteen questions in one paragraph, and the lines around it said plainly. Every point of
  the published section is kept (the meaning check compares each with the published text).
- Question 4, d: "Come all the way back" is the Human version (installed, fix-20261018/rf-zf/HG18.smp1.json); Joel: "i am
  fine with all the humanized replacements as long as we don't lose anything". The one point it lost, pressing your
  feet or hands into a surface, goes back in the count's first step, which in the published text was "feel the body's
  contact and chosen weight".
- The inner-adult sweep (../CONFLATION-SWEEP.md, Joel: "check the guide for that conflation bc i have seen it before as
  well"): five of its six findings as the smallest fixes in the guide's own terms (his "inherited inner parent"; the roles
  by their capitalized names; "protector part" for a guard). Its finding 4 (the synchronicity cue's "a Protector
  warning") was in the NLP section's published text, which the installed Human version (rf-z/HG31.v3.json) has replaced;
  the same question in that version ("a message from my Inner Child, my Protector") goes to Joel, since either reading
  fits the guide.

  python3 articles/inner-signal/humanize/fix-20261021/b469/make_b469.py   (from the repo root)

Writes CANDIDATE.md, drafts.json (each changed paragraph as Pangram reads it: alone, or with the neighbor
tools/humanization/paragraphs_alone.py accepts when it is under 50 words), meta.json, the march draft and map,
REWRITE.md (for the stance check) and VERIFY-PROMPT.txt (each edit against the published text it replaces).
"""
import json, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
H = REPO / 'articles' / 'inner-signal' / 'humanize'
OUT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import sections as S          # noqa: E402
import paragraphs_alone as PA  # noqa: E402
import reviewer as R          # noqa: E402

APPC_OLD = None   # read from the working copy below: Appendix C's blocks from its first line to the audit's heading
APPC_NEW = '\n\n'.join([
    'Use this checklist when something is pressing on you too hard, whether it’s a person, an ad, an ideology, a '
    'spiritual teaching, a romantic pull or a voice inside you, stuff like that. You could say something like, “Okay, '
    'I notice that I’m being influenced. I don’t have to obey it, and I don’t have to attack it either. Let me slow '
    'down and ask what it’s taking for granted, and who it benefits. My body is telling me something, but I won’t '
    'assume I know what it proves. And what would love, truth, humility and ordinary life need from me here?',
    'If it’s true, it can handle my questions. If it’s real love, it’ll survive my boundaries. And real guidance will '
    'still be there after I sleep on it. Anything that’s really for me won’t ask me to give up my adult self.”',
    'Before acting on it, look for the usual signs, like urgency, secrecy, shame, a threat that you’ll be left out or '
    'a promise that you’re special, that kind of thing. Is there a sexual charge, or spiritual superiority? Be wary '
    'if it demands money or sex from you. Demands for your loyalty or your silence are signs too, and so is any '
    'demand for obedience.',
    'It’s a warning if your choices are being narrowed. Same if asking questions gets treated as betrayal, or your '
    'resistance gets treated like a pathology. Or if ordinary life starts to look small next to it, like the dishes '
    'and your friends don’t matter anymore.',
    'Notice whether your child part is being seduced or scared. Being rescued counts too. And is your adult self '
    'still allowed to say no?',
    'If you see several of these, slow down. Don’t go deeper into trance, and don’t make a decision you can’t undo. '
    'Just come back to the room and your body for a while. Then eat, sleep, give it time, get some counsel and so on.',
    'You can tell a good guide because your adult self gets stronger with them. And can they take your no? A bad '
    'guide can’t. They take your adult self’s place, and they’ll call your no resistance, ego, fear, low vibration, '
    'trauma, sin, you name it, or proof that you need more of their guidance.',
])
EDITS = [
    {'key': 'HG18-count-feet', 'lineage': 'HG18-p3', 'section': 'HG18', 'kind': 'edit',
     'old': "Then count up, using the five steps listed above: 1...feel your body again, feel your weight (of your choice). "
            "2...feel your breathing return to normal. 3...become aware of your surroundings, know where you are. 4...wiggle "
            "your fingers and toes, move your shoulders and your eyes. 5...open your eyes, back in the here and now, feeling "
            "normal and clear. This session is now over.\"",
     'new': "Then count up, using these five steps: 1...feel your body again and what it's resting on, feel your weight (of "
            "your choice). 2...feel your breathing return to normal. 3...hear the room, name "
            "where you are. 4...wiggle your fingers and toes, move your shoulders and your eyes. 5...open "
            "your eyes, back in the here and now, feeling normal and clear. This session is now over.",
     'published': "One — feel the body’s contact and chosen weight. Two — let the breath return to its ordinary rhythm. Three — "
                  "hear the room and name where you are. Four — move fingers, toes, shoulders, and eyes. Five — eyes open, "
                  "present, ordinary, clear. The session has ended. ... If a recording stops unexpectedly: say, “The recording "
                  "stopped and the session is over.” Open your eyes, name the location and day, press your feet or hands into a "
                  "surface, move, look around, and use the five-step count.",
     'diagnosis': 'not a 4.1 fix: the count\'s first step gets back the published "feel the body\'s contact" ("and what it\'s '
                  'resting on"), which the installed Human version (466g HG18-smp1) dropped (question 4; Joel, 17:56: "as long '
                  'as we don\'t lose anything"). And the cold read\'s two catches in the same paragraph (r1/SENSE-HG18.md P3): '
                  '"the five steps listed above" pointed at nothing above (they follow the colon), now "these five steps"; a '
                  'closing quotation mark with no opening one, a typo, out. Round 1 had put the pressing in this step instead, '
                  'which the meaning check read as an addition to every count (r1/VERIFY.md pair 1). Round 3: step three\'s '
                  '"know where you are" back to the published "name where you are" (r2 VERIFY pair 1: knowing had replaced '
                  'the act of naming)'},
    {'key': 'HG18-stopped-press', 'lineage': 'HG18-p5', 'section': 'HG18', 'kind': 'edit',
     'old': "If your recording cuts out for some reason, you can say to yourself, \"The recording has stopped and the session is "
            "over,\" and then do the above on your own.",
     'new': "If your recording cuts out for some reason, you can say to yourself, \"The recording has stopped and the session is "
            "over,\" and then do the above on your own. Once your eyes are open, press your feet or hands into a surface as well.",
     'published': "If a recording stops unexpectedly: say, “The recording stopped and the session is over.” Open your eyes, name "
                  "the location and day, press your feet or hands into a surface, move, look around, and use the five-step count.",
     'diagnosis': 'not a 4.1 fix: the one point the installed Human version (466g HG18-smp1) lost from the published steps, '
                  'pressing your feet or hands into a surface when a recording stops (question 4; Joel, 17:56: "as long as we '
                  'don\'t lose anything"), back where the published text had it, as a sentence of its own after the installed one (splitting that '
                  'sentence instead made the in-context linter count its installed "you can say to yourself" as mine, E41, '
                  'and so did "Start by pressing", a coach phrase); '
                  '"do the above" already carries the rest of the published list (eyes, location and day, moving, looking '
                  'around, the count). Round 3: "first" out, now "as well" (r2 VERIFY pair 2: the published order presses after '
                  'the eyes open; "first" put it before the count)'},
    {'key': 'HG32-prose', 'lineage': 'HG32-c', 'section': 'HG32', 'kind': 'rewrite', 'old': APPC_OLD, 'new': APPC_NEW,
     'published': None,
     'diagnosis': 'question 2, c (Joel, 17:56): the general list of fourteen questions becomes three short paragraphs of prose '
                  '(every sign kept, as statements in different shapes; where a list is needed it ends on a catch-all, his move, E125), and the lines around it are said plainly: the opening line '
                  'leads with "pressing on you too hard"; the statement to say gets the guide\'s own lead-in ("You could say '
                  'something like," as in "Love doesn\'t have to wait for trust") and plain words ("taking for granted" for '
                  '"presupposed"); its four tests keep their pairs (truth and questions, love and boundaries, guidance and '
                  'sleep, what is for me and the adult self) in four different shapes; the good and bad guide in two '
                  'sentences instead of four parallel ones. The hypnosis-specific audit and its last line stay as published. Round 2 '
                  'gave every paragraph a break the march can see (a question, a particular, a pause) and took the meaning check\'s '
                  'catches (r1/VERIFY.md pair 2); round 3 put back two published meanings (r2 VERIFY pair 3): "without assuming what '
                  'it proves" ("I won\'t assume I know what it proves") and love that survives boundaries ("Real love can handle my '
                  'boundaries, can\'t it?")'},
]
SWEEP = 'the inner-adult sweep (fix-20261021/CONFLATION-SWEEP.md, finding %d; Joel, 17:56: "check the guide for that conflation")'
CONFLATION = [
    {'key': 'HG14-cf-addressee', 'lineage': 'HG14-cf1', 'section': 'HG14', 'kind': 'edit',
     'old': "(“I notice you and what you are trying to do. I want to know more. Could I ask you what you are afraid would "
            "happen if you stopped protecting me by…..?)",
     'new': "(To the protector: “I notice you and what you are trying to do. I want to know more. Could I ask you what you "
            "are afraid would happen if you stopped protecting me by…..?”)",
     'published': "“I notice you. You are trying to protect something. I want to understand. What are you afraid would happen "
                  "if you stopped?”",
     'diagnosis': SWEEP % 1 + ': the script comes right after the paragraph on the inherited parent, which ends on "this '
                  'voice may jump in to say that what you\'re doing is “fake”", so "I notice you" reads as said to that voice, '
                  'and the lines after it ("if you stopped protecting me", "they don\'t have to stop protecting you") then '
                  'hand the inherited parent the protector\'s job and leave to carry on. The published script said it to the '
                  'protector ("You are trying to protect something"). Three words name who it\'s said to, a stage direction '
                  'like the script\'s own "(Now talk to the protector."; the closing quotation mark that was missing goes in'},
    {'key': 'HG20-cf-roles', 'lineage': 'HG20-cf2', 'section': 'HG20', 'kind': 'edit',
     'old': "bring in a “nurturer”, “protector”, “leader”, etc to help you either change the “tone” of the interaction, set "
            "boundaries, or help you figure out how to live your life in a better fashion, feel free to do so. You don’t have "
            "to talk to them, just use them to get whatever function you need that you aren’t able to do on your own.",
     'new': "bring in your “Nurturer”, “Protector” or “Leader” to help you either change the “tone” of the interaction, set "
            "boundaries, or find your way toward the life you want, feel free to do so. You don’t have to talk to them, just "
            "use the one whose job you need, and if you can’t do it yet, borrow it.",
     'published': "The Nurturer can change the tone; the Protector can carry out a boundary; the Leader can point toward the "
                  "life you want. They don’t each need a speech. When a capacity isn’t available, borrow that one function. Use "
                  "the Witness only if you need it to begin; don’t restart a step you can already do.",
     'diagnosis': SWEEP % 2 + ': the sentence before says "If you can identify any “protector” parts, talk to them", in the '
                  'same lowercase, quoted form, so "bring in a “protector”" reads as one more of those guards. The published '
                  'text and the rest of the guide give the three roles capitals. And the stance check\'s conflict in the same '
                  'paragraph (r1/STANCE.md, conflict 1): "use them to get whatever function you need that you aren\'t able to '
                  'do on your own" makes the three roles outside helpers, where the guide has them as your own adult functions '
                  '("I don\'t mean them as if there were really three people in you") and a missing one borrowed (the published '
                  '"When a capacity isn\'t available, borrow that one function"); now "and if you can\'t do one yet, borrow it". '
                  'Round 4 (r2/STANCE-r2.md, conflicts 3 and 4): "your" for "a" and the three roles without "etc", so a '
                  '"Protector" can\'t be the guard of the sentence before or one of an open set of helpers, and "the one whose '
                  'job you need" for "whatever function you need", each role with its own job as published; and the Leader\'s '
                  'job back to the published "the life you want" ("find your way toward the life you want" for "help you figure '
                  'out how to live your life in a better fashion", VERIFY-r4.md fix 4)'},
    {'key': 'HG24-cf-grownup', 'lineage': 'HG24-cf3', 'section': 'HG24', 'kind': 'edit',
     'old': "It could also be an inner voice of a parent that you are picking up, and it is trying to enforce a rule about how "
            "you should be to belong to them. Again, it isn't useful to argue with this part, but find out what rule it is "
            "enforcing and then work on finding some ordinary evidence to build a more believable 'grown up' voice.",
     'new': "It could also be the voice of your inherited inner parent that you are picking up, and it is trying to enforce a "
            "rule about how you should be to belong to them. Again, it isn't useful to argue with this part, but find out what "
            "rule it is enforcing and then work on finding some ordinary evidence to build a more believable 'grown up' voice "
            "of your own.",
     'published': "The voice may be the inherited parent enforcing an old belonging rule. Don’t argue with it. Ask which rule it "
                  "is enforcing and what ordinary evidence would make the new adult voice more believable.",
     'diagnosis': SWEEP % 3 + ', the pattern Joel fixed in "When “your voice” is everybody else’s voice": the parent\'s voice '
                  'was just named, so "a more believable \'grown up\' voice" can read as a more convincing version of that '
                  'same voice (a parent is a grown-up whose voice you picked up). The published text says "the new adult '
                  'voice". Two changes, as in his fix: his name for the internalized voice, "inherited inner parent", and '
                  '"of your own" for the adult one'},
    {'key': 'HG36-cf-protector', 'lineage': 'HG36-cf5', 'section': 'HG36', 'kind': 'edit',
     'old': "it could be your inner child, it could be a Protector, it could be all of the things",
     'new': "it could be your inner child, it could be a protector part, it could be all of the things",
     'published': "Sometimes the inner child is finally speaking. Sometimes a Protector is showing fear, or shame, grief, anger, "
                  "longing, and other buried material are asking for care.",
     'diagnosis': SWEEP % 5 + ': what comes up in an altered state "to be dealt with", next to the inner child, is one of the '
                  'guards (Appendix D: "the anxiety comes from a protector part of you, who is trying to help you, but who '
                  'believes you are in danger"), not the Protector you build, but the capital P (in the published text too: '
                  '"a Protector is showing fear") is the guide\'s spelling for the role. "a protector part", the guide\'s '
                  'own words for a guard'},
    {'key': 'HG37-cf-nurturer', 'lineage': 'HG37-cf6', 'section': 'HG37', 'kind': 'edit',
     'old': "if you feel sadness or fear or a need to protect yourself from it, call upon your Nurturer.",
     'new': "if you feel sadness or fear or like you’re trying to protect something, call upon your Nurturer.",
     'published': "If vulnerability appears—a knot in the throat, sadness, fear, or a sense of trying to protect something—you "
                  "can bring in the Nurturer.",
     'diagnosis': SWEEP % 6 + ': "a need to protect yourself from it" asks for protection from the presence, the Protector\'s '
                  'job in the guide\'s map ("Nurturer warms, Protector makes it safe"), so sending it to the Nurturer swaps '
                  'the roles. The published sentence has "a sense of trying to protect something" among the signs of '
                  'vulnerability, which the Nurturer meets; this puts it back in plain words'},
]
EDITS += CONFLATION
EDITS.append(
    {'key': 'HG24-cf-anxious', 'lineage': 'HG24-cf7', 'section': 'HG24', 'kind': 'edit',
     'old': "-Tell your Little parts and Protector parts that you’re there for your Little parts and that you recognize that "
            "your Protector parts are trying to protect you",
     'new': "-Tell your Little parts and protector parts that you’re there for your Little parts and that you recognize that "
            "your protector parts are trying to protect you",
     'published': "Little one, I am here. Protector, thank you for warning me. You do not have to scream for me to listen.",
     'diagnosis': 'the stance check of round 2 (r2/STANCE-r2.md, published contradiction 1) and the sweep\'s note on it (it '
                  'listed this line as clear but said "the capital P is the only mixed signal; lowercase would match" '
                  'Appendix D\'s "a protector part of you" and "Thank you protector"): the anxious guards that "scream at you" '
                  'carry the capital P of the Protector you build. Lowercase only; "Little parts" keeps its capital, as Joel '
                  'writes it'})
VERIFIED = ('HG18-count-feet', 'HG18-stopped-press', 'HG32-prose', 'HG20-cf-roles')   # the meaning check's pairs; the sweep's fixes go to CONFLATION-REVIEW
SECTIONS = {'HG18': 'Come all the way back', 'HG32': 'Appendix C: The extended de-hypnosis checklist'}


def main():
    global APPC_OLD
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    blocks = md.split('\n\n')
    s = next(i for i, b in enumerate(blocks) if b.startswith('# Appendix C'))
    a = next(i for i in range(s, len(blocks)) if blocks[i].startswith('## Hypnosis-specific audit'))
    APPC_OLD = '\n\n'.join(blocks[s + 1:a])
    appc = next(e for e in EDITS if e['key'] == 'HG32-prose')
    appc['old'] = APPC_OLD
    appc['published'] = APPC_OLD   # Appendix C was as published
    paras = {}
    for e in EDITS:
        assert md.count(e['old']) == 1, (e['key'], md.count(e['old']))
        if '\n\n' in e['old']:
            paras[e['key']] = (e['old'], e['new'])
        else:
            para = next(b for b in blocks if e['old'] in b)
            paras[e['key']] = (para, para.replace(e['old'], e['new']))
        md = md.replace(e['old'], e['new'])
    (OUT / 'CANDIDATE.md').write_text(md, encoding='utf-8')
    secs = {h: bl for h, bl in S.sections(md, str(H / 'source' / 'substack-editor-20260928.html'))}
    pp = PA.paragraphs(md)
    drafts, meta = {}, {}
    for e in EDITS:
        new_paras = [x for x in paras[e['key']][1].split('\n\n') if x.strip()]
        for n, p in enumerate(new_paras, 1):
            i = next(j for j, (_, q) in enumerate(pp) if q == p.strip())
            t, tries = PA.tries_for(md, pp, i)
            text = t if len(t.split()) >= 50 else next(x for x in tries if len(x.split()) >= 50)
            k = e['key'] if len(new_paras) == 1 else '%s-p%d' % (e['key'], n)
            drafts[k] = text
            meta[k] = {'section': e['section'], 'lineage': e['lineage'] if len(new_paras) == 1 else '%s-p%d' % (e['lineage'], n),
                       'words': len(text.split()), 'edit': e['key'], 'alone': text == t}
    for key, title in SECTIONS.items():
        bl = secs['# ' + title]
        drafts['%s-w469' % key] = S.text_of(bl)
        meta['%s-w469' % key] = {'section': key, 'words': len(drafts['%s-w469' % key].split())}
        (OUT / ('%s-section.md' % key)).write_text('\n\n'.join(m for m, _ in bl) + '\n', encoding='utf-8')
    (OUT / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (OUT / 'meta.json').write_text(json.dumps({'edits': EDITS, 'texts': meta}, ensure_ascii=False, indent=1) + '\n',
                                   encoding='utf-8')
    mparas, mp = [], []
    for e in EDITS:
        for ver, p in (('was', paras[e['key']][0]), ('new', paras[e['key']][1])):
            for q in [x for x in p.split('\n\n') if x.strip()]:
                q = S.plain(q)
                n = len(R.march_paragraphs(q))
                if n:
                    mparas.append(q)
                    mp.append({'key': e['key'], 'ver': ver, 'n': n, 'start': sum(m['n'] for m in mp)})
    if not (OUT / 'march-labels.txt').exists():
        (OUT / 'march-draft.txt').write_text('\n\n'.join(mparas), encoding='utf-8')
        (OUT / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    tops = [x for x in md.split('\n\n') if x.startswith('# ')]
    rw = []
    for key in dict.fromkeys(e['section'] for e in EDITS):
        rw.append(tops[int(key[2:]) - 1])
        rw += [paras[e['key']][1] for e in EDITS if e['section'] == key]
    (OUT / 'REWRITE.md').write_text('\n\n'.join(rw) + '\n', encoding='utf-8')
    pairs = []
    for i, e in enumerate([e for e in EDITS if e['key'] in VERIFIED], 1):
        was = e['published']
        pairs.append('## Pair %d (%s)\n\nPUBLISHED:\n%s\n\nEDITED:\n%s\n' % (i, e['key'], S.plain(was) if '\n\n' not in was else
                     '\n\n'.join(S.plain(x) for x in was.split('\n\n')), '\n\n'.join(S.plain(x) for x in paras[e['key']][1].split('\n\n'))))
    prompt = (
        "You check that a rewrite of part of a long self-hypnosis guide by Joel keeps every point of his published text. Below "
        "are %d pairs. In each, PUBLISHED is what the published guide says for that passage and EDITED is the new "
        "text. The guide is being rewritten in plainer words, and an earlier rewrite of these passages is installed; "
        "pairs 1 and 2 are the return steps' count and the paragraph for a recording that stops (in the published "
        "guide, the count's first step and the stopped-recording steps), pair 3 the general part of a checklist "
        "(the checklist's own audit list after it is unchanged), pair 4 a paragraph about bringing in the inner adult's "
        "three roles (Nurturer, Protector, Leader) during an inner meeting.\n\nFor each pair, list every point the published text makes (a claim, a step, a "
        "caution, a condition, a sign to watch for, a hedge such as \"may\") and say whether the edited text keeps it: KEPT, "
        "CHANGED (how a reader would now understand it differently) or LOST. Then list anything the edited text says that "
        "the published one doesn't: ADDED. Judge meaning only, not style or which version is better, and don't suggest "
        "rewrites. Keep your reasoning short.\n\nWrite your report with a single Write call to `%s`, one \"## Pair N\" part "
        "per pair, ending each with one line `VERDICT: OK` (every point kept, nothing added) or `VERDICT: CHANGED` (anything "
        "changed, lost or added), then reply with only the verdicts. Don't read any other file, don't run commands, and "
        "don't use the web.\n\n%s" % (len(VERIFIED), OUT / 'VERIFY.md', '\n'.join(pairs)))
    (OUT / 'VERIFY-PROMPT.txt').write_text(prompt, encoding='utf-8')
    for k, v in drafts.items():
        print(k, len(v.split()), 'words', '' if meta[k].get('alone', True) else '(with its neighbor)')
    print(len(mp), 'march paragraphs')


if __name__ == '__main__':
    main()
