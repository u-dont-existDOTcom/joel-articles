"""Neuro De-Armoring Cards, 7 November (2): his three answers that needed another version.

His answers of 13:10 UTC (`../x1107a/ANSWERS-X1107A-20261107-1310.json`): five cards approved and in the article,
SB-38 and SB-40 marked revise, SB-37 approved with a question its last sentence didn't answer.

- "when you are editing the guide, you don't want to keep the old junk in there and argue with the guide itself, we
  want a public-facing document which makes sense and is not confusing."
- "if you are stating that something is a hypothesis then you have to explain how the hypothesis does or doesn't make
  sense, otherwise it's useless. and if apathy and schizotypy have never been tested, why are those in there, is
  there a reason other than gemini wrote something about them?"
- "why would you say it's a vacuum then say it's not a vacuum? arguing with yourself again here."
- SB-37: "you mean it is the over-excitement of the neurons or psychological over-excitement? if it's psychological
  over-excitement you'd need to explain how that's not a tautology ... i can be overly joyful without being rageful"

  python3 articles/neuro-de-armoring/humanize/fix-20261107/sci/x1107b/build_x1107b.py
Writes each text and receipt, then REVIEW-X1107B.json, .html, .artifact.html and .md here.
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402
import texts_b as T  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261107/sci/x1107b/'
TABLE = BLOB + LANE + 'fix-20261107/sci/x1107a/SCIENCE-SECTION-B.md'
GIT_FILE = REL + 'REVIEW-X1107B.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
HIS38 = 'https://www.pangram.com/history/f2a4727d-a109-46d4-a907-40efa6350e96'
JHU = ('https://www.hopkinsmedicine.org/news/newsroom/news-releases/2025/09/'
       'scientists-find-potential-new-drug-target-for-psychiatric-and-neurological-disorders')
ITOH = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11295041'

TYPES = {
    'science': {'label': 'A claim corrected',
                'about': 'What the article says here doesn\'t match its sources, or says as fact what is a guess. The '
                         'card has the paragraph as it would read, with the source for each claim.'},
    'coherence': {'label': 'The guide contradicting itself',
                  'about': 'A place where the guide names a thing one way and then says it isn\'t that, which a reader '
                           'has to work through for nothing.'},
}
SECTION = 'B. The "Overheating" CPU: Glutamate Excitotoxicity'
READER = ('someone with trauma armor who is about to take NAC, zinc, magnesium, L-serine or D-serine to calm a '
          'glutamate storm and to make therapy sessions stick, and wants to know what each one actually does')
SAME_B = ('none: read section B from its heading to section C for the glutamate mechanism, GluD, D-serine and the '
          'fixes; each point here is made once in the section')
PASS_ALL = {
    'Q2': 'N/A: no instruction in this paragraph; it explains a mechanism',
    'Q3': 'PASS: each thing is named exactly (NMDA receptors, the amygdala, GluD receptors, D-serine, GABA, cystine)',
    'Q5': 'PASS: each "so", "and" and "because" turns on the clause before it',
    'Q7': 'PASS: each fact is about the chemistry the reader is about to change with the protocol',
    'Q8': 'N/A: no group or list in this paragraph',
    'Q9': 'PASS: one step a clause, with the small words that carry the relation kept',
}


def plain(md):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md))


R = {
    'B37b': {
        'placement': 'third paragraph of section B, after the Problem (glutamate floods the brain under stress); it '
                     'says what that flood does, before the GluD paragraph',
        'opens': 'it tells the reader what a glutamate flood does to their brain cells: the key stuck "On" and the '
                 'calcium pouring in',
        's': [
            ('the reader learns what over-activation does, and what an NMDA receptor is',
             'it opens the paragraph after the Problem names the flood', None),
            ('the reader learns cells die only in extreme cases, and what "excitotoxicity" means',
             'it says what that calcium does when it is extreme', 'that calcium overload'),
            ('the reader learns why the storm feels like threat and not like excitement: the circuit it reaches is '
             'the threat detector', 'it answers what the extreme case left open, what the reader actually feels',
             'What you feel from a glutamate storm'),
            ('the reader learns the claim has a test behind it: block those receptors and anxious behaviour drops',
             'it gives the evidence for the sentence before', 'the NMDA receptors there'),
        ],
        'checked': [{'point': 'the feeling of a glutamate storm is "the over-excitement itself"',
                     'found': 'stress raises glutamate in the amygdala, the threat detector (Wilson 2015), and NMDA '
                              'blockers there lower anxious behaviour (Boyle 2013)',
                     'still_needed': 'yes: he asked what the excitement is, since joy is excitement too',
                     'fate': 'changed'}],
        'q': {'Q1': 'PASS: each sentence opens on its subject (glutamate, extreme cases, what you feel, the test)',
              'Q4': 'PASS: NMDA receptors as the doors glutamate unlocks; the amygdala as the part that flags '
                    'threats; excitotoxicity where it is named',
              'Q6': 'PASS: what happens, when it kills, what it feels like and why, the evidence'},
    },
    'B38b': {
        'placement': 'fourth paragraph of section B, after the NMDA mechanism, which its "So if NMDA is the spark" '
                     'points back to; before the D-serine paragraph, which it sets up',
        'opens': 'it asks the reader\'s own next question after the NMDA paragraph: is anything else turning the '
                 'signal up or down',
        's': [
            ('the reader is asked whether anything besides NMDA sets the level, the question the paragraph answers',
             'it follows the NMDA paragraph, which it names as the spark', None),
            ('the reader learns what GluD receptors are and that D-serine, one of the tools below, opens them',
             'it answers the question just asked', 'Well according to'),
            ('the reader learns the one pattern measured in people: the channel sticks open and leaks',
             'it moves from what the receptor is to what goes wrong with it', 'has been measured'),
            ('the reader learns the two cases that show it', 'it names the cases for the pattern just stated',
             'That is what'),
            ('the reader learns what the armor guess is and why it makes sense: a floor the signal can\'t drop below '
             'is what hyper-vigilance would be', 'it extends the measured pattern to the armored state',
             'jams the dial the same way'),
            ('the reader learns it is untested and testable, so they can hold it as a guess',
             'it says what the guess still needs', 'Nobody has tested that'),
        ],
        'checked': [{'point': 'GluD is a "master volume knob" setting the synapse\'s baseline hum',
                     'found': 'GluD2 is a channel opened by D-serine and GABA (Wang 2025)',
                     'still_needed': 'yes: it is why D-serine matters here', 'fate': 'changed'},
                    {'point': 'in an armored state the dial jams High (ataxia, hyper-vigilance) or Low (apathy, '
                              'schizotypy)',
                     'found': 'what is measured in people is a channel stuck open: the ataxia mutation, and a '
                              'schizophrenia-risk variant of GluD1 (Allen 2023). Nothing puts apathy or schizotypy on '
                              'a "Low" setting',
                     'still_needed': 'yes for the High side, as his hypothesis with its mechanism; no for the Low '
                                     'side', 'fate': 'changed'}],
        'q': {'Q1': 'PASS: the question first, then the finding, the pattern, its cases, the guess and its test',
              'Q4': 'PASS: channels, GABA as the brain\'s calming chemical, ataxia as inherited, and the leak '
                    'explained as a floor the signal can\'t drop below',
              'Q6': 'PASS: question, what it is, what goes wrong, where that is seen, the guess, what would test it'},
    },
    'B40b': {
        'placement': 'first of the Fix\'s items in section B, after the D-serine paragraph; its label carries the Fix '
                     'heading as the article has it',
        'opens': 'it tells the reader what NAC does: it cuts how much glutamate is fired into the synapse',
        'same': 'none: read the Fix list from its heading to section C for what each tool does; NAC appears once in it',
        's': [
            ('the reader learns how NAC turns glutamate release down, through the swap and the brake',
             'it opens the Fix list, under its label', None),
        ],
        'checked': [{'point': 'NAC "clears the flood by exchanging glutamate for cystine" (the Vacuum)',
                     'found': 'the swap raises glutamate outside the synapse, which trips mGluR2/3 and cuts release '
                              'into it (Moran 2005, rats)', 'still_needed': 'yes: it is the first fix',
                     'fate': 'changed'}],
        'q': {'Q1': 'PASS: the label says what it is, then the sentence says how',
              'Q4': 'PASS: cystine as an amino acid, mGluR2/3 named as the brake, support cells for glia',
              'Q6': 'PASS: the swap, then what it trips, then the effect'},
    },
    'B119b': {
        'reader': 'someone setting up the anxiety (Glutamate Shield) part of the daily protocol and choosing doses',
        'placement': 'the NAC line of the Glutamate Shield list, with its dose',
        'opens': 'it gives the reader the NAC dose they are about to take',
        'same': 'none: read the Glutamate Shield list from its heading to the next for the doses; NAC is listed once',
        's': [
            ('the reader gets the NAC dose, split through the day', 'it is the list item for NAC', None),
            ('the reader learns what the dose does', 'it gives the reason for the dose before it',
             'none: a list item\'s note on the dose just given, which the reader reads with it'),
        ],
        'checked': [{'point': 'NAC "mops up glutamate"',
                     'found': 'it cuts synaptic glutamate release through mGluR2/3 (Moran 2005)',
                     'still_needed': 'yes', 'fate': 'changed'}],
        'q': {'Q1': 'PASS: the dose first, then the reason', 'Q2': 'PASS: the dose is the instruction, with its reason',
              'Q4': 'PASS: no new term', 'Q6': 'PASS: dose, then what it does',
              'Q8': 'PASS: NAC belongs in the Glutamate Shield list'},
    },
}


def receipts():
    out = {}
    for key, md in T.TEXTS.items():
        text = plain(md)
        d = R[key]
        r = S.make(text, SECTION if key.startswith('B3') or key == 'B40b' else key, d.get('reader', READER))
        sents = S.sentences(text)
        assert len(sents) == len(d['s']), (key, len(sents), len(d['s']))
        for x, (pay, fol, link) in zip(r['sentences'], d['s']):
            x['payoff'], x['follows'] = pay, fol
            if 'link' in x:
                x['link'] = link if link else 'none: it opens on its own subject'
        r['placement'] = d['placement']
        r['opens']['why_reading'] = d['opens']
        r['same_point'] = d.get('same', SAME_B)
        r['checked'] = d['checked']
        q = dict(PASS_ALL)
        q.update(d['q'])
        r['questions'] = q
        (HERE / ('%s.txt' % key)).write_text(text + '\n', encoding='utf-8')
        (HERE / ('%s.receipt.json' % key)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n',
                                                      encoding='utf-8')
        probs = S.check(text, r)
        for p in probs:
            print(key, 'RECEIPT PROBLEM', p)
        out[key] = bool(probs)
    return out


def block(prefix):
    hits = [b['i'] for b in BL if b['text'].startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def card(sid, typ, title, pairs, what, why, stays, deciding, note, ask_because, approve_label=None):
    edits = []
    for key, prefix in pairs:
        i = block(prefix)
        edits.append({'block': i, 'before': sr.block_text(BL, i), 'after': plain(T.TEXTS[key])})
    s = {'id': sid, 'type': typ, 'title': title, 'advice': 'approve',
         'spans': [{'block': e['block'], 'start': 0, 'end': len(e['before'])} for e in edits],
         'edits': edits, 'what': what, 'why': why, 'stays': stays, 'deciding': deciding, 'advice_note': note,
         'ask_because': ask_because,
         'found_by': 'Your answers of 13:10 UTC, and section B\'s science pass ([the table](%s))' % TABLE,
         'receipt': [REL + '%s.receipt.json' % k for k, _ in pairs]}
    if approve_label:
        s['approve_label'] = approve_label
    return s


def main():
    bad = receipts()
    S_ = [
        card('SB-37b', 'science', 'What the storm feels like, and why it isn\'t joy',
             [('B37b', 'The Mechanism: Excess')],
             'The last sentence is replaced. Instead of "the over-excitement itself" it says which circuit the storm '
             'reaches, the amygdala, the part that flags threats, which is why the feeling comes out as threat and '
             'not as pleasure; and it gives the animal evidence. The rest of the paragraph is as you approved it.',
             'You\'re right that "over-excitement" explains nothing: joy is excitement too. What the research gives is '
             'the circuit, not the amount. Under stress the glutamate rise reaches the amygdala '
             '([Wilson, 2015](%s)), whose job is flagging threats, and blocking NMDA receptors there lowers anxious '
             'behaviour in animals ([Boyle, 2013](%s)). So the feeling follows which circuit is firing too hard, '
             'which is answerable rather than circular.' % (T.WILSON, T.BOYLE),
             'The first two sentences exactly as you approved them, with the calcium correction and the "key stuck in '
             'the On position".',
             'Whether the paragraph explains the feeling by the circuit, and whether that reads clearly to you.',
             'Approve.',
             'meaning: it changes what the article says the storm is, from an amount of excitement to the circuit the '
             'rise reaches, and adds the animal evidence for it'),
        card('SB-38b', 'science', 'GluD: one direction in the research, the guess with its reason, apathy and '
             'schizotypy out', [('B38b', 'The Signal Dial')],
             'No arguing with the sources in the text. It states the finding, then the one pattern measured in people '
             '(the channel sticks open and leaks), the two cases that show it, your armor guess with the reason it '
             'makes sense, and that it is untested and testable. "Low", apathy and schizotypy come out.',
             'Your two questions, answered. **Why apathy and schizotypy were in there:** no reason beyond Gemini. '
             'Nothing in the research puts a GluD setting on "Low" and those states; the news story mentions GluDs '
             'looking less active in schizophrenia, but the measured variant goes the other way, so a "Low" row in '
             'your dial has nothing behind it. **How the hypothesis makes sense:** what has actually been put under '
             'the microscope in people is a channel stuck open, leaking current with no signal coming in. That is the '
             'ataxia mutation, and a GluD1 variant carried by people at raised risk of schizophrenia does the same '
             '([Allen, et al, 2023](%s)). A channel that leaks gives the synapse a floor it can never drop below, '
             'which is exactly what hyper-vigilance is as an experience, so "jammed on High" has a mechanism under it '
             'rather than a name. And it is testable: the same paper found a drug that shuts those leaking channels '
             'in the lab. I left the dispute out of the text: one lab\'s tests found no direct opening '
             '([Itoh, et al, 2024](%s)), which is why the Nature paper matters, but a reader doesn\'t need me '
             'arguing with it.' % (T.ALLEN, ITOH),
             'Your opening question, your "Well according to", the label, and High as hyper-vigilance.',
             'Whether the Low side goes. If you want apathy kept, it would be as your own clinical observation, not '
             'as something the GluD research says.',
             'Approve. The version you fixed on 7 November read Human ([that check](%s)), so I humanize this one '
             'keeping those moves and check it then.' % HIS38,
             'meaning: it drops the "Low" row of your dial and says the armor part is a guess; downside: apathy and '
             'schizotypy leave the article, and you may want them on your own clinical grounds'),
        card('SB-40b', 'coherence', 'Call it the Brake, since that\'s what it does',
             [('B40b', 'The Fix ("Lock'), ('B119b', 'NAC: 1.8g')],
             'The label changes from "The Vacuum (NAC)" to "The Brake (NAC)", and the line just says how the brake '
             'works, with nothing about vacuums. The NAC dose line\'s note becomes "Turns down glutamate release"; '
             'the dose stays as it is.',
             'You\'re right, that was me arguing with the guide in front of the reader. The mechanism is a brake: the '
             'swap NAC drives puts more glutamate outside the synapse, and that trips mGluR2/3, which cuts how much '
             'is fired into it ([Moran, et al, 2005](%s)). So the label should say brake and the sentence should just '
             'explain it.' % T.MORAN,
             'The "Lock, Stock, and Barrel" heading and the dose, 1.8g – 2.4g (divided doses).',
             'Whether the Vacuum label goes. If you want it kept I will make the sentence fit it instead.',
             'Approve.',
             'downside: the Vacuum label goes, so the Fix list loses one of its names and anyone who read the post '
             'before sees a different word',
             approve_label='use this and rename it the Brake'),
    ]
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261107-x1107b',
        'title': 'Neuro De-Armoring Cards, 7 November (2): your three answers',
        'intro': [
            'Your five approved cards are in the article. These are the three that needed another version: SB-38 and '
            'SB-40, which you marked revise, and SB-37\'s last sentence, which didn\'t answer your question.',
            'Still not humanized and still not checked in Pangram: once the claims are settled I humanize each one '
            'and check it then.',
            'No compound, dose, unit, timing or warning changes on this page. Leucine is out of the article, as you '
            'said.',
        ],
        'git_file': GIT_FILE,
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1107B.md'},
        'types': TYPES,
        'suggestions': S_,
    }
    probs = sr.check(review, BL)
    for x in probs:
        print('PROBLEM', x)
    (HERE / 'REVIEW-X1107B.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n',
                                             encoding='utf-8')
    if probs or any(bad.values()):
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1107B.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1107B.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for s in S_:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '']
        for e in s['edits']:
            md += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
                   '**As it would read:**', '', '> %s' % e['after'], '']
        md += ['**What changes:** %s' % s['what'], '', '**Why:** %s' % s['why'], '',
               '**What stays:** %s' % s['stays'], '', '**You\'re deciding:** %s' % s['deciding'], '',
               '**My advice:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1107B.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [x['id'] for x in S_])
    return 0


if __name__ == '__main__':
    sys.exit(main())
