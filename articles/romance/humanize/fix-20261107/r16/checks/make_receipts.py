#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r16's checks (texts.py). Every sentence has its row: the live post's sentences
as well as mine (gate E373). Rows for sentences r14 and r15 already had come from their receipt makers.
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402


def rows_from(rnd):
    """The R table of an earlier round's receipt maker, read without running its checks."""
    src = (HERE.parents[1] / rnd / 'checks' / 'make_receipts.py').read_text(encoding='utf-8')
    head = src.split('\nQ = {')[0].split('from texts import TEXTS  # noqa: E402', 1)[1]
    ns = {}
    exec(head, ns)
    return ns['R']


R14, R15 = rows_from('r14'), rows_from('r15')
jeal_rows = list(R14['r14-jeal'][3][:27]) + list(R15['r15-jeal367'][3]) + list(R15['r15-jeal369'][3])
jeal_rows[27] = ('if only serious attractions count, people say nothing, so he would rather mention every one casually',
                 'his preference and why', 'If only the serious attractions')
jeal_rows[30] = ('polyamory isn’t automatically better; it can be dishonest too', 'his caveat', 'Polyamory isn’t automatically better')
slow_rows = list(R15['r15-slow'][3])
slow_rows[4:6] = [('some of it may improve if both help, but sometimes bad fit feels like "let’s just be friends"',
                   'what may help, and when it doesn’t', 'Some of those things might get better')]
deep_rows = list(R15['r15-deeper'][3])
deep_rows[16:18] = [('he understands why, but it still felt dismissive, as if she wanted his knee fine', 'his view of it',
                     'I get why')]
deep_rows[17:19] = [('Bee had supported a broke, crazy boyfriend before him', 'her past', 'Before me, Bee had also stayed'),
                    ('she blamed herself, and he agrees', 'his verdict on it', 'Later she blamed herself'),
                    ('helping through a passing incapacity like his knee differs from carrying a man who won’t take '
                     'responsibility', 'why he agrees', 'Helping carry somebody through a temporary incapacity')]
