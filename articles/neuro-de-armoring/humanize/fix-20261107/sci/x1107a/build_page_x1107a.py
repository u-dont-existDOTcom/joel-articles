"""Neuro De-Armoring Cards, 7 November: section B's science, first.

His message of 2026-11-07 01:00 UTC: "the first thing before humanizing a science article is to make sure the science is
right (saying it's speculative if it's speculative, but making sure the speculation makes sense)". Each card is a claim
corrected in section B (blocks 37 to 42) or in a place later that rests on one (blocks 119 and 148), made as a small edit
to the paragraph as it stands (block 38: to his own humanized version). They are claim changes, so they go to him
(AGENTS.md: "a card is for what has a real tradeoff: a changed claim"). None has had a humanizing pass or a Pangram
check yet (gate neuro-2026-11-07c): that comes after he approves the claims.

  python3 articles/neuro-de-armoring/humanize/fix-20261107/sci/x1107a/receipts.py
  python3 articles/neuro-de-armoring/humanize/fix-20261107/sci/x1107a/build_page_x1107a.py
Writes REVIEW-X1107A.json, .html, .artifact.html and .md beside this file.
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import suggestion_review as sr  # noqa: E402
import texts as T  # noqa: E402
from receipts import plain  # noqa: E402

BRANCH = 'main'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261107/sci/x1107a/'
GIT_FILE = REL + 'REVIEW-X1107A.html'
TABLE = BLOB + REL + 'SCIENCE-SECTION-B.md'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
HIS38 = 'https://www.pangram.com/history/f2a4727d-a109-46d4-a907-40efa6350e96'

TYPES = {
    'science': {'label': 'A claim corrected',
                'about': 'What the article says here doesn\'t match its sources, or says as fact what is a guess. The '
                         'card has the paragraph with the claim corrected and the source for it.'},
    'cut': {'label': 'A claim cut',
            'about': 'A claim whose reason doesn\'t hold up, which I would take out.'},
}


def block(prefix):
    hits = [b['i'] for b in BL if b['text'].startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def rec(*keys):
    return [REL + '%s.receipt.json' % k for k in keys]


def card(sid, typ, title, i, key, what, why, stays, deciding, note, extra_edits=(), approve_label=None):
    before = sr.block_text(BL, i)
    edits = [{'block': i, 'before': before, 'after': plain(T.TEXTS[key])}]
    keys = [key]
    for j, k in extra_edits:
        edits.append({'block': j, 'before': sr.block_text(BL, j), 'after': plain(T.TEXTS[k])})
        keys.append(k)
    s = {'id': sid, 'type': typ, 'title': title, 'advice': 'approve',
         'spans': [{'block': e['block'], 'start': 0, 'end': len(e['before'])} for e in edits],
         'edits': edits, 'what': what, 'why': why, 'stays': stays, 'deciding': deciding, 'advice_note': note,
         'found_by': 'This turn\'s science pass of section B ([the table, with every source](%s))' % TABLE,
         'receipt': rec(*keys)}
    if approve_label:
        s['approve_label'] = approve_label
    return s


def main():
    i37, i38, i39 = block('The Mechanism: Excess'), block('The Signal Dial'), block('D-serine may support')
    i40, i41, i42 = block('The Fix ("Lock'), block('The Lock (Zinc'), block('The Repair (Leucine')
    i119, i148 = block('NAC: 1.8g'), block('Use D-Serine for acute')

    S = [
        card('SB-37', 'science', 'Excitotoxicity is calcium overload, not cells "vibrating to death"', i37, 'B37',
             'Cells die because over-activated NMDA receptors let too much calcium in, and that happens in extreme '
             'cases like a stroke or a brain injury. The feelings stay, said as the over-excitement itself rather '
             'than neurons dying. NMDA receptors get a few words of explanation where they first come up in the '
             'section.',
             'Nothing vibrates: the cell is killed by the calcium the receptor lets in, and it matters in strokes, '
             'brain injury and neurodegeneration ([Sattler & Tymianski 2001](%s)). Nothing I found ties anxiety or '
             'rage to cells dying, and saying it does tells a reader their anxiety is brain damage.' % T.SATTLER,
             'The key stuck in the "On" position, the word excitotoxicity, and the anxiety, rage and "itchy brain".',
             'Whether the paragraph says what the cell death really is, and keeps the feelings as over-excitement.',
             'Approve. It also sets up the calcium for the Lock below.'),
        card('SB-38', 'science', 'GluD: a new finding, still argued over, and the armor part said as a guess', i38,
             'B38',
             'This starts from your version, the one that read Human ([your check](%s)): your "Well according to", '
             'the label and the High/Low ending stay. What changes is what the finding says (GluDs are channels, '
             'opened by D-serine and GABA, not a volume knob), that it is still disputed, the two known cases, and '
             'that the armor part is a guess nobody has tested. Your version had dropped the link to the news story; '
             'I put a citation back, to the paper itself, since the paragraph rests on it.' % HIS38,
             'The paper ([Wang et al. 2025](%s)) found purified human GluD2 is a channel that D-serine and GABA open. '
             'A year earlier two labs tested the same idea and found no sign of direct gating ([Itoh et al. 2024](%s)), '
             'so it is new and contested. The known cases: an ataxia mutation makes the channel leak, and in '
             'schizophrenia GluDs are less active ([Johns Hopkins](%s)). So your speculation makes sense on the Low '
             'side (schizotypy, less active); on the High side the only known case is a movement disorder, so '
             'hyper-vigilance there is a guess with nothing under it yet. It also gives the section a better reason '
             'to mention GluD: D-serine, one of your tools, opens it.' % (T.WANG, T.ITOH, T.JHU),
             'Your opening question\'s place, your "Well according to", the label, and the High/Low with its four '
             'states.',
             'Whether the paragraph says the finding as it is, with its dispute, and calls the armor part a hypothesis.',
             'Approve. After that I humanize it from here, keeping your moves; it is longer than your version because '
             'the dispute and the two cases take room.'),
        card('SB-39', 'science', 'D-cycloserine is a different drug from D-serine, and its boost is small', i39, 'B39',
             'The drug tested with exposure therapy is named as a different one that works on the same NMDA spot as '
             'D-serine, not "the drug form" of it, and its effect is given as it was found: a small boost across 21 '
             'trials. Exposure therapy gets a few words of explanation. The session-quality rule stays word for '
             'word, now with its source.',
             'D-cycloserine (DCS) is its own drug that acts at the NMDA receptor\'s glycine spot, the spot D-serine '
             'switches on ([Smits et al. 2013](%s); [Wolosker et al. 1999](%s)). The best evidence, 21 trials with '
             '1,047 patients, found a small boost ([Mataix-Cols et al. 2017](%s)), and it helped after sessions that '
             'ended with low fear, not after the others, which is your session rule. I found no trial of D-serine '
             'itself with exposure therapy, which your "possibly" already covers.' % (T.SMITS, T.WOLOSKER, T.MATAIX),
             '"It does not erase fear directly" and the whole session-quality sentence, word for word.',
             'Whether DCS is named as a separate drug and its effect given as small.',
             'Approve.'),
        card('SB-40', 'science', 'NAC works as a brake on glutamate release, not a vacuum', i40, 'B40',
             'The Vacuum keeps its label, and the line says it works less like a vacuum than a brake, and how. The '
             'NAC dose line in the Glutamate Shield (block %d) changes its note from "Mops up glutamate" to "Turns '
             'down glutamate release"; the dose stays exactly as it is.' % i119,
             'The swap NAC drives puts more glutamate outside the synapse, not less; that glutamate trips a brake '
             '(mGluR2/3) that cuts how much glutamate is released into the synapse, in rats ([Moran et al. 2005](%s)). '
             'One rat study found the opposite at high concentrations, through another receptor (mGluR5), which is '
             'worth knowing but not a reason to change your dose ([Kupchik et al.](%s)).'
             % (T.MORAN, 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3340445'),
             'The "Lock, Stock, and Barrel" heading, the Vacuum label, and the dose, 1.8g – 2.4g (divided doses).',
             'Whether NAC is described as the brake it is.',
             'Approve.', extra_edits=[(i119, 'B119')]),
        card('SB-41', 'science', 'Magnesium plugs the channel; zinc mostly makes it open less', i41, 'B41',
             'Says what each of the two does instead of both "physically blocking".',
             'Magnesium sits in the channel and plugs it until the cell is excited enough to push it out '
             '([Jalali-Yazdi et al. 2018](%s)). Zinc mainly binds outside and makes the channel open less often; its '
             'own plug is weaker ([Amico-Ruvio et al. 2011](%s)). Whether swallowing them changes this in the brain '
             'is a separate question the article doesn\'t claim, so I left it.' % (T.JALALI, T.AMICO),
             'The Lock label and "the voltage".',
             'Whether the two are told apart.',
             'Approve; a small change.'),
        card('SB-42', 'cut', 'L-serine stays with a corrected reason; leucine goes', i42, 'B42',
             'L-serine stays, now feeding the NMDA spot (and maybe the GluD channels) that D-serine switches on, '
             'instead of "recalibrating the GluD Volume Dial". Leucine comes out of the Repair and its label, with '
             'its reason. Leucine appears nowhere else in the article, so nothing else changes.',
             'The brain does make D-serine from L-serine ([Wolosker et al. 1999](%s)), and the conversion really is '
             'weak (oral L-serine raised brain D-serine only a little in rats). But there is no volume dial (SB-38). '
             'For leucine I found nothing on "tuning synaptic gain". What I found points the other way: in rats at '
             'least half of the nitrogen in brain glutamate came from leucine ([2004 study](%s)), and leucine '
             'competes with tryptophan and tyrosine, the raw materials for serotonin and dopamine, to get into the '
             'brain ([National Academies](%s)). So for a protocol trying to calm glutamate, it isn\'t a repair.'
             % (T.WOLOSKER, 'https://pubmed.ncbi.nlm.nih.gov/14720211/', 'https://www.ncbi.nlm.nih.gov/books/NBK209312/'),
             'L-serine, "sessions that end with low fear and a sense of mastery stick better", and the D-serine '
             'sentence with "more risk, but also more benefit".',
             'Whether leucine stays in the protocol. That one is yours: if you have a reason for it I didn\'t find, '
             'Revise and say it, and I will check it.',
             'Approve, which cuts leucine. This paragraph read Human High as it stands, so after your answer it needs '
             'a humanizing pass and a new check.', approve_label='use this and cut leucine'),
        card('SB-148', 'science', 'D-serine turns things up, not down', i148, 'B148',
             'The reason for the timing changes from "when the GluD dial is turned down" to "when the D-serine starts '
             'working". The timing itself, 45 minutes or so after PQQ & Ketones, stays exactly.',
             'D-serine opens the GluD channels and switches on the NMDA spot, so it turns them up '
             '([Wang et al. 2025](%s); [Wolosker et al. 1999](%s)); "turned down" said the opposite. One thing I '
             'left for later in Part 2: "force memory reconsolidation" is stronger than what the DCS trials show, '
             'which is help with consolidating new learning.' % (T.WANG, T.WOLOSKER),
             'The scenario, the LifeLab link, and the timing.',
             'Whether the reason for the timing says the right direction.',
             'Approve.'),
    ]

    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261107-x1107a',
        'title': 'Neuro De-Armoring Cards, 7 November: section B\'s science',
        'intro': [
            'You asked for the science first. This is section B (the Overheating CPU), checked claim by claim '
            'against the sources themselves, with every link opened today: [the table](%s).' % TABLE,
            'Seven cards, each a claim corrected. They are small edits to the paragraphs as they stand (block 38: to '
            'your Human version), not humanized yet, and none has been to Pangram: once you approve the claims, I '
            'humanize each one and check it then.',
            'What already holds: stress raising glutamate (in animal work), L-serine becoming D-serine, the '
            'session-quality rule for DCS, and the agmatine paragraphs, checked earlier.',
            'No compound is added, no dose, unit or warning changes, and the timing in block %d stays as it is. The '
            'one thing taken out is leucine (SB-42), which is yours to decide.' % i148,
        ],
        'git_file': GIT_FILE,
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1107A.md'},
        'types': TYPES,
        'suggestions': S,
    }
    probs = sr.check(review, BL)
    for x in probs:
        print('PROBLEM', x)
    (HERE / 'REVIEW-X1107A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    if probs:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1107A.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1107A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for s in S:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '']
        for e in s['edits']:
            md += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
                   '**As it would read:**', '', '> %s' % e['after'], '']
        md += ['**What changes:** %s' % s['what'], '', '**Why:** %s' % s['why'], '',
               '**What stays:** %s' % s['stays'], '', '**You\'re deciding:** %s' % s['deciding'], '',
               '**My advice:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1107A.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [x['id'] for x in S])
    return 0


if __name__ == '__main__':
    sys.exit(main())
