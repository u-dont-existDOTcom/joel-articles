#!/usr/bin/env python3
"""status.py - where each sentence of the guide as it stands was last checked in Pangram, and what its window read.

Turn 49 (2026-11-19), the next step after round 42: the Medium windows of the first batch (h42), the lesson-19b way. The
first batch is ten passes old, so this finds, for every sentence of GUIDE-SO-FAR.md, the newest check whose text holds it
(the ledger's predictions and results, newest first), and the window it fell in (the window texts the passes from h42 on
keep in their RESULTS-*.json: AI windows, then Human windows below High). A sentence in a check whose windows were all
Human High, or in none of its listed windows, read Human High there.

  python3 status.py      writes STATUS.json and STATUS.md beside it
"""
import glob, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
HUM = ART / 'humanize'
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
HIS = set(json.loads((HUM / 'h41-20261109/boilerplate/HIS-OWN.json').read_text(encoding='utf-8')))

FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '–': '-', '—': '-', ' ': ' '})


def plain(md):
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)
    t = re.sub(r'\[([^\]]*)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', t)
    t = re.sub(r'<sub>(.*?)</sub>', r'\1', t)
    t = t.replace('**', '').replace('__', '')
    t = re.sub(r'(?<![\w*])\*(?!\s)([^*\n]+?)\*(?!\w)', r'\1', t)
    out = []
    for l in t.split('\n'):
        l = re.sub(r'^\s*(?:[-*]|\d+\.)\s+', '', l)
        l = re.sub(r'^\s*>\s?', '', l)
        l = re.sub(r'^#+\s*', '', l)
        out.append(l.rstrip())
    return '\n'.join(out).strip()


def norm(s):
    s = s.translate(FLAT).lower().replace('--', '-')
    s = re.sub(r'[*_`#>]', '', s)
    return re.sub(r'\s+', ' ', s).strip(' "\'()[]')


def sentences(text):
    out = []
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        parts = re.split(r'(?<=[.!?])["\')\]]?\s+(?=[A-Z0-9"(\[])', line)
        out += [p.strip() for p in parts if len(p.split()) >= 1]
    return out


# ---- every check: its text (prediction) and its result, newest last ----
preds, results = {}, {}
for line in (HUM / 'pangram-ledger.jsonl').read_text(encoding='utf-8').splitlines():
    d = json.loads(line)
    if d.get('type') == 'prediction' and d.get('text'):
        preds[d['id']] = d
    elif d.get('type') == 'result':
        results.setdefault(d.get('prediction'), d)
