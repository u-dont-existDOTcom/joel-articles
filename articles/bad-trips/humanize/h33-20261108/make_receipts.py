#!/usr/bin/env python3
"""make_receipts.py - fills TEST-SNOJ and TEST-FNOJ's receipts: sentences an earlier receipt in this lane covers keep its
payoff, follows and link; the new ones are below. The needed read is NEEDED-READ.md (Haiku).

  python3 make_receipts.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
EARLIER = {}
for f in sorted(HERE.parent.glob('h*/TEST-*.receipt.json')):
    if f.parent == HERE:
        continue
    try:
        for s in json.loads(f.read_text())['sentences']:
            if s.get('payoff') and s.get('follows'):
                EARLIER[s['s']] = s
    except (ValueError, KeyError):
        continue
NEW = {
 'During the experience, the sitter (the sober person with you) keeps you safe and offers you choices if relevant.':
  ('they know what the sitter does during it, and who the sitter is', 'from before the session to during it', 'During the experience'),
 'Stop adding stimulation.': ('they stop adding stimulation as it ends', 'the first step of the closure', 'Stop adding stimulation'),
 "Sometimes it can be helpful to remind them where they are and what's happening, since a trip can make them lose track of the fact that they took a substance which has temporary effects.":
  ('they tell the person where they are and that the effects pass', 'after the room is calmer, the next thing to do', 'Sometimes it can be helpful to remind them'),
 'As the person helping, you want to play the role of the calm, caring anchor to the safe present moment, not a guru.':
  ('they know their role: a calm anchor to the present, not a guru', 'the next section\'s heading, after the reminder, as a line', None),
 "So don't try to win an argument with their visions, the entities they spoke to, the memories that surfaced, or whatever cosmic conclusions they reached ten minutes ago...":
  ('they don\'t argue with what the person saw or concluded', 'it follows from the role: an anchor doesn\'t argue', 'So'),
 "But don't let silence validate anything harmful either, like a plan that ends with somebody getting hurt.":
  ('they still speak up when a conclusion means harm', 'the limit on not arguing', 'But'),
 "Don't encourage them to believe they are crazy, impure, weak or broken.":
  ('they don\'t feed the person\'s fear about themselves', 'the next don\'t, about what the person believes of themselves', "Don't encourage them"),
 "While many interpretations are possible, a therapeutic one would not be that they're being punished or failing the medicine.":
  ('they don\'t frame it as punishment or failure', 'the same don\'t, for the interpretations', 'While many interpretations are possible'),
 "Don't force eye contact, touch, music, prayer, chanting, a confession or an insight on them.":
  ('they force nothing on the person', 'the last don\'t, about what they do to the person', "Don't force"),
 "After they've slept, they may wish to talk more about their experience.":
  ('they leave the talking for after sleep', 'what to do with all of it instead: later', "After they've slept"),
}
Q = {
 'SNOJ': {'Q1': 'PASS: each paragraph opens on its point', 'Q2': 'PASS: the instructions say what they are for', 'Q3': 'PASS: "a psychoactive drug", "this type of meditation"',
          'Q4': 'PASS: "sitter" glossed where first used; "plastic" glossed', 'Q5': 'PASS: the order of a session', 'Q6': 'PASS: before, during, the end, after',
          'Q7': 'PASS: all for someone planning a session', 'Q8': 'PASS: the closure steps are the end\'s', 'Q9': 'PASS: one step a sentence'},
 'FNOJ': {'Q1': 'PASS: each sentence opens on its point', 'Q2': 'PASS: each don\'t is the helper\'s act', 'Q3': 'PASS: the items are named',
          'Q4': 'PASS: no term a reader wouldn\'t know', 'Q5': 'PASS: "So" after the role, "But" for the limit', 'Q6': 'PASS: the role, then its don\'ts, then later',
          'Q7': 'PASS: all for the helper now', 'Q8': 'PASS: the don\'ts are all about the person\'s experience', 'Q9': 'PASS: one don\'t a sentence'},
}
for n in ('SNOJ', 'FNOJ'):
    p = HERE / ('TEST-%s.receipt.json' % n)
    r = json.loads(p.read_text())
    for s in r['sentences']:
        e = EARLIER.get(s['s'])
        if e:
            s['payoff'], s['follows'] = e['payoff'], e['follows']
            if 'link' in s:
                s['link'] = e.get('link') or "none: the first sentence after its heading"
        else:
            pay, fol, link = NEW[s['s']]
            s['payoff'], s['follows'] = pay, fol
            if 'link' in s:
                s['link'] = link or "none: it stands in for the section's heading, after the base"
    r['placement'] = ('a test text: his Give the Session without his story, joke and aside' if n == 'SNOJ' else
                      'a test text: the Human base (the first five minutes to his reminder), then his anchor line and don\'ts without his guru picture and demon line')
    r['opens']['why_reading'] = ('it tells someone planning a session to think it through first' if n == 'SNOJ' else
                                 'it names what to do first when someone could get hurt in the next five minutes')
    r['same_point'] = 'none merged: a measurement of his version, one thing taken out'
    r['needed'] = {'reader': 'a fresh Haiku agent given tools/humanization/needed_read_brief.md with each text (NEEDED-READ.md)', 'unneeded': [], 'kept': {}}
    r['questions'] = Q[n]
    p.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
print('filled')
