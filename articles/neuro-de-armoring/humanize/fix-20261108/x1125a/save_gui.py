"""Save what his Pangram history returned for a batch (read by SHA-256 in the page, window.__readIdx: each window as
[label, confidence, words, start, end]) into DIR/RESULTS-GUI.json in the shape record_gui.py reads, with each window's
text cut from the checked text (DIR/TEXTS.json).

  python3 .../x1125a/save_gui.py DIR 'JSON from the page'
"""
import json
import pathlib
import re
import sys

DETECTOR = 'Pangram 4.1 (web app, his account, Claude in Chrome in his browser)'
D = pathlib.Path(sys.argv[1])
got = json.loads(sys.argv[2])
texts = json.loads((D / 'TEXTS.json').read_text(encoding='utf-8'))
f = D / 'RESULTS-GUI.json'
res = json.loads(f.read_text(encoding='utf-8')) if f.exists() else {'detector': DETECTOR, 'results': {}}
for k, r in got.items():
    n = re.sub(r'\n{2,}', '\n', texts[k])
    r['windows'] = [[w[0], w[1], w[2], n[w[3]:w[4]].strip(' .') if False else n[w[3]:w[4]].strip()] for w in r['windows']]
    res['results'][k] = r
    print(k, r['headline'], '%.1f%% AI' % (r['ai'] * 100), '; '.join('%s %s %d' % (w[0], w[1], w[2]) for w in r['windows']))
f.write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