uuid = lambda s: (re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', s or '') or [None])[0]
wtexts = {}
for f in glob.glob(str(HUM / '**/RESULTS*.json'), recursive=True):
    if '-idx' in f:
        continue
    try:
        d = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    except Exception:
        continue
    if not isinstance(d, dict):
        continue
    for k, v in d.items():
        if isinstance(v, list) and len(v) >= 8 and uuid(str(v[5])):
            # the summary, in order: "Human, High, 39; AI-Generated, Low, 9; ..."; h42 kept an AI window's text without its
            # confidence ("AI-Generated (9 words): ..."), so it is taken from the summary, in order, by label and words
            summ = []
            for part in str(v[3]).split(';'):
                q = [x.strip() for x in part.split(',')]
                if len(q) == 3 and q[2].isdigit():
                    summ.append({'label': q[0], 'conf': q[1], 'words': int(q[2]), 'used': False})
            ws = []
            for w in list(v[6]) + list(v[7]):
                m = re.match(r'(AI-Generated|AI-Assisted|Human)\s*(High|Medium|Low)?\s*\((\d+) words\):\s*(.*)$', str(w), re.S)
                if not m:
                    continue
                lab, conf, n, txt = m.group(1), m.group(2), int(m.group(3)), m.group(4)
                if conf is None:
                    s = next((x for x in summ if not x['used'] and x['label'] == lab and x['words'] == n), None) or \
                        next((x for x in summ if not x['used'] and x['label'] == lab), None)
                    if s:
                        s['used'] = True
                        conf = s['conf']
                ws.append({'label': lab, 'conf': conf or '?', 'words': n, 'text': txt})
            wtexts[uuid(str(v[5]))] = ws
checks = []
for pid, p in preds.items():
    r = results.get(pid)
    if not r or not r.get('windows'):
        continue
    u = uuid(r.get('link'))
    wins = []
    for w in r['windows']:
        if isinstance(w, str):   # the older form, "Human, High, 83"
            q = [x.strip() for x in w.split(',')]
            w = {'label': 'Human' if q[0] == 'Human' else 'AI', 'confidence': q[1] if len(q) > 1 else '?'}
        wins.append(w)
    r['windows'] = wins
    allhigh = all(w.get('label') == 'Human' and w.get('confidence') == 'High' for w in wins)
    checks.append({'id': pid, 'at': p.get('at', ''), 'text': norm(p['text']), 'link': r.get('link'), 'uuid': u,
                   'headline': r.get('headline'), 'windows': r['windows'], 'allhigh': allhigh,
                   'wtexts': [dict(w, n=norm(w['text'])) for w in wtexts.get(u, [])], 'scope': p.get('scope')})
checks.sort(key=lambda c: c['at'])

# ---- each sentence of the guide as it stands ----
rows, heading = [], ''
for b in BLOCKS:
    if b['kind'] in ('image', 'youtube', 'hr') or not b.get('md'):
        continue
    if b['kind'] in ('h1', 'h2', 'h3'):
        heading = plain(b['md'])
    for s in sentences(plain(b['md'])):
        ns = norm(s)
        if len(ns) < 3:
            continue
        hit = None
        for c in reversed(checks):
            if ns in c['text']:
                hit = c
                break
        row = {'block': b['id'], 'kind': b['kind'], 'heading': heading, 's': s, 'his_block': b['id'] in HIS or
               b['id'].startswith(('N-', 'R27-', 'R30-OILS', 'R30-RUE'))}
        if hit is None:
            row['status'] = 'never checked'
        else:
            row.update(check=hit['id'], at=hit['at'], link=hit['link'], scope=hit['scope'], headline=hit['headline'])
            if hit['allhigh']:
                row['status'] = 'Human High'
            elif not hit['wtexts']:
                row['status'] = 'below High somewhere in its check (window texts not kept)'
                row['windows'] = hit['windows']
            else:
                w = next((w for w in hit['wtexts'] if ns in w['n'] or (len(w['n']) > 12 and w['n'] in ns)), None)
                row['status'] = 'Human High' if w is None else '%s %s' % (w['label'], w['conf'])
                if w is not None:
                    row['window'] = '%s %s (%d words): %s' % (w['label'], w['conf'], w['words'], w['text'])
        rows.append(row)

(HERE / 'STATUS.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
bad = [r for r in rows if r['status'] != 'Human High']
md = ['# Each sentence of the guide as it stands, by its newest Pangram check (turn 49, 2026-11-19)', '',
      'Made by `status.py` from `../pangram-ledger.jsonl` and the window texts the passes from h42 on keep. %d sentences; '
      '%d read Human High in their newest check; %d below High, never checked, or in a check whose window texts '
      'weren\'t kept.' % (len(rows), len(rows) - len(bad), len(bad)), '',
      'What it can\'t see: checks Joel ran himself, which are in his Pangram history and not in the ledger. His versions put '
      'in whole (the medical part\'s Call medics list, Risk of Harm, MDMA, Chest Pain, Recent Oral Toxic Ingestion, Serotonin '
      'Syndrome\'s steps, My Brain Feels Damaged, Active Seizure) read Human High in his own checks, so a sentence of theirs '
      'shown here as AI from an older section check, or as never checked, is his and read High. Everything else here is '
      'the work still to do: each paragraph checked by itself as it stands first (this turn, 10 of 26 paragraphs with a '
      'window below High in a section check read Human High alone).', '',
      '| block | heading | his block | status | sentence | check |', '|---|---|---|---|---|---|']
for r in bad:
    link = '[%s](%s)' % (uuid(r.get('link'))[:8], r['link']) if r.get('link') else ''
    md.append('| %s | %s | %s | %s | %s | %s |' % (r['block'], r['heading'][:40], 'his' if r['his_block'] else '',
                                                   r['status'], r['s'].replace('|', '/')[:160], link))
(HERE / 'STATUS.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(len(rows), 'sentences;', len(bad), 'not Human High in their newest check')
import collections
print(collections.Counter(r['status'] for r in rows))
