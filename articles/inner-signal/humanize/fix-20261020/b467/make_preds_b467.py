"""Batch 467g's predictions, written before the run (2026-10-21): PREDICTIONS.md here, and one ledger prediction per text
(tools/humanization/pangram_ledger.py, articles/inner-signal/humanize/pangram-ledger.jsonl), which refuses what the
2026-10-20 budget rule forbids.

  python3 articles/inner-signal/humanize/fix-20261020/b467/make_preds_b467.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
B = pathlib.Path(__file__).resolve().parent
LEDGER = REPO / 'articles' / 'inner-signal' / 'humanize' / 'pangram-ledger.jsonl'

# key: (lineage, scope, call, chance, why, tells, human tells)
PREDS = {
    'HG12-p3c': ('HG12-p3', 'paragraph', 'Human', 0.85,
                 'the paragraph without its red closer; its other sentences read Human, high in the whole guide',
                 'a long packed first sentence', 'his "IN my mind", the parenthetical aside'),
    'HG12-p7e': ('HG12-p7', 'paragraph', 'Human', 0.65,
                 'his story with a plain closer; light green around the red closer in the whole guide (the lust sentence at AI '
                 'likelihood 0.48)', 'light-green sentences next to where the red one was',
                 'his particulars (lust energy, the heart and sacral chakras, the "perfected" love state)'),
    'HG15-p9e': ('HG15-p9', 'paragraph', 'Human', 0.65,
                 'the doer question and its list, then one plain sentence for the reassurance and the aphorism',
                 'a list of five and "etc." in one sentence', 'the opening question, "it has become a way to buy belonging"'),
    'HG15-p11t': ('HG15-p11', 'paragraph', 'Human', 0.8,
                  'one word back to the guide\'s term ("inherited parent"); the paragraph read Human, high in the whole guide '
                  'apart from the adult\'s line (low)', 'the adult\'s scripted "X, not Y" line, light green',
                  'his "And that’s not good because ..."'),
    'HG33-buteyko-e': ('HG33-p4', 'paragraph', 'Human', 0.7,
                       'the three breathing steps as two sentences; his NOTE in capitals and STOP! around them',
                       'instructions in a row', 'his capitals, the parenthetical NOTE, the question to the reader'),
    'HG35-forgive-e2': ('HG35-p13', 'paragraph', 'Human', 0.5,
                        'the colon list as two sentences of two points; the question stays, and it read AI (low) in part B',
                        'the signpost question kept', 'his run-on first sentence, "We can not \'force\' forgiveness"'),
    'HG12-w467': ('HG12', 'section', 'Human', 0.55,
                  'the section with both fixes; its light green (the set-up and reveal in P1, "amplified with loveyhuasca") '
                  'is left', 'two light-green stretches left', 'his particulars throughout, the chrunga paragraph'),
    'HG15-w467': ('HG15', 'section', 'Human', 0.5,
                  'the section with its fix; its question lists read Human, high in the whole guide, but alone a section '
                  'of question lists is at risk', 'three question lists', 'his casual openings, "adulting"'),
    'HG33-w467': ('HG33', 'section', 'Human', 0.55,
                  'the appendix with the breathing fix; light green elsewhere in it in part B (the protector sentence, the '
                  'inner child line)', 'light-green stretches left', 'his capitals and asides'),
    'HG35-w467': ('HG35', 'section', 'Human', 0.45,
                  'the appendix with the forgiveness fix; the question kept, and more light green in part B',
                  'the kept question, light green left', 'his questions to ask a hypnotist, his quoted lines'),
}


def main():
    drafts = json.loads((B / 'batch' / 'drafts.json').read_text(encoding='utf-8'))
    gate = json.loads((B / 'batch' / 'GATE.json').read_text(encoding='utf-8'))
    rows = ['# Predictions and Pangram results: batch 467g', '',
            "Pangram's web app (4.1). The first fixes from the whole guide's 4.1 reading (the Substack checks of 2026-10-20, "
            "`../substack41/RESULT-41a.json` and `RESULT-41b.json`): each changed paragraph alone and each section whole. "
            'Predictions written before the run; chance = my chance of a 100% Human result.', '', '## Batch 467g', '',
            '| text | mine | chance | why | Pangram |', '|---|---|---|---|---|']
    tmp = B / 'batch' / 'texts'
    tmp.mkdir(exist_ok=True)
    for key, (lineage, scope, call, chance, why, tells, human) in PREDS.items():
        rows.append('| %s | %s | %d%% | %s | |' % (key, call, round(chance * 100), why))
        f = tmp / ('%s.txt' % key)
        f.write_text(drafts[key], encoding='utf-8')
        diag = gate[key].get('diagnosis') or gate[key].get('was', '')
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                            '--lineage', lineage, '--scope', scope, '--text', str(f), '--key', key, '--batch', 'b467g',
                            '--call', call, '--chance', str(chance), '--tells', tells, '--human-tells', human,
                            '--diagnosis', diag, '--detector', 'pangram 4.1, web app'],
                           capture_output=True, text=True, cwd=REPO)
        print(key, (r.stdout or r.stderr).strip()[-200:])
        if r.returncode:
            return r.returncode
    (B / 'batch' / 'PREDICTIONS.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
