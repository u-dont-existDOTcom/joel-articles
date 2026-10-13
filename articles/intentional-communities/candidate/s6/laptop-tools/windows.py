"""Copy of pangram-runs/community-s5/windows.py on Joel's laptop (2026-10-06): print each entry of a Pangram API batch log
with its windows (label, score, confidence, words, start and end of the text), read from the API cache by the text's sha256.
Usage there: python3 community-s5/windows.py api60.log [name ...]"""
import json, sys
from pathlib import Path
HERE = Path(__file__).parent
log = HERE / sys.argv[1]
only = set(sys.argv[2:])
for l in open(log, encoding='utf-8'):
    l = l.strip()
    if not l.startswith('{'):
        continue
    d = json.loads(l)
    if only and d['name'] not in only:
        continue
    c = json.load(open(HERE / 'out' / 'cache' / (d['sha256'] + '.json'), encoding='utf-8'))
    ws = c.get('windows') or c.get('result', {}).get('windows') or []
    print('==', d['name'], d['words'], d['prediction_short'], 'ai', d['fraction_ai'], 'assist', d['fraction_ai_assisted'])
    for w in ws:
        t = w.get('text', '')
        print('  ', w.get('label'), round(w.get('ai_assistance_score', 0), 3), w.get('confidence'), w.get('word_count'), '|', t[:90].replace('\n', ' / '), '...', t[-60:].replace('\n', ' / '))
