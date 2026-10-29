"""aiwin.py: every AI window (and Human Low) of each 4.1 whole-guide check, with the origin of each sentence in it."""
import json, glob, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from whose import norm, PUB, OUTS
H = pathlib.Path(__file__).resolve().parents[3]  # build -> emulate-lessons -> fix-20261029 -> humanize
CHECKS = [
 ('41a', 'fix-20261020/result41/WINDOWS-41a.json', None),
 ('41b', 'fix-20261020/result41/WINDOWS-41b.json', None),
 ('41r2-b', 'fix-20261020/result41/WINDOWS-41r2-b.json', None),
 ('41r3-a', 'fix-20261020/result41/WINDOWS-41r3-a.json', None),
 ('1022-A', 'fix-20261022/recheck/RESULT-A.json', 'fix-20261022/recheck/TEXT-A.txt'),
 ('1023-A', 'fix-20261023/recheck/RESULT-A.json', 'fix-20261023/recheck/TEXT-A.txt'),
 ('1023-B', 'fix-20261023/recheck/RESULT-B.json', 'fix-20261023/recheck/TEXT-B.txt'),
 ('A3', 'fix-20261023/recheck-a3/RESULT-A.json', 'fix-20261023/recheck-a3/TEXT-A.txt'),
 ('A4', 'fix-20261023/recheck-a4/RESULT-A.json', 'fix-20261023/recheck-a4/TEXT-A.txt'),
 ('B2', 'fix-20261023/recheck-b2/RESULT-B.json', 'fix-20261023/recheck-b2/TEXT-B.txt'),
 ('1025-A', 'fix-20261025/recheck/RESULT-A.json', 'fix-20261025/recheck/TEXT-A.txt'),
 ('1025-B', 'fix-20261025/recheck/RESULT-B.json', 'fix-20261025/recheck/TEXT-B.txt'),
 ('479-A', 'fix-20261025/b479/recheck/RESULT-A.json', 'fix-20261025/b479/recheck/TEXT-A.txt'),
 ('479-B', 'fix-20261025/b479/recheck/RESULT-B.json', 'fix-20261025/b479/recheck/TEXT-B.txt'),
 ('480-A', 'fix-20261026/b480/recheck/read/RESULT-A.json', 'fix-20261026/b480/recheck/TEXT-A.txt'),
 ('480-B', 'fix-20261026/b480/recheck/read/RESULT-B.json', 'fix-20261026/b480/recheck/TEXT-B.txt'),
 ('481-A', 'fix-20261026/b481/recheck/read/RESULT-A.json', 'fix-20261026/b481/recheck/TEXT-A.txt'),
 ('481-B', 'fix-20261026/b481/recheck/read/RESULT-B.json', 'fix-20261026/b481/recheck/TEXT-B.txt'),
 ('1029-A', 'fix-20261029/recheck/read/RESULT-A.json', 'fix-20261029/recheck/TEXT-A.txt'),
 ('1029-B', 'fix-20261029/recheck/read/RESULT-B.json', 'fix-20261029/recheck/TEXT-B.txt'),
]
def sents(t):
    return [s for s in re.split(r'(?<=[.!?])\s+|\n+', t) if len(s.split()) >= 3]
def origin(s):
    n = norm(s)
    if len(n) < 12: return '?'
    if n in PUB: return 'PUB'
    hits = [f for f, t in OUTS.items() if n in t]
    if hits: return 'EMU:' + hits[0].split('/')[-2]
    return 'OTHER'
def windows(rf, tf):
    d = json.loads((H / rf).read_text())
    ws = d['windows']
    txt = (H / tf).read_text() if tf else None
    out = []
    for w in ws:
        a = w.get('start_index', w.get('start')); b = w.get('end_index', w.get('end'))
        text = w.get('text') if 'text' in w else (txt[a:b] if txt else '')
        out.append(dict(label=w['label'], conf=w['confidence'], words=w.get('word_count', w.get('words')), hum=w.get('is_humanized'), text=text, cal=w.get('calibrated_confidence')))
    return d, out
if __name__ == '__main__':
    only = sys.argv[1:] 
    for name, rf, tf in CHECKS:
        if only and name not in only: continue
        try:
            d, ws = windows(rf, tf)
        except Exception as e:
            print('ERR', name, e); continue
        ai = [w for w in ws if not w['label'].startswith('Human')]
        print('=====', name, rf, '| windows', len(ws), '| AI', len(ai), '| humanized flags', sum(1 for w in ws if w['hum']))
        for w in ai:
            ss = sents(w['text'])
            org = [origin(s) for s in ss]
            print('  [%s %s %sw hum=%s] %s' % (w['label'], w['conf'], w['words'], w['hum'], re.sub(r'\s+',' ',w['text'])[:160]))
            from collections import Counter
            print('      origins:', dict(Counter(org)))
