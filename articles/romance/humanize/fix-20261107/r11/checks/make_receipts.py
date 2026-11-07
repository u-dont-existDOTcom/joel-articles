#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r11's checks (texts.py). Every sentence has its row: the live post's sentences
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
FLAWS = 'Someone getting to know a new partner, deciding what to tell them about their own flaws and what to ask.'
R = {
    'r11-dam': ('Holding up a leaky dam', DAM, 'It tells the reader attachment turns a chance into certainty, which they may be feeling now.', [
        ('once attached, a chance becomes "she’s the right person"', 'opens the section', None),
        ('he asks what that certainty rests on', 'the challenge to it', 'Based on what?'),
        ('sometimes he learned something, sometimes only got attached, which makes it hard to question', 'the two answers',
         'Sometimes I actually learned something'),
        ('quick sex is a reason not to move in quickly too', 'what follows for him from that', 'If I have sex with somebody quickly'),
        ('moving in right away is a common-law marriage without discussing it', 'why moving in waits',
         'Moving in together right away'),
        ('being entangled can pass for the relationship going well', 'the risk in it', 'It’s too easy'),
        ('so keep friends, a community, and dates to check how it’s going', 'what he wants because of that', 'So I want us'),
        ('he can know he wants her long before knowing about children, community or a life together',
         'why the slower questions need time', 'I can know I want her much faster'),
        ('one of you will ask why they are special', 'the question that will come', 'At some point one of you will ask'),
        ('why you and not somebody else', 'the same question again', 'Why are you with me'),
        ('the answer may be only sex and getting hitched', 'the answer he fears', 'If the answer is basically'),
        ('that answer is a damn shame', 'his verdict on that answer', 'that’s a damn shame'),
    ]),
    'r11-s22b': ('After leaving', AFTER, 'It tells the reader they can see now what they couldn’t while bonded.', [
        ('once out, you can see what you couldn’t while bonded', 'opens the paragraph', None),
        ('look at your own part', 'the first thing to look at', 'Look at what you contributed'),
        ('understand what was true on your ex’s side, their inner conflicts included, and don’t make them a cartoon villain',
         'the other side to look at', 'Try to understand whatever was true'),
    ]),
    'r11-sit': ('Situationships', SIT, 'It tells the reader what a situationship is, the kind they may be in.', [
        ('a situationship is hard to define, which is the point', 'opens the section', None),
        ('it is usually a happenstance relationship based on sex', 'what it usually is', 'Usually it’s a happenstance'),
        ('there is less communication, and it is more superficial', 'how it differs', 'There’s less communication'),
        ('it is clearly a relationship even when someone refuses to name it', 'yet what it is', 'Yet it is obviously'),
        ('you have sex, go out and spend time alone, as you wouldn’t with a friend', 'the evidence for that',
         'You’re regularly having sex'),
        ('it fills the void only by accident and sometimes, maybe enough to stop you looking deeper', 'what it does for you',
         'It feels like it’s filling'),
        ('either side can be the one keeping it undefined', 'who wants what', 'It can go either way'),
        ('often the man wants it undefined and the woman commitment, since she risks pregnancy', 'the usual case',
         'Often the man wants'),
        ('the one who keeps it undefined gets fun without responsibility, yet the responsibility stays', 'what that one gets',
         'Whoever keeps it undefined'),
        ('they don’t escape the void another superficial fix creates either', 'what they don’t escape', 'They don’t escape'),
        ('doomscrolling entertains you too', 'the comparison that sums it up', 'Doomscrolling entertains you too'),
        ('"Why are you making this heavy?" can be a real question', 'what the other person may ask',
         'And “Why are you making this heavy?”'),
        ('they may mean: don’t you want the fun, are you giving it up?', 'what that question means', 'They may actually mean'),
        ('his answer: he is checking whether it fulfils him or drains him', 'his answer to it', 'My answer would be'),
        ('he had something like it with H., but much deeper', 'his own case', 'I had something sort of like that with H.'),
        ('they were and are best friends, together nearly all the time', 'how close they were', 'We were (and still are) BFFs'),
        ('she fell in love with him and he didn’t with her', 'what happened between them', 'She was falling in love with me'),
        ('she felt like a sister to him, partly as he isn’t attracted to white women', 'why he didn’t',
         'She felt more like a sister'),
        ('theirs was not superficial, only painfully uneven', 'his verdict on it', 'Ours wasn’t superficial'),
    ]),
    'r11-clar': ('The window of clarity, and how it closes', CLAR, 'It tells the reader when the window of objectivity closes for him, which may be soon for them.', [
        ('for him the window of objectivity closes once sex seems sure soon', 'opens the section', None),
        ('he idealizes her more and after sex may feel unable to leave', 'what happens to him then',
         'I begin idealizing her more'),
        ('he may not be representative of modern casual dating', 'who this may not fit', 'Maybe I’m not representative'),
        ('if you are numb to casual sex, the window may close later or never', 'how it may differ for others',
         'If you’re quite numb'),
        ('for him this is the pattern, healthy in a healthy small society', 'his pattern all the same',
         'But for me, this is the pattern'),
        ('the attachment part comes from his experience and his reading', 'where this comes from', 'The attachment theory part'),
        ('sex turns on bonding chemistry that biases us toward attachment', 'what the reading says',
         'Sex turns on bonding chemistry'),
        ('oxytocin is called the love hormone, but you can get more attached and more freaked out at once',
         'what the chemistry can do', 'People call oxytocin'),
        ('if closeness was safe in childhood, it may feel like coming home', 'when it feels good', 'If closeness was safe'),
        ('if it came with neglect, abuse or people disappearing, you may get anxious or suspicious', 'when it feels bad',
         'But if it came with neglect'),
        ('you might feel worthless or go into fight or flight', 'what else can happen', 'You might feel worthless'),
        ('Helen Fisher’s research names types of brain chemistry that shape attraction', 'the second piece of the reading',
         'There are several main types'),
    ]),
    'r11-flaws': ('My flaws', FLAWS, 'It tells the reader his own flaws, the kind of list they may need to give.', [
        ('his list is not flattering: impulsive, idealizing but not demonizing', 'opens the section', None),
        ('he is very open and not private', 'the next flaw', 'I’m very open'),
        ('he cares more about honesty than the romantic ideal', 'the next flaw', 'I care more about honesty'),
        ('he still loves his exes', 'the next flaw', 'I still love my exes'),
        ('after deep love his expectations are high, so a basic relationship won’t please him', 'the last flaw',
         'After being deeply in love'),
        ('he is unique, with convictions many won’t share', 'what else she should know', 'I’m also extremely unique'),
        ('he is anti-vax, anti-money, anti-civilization, and not yet living as he wants', 'which convictions',
         'I’m anti-vax'),
        ('a woman should know that before fitting him into her plans', 'why he says it', 'A woman should know that'),
        ('Key was an inner-child therapist and Reiki healer', 'his exes as an example', 'Key was an inner-child therapist'),
        ('Key and Bee were curious and open-minded, which he loved', 'what he loved in them', 'Both Key and Bee'),
        ('they were open to spiritual experience and childlike wonder and worked on themselves', 'more of what he saw',
         'They were open to spiritual'),
        ('they both meditated a lot', 'one more thing he saw', 'They both meditated a lot'),
        ('he assumed such depth meant they were far along the path', 'what he concluded', 'I saw all that'),
        ('that was his mistake', 'his verdict on it', 'That was my mistake'),
        ('their meditations may have helped them', 'what was true in it', 'Their meditations may have helped'),
        ('he still didn’t know how they would act when it got ugly', 'what it didn’t tell him', 'I still had no idea'),
        ('with enough trauma, huge progress can leave much unresolved', 'why it didn’t', 'If somebody starts with enough trauma'),
        ('his blind spot is reading where people are emotionally', 'his own blind spot', 'My own blind spot'),
        ('a partner may agree, then later say she was fawning', 'how it shows', 'A partner may agree'),
        ('no, he really didn’t understand', 'his answer to her', 'No, I really didn’t'),
        ('if you are fawning, tell him, since he can’t read your mind', 'what he asks of the reader', 'If you’re fawning'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s, with the moves named in texts.py (176’s reason before its list; the oxytocin '
          'paragraph’s point in its first sentence)',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
LOW = [{'point': 'the Low windows’ points', 'found': 'the live post (../../live-check/LOW-WINDOWS.json)',
        'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
AI = [{'point': 'the AI window’s point', 'found': 'the live post (../../live-check/AI-WINDOWS.json)',
       'still_needed': 'yes: the section needs it', 'fate': 'changed'}]
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
    r['checked'] = AI if name == 'r11-s22b' else LOW
    r['placement'] = ('The paragraph by itself, in its place in the live post, for the section gate (E343).' if name == 'r11-s22b'
                      else 'The whole section, in its place in the live post, its heading left out.')
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
