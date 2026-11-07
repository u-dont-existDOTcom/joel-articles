#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r06's section checks (texts.py). Every sentence has its row: the live post's
sentences as well as mine, since the article's published text is not only his own words (gate E373).
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

U = 'none: the live post’s sentence, unchanged, in its place in his story'
Q_ = 'none: the next question in his run of questions'
R = {
    'r06-secA': ('Spirituality to bypass intimacy', 'Someone using meditation or monastic life to cope without intimacy, '
                 'deciding whether celibacy would really free them.', 'It tells the reader Joel used spirituality as a '
                 'stand-in for intimacy, which they may be doing.', [
        ('Joel used spirituality as a replacement for intimacy he couldn’t get', 'opens the section', None),
        ('how deprived he was as a boy and young man', 'why it was unavailable', 'As a boy and young man'),
        ('meditation helped him cope but didn’t cure it', 'what the replacement did', 'Meditation'),
        ('his ayahuasca ego death ended when he said he wanted a girlfriend', 'his story of it', 'I remember once'),
        ('the trip stopped and a voice told him to go find one', 'how the story ends', 'Right then'),
        ('nobody believes the story', 'his aside on it', 'this story'),
        ('he doubts most people can be happy celibate', 'what he concludes', 'celibate'),
        ('few are serious enough about liberation to give up sex for life', 'why he doubts it', 'spiritual liberation'),
        ('the Buddha didn’t advise everyone to become a monastic', 'support from the tradition', 'The Buddha'),
        ('if monastic life makes you happier, stay', 'the exception', 'If becoming a monastic'),
        ('who it might suit: the very advanced, low desire, the old', 'who the exception covers', 'It might work'),
        ('you may not know what you’re unaware of', 'the catch in the exception', 'But how do you know'),
        ('inner-child work and self-hypnosis can show it', 'how to find out', 'can help a lot with that'),
        ('a test: alone with a beautiful person who wants you', 'a test of the freedom', 'And if you’re so happy'),
        ('the same for women', 'the test for women', 'Or vice versa'),
        ('whether you feel you are losing control', 'the test’s first question', Q_),
        ('whether you are afraid', 'the test’s last question', Q_),
        ('Bhante Gunaratana tells such a story', 'an example of the test', 'tells a story like this'),
        ('a woman waited naked in his bed at a retreat', 'what happened', 'A super beautiful girl'),
        ('he screamed at her to get out', 'how he reacted', 'He went nuts'),
        ('he was still repressing something', 'what it shows', 'Obviously'),
        ('robes don’t change anything', 'what the example adds up to', 'Robes do nothing'),
        ('an abbot molested Joel in public', 'his own evidence', 'I was mildly molested'),
        ('Thai parents keep children away from monks', 'how common it is', 'In Thailand'),
        ('Tibet is worse', 'a worse case', 'Tibet is worse'),
        ('forced celibacy doesn’t end sexuality', 'why robes do nothing', 'Forced celibacy'),
        ('it usually goes somewhere weird', 'what happens to it', 'it eventually sends it'),
        ('the point pressed as a question', 'the point pressed', 'Why wouldn’t it?'),
        ('some people become monks for practical reasons', 'another reason people choose robes', 'practical reasons too'),
        ('in a poor country: food, a roof, respect, no job or family to support', 'the reasons, first case',
         'In a poor country'),
        ('even where food doesn’t matter, a nobody gets to be Venerable Somebody and is bowed to', 'the reasons where '
         'the first one falls away', 'And even where the food doesn’t matter'),
        ('he may still sincerely want liberation', 'what this says about him', 'Of course'),
        ('people want several things at once', 'why both can be true', 'several things at once'),
    ]),
    'r06-secB': ('Don’t make your partner your whole world', 'Someone newly in love who has let everything else drop, '
                 'deciding how much of their own life to keep.', 'It tells the reader that when in love, the partner '
                 'becomes everything, the state they are in.', [
        ('in love, his partner becomes his everything', 'opens the section', None),
        ('everything else drops away', 'what that does', 'Everything else'),
        ('he still sees friends, but only wants her', 'how far it goes', 'I still try'),
        ('the paradise carries the seed of its end', 'the turn', 'That little paradise'),
        ('it feels magical because you stop parenting yourself', 'why it feels that way', 'Part of why'),
        ('that makes you soft, like a treat or heroin', 'what it costs', 'This makes you'),
        ('keep your own healing practices', 'what to do', 'don’t let that'),
        ('or you will blame them when you feel bad', 'what happens if you don’t', 'Otherwise'),
        ('don’t let your world get small', 'what follows from it', 'So don’t'),
        ('keep your friends unless they harm the relationship', 'the first step', 'Don’t abandon your friends'),
        ('if they do, ask why', 'the condition', 'And if they aren’t'),
        ('are they bad friends', 'the first reason to ask about', Q_),
        ('are they after one of you', 'the next reason', Q_),
        ('or is the relationship too weak for an outside view', 'the last reason', Q_),
        ('less time with friends than before is fine', 'how much time', 'You don’t need'),
        ('keep room to explore life on your own', 'what to keep', 'But keep some room'),
        ('for him: friends, therapy, a mission, interests, community, being alone', 'his own list', 'For me'),
        ('Toft: a man can get feminine energy from many places', 'a source for the same idea', 'Toft also'),
        ('Joel likes the idea', 'his response', 'that idea'),
        ('a girlfriend shouldn’t be his only source', 'what it means for him', 'A girlfriend shouldn’t'),
        ('announcing "I need time for myself!" when overwhelmed sounds like time away from her', 'the problem with '
         'waiting', 'When I’m already overwhelmed'),
        ('so he would make alone time normal from early on', 'his answer to it', 'So'),
        ('go out into the world together', 'the other side of alone time', 'And bring each other out'),
        ('see people together', 'the first way to do it', 'See people'),
        ('go places', 'the second way to do it', 'Go places'),
        ('don’t disappear into each other', 'what it guards against', 'disappear into each other'),
    ]),
    'r06-secC': ('Can making love be a spiritual practice?', 'Someone who thinks sex and spiritual life pull against '
                 'each other, deciding whether to keep them apart.', 'It tells the reader the early Buddhist texts don’t '
                 'teach tantric sex, which they may have assumed they do.', [
        ('the early texts don’t teach tantric sex as a path', 'opens the section', None),
        ('nor do they reserve awakening for monastics', 'the other half', 'But they also'),
        ('DN 16 counts hundreds of lay stream-enterers and more', 'the evidence', 'In DN 16'),
        ('those are three of the four stages', 'what the terms mean', 'Those are'),
        ('SN 55.24 has a comic complaint', 'more evidence', 'SN 55.24'),
        ('Sakyans grumbled that everyone is a stream-enterer now', 'what the complaint was', 'When the Buddha'),
        ('a married couple asked how to stay together in future lives', 'a married couple’s case', 'And when the married '
         'couple'),
        ('the Buddha’s answer: faithful, generous, kind to each other', 'his answer', 'none: the quoted verse the sentence '
         'before introduces with a colon'),
        ('household life isn’t opposed to spiritual development', 'what the texts add up to', 'Marriage, sex'),
        ('Kim Anami says sexual energy can heal and awaken', 'further than the texts', 'goes even further'),
        ('her students say it spilled into health, work, money, creativity', 'what her students report', 'She’s also'),
        ('her jade-egg practice trains for the cervical orgasm', 'what her practice is', 'Her jade-egg practice'),
        ('the Keenes are the example Joel likes', 'his favourite case', 'Brad and Pam Keene'),
        ('Pam’s awakening completed while they made love', 'what happened', 'Pam says'),
        ('she helped Brad awaken, so the marriage became the path', 'what it shows', 'She later helped Brad'),
        ('Twin Flames have something more than masculine and feminine', 'the next thought', 'In the previous section'),
        ('the in-love paradise of Twin Flames is more special', 'what is more', 'But there’s really'),
        ('Cody’s Yin/Yang puts it better', 'a better word for it', 'Maybe a better way'),
        ('Malia found her twin flame in January 2026', 'his friend’s case', 'My ex-girlfriend, Malia'),
        ('they feel each other’s emotions at any distance', 'what it was like', 'They only talked'),
        ('when one feels bad, so does the other', 'how far it goes', 'To the point'),
        ('the same with happiness, like entangled photons', 'the other side', 'If one is very happy'),
        ('Joel had telepathy too, with Bee, but less', 'his own case', 'I’ve also had telepathy'),
        ('Mouhamed’s family forbade it and he left', 'what happened next', 'Meanwhile his family'),
        ('maybe because of the age gap', 'a guess at why', 'Not sure why'),
        ('they pretend they will get over it', 'how they are now', 'They both try'),
        ('Malia is trying to marry ChatGPT', 'his joke on it', 'Meanwhile, Malia’s'),
        ('Joel worries about people in love with an AI', 'his aside on it', 'Note:'),
        ('those people may not be ready for a real relationship', 'his take on it', 'But oh well'),
        ('back to the topic', 'the return', 'Back to the topic'),
        ('many don’t believe in twin flames because they haven’t found one', 'the first camp', 'There are a ton of people'),
        ('that’s fine with him', 'his stance on them', 'That’s fine'),
        ('they say marry your best friend', 'what that camp says', 'They might be the people'),
        ('the other camp believes in one person made for you', 'the second camp', 'Then there are the folks'),
        ('that’s fine with him too', 'his stance on them', 'I’m also not trying'),
        ('he wants to tell his story', 'what he will do instead', 'But I do want'),
        ('he went from the first camp to the second to a new one', 'his story in short', 'I used to fall'),
    ]),
    'r06-secD': ('Which marriage vows are honest?', 'Someone about to make wedding vows, deciding what they can honestly '
                 'promise.', 'It tells the reader conventional vows are dishonest, which they may half know.', [
        ('conventional vows are dishonest, and most people know it', 'opens the section', None),
        ('you can’t promise future feelings', 'why they are dishonest', 'You can’t promise'),
        ('you can promise actions you can deliver', 'what you can promise', 'You can promise actions'),
        ('examples: the truth, showing up, the children', 'examples of it', 'So for example'),
        ('the Bible has a warning like his', 'support from the Bible', 'We also find'),
        ('Ecclesiastes: better no vow than a broken one', 'the first verse', 'Ecclesiastes'),
        ('the passage warns of God’s anger', 'what the verse says follows', 'the passage warns'),
        ('Matthew and James: let your yes be yes, anything more is from evil', 'the second verses', 'Matthew'),
        ('so the extra promise looks suspicious: a trustworthy yes needs no other layer', 'what the verses mean for '
         'vows', 'the extra promise'),
        ('where promising romantic interest came from', 'the next question', 'Where did the idea'),
        ('it began in 19th-century England', 'the answer', 'It turns out'),
        ('the trend snowballed until today', 'what followed', 'That trend'),
        ('you can contract actions, not feelings', 'what the ancestors knew', 'But what our ancestors knew'),
    ]),
    'r06-secD2': ('Which marriage vows are honest?', 'Someone about to make wedding vows, deciding what they can honestly '
                  'promise.', 'It tells the reader conventional vows are dishonest, which they may half know.', [
        ('conventional vows are dishonest, and most people know it', 'opens the section', None),
        ('you can’t promise future feelings', 'why they are dishonest', 'You can’t promise'),
        ('you can promise actions you can deliver', 'what you can promise', 'You can promise actions'),
        ('examples: the truth, showing up, the children', 'examples of it', 'So for example'),
        ('the Bible has a warning like his', 'support from the Bible', 'We also find'),
        ('Ecclesiastes: better no vow than a broken one', 'the first verse', 'Ecclesiastes'),
        ('the passage warns of God’s anger', 'what the verse says follows', 'the passage warns'),
        ('Matthew and James: let your yes be yes, anything more is from evil, which makes the extra promise suspicious',
         'the second verses and what they mean for vows', 'Matthew'),
        ('where promising romantic interest came from', 'the next question', 'Where did the idea'),
        ('it began in 19th-century England', 'the answer', 'It turns out'),
        ('the trend snowballed until today', 'what followed', 'That trend'),
        ('you can contract actions, not feelings', 'what the ancestors knew', 'But what our ancestors knew'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s, with the reorders r03 to r05 recorded for the changed paragraphs',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
CHECKED = {
    'r06-secD2': [{'point': 'if your yes is trustworthy, why does it need another layer?', 'found': 'the verse in the same '
                   'sentence already says it: let your yes be yes, and anything beyond comes from evil', 'still_needed': 'no: '
                   'it says the verse again as a question, so it is a repeat (E378)', 'fate': 'cut'}],
    'r06-secC': [{'point': 'Kim Anami treats sexual energy as a path into healing, creativity, worldly action and spiritual '
                  'awakening', 'found': 'her page the live post links (https://kimanami.com/my-vagina-heals-everything/) '
                  'could not be read from here on 2026-11-07 (the fetch waited for an approval nobody answered); the live '
                  'post’s claim is kept, with creativity and work said once, in the students’ sentence that already names '
                  'them', 'still_needed': 'yes: it is what goes further than the sutta', 'fate': 'changed'}],
}
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
    r['checked'] = CHECKED.get(name, [{'point': 'the AI window’s point', 'found': 'the live post (../../live-check/AI-WINDOWS.json)',
                                       'still_needed': 'yes: the section needs it', 'fate': 'changed'}])
    r['placement'] = 'The whole section in its place in the live post, from its heading to the next.'
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
