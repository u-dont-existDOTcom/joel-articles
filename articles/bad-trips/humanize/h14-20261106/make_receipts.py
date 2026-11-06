#!/usr/bin/env python3
"""make_receipts.py - the making-sense receipts for this folder's narrowing tests of Get One Human Anchor (the Human
section, Psychological First Aid to the reminder, then the section's heading and one part with one sentence changed).

The Human section's sentences are filled from h13's receipt of the same base (TEST-base-L1.receipt.json); the anchor
part's sentences from NEW below.

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
HEAD = {'payoff': 'they know the next step after the first five minutes: one calm person with them',
        'follows': "the next section's heading, after the reminder of where they are",
        'link': "none: a new section's heading; it opens the next step, who should be with them"}
NEW = {
    "If you're the one in the altered state, you can say or send something like this:": (
        'they know the words below are for the one in the altered state to say or send', 'under the heading: what the person can ask for',
        'the one in the altered state'),
    "And if you're the one sitting with them, you can say:": (
        'they know the words below are for the one helping', 'after the words for the person, the words for the helper',
        'And if'),
    "Please stay with me, speak slowly, remind me where I am, and help me not make any big decisions until tomorrow.": (
        'the helper hears the asks: stay, speak slowly, say where they are, no big decisions until tomorrow',
        'after what is not needed, what is', 'Please stay with me'),
    "So pick one calm person to be the anchor, and let them take the lead.": (
        'they know to pick one calm person to be the anchor and lead', 'what to do about both ways a trip gets worse', 'So'),
    "What works better is one calm person as the anchor, taking the lead.": (
        'they know what works better than either: one calm person as the anchor, leading',
        'the answer to both ways a trip gets worse', 'What works better'),
    "One calm person should be the anchor and lead, but one person can only handle so much.": (
        'they know one calm person should lead, and that one person has a limit',
        'the answer to both ways a trip gets worse, with its limit', 'One calm person'),
    "One person can only handle so much, though, between fatigue, logistics, keeping them safe, and any risk of violence or self-harm.": (
        'they see the limit of having one person, and what wears it down', 'the limit, straight after the one-person rule',
        'One person'),
    "When it's too much, bring in one more calm adult or a crisis professional to back them up.": (
        'they know to add a second person at that limit, as backup to the anchor', 'what to do at that limit',
        "When it's too much"),
    "Fatigue sets in, the logistics pile up, keeping them safe gets harder, or there's a risk of violence or self-harm.": (
        'they see what wears one person down', 'the limit said as what happens', 'Fatigue sets in'),
    "When that happens, bring in one more calm adult or a crisis professional to back them up.": (
        'they know to add a second person then, as backup to the anchor', 'what to do when it happens',
        'When that happens'),
    "If it gets to be more than one person can manage, get one more calm adult or a crisis professional to back them up, whether it's fatigue, the logistics, keeping them safe, or a risk of violence or self-harm.": (
        'they know when to add a second person, that the second person backs up the anchor, and the reasons it gets to be too much',
        'the exception to having one person', 'more than one person can manage'),
    "And if it gets to be too much for one person to handle, from fatigue or logistics or just keeping them safe, or because there's a risk of violence or self-harm, bring in one more calm adult or a crisis professional to back them up.": (
        'they know when to add a second person, and that the second person backs up the anchor',
        'the exception to having one person', 'too much for one person'),
    "One person can only handle so much, though.": (
        'they see the limit of having one person', 'the limit, straight after the one-person rule',
        'One person'),
    "When fatigue or logistics get to be too much, or keeping them safe does, or there's a risk of violence or self-harm, bring in one more calm adult or a crisis professional to back them up.": (
        'they know when to add a second person, and that the second person backs up the anchor',
        'what to do at that limit', 'too much'),
    "I'm tripping really hard right now, or something like it, and I need help getting grounded.": (
        'the helper hears what is happening and what is needed', "the script's first line, after its label",
        'I need help getting grounded'),
    "You don't need to fix my life.": (
        "the helper hears what isn't asked of them", 'after what is needed, what is not', "You don't need"),
    "Can you just stay with me and talk slowly, keep reminding me where I am, and help me not make any big decisions until tomorrow?": (
        'the helper hears the asks: stay, talk slowly, keep saying where they are, no big decisions until tomorrow',
        'after what is not needed, what is', 'Can you just'),
    "Hey, I'm here, and I'm staying.": (
        'the person hears first that someone is there and staying', "the script's first line, after its label",
        "I'm here"),
    "Let's just keep your body safe and keep it simple, okay?": (
        'the person hears what happens now: their body kept safe and things kept simple',
        "after what needn't be done, what will", "Let's just"),
    "So one calm person should be the anchor and take the lead.": (
        'they know one calm person should be the anchor and lead', 'what to do about both ways a trip gets worse', 'So'),
    "If keeping them safe gets to be more than one person can manage, because of fatigue, logistics, or a risk of violence or self-harm, bring in one more calm adult or a crisis professional to back them up.": (
        'they know when to add a second person, and that the second person backs up the anchor',
        'the exception to having one person', 'more than one person can manage'),
    "Pick one calm person as the anchor and let them lead.": (
        'they know to pick one calm person to be the anchor and lead', "the heading's act, said as what to do",
        'one calm person as the anchor'),
    "A second calm adult or a crisis professional comes in only as backup, when safety, fatigue, logistics, violence, or self-harm risk is more than one person can hold.": (
        'they know a second person backs the anchor up, and when to bring one in', 'the exception to having one person',
        'A second calm adult'),
    "I'm having a really intense trip, or something like one, and I need help getting grounded.": (
        'the helper hears what is happening and what is needed', "the script's first line, after its label",
        'I need help getting grounded'),
    "You don't have to fix my life.": (
        "the helper hears what isn't asked of them", 'after what is needed, what is not', "You don't have to"),
    "Just stay with me and talk slowly, and keep reminding me where I am.": (
        'the helper hears the first asks: stay, talk slowly, keep saying where they are', 'after what is not needed, what is',
        'Just stay with me'),
    "And help me hold off on any big decisions until tomorrow.": (
        'the helper hears the last ask: no big decisions until tomorrow', 'the last ask, after the others', 'And help me'),
    "I'm right here, and I'm not going anywhere.": (
        'the person hears first that someone is there and staying', "the script's first line, after its label",
        "I'm right here"),
    "Let's just keep your body safe and keep it simple.": (
        'the person hears what happens now: their body kept safe and things kept simple',
        "after what needn't be done, what will", "Let's just"),
    "So have one calm person be the anchor, and let them take the lead.": (
        'they know to pick one calm person to be the anchor and lead', 'what to do about both ways a trip gets worse',
        'So'),
    "When safety, fatigue, logistics, violence, or self-harm risk exceeds what one person can hold, bring in one additional calm adult or crisis professional.": (
        'they know when to add a second person', 'the exception to having one person', 'what one person can hold'),
    "That is backup.": (
        'they know the second person backs up the lead and does not replace it', 'what the second person is for',
        'That'),
    "When it's more than one person can handle, because of safety, fatigue, logistics, violence, or self-harm risk, bring in one additional calm adult or crisis professional.": (
        'they know when to add a second person', 'the exception to having one person', 'more than one person can handle'),
    "They're there as backup, and the anchor still leads.": (
        'they know the second person backs up and the anchor keeps leading', 'what the second person is for',
        "They're there"),
    "I'm here.": (
        'the person hears first that someone is there', "the script's first line, after its label", "I'm here"),
    "You're not alone.": (
        'the person hears they are not alone with it', "after hearing someone's there", 'not alone'),
    "Let's just get your body safe and keep it simple, and I'm staying with you.": (
        'the person hears what happens now: their body safe, things simple, and the helper staying',
        "after what needn't be done, what will", "Let's just"),
    "Script for the person in the altered state:": (
        'they know the words below are for the one in the altered state to say', 'under the heading: what the person can ask for',
        'the person in the altered state'),
    "I'm in an intense psychedelic or altered state and I need grounding.": (
        'the helper hears what is happening and what is needed', "the script's first line, after its label",
        'I need grounding'),
    "I don't need you to solve my life.": (
        "the helper hears what isn't asked of them", 'after what is needed, what is not', "I don't need you"),
    "Please stay with me and talk slowly, and keep reminding me where I am.": (
        'the helper hears the first asks: stay, talk slowly, keep saying where they are', 'after what is not needed, what is',
        'Please stay with me'),
    "Help me not make any big decisions until tomorrow.": (
        'the helper hears the last ask: no big decisions until tomorrow', 'the last ask, after the others',
        'Help me'),
    "Many bad trips get worse because somebody is alone with a frightened or over-certain mind.": (
        'they see why a person on a bad trip needs someone with them', "the section's first point, under its heading",
        'alone'),
    "Other times it's the opposite: too many people crowd in and start advising, arguing, spiritualizing, or panicking.": (
        'they see that too many people make it worse too, so it should be one person', 'the opposite case to being alone',
        "Other times it's the opposite"),
    "Being alone with a frightened or over-certain mind makes a lot of bad trips worse.": (
        'they see why a person on a bad trip needs someone with them', "the section's first point, under its heading",
        'alone'),
    "Others get worse because too many people crowd in and start advising, arguing, spiritualizing, or panicking.": (
        'they see that too many people make it worse too, so it should be one person', 'the other way a trip gets worse',
        'Others get worse'),
    "Use one calm human anchor as the lead.": (
        'they know to pick one calm person to lead', "the heading's act, said as what to do", 'one calm human anchor'),
    "When safety, fatigue, logistics, violence, or self-harm risk exceeds what one person can hold, bring in one additional calm adult or crisis professional as backup.": (
        'they know when to add a second person, and that the second person backs up the lead',
        'the exception to having one person', 'what one person can hold'),
    "Script for the sitter or friend:": (
        'they know the words below are for the one helping', 'under the heading: what the anchor says',
        'sitter or friend'),
    "I'm here with you.": (
        "the person hears first that someone is there with them", "the script's first line, after its label",
        'with you'),
    "This is a wave.": (
        'the person hears that it will pass', 'after hearing someone is with them',
        "none: the script's next line, said aloud to the person; it tells them the fear will pass"),
    "We don't have to solve your whole life right now.": (
        'the person hears that nothing has to be worked out now', 'after hearing it will pass', 'right now'),
    "Let's make your body safe, keep things simple, and stay together.": (
        'the person hears what happens now: a safe body, simple things, together', "after what needn't be done, what will",
        "Let's"),
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
                    'Psychological First Aid: The First Five Minutes, and Get One Human Anchor', '--reader',
                    'someone sitting with a person on a bad psychedelic trip, or tripping themselves, who needs to know what to do in the first five minutes, and then who should be with them',
                    '--out', str(out)], check=True, capture_output=True)
    r = json.loads(out.read_text())
    for s in r['sentences']:
        if s['s'] in OLD:
            for k in ('payoff', 'follows', 'link'):
                if k in OLD[s['s']]:
                    s[k] = OLD[s['s']][k]
        elif s['s'] == 'Get One Human Anchor':
            s.update(HEAD)
        elif s['s'] in NEW:
            s['payoff'], s['follows'], s['link'] = NEW[s['s']]
        else:
            raise SystemExit('no entry for: %r' % s['s'])
    r['placement'] = ("Psychological First Aid to the reminder, then Get One Human Anchor's heading and one of its parts with "
                      "one sentence changed (a narrowing test)")
    r['opens']['why_reading'] = BASE['opens']['why_reading']
    r['same_point'] = ("none: read the section from its heading to the next for being alone, too many people, one calm "
                       "lead with a backup, and the two scripts; the committee line, which said again the first "
                       "paragraph, is cut (experiments/t19-anchor/apply_t19.py)")
    r['questions'] = Q
    out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
    c = subprocess.run([sys.executable, str(SR), 'check', str(text), str(out)], capture_output=True, text=True)
    print(name, (c.stdout + c.stderr).strip().splitlines()[-1])
