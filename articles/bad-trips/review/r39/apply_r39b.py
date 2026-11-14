#!/usr/bin/env python3
"""apply_r39b.py - his message of 2026-11-13 14:15 UTC into the guide (../../experiments/t39-answers/JOEL-MESSAGE-20261113-1415.md):

- Active Seizure's call list without the periods at the end of its items, his fix ("i fixed the call list, you had to
  remove the periods at the end of each list item (i wouldn't put them in anyway, since they aren't full sentences)"; his
  check a53907ff, Human, 0% AI). The version he wants instead ("but i want this version which explains better", f6b4e35a)
  can't be read this turn: the link to his computer, where his Pangram history is open, failed to connect, and his
  history's API is not reachable from here. It goes in, whole, once its text is read.
- The same rule on the guide's other list whose items finish its lead-in, "Bring in mental-health support when:" (B97):
  the periods go (lesson bad-trips-2026-11-12m, the linter's O74).
- His DMSO text ("btw here is some DMSO info that should be in this guide, i took it from my neuro-dearmoring guide
  research"), whole, in the DMSO section (B201's section, Mental Stabilizers That Don't Abort the Trip): his first paragraph
  after the section's opening paragraph, his two evidence paragraphs after the paragraph on ozonated-charcoal water. Obvious
  corrections: the 1967 study's link mended ("[...(]https://" made "[...](https://"), "straightfoward" made
  "straightforward", a double space made one, and the two studies he names without links linked (Lu & Mattson 2001, the guide's own link for it;
  Hanslick et al. 2009, PubMed 19100327). His sleep sentence ("However, using too much DMSO for too many days at a time does
  have one side effect for me, which is reduced sleep, so it's best taken in the morning, and reduce the dose if you notice
  you're sleeping less.") says what the section's "Reduced sleep" side effect already says, so its advice, in his words, goes
  there, said once.

  python3 articles/bad-trips/review/r39/apply_r39b.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]


def no_periods(md):
    out = []
    for line in md.split('\n'):
        assert line.startswith('- ') and line.endswith('.'), line
        out.append(line[:-1])
    return '\n'.join(out)


i = ids.index('H49-SEIZE-CALL')
B[i]['md'] = no_periods(B[i]['md'])
i = ids.index('B97')
assert B[i - 1]['md'] == '## Bring in mental-health support when:'
B[i]['md'] = no_periods(B[i]['md'])

P1 = ("In my experience, DMSO makes me alert, smarter, happier, healthier, and more relaxed, and pretty much everyone I've heard "
      "from on forums and in real life says the same thing. It also is one of the only things that can instantly turn a bad "
      "psychedelic trip good. When I nebulize it, within a minute, my brain feels crystal clean and super blissed out (much more "
      "bliss than other routes).")
P2 = ("One famous [1967 study by Ramirez & Luza](https://nyaspubs.onlinelibrary.wiley.com/doi/epdf/10.1111/j.1749-6632.1967.tb34937.x) "
      "found it more effective than the best antipsychotic drugs at the time, slashing mental patients' psych ward stays in half, "
      "although it hasn't been tested (that I know of, yet) specifically for anxiety or PTSD, although those patients surely had "
      "both of those conditions. It's routinely used in humans who receive organ or stem cell transplants, as it is the best cell "
      "preservative that we've found so far. There is evidence ([Kortleve, et al, 2023](https://assets-eu.researchsquare.com/files/"
      "rs-2624641/v1/45119f29-3464-4680-8468-490477ae59ae.pdf?c=1688109028)) that using too much DMSO (10% vs 5%) in stem cell "
      "transfusions increases mild side effects in adult humans.")
P3 = ("In rat brain cells in a dish, DMSO at 0.5 to 1.5% quickly turned down the signals glutamate sends through its NMDA and AMPA "
      "receptors, and the calcium they let in. It also kept glutamate from killing the cells ([Lu & Mattson, 2001]"
      "(https://pubmed.ncbi.nlm.nih.gov/11421595/)). But it also appears to be neurotoxic to healthy mice neurons when they are "
      "exposed for too long ([Hanslick, et al, 2009](https://pubmed.ncbi.nlm.nih.gov/19100327/)). Translating mouse research to "
      "humans isn't straightforward.")
SLEEP_OLD = "It builds up past a threshold that seems to differ between people. "
SLEEP_NEW = ("It builds up past a threshold that seems to differ between people, so it's best taken in the morning, and reduce the "
             "dose if you notice you're sleeping less. ")

h = [k for k, b in enumerate(B) if b['md'] == '### [**DMSO**](http://dmso.u-dont-exist.com/)']
assert len(h) == 1
h = h[0]
assert B[h + 1]['md'].startswith('DMSO is another stabilizer I use when a trip becomes too intense')
assert B[h + 2]['md'].startswith('It overlaps with aged ozonated-charcoal water')
if not any(b['id'] == 'R39B-DMSO-1' for b in B):
    base = dict(B[h + 1])
    B.insert(h + 2, dict(base, id='R39B-DMSO-1', kind='p', md=P1))
    B.insert(h + 4, dict(base, id='R39B-DMSO-2', kind='p', md=P2))
    B.insert(h + 5, dict(base, id='R39B-DMSO-3', kind='p', md=P3))
s = [k for k, b in enumerate(B) if '- **Reduced sleep:** DMSO reduces how long I sleep' in b['md']]
assert len(s) == 1
assert B[s[0]]['md'].count(SLEEP_OLD) == 1
B[s[0]]['md'] = B[s[0]]['md'].replace(SLEEP_OLD, SLEEP_NEW)

MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

OE = ART / 'OWNER-EDITS.json'
oe = json.loads(OE.read_text(encoding='utf-8'))
have = {e['id'] for e in oe['entries']}
new = [
    {'id': 'r39b-call-periods', 'status': 'applied',
     'what': "Active Seizure's call list without periods at the end of its items, his fix a53907ff (review/r39/apply_r39b.py)",
     'joel': ('2026-11-13 14:15 UTC: "i fixed the call list, you had to remove the periods at the end of each list item (i '
              'wouldn\'t put them in anyway, since they aren\'t full sentences)"'),
     'must_contain_exact': ["- They injure their head, break a bone, or bleeding won't stop\n"],
     'must_not_contain': ["- They injure their head, break a bone, or bleeding won't stop."]},
    {'id': 'r39b-support-periods', 'status': 'applied',
     'what': "Bring in mental-health support when: its items without periods, his rule of 2026-11-13 (review/r39/apply_r39b.py)",
     'joel': '2026-11-13 14:15 UTC, the same message ("i wouldn\'t put them in anyway, since they aren\'t full sentences")',
     'must_contain_exact': ['- Sleep won\'t return\n'],
     'must_not_contain': ["- Sleep won't return."]},
    {'id': 'r39b-dmso-info', 'status': 'applied',
     'what': ("The DMSO section: his DMSO text from his neuro de-armoring research, whole, its sleep advice in the Reduced sleep "
              "side effect (review/r39/apply_r39b.py)"),
     'joel': '2026-11-13 14:15 UTC: "btw here is some DMSO info that should be in this guide, i took it from my neuro-dearmoring guide research"',
     'must_contain': ['In my experience, DMSO makes me alert, smarter, happier, healthier, and more relaxed',
                      'slashing mental patients\' psych ward stays in half',
                      'Translating mouse research to humans isn\'t straightforward.',
                      "so it's best taken in the morning, and reduce the dose if you notice you're sleeping less"]},
]
oe['entries'] += [e for e in new if e['id'] not in have]
OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied: his call list fix, the support list, his DMSO text |', len(MD.read_text().split()), 'words')
