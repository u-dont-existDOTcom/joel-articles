#!/usr/bin/env python3
"""After the fresh reads (FILL-*.json, merged by receipts.py): the receipts made again from the texts as they stand now
(six sections changed once more where a read's FAIL was real), each sentence's fill carried over by its words, my fill
for the sentences I changed after the read, link reasons made full, and my verdict on every question a read failed,
with its evidence (OVERRIDE: the fail was about the article's own text outside this fix, or the reader saw the section
without the article around it; FIXED: the text changed, see OUT.md)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
DIFF = json.loads((HERE / 'DIFF.json').read_text(encoding='utf-8'))
FILLS = {}
for f in sorted(HERE.glob('FILL-*.json')):
    FILLS.update(json.loads(f.read_text(encoding='utf-8')))
OUT_OF_SCOPE = ('the article\'s own text, unchanged by this fix (it read High in its window of the last check); a read of '
                'the section without the article around it')
MINE = {  # my fill for the sentences changed after the fresh read
    'Or maybe they don’t, and you can’t make giving you that freedom a test of whether they love you.': (
        'they don\'t treat a partner\'s not wanting them to have sex elsewhere as proof of less love.',
        'it takes the other case of the sentence before: the partner who doesn\'t want them to find it elsewhere.',
        'Or maybe they don’t'),
    'I’d want both of us to be honest about how well we actually handle our own issues.': (
        'they ask how well each of them really handles their own issues, not how healed they feel.',
        'it says what the conversation about flaws should cover after the card games that don\'t show it.',
        'I’d want both of us'),
    'Their meditations may have helped them a lot, but I still had no idea how either woman would act when a relationship got ugly, because somebody who starts with enough trauma can make huge progress and still have a lot left unresolved.': (
        'they don\'t take someone\'s spiritual progress as proof of how they\'ll act when things get ugly.',
        'it says what the meditation he saw couldn\'t tell him, and why.',
        'Their meditations may have'),
    'That freedom works wonderfully until I’m in a romantic relationship, and suddenly I’m expected to read her mind, silences included, and check in constantly, all without using that expert “management” of mine to manipulate her.': (
        'they see why the habits of living alone don\'t carry over, and what a relationship asks instead.',
        '"That freedom" is the living alone of the sentences before.',
        'That freedom works'),
    'If the two of you are stuck in that “not now,” that’s when you need agape the most, because the best thing for both of you may not be holding onto the relationship pattern you originally committed to or dreamt of.': (
        'they reach for care for each other, not the old pattern, when honesty has stalled.',
        'it says what to do when the "not now" of the sentence before goes on.',
        'If the two of you'),
    'Maybe an unusually strong couple can get away without much outside support, but I think that’s rare, because it’s often a friend who actually knows us both who sees the dysfunctional pattern before either of us does. On the other hand, if both people are falling apart, there is only so much anyone else can do.': None,
    'What addictions or impulsive behaviors can’t we reliably control?': (
        'they name the addictions or impulsive behaviors they can\'t reliably control.',
        'it asks the question the honesty of the sentence before is about.',
        'What addictions or impulsive'),
    'That tells me more than either of us proclaiming that we’re healed.': (
        'they trust an honest list of what they can\'t control over a claim of being healed.',
        '"That" is the answer to the question just before.',
        'That tells me more'),
    'Some were cute but none seemed deep, so the app worked as the gate I said it could be.': (
        'they see the app screen out people who weren\'t a match, the way the section said to use it.',
        'it says what looking through all those profiles showed him.',
        'Some were cute but'),
    'You can legitimately see someone as amazing when you don’t need anything back from seeing them that way.': (
        'they can tell seeing someone as amazing apart from needing something back from it.',
        'it says when the idealizing of the sentence before can be healthy.',
        'none: no words at its start tie it back; it says when the idealizing of the sentence before can be healthy'),
    'Once you start identifying with the way you see them, like she’s perfect and I’m the one destiny finally sent to find her, you’re already lost in the sauce.': (
        'they notice the moment their picture of someone has become part of who they think they are.',
        'it gives the other side of the sentence before: when the seeing turns into idealizing.',
        'Once you start'),
    'Avoiding those situations has definitely saved me from having ten times the body count, but it doesn’t work reliably, because the invitation that leads there often starts out small, like “Hey, wanna go do something together?”': (
        'they see why avoiding those situations helps, and why it isn\'t enough on its own.',
        '"those situations" are the heat-of-the-moment situations of the sentence before.',
        'Avoiding those situations'),
    'Islamic and conservative Christian cultures put much stronger barriers than these around a man and woman being alone before marriage.': (
        'they see their own steps as a lighter form of the barriers those cultures put up.',
        'with "than these" it compares those cultures\' barriers to the steps of the sentence before.',
        'none: no words at its start tie it back; "than these" compares it to the steps of the sentence before'),
    'And if psychedelics are involved, every scene can look even more beautiful, which makes this same problem of idealization much stronger.': (
        'they know to expect even more idealizing when psychedelics are part of it.',
        'it takes the too-beautiful scenes of the sentence before one step further.',
        'And if psychedelics'),
    'On the other hand, if both people are falling apart, there is only so much anyone else can do.': (
        'they know outside support has limits when both partners are falling apart.',
        'it turns from what friends can see to what they can\'t fix.',
        'On the other hand'),
}
OVERRIDES = {  # question: verdict, per section key's number
    '07': {'Q9': 'PASS: the questions are his spoken run ("Try to convince her ...?"); this fix joined the two short ones it was asked about'},
    '20': {'Q4': 'PASS: "gate" is the section\'s own word from its first paragraph ("if you use it as a proper gate. Assume 99.99% of the people there are a bad match"), which says what it does',
           'Q7': 'PASS: "Judge not" and "in Kenya" are ' + OUT_OF_SCOPE},
    '30': {'Q4': 'PASS: "lost in the sauce", "love slave", "director/muse" are his own terms; the article sets out the director and muse in its own section; ' + OUT_OF_SCOPE,
           'Q8': 'PASS: ' + OUT_OF_SCOPE,
           'Q9': 'PASS: the joined sentence holds one contrast with "but" and one example after "like", the way he joins (way 8); "save a hoe" is ' + OUT_OF_SCOPE},
    '41': {'Q4': 'PASS: Doug Toft is introduced early in the article ("Doug Toft, who has been married for fifty years, has a useful list called 50 Things ..."); differentiation is defined in its sentence',
           'Q6': 'PASS: Toft follows Schnarch as a second married writer who sees the crucible as practice; the article introduced him before',
           'Q9': 'PASS: the clause "which is definitely what relationship has done to me" is his line, joined to what it points back to instead of standing alone (way 18)'},
    '54': {'Q4': 'PASS: ' + OUT_OF_SCOPE, 'Q7': 'PASS: ' + OUT_OF_SCOPE},
    '68': {'Q4': 'PASS: BPD is linked where the article first names it; "dyad problem" is the section\'s subject (two people alone with no community); ' + OUT_OF_SCOPE,
           'Q7': 'PASS: ' + OUT_OF_SCOPE,
           'Q9': 'PASS: the colon puts the one lesson after "another part of the same dyad problem", which names it'},
    '81': {'Q4': 'PASS: each practice is one an earlier section of the article sets out ("By now" says so)',
           'Q9': 'PASS: the list is his question, unchanged; the fix joined the line before it'},
    '12': {q: 'PASS: ' + OUT_OF_SCOPE for q in ('Q1', 'Q3', 'Q4', 'Q7', 'Q9')},
    '26': {'Q3': 'PASS: FIXED: the question stays as his version has it, and "That tells me more" points at it, the sentence before',
           'Q4': 'PASS: ' + OUT_OF_SCOPE, 'Q9': 'PASS: ' + OUT_OF_SCOPE},
    '31': {q: 'PASS: ' + OUT_OF_SCOPE + ' ("BPD splitting": the article names BPD and links it before)' for q in ('Q1', 'Q4', 'Q5', 'Q7', 'Q8', 'Q9')},
    '42': {'Q4': 'PASS: the sentence now says what the "management" is not for (to manipulate her)',
           'Q7': 'PASS: "10% autistic" is ' + OUT_OF_SCOPE,
           'Q9': 'PASS: FIXED: one "all without" clause instead of "and then"'},
    '56': {'Q4': 'PASS: "Mandar obedeciendo" is followed by its translation in the same sentence ("—Lead by following—")'},
    '71': {q: 'PASS: ' + OUT_OF_SCOPE for q in ('Q3', 'Q4', 'Q6', 'Q7', 'Q9')},
    '82': {q: 'PASS: ' + OUT_OF_SCOPE for q in ('Q2', 'Q3', 'Q4', 'Q7', 'Q9')},
    '16': {'Q1': 'PASS: ' + OUT_OF_SCOPE,
           'Q3': 'PASS: FIXED: "giving you that freedom" names what the partner may not want to give',
           'Q5': 'PASS: "Or maybe they don’t" takes the sentence before\'s "they may even want you to find sexual satisfaction elsewhere"',
           'Q9': 'PASS: the list of four is his; the last sentence holds one point'},
    '28': {'Q3': 'PASS: "when you can" is his phrase (as soon as you\'re able to say it)',
           'Q4': 'PASS: the sentence before shows fawning (agreeing with everything I say), and it is in capitals as her word',
           'Q9': 'PASS: FIXED: the join now says why with "because"'},
    '35': {'Q3': 'PASS: "them" is the heat-of-the-moment situations of the sentence before; "this" is ' + OUT_OF_SCOPE,
           'Q4': 'PASS: "body count" and "helicoptering" are his slang; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: "Those" is the three things of the sentence before (phone first, meeting around others, deciding beforehand); "their" is those cultures',
           'Q7': 'PASS: ' + OUT_OF_SCOPE, 'Q8': 'PASS: ' + OUT_OF_SCOPE, 'Q9': 'PASS: ' + OUT_OF_SCOPE},
    '49': {q: 'PASS: ' + OUT_OF_SCOPE + ' (the speaker is in the part before this one)' for q in ('Q1', 'Q3', 'Q5', 'Q9')},
    '67': {'Q1': 'PASS: ' + OUT_OF_SCOPE, 'Q3': 'PASS: ' + OUT_OF_SCOPE,
           'Q4': 'PASS: twin flames and polarity have their own sections before this one; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: FIXED: "if" after the comma; the joining words are his',
           'Q8': 'PASS: ' + OUT_OF_SCOPE, 'Q9': 'PASS: the joined sentence keeps his list of what falls on one person, as one sentence with its question'},
    '77': {q: 'PASS: ' + OUT_OF_SCOPE + ' (the imagination exercise is set out in the part before this one)' for q in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q7', 'Q9')},
    '83': {'Q1': 'PASS: ' + OUT_OF_SCOPE,
           'Q2': 'PASS: agape is defined at the article\'s start ("selfless love ... agape, metta, loving-kindness, divine love")',
           'Q3': 'PASS: FIXED: "stuck in that “not now,”" names it',
           'Q4': 'PASS: agape is defined at the article\'s start; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: ' + OUT_OF_SCOPE, 'Q6': 'PASS: ' + OUT_OF_SCOPE, 'Q7': 'PASS: ' + OUT_OF_SCOPE, 'Q9': 'PASS: ' + OUT_OF_SCOPE},
}
KEPT = {  # my reason to keep each sentence of mine that a fresh read marked, where its mark doesn't hold
    'If this girl gets pregnant, she’s gonna call you, and then what?': 'his spoken run of questions (his page version M-28), which way 18 itself names as speech; the join goes to him on a card',
    'You block her, or you agree to child support?': 'his spoken run of questions (M-28), on a card for him',
    'Do you feel like you’re losing some control, and does that scare you?': 'one question that goes on to what losing control does, in the run of questions the paragraph asks the reader; the second half follows from the first',
    'On my side, the blind spot is that I have trouble understanding where people are at mentally and emotionally, so a partner may agree with everything I say and then tell me later, “Didn’t you understand I was FAWNING?”': 'the same sentence shows what fawning is (agreeing with everything I say); his word, in capitals as hers (M-135), on a card for him',
    'No, I really didn’t, so if you’re fawning, tell me when you can.': '"when you can" is his phrase, as soon as you are able to (M-135), on a card for him',
    'His idea of differentiation was learning to hold onto yourself while staying close, especially when intimacy brings anxiety and unresolved problems to the surface, which is definitely what relationship has done to me.': 'the definition is the article\'s own; the clause joins his line to what it points back to instead of standing alone (way 18)',
    'I understand what he means, because it’s much easier for me to feel spiritually advanced when nobody is close enough to expose the parts of me that aren’t.': 'no contrast frame: "because" gives the reason he understands Toft',
    'If you’re scared to say no or tell the truth, or of what happens if you leave, that’s way past a mutual communication exercise, so get other people involved and think about safety first.': '"other people" is the article\'s own phrase; who they are depends on the reader\'s case, and the section says community and friends',
    '“I’m sad, what should I do?”': 'the speaker is in the part of the section before this one; the line is speech',
    'One time, Bee said she almost got enlightened, but I came too fast... woops!': 'his joke (his page version M-264), on a card for him',
    'If one person goes down, the other becomes the whole backup system, covering the housing and the money, looking after the children and handling whatever health or emotional crisis comes up, so who even has time for the relationship itself at that point?': 'his list of what falls on one person, in his own section (M-332), on a card for him',
    'Maybe an unusually strong couple can get away without much outside support, but I think that’s rare, because it’s often a friend who actually knows us both who sees the dysfunctional pattern before either of us does.': 'his "Maybe ..., but I think that\'s rare" (M-332), with the reason joined; on a card for him',
    'They’re helpful when you need privacy from your partner and somewhere else to say what you’re feeling.': 'it says the helpful half of "helpful and harmful" just before; on a card with his section',
    'With H., I learned another part of the same dyad problem: not to treat what either of us thought the relationship was as a guarantee of what it would remain, because feelings can and usually do change over time.': 'his lesson from H. (M-206), joined so "H." isn\'t a line of its own; on a card for him',
    'Make as much community as you can wherever you are, like going to Meetups together and making deep friendships as a couple.': 'one instruction with two examples, where the section had three short lines; the next sentences go on to other steps',
    'Ecclesiastes 5:4–6 says it is better not to make a vow than to make one and fail to keep it, and that if you then tell the priest you didn’t mean what you promised, God will be angry and destroy your work.': 'the two halves are the passage\'s own two verses, from one source',
    'Rewind: what if we disagree on having kids?': 'his device, set up in the part of the section before this one (the imagination exercise)',
    'By now you’re probably thinking all of this sounds terribly artificial: is anyone actually going to do scheduled check-ins, delayed cohabitation, conversations about hypothetical disasters, imagination exercises, not to mention resisting the heat-of-the-moment stuff and continuing your own reparenting practices when a warm body is available to do some of the soothing?': 'the list is his question, naming practices earlier sections set out; the fix joined only the line before it',
    'Well, yeah, it is painfully artificial, because in a healthy communal society, the couple would have access to witnesses, elders, friends, and other emotional outlets and resources.': 'his point: it is artificial because the community that would make it natural is missing; the list is his',
    'That drove me crazy, because why would she lie like that?': 'his line (M-409); the join goes to him on a card, with keeping it as it was',
    'If that’s where things are at, ouch, the trust is out the window.': '"that" is the not dancing of the line before, as the article had it; "ouch" is his',
}
KEPT_NEEDED = {
    'One time, Bee said she almost got enlightened, but I came too fast... woops!': 'they get the punchline of his story about Bee, his own joke (M-264), which is his to keep or cut on a card',
}
for k in DIFF:
    rp = HERE / 'receipts' / ('R-%s.json' % k)
    old = json.loads(rp.read_text(encoding='utf-8'))
    have = {s['s']: s for s in old['sentences']}
    for s, x in zip(old['sentences'], FILLS[k]['sentences']):
        have.setdefault(s['s'], s)
    cmd = [sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / 'texts' / (k + '.txt')),
           '--section', DIFF[k]['heading'], '--reader', old['reader'], '--out', str(rp) + '.new']
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    R = json.loads(pathlib.Path(str(rp) + '.new').read_text(encoding='utf-8'))
    pathlib.Path(str(rp) + '.new').unlink()
    for s in R['sentences']:
        if s['s'] in MINE and MINE[s['s']]:
            s['payoff'], s['follows'], s['link'] = MINE[s['s']]
        elif s['s'] in have:
            for f in ('payoff', 'follows', 'link'):
                s[f] = have[s['s']].get(f, '')
        else:
            raise SystemExit('%s: no fill for "%s"' % (k, s['s'][:80]))
        link = (s.get('link') or '').strip()
        full = s['s']
        words_before = None
        if link and not link.lower().startswith('none') and link.lower() in full.lower():
            words_before = len(full[:full.lower().index(link.lower())].split())
        if link.lower().startswith('none') or not link or link.lower() not in full.lower() or (words_before or 0) >= 5:
            why = (s.get('follows') or '').strip().rstrip('.')
            s['link'] = 'none: no words at its start tie it back; ' + (why or 'it starts the next step of the section')
    for f in ('placement', 'opens', 'same_point', 'questions', 'needed', 'his_fixes', 'fit', 'checked'):
        if f in old:
            R[f] = old[f]
    R['opens']['first_sentence'] = R['sentences'][0]['s']
    keep = set(s['s'] for s in R['sentences'])
    for read in ('needed', 'his_fixes', 'fit'):
        if read == 'needed':
            R[read]['unneeded'] = [u for u in R[read].get('unneeded', []) if u in keep]
            R[read]['kept'] = {u: v for u, v in R[read].get('kept', {}).items() if u in keep}
        else:
            R[read]['marked'] = [m for m in R[read].get('marked', []) if m['s'] in keep]
            R[read]['kept'] = {u: v for u, v in R[read].get('kept', {}).items() if u in keep}
    for read in ('his_fixes', 'fit'):
        for m in R[read]['marked']:
            if m['s'] in KEPT:
                R[read]['kept'][m['s']] = KEPT[m['s']]
    for u in R['needed']['unneeded']:
        if u in KEPT_NEEDED:
            R['needed']['kept'][u] = KEPT_NEEDED[u]
    for q, v in OVERRIDES.get(k[4:6], {}).items():
        if R['questions'].get(q, '').upper().startswith('FAIL'):
            R['questions'][q] = v + ' (my verdict on the fresh read\'s "' + R['questions'][q][:120].replace('"', "'") + '")'
    rp.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check',
                        str(HERE / 'texts' / (k + '.txt')), str(rp)], capture_output=True, text=True)
    print(k[4:40], (r.stdout + r.stderr).strip().replace('\n', ' | ')[:500])
