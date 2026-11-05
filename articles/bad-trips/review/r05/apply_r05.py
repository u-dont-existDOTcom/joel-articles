#!/usr/bin/env python3
"""apply_r05.py - round 5's answers (Joel, exported 2026-11-04 22:14 UTC; ANSWERS-R05-20261104-2214.json) put into the
guide: both cards Revise, each with his own version in "your_version", which goes in as he wrote it.

Starts from the guide after round 4 (../r04/GUIDE-AFTER-R04-blocks.json, which round 5's page showed; PAGE-R05.md's
SHA-256 is the one his export names) and writes the guide after round 5 (GUIDE-AFTER-R05.md and
GUIDE-AFTER-R05-blocks.json beside this script), which becomes ../../GUIDE-SO-FAR.md.

- CBD-YOURS: B111 becomes his three paragraphs (he broke it up: "i broke it up"), B111 and two new blocks N-CBD-2 and
  N-CBD-3. His words and characters as he typed them, with three changes, none to his words:
  * the trailing space at the end of his first two paragraphs goes;
  * "in a rats with temporal-lobe epilepsy" becomes "in rats with temporal-lobe epilepsy" (his obvious typo; his rule:
    fix his obvious typos, no Pangram recheck needed);
  * W-CBD2's links go back on the words that name the same sources, as round 5's card said ("the links go back on the
    study names"): "approved" to the FDA's Epidiolex label, "12-week trial" to the trial (O'Brien et al. 2022), and
    "rats with temporal-lobe epilepsy" and "absence-epilepsy model" to the two DMSO studies. The 2025 study's link goes
    with the sentence he took out ("i took that one out": a meant cut, KEEP-AS-IS C8). His own link, "just anecdotes" to
    a YouTube video, stays as he made it (checked 2026-11-04 22:58 UTC from his laptop: "Miraculous CBD Oil Stops
    Child's Epileptic Seizure Instantly", High At 9 News, 35 seconds).
- PFA-YOURS: B236 becomes his paragraph, with one typo fixed: "Anything that could let someone hurt themselves in the
  next five minutes take priority" -> "takes priority" (the subject is "Anything").

Each block's old Markdown must be what round 5's page showed, or the script stops.

  python3 apply_r05.py            write the guide after round 5 and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BLOCKS = json.loads((HERE.parent / 'r04' / 'GUIDE-AFTER-R04-blocks.json').read_text(encoding='utf-8'))
REVIEW = json.loads((HERE / 'REVIEW-R05.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R05-20261104-2214.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R05.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R05-blocks.json'

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r05', (ANSWERS['review_id'], REVIEW['review_id'])
assert hashlib.sha256((HERE / 'PAGE-R05.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'CBD-YOURS', 'PFA-YOURS'}
assert all(x['status'] == 'revise' and x['your_version'] for x in ITEM.values())

FDA = 'https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/210365s024s029s030lbl.pdf'
GEL = 'https://pubmed.ncbi.nlm.nih.gov/35802375/'
RAT_TLE = 'https://pubmed.ncbi.nlm.nih.gov/23643984/'
ABSENCE = 'https://pubmed.ncbi.nlm.nih.gov/21320528/'
VIDEO = 'https://www.youtube.com/watch?v=RCxGSrUsB0Q'

UNIT = {b['id']: b for b in BLOCKS}
LOG = []


def link(md, words, url):
    assert md.count(words) == 1, (words, md)
    return md.replace(words, '[%s](%s)' % (words, url))


# ---------------------------------------------------------------- CBD-YOURS
old = UNIT['B111']['md']
assert old.startswith('I would also use topical magnesium chloride') and '[2025 study]' in old, old
his = ITEM['CBD-YOURS']['your_version']
assert '[just anecdotes](%s)' % VIDEO in his
paras = [p.rstrip() for p in his.split('\n\n')]
assert len(paras) == 3, paras
assert paras[2].count('in a rats with temporal-lobe epilepsy') == 1
paras[2] = paras[2].replace('in a rats with temporal-lobe epilepsy', 'in rats with temporal-lobe epilepsy')
paras[0] = link(paras[0], 'approved', FDA)
paras[1] = link(paras[1], '12-week trial', GEL)
paras[2] = link(paras[2], 'rats with temporal-lobe epilepsy', RAT_TLE)
paras[2] = link(paras[2], 'absence-epilepsy model', ABSENCE)
at = BLOCKS.index(UNIT['B111'])
UNIT['B111']['md'] = paras[0]
BLOCKS.insert(at + 1, {'id': 'N-CBD-2', 'kind': 'p', 'md': paras[1], 'text': None})
BLOCKS.insert(at + 2, {'id': 'N-CBD-3', 'kind': 'p', 'md': paras[2], 'text': None})
LOG.append('B111: CBD-YOURS, his three paragraphs (B111, N-CBD-2, N-CBD-3); "a rats" -> "rats"; the FDA, trial and two '
           'DMSO links on the words that name them; the 2025 study and its link out (his cut)')

# ---------------------------------------------------------------- PFA-YOURS
assert UNIT['B236']['md'] == REVIEW['suggestions'][1]['edits'][0]['before'] if REVIEW['suggestions'][1].get('edits') \
    else UNIT['B236']['md'].startswith('Begin with whatever could hurt somebody'), UNIT['B236']['md']
his = ITEM['PFA-YOURS']['your_version'].strip()
assert his.count('in the next five minutes take priority') == 1, his
UNIT['B236']['md'] = his.replace('in the next five minutes take priority', 'in the next five minutes takes priority')
LOG.append('B236: PFA-YOURS, his paragraph; "take priority" -> "takes priority"')

# ---------------------------------------------------------------- write
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
OUT.write_text(text, encoding='utf-8')
OUT_BLOCKS.write_text(json.dumps([{'id': b['id'], 'kind': b['kind'], 'md': b['md'], 'text': None} for b in BLOCKS],
                                 ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
before = (HERE.parent / 'r04' / 'GUIDE-AFTER-R04.md').read_text(encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before)), len(re.findall(r'\S+', text))
print('\n'.join(LOG))
print('2 cards applied (his versions); %d words -> %d (%+d); %s sha256 %s' % (
    w0, w1, w1 - w0, OUT.name, hashlib.sha256(text.encode()).hexdigest()))
