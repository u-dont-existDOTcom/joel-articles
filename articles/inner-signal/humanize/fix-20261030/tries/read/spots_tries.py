"""SPOTS.json and SPOTS.md for the second recheck of 30 October (the tries; try 15 and try 13): how each try read in place
beside how the words it replaced read in the recheck before (../../recheck/read/RESULT-*.json), and every AI window of
this recheck with the try it sits on, if any. A spot's reading is its worst window: any AI window over its words makes it
AI (with that window's confidence); otherwise the lowest confidence of the Human windows over it.

  python3 articles/inner-signal/humanize/fix-20261030/tries/read/spots_tries.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
T = HERE.parent
LAST = T.parent / 'recheck' / 'read'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
ORDER = {'Low': 0, 'Medium': 1, 'High': 2}


def find(text, s):
    ft, fs = text.translate(FLAT), s.translate(FLAT).strip()
    for probe in (fs, fs[:150]):
        if probe and ft.count(probe) == 1:
            k = ft.find(probe)
            return k, k + len(probe)
    return None


def reading(result, a, b):
    ws = [(i, w) for i, w in enumerate(result['windows']) if w['start_index'] < b and w['end_index'] > a]
    ai = [(i, w) for i, w in ws if w['label'].startswith('AI')]
    if ai:
        worst = max(ai, key=lambda iw: ORDER.get(iw[1]['confidence'], 0))
        return 'AI (%s)' % worst[1]['confidence'], [i for i, _ in ai]
    low = min(ws, key=lambda iw: ORDER.get(iw[1]['confidence'], 0))[1]['confidence'] if ws else None
    return ('Human (%s)' % low) if low else 'not read', []


def main():
    tries = json.loads((T / 'TRIES.json').read_text(encoding='utf-8'))['tries']
    now = {p: json.loads((HERE / ('RESULT-%s.json' % p)).read_text(encoding='utf-8')) for p in 'AB'}
    last = {p: json.loads((LAST / ('RESULT-%s.json' % p)).read_text(encoding='utf-8')) for p in 'AB'}
    spots, covered = [], {'A': [], 'B': []}
    for t in tries:
        rec = {'id': t['id'], 'kind': t['kind'], 'where': t['where'], 'whose': t['whose'], 'after': t['after']}
        for p in 'AB':
            loc = find(now[p]['text'], t['after'])
            if not loc:
                continue
            rec['part'] = p
            rec['reading'], rec['ai_windows'] = reading(now[p], *loc)
            covered[p].append(loc)
            old = find(last[p]['text'], t['before'])
            rec['reading_before'] = reading(last[p], *old)[0] if old else 'not found'
            break
        spots.append(rec)
    red_elsewhere = []
    for p in 'AB':
        r = now[p]
        for i, w in enumerate(r['windows']):
            if not w['label'].startswith('AI'):
                continue
            a, b = w['start_index'], w['end_index']
            on = [s['id'] for s in spots if s.get('part') == p and i in s.get('ai_windows', [])]
            if not on:
                red_elsewhere.append({'part': p, 'window': i, 'confidence': w['confidence'],
                                      'calibrated': round(w.get('calibrated_confidence') or 0, 3),
                                      'words': w['word_count'], 'text': r['text'][a:b].strip()})
    (HERE / 'SPOTS.json').write_text(json.dumps({'spots': spots, 'red_elsewhere': red_elsewhere}, ensure_ascii=False,
                                                indent=1) + '\n', encoding='utf-8')
    lines = ['# The second recheck of 30 October: how each try read in place', '',
             'Each try (../TRIES.json) with its reading in this recheck and the reading of the words it replaced in the '
             'recheck before. A reading is the worst window over the words.', '']
    for s in spots:
        lines.append('- **%s** (%s; %s; part %s): now **%s**, before %s. %s' % (
            s['id'], s['kind'], s['where'], s.get('part', '?'), s.get('reading'), s.get('reading_before'),
            s['after'][:160] + ('...' if len(s['after']) > 160 else '')))
    lines += ['', '## Red on words no try changed', '']
    for x in red_elsewhere:
        lines.append('- **AI (%s)**, part %s window %d (calibrated %s), %d words: %s' % (
            x['confidence'], x['part'], x['window'], x['calibrated'], x['words'], x['text'][:400].replace('\n', ' / ')))
    (HERE / 'SPOTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(len(spots), 'tries;', len(red_elsewhere), 'AI windows elsewhere')


if __name__ == '__main__':
    main()
