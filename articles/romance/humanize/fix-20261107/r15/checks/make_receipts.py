#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r15's checks (texts.py). Every sentence has its row: the live post's sentences
as well as mine, since the article's published text is not only his own words (gate E373). A row is (what the reader
learns, how it follows, the words that tie it to what came before).
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

SIT = 'Someone in a relationship that is mostly sex and has no name, deciding whether to ask what it is.'
SLOW = 'Someone taking a relationship slowly, deciding whether that will tell them enough before sex.'
DISC = 'Someone whose partner’s moods drag them down, deciding who to talk to and how to calm their body.'
JEAL = 'Someone jealous in a relationship, deciding whether the jealousy is about now or about their past.'
DEEP = 'A man who provides for a partner, wondering whether she loves him or what he does for her.'
IDEAL = 'Someone being adored early in a relationship, deciding whether that is love or a warning sign.'
R = {
    'r15-sit': ('Situationships', SIT, 'It tells the reader what a situationship is, the kind they may be in.', [
        ('a situationship is hard to define, which is the point', 'opens the section', None),
        ('it is usually a happenstance relationship based on sex', 'what it usually is', 'Usually it’s a happenstance'),
        ('there is less communication, and it is more superficial', 'how it differs', 'There’s less communication'),
        ('it is clearly a relationship even when someone refuses to name it', 'yet what it is', 'Yet it is obviously'),
        ('you have sex and spend time as you wouldn’t with a friend, so it fills the void only by accident, maybe enough '
         'to stop you looking deeper', 'the evidence and what it does', 'You’re regularly having sex'),
        ('either side can keep it undefined, but often it is the man, since she risks pregnancy', 'who keeps it undefined',
         'It can go either way'),
        ('the one keeping it undefined gets the fun without the responsibility', 'what that one gets',
         'Whoever keeps it undefined'),
        ('pregnancy and attachment happen whether or not it has a name, and the void of a superficial fix stays',
         'what stays all the same', 'People still get pregnant and attached'),
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
    'r15-slow': ('Slow & steady may win the race, but turtles have problems too!', SLOW, 'It tells the reader what going slowly shows and what it can’t.', [
        ('going slowly shows moods and treatment, but not how the sex or the aftermath will be', 'opens the section', None),
        ('after twenty years the polarity may be missing on the first night', 'how far that goes',
         'You can know somebody for twenty years'),
        ('touch or smell can feel wrong, or desire and kinks may not fit', 'more of what may not fit', 'Touch or smell can feel wrong'),
        ('one person may be shut down, or the bodies may not connect', 'the rest of what may not fit',
         'Maybe one person is sexually shut down'),
        ('some of it may improve if both help each other', 'what may help', 'Some of those things might get better'),
        ('sometimes bad fit feels like "let’s just be friends"', 'when it doesn’t', 'Sometimes bad sexual fit'),
        ('saying the sex isn’t working may sound conditional', 'how saying so sounds', 'Saying, “The sex isn’t working'),
        ('universal love doesn’t make someone special', 'his answer to that', 'But universal love'),
        ('universal love isn’t romance', 'what it isn’t', 'It isn’t romance'),
        ('it is the basis of any good relationship', 'what it is', 'It’s the basis of any good relationship'),
        ('he can love her and not want romance with her', 'what follows for him', 'I can still love her'),
        ('romance needs good sex too, or they are caring friends', 'why that is', 'Romantic love generally needs'),
    ]),
    'r15-disc': ('Disconnect to connect', DISC, 'It tells the reader self-reflection has blind spots, theirs included.', [
        ('self-reflection is a start but has blind spots', 'opens the section', None),
        ('a peer gives another angle', 'what helps next', 'A peer can give another angle'),
        ('your partner wants to keep you, so has a motive a peer counselor hopefully lacks', 'why a peer and not your partner',
         'Your partner is also usually trying'),
        ('he recommends peer counseling outside the couple, since his partner would carry what he doesn’t understand',
         'his advice and why', 'I recommend peer counseling outside the couple'),
        ('his mind knows he needn’t be dragged down, but his body still is', 'the next part', 'I also have to deal with'),
        ('his breathing gets shallow, and it is hard to feel okay while she hurts', 'how it shows', 'My breathing gets shallow'),
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
        ('meditation helps, but he would put reparenting, peer counseling and body work first', 'another option',
         'Meditation is also helpful'),
        ('many can’t meditate yet, and without that grounding it can lead to spiritual bypassing', 'why that order',
         'Many people say they cannot meditate'),
    ]),
    'r15-jeal367': ('Jealousy on trial', JEAL, 'It tells the reader why every attraction should be easy to mention.', [
        ('if only serious attractions count, people say nothing, so he would rather mention every one casually',
         'opens the paragraph', None),
        ('people promise lifelong exclusive partnership far more often than they live it', 'what he observes next',
         'People promise a foundational'),
        ('in polyamory boundaries are more negotiable, so negotiating is required', 'the other side', 'In a polyamorous relationship'),
    ]),
    'r15-jeal369': ('Jealousy on trial', JEAL, 'It tells the reader polyamory isn’t automatically better.', [
        ('polyamory isn’t automatically better; it can be dishonest too', 'opens the paragraph', None),
        ('he thinks it often covers an inability to connect or a lack of self-control', 'what he believes it often is',
         'These days, I believe'),
        ('pretending to be monogamous can do more damage, so saying you can’t is more honest', 'what is more honest',
         'Sometimes pretending to be monogamous'),
        ('he learned most of it by screwing up, thought some through, and isn’t sure of all of it', 'where he learned it',
         'I learned most of this'),
    ]),
    'r15-deeper': ('It always goes deeper', DEEP, 'It tells the reader the provider question goes deeper than practical.', [
        ('the question is more than practical', 'opens the section', None),
        ('it is philosophical', 'what kind of question', 'It’s philosophical'),
        ('men wonder whether she loves them or what they do for her', 'what the question is', 'Men have this'),
        ('provision may be part of it, and that’s fine', 'his answer', 'I don’t need the answer'),
        ('she may like that he’s competent, protective and useful', 'what she may like', 'Maybe she likes'),
        ('he likes her beauty and sexuality', 'what he likes', 'I definitely like her beauty'),
        ('he wants what they have to grow beyond that', 'what he wants', 'I just want what we have'),
        ('Bee said you’re either going up or going down', 'why it has to grow', 'Because as Bee always said'),
        ('he wondered how a woman would love him if he couldn’t provide', 'his question for years', 'I had wondered for years'),
        ('Bee said she’d rather be with him in the forest than another man in a mansion', 'her answer', 'Then Bee told me'),
        ('that made him fall in love with her', 'what it did', 'That’s what made me fall in love'),
        ('a smaller test came later', 'the next test', 'I got a smaller'),
        ('Bee gave him shoes that didn’t fit', 'what happened', 'Bee gave me some shoes'),
        ('his knee was hurt for a month', 'the result', 'I wore them for a day'),
        ('she nursed him reluctantly', 'how she cared for him', 'She did nurse me'),
        ('she suggested it was in his head', 'what she said', 'She also kept suggesting'),
        ('he understands why, since neither believed the shoes could do it', 'his view of it', 'I get why'),
        ('it still felt dismissive, as if she wanted his knee fine', 'how it felt', 'It still felt dismissive'),
        ('Bee had supported a broke, crazy boyfriend before him', 'her past', 'Before me, Bee had also stayed'),
        ('she blamed herself and he agrees: helping through a rough patch differs from carrying a man who won’t take '
         'responsibility', 'his verdict on it', 'Later she blamed herself'),
        ('some women are fixers, which can create the opposite pattern', 'the other side of it', 'Some women are fixer types'),
        ('what makes him desirable differs from what makes him loved when he isn’t', 'his summing up',
         'What makes me desirable'),
    ]),
    'r15-ideal': ('Beware idealization in either direction', IDEAL, 'It tells the reader idealization can look like love.', [
        ('idealization can be sick or close to real love', 'opens the section', None),
        ('so it is easy to confuse them', 'what follows', 'That’s why it’s so easy'),
        ('his main experiences were with Bee and Key', 'his own case', 'So far in my life'),
        ('they are the two women he has been in love with', 'why them', 'They’re also the two women'),
        ('both saw him as a knight and he became their love slave', 'what happened', 'Both of them saw me'),
        ('he isn’t trying to save anyone', 'what it wasn’t', 'I’m not Superman'),
        ('it is a director/muse dynamic, exaggerated', 'what it was', 'There’s just a natural director/muse'),
        ('it shouldn’t have to happen that way', 'his verdict', 'It shouldn’t have to happen'),
        ('it is a bad shortcut to the archetypes', 'why it shouldn’t', 'It’s a bad shortcut'),
        ('really seeing someone as amazing doesn’t depend on what it gives you', 'what real seeing is',
         'Legitimately seeing someone as amazing'),
        ('identifying with your view of them means you are lost', 'when it goes wrong', 'You’re already lost in the sauce'),
        ('idealization predicts demonization for him', 'what idealization predicts', 'The degree of idealization'),
        ('he uses it almost as a diagnosis in his life', 'how he uses it', 'I don’t mean this as a clinical diagnosis'),
        ('"you’re a great guy" sounds healthy', 'the healthy version', 'If a woman says'),
        ('flaws and love together sound healthy', 'the rest of it', 'Of course you have flaws'),
        ('"you’re perfect" worries him', 'the worrying version', 'If she says'),
        ('"no flaw" makes him run', 'his reaction', 'I can’t find any flaw'),
        ('splitting turns worship into hatred and then public accusations', 'what happens next',
         'When the BPD splitting happens'),
        ('the one who thought him perfect later says he thinks he’s perfect', 'the irony', 'Sometimes the woman who thought'),
        ('he gets nervous when someone knows him too well too soon', 'what he watches for', 'I’ve learned to get nervous'),
        ('"we’re twin flames"', 'an example of it', 'We’re twin flames'),
        ('"she knows my motives"', 'another example', 'She knows my motives'),
        ('"I’m Lord Krishna"', 'another example', 'I’m Lord Krishna'),
        ('maybe he is better than the others', 'his joke', 'Okay, maybe I really am'),
        ('if nothing bothers her yet, she hasn’t found all of him', 'the point', 'But if she hasn’t found anything'),
        ('he still loves his exes', 'an example', 'For example, I still love'),
        ('he talks about them because he thinks of them', 'why he talks of them', 'Sometimes I talk about them'),
        ('he isn’t trying to make her jealous', 'what it isn’t', 'I’m not trying to make her jealous'),
        ('if she can’t handle it she isn’t ready', 'his verdict', 'If she can’t handle that'),
        ('she may ask him to talk less about exes', 'her request', 'If she says, “Can you talk less'),
        ('sure', 'his answer', 'Sure.'),
        ('maybe he does talk about them too much', 'his concession', 'Maybe I do talk about them'),
        ('but they still matter to him', 'his limit', 'But they still matter'),
        ('he won’t pretend they aren’t on his mind', 'why they stay', 'If I’m supposed to listen'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s, but for the moves named in texts.py (367 and 369 with their reasons first)',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
LOW = [{'point': 'the Low windows’ points', 'found': 'the live post (../../live-check/LOW-WINDOWS.json)',
        'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
PARA = ('r15-jeal367', 'r15-jeal369')
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
    r['checked'] = LOW
    r['placement'] = ('The paragraph with the one it leans on, in its place in the live post, for the section gate (E343).'
                      if name in PARA else 'The whole section, in its place in the live post, its heading left out.')
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
