#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r14's checks (texts.py). Every sentence has its row: the live post's sentences
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
MUSES = 'Someone in a relationship, working out who leads and who inspires, and how that shows up in fights.'
QUEEN = 'Someone curious whether sex can be far more than they have known, and whether the claims hold up.'
JEAL = 'Someone jealous in a relationship, deciding whether the jealousy is about now or about their past.'
LABELS = 'Someone asking whether a label like "boyfriend" or "girlfriend" would make their relationship more committed.'
R = {
    'r14-sit34': ('Situationships', SIT, 'It tells the reader who usually keeps it undefined, which may be them or their partner.', [
        ('either side can keep it undefined, but often it is the man, since she risks pregnancy', 'opens the paragraph', None),
        ('the one keeping it undefined gets the fun without the responsibility', 'what that one gets',
         'Whoever keeps it undefined'),
        ('pregnancy and attachment happen whether or not it has a name, and the void of a superficial fix stays',
         'what stays all the same', 'People still get pregnant and attached'),
        ('doomscrolling entertains you too', 'the comparison that sums it up', 'Doomscrolling entertains you too'),
    ]),
    'r14-slow181': ('Slow & steady may win the race, but turtles have problems too!', SLOW, 'It tells the reader twenty years of knowing someone may not show sexual fit.', [
        ('after twenty years the polarity may be missing on the first night', 'opens the paragraph', None),
        ('touch or smell can feel wrong, or desire and kinks may not fit', 'more of what may not fit', 'Touch or smell can feel wrong'),
        ('one person may be shut down, or the bodies may not connect', 'the rest of what may not fit',
         'Maybe one person is sexually shut down'),
        ('some of it may improve if both help each other', 'what may help', 'Some of those things might get better'),
        ('sometimes bad fit feels like "let’s just be friends"', 'when it doesn’t', 'Sometimes bad sexual fit'),
    ]),
    'r14-disc220': ('Disconnect to connect', DISC, 'It tells the reader a peer sees what they can’t.', [
        ('a peer gives another angle', 'opens the paragraph', None),
        ('your partner wants to keep you, so has a motive a peer counselor hopefully lacks', 'why a peer and not your partner',
         'Your partner is also usually trying'),
        ('he recommends peer counseling outside the couple, since his partner would carry what he doesn’t understand',
         'his advice and why', 'I recommend peer counseling outside the couple'),
    ]),
    'r14-disc221': ('Disconnect to connect', DISC, 'It tells the reader the body gets dragged down even when the mind knows better.', [
        ('his mind knows he needn’t be dragged down, but his body still is', 'opens the paragraph', None),
        ('his breathing gets shallow, and it is hard to feel okay while she hurts', 'how it shows', 'My breathing gets shallow'),
    ]),
    'r14-disc223': ('Disconnect to connect', DISC, 'It tells the reader crying is a kind of breathwork that calms.', [
        ('crying is a kind of automatic breathwork', 'opens the paragraph', None),
        ('breathwork is an easy way to calm down', 'what breathwork does', 'Breathwork is one of the easiest'),
        ('reduced breathing helps him when his partner stirs up drama', 'which breathwork he uses',
         'Reduced breathing or the Buteyko method'),
        ('sometimes she means to upset him, and sometimes he can’t tell', 'whether she means it',
         'Sometimes she’s deliberately trying'),
        ('his Somatic Modalities guide has more body-based options', 'where to read more',
         'I explain more of the body-based options'),
    ]),
    'r14-disc224': ('Disconnect to connect', DISC, 'It tells the reader where meditation fits among the other help.', [
        ('meditation helps, but he would put reparenting, peer counseling and body work first', 'opens the paragraph', None),
        ('many can’t meditate yet, and without that grounding it can lead to spiritual bypassing', 'why that order',
         'Many people say they cannot meditate'),
    ]),
    'r14-muses': ('Muses & Directors', MUSES, 'It tells the reader he sees the woman as the engine and himself as the steering wheel.', [
        ('she is the engine, he the steering wheel, and he gets motivation from her', 'opens the section', None),
        ('she is the life force', 'what the engine is', 'She is the life force'),
        ('she brings inspiration, beauty, intuition, creativity and the sense life is worth it', 'what she brings', 'She brings inspiration'),
        ('he gives it direction and makes it work', 'what the steering wheel does', 'I help give it direction'),
        ('he finds the intuitive mind sexy because he can’t follow it', 'what draws him', 'I find the intuitive mind incredibly sexy'),
        ('during sex some women have had psychic experiences and past-life memories', 'what he has seen', 'During sex'),
        ('Bee almost got enlightened, but he came too fast', 'one time it happened', 'One time, Bee said'),
        ('he laughs at himself for it', 'his reaction', 'Woops...'),
        ('Key could talk and teleport him outside the galaxy', 'another example', 'Key could sometimes start talking'),
        ('he can’t describe it any other way', 'his aside', 'I don’t know how else to describe it'),
        ('her voice made him shed liberating tears', 'what her voice did', 'Her voice would become so beautiful'),
        ('Bee could talk for hours and he felt timeless love instead of boredom', 'Bee’s version of it',
         'Bee could bring out something similar'),
        ('maybe women are poetry and men are prose', 'his summing up', 'Maybe women are poetry'),
        ('some women lack it and artistic men have it', 'the exception', 'Some women barely have that poetic quality'),
        ('he means archetypes, feminine and masculine', 'what he means', 'I’m referring more to feminine vs masculine'),
        ('the feminine intuitive leap attracts him because it is strange and often right', 'what attracts him',
         'What attracts me is the feminine intuitive leap'),
        ('he hopes girls keep it without falling into helplessness or chaos', 'his hope for girls', 'I hope this feminine quality'),
        ('boys should keep access to it too', 'his hope for boys', 'Boys should also maintain their access'),
        ('this polarity attracts but also shows up in fights', 'where it costs', 'This polarity is attracting'),
        ('Toft says after fifty years his wife wants to talk and he wants to fix', 'an example from Toft', 'Toft says'),
        ('he sees that too', 'his own case', 'I recognize that as well'),
        ('so he asks whether she wants help or listening', 'what he does', 'So I ask'),
        ('listening doesn’t make him a doormat', 'his limit', 'Listening doesn’t mean I’m gonna be a doormat'),
        ('being demonized is the safety problem he discussed', 'where the limit is', 'If I start listening to her demonize me'),
        ('he likes it when she sees the big picture and he fills in details', 'where he likes the polarity',
         'Where I like the polarity'),
        ('micromanaging makes him feel useless', 'where it goes wrong', 'If she micromanages'),
        ('if she earns more, she may start making all the decisions', 'another way it goes wrong', 'If she earns more than me'),
        ('where she knows more, he wants her help', 'when her help is welcome', 'She may know much more than I do'),
        ('her help is sexy until it becomes doing everything for him', 'where help turns', 'let me help you with this'),
        ('women often want him to say directly what he wants', 'what women want from him', 'In my experience'),
        ('"This is where I want to go."', 'what he says', 'This is where I want to go'),
        ('"This is what I think we should do."', 'what he says next', 'This is what I think we should do'),
        ('"Are you game?"', 'his question', 'Are you game'),
        ('she may have a better idea or say no, but wants him to take initiative', 'what she wants', 'She might have a better idea'),
        ('equality doesn’t mean splitting every role in half', 'his view of equality', 'I don’t think equality means'),
        ('if he likes driving and she cooking, great', 'his example', 'If I like driving'),
        ('whoever is better at something does more of it', 'how roles fall', 'If she’s way better at something'),
        ('when he leads he still wants her view', 'how he leads', 'When I’m leading'),
        ('lead by following, as the Zapatistas say', 'his closing saying', 'Mandar obedeciendo'),
    ]),
    'r14-queen': ('The Queen of Orgasms', QUEEN, 'It tells the reader sex can be far better than most people know.', [
        ('most people don’t know how good sex can be with polarity, trust, love and safety', 'opens the section', None),
        ('women have shown him the cervix can open and become intensely pleasurable', 'what he has seen', 'Women have shown me'),
        ('after cervical sex, regular sex hardly seems like sex', 'what it changes', 'After you experience cervical sex'),
        ('it seems more like foreplay', 'his comparison', 'It seems more like foreplay'),
        ('he hasn’t researched it deeply, since life and the work got in the way', 'his caveat', 'However, I’ve not yet'),
        ('women describe these orgasms as an energy taking over the body, not friction to release', 'how women describe it',
         'Women describe cervical and whole-body orgasms'),
        ('critics call it fiction, but studies document it as real and distinct in the body', 'what the evidence says',
         'Although the peanut gallery critics'),
        ('Kim Anami, Diana Richardson and others claim days of afterglow and healings', 'what educators claim',
         'Kim Anami, Diana Richardson'),
    ]),
    'r14-jeal': ('Jealousy on trial', JEAL, 'It tells the reader any attraction now reads as a sign of cheating, as they may fear.', [
        ('today a brief attraction reads as a sign infidelity is next', 'opens the section', None),
        ('so he faced it when B. wanted to marry him', 'what he did about it', 'That’s why I felt I had no choice'),
        ('he told her he couldn’t commit while attracted to others, so he would try to fix it', 'what he told her', 'I told her'),
        ('meditating, he found something like a switch in his mind', 'what he found', 'I meditated for a while'),
        ('it felt like programming about finding his life mate', 'what the switch was', 'It felt like evolutionary programming'),
        ('he asked himself whether she was the one', 'his question', 'I asked myself'),
        ('the answer was yes, and he switched off mate-finding', 'the answer', 'The inner Magic 8 Ball'),
        ('it worked almost always', 'how well it worked', 'It worked about 99% of the time'),
        ('only one beautiful girl caught his eye once', 'the one exception', 'I was no longer interested'),
        ('B. never believed the switch was real', 'her side', 'That amazed me'),
        ('she imagined him looking at other women when he wasn’t', 'what she did', 'She even started hallucinating'),
        ('so her jealousy wasn’t about what he was doing', 'what that shows', 'So her jealousy was not simply tracking'),
        ('more likely it was childhood insecurity justifying itself', 'his guess why', 'More likely it was insecure attachment'),
        ('jealousy is insecurity, but sometimes the relationship really is insecure', 'what jealousy is',
         'Jealousy is always insecurity'),
        ('either way it can fulfil itself', 'the risk either way', 'Although, either way'),
        ('instead of stewing, speak your heart without hiding behind anger', 'what to do instead', 'Instead of stewing in jealousy'),
        ('in a monogamous relationship you might say this', 'an example of it', 'In a monogamous relationship'),
        ('"you pay her more attention and I feel unloved and insecure"', 'what you might say', 'I notice you pay attention'),
        ('"can we talk about it?"', 'the next words', 'Can we talk about it'),
        ('"do you want to explore things with her?"', 'the next question', 'Do you really want to explore'),
        ('"fine, but don’t decide lightly, it can’t be undone"', 'the last words', 'If so that’s fine'),
        ('maybe he really is neglecting you', 'one possibility', 'Maybe he really is neglecting you'),
        ('maybe one glance got inflated by your insecurity', 'the other possibility', 'Maybe the “attention” was one glance'),
        ('that part shouldn’t be put on your partner', 'what to do with that part', 'That part should not be projected'),
        ('each couple works out what feels healthy', 'what stays open', 'Every couple has to work out'),
        ('he believes exclusivity can be chosen honestly', 'his belief', 'I do believe two people'),
        ('admit attraction exists and decide daily not to act on it', 'how they can do it', 'They can admit that attraction'),
        ('he would rather any attraction be easy to mention', 'his preference', 'I would rather make every attraction possible'),
        ('if only serious ones count, people say nothing', 'why he prefers it', 'If only the serious attractions'),
        ('lifelong exclusive partnership is promised more than lived', 'what he observes', 'A foundational, permanent, exclusive'),
        ('in polyamory boundaries are more negotiable, so negotiating is required', 'the other side', 'In a polyamorous relationship'),
        ('polyamory isn’t automatically better; it can be dishonest too', 'his caveat', 'That’s not to say that polyamory'),
        ('he thinks it often covers an inability to connect or a lack of self-control', 'what he believes it often is',
         'These days, I believe'),
        ('saying you can’t do monogamy beats pretending, and pretending can do more damage', 'what is more honest',
         'If you can’t do monogamy'),
        ('he learned most of this by screwing up', 'where he learned it', 'I learned most of this'),
        ('some he only thought through and isn’t sure of', 'his doubt', 'Some of it I just thought through'),
    ]),
    'r14-labels': ('Labels Are Descriptive, Not Prescriptive', LABELS, 'It tells the reader a label won’t create commitment, the question they have.', [
        ('labels don’t create commitment but can show whether two people agree on the relationship', 'opens the section', None),
        ('commitment grows from depth: deep talks make him ready to help', 'where commitment comes from',
         'True commitment grows out of relational depth'),
        ('he doesn’t need to promise it on paper', 'what that means', 'I don’t need to promise that on paper'),
        ('saying "I’m here for you" without real talk is a red flag', 'a warning sign', 'If someone says'),
        ('the one getting more may think it’s fulfilling', 'who thinks it works', 'The person getting more'),
        ('usually they just don’t notice it isn’t', 'what is really going on', 'Usually they’re just less aware'),
        ('a college friend with four girlfriends was chasing a fifth', 'his example', 'In college I had a friend'),
        ('he asked if he was really happy', 'his question', 'I asked him'),
        ('the friend said he was miserable', 'the answer', 'He said'),
        ('he felt empty inside', 'the rest of the answer', 'I feel empty inside'),
        ('the full conversation would stop most casual sex', 'how big the conversation is', 'The full conversation is so big'),
        ('so almost nobody has it', 'what follows', 'Which is why almost nobody'),
        ('he can’t decide for others', 'his limit', 'I can’t decide what is okay'),
        ('most defenders of casual sex aren’t honest about pregnancy, attachment or what they owe', 'what he can say',
         'I can say that most people'),
        ('outside a loving community, honest casual sex is nearly impossible', 'his view', 'Outside a loving poly community'),
        ('for something like casual love-making you need a free-love community where people matter', 'what you would need',
         'If you want something closer'),
        ('but such communities may attract people who struggle to connect, as Winiecki wrote', 'the catch',
         'But if the community is specifically designed'),
        ('it is a horrible catch-22', 'his verdict', 'This is a horrible catch-22'),
        ('wounded people get lonely, and loneliness can kill', 'one side of it', 'Wounded people get lonely'),
        ('the wounds that make them want a relationship can make them bad partners', 'the other side',
         'But the wounds that make somebody desperate'),
        ('people do more than trigger each other', 'how bad it gets', 'People don’t only trigger each other'),
        ('sometimes they terrorize or kill each other', 'the worst of it', 'Sometimes they terrorize'),
        ('he is conservative about this', 'his stance', 'I’m pretty conservative about this'),
        ('he would tell most friends not to date yet', 'his advice', 'I would tell most of my friends'),
        ('first love your inner child', 'what comes first', 'First love your inner child'),
        ('if you can’t, forget a relationship for now', 'what follows if not', 'If you can’t even do that'),
        ('get a cat or a puppy', 'his joke', 'Get a cat or a puppy'),
        ('dishonest, uncaring or repeating disasters means not ready', 'signs you’re not ready', 'If you’re dishonest'),
        ('you’re not ready', 'his verdict', 'You’re not ready'),
        ('you needn’t be healed, but must parent your inner intimacy and a real child', 'what ready means',
         'You don’t have to be completely healed'),
        ('if you can’t parent either way, don’t date', 'the test', 'If you can’t be a parent in either sense'),
        ('a good relationship teaches self-love, so you need one most when least able', 'the problem', 'A good relationship can teach you self-love'),
        ('it depends on what each of you is ready for', 'what it depends on', 'It depends what each of you'),
        ('a video helps explain the long process', 'where to look', 'Here’s a video'),
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
PARA = ('r14-sit34', 'r14-slow181', 'r14-disc220', 'r14-disc221', 'r14-disc223', 'r14-disc224')
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
    r['placement'] = ('The paragraph (with the one it leans on, where it is under 50 words) in its place in the live post, '
                      'for the section gate (E343).' if name in PARA
                      else 'The whole section, in its place in the live post, its heading left out.')
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
