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
HEAD = {'payoff': 'they know this part says whom to call, and when',
        'follows': "the next section's heading, after the reminder of where they are",
        'link': "none: a new section's heading; it opens the list of people and services to contact"}
NEW = {
    "Save the relevant links and local numbers before you need them.": ('they know to save the links and numbers ahead of time', "the section's first point, under its heading", 'before you need them'),
    "TripSit live chat: a harm-reduction chat you open in your browser, for people using drugs and for whoever's looking after them.": ('they know what TripSit offers and for whom', 'the next item in the same list', 'TripSit'),
    "Fireside Project: psychedelic peer support by phone or text at 623-473-7433, every day from 11 a.m. to 11 p.m.": ('they know what Fireside offers, how to reach it, and its hours', 'the first item under its heading', 'Fireside Project'),
    "Pacific Time; its FAQ says it's U.S.-only for now.": ('they know the hours are Pacific Time and that Fireside is U.S.-only', 'the end of the same item, split off at "p.m."', 'none: the end of the same item, split by the sentence counter at "p.m."'),
    "Find A Helpline: a worldwide list of free helplines, and many of them take calls, texts, online chat or WhatsApp.": ('they know what Find A Helpline is and how its helplines can be reached', 'the list item, under its heading', 'Find A Helpline'),
    "Any kind of crisis counts, and it can put a human on the other end quickly.": ('they know the helplines are for any crisis and fast to reach', 'what the helplines are for, after what they are', 'Any kind of crisis'),
    "Fireside Project: U.S.-only according to its current FAQ; phone or text psychedelic peer support at 623-473-7433, daily from 11 a.m. to 11 p.m.": ('they know who Fireside serves, how to reach it, and its hours', 'the first item under its heading', 'Fireside Project'),
    "Pacific Time.": ('they know the hours are Pacific Time', 'the end of the hours, split off at "p.m."', 'none: the end of the same item, split by the sentence counter at "p.m."'),
    "During or soon after a psychedelic experience": ('they know the first list is for during or just after a trip', 'a list heading, after the opening paragraph', 'During or soon after'),
    "Fireside Project: U.S.-only according to its current FAQ; phone or text psychedelic peer support at 623-473-7433, daily from 11 a.m. to 11 p.m. Pacific Time.": ('they know who Fireside serves, how to reach it, and its hours', 'the first item under its heading', 'Fireside Project'),
    "TripSit live chat: browser-based harm-reduction chat for people using drugs and the people supporting them.": ('they know what TripSit offers and for whom', 'the next item in the same list', 'TripSit'),
    "It is not psychedelic-specific, but it can put a human on the other end quickly.": ('they know the helplines are general and fast to reach', 'what the helplines are for, after what they are', 'It is not psychedelic-specific'),
    "U.S. crisis chat and text": ('they know the next list is U.S. crisis lines', 'a list heading, after the directories', 'U.S. crisis'),
    "988 Suicide & Crisis Lifeline: U.S. call, text, and chat for suicidal or mental-health crises.": ('they know what 988 is for and how to reach it', 'the first item under its heading', '988'),
    "Crisis Text Line: U.S. text, chat, and WhatsApp support, with partner text lines listed for Canada, the UK, and Ireland.": ('they know what Crisis Text Line offers, and where else it has partners', 'the next item in the same list', 'Crisis Text Line'),
    "Integration and post-experience support": ('they know the last list is for after the experience', 'a list heading, after the crisis lines', 'post-experience'),
    "ICEERS Support Center: up to five free online integration sessions for challenging experiences.": ('they know what ICEERS offers', 'the first item under its heading', 'ICEERS'),
    "CPEP online peer group: a free confidential monthly group for post-psychedelic difficulties.": ('they know what the CPEP group is', 'the next item in the same list', 'CPEP'),
    "Cheetah House: resources, consultations, and support groups for meditation-related difficulties, including chat-based peer support.": ('they know what Cheetah House offers, for meditation-related difficulties', 'the last item in the list', 'Cheetah House'),
    "Save the relevant links and local numbers before you need them.": (
        'they know to save the links and numbers ahead of time', "the section's first point, under its heading", 'before you need them'),
    "Save the links you'd use, and your local numbers, before you need them.": (
        'they know to save the links and numbers ahead of time', "the section's first point, under its heading", 'before you need them'),
    "Hours and services change, and not every option works in every country.": (
        'they know to check the hours and whether a service works where they are', 'the caveat for the list that follows', 'Hours and services'),
    "Their hours and services change, and some only work in one country.": (
        'they know to check the hours and whether a service works where they are', 'the caveat for the list that follows', 'Their hours'),
    "Global crisis and emotional-support directories": (
        'they know the next list is directories of crisis lines', 'a list heading, after the opening paragraph', 'directories'),
    "Find A Helpline: a global directory of free helplines, many offering phone, text, online chat, or WhatsApp.": (
        'they know what Find A Helpline is and how its helplines can be reached', 'the list item, under its heading', 'Find A Helpline'),
    "They're for any kind of crisis, and they can put a human on the other end quickly.": (
        'they know the helplines are general and fast to reach', 'what the helplines are for, after what they are', "They're for any kind of crisis"),
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
                    'Psychological First Aid: The First Five Minutes, and Who to Contact, and When', '--reader',
                    'someone sitting with a person on a bad psychedelic trip, or tripping themselves, who needs to know what to do in the first five minutes, and whom to contact',
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text())
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] == 'Who to Contact, and When':
            s.update(HEAD)
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        else:
            raise SystemExit('no entry for: %r' % s['s'])
    r['placement'] = ("Psychological First Aid to the reminder, then Who to Contact, and When's heading and one part with one "
                      "sentence changed (a narrowing test)")
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next for saving the numbers, the caveat and the "
                       "lists; its peer-support line, a repeat of the call-for-help part, is cut "
                       "(experiments/t19-anchor/apply_t19d.py)")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
