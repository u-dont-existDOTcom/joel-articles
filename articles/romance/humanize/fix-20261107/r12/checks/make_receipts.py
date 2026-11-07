#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r12's checks (texts.py). Every sentence has its row: the live post's sentences
as well as mine, since the article's published text is not only his own words (gate E373).
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

DAM = 'Someone a few weeks into a relationship, deciding whether their growing certainty about the person is earned.'
AFTER = 'Someone just out of a relationship, deciding what to tell people and how to see their ex.'
SIT = 'Someone in a relationship that is mostly sex and has no name, deciding whether to ask what it is.'
CLAR = 'Someone close to having sex with a new person, deciding what to find out before the bond clouds their view.'
PEEK = 'Someone dating a new person, deciding how to find out whether they are compatible before the bond clouds it.'
TRICKY = 'Someone in a new relationship, noticing they see their friends less and deciding who to talk to about it.'
R = {
    'r12-s22': ('After leaving', AFTER, 'It tells the reader the aftermath is worse than the breakup, the stretch they may be in.', [
        ('the breakup is hard, the aftermath worse', 'opens the section', None),
        ('avoid public demonization, but don’t hide the truth to save face', 'the first advice', 'Public demonization'),
        ('sometimes the truth is abuse, coercion or serious deception', 'what the truth can be', 'Sometimes the truth'),
        ('how much you say, to whom and how publicly depend on what happened and why you tell', 'how to tell it',
         'So how much you say'),
        ('once out, you can see what you couldn’t while bonded', 'what changes after leaving', 'Once you’re out'),
        ('look at your own part', 'the first thing to look at', 'Look at what you contributed'),
        ('understand what was true on your ex’s side, their inner conflicts included, and don’t make them a cartoon villain',
         'the other side to look at', 'Try to understand whatever was true'),
        ('the easiest story is that they were fake, since it explains everything', 'the story that tempts',
         'Sometimes the easiest story'),
        ('take that story only if it is really the simplest explanation', 'what to do about it', 'Grab it only if'),
        ('people not heavily invested in your innocence can help: a therapist, pastor or stranger may see more clearly',
         'who can help check it', 'People who aren’t heavily invested'),
        ('the curiosity itself can heal', 'what the checking gives you', 'Even the curiosity'),
        ('spiritual practice matters in an ending, but not to skip the feelings', 'the next advice',
         'Spiritual practice during an ending'),
        ('pray for your ex’s wellbeing', 'the first practice', 'Pray for your ex’s wellbeing'),
        ('remember what was real and good, and don’t let pain license hate', 'the next practice',
         'Remember what was real and good'),
        ('avoid the New Age belief that everyone mirrors you', 'a belief to avoid', 'Avoid the New Age belief'),
        ('that belief isn’t true', 'his answer to it', 'No, that isn’t true'),
        ('we partly mirror each other, but much in each person has nothing to do with you', 'why it isn’t',
         'We partly mirror one another'),
        ('the Buddha’s cousin still tried to kill him', 'his example', 'No matter how enlightened the Buddha was'),
        ('owning your part doesn’t erase theirs', 'what the example shows', 'Looking honestly at your part'),
        ('asking what Mr. Rogers would do can help', 'a question that helps', 'Sometimes it helps to ask'),
        ('public demonization needn’t be the last chapter', 'what he learned after', 'I also learned'),
        ('avoiding contact forever may keep them from apologizing and learning honesty', 'why not forever',
         'If you avoid contact forever'),
        ('distance for a while helps until cooler heads prevail', 'what helps instead', 'But it can help to keep distance'),
        ('an apology tempts you to let them back, but you deserve a stable love', 'the risk after an apology',
         'It can be tempting'),
        ('you’re not a yo-yo', 'his closing line', 'You’re not a yo-yo'),
    ]),
    'r12-dam': ('Holding up a leaky dam', DAM, 'It tells the reader attachment turns a chance into certainty, which they may be feeling now.', [
        ('once attached, a chance becomes "she’s the right person"', 'opens the section', None),
        ('he asks what that certainty rests on', 'the challenge to it', 'Based on what?'),
        ('sometimes he learned something, sometimes only got attached, which makes it hard to question', 'the two answers',
         'Sometimes I actually learned something'),
        ('quick sex is a reason not to move in quickly too', 'what follows for him from that',
         'If I have sex with somebody quickly'),
        ('moving in right away is an undiscussed common-law marriage, and being entangled passes for going well',
         'his two reasons', 'Moving in together right away'),
        ('so he wants friends and a community around them, and dates to check how it’s going',
         'what he wants because of that', 'So I want us'),
        ('he can know he wants her long before knowing about children, community or a life together',
         'why the slower questions need time', 'I can know I want her much faster'),
        ('one of you will ask why they are special', 'the question that will come', 'At some point one of you will ask'),
        ('why you and not somebody else', 'the same question again', 'Why are you with me'),
        ('the answer may be only sex and getting hitched', 'the answer he fears', 'If the answer is basically'),
        ('that answer is a damn shame', 'his verdict on that answer', 'that’s a damn shame'),
    ]),
    'r12-sit33': ('Situationships', SIT, 'It tells the reader what a situationship is, the kind they may be in.', [
        ('a situationship is hard to define, which is the point', 'opens the section', None),
        ('it is usually a happenstance relationship based on sex', 'what it usually is', 'Usually it’s a happenstance'),
        ('there is less communication, and it is more superficial', 'how it differs', 'There’s less communication'),
        ('it is clearly a relationship even when someone refuses to name it', 'yet what it is', 'Yet it is obviously'),
        ('you have sex and spend time as you wouldn’t with a friend, so it fills the void only by accident, maybe enough '
         'to stop you looking deeper', 'the evidence and what it does', 'You’re regularly having sex'),
    ]),
    'r12-sit34': ('Situationships', SIT, 'It tells the reader either side can keep it undefined, which may be them.', [
        ('either side can be the one keeping it undefined', 'opens the paragraph', None),
        ('often the man wants it undefined and the woman commitment, since she risks pregnancy', 'the usual case',
         'Often the man wants'),
        ('if you keep it undefined, you get the fun without the responsibility', 'what the one keeping it gets',
         'If you’re the one keeping it undefined'),
        ('not naming it doesn’t make the responsibility disappear, nor the void of another superficial fix',
         'what that one doesn’t escape', 'Refusing to name the relationship'),
        ('doomscrolling entertains you too', 'the comparison that sums it up', 'Doomscrolling entertains you too'),
    ]),
    'r12-clar108': ('The window of clarity, and how it closes', CLAR, 'It tells the reader the "love hormone" may not feel like love to them.', [
        ('oxytocin is called the love hormone, as if attachment should feel safe', 'opens the paragraph', None),
        ('if childhood closeness was safe it may feel like home, if not you can get more attached and more freaked out '
         'at once', 'the two cases', 'If closeness was safe'),
        ('you might get anxious or suspicious', 'what that can look like', 'You might get anxious'),
        ('you might feel worthless or go into fight or flight', 'what else can happen', 'You might feel worthless'),
    ]),
    'r12-peek': ('Peeking thru the window', PEEK, 'It tells the reader the main thing to find out before the window closes.', [
        ('before the window closes, find out whether you are compatible', 'opens the section', None),
        ('do you share goals and values on children, religion, politics, health, love and romance?', 'the first question',
         'Do you have the same goals'),
        ('where do you want to live?', 'the next question', 'Where do you want to live'),
        ('do you both want a community?', 'the next question', 'Do you both want to find a community'),
        ('what relationship do you want with technology and money?', 'the next question', 'What kind of relationship'),
        ('ask deep questions', 'how to find out', 'Ask deep questions'),
        ('card games may seem silly but get you past small talk', 'a way to ask them', 'Conversation-card games'),
        ('asking how she handles jealousy gets a beautiful, empty answer', 'where questions fail', 'But asking'),
        ('he would rather ask what she would do in a real situation', 'what he asks instead', 'I’d rather ask'),
        ('a general answer tells him she doesn’t know yet', 'how he reads the answer', 'If all she can give me'),
        ('a card game makes its own little high', 'a risk in the games', 'A card game can create'),
        ('two hours of secrets can feel close, but it shows only the game worked, not the relationship',
         'what the high means', 'If we spend two hours'),
        ('take them to a party, your family or friends, and your activities, and watch', 'another way to find out',
         'You can also bring the person'),
        ('do your usual day with them and see how it feels', 'one more way', 'Try doing what you would normally do'),
        ('is it weird?', 'the first thing to notice', 'Is it weird?'),
        ('do they wonder why you do this?', 'the next thing to notice', 'Are they wondering'),
        ('do they look bored, wanting to see you later instead?', 'the next thing to notice', 'Do they look bored'),
        ('can you be normal together, not just romantic?', 'the last thing to notice', 'Can you guys be normal'),
        ('see their negative side first too', 'what else to see early', 'See their negative side first too'),
        ('no negative side is a red flag for fakery', 'why it matters', 'If there is no negative side'),
        ('test whether their spiritual story survives a bad afternoon', 'a test for it', 'Ask whether the spiritual story'),
        ('how recent is their healing story?', 'a question for it', 'How recent is the healing story'),
        ('jealousy, abandonment, possessiveness and the better-than-before story show only under stress',
         'when the negative side shows', 'Jealousy, abandonment, possessiveness'),
        ('by then you are stressed and entangled', 'the catch in that', 'By then, of course'),
        ('sometimes all he has is a little "wait" feeling', 'his own signal', 'Sometimes the only thing I have'),
        ('the feeling proves nothing', 'what it is worth', 'It doesn’t prove anything'),
        ('if he is about to skip a question because he wants it to work, he asks it', 'what he does with it',
         'But if I’m about to ignore a question'),
        ('if they are nasty to others, they will be to you', 'a warning sign', 'If they’re nasty to their friends'),
        ('we are drawn to the inner child because ours wants fun', 'why we miss it', 'We mostly seem to get attracted'),
        ('find out whether a healthy adult is there before you are too bonded', 'what to find out',
         'But you also need to find out'),
    ]),
    'r12-tricky': ('Things get tricky fast', TRICKY, 'It tells the reader couples pull away from friends, which they may be doing.', [
        ('couples withdraw from unsupportive friends and stop telling them the truth', 'opens the section', None),
        ('sharp questions start to feel rude', 'what follows', 'Sharp questions start to feel rude'),
        ('problems dissolve into "but I love her", and the relationship’s small world feels more real, right when an '
         'outside view is most needed', 'where it ends up', 'An obvious problem dissolves'),
        ('withdrawing can be right: complaining about your girlfriend can violate her privacy', 'the other side of it',
         'Sometimes withdrawing isn’t wrong'),
        ('the point is to realize what is happening', 'what matters then', 'It’s just important to realize'),
        ('each telling their own friends doesn’t help, so we need people who know both of us over time', 'what does help',
         'It doesn’t help if she tells'),
        ('he will come back to that', 'a pointer ahead', 'I’ll come back to that'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s; the joins named in texts.py keep it',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
LOW = [{'point': 'the Low windows’ points', 'found': 'the live post (../../live-check/LOW-WINDOWS.json)',
        'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
AI = [{'point': 'the AI windows’ points', 'found': 'the live post (../../live-check/AI-WINDOWS.json and #47)',
       'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
PARA = ('r12-sit33', 'r12-sit34', 'r12-clar108')
bad = 0
for name, text in TEXTS.items():
    section, reader, why, rows = R[name]
    r = S.make(text, section, reader)
    assert len(r['sentences']) == len(rows), (name, len(r['sentences']), len(rows))
    for s, (pay, fol, link) in zip(r['sentences'], rows):
        s['payoff'], s['follows'] = 'the reader learns ' + pay, fol
        if 'link' in s:
            s['link'] = link
    r['opens']['why_reading'] = why
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = AI if name == 'r12-s22' else LOW
    r['placement'] = ('The paragraph by itself, in its place in the live post, for the section gate (E343).' if name in PARA
                      else 'The whole section, in its place in the live post, its heading left out.')
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
