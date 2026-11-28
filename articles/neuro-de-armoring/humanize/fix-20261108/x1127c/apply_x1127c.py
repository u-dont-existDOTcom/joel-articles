#!/usr/bin/env python3
"""Put this turn's paragraphs of mine that read Human High in every window into HUMANIZED-SO-FAR.md (texts_x1127c.NEW),
each through the apply gate (tools/humanization/apply_gate.py: a check of the paragraph by itself, or with its neighbour
when under 50 words, read Human High in every window).

- P030, Part 1's intro line (35 words): checked with the paragraph after it, PAIR-030-032#339 (one window, High).
- P032, the Metabolic Red Line's first paragraph: P032#340 (one window, High).
- P033, its second paragraph: only with a check that read High in every window (P033's best so far is listed in the
  run's record when it has none).

The intro line's old text was held word for word by the warning check (unit W020, its only warning word "must", in
"you must understand ... before applying the tools", which warns of nothing). Lesson bad-trips-2026-11-27f frees such a
line: FIDELITY-KEYS.json's "not_cautions" names it, and its facts stay held by the article-wide counts.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127c/apply_x1127c.py [--write] [KEY ...]
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import texts_x1127c as T  # noqa: E402
import apply_gate as G  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
KEYS = H / 'FIDELITY-KEYS.json'
LEDGER = H / 'pangram-ledger.jsonl'
REC = HERE / 'APPLIED-X1127C.json'
NOT_CAUTION = {'unit': 'W020', 'cues': ['must'],
               'by': 'lesson bad-trips-2026-11-27f (his CHARCOAL-WORDS answer "a", 2026-11-27 15:34 UTC: "from now on a line '
                     'whose only warning word isn\'t a caution may be said in other words, as long as every fact stays"), '
                     'applied by fix-20261108/x1127c/apply_x1127c.py',
               'why': 'Part 1\'s intro line: "must" is in "you must understand ... before applying the tools", an '
                      'instruction to read the science first, not a caution; trauma, withdrawal and chronic stress stay '
                      'in the line'}


def main(write, keys):
    text = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode('utf-8')).hexdigest()
    done = []
    for k in keys:
        G.require(str(LEDGER), [T.plain(T.NEW[k])])
        assert text.count(T.OLD[k]) == 1, k
        text = text.replace(T.OLD[k], T.NEW[k], 1)
        done.append(k)
    after = hashlib.sha256(text.encode('utf-8')).hexdigest()
    print(before[:8], '->', after[:8], done)
    kj = json.loads(KEYS.read_text(encoding='utf-8'))
    if 'p030' in keys and not any(e.get('unit') == 'W020' for e in kj.get('not_cautions', [])):
        kj.setdefault('not_cautions', []).append(NOT_CAUTION)
    tmpk = pathlib.Path('/tmp/apply_x1127c.keys.json')
    tmpk.write_text(json.dumps(kj, ensure_ascii=False), encoding='utf-8')
    tmp = pathlib.Path('/tmp/apply_x1127c.md')
    tmp.write_text(text, encoding='utf-8')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/fidelity_keys.py'), 'check', str(tmpk), str(tmp)],
                       capture_output=True, text=True)
    print(r.stdout.strip()[-400:])
    if 'verdict: PASS' not in r.stdout:
        sys.exit('the warning check fails; nothing written')
    if not write:
        return
    ARTICLE.write_text(text, encoding='utf-8')
    KEYS.write_text(json.dumps(kj, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    rec = json.loads(REC.read_text(encoding='utf-8')) if REC.exists() else {
        'about': 'What x1127c put into HUMANIZED-SO-FAR.md, each paragraph through the apply gate.', 'runs': []}
    checks = {'p030': 'PAIR-030-032#339, https://www.pangram.com/history/af3159d7-72d3-403f-9b5b-90a4965fcaf7 (Human '
                      'Written, one window, High, 130 words, with the paragraph after it)',
              'p032': 'P032#340, https://www.pangram.com/history/ef537748-af2f-4cc0-92ee-80d4cb5bd35a (Human Written, one '
                      'window, High, 95 words)',
              'p033': 'P033#343, https://www.pangram.com/history/72ba33d4-6a70-4601-88a8-a249cc49dd1e (Human Written, one '
                      'window, High, 83 words; try 5, the DeltaFosB sentence joined to the one it continues)'}
    rec['runs'].append({'applied': [{'key': k, 'check': checks[k], 'old': T.OLD[k], 'new': T.NEW[k]} for k in done],
                        'not_cautions': [NOT_CAUTION] if 'p030' in keys else [],
                        'before_sha256': before, 'after_sha256': after})
    REC.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('written', after[:8])


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if a != '--write']
    main('--write' in sys.argv, args or ['p030', 'p032'])
