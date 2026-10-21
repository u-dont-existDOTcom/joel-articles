"""Batch 468g's predictions, written before the run (2026-10-21): batch/PREDICTIONS.md, and one ledger prediction per
text (tools/humanization/pangram_ledger.py, articles/inner-signal/humanize/pangram-ledger.jsonl), which refuses what the
2026-10-20 budget rule forbids (a retry with no diagnosis, a lineage past its tries, the same text twice).

  python3 articles/inner-signal/humanize/fix-20261020/b468/make_preds_b468.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
B = pathlib.Path(__file__).resolve().parent
LEDGER = REPO / 'articles' / 'inner-signal' / 'humanize' / 'pangram-ledger.jsonl'

# key: (lineage, scope, call, chance, why, tells, human tells)
PREDS = {
    'HG15-p9e2': ('HG15-p9', 'paragraph', 'Human', 0.5,
                  'the concession in the frame of Joel\'s that read dark green in 4.1, the reframe as what the reader does; '
                  'the closer is still a conditional reframe ("if ..., then you\'re using it to buy belonging")',
                  'a conditional reframe closing the paragraph; "feels like losing yourself" kept from the published text',
                  '"I\'m not saying ... can\'t be", "by for example ... etc.", the opening question'),
    'HG35-forgive-e3': ('HG35-p13', 'paragraph', 'AI', 0.45,
                        'the four points as clauses about the people in one uneven sentence; still four points in one '
                        'sentence after "it can all be true at once", and it ends on the forgiveness, a hopeful turn',
                        'four points in a row; a "but one day we may find" turn at the end',
                        'his run-on first sentence and "We can not \'force\'", "They really did hurt us", "answer for it"'),
    'HG35-quote-e': ('HG35-p15', 'paragraph', 'AI', 0.45,
                     'the two promises as one spoken sentence, so the red one is read with the one that read Human; the '
                     'permission stays its own sentence as installed (its break), and it was inside the AI-low run; checked '
                     'with the paragraph before it (Human, high, its last sentence medium, in the section check)',
                     'the stock "You don\'t have to forgive before you\'re ready." unchanged; the paragraph before ends on a '
                     'light-green line', '"I\'m not going to", "our whole life", "and I also won\'t"'),
    'HG35-selfforgive-e': ('HG35-p18', 'paragraph', 'Human', 0.5,
                           'the person feels the remorse and takes in the harm, the two cautions in different shapes, no '
                           '"without ...ing"; checked with the paragraph after it (Human in the section check, its first '
                           'sentence low)',
                           'two instructions in a row still, the second a packed sentence; the paragraph after starts with a '
                           'four-step list (light green)',
                           '"permanent criminal", "stop short of", B680\'s run-on with "feel the remorse" twice'),
}


def main():
    drafts = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
    edits = {e['key']: e for e in json.loads((B / 'meta.json').read_text(encoding='utf-8'))['edits']}
    rows = ['# Predictions and Pangram results: batch 468g', '',
            "Pangram's web app (4.1). The second tries for batch 467g's two misses (HG15-p9, HG35-p13) and the first 4.1 "
            "tries for the two lines of Appendix F that read AI, low, in its section check (HG35-p15, HG35-p18), each "
            "paragraph as Pangram reads it (a paragraph under 50 words with its neighbor). Predictions written before the "
            'run; chance = my chance of a 100% Human result.', '', '## Batch 468g', '',
            '| text | mine | chance | why | Pangram |', '|---|---|---|---|---|']
    tmp = B / 'batch' / 'texts'
    tmp.mkdir(parents=True, exist_ok=True)
    for key, (lineage, scope, call, chance, why, tells, human) in PREDS.items():
        rows.append('| %s | %s | %d%% | %s | |' % (key, call, round(chance * 100), why))
        f = tmp / ('%s.txt' % key)
        f.write_text(drafts[key], encoding='utf-8')
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                            '--lineage', lineage, '--scope', scope, '--text', str(f), '--key', key, '--batch', 'b468g',
                            '--call', call, '--chance', str(chance), '--tells', tells, '--human-tells', human,
                            '--diagnosis', edits[key]['diagnosis'], '--detector', 'pangram 4.1, web app'],
                           capture_output=True, text=True, cwd=REPO)
        print(key, (r.stdout or r.stderr).strip()[-300:])
        if r.returncode:
            return r.returncode
    (B / 'batch' / 'PREDICTIONS.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
