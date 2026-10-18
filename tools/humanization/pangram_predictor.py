#!/usr/bin/env python3
"""pangram_predictor.py - learn, from the lane's own Pangram checks, what predicts a "Human Written" result (2026-10-18).

Joel, 2026-10-18 01:29 UTC: "your mission is to improve the scorecard especially for predictions and fixes, as well as the speed
of fixing." My written predictions run about 80% right lately; this asks the checks themselves. Every batch folder of the
community lane (and any other folder given) that keeps drafts.json, GATE.json and a results file is one row per checked text:
the exact text, the gate's kind of record (screen, draft, edit, owner, section), Pangram's headline, and my written prediction
where the batch's PREDICTIONS table has one.

  python3 tools/humanization/pangram_predictor.py collect ROOT [ROOT ...] --out DATA.json
  python3 tools/humanization/pangram_predictor.py evaluate DATA.json [--report REPORT.json]
  python3 tools/humanization/pangram_predictor.py train DATA.json --model MODEL.json
  python3 tools/humanization/pangram_predictor.py predict MODEL.json DRAFTS.json [--gate GATE.json]

"evaluate" cross-validates by batch (no batch is in both its training and test fold), for paragraphs and for whole sections
apart, and prints the accuracy beside mine on the same texts and beside always saying AI. "train" fits on everything and
writes the model as plain JSON (feature means, scales and weights; no pickle). "predict" gives each text its probability of
"Human Written" and the features that pushed it most, for the PREDICTIONS table's "why".

The features are counted, not judged: sentence lengths and their spread, punctuation, contractions, pronouns, the lane's
mechanical tells (lists of three, "and ... and", "not X but Y", summing-up closers), stock AI words, and the record's kind
(Joel's own text, my draft, a cheap screen, a section). A probability is a forecast of Pangram, like the march, never a
reason to skip a check that a rule requires.
"""
import argparse, glob, hashlib, json, math, os, re, sys
from collections import Counter, defaultdict

PASS = 'Human Written'
KINDS = ('owner', 'draft', 'edit', 'screen', 'section')
AI_WORDS = ('crucial', 'delve', 'foster', 'nuanced', 'tapestry', 'landscape', 'robust', 'navigate', 'navigating', 'ensure', 'ensuring',
            'meaningful', 'genuine', 'genuinely', 'deeply', 'profound', 'intricate', 'realm', 'underscore', 'pivotal', 'holistic',
            'framework', 'dynamic', 'dynamics', 'journey', 'essential', 'vital', 'leverage', 'cultivate', 'cultivating', 'resonate',
            'embrace', 'embracing', 'transformative', 'nurture', 'nurturing', 'boundaries', 'authentic', 'intentional', 'ultimately',
            'truly', 'quietly', 'subtle', 'subtly', 'invaluable', 'seamless', 'testament', 'multifaceted', 'interplay', 'capacity')
CASUAL = ('lol', 'etc', 'kinda', 'gonna', 'wanna', 'ok', 'okay', 'yeah', 'actually', 'really', 'pretty', 'stuff', 'guy', 'guys',
          'folks', 'crazy', 'super', 'totally', 'basically', 'anyway', 'honestly', 'damn', 'shit', 'hell', 'weird', 'cool')
FIRST = re.compile(r"\b(i|me|my|mine|i'm|i've|i'd|i'll)\b", re.I)
SECOND = re.compile(r"\b(you|your|yours|you're|you've|you'll|you'd)\b", re.I)
WE = re.compile(r"\b(we|us|our|ours|we're|we've)\b", re.I)
CONTR = re.compile(r"\b\w+(n't|'re|'s|'ll|'ve|'m|'d)\b", re.I)
TRIAD = re.compile(r"\b[\w-]+(?: [\w-]+){0,3}, [\w-]+(?: [\w-]+){0,3},? (?:and|or) [\w-]+", re.I)
NOT_BUT = re.compile(r"\bnot (?:just |only |merely |simply )?[\w' -]{1,40}?,? but\b|\bisn't (?:just |only )?[\w' -]{1,40}?[.;,] it's\b", re.I)
AND_AND = re.compile(r"\b(and|or)\b[^.,;:!?]{1,60}\b\1\b[^.,;:!?]{1,60}\b\1\b", re.I)
CLOSER = re.compile(r"(?:^|[.!?]\s+)(?:this|that|these|those|it|all of this|in the end|ultimately|in short)\b[^.!?]{0,80}[.!?]\s*$", re.I)
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')


