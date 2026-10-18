"""HG31 round 2 (2026-10-18): my answers to the second reader's findings (verify-f, Sonnet in six parts, faithful.py
verify-chunks), as fixes that put the published meaning back with the fewest words changed, plus the published links'
places in the fixed text and two stray spaces Emulate left before punctuation. Findings let stand, and why, are in
dispositions.json. Run from fix-20261018/: python3 rev-g/make_HG31_round2.py"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
FROM = 'verify-f (the second reader, in six parts), checked by me'
P = {
 1: [('SHIFT', '"bodily states" had become how imagery is linked to them', 'how imagery is linked to bodily states', 'bodily states')],
 3: [('INVENTED', '"When it works" (a success condition) for the first of the four levels; LOST "changes the form of an inner experience"',
      'When it works, it works on a Sensory Level of NLP: changing where', 'First, it works on a Sensory Level of NLP: changing the form of an inner experience, where')],
 6: [('LOST', '"only" in "presume only safe capacity"', 'presuming their ability to do something safe', 'presuming only their ability to do something safe')],
 10: [('SHIFT', '"lower the pressure" is its own step; INVENTED "in the person" (it is the self)',
       'and I take the pressure off by presuming only a small safe capacity in the person and invite just one movement:',
       'I take the pressure off, presume only a small safe capacity and invite just one movement:')],
 12: [('SHIFT', '"validate function": the function of the reaction, not of what I am doing', "I validate the function of what I'm doing", 'I validate the function of the reaction')],
 17: [('SHIFT', '"my system is reacting", not a part with an intent', 'a part of me is trying to protect me by doing/thinking', 'my system is reacting by doing/thinking'),
      ('SHIFT', '"my adult self is here", not a part of me that is adult', 'there is a part of me that is adult, and that is breathing in this room right now, and is willing',
       'my adult self is here, breathing in this room right now, and willing')],
 19: [('INVENTED', '"Try some of the other" (an instruction, and "other" verbs)', 'Try some of the other ‘awareness’ verbs, which point attention', '‘Awareness’ verbs point attention')],
 22: [('SHIFT', '"safety", not "not doing something unsafe"', 'not doing something unsafe', 'safety')],
 26: [('SHIFT', '"too strong" (published), softened to inaccurate and "a bit strong"; INVENTED "the intention is good"; the repeat it made',
       'is that it’s likely to be inaccurate. It’s unlikely that simply breathing will get rid of the trauma. So while the intention is good, the phrasing is a bit strong.',
       'is that it’s too strong. It’s unlikely that simply breathing will get rid of the trauma.')],
 40: [('SHIFT', '"can soften", inflated to "very useful"', 'can be very useful to soften a sentence', 'can soften a sentence'),
      ('LOST', 'the tag question that shows itself ("don’t they?")', 'But they get oily really fast, so use them sparingly.', 'But they get oily really fast, don’t they? So use them sparingly.')],
 46: [('INVENTED', '"truly effective": the published says ethical practice needs both', 'In order to be truly effective (and ethical) with people, it is necessary to do both.',
       'In order to be ethical with people, it is necessary to do both.')],
 47: [('INVENTED', '"Good" added to "Compared to what?"', '‘Good’ compared to what?', 'Compared to what?')],
 59: [('LOST', '"without leaving the body, the facts, or ordinary human reality"', 'feeling my body and being still within the human reality',
       'without leaving my body, the facts or ordinary human reality'),
      ('SHIFT', '"choose one loving action", hedged to "usually I can do at least one"', 'and usually I can do at least one thing that comes from a loving place',
       'and I choose at least one thing to do that comes from a loving place'),
      ('LOST', '"objectivity" and "ease" in what I make room for', 'like clarity, peace, freedom, joy and gratitude', 'like objectivity, clarity, ease, peace, freedom, joy and gratitude')],
 68: [('LOST', '"use that opening"; INVENTED "to stimulate re-embodiment"', 'feel feet/body/breath/room to stimulate re-embodiment,', 'use that opening to feel feet/body/breath/room,')],
 71: [('SHIFT', '"rehearse returning to" a grounded, wider perspective', 'rehearse further steps to get a more grounded and wide view,', 'rehearse returning to a more grounded and wide view,')],
 74: [('SHIFT', '"resembles" an implementation intention, not "is a kind of"', 'This is a kind of implementation intention ,', 'This is like an implementation intention,'),
      ('TYPO', 'a stray space before the parenthesis', 'by Gollwitzer ).', 'by Gollwitzer).')],
 76: [('INVENTED', '"creating false positives" as a further reason to deactivate', 'are creating false positives or making any of these worse', 'are making any of these worse'),
      ('SHIFT', '"certainty" that random events are personally directed messages', 'you feel that random events are occurring', 'you become certain that random events are occurring')],
 79: [('SHIFT', '"I prefer questions that widen meaning without lying" (LOST "widen meaning")',
       'so I have to be honest when I reframe. To reframe in a helpful way is to ask myself a series of questions like:',
       'so I prefer to ask myself questions that widen the meaning without lying, like:')],
 83: [('INVENTED', '"see the truth" and "a great way"; the repeat they made', 'Use them to see the truth from more than one angle. They’re a great way to get out of a prison of perception.',
       'Use them to get out of a prison of perception, to see from more than one angle.')],
 101: [('LOST', '"inside soft language"', 'Giving covert commands', 'Giving covert commands inside soft language')],
 104: [('SHIFT', 'the states are the levers, not the people in them', 'Manipulating people in trance,', 'Using people’s trance,')],
 108: [('INVENTED', '"Where?" is not one of the published dimensions', 'posture? Where? How big?', 'posture? How big?')],
 110: [('LOST', '"add space"', 'turn down the volume, change body posture', 'turn down the volume, add space, change body posture')],
}
LINKS = {9: [{'published': 'indirect language', 'new': 'indirect language'}],
         74: [{'published': 'implementation intention', 'new': 'this paper by Gollwitzer'}],
         75: [{'published': 'Blain and colleagues', 'new': 'Blain et al.'}, {'published': 'Grant and colleagues', 'new': 'Grant et al.'}]}
fixed = json.loads((HERE / 'HG31.fixed.json').read_text(encoding='utf-8'))
now = {u['blocks'][0]: '\n\n'.join(u['paras']) for u in fixed['units'] if u['kind'] == 'emulate'}
out = []
for b in sorted(set(P) | set(LINKS)):
    body = now[b]
    probs = []
    for t, what, rep, wth in P.get(b, []):
        assert body.count(rep) == 1, (b, rep, body.count(rep))
        body = body.replace(rep, wth)
        probs.append({'type': t, 'what': what, 'replace': rep, 'with': wth, 'round': 2, 'from': FROM})
    for l in LINKS.get(b, []):
        assert l['new'] in body, (b, l)
    rec = {'block': b, 'problems': probs}
    if b in LINKS:
        rec['links'] = LINKS[b]
    out.append(rec)
(HERE / 'HG31.round2.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(out), 'stretches,', sum(len(r['problems']) for r in out), 'fixes ->', HERE / 'HG31.round2.json')
