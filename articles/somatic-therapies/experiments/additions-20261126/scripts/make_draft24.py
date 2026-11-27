#!/usr/bin/env python3
"""Draft 24 (turn of 2026-11-27 19:25 UTC): IC2's last try (6 of 6), from its near miss (ic2-9: High 38, Medium 20 over its
second sentence), after the tell panel on draft 23 (panel/IC2-23: all three readers on the reassurance-plus-evidence close,
"treat the pain as real" as a stock phrase): the stock phrase in his own word from the section ("normal test results don't
prove the pain is imaginary"), "Neither one sees the pain as imaginary" ("sees", READ-24: "Neither one treats the pain" first reads as "neither works"); the rest of ic2-9 word for word.
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft24.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
IC = json.loads((D / 'INNER-CHILD-ADDS-13.json').read_text(encoding='utf-8'))
IC9 = json.loads((D / 'INNER-CHILD-ADDS-9.json').read_text(encoding='utf-8'))
o = "They both treat the pain as real, and they've helped people with long-lasting back, muscle and joint pain."
assert o in IC9['IC2']['add']
IC['IC2']['add'] = IC9['IC2']['add'].replace(o, "Neither one sees the pain as imaginary, and they've helped people with long-lasting back, muscle and joint pain.")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-14.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
sys.path.insert(0, str(D.resolve().parents[3] / 'tools' / 'humanization'))
import sense_receipt
lines = []
for k, v in IC.items():
    lines.append('## %s, in "%s"' % (k, v['section']))
    lines.append('Where: ' + v['where'])
    lines.append('The sentence before it (his): ' + v['his_before'])
    for j, s in enumerate(sense_receipt.sentences(v['add_plain']), 1):
        lines.append('%s-S%d: %s' % (k, j, s))
    lines.append('')
(D / 'reads' / 'drafts24-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(IC['IC2']['add_plain'])
