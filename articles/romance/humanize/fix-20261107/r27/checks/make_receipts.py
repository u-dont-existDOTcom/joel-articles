#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r27's checks (texts.py). A sentence an earlier receipt in this article already
has a row for keeps it; the rest, his T2 answer's sentences and S17's two changed ones, are written here. Writes
RECEIPT-<name>.json and checks each; exits 1 if one fails."""
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
    if '/r27/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))
NEW = {
    'And even better than simply suppressing it': (
        'a better way than suppressing outside attraction: Esther Perel says that energy can be redirected into the '
        'relationship to make it more alive', 'the choice not to act on attraction (366)', 'even better than simply suppressing it'),
    'And even better than simply suppressing it, they can put it to work.': (
        'better than suppressing outside attraction, a couple can put that energy to use', 'the choice not to act on '
        'attraction (366)', 'even better than simply suppressing it'),
    'I agree with Esther Perel, who writes': (
        'Esther Perel says that energy can be redirected into the relationship to make it more alive, and he agrees',
        'putting the attraction to work', 'this sexual energy'),
    'That exaggerated version shouldn’t have to happen, though': (
        'being idealized is a bad shortcut to the divine archetypes, so the knight-and-muse story is no model to copy',
        'the director/muse dynamic playing out in an exaggerated way', 'That exaggerated version'),
    'The degree of idealization also predicts the degree of demonization for me': (
        'the more someone idealizes him, the more they later demonize him, and he uses that as a working warning sign',
        'what real appreciation is (146)', 'also'),
    'When the BPD splitting happens, she flips': (
        'what the flip looks like: worship turns to hatred, first in private, then in public',
        'the woman who finds no flaw', 'When the BPD splitting happens'),
    'Suddenly she finds plenty of flaws': (
        'once it flips, every flaw she finds becomes her reason to think he faked it all along', 'the flip to hating him',
        'Suddenly'),
    'I’m happy to, since maybe I do talk about them too much': (
        'how he meets a partner halfway on a real flaw she finds: he can talk about his exes less',
        'her asking him to talk less about his exes', 'I’m happy to'),
    'But I still care about them, and if I’m supposed to listen': (
        'his limit: he still cares about them, and won\'t pretend they aren\'t on his mind while he listens to all of hers',
        'agreeing to talk less about them', 'But I still care about them'),
    'She shouldn’t need a knight in shining armor to bring that beauty out': (
        'being idealized as a rescuer is a bad shortcut to the divine archetypes, so the knight-and-muse story is no '
        'model to copy', 'the director/muse dynamic playing out in an exaggerated way', 'knight in shining armor'),
    'When the BPD splitting kicks in, she goes from': (
        'what the flip looks like: “you’re perfect” turns into “you’re a fraud,” first in private, then in public',
        'the woman who finds no flaw', 'When the BPD splitting kicks in'),
    'Suddenly she can see every flaw I have': (
        'once it flips, she sees every flaw and decides he faked it all along', 'the flip', 'Suddenly'),
    'But I still care about them, and if I’m gonna listen': (
        'his limit: he still cares about them, and if he listens to all that is on her mind, she has to hear some of his',
        'agreeing to talk less about them', 'But I still care about them'),
    'But I still care about them, and I’m not gonna act like they never cross my mind': (
        'his limit: he still cares about them and won\'t pretend they never cross his mind while he listens to all of hers',
        'agreeing to talk less about them', 'But I still care about them'),
    'Imagine if you and your partner both saw': (
        'what it would be like if both partners treated outside attractions as energy, not a threat',
        'Perel\'s redirected energy', 'those outside attractions'),
    'It sure would beat beating around the bush': (
        'that would beat dodging the subject out of fear and jealousy', 'the imagined couple', 'It sure would beat'),
    'You can start playing around with opening up': (
        'a first step: mention small passing attractions instead of hiding until a big crush gets confessed',
        'beating around the bush', 'opening up'),
    'Lots of couples promise forever to each other': (
        'many couples promise lifelong exclusivity', 'his small-attractions advice, as the next topic: what gets promised',
        'none: it opens its paragraph, and the paragraph before it ends its own point'),
    'On the other hand, in a polyamorous relationship': (
        'in polyamory the boundaries are more negotiable, but someone has to negotiate them, down to who stays the night',
        'how few live up to the promise', 'On the other hand'),
    'That can end up sometimes creating more drama': (
        'that negotiating can make more drama than it is worth', 'the negotiating', 'That can end up'),
    'Polyamory can also be a way of escaping deeper intimacy': (
        'polyamory can be a way to escape deeper intimacy, as with his college friend who had 4 girlfriends and was '
        'deeply unhappy', 'the drama of negotiating', 'can also be'),
    'Or it can be a way of escaping guilt': (
        'or a way to escape guilt, when a cheater finally announces being poly as if that undid the dishonesty',
        'escaping intimacy', 'Or it can be'),
    'But they are right to finally come clean': (
        'coming clean is still right, and can stop the dishonesty from here on', 'the cheater who comes out as poly', 'But they are right'),
    "Some of it I just thought through, and I'm still not sure": (
        'some of it he only thought through, and he is not sure of all of it', 'learning most of it by screwing up', 'Some of it'),
    'Her jade-egg practice is a preliminary training': (
        'her jade-egg practice trains the pelvic floor and attention for the cervical O', 'the students\' stories', 'Her jade-egg practice'),
    'Brad and Pam Keene are the couple I really liked': (
        'Brad and Pam Keene are his favourite example of her method', 'her practice and students', 'her method'),
}
META = {
    'r27-jeal': ('Jealousy on trial (357 to 370)', 'Someone dealing with jealousy, or weighing monogamy against polyamory.',
                 'It tells the reader what jealousy is telling them and which kind of honesty each relationship needs.'),
    'r27-jeal-b': ('Jealousy on trial (357 to 370)', 'Someone dealing with jealousy, or weighing monogamy against polyamory.',
                   'It tells the reader what jealousy is telling them and which kind of honesty each relationship needs.'),
    'r27-ideal': ('Beware idealization in either direction (143 to 151)',
                  'Someone who idealizes a partner, or is being put on a pedestal by one, and can\'t tell it from love.',
                  'It tells the reader how to tell real appreciation from idealization, and why a pedestal warns of a fall.'),
    'r27-ideal-b': ('Beware idealization in either direction (143 to 151)',
                  'Someone who idealizes a partner, or is being put on a pedestal by one, and can\'t tell it from love.',
                  'It tells the reader how to tell real appreciation from idealization, and why a pedestal warns of a fall.'),
    'r27-p145': ('Beware idealization in either direction, 145',
                  'Someone who idealizes a partner, or is being put on a pedestal by one, and can\'t tell it from love.',
                  'It tells the reader how to tell real appreciation from idealization, and why a pedestal warns of a fall.'),
    'r27-p148': ('Beware idealization in either direction, 148',
                  'Someone who idealizes a partner, or is being put on a pedestal by one, and can\'t tell it from love.',
                  'It tells the reader how to tell real appreciation from idealization, and why a pedestal warns of a fall.'),
    'r27-p151': ('Beware idealization in either direction, 151',
                  'Someone who idealizes a partner, or is being put on a pedestal by one, and can\'t tell it from love.',
                  'It tells the reader how to tell real appreciation from idealization, and why a pedestal warns of a fall.'),
    'r27-ideal-c': ('Beware idealization in either direction (143 to 151)',
                    'Someone who idealizes a partner, or is being put on a pedestal by one, and can\'t tell it from love.',
                    'It tells the reader how to tell real appreciation from idealization, and why a pedestal warns of a fall.'),
    'r27-spir': ('Can making love be a spiritual practice?', 'Someone wondering whether sex and spiritual practice fit.',
                 'It tells the reader whether a couple can make sex part of a spiritual path, with the evidence he has.'),
}
Q = {
    'Q1': 'PASS: each sentence gives its point first, in plain words (his own wording, three slips fixed)',
    'Q2': 'PASS: the advice is his, as he wrote it',
    'Q3': 'PASS: the people are named as he named them',
    'Q4': 'PASS: no new term; "poly" follows "polyamorous" in the same paragraph pair',
    'Q5': 'PASS: each sentence\'s tie is in its words (the links field), or it opens its paragraph',
    'Q6': 'PASS: the order is his',
    'Q7': 'PASS: each fix keeps what the sentence tells the reader',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence',
}
LOW = {
    'r27-jeal': [{'point': 'the AI windows on 366 to 370', 'found': 'the section checks #83, #94, #133, #134',
                  'still_needed': 'yes: they get the section\'s advice on monogamy and polyamory, now in his words',
                  'fate': 'changed'}],
    'r27-jeal-b': [{'point': '366\'s comparison with nothing to attach to', 'found': 'the sense read (whole/sense-r27)',
                    'still_needed': 'yes: they get what is better than suppressing an attraction', 'fate': 'changed'}],
    'r27-ideal': [{'point': 'the five Human Low windows of #132 (145, 147, 148, 151)', 'found': '#132',
                   'still_needed': 'yes: they get the warning signs of idealization, now said plainly', 'fate': 'changed'}],
    'r27-ideal-b': [{'point': '#138\'s AI Low windows on 148 and 151 and Low on 145 and 148\'s last', 'found': '#138',
                     'still_needed': 'yes: they get the warning signs of idealization, said as what people say and do',
                     'fate': 'changed'}],
    'r27-spir': [{'point': 'none: #118 read one Human High window', 'found': '#118',
                  'still_needed': 'yes: they see one couple the method worked for', 'fate': 'kept'}],
}
PLACE = {'r27-jeal': 'The whole section, 357 to 370, with his T2 answer for 366 to 370.',
         'r27-ideal': 'The whole section, 143 to 151, as #132 checked it but for 145, 147, 148 and 151.',
         'r27-jeal-b': 'The whole section as r27-jeal, with 366\'s comparison given what it compares.',
         'r27-spir': 'The whole section as #118 checked it, with his doubled "example" taken out.'}
# The fresh reader's needed read (a Sonnet subagent given needed_read_brief.md, the seven changed paragraphs, their
# headings and what each is for; 2026-11-08). Nothing is cut: each sentence it listed is his, kept for what it does.
READER = ('a fresh reader (a Sonnet subagent that saw only the changed paragraphs, their headings and what they are '
          'for, given tools/humanization/needed_read_brief.md), 2026-11-08')
NEEDED = {
    'r27-jeal': {'reader': READER, 'unneeded': [
        'It sure would beat beating around the bush because of fear and jealousy.',
        'I learned most of this by screwing it up.',
        "Some of it I just thought through, and I'm still not sure about all of it."],
        'kept': {
        'It sure would beat beating around the bush because of fear and jealousy.':
            'they hear why hiding attractions costs something: fear and jealousy are what make people dodge the '
            'subject (his pun, on his keep-as-is list)',
        'I learned most of this by screwing it up.':
            'they know how much weight to give the advice before them: he learned it from his own mistakes',
        "Some of it I just thought through, and I'm still not sure about all of it.":
            'they know which of it is untested, so they test it for themselves instead of taking it as settled'}},
    'r27-spir': {'reader': READER, 'unneeded': ['No partner required for the jade egg phase.'], 'kept': {
        'No partner required for the jade egg phase.':
            'they learn a reader without a partner can start the practice now (his line, read High in #118)'}},
}
NEEDED['r27-jeal-b'] = NEEDED['r27-jeal']
for _k in ('r27-ideal-b', 'r27-ideal-c', 'r27-p145', 'r27-p148', 'r27-p151'):
    LOW[_k] = LOW.get(_k) or [{'point': 'this paragraph\'s window in #138', 'found': '#138',
                               'still_needed': 'yes: they get the warning signs of idealization, said plainly',
                               'fate': 'changed'}]
    PLACE[_k] = PLACE.get(_k) or 'By itself, as it sits in r27-ideal-b (E343: narrowed after the section read Mixed).'
NEEDED['r27-ideal'] = {'reader': READER, 'unneeded': [
    'Sometimes she ends up accusing me of thinking I’m perfect, when she’s the one who used to say I was.',
    'I’m happy to, since maybe I do talk about them too much sometimes.',
    'But I still care about them, and if I’m supposed to listen to everything on her mind, I don’t want to pretend they '
    'aren’t on mine.'], 'kept': {
    'Sometimes she ends up accusing me of thinking I’m perfect, when she’s the one who used to say I was.':
        'they learn to expect the reversal: the one who put them on the pedestal later accuses them of standing on it',
    'I’m happy to, since maybe I do talk about them too much sometimes.':
        'they see what happens once a partner who isn\'t idealizing finds a real flaw (149: she hasn\'t found all of me '
        'until something bothers her): she asks, and he meets her partway',
    'But I still care about them, and if I’m supposed to listen to everything on her mind, I don’t want to pretend they '
    'aren’t on mine.':
        'they see where meeting her partway stops: he won\'t pretend to be someone without that flaw'}}
for _k in ('r27-ideal-b', 'r27-ideal-c', 'r27-p145', 'r27-p148', 'r27-p151'):
    NEEDED[_k] = dict(NEEDED['r27-ideal'], reader=READER + '; the same paragraphs\' jobs, reworded after #138')
bad = 0
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
    r['needed'] = NEEDED[name]
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
