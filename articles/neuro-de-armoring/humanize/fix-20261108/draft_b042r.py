"""B042r: block 42 after the comparison read and the needed read (2026-11-08).

The comparison read (`read-0108/`) found "So taking L-Serine feeds the spot D-serine switches on" unclear: L-serine
doesn't act at the spot, it becomes the D-serine that does. The needed read (`needed/b042/READ.md`) said the same
(a feeding picture and a switching picture, nothing to tell what is fed) and listed "and maybe the GluD channels too"
as a hedge the reader can't use to decide on L-serine, as in block 39. The last sentence is his own (6 November) and
stays word for word.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/draft_b042r.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402

WOLOSKER = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC23961'
MD = ('The Repair (L-Serine): Your brain makes D-Serine out of L-Serine ([Wolosker, et al, 1999](%s)). So taking '
      'L-Serine gives you more D-serine for that spot on the NMDA receptor, which means a session that ends with the '
      'fear down and a sense of mastery has a better chance of sticking. The conversion isn\'t very efficient though, so '
      'some people take D-serine itself instead (more risk, but also more benefit).' % WOLOSKER)
TEXT = MD.replace('[Wolosker, et al, 1999](%s)' % WOLOSKER, 'Wolosker, et al, 1999')


def main():
    old = json.loads((HERE.parent / 'fix-20261107' / 'hum' / 'B042h2.receipt.json').read_text(encoding='utf-8'))
    r = S.make(TEXT, old['section'], old['reader'])
    pays = [('they learn where D-Serine comes from, which is why L-Serine is in the protocol',
             'it follows the Lock in the Fix list', None),
            ('they learn what taking L-Serine does for their next therapy session: more D-serine for the spot learning '
             'needs, so a session that ends well sticks better', 'it says what that conversion is good for',
             'So taking L-Serine'),
            ('they learn that the conversion is weak, so some take D-serine itself, with more risk',
             'it qualifies the sentence before', 'The conversion')]
    for x, (p, f, link) in zip(r['sentences'], pays):
        x['payoff'], x['follows'] = p, f
        if 'link' in x:
            x['link'] = link or 'none: it opens on its own subject'
    for k in ('placement', 'opens', 'same_point', 'questions'):
        r[k] = old[k]
    r['opens']['first_sentence'] = S.sentences(TEXT)[0]
    r['questions']['Q4'] = 'PASS: the NMDA spot carried from block 39, where it is introduced'
    r['questions']['Q3'] = 'PASS: each thing is named exactly (L-Serine, D-serine, the NMDA receptor)'
    r['checked'] = [{'point': 'L-Serine "feeds the spot D-serine switches on, and maybe the GluD channels too"',
                     'found': 'L-serine is made into D-serine (Wolosker 1999), which acts at the NMDA spot; L-serine '
                              'itself does not act there',
                     'still_needed': 'yes: they decide on L-serine knowing it works by raising D-serine',
                     'fate': 'changed'}]
    r['needed'] = {'reader': 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this '
                             'paragraph, its heading and what it is for (needed/b042/BRIEF.txt, READ.md)',
                   'unneeded': ['and maybe the GluD channels too'], 'kept': {}}
    probs = S.check(TEXT, r)
    for p in probs:
        print('RECEIPT PROBLEM', p)
    (HERE / 'B042r.txt').write_text(TEXT + '\n', encoding='utf-8')
    (HERE / 'B042r.md').write_text(MD + '\n', encoding='utf-8')
    (HERE / 'B042r.receipt.json').write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('ok' if not probs else 'FAIL')
    return 1 if probs else 0


if __name__ == '__main__':
    sys.exit(main())
