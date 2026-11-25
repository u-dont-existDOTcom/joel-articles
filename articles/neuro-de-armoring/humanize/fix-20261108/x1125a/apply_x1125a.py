#!/usr/bin/env python3
"""Put this turn's paragraphs into HUMANIZED-SO-FAR.md: each is a warning at the top ("A Complete Guide to
Bio-De-Armoring"), fixed for sense first, read by fresh readers, and checked by itself in Pangram at Human High in
every window (apply_gate.py, gate bad-trips-2026-11-12l, checks the ledger for each before anything is written).

Two changes of layout go with them, neither a change of words:
- the 5-HTP rule ("Rule: do not take 5-HTP on the same day as a psychedelic trip, and do not use it anywhere near
  ayahuasca/harmalas or iboga."), which opened the uridine paragraph, moves to the end of the 5-HTP paragraph before
  it, as the post's sentence, unchanged, so everything about 5-HTP is in one place and the uridine paragraph is about
  uridine (lesson neuro-2026-11-24c: one idea in one place);
- when the DMSO item goes in: the section's label, "⚠️ CRITICAL MEDICAL DISCLAIMER:", which the post has as a bold
  line of its own above its list of warnings and the Markdown import had run into the first item, becomes a block of
  its own.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/apply_x1125a.py KEY=VERSION ... [--write]
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
RULE = 'Rule: do not take 5-HTP on the same day as a psychedelic trip, and do not use it anywhere near ayahuasca/harmalas or iboga.'


def main(picks, write):
    text = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode('utf-8')).hexdigest()
    applied, mine = [], []
    for key, ver in picks.items():
        new = T.VERSIONS[ver][key]
        old = T.now(key)
        assert text.count(old) == 1, key
        if key == 'uri' and 'htp' not in picks:
            htp = T.now('htp')
            assert old.startswith(RULE + ' ') and text.count(htp) == 1
            text = text.replace(htp, htp + ' ' + RULE)
            applied.append({'key': 'htp', 'move': 'the 5-HTP rule, the post\'s sentence unchanged, from the head of the '
                            'uridine paragraph to the end of the 5-HTP paragraph', 'old': htp, 'new': htp + ' ' + RULE})
        if key == 'dmso':
            assert old.startswith(T.LABEL) and not new.startswith(T.LABEL)
            text = text.replace(old, T.LABEL + '\n\n' + new)
        else:
            text = text.replace(old, new)
        mine.append(new)
        applied.append({'key': key, 'version': ver, 'old': old, 'new': new})
    apply_gate.require(LEDGER, mine)
    rec = {'about': 'the warnings at the top, fixed for sense first and checked by themselves (2026-11-25)',
           'whose': 'mine: the post\'s model text made to say what each warning is for, with his own words kept where '
                    'he gave them (62a\'s heart-rate test, "from experience, like Scott\'s below")',
           'applied': applied, 'before_sha256': before,
           'after_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], [a['key'] for a in applied])
    if write:
        ARTICLE.write_text(text, encoding='utf-8')
        f = HERE / 'APPLIED-X1125A.json'
        prev = json.loads(f.read_text(encoding='utf-8')) if f.exists() else {'runs': []}
        prev['runs'].append(rec)
        f.write_text(json.dumps(prev, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        r = subprocess.run([sys.executable, str(T.ROOT / 'tools/humanization/fidelity_keys.py'), 'check',
                            str(H / 'FIDELITY-KEYS.json'), str(ARTICLE)], capture_output=True, text=True)
        print('fidelity:', (r.stdout + r.stderr).strip()[-400:])


if __name__ == '__main__':
    main(dict(a.split('=') for a in sys.argv[1:] if '=' in a), '--write' in sys.argv)
