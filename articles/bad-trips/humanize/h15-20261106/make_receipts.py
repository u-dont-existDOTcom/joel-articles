#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's narrowing tests of Alone at 3 a.m. (the Human
section, Psychological First Aid to the reminder, then the section with one sentence changed).

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
HEAD = {'payoff': 'they know this part is for someone on their own in the middle of the night',
        'follows': "the next section's heading, after the reminder of where they are",
        'link': "none: a new section's heading; it opens the case of being alone at night"}
NEW = {
    "The triage app has the stripped-down 3 a.m. plan.": (
        'they know where the short plan for this is', "the section's first point, under its heading", '3 a.m.'),
    "If you're on your own at 3 a.m., the triage app has a stripped-down plan for it.": (
        'they know where the short plan for being alone at night is', "the section's first point, under its heading",
        'on your own at 3 a.m.'),
    "Once the lamp is on, the keys are away, and \"No big actions until morning\" is visible, use the phone only to reach a calm person or support service.": (
        'they know what the phone is for once the room is safe', "after the plan, its steps done, what's next",
        'Once'),
    "Once you've got a lamp on, the keys put away and \"No big actions until morning\" written up where you can see it, only use the phone to reach a calm person or a support service.": (
        'they know what the phone is for once the room is safe', "after the plan, its steps done, what's next",
        'Once'),
    "Send the human-anchor script.": (
        'they know what to send the calm person', 'what to send, once they reach someone', 'human-anchor'),
    "When the body still needs movement, keep it contained and boring: brush your teeth, stretch gently, take a calm shower, or do a few slow wall push-ups.": (
        'they know how to move without making it worse', 'after reaching someone, what to do with the body',
        'When the body still needs movement'),
    "When the body still needs movement, keep it contained and boring: brush your teeth, stretch gently, take a calm shower, or do a few slow wall push-ups, and then try to get some sleep.": (
        'they know how to move without making it worse, and that sleep comes after', 'after reaching someone, what to do with the body',
        'When the body still needs movement'),
    "Then protect sleep.": (
        'they know sleep comes next', 'the last step, after moving', 'Then'),
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
                    'Psychological First Aid: The First Five Minutes, and Alone at 3 a.m.', '--reader',
                    'someone sitting with a person on a bad psychedelic trip, or tripping themselves, who needs to know what to do in the first five minutes, and what to do if they are alone at night',
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text())
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] == 'Alone at 3 a.m.':
            s.update(HEAD)
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        else:
            raise SystemExit('no entry for: %r' % s['s'])
    r['placement'] = ("Psychological First Aid to the reminder, then Alone at 3 a.m. with one sentence changed (a narrowing "
                      "test)")
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next for the triage plan, the phone, the script, "
                       "moving and sleep; its repeats of Stillness or Movement? and of the services are cut "
                       "(experiments/t19-anchor/apply_t19c.py, apply_t19d.py)")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
