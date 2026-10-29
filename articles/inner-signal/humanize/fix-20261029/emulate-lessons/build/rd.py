"""rd.py: where a sentence sits in a whole-guide recheck, and the windows that overlap it.
python3 rd.py RECHECK_DIR PART 'sentence'   (PART A or B; RESULT-<P>.json in DIR or DIR/read, TEXT-<P>.txt in DIR)"""
import json, sys, pathlib, re
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '–': '-', '—': '-'})

def load(dirp, part):
    d = pathlib.Path(dirp)
    res = None
    for c in [d / f'RESULT-{part}.json', d / 'read' / f'RESULT-{part}.json']:
        if c.exists():
            res = json.loads(c.read_text()); rf = c; break
    txt = None
    for c in [d / f'TEXT-{part}.txt', d.parent / f'TEXT-{part}.txt']:
        if c.exists():
            txt = c.read_text(); tf = c; break
    return res, rf, txt, tf

def windows_for(res, txt, sentence):
    t = txt.translate(FLAT)
    s = sentence.translate(FLAT)
    k = t.find(s)
    if k < 0:
        # try a prefix
        s2 = s[:60]
        k = t.find(s2)
        if k < 0:
            return None, []
        e = k + len(s)
    else:
        e = k + len(s)
    out = []
    for i, w in enumerate(res['windows']):
        a = w.get('start_index', w.get('start')); b = w.get('end_index', w.get('end'))
        if a < e and b > k:
            out.append((i, w['label'], w['confidence'], round(w.get('calibrated_confidence') or 0, 3), w.get('word_count', w.get('words')), w.get('is_humanized')))
    return (k, e), out

if __name__ == '__main__':
    res, rf, txt, tf = load(sys.argv[1], sys.argv[2])
    for s in sys.argv[3:]:
        span, ws = windows_for(res, txt, s)
        print(rf, '|', s[:70], '->', span, ws)
