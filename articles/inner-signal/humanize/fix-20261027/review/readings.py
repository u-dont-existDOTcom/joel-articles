"""Each card's reading in place (2026-10-27): for every card of question 21's page (../../fix-20261026/review/
build_review_481.py's CARDS), how its new words read in Joel's newest check (batch 481's recheck, read in
../../fix-20261026/b481/recheck/read/, his links of 2026-10-27 15:37 UTC), and for batch 481's cards how the words they
replace read in the check before it (batch 480's recheck, ../../fix-20261026/b480/recheck/read/): the worst window over
the words (AI, then Human Low, Medium, High), with its calibrated confidence.

  python3 articles/inner-signal/humanize/fix-20261027/review/readings.py   -> READINGS.json
"""
import importlib.util
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", ' ': ' '})
RANK = {('Human', 'High'): 0, ('Human', 'Medium'): 1, ('Human', 'Low'): 2, ('AI', 'Low'): 3, ('AI', 'Medium'): 4,
        ('AI', 'High'): 5}
NEW = {p: json.loads((H / ('fix-20261026/b481/recheck/read/RESULT-%s.json' % p)).read_text(encoding='utf-8')) for p in 'AB'}
OLD = {p: json.loads((H / ('fix-20261026/b480/recheck/read/RESULT-%s.json' % p)).read_text(encoding='utf-8')) for p in 'AB'}
FEED = {p: NEW[p]['link'] for p in 'AB'}


def kind(label):
    return 'AI' if str(label).startswith('AI') else 'Human'


def reading(results, words):
    """(part, label, confidence, calibrated, window number) of the worst window over WORDS, or None if not found once."""
    w = words.translate(FLAT).strip()
    for p, r in results.items():
        t = r['text'].translate(FLAT)
        if t.count(w) == 1:
            a = t.index(w)
            b = a + len(w)
            over = [(i, x) for i, x in enumerate(r['windows']) if x['start_index'] < b and x['end_index'] > a]
            i, x = max(over, key=lambda iw: RANK[(kind(iw[1]['label']), iw[1]['confidence'])])
            return {'part': p, 'label': kind(x['label']), 'confidence': x['confidence'],
                    'calibrated': round(x['calibrated_confidence'], 3) if x.get('calibrated_confidence') is not None else None,
                    'window': i, 'words': x['word_count']}
    return None


def main():
    spec = importlib.util.spec_from_file_location('b481', H / 'fix-20261026/review/build_review_481.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    out = {}
    for sid, name, old_ref, new_ref, typ, title, why, note in m.CARDS:
        old_c, new_c = m.SPOTS[old_ref[0]][old_ref[1]], m.SPOTS[new_ref[0]][new_ref[1]]
        now = reading(NEW, new_c['new'])
        before = reading(OLD, old_c['old']) if new_ref[0] == 'b481' else None
        out[sid] = {'title': title, 'type': typ, 'batch': new_ref[0], 'now': now, 'before': before}
    (HERE / 'READINGS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for sid, r in out.items():
        n, b = r['now'], r['before']
        f = lambda x: '-' if not x else '%s %s %s (%s)' % (x['part'], x['label'], x['confidence'], x['calibrated'])
        print('%-7s %-5s now %-28s before %s' % (sid, r['batch'], f(n), f(b)))


if __name__ == '__main__':
    main()
