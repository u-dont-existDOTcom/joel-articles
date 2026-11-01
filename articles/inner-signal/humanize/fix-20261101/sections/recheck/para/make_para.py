"""Batch p1101: round 3's paragraphs (../../fixes_round3.py), each checked alone (or with its heading, or with the
paragraph it leans on when it is under 50 words), since the six sections' two section checks are spent. Try 1 of 6 per
paragraph lineage (docs/PANGRAM-PRODUCTION-BUDGET-20261020.md), each with its diagnosis (FIXES-S1101.json, "round3").

  python3 articles/inner-signal/humanize/fix-20261101/sections/recheck/para/make_para.py [--ledger]
Writes p1101-items.json, PREDICTIONS.md / .json; with --ledger, adds each prediction to the lane's ledger.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
S = HERE.parents[1]
H = S.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
# key: (blocks, lineage, scope, chance, why)
UNITS = {
    'p1101-17a': ([105], 'HG1101-17-P1', 'paragraph', 0.5,
                  'round 1\'s paired negations cut to one "though, and"; the rest of the paragraph read Human (Low) or '
                  'High on 1 November'),
    'p1101-17b': ([106, 107], 'HG1101-17-P23', 'pair', 0.45,
                  'the quote\'s last line and the last paragraph without round 1\'s repeated list of what is good about '
                  'being young; still two lists, the published ones'),
    'p1101-42': ([299], 'HG1101-42-P4', 'paragraph', 0.7, 'the short closing sentence joined to the one it qualifies'),
    'p1101-44a': ([314], 'HG1101-44-P4', 'paragraph', 0.7, 'the short last sentence joined to the one before; the '
                                                         'rest read Human (High) and Medium'),
    'p1101-44b': ([315], 'HG1101-44-P5', 'paragraph', 0.45, 'says why (the voice that isn\'t coming back) instead of '
                                                           'rules in the published order'),
    'p1101-44c': ([316], 'HG1101-44-P6', 'paragraph', 0.45, 'says what being left in a role or blank means once you get '
                                                           'up'),
    'p1101-53a': ([368], 'HG1101-53-P1', 'paragraph', 0.4, 'starts from what the extra time is for; still a run of '
                                                          'steps, which read AI twice'),
    'p1101-53b': ([368, 369], 'HG1101-53-P12', 'pair', 0.35, 'the two paragraphs together, as the section has them; '
                                                            'read AI twice'),
    'p1101-59': ([405, 406], 'HG1101-59-P1', 'paragraph', 0.45, 'says what "diffuse" is before the step; the window '
                                                              'was a heading and an order twice'),
    'p1101-93': ([731, 732], 'HG1101-93-P1', 'paragraph', 0.6, 'the opening says what happens instead (flattery); the '
                                                              'rest read Human (High) twice'),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    items, rows = [], []
    for k, (blocks, lineage, scope, chance, why) in UNITS.items():
        text = '\n\n'.join(bl[i]['text'] for i in blocks)
        h = hashlib.sha256(text.encode('utf-8')).hexdigest()
        items.append([k, text, h])
        rows.append({'key': k, 'lineage': lineage, 'scope': scope, 'blocks': blocks, 'words': len(text.split()),
                     'call': 'Human' if chance >= 0.5 else 'AI', 'chance': chance, 'why': why,
                     'where': sr.where(bl, blocks[-1])})
        assert len(text.split()) >= 50, (k, len(text.split()))
    (HERE / 'p1101-items.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    out = ['# Batch p1101: round 3\'s paragraphs, each checked alone (predictions, before the run)', '',
           '| text | mine | chance | why | Pangram |', '|---|---|---|---|---|']
    out += ['| %s: %s (%d words) | %s | %.2f | %s | |' % (r['key'], r['where'], r['words'], r['call'], r['chance'], r['why'])
            for r in rows]
    (HERE / 'PREDICTIONS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(rows), 'units,', sum(r['words'] for r in rows), 'words')
    if not a.ledger:
        return
    tdir = HERE / 'texts'
    tdir.mkdir(exist_ok=True)
    for (k, text, h), r in zip(items, rows):
        f = tdir / (k + '.txt')
        f.write_text(text, encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', r['scope'], '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', k, '--batch', 'p1101', '--diagnosis', r['why'],
               '--tells', 'read AI or Human (Low) in its section check of 1 November (r1101)',
               '--human-tells', 'round 3, with its diagnosis (fixes_round3.py)',
               '--decides', 'whether round 3 of this paragraph reads Human alone, before the whole-guide check']
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (k, p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
