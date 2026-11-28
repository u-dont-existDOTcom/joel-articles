"""Which of his fixes (PAIRS.json) changed a text that had already read Human High in every window in Pangram?"""
import json, sys, re, glob
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2] / 'tools' / 'humanization'))
import pangram_ledger as L
REPO = str(__import__('pathlib').Path(__file__).resolve().parents[2]) + '/'
def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('—', '--')
    s = re.sub(r'\]\([^)]*\)', '', s)
    return re.sub(r'\s+', ' ', re.sub(r'[*_#>\[\]]', '', s)).strip().lower()
def wins(res):
    out = []
    for w in res.get('windows') or []:
        if isinstance(w, dict):
            out.append((str(w.get('label') or ''), str(w.get('confidence') or '')))
        else:
            parts = [p.strip() for p in str(w).split(',')]
            out.append((parts[0] if parts else '', parts[1] if len(parts) > 1 else ''))
    return out
def all_high(res):
    ws = wins(res)
    return bool(ws) and all(l in ('Human', 'Human Written') and c == 'High' for l, c in ws)
recs = []
for lp in glob.glob(REPO + 'articles/*/humanize/pangram-ledger.jsonl') + [REPO + 'articles/inner-child-therapy/tools/pangram-ledger.jsonl']:
    st = L.state(L.read(lp)); vals = st.values() if isinstance(st, dict) else st
    for r in vals:
        if isinstance(r, dict) and r.get('text') and r.get('result'):
            recs.append((norm(r['text']), r))
pairs = json.load(open(REPO + 'articles/bad-trips/humanize/h46-20261112/his-fixes/PAIRS.json'))['kept']
out = []
checked = 0
for p in pairs:
    b = norm(p['before'])
    if len(b) < 40:
        continue
    h = norm(p['his'])
    # the whole before inside the checked text, and the checked text not his version (a prefix match took his
    # versions that start like the before: the re-tag reader caught three such false matches, 2026-11-28)
    found = [r for t, r in recs if b in t and not (h != b and h in t)]
    if found:
        checked += 1
    hh = [r for r in found if all_high(r['result'])]
    if hh:
        best = hh[0]
        out.append({'lane': p['lane'], 'id': p['id'], 'title': p.get('title'), 'file': p['file'], 'before': p['before'],
                    'his': p['his'], 'comment': p.get('comment', ''), 'before_check': best['result'].get('link'),
                    'before_scope': best.get('scope'), 'before_words': best.get('words')})
print('his fixes whose before was checked in Pangram:', checked, 'of', len(pairs))
print('of those, whose before had read Human High in every window:', len(out))
pass
for o in out: print(o['lane'], o['id'], o['before_scope'], o['before_words'], o['before_check'])