def plain(t):
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'[*_`#>]', '', t)
    return t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')


def sentences(t):
    return [s for s in re.split(r'(?<=[.!?])["\')\]]*\s+(?=[A-Z0-9"\'(\[])', t.strip()) if s.strip()]


def features(text, kind=None):
    t = plain(text)
    w = re.findall(r"[A-Za-z']+", t)
    n = max(len(w), 1)
    ss = sentences(t)
    lens = [len(re.findall(r"[A-Za-z']+", s)) for s in ss] or [n]
    m = sum(lens) / len(lens)
    sd = math.sqrt(sum((x - m) ** 2 for x in lens) / len(lens))
    per = lambda c: 100.0 * c / n
    low = [x.lower() for x in w]
    lc = Counter(low)
    paras = [p for p in re.split(r'\n\s*\n', text) if p.strip()]
    f = {
        'log_words': math.log(n),
        'sent_mean': m, 'sent_sd': sd, 'sent_cv': sd / m if m else 0, 'sent_max': max(lens),
        'short_sent': sum(1 for x in lens if x < 8) / len(lens), 'long_sent': sum(1 for x in lens if x > 30) / len(lens),
        'comma': per(t.count(',')), 'semicolon': per(t.count(';')), 'colon': per(t.count(':')),
        'dash': per(t.count('—') + t.count(' - ') + t.count('--')), 'paren': per(t.count('(')),
        'quote': per(t.count('"')), 'question': per(t.count('?')), 'exclaim': per(t.count('!')),
        'ellipsis': per(t.count('...') + t.count('…')),
        'contraction': per(len(CONTR.findall(t))), 'first': per(len(FIRST.findall(t))), 'second': per(len(SECOND.findall(t))),
        'we': per(len(WE.findall(t))),
        'triad': per(len(TRIAD.findall(t))), 'not_but': per(len(NOT_BUT.findall(t))), 'and_and': per(len(AND_AND.findall(t))),
        'closer': 1.0 if any(CLOSER.search(p.strip()) for p in paras) else 0.0,
        'ai_words': per(sum(lc[x] for x in AI_WORDS)), 'casual': per(sum(lc[x] for x in CASUAL)),
        'emoji': per(len(EMOJI.findall(text))), 'digits': per(len(re.findall(r'\d+', t))),
        'starts_and_but_so': sum(1 for s in ss if re.match(r'^(and|but|so|or)\b', s.strip(), re.I)) / len(ss) if ss else 0,
        'ttr': len(set(low[:150])) / max(len(low[:150]), 1), 'long_words': sum(1 for x in w if len(x) >= 9) / n,
        'paras': len(paras),
    }
    for k in KINDS:
        f['kind_' + k] = 1.0 if kind == k else 0.0
    return f


# --- collecting the lane's checks -----------------------------------------------------------------------------------

def result_headline(v):
    if isinstance(v, list):
        return v[0], v[1], v[3] if len(v) > 3 else ''
    return v.get('headline'), v.get('avg_ai_likelihood'), '; '.join(v.get('windows') or [])


def my_calls(root):
    """batch number -> {key: my call}, from the PREDICTIONS tables (the "mine" column) beside each batch."""
    out = defaultdict(dict)
    for f in glob.glob(os.path.join(root, '**', 'PREDICTIONS*.md'), recursive=True):
        hdr = None
        for ln in open(f, encoding='utf-8'):
            if not ln.startswith('|'):
                if ln.startswith('#'):
                    hdr = hdr  # headings don't reset the table
                continue
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            low = [c.lower() for c in cells]
            if 'mine' in low and 'text' in low:
                hdr = (low.index('text'), low.index('mine')); continue
            if hdr and len(cells) > max(hdr) and not re.match(r'^:?-+:?$', cells[0]):
                key, mine = cells[hdr[0]], cells[hdr[1]].split()[0] if cells[hdr[1]] else ''
                m = re.match(r'^(\d{3})g-(.+)$', key)
                b = re.search(r'/b(\d{3})/', f.replace('\\', '/'))
                if m:
                    out[int(m.group(1))][m.group(2)] = mine
                elif b:
                    out[int(b.group(1))][key] = mine
    return out