IDEAL = R15['r15-ideal'][1]
SIT = R14['r14-sit34'][1]
ROM = 'A man and a woman in a relationship, working out how each can be strong and still lean on the other.'
FAN = 'Someone with a fantasy they haven’t shared, deciding whether and how to bring it to a partner.'
R = {
    'r16-ideal147': ('Beware idealization in either direction', IDEAL, 'It tells the reader idealization predicts demonization.', [
        ('idealization predicts demonization for him', 'opens the paragraph', None),
        ('he uses it almost as a diagnosis in his life', 'how he uses it', 'I don’t mean this as a clinical diagnosis'),
        ('"you’re a great guy" sounds healthy', 'the healthy version', 'If a woman says'),
        ('flaws and love together sound healthy', 'the rest of it', 'Of course you have flaws'),
        ('"you’re perfect" worries him', 'the worrying version', 'If she says'),
        ('"no flaw" makes him run', 'his reaction', 'I can’t find any flaw'),
        ('in splitting someone flips from all good to all bad, and hatred replaces worship', 'what happens then',
         'When the BPD splitting happens'),
        ('then come public accusations and a rewritten past', 'what comes after', 'Then come public accusations'),
        ('the one who thought him perfect later says he thinks he’s perfect', 'the irony', 'Sometimes the woman who thought'),
    ]),
    'r16-jeal': (R14['r14-jeal'][0], R14['r14-jeal'][1], R14['r14-jeal'][2], jeal_rows),
    'r16-sit34': ('Situationships', SIT, 'It tells the reader who usually keeps it undefined, which may be them or their partner.', [
        ('either side can keep it undefined, but often it is the man, since she risks pregnancy', 'opens the paragraph', None),
        ('the one keeping it undefined gets the fun without most of the responsibility', 'what that one gets',
         'Whoever keeps it undefined'),
        ('people still get pregnant and attached, whatever they call it', 'what stays all the same', 'But people still get pregnant'),
        ('the one keeping it that way still ends up with the void of a superficial fix', 'what that one doesn’t escape',
         'The one keeping it that way'),
        ('doomscrolling entertains you too', 'the comparison that sums it up', 'Doomscrolling entertains you too'),
    ]),
    'r16-slow': (R15['r15-slow'][0], R15['r15-slow'][1], R15['r15-slow'][2], slow_rows),
    'r16-deeper': (R15['r15-deeper'][0], R15['r15-deeper'][1], R15['r15-deeper'][2], deep_rows),
    'r16-romance': ('Romance Shouldn’t Be Adjudicated', ROM, 'It tells the reader proving manhood makes it an act.', [
        ('if he has to prove he’s the man, it is already an act he must defend', 'opens the section', None),
        ('he doesn’t think of himself as super-masculine', 'what he is like', 'I don’t actually walk around'),
        ('he cries, needs help and gets things wrong', 'the evidence', 'I cry, I need help'),
        ('Bee once called him her "wife"', 'a story about it', 'Bee once called me'),
        ('he doesn’t recommend that as a polarity exercise', 'his joke', 'I don’t recommend that'),
        ('when a woman appreciates his masculine side, it comes out by itself', 'what brings it out', 'When a woman appreciates'),
        ('the same goes for her: she needn’t perform softness to prove she is feminine', 'the same for women',
         'The same is true for a woman'),
        ('surrender means more when she could take control', 'what surrender means', 'Surrender means so much more'),
        ('a strong woman choosing to surrender is sexy', 'why it is sexy', 'When a strong woman surrenders'),
        ('women get pulled two ways', 'what happens to women', 'Women can get pulled in two directions'),
        ('she may worry she’s too emotional, difficult or needy', 'one direction', 'She may worry'),
        ('then she may need nobody, and receiving care feels like weakness', 'the other direction', 'Then she can over-correct'),
        ('Toft still tells his wife she’s beautiful after fifty years', 'an example', 'Toft says'),
        ('Anami talks about women learning to receive', 'another voice', 'Anami talks a lot'),
        ('receiving doesn’t make her helpless, and a man receiving care is still a grown man', 'what receiving means',
         'Letting a man help'),
        ('it can be as simple as her asking him to drive because she likes it', 'an everyday case', 'Sometimes that’s as ordinary'),
        ('he asks for her intuition, she asks for his practical help', 'how they trade', 'I might ask'),
        ('that is invitational: a party you’re invited to, not a war you’re drafted into', 'what it is called',
         'That’s called invitational'),
        ('a woman who can’t invite may manufacture a crisis to make him lead', 'when invitation fails',
         'When a woman doesn’t know how to gently invite'),
        ('he has seen a lot of that', 'his experience', 'Unfortunately, I’ve seen a lot'),
    ]),
    'r16-fantasy': ('Fantasy', FAN, 'It tells the reader safety lets polarity go all the way.', [
        ('inside real safety the polarity can go all the way', 'opens the section', None),
        ('fantasy is one of the best ways to try that', 'how to try it', 'Fantasy is one of the best ways'),
        ('domination fantasies give extreme polarity without harm, since consent stays', 'why fantasy works',
         'Domination fantasies are common'),
        ('nobody is entitled to another’s fantasies', 'a limit on fantasy', 'Nobody is entitled'),
        ('they are private until shared, and sharing one is a great act of trust', 'what sharing means', 'They’re private until'),
        ('Esther Perel says fantasy is play, not a request', 'how to take a shared fantasy', 'Esther Perel makes the distinction'),
        ('a rape fantasy isn’t a wish to be raped', 'what that means', 'So someone with a rape fantasy'),
        ('a couple can keep it in their heads or act some of it out', 'what to do with it', 'A couple can keep a fantasy'),
        ('fantasy should add to arousal, not be the only way, so he can enjoy the real woman', 'a caution',
         'Fantasy should also add to arousal'),
    ]),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: "splitting" is explained where it is first used; no other new term',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s; the joins named in texts.py keep it',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
LOW = [{'point': 'the Low windows’ points', 'found': 'the live post (../../live-check/LOW-WINDOWS.json)',
        'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
PARA = ('r16-ideal147', 'r16-sit34')
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
    r['checked'] = LOW
    r['placement'] = ('The paragraph (with the one it leans on) in its place in the live post, for the section gate (E343).'
                      if name in PARA else 'The whole section, in its place in the live post, its heading left out.')
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
