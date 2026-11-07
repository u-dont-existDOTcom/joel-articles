#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r13's checks (texts.py). Every sentence has its row: the live post's sentences
as well as mine, since the article's published text is not only his own words (gate E373).
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402


def rows_of(rnd, key):
    spec = importlib.util.spec_from_file_location('m' + rnd, str(HERE.parents[1] / rnd / 'checks' / 'make_receipts.py'))
    src = (HERE.parents[1] / rnd / 'checks' / 'make_receipts.py').read_text(encoding='utf-8')
    ns = {}
    exec(src.split('\nQ = {')[0].split('import sense_receipt as S')[1].split('\n', 1)[1].replace('from texts import TEXTS  # noqa: E402', ''), ns)
    return ns['R'][key]


R12S22 = rows_of('r12', 'r12-s22')
R12DAM = rows_of('r12', 'r12-dam')
R11CLAR = rows_of('r11', 'r11-clar')
s22 = list(R12S22[3])
s22[6] = ('don’t make your ex a cartoon villain: understand what was true on their side, their inner conflicts included',
          'the other side to look at', 'And don’t turn your ex')
s22[17:19] = [('the Buddha’s cousin still tried to kill him: owning your part doesn’t erase theirs', 'his example and its lesson',
               'No matter how enlightened the Buddha was')]
dam = list(R12DAM[3])
dam[3:6] = [('quick sex is a reason not to move in quickly, and to keep friends, a community and dates to check how it’s going',
             'what follows for him from that', 'If I have sex with somebody quickly'),
            ('moving in right away is an undiscussed common-law marriage, and being entangled passes for going well',
             'his two reasons', 'Moving in together right away')]
clar = list(R11CLAR[3])
clar[7:11] = [('oxytocin is called the love hormone, as if attachment should feel safe', 'what the reading says next',
               'People call oxytocin'),
              ('if childhood closeness was safe it may feel like home, if not you can get more attached and more freaked out '
               'at once', 'the two cases', 'If closeness was safe'),
              ('you might get anxious or suspicious', 'what that can look like', 'You might get anxious'),
              ('you might feel worthless or go into fight or flight', 'what else can happen', 'You might feel worthless')]