def collect(roots):
    rows, seen = [], set()
    for root in roots:
        calls = my_calls(root)
        for d in sorted(glob.glob(os.path.join(root, '**', 'drafts.json'), recursive=True)):
            folder = os.path.dirname(d)
            res = sorted(glob.glob(os.path.join(folder, '*results*.json')))
            if not res:
                continue
            m = re.search(r'b(\d{3})', os.path.basename(res[0])) or re.search(r'b(\d{3})', folder)
            batch = int(m.group(1)) if m else None
            drafts = json.load(open(d, encoding='utf-8'))
            gate = json.load(open(os.path.join(folder, 'GATE.json'), encoding='utf-8')) if os.path.exists(os.path.join(folder, 'GATE.json')) else {}
            al = json.load(open(os.path.join(folder, 'aliases.json'))) if os.path.exists(os.path.join(folder, 'aliases.json')) else {}
            for k, v in json.load(open(res[0], encoding='utf-8')).items():
                text = drafts.get(k) or drafts.get(al.get(k, ''))
                head, ai, win = result_headline(v)
                if text is None or head is None:
                    continue
                h = hashlib.sha256(text.encode('utf-8')).hexdigest()
                if h in seen:
                    continue
                seen.add(h)
                kind = (gate.get(k) or gate.get(al.get(k, '')) or {}).get('kind')
                rows.append({'batch': batch, 'key': k, 'kind': kind, 'text': text, 'headline': head, 'ai': ai, 'windows': win,
                             'pass': head == PASS, 'mine': (calls.get(batch) or {}).get(k), 'folder': os.path.relpath(folder, root)})
    return rows


# --- logistic regression, by hand (plain JSON model, no pickle) --------------------------------------------------------

def fit(X, y, l2=1.0, iters=400, lr=0.5):
    n, d = len(X), len(X[0])
    mu = [sum(r[j] for r in X) / n for j in range(d)]
    sc = [math.sqrt(sum((r[j] - mu[j]) ** 2 for r in X) / n) or 1.0 for j in range(d)]
    Z = [[(r[j] - mu[j]) / sc[j] for j in range(d)] for r in X]
    w, b = [0.0] * d, 0.0
    for _ in range(iters):
        gw, gb = [0.0] * d, 0.0
        for z, t in zip(Z, y):
            p = 1 / (1 + math.exp(-max(-30, min(30, b + sum(wi * zi for wi, zi in zip(w, z))))))
            e = p - t
            gb += e
            for j in range(d):
                gw[j] += e * z[j]
        b -= lr * gb / n
        for j in range(d):
            w[j] -= lr * (gw[j] / n + l2 * w[j] / n)
    return {'mu': mu, 'sc': sc, 'w': w, 'b': b}


def prob(model, x):
    z = [(x[j] - model['mu'][j]) / model['sc'][j] for j in range(len(x))]
    s = model['b'] + sum(wi * zi for wi, zi in zip(model['w'], z))
    return 1 / (1 + math.exp(-max(-30, min(30, s))))


def matrix(rows, names):
    return [[features(r['text'], r['kind'])[k] for k in names] for r in rows]


