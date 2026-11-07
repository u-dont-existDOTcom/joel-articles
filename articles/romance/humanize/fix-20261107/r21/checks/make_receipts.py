#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r21's checks of mine (texts.py): the section with his S17 in it (his words, with
my r20 304 to 306 and my "your attention"), and the three stretches. "r21-bypass" is the live post with his S2 as he sent
it, no change of mine, so it goes with --unchanged and needs none. Every sentence has its row: a sentence an earlier
receipt in this article already has a row for keeps it; the rest are written here. Writes CHECK-<name>.txt and
RECEIPT-<name>.json and checks each; exits 1 if one fails. CHECK-r21-bypass.txt is written too, with no receipt."""
import glob
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

OLD = {}
for f in sorted(glob.glob(str(ROOT / 'articles' / 'romance' / 'humanize' / '**' / 'RECEIPT-*.json'), recursive=True)):
    if '/r21/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))
NEW = {
    # his S17 (TEACH-KIM-ANAMI)
    'Marriage, sex, and household life aren':
        ('marriage and sex aren’t in conflict with serious spiritual growth', 'what the texts show',
         'Marriage, sex, and household life'),
    'Kim Anami goes even further':
        ('Anami says sexual energy, used properly, can heal you and wake you up with your beloved', 'a bolder view',
         'goes even further'),
    'She’s also collected a ton of stories':
        ('her students say the effects spilled into their health, careers, money and creativity', 'her evidence',
         'She’s also collected'),
    'Her jade-egg practice':
        ('her jade-egg practice trains the pelvic floor and attention for the cervical O', 'one of her practices',
         'Her jade-egg practice'),
    'No partner required for the jade egg phase':
        ('the jade egg needs no partner', 'a note on that practice', 'the jade egg phase'),
    'Brad and Pam Keene are the example couple':
        ('the Keenes are his favorite example of her method', 'an example', 'as an example of how her method works'),
    'Pam explained that her Kundalini process':
        ('Pam awakened while making love', 'what happened to them', 'Pam explained'),
    # Jealousy 367 to 369
    'I’d rather be able to mention any attraction casually':
        ('he’d rather any attraction, even a small one, can be mentioned casually', 'his own preference', None),
    'If you’re only supposed to bring up the serious ones':
        ('if only serious ones may be mentioned, each mention is a big talk and people keep quiet',
         'why he’d rather have it so: what happens otherwise',
         'the serious ones'),
    'Lots of couples promise to be each other’s one and only':
        ('far more couples promise lifelong exclusivity than keep it', 'opens the paragraph', None),
    'In a polyamorous relationship the boundaries might be more negotiable, but then':
        ('polyamory’s boundaries can be negotiated, so they have to be', 'the other kind of relationship',
         'In a polyamorous relationship'),
    'Polyamory can be just as dishonest':
        ('polyamory can be dishonest too, often a way around not being able to go deep with one person',
         'opens the paragraph: the other side', None),
    'Or it’s their way of admitting':
        ('or a way to admit they lack self-control without doing the work that would make it ethical',
         'a second reason', 'Or it’s their way'),
    'If you can’t do monogamy, it’s still more honest':
        ('admitting you can’t do monogamy is more honest than faking it', 'what is still true', 'monogamy'),
    'Sometimes all that pretending':
        ('the pretending can do more damage than the other relationship would', 'why honesty matters here',
         'all that pretending'),
    # Romance 285 to 287
    'The same is true for a woman.':
        ('the same holds for a woman', 'opens the paragraph, tying back to the man', None),
    'She shouldn’t have to play the damsel':
        ('she shouldn’t have to act helpless to prove she’s feminine', 'what that means for her', 'She'),
    'Her surrender means a lot more':
        ('her surrender means more when she could take charge', 'the other side of it', 'Her surrender'),
    'She may worry that I don’t find her beautiful enough, or that she’s too much':
        ('she may worry she isn’t beautiful enough for me, or is too much', 'one direction', 'She may worry'),
    'Maybe she thinks she cries too easily':
        ('she may think she’s too emotional, needy or illogical for me', 'what “too much” means', 'Maybe she thinks'),
    'Then she can swing the other way':
        ('then she may act like she needs nobody', 'the other direction', 'Then she can swing the other way'),
    'Letting a man take care of her starts to feel like weakness':
        ('then receiving care or letting a man lead feels weak to her', 'what that does', 'Letting a man'),
    'Letting a man help her, or lead for a while':
        ('a strong woman stays strong when she lets a man help or lead', 'what is so', 'Letting a man help her'),
    'So does lying back while he pleases her':
        ('receiving pleasure leaves her strong too', 'the same for pleasure', 'So does'),
    'And a man she takes care of stays a grown man':
        ('a man she takes care of is still a man', 'the same for a man', 'And a man'),
    'Sometimes it’s as simple as a woman who drives just fine':
        ('it can be as simple as her asking me to drive because she likes it', 'an everyday example',
         'Sometimes it’s as simple as'),
    'She’s choosing the ride':
        ('she chooses it', 'what the example shows', 'the ride'),
    'Or I might ask, “Honey, how do you see this intuitively?” because I want':
        ('I may ask her intuition because I want her to use her power', 'an example the other way', 'Or I might ask'),
    'She might have me think through the practical side':
        ('she may want my help with the practical side', 'her side of it', 'the practical side'),
    # Idealization 148
    'Once the BPD splitting kicks in':
        ('when the BPD splitting starts, worship can turn to private hatred', 'what the extreme leads to',
         'BPD splitting'),
    'Then come the public accusations':
        ('then come public accusations', 'what follows', 'Then'),
    'She rewrites our whole history':
        ('she rewrites the past and reads every flaw as a sign I was fake', 'more of what follows', 'She rewrites'),
}
META = {
    'r21-spir': ('Can making love be a spiritual practice?',
                 'A Buddhist or spiritual seeker wondering whether married life and sex rule out serious awakening.',
                 'It tells the reader serious awakening isn’t only for monks, and that sex itself may be a path.'),
    'r21-jeal366': ('Jealousy (366 to 370)', 'Someone in, or weighing, a monogamous or polyamorous relationship.',
                    'It tells the reader which kind of honesty each kind of relationship needs.'),
    'r21-rom284': ('Romance (284 to 288)', 'A woman or man wondering how strength and surrender fit together.',
                   'It tells the reader that letting a partner lead or care for you is a choice, not weakness.'),
    'r21-ideal147': ('Beware idealization (147 and 148)', 'Someone being idealized by a new partner.',
                     'It tells the reader why too much idealization is a warning sign.'),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these paragraphs tell; they give no advice beyond what the live post gives',
    'Q3': 'PASS: the people, texts and practices are named as in the live post',
    'Q4': 'PASS: no new term; BPD is used earlier in the article',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or it opens its paragraph',
    'Q6': 'PASS: the order is the live post’s',
    'Q7': 'PASS: each change keeps what the paragraph tells the reader',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence',
}
LOW = {
    'r21-spir': [{'point': 'S17’s AI windows', 'found': 'the section check #45 and his own check of S17 (0e2f8a68, Human '
                  'High)', 'still_needed': 'yes', 'fate': 'changed'}],
    'r21-jeal366': [{'point': 'the AI windows on 367 to 369 and the Low ones on 366 and 370', 'found': 'the section check '
                     '#94', 'still_needed': 'yes', 'fate': 'changed'}],
    'r21-rom284': [{'point': 'the AI windows on 285 to 287 and the Low ones beside them', 'found': 'the section check '
                    '#98', 'still_needed': 'yes', 'fate': 'changed'}],
    'r21-ideal147': [{'point': 'the AI windows on 148 and the Low one on 147’s end', 'found': 'the pair check #93',
                      'still_needed': 'yes', 'fate': 'changed'}],
}
PLACE = {
    'r21-spir': 'The whole section, 304 to 317, as #45 had it, with r20’s 304 to 308 and his S17 in it.',
    'r21-jeal366': '366 to 370: the new 367 to 369 with the paragraph before and after it (E349).',
    'r21-rom284': '284 to 288: the new 285 to 287 with the paragraph before and after it (E349).',
    'r21-ideal147': '147 with the new 148 (148 alone is under the web app’s 50 words).',
}
bad = 0
(HERE / 'CHECK-r21-bypass.txt').write_text(TEXTS['r21-bypass'], encoding='utf-8')
for name in META:
    text = TEXTS[name]
    section, reader, why = META[name]
    r = S.make(text, section, reader)
    for s in r['sentences']:
        row = next((v for k, v in NEW.items() if s['s'].startswith(k)), None) or OLD.get(s['s'].strip())
        assert row, ('no row', name, s['s'][:60])
        pay, fol, link = row
        s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
        s['follows'] = fol
        if 'link' in s:
            s['link'] = link or 'none: it opens its paragraph, and the paragraph before it ends its own point'
    r['opens']['why_reading'] = why
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = LOW[name]
    r['placement'] = PLACE[name]
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
