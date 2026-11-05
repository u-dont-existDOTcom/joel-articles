#!/usr/bin/env python3
"""apply_r07.py - round 7's answers (Joel, exported 2026-11-05 17:09 UTC; ANSWERS-R07-20261105-1709.json) put into the
guide: all four cards approved, each as the card's "as it would read", with the guide's links kept on the same words.

Starts from the guide after round 6 (../../GUIDE-SO-FAR-blocks.json as main has it after pull request 306, whose page
form is PAGE-R07.md, the SHA-256 his export names) and writes the guide after round 7 (GUIDE-AFTER-R07.md and
GUIDE-AFTER-R07-blocks.json beside this script), which becomes ../../GUIDE-SO-FAR.md.

- ABRACE (N-CANNA-1): "a company" becomes "a patients' association", "in 30 tests" becomes "in more than 30 tests".
- AUTHORS (N-CBD-2): the authors' sentence as the paper has it, the two generalized syndromes said, and his last sentence
  with its conclusion ("so topical CBD might do better for those than it did in that trial").
- AFTER-MOVE (B111): "During the seizure, alongside any rescue medicine, I would use ..." for "I would also use ... as
  adjuncts", and the focal-seizure sentence out.
- FORUMS (N-CANNA-2): his first sentence as it was; my two sentences after it as the card has them. The rat study's link
  moves to the words that now describe the rats ("rats bred to have seizures").

Each block's plain text before must be the card's "before", and after must be its "as it would read" (my_version), or
the script stops.

  python3 apply_r07.py            write the guide after round 7 and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
REVIEW = json.loads((HERE / 'REVIEW-R07.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R07-20261105-1709.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R07.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R07-blocks.json'

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r07', (ANSWERS['review_id'], REVIEW['review_id'])
assert hashlib.sha256((HERE / 'PAGE-R07.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'ABRACE', 'AUTHORS', 'AFTER-MOVE', 'FORUMS'}
assert all(x['status'] == 'approved' for x in ITEM.values()), {k: v['status'] for k, v in ITEM.items()}

RATS = 'https://pubmed.ncbi.nlm.nih.gov/33370468/'
UNIT = {b['id']: b for b in BLOCKS}
LOG = []


def plain(md):
    return re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1', md).strip()


def edit(bid, card, pairs, why):
    md = UNIT[bid]['md']
    assert plain(md) == ITEM[card]['before'].strip(), (bid, plain(md)[:120])
    for old, new in pairs:
        assert md.count(old) == 1, (bid, old)
        md = md.replace(old, new)
    assert plain(md) == ITEM[card]['my_version'].strip(), (bid, plain(md), ITEM[card]['my_version'])
    UNIT[bid]['md'] = md
    LOG.append('%s: %s, %s' % (bid, card, why))


edit('N-CANNA-1', 'ABRACE', [('by a company called ABRACE', "by a patients' association called ABRACE"),
                             ('that in 30 tests they did', 'that in more than 30 tests they did')],
     'a patients\' association, "more than 30 tests" (the Congress transcript)')
edit('N-CBD-2', 'AUTHORS',
     [('The study authors suggested the dosing may have been too low, or it works better for generalized rather than '
       'focal seizures. Generalized are the type people usually have with MDMA & psychedelic overdoses.',
       "The study authors suggested the dosing may have been too low, or that adults with focal epilepsy just don't "
       "respond as well as people with the syndromes oral CBD is approved for. The seizures in Dravet and Lennox-Gastaut "
       "syndrome are mostly generalized. Generalized are the type people usually have with MDMA & psychedelic overdoses, "
       "so topical CBD might do better for those than it did in that trial.")],
     'the authors\' sentence as the paper has it, and the conclusion said')
edit('B111', 'AFTER-MOVE',
     [('I would also use topical magnesium chloride', 'During the seizure, alongside any rescue medicine, I would use topical magnesium chloride'),
      ('CBD preparation as adjuncts (a lot of CBD', 'CBD preparation (a lot of CBD'),
      (' For focal seizures outside those syndromes, the evidence is mixed, but still long-term.', '')],
     '"During the seizure, alongside any rescue medicine", the focal sentence out')
old_rats = ('But other people say THC vapes and concentrates brought their seizures on, and in [rats that get the brief '
            'staring seizures called absence seizures](%s), high-THC smoke made them worse while injected CBD cut them '
            'about in half. So the THC may be what makes it go either way.' % RATS)
new_rats = ('But a few people on the same forums said THC vapes and concentrates brought their seizures on. And [rats bred '
            'to have seizures](%s) had more of them after high-THC smoke.' % RATS)
edit('N-CANNA-2', 'FORUMS', [(old_rats, new_rats)], 'my two sentences as the card has them, the rat study linked on its new words')

text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
OUT.write_text(text, encoding='utf-8')
OUT_BLOCKS.write_text(json.dumps([{'id': b['id'], 'kind': b['kind'], 'md': b['md'], 'text': None} for b in BLOCKS],
                                 ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
before = (ART / 'GUIDE-SO-FAR.md').read_text(encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before)), len(re.findall(r'\S+', text))
print('\n'.join(LOG))
print('4 cards applied; %d words -> %d (%+d); %s sha256 %s' % (w0, w1, w1 - w0, OUT.name,
                                                              hashlib.sha256(text.encode()).hexdigest()))
