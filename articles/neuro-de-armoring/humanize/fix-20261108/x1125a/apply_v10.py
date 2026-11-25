#!/usr/bin/env python3
"""Put version 10's three paragraphs into HUMANIZED-SO-FAR.md: the plant medicines, uridine and the DMSO item, each the
paragraph the article already has with one word made plain after the comparison read (read-1125a/READER-1.md: F1.2,
F1.17, F1.1), and each Human High by itself again (batch x1125g; apply_gate.py checks the ledger first).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/apply_v10.py [--write]
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import texts_x1125a as T  # noqa: E402
sys.path.insert(0, str(T.ROOT / 'tools' / 'humanization'))
import apply_gate  # noqa: E402

H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
LEDGER = H / 'pangram-ledger.jsonl'
PAIRS = (('ethno', T.V4), ('uri', T.V4), ('dmso', T.V6))


def main(write):
    text = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode('utf-8')).hexdigest()
    applied = []
    for key, was in PAIRS:
        old, new = was[key], T.V10[key]
        assert text.count(old) == 1, key
        text = text.replace(old, new)
        applied.append({'key': key, 'version': 'v10', 'old': old, 'new': new})
    apply_gate.require(LEDGER, [a['new'] for a in applied])
    rec = {'about': 'three one-word clarity fixes from the comparison read of 2026-11-25, each checked by itself',
           'whose': 'mine', 'applied': applied, 'before_sha256': before,
           'after_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], [a['key'] for a in applied])
    if write:
        ARTICLE.write_text(text, encoding='utf-8')
        f = HERE / 'APPLIED-X1125A.json'
        prev = json.loads(f.read_text(encoding='utf-8'))
        prev['runs'].append(rec)
        f.write_text(json.dumps(prev, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        r = subprocess.run([sys.executable, str(T.ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                            str(H / 'FIDELITY-KEYS.json'), str(ARTICLE)], capture_output=True, text=True)
        print('fidelity:', (r.stdout + r.stderr).strip()[-300:])


if __name__ == '__main__':
    main('--write' in sys.argv)
