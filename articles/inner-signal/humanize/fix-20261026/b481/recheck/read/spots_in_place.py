"""How each of batch 481's changes read in place in its recheck (2026-10-27, Joel's links of 15:37 UTC): for every spot of
../CHANGED-A.json and ../CHANGED-B.json (its new words, with my chance it reads red and my chance it reads Human at High
confidence, written before the paste), the windows of RESULT-A.json or RESULT-B.json that overlap its words, and the
spot's reading: its worst window (AI, then Human Low, Human Medium, Human High). Windows are numbered from 0, as
CONFIDENCE.md (window_confidence.py) numbers them. Writes SPOTS.json and SPOTS.md, with the
Brier score of the chances of High against what came.

  python3 articles/inner-signal/humanize/fix-20261026/b481/recheck/read/spots_in_place.py
"""
import json
import pathlib

X = pathlib.Path(__file__).resolve().parent
R = X.parent
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
RANK = {('Human', 'High'): 0, ('Human', 'Medium'): 1, ('Human', 'Low'): 2, ('AI', 'Low'): 3, ('AI', 'Medium'): 4,
        ('AI', 'High'): 5}


def kind(label):
    return 'AI' if str(label).startswith('AI') else 'Human'


def main():
    rows = []
    for part in ('A', 'B'):
        res = json.loads((X / ('RESULT-%s.json' % part)).read_text(encoding='utf-8'))
        text, wins = res['text'], res['windows']
        flat = text.translate(FLAT)
        for c in json.loads((R / ('CHANGED-%s.json' % part)).read_text(encoding='utf-8')):
            if c.get('chance_high') is None:
                continue  # the audit, kept as he wrote it, is a part of its own and not a change
            k = flat.find(c['text'].translate(FLAT))
            assert k >= 0 and flat.count(c['text'].translate(FLAT)) == 1, c['name']
            a, b = k, k + len(c['text'])
            over = [(i, w) for i, w in enumerate(wins) if w['start_index'] < b and w['end_index'] > a]
            worst = max(over, key=lambda iw: RANK[(kind(iw[1]['label']), iw[1]['confidence'])])
            read = '%s %s' % (kind(worst[1]['label']), worst[1]['confidence'])
            rows.append({'part': part, 'name': c['name'], 'text': c['text'], 'chance_red': c['chance_red'],
                         'chance_high': c['chance_high'], 'read': read,
                         'windows': ['#%d %s %s (%s, %d words)' % (i, kind(w['label']), w['confidence'],
                                                                   '%.3f' % w['calibrated_confidence']
                                                                   if w.get('calibrated_confidence') is not None else '-',
                                                                   w['word_count']) for i, w in over]})
    high = [r for r in rows if r['read'] == 'Human High']
    brier = sum((r['chance_high'] - (1 if r['read'] == 'Human High' else 0)) ** 2 for r in rows) / len(rows)
    (X / 'SPOTS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    out = ['# Batch 481\'s changes in place', '',
           'Each change of the recheck (its new words), the windows of its part that overlap them, and its reading: the '
           'worst of those windows. "My chance of High" was written before the paste (`../CHANCES.json`). Made by '
           '`spots_in_place.py`.', '',
           '%d changes: %d read Human at High confidence, %d at Medium, %d at Low, %d AI. Brier score of my chances of '
           'High: %.3f (always 0.5 would be 0.250).' % (
               len(rows), len(high), sum(r['read'] == 'Human Medium' for r in rows),
               sum(r['read'] == 'Human Low' for r in rows), sum(r['read'].startswith('AI') for r in rows), brier), '',
           '| part | change | reads | my chance of High | windows | its new words |', '| --- | --- | --- | --- | --- | --- |']
    for r in rows:
        out.append('| %s | %s | %s | %.2f | %s | %s |' % (r['part'], r['name'], r['read'], r['chance_high'],
                                                          '; '.join(r['windows']), r['text'][:160].replace('|', '/')))
    (X / 'SPOTS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('\n'.join(out[4:5]))
    for r in rows:
        if r['read'] != 'Human High':
            print(r['part'], r['name'], r['read'], r['windows'])


if __name__ == '__main__':
    main()