def evaluate(rows, folds=5):
    names = sorted(features('x').keys())
    out = {}
    for part, sel in (('paragraphs', lambda r: r['kind'] != 'section'), ('sections', lambda r: r['kind'] == 'section')):
        data = [r for r in rows if sel(r)]
        batches = sorted({r['batch'] for r in data})
        fold_of = {b: i % folds for i, b in enumerate(batches)}
        X = matrix(data, names)
        y = [1.0 if r['pass'] else 0.0 for r in data]
        pred = [None] * len(data)
        for f in range(folds):
            tr = [i for i, r in enumerate(data) if fold_of[r['batch']] != f]
            te = [i for i, r in enumerate(data) if fold_of[r['batch']] == f]
            if not tr or not te:
                continue
            m = fit([X[i] for i in tr], [y[i] for i in tr])
            for i in te:
                pred[i] = prob(m, X[i])
        ok = [i for i in range(len(data)) if pred[i] is not None]
        acc = sum(1 for i in ok if (pred[i] >= 0.5) == (y[i] == 1.0)) / len(ok)
        mine = [i for i in ok if data[i]['mine'] in ('Human', 'AI')]
        out[part] = {
            'texts': len(data), 'pass_rate': sum(y) / len(y),
            'model_accuracy': round(acc, 3),
            'always_ai_accuracy': round(1 - sum(y) / len(y), 3), 'always_human_accuracy': round(sum(y) / len(y), 3),
            'with_my_call': len(mine),
            'my_accuracy_on_those': round(sum(1 for i in mine if (data[i]['mine'] == 'Human') == (y[i] == 1.0)) / len(mine), 3) if mine else None,
            'model_accuracy_on_those': round(sum(1 for i in mine if (pred[i] >= 0.5) == (y[i] == 1.0)) / len(mine), 3) if mine else None,
            'both_wrong': sum(1 for i in mine if (data[i]['mine'] == 'Human') != (y[i] == 1.0) and (pred[i] >= 0.5) != (y[i] == 1.0)),
            'by_kind': {k: {'n': sum(1 for i in ok if data[i]['kind'] == k),
                            'pass_rate': round(sum(y[i] for i in ok if data[i]['kind'] == k) / max(1, sum(1 for i in ok if data[i]['kind'] == k)), 3),
                            'model_accuracy': round(sum(1 for i in ok if data[i]['kind'] == k and (pred[i] >= 0.5) == (y[i] == 1.0)) /
                                                    max(1, sum(1 for i in ok if data[i]['kind'] == k)), 3)}
                        for k in KINDS if any(data[i]['kind'] == k for i in ok)},
        }
        m = fit(X, y)
        out[part]['weights'] = sorted(((round(wj, 3), nm) for wj, nm in zip(m['w'], names)), key=lambda t: -abs(t[0]))[:14]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('collect'); c.add_argument('roots', nargs='+'); c.add_argument('--out', required=True)
    e = sub.add_parser('evaluate'); e.add_argument('data'); e.add_argument('--report')
    t = sub.add_parser('train'); t.add_argument('data'); t.add_argument('--model', required=True)
    p = sub.add_parser('predict'); p.add_argument('model'); p.add_argument('drafts'); p.add_argument('--gate')
    a = ap.parse_args()
    if a.cmd == 'collect':
        rows = collect(a.roots)
        json.dump(rows, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False)
        print(len(rows), 'checked texts;', Counter(r['kind'] for r in rows), '; pass rate', round(sum(r['pass'] for r in rows) / len(rows), 3))
    elif a.cmd == 'evaluate':
        rep = evaluate(json.load(open(a.data, encoding='utf-8')))
        if a.report:
            json.dump(rep, open(a.report, 'w', encoding='utf-8'), indent=1)
        print(json.dumps(rep, indent=1))
    elif a.cmd == 'train':
        rows = json.load(open(a.data, encoding='utf-8'))
        names = sorted(features('x').keys())
        model = {'format': 'pangram-predictor-v1', 'features': names, 'parts': {}}
        for part, sel in (('paragraphs', lambda r: r['kind'] != 'section'), ('sections', lambda r: r['kind'] == 'section')):
            data = [r for r in rows if sel(r)]
            model['parts'][part] = fit(matrix(data, names), [1.0 if r['pass'] else 0.0 for r in data])
            model['parts'][part]['texts'] = len(data)
        json.dump(model, open(a.model, 'w', encoding='utf-8'), indent=1)
        print('model written:', a.model)
    else:
        model = json.load(open(a.model, encoding='utf-8'))
        drafts = json.load(open(a.drafts, encoding='utf-8'))
        gate = json.load(open(a.gate, encoding='utf-8')) if a.gate else {}
        names = model['features']
        for k, text in drafts.items():
            kind = (gate.get(k) or {}).get('kind')
            part = model['parts']['sections' if kind == 'section' else 'paragraphs']
            f = features(text, kind)
            x = [f[n] for n in names]
            pr = prob(part, x)
            push = sorted(((part['w'][j] * (x[j] - part['mu'][j]) / part['sc'][j], names[j]) for j in range(len(names))), key=lambda t: t[0])
            lo = ', '.join('%s' % n for v, n in push[:3] if v < 0)
            hi = ', '.join('%s' % n for v, n in push[-3:][::-1] if v > 0)
            print('%-28s P(Human Written) %.2f  -> %s | for Human: %s | for AI: %s' % (k, pr, 'Human' if pr >= 0.5 else 'AI', hi, lo))


if __name__ == '__main__':
    main()