SIT = 'Someone in a relationship that is mostly sex and has no name, deciding whether to ask what it is.'
PTSD = 'Someone who falls in love fast, deciding how far to trust a new partner who idealizes them.'
SLOW = 'Someone taking a relationship slowly, deciding whether that will tell them enough before sex.'
DISC = 'Someone whose partner’s moods drag them down, deciding who to talk to and how to calm their body.'
R = {
    'r13-s22': (R12S22[0], R12S22[1], R12S22[2], s22),
    'r13-dam': (R12DAM[0], R12DAM[1], R12DAM[2], dam),
    'r13-clar': (R11CLAR[0], R11CLAR[1], R11CLAR[2], clar),
    'r13-sit34': ('Situationships', SIT, 'It tells the reader who usually keeps it undefined, which may be them or their partner.', [
        ('either side can keep it undefined, but often it is the man, since she risks pregnancy', 'opens the paragraph', None),
        ('the one keeping it undefined gets the fun without the responsibility', 'what that one gets',
         'Whoever keeps it undefined'),
        ('not naming the relationship doesn’t make the responsibility disappear', 'what stays all the same',
         'Refusing to name the relationship'),
        ('they don’t escape the void another superficial fix creates', 'what they don’t escape', 'What they don’t escape'),
        ('doomscrolling entertains you too', 'the comparison that sums it up', 'Doomscrolling entertains you too'),
    ]),
    'r13-ptsd': ('Anti-PTSD Can Be Just As Dangerous As PTSD', PTSD, 'It tells the reader he sees only the love angle when in love, as they may.', [
        ('in love, he sees everything from the love angle', 'opens the section', None),
        ('he should admit that before giving advice', 'why he says it', 'I should probably admit that'),
        ('he told a friend he has "anti-PTSD"', 'where the term came from', 'A friend in my TherapyCircle chat'),
        ('anti-PTSD feels nice but leaves him more at risk than PTSD would', 'what it costs him', 'I coined it as a joke'),
        ('he expects each new woman to be the beautiful exception', 'what it looks like', 'Instead of expecting danger'),
        ('he sees the good', 'one part of it', 'I see the good'),
        ('he gives the benefit of the doubt too long', 'another part of it', 'I give the benefit of the doubt'),
        ('then the old pattern returns and gives him real PTSD', 'how it ends', 'Then the false positive resolves'),
        ('his parents taught him to assume the best of everybody', 'where it comes from', 'I grew up assuming the best'),
        ('now he tries to check for red flags before being alone with someone', 'what he does now',
         'Now I’m trying to be more suspicious'),
        ('why does she contact him only sometimes?', 'the first question he asks', 'Why does she contact me only sometimes'),
        ('what is the pattern?', 'the next question', 'What’s the pattern'),
        ('is she communicating enough to show her interest?', 'the next question', 'Is she communicating enough'),
        ('would his twin flame act like this?', 'his own question', 'Would my twin flame behave like this'),
        ('that is his question', 'whose question it is', 'That’s my question'),
        ('not everyone wants someone who channels the divine', 'why it is his', 'Not everybody is searching'),
        ('his second marriage to Bee is the clearest example', 'his example', 'My second marriage to Bee'),
        ('within a week he knew she saw him as her father', 'what he saw', 'I knew within a week'),
        ('it seemed the only way to her heart, so he went with it', 'what he did about it',
         'I didn’t know where that might lead'),
        ('that dynamic isn’t the main problem: many women have seen him that way', 'what the dynamic means',
         'That dynamic alone isn’t necessarily'),
        ('the question is whether they hold it lightly or put their father on him', 'what matters instead',
         'The question is whether'),
        ('with Bee the issues were BPD and witchcraft from her aunts', 'what it was with Bee', 'With Bee, the main issues'),
        ('she would say the same', 'her agreement', 'She would tell you the same'),
        ('she loved him openly and seemed to understand him', 'what drew him', 'She loved me openly'),
        ('the forest-and-mansion line made it feel unconditional', 'what mattered most', 'Most of all, there was'),
        ('it was the best drug he ever had', 'his verdict on it', 'Best drug I ever had'),
        ('he doesn’t know if that love was true', 'his doubt', 'I don’t know whether'),
        ('it was true in part of her, and maybe BPD idealization', 'his guess', 'I think it was true'),
        ('look at everything from many angles', 'what that teaches', 'You have to look at everything'),
        ('in love you see only the love angle', 'the catch', 'But when you’re in love'),
        ('that is the reality shift he means', 'what he calls it', 'That’s the reality shift'),
        ('it is great if the ground is ready for it', 'when it works', 'It’s great if the ground'),
        ('with the wrong person, rose-colored glasses hide what is real', 'when it doesn’t', 'If the rose-colored glasses'),
        ('he became the father where he wanted an equal', 'how it turned out', 'So I became the father'),
        ('maybe she grew up and left, as daughters do', 'part of why', 'Part of what happened'),
        ('that wasn’t the whole story', 'what else there was', 'That wasn’t the whole story'),
        ('the two years held enough insanity for lifetimes', 'what else happened', 'The two years in-between'),
        ('he is grateful he loved her', 'how he sees it now', 'Looking back'),
        ('he trained himself to replace missing her with loving her, and now feels joy', 'how he got there',
         'For three months after we broke up'),
        ('he wouldn’t advise entering a dangerous relationship for its worth', 'what he doesn’t advise',
         'That doesn’t mean I’d advise'),
        ('know your pattern, stop idealizing without closing up, and know what you’re getting into', 'what he advises instead',
         'Going in, it helps'),
    ]),
    'r13-slow': ('Slow & steady may win the race, but turtles have problems too!', SLOW, 'It tells the reader what going slowly shows and what it can’t.', [
        ('going slowly shows moods and treatment, but not how the sex or the aftermath will be', 'opens the section', None),
        ('you can know someone twenty years and find no fit the first night', 'how far that goes',
         'You can know somebody for twenty years'),
        ('some of it may improve if both help each other', 'what may help', 'Some of those things might get better'),
        ('sometimes bad fit feels like "let’s just be friends"', 'when it doesn’t', 'Sometimes bad sexual fit'),
        ('saying the sex isn’t working may sound conditional', 'how saying so sounds', 'Saying, “The sex isn’t working'),
        ('universal love doesn’t make someone special', 'his answer to that', 'But universal love'),
        ('universal love isn’t romance', 'what it isn’t', 'It isn’t romance'),
        ('it is the basis of any good relationship', 'what it is', 'It’s the basis of any good relationship'),
        ('he can love her and not want romance with her', 'what follows for him', 'I can still love her'),
        ('romance needs good sex too, or they are caring friends', 'why that is', 'Romantic love generally needs'),
    ]),
    'r13-disc': ('Disconnect to connect', DISC, 'It tells the reader self-reflection has blind spots, theirs included.', [
        ('self-reflection is a start but has blind spots', 'opens the section', None),
        ('a peer gives another angle', 'what helps next', 'A peer can give another angle'),
        ('your partner wants to keep you, so has a motive a peer counselor hopefully lacks', 'why a peer and not your partner',
         'Your partner is also usually trying'),
        ('he recommends peer counseling outside the couple', 'his advice', 'That’s why I recommend'),
        ('if his partner gets all his pain, she carries what he doesn’t understand', 'why outside',
         'If my partner is the only person'),
        ('he also has to deal with his body', 'the next part', 'I also have to deal with'),
        ('his mind knows he needn’t be dragged down with her', 'what his mind knows', 'My mind may understand'),
        ('his body still feels dragged down, fragile and sensitive', 'what his body does', 'Meanwhile my body feels'),
        ('his breathing gets shallow', 'how it shows', 'My breathing gets shallow'),
        ('it is hard to feel okay while she hurts', 'what it adds up to', 'It becomes extremely hard'),
        ('crying helps, but men in relationships are expected to be the shoulder', 'one way through it', 'Crying helps a lot'),
        ('that is another reason for a peer counselor', 'what follows', 'That is another reason'),
        ('crying is a kind of automatic breathwork', 'why crying helps', 'Crying also contains'),
        ('breathwork is an easy way to calm down', 'what breathwork does', 'Breathwork is one of the easiest'),
        ('reduced breathing helps him when his partner stirs up drama', 'which breathwork he uses',
         'Reduced breathing or the Buteyko method'),
        ('sometimes she means to upset him, and sometimes he can’t tell', 'whether she means it',
         'Sometimes she’s deliberately trying'),
        ('his Somatic Modalities guide has more body-based options', 'where to read more',
         'I explain more of the body-based options'),
        ('meditation helps too', 'another option', 'Meditation is also helpful'),
        ('he would still put reparenting, peer counseling and body work first', 'his order of them', 'For most people'),
        ('many say they cannot meditate yet', 'why that order', 'Many people say they cannot meditate'),
        ('meditation without that grounding can lead to spiritual bypassing', 'the risk otherwise', 'Meditation without grounding'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s, but for the moves named in texts.py (176’s wants said with its point, 438’s '
          'point first)',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
LOW = [{'point': 'the Low windows’ points', 'found': 'the live post (../../live-check/LOW-WINDOWS.json)',
        'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
AI = [{'point': 'the AI windows’ points', 'found': 'the live post (../../live-check/AI-WINDOWS.json and #47)',
       'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
bad = 0
for name, text in TEXTS.items():
    section, reader, why, rows = R[name]
    r = S.make(text, section, reader)
    assert len(r['sentences']) == len(rows), (name, len(r['sentences']), len(rows))
    for s, (pay, fol, link) in zip(r['sentences'], rows):
        s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
        s['follows'] = fol
        if 'link' in s:
            s['link'] = link
    r['opens']['why_reading'] = why
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = AI if name == 'r13-s22' else LOW
    r['placement'] = ('The paragraph by itself, in its place in the live post, for the section gate (E343).' if name == 'r13-sit34'
                      else 'The whole section, in its place in the live post, its heading left out.')
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
