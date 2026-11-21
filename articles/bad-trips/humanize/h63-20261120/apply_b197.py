#!/usr/bin/env python3
"""apply_b197.py - the ozone story's last line (B197) as the try that read Human High in every window by itself goes
into the guide (apply_gate.py refuses it otherwise).

The near miss was turn 54's c3-ozone-1 (his C3 answer a, "suggested"; 4cf06939: its last line AI Low, the middle Human
Low). The tries of this turn change only the last line, which all three fresh reads marked as a summing-up the reader can
do nothing with: it now ends on what to do. Read beside the line as the guide has it (lesson bad-trips-2026-11-20f):
nothing goes; "suggested" (his C3 answer) stays; "address" is said as "work on", and the advice is added. OWNER-EDITS
c3-ozone-suggested is brought in line with the new last line ("suggested" kept, "showed me" still refused).

  python3 articles/bad-trips/humanize/h63-20261120/apply_b197.py KEY      (from the repo root; KEY is the passing try)
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import apply_gate  # noqa: E402

BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
OLD_LAST = 'The mistake suggested that DMSO and aged ozonated-charcoal water address different kinds of overload.'


def main(key):
    test = (HERE / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').rstrip('\n')
    last = test[test.index('The mistake suggested'):]
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    b = [x for x in B if x['id'] == 'B197'][0]
    assert b['md'].count(OLD_LAST) == 1, b['md'][-160:]
    new_md = b['md'].replace(OLD_LAST, last)
    assert apply_gate.plain(new_md) == apply_gate.plain(test), 'the try is not the paragraph as it would read'
    apply_gate.require(str(ART / 'humanize' / 'pangram-ledger.jsonl'), [new_md])
    b['md'] = new_md
    MD.write_text('\n\n'.join(x['md'] for x in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    e = [x for x in oe['entries'] if x['id'] == 'c3-ozone-suggested'][0]
    e['must_contain_exact'] = [last]
    note = ('2026-11-20 (turn 55): the last line ends on what to do, read Human High by itself (%s, '
            'humanize/h63-20261120/apply_b197.py); "suggested" kept' % key)
    if note not in e.setdefault('changed', []):
        e['changed'].append(note)
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied', key, '|', last)


if __name__ == '__main__':
    main(sys.argv[1])
