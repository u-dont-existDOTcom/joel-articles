#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's narrowing tests of Who to Contact, and When (the
Human section, Psychological First Aid to the reminder, then the section's heading and one part with one sentence
changed).

The Human section's sentences are filled from h13's receipt of the same base (TEST-base-L1.receipt.json); the
section's from NEW below.

  python3 make_receipts.py NAME...     make and check TEST-base-NAME.receipt.json for each NAME
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
SR = REPO / 'tools/humanization/sense_receipt.py'
BASE = json.loads((HERE.parent / 'h13-20261106/TEST-base-L1.receipt.json').read_text())
OLD = {s['s']: s for s in BASE['sentences']}
HEAD = {'payoff': 'they know this part is for the person helping, and that the job is to be a calm anchor',
        'follows': "the next section's heading, after the reminder of where they are",
        'link': "none: a new section's heading; it opens the helper's part"}
NEW = {
    "A good sitter is not there to win a philosophy debate, perform a rescue fantasy, impose an interpretation, or demonstrate spiritual advancement.": (
        "they know what the sitter's job isn't", "the section's first point, under its heading", 'A good sitter'),
    "Zendo-style harm reduction puts it simply: make a safe space, and sit with them rather than guide them.": (
        "they know the first two things the sitter's job is, in Zendo's terms", "after what the job isn't, what it is", 'Zendo-style'),
    "Talk them through it, not down from it, and remember that difficult doesn't automatically mean bad.": (
        'they know the other two: talk them through, and difficult is not bad', 'the rest of the same list', 'Talk them through it'),
    "Stay present.": ('they know to stay with the person', "the paragraph's point, first", 'none: the paragraph\'s first sentence, its point, after the paragraph on grief'),
    "If it helps, you can say to yourself: This feeling is allowed to move through.": (
        'they have a phrase to steady themselves with', 'how to stay present', 'If it helps'),
    "I don't have to become it.": ('the phrase goes on: they needn\'t become the feeling', "the phrase's next line", 'it'),
    "I can love the part of me that feels it.": ('the phrase ends: they can love the part that feels it', "the phrase's last line", 'the part of me that feels it'),
    "Or simply: Can I send love to the one who's suffering?": ('they have a shorter phrase too', 'the other phrase, after the first', 'Or simply'),
    "A useful phrase is: This feeling is allowed to move through.": ('they have a phrase to steady themselves with', 'how to stay present', 'A useful phrase'),
    "Crying, grieving, remembering, or touching a genuine wound calls for loving awareness.": ('they know what to give someone in grief or pain', "the paragraph's point, first", 'none: a new paragraph on grief, after the sitter\'s job in Zendo\'s terms'),
    "As the sitter, you're not there to win a philosophy debate or play the rescuer, and you're not there to hand them your interpretation or show how spiritually advanced you are.": (
        "they know what the sitter's job isn't", "the section's first point, under its heading", 'As the sitter'),
    "Zendo-style harm reduction can be summarized as creating a safe space, sitting rather than guiding, talking through rather than down, and remembering that difficult does not automatically mean bad.": (
        "they know what the sitter's job is, in Zendo's terms", "after what the job isn't, what it is", 'Zendo-style'),
    "If they're crying, grieving, remembering something, or touching a real wound, what they need from you is loving awareness.": (
        'they know what to give someone in grief or pain', "the paragraph's point, first", 'If they'),
    "Interrogation, analysis every thirty seconds, and \"bro, you're purging ancestral karma\" while somebody white-knuckles the carpet are generally less helpful.": (
        'they know what not to do then', 'after what to give, what not to', 'Interrogation'),
    "Don't drag somebody out of real grief.": ('they know not to pull someone out of real grief', "the paragraph's first point", "Don't drag"),
    "Don't trap them inside a loop that is grinding them down either.": ('they know not to leave them stuck in a loop either', 'the other side of the same point', 'either'),
    "Don't drag somebody out of real grief, but don't leave them stuck in a loop that's grinding them down either.": (
        'they know to let grief be, but not to leave someone stuck in a loop', "the paragraph's point", "Don't drag"),
}
Q = {
    'Q1': 'PASS: each paragraph opens on its point: the first priority, the room fixes with their reason, what the reminder is for, then the anchor part\'s point',
    'Q2': "PASS: every act is the helper's own, with its purpose: the dangers removed, the lights dimmed and the extra people out because they're overwhelmed, the reminder because a trip can make them lose track; one calm person as the lead, a second as backup when it's more than one can hold",
    'Q3': 'PASS: which things exactly: keys, stove, roads, balconies, pools, weapons, the phone; the lights, the extra people; place, date and time, the substance; who leads and who backs up, and when',
    'Q4': 'PASS: no terms a reader would not know; "anchor" is the heading\'s word, said in the sentence as the calm person who leads',
    'Q5': 'PASS: each turn has what it turns on: since a trip makes them lose track; the opposite of alone is too many people; backup when one person cannot hold it',
    'Q6': 'PASS: dangers, room, what to say, then who should be with them',
    'Q7': 'PASS: every fact is about the person in front of them now',
    'Q8': 'PASS: the anchor part is one point, under its heading',
    'Q9': "PASS: nothing compressed: the reminder's facts one a sentence, as said aloud; the anchor part one step a sentence",
}
for name in sys.argv[1:]:
    text = HERE / ('TEST-base-%s.txt' % name)
    out = HERE / ('TEST-base-%s.receipt.json' % name)
    subprocess.run([sys.executable, str(SR), 'make', str(text), '--section',
                    'Psychological First Aid: The First Five Minutes, and For the Person Helping', '--reader',
                    'someone sitting with a person on a bad psychedelic trip, or tripping themselves, who needs to know what to do in the first five minutes, and how to help as a calm anchor',
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text())
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] == 'For the Person Helping: Calm Anchor, Not Guru':
            s.update(HEAD)
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        else:
            raise SystemExit('no entry for: %r' % s['s'])
    r['placement'] = ("Psychological First Aid to the reminder, then For the Person Helping's heading and one paragraph with one "
                      "sentence changed (a narrowing test)")
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next for the sitter's job, grief, staying present "
                       "and loops; the opening's partial overlaps with the Don't list are in humanize/h16-20261107/RESULTS.md")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
