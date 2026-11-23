"""Puts in what of his new warnings read Human High in every window by itself (checks-1123g): 5-HTP's lingering-anhedonia
sentence at the end of its stop signs. The lion's mane item and agmatine's sentence read AI and wait (texts_x1123a).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1123a/apply_x1123a.py [--write]
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import apply_gate  # noqa: E402
import texts_x1123a as T  # noqa: E402

MDF = H / 'HUMANIZED-SO-FAR.md'
LEDGER = H / 'pangram-ledger.jsonl'
END = 'or a too-bright / hypomanic feeling.'


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def main():
    write = '--write' in sys.argv
    md = MDF.read_text(encoding='utf-8')
    lines = md.split('\n')
    (i,) = [n for n, l in enumerate(lines) if l.startswith('Side effects / stop signs: The most dangerous symptoms')]
    assert lines[i].rstrip().endswith(END), lines[i][-80:]
    new_line = lines[i].rstrip() + T.HTP_ADD
    apply_gate.require(LEDGER, [new_line])
    out = '\n'.join(lines[:i] + [new_line] + lines[i + 1:])
    tmp = HERE / 'HUMANIZED-AFTER-X1123A.md'
    tmp.write_text(out, encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                         str(H / 'FIDELITY-KEYS.json'), str(tmp)], capture_output=True, text=True)
    print(fk.stdout.strip().splitlines()[-1] if fk.stdout.strip() else fk.stderr.strip()[-300:])
    rec = {'review': 'x1123a', 'before_sha256': sha(md), 'after_sha256': sha(out),
           'applied': [{'what': '5-HTP stop signs: his lingering-anhedonia warning (2026-11-22 17:39 UTC), my wording',
                        'line': i + 1, 'added': T.HTP_ADD.strip(),
                        'check': 'https://www.pangram.com/history/e48362d5-bcae-42d3-ab11-2965f7404666',
                        'result': 'Human Written, every window High (the paragraph by itself)'}],
           'waiting': [{'what': 'lion\'s mane and ashwagandha item (texts_x1123a.LMA)',
                        'check': 'https://www.pangram.com/history/50622455-2e3a-482e-ac66-0ae461f68592',
                        'result': 'AI Detected, 93% AI'},
                       {'what': 'agmatine stop line with the added sentence (texts_x1123a.agm_paragraph)',
                        'check': 'https://www.pangram.com/history/1eea33ab-e9b9-4bd4-b32d-0489aec27358',
                        'result': 'AI Generated, 100% AI: the post\'s paragraph reads AI with it'}]}
    if write:
        if fk.returncode != 0:
            raise SystemExit('fidelity check failed: ' + fk.stdout[-500:])
        MDF.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1123A.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        tmp.unlink()
        print('written', sha(out)[:8])
    else:
        print('dry run', sha(out)[:8])


if __name__ == '__main__':
    main()
