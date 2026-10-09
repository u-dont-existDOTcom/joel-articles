#!/usr/bin/env python3
"""find_tells.py - look for AI tells in the Pangram-labeled calibration paragraphs, without the owner's list.

Joel, 2026-10-07 15:44: "i'm surprised it looks like all the ai tells you have are the ones i told you
specfically. you haven't found any yourself?" This is the check to run after each batch of Pangram results
(E144). It reads the single-paragraph PASS_*/FAIL_* files in calibration/ and writes, to OUT:
  rows.json             each paragraph with its label and family
  features.tsv          surface features, failing vs passing drafts of the same paragraph (sign test)
  candidates.tsv        candidate tells: family-weighted rates with a bootstrap interval, and a
                        permutation test inside families that have both a pass and a fail
  last_sentence.tsv     close fail-to-pass pairs where the passing draft dropped the failing one's last sentence
  pairs.json            every close fail-to-pass pair, with what was cut and what was added
A family is the drafts of one paragraph (linked by shared word runs), so a paragraph tried ten times
counts once. Inside a family the topic is held fixed; across families it isn't.

Usage: python3 tools/humanization/find_tells.py OUT [--perms 400]
"""
import argparse, collections, difflib, glob, json, math, os, random, re, sys
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tells_lint as TL  # noqa: E402

CAL = os.path.join(HERE, 'calibration')
W = re.compile(r"[A-Za-z']+")


def words(s):
    return W.findall(s)


def load():
    rows = []
    for f in sorted(glob.glob(CAL + '/*.txt')):
        b = os.path.basename(f)
        if b.endswith('.owner.txt') or not (b.startswith('PASS') or b.startswith('FAIL')):
            continue
        t = open(f, encoding='utf-8').read().strip()
        ps = [p for p in re.split(r'\n\s*\n', t) if p.strip()]
        if len(ps) != 1:
            continue
        m = re.search(r'_(\d+)pct', b)
        rows.append(dict(file=b, label=b[:4], pct=int(m.group(1)) if m else None, text=re.sub(r'\s+', ' ', ps[0]).strip()))
    return rows


def families(rows):
    n = len(rows); par = list(range(n))

    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i
    sh = []
    for r in rows:
        w = [x.lower() for x in words(r['text'])]
        sh.append({tuple(w[i:i + 3]) for i in range(len(w) - 2)})
    cw = [collections.Counter(TL.content(r['text'])) for r in rows]
    for i in range(n):
        for j in range(i + 1, n):
            if len(sh[i] & sh[j]) / max(1, len(sh[i] | sh[j])) >= 0.12:
                par[find(i)] = find(j); continue
            A, B = cw[i], cw[j]
            num = sum(A[k] * B[k] for k in A)
            den = math.sqrt(sum(v * v for v in A.values())) * math.sqrt(sum(v * v for v in B.values()))
            if den and num / den >= 0.55:
                par[find(i)] = find(j)
    groups = collections.defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    for k, idx in enumerate(sorted(groups.values(), key=len, reverse=True)):
        for i in idx:
            rows[i]['fam'] = k
    return rows


def feats(t):
    ss = TL.sentences(t); w = words(t); n = max(1, len(w))
    sl = [len(words(s)) for s in ss] or [0]
    first = [(words(s)[0].lower() if words(s) else '') for s in ss]

    def share(names):
        return sum(1 for x in first if x in names) / max(1, len(ss))

    def per100(rx):
        return 100 * len(re.findall(rx, t, re.I)) / n
    mean = sum(sl) / len(sl); sd = (sum((x - mean) ** 2 for x in sl) / len(sl)) ** 0.5
    return dict(
        words=len(w), sentences=len(ss), sent_len_mean=mean, sent_len_cv=sd / mean if mean else 0,
        last_sent_len=sl[-1], open_if_when=share({'if', 'when', 'whenever', 'once', 'until', 'unless'}),
        open_and_but_so=share({'and', 'but', 'so', 'or', 'then', 'still', 'yet'}),
        open_i=share({'i', "i'd", "i'm", "i've", "i'll", 'my'}), open_you=share({'you', 'your', "you're", "you'd", "you'll"}),
        questions=t.count('?'), exclaims=t.count('!'), parens=t.count('('), colons=t.count(':'),
        commas_per_sent=t.count(',') / max(1, len(ss)), contractions_100=per100(r"\b\w+'(s|t|re|ll|d|ve|m)\b"),
        first_person_100=per100(r"\b(i|me|my|i'd|i'm|i've|i'll|myself)\b"), you_100=per100(r"\byou(r|'re|'ll|'d|'ve|rself)?\b"),
        hedge_100=per100(r"\b(maybe|might|perhaps|probably|kind of|sort of|i think|i guess|seems?)\b"),
        that_100=per100(r"\bthat\b"), would_100=per100(r"\bwould\b|'d\b"), neg_100=per100(r"\b(not|never|no|nothing|nobody)\b|n't\b"),
        avg_word_len=sum(len(x) for x in w) / n, triads=sum(len(TL.triads(s)) for s in ss),
        coach_100=sum(len(re.findall(r, t, re.I)) for r in TL.COACH) * 100 / n,
    )


def sign_p(k, n):
    if n == 0:
        return 1.0
    return min(1.0, 2 * sum(comb(n, i) for i in range(0, min(k, n - k) + 1)) / 2 ** n)


def sent_open(ws):
    return r"(?:^|[.!?][\"”)]?\s+)(?:%s)\b" % '|'.join(ws)


CANDIDATES = {
    'even': (r"\beven\b", re.I),
    'actually': (r"\bactually\b", re.I),
    'colon inside a sentence': (r"[a-z][^.?!:]{8,}:\s", re.I),
    'colon not followed by a quote': (r"[a-z)][^.?!:\"“]{8,}:\s+(?![\"“'‘])\S", re.I),
    '"the way you\'d" simile': (r"\bthe way (you|you'd|someone|a|an|people)\b", re.I),
    'proof / prove': (r"\bproofs?\b|\bproves?\b|\bproving\b", re.I),
    '"still counts" / "counts as"': (r"\b(still|that|it|this|which) counts\b|\bcounts as\b|\bcounts too\b", re.I),
    'corrective negation (isn\'t, doesn\'t mean)': (r"\b(isn't|aren't|wasn't|doesn't (mean|make|prove)|don't (mean|make)|isn't automatically)\b", re.I),
    '"Say you…" opener': (sent_open(['Say']), 0),
    '"Or" sentence opener': (sent_open(['Or']), 0),
    '"Even" sentence opener': (sent_open(['Even']), 0),
    'you might think/wonder/feel/find': (r"\byou might (think|wonder|feel|find|notice|realize)\b", re.I),
    'question': (r"\?", 0),
    'parenthesis': (r"\(", 0),
    'exclamation': (r"!", 0),
    "I'd": (r"\bI'd\b", 0),
    'honestly': (r"\bhonestly\b", re.I),
    'list of three (linter)': ('triad', 0),
    'last sentence opens That/This/It/So/Which': ('last', 0),
}


def has(name, t):
    rx, fl = CANDIDATES[name]
    if rx == 'triad':
        return any(TL.triads(s) for s in TL.sentences(t))
    if rx == 'last':
        ss = TL.sentences(t)
        return bool(ss) and bool(re.match(r"(That|This|It|So|Which|And that)\b", ss[-1]))
    return bool(re.search(rx, t, fl))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('out'); ap.add_argument('--perms', type=int, default=400)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rows = families(load())
    fam = collections.defaultdict(list)
    for r in rows:
        r['f'] = feats(r['text']); r['h'] = {k: has(k, r['text']) for k in CANDIDATES}
        fam[r['fam']].append(r)
    mixed = [v for v in fam.values() if {x['label'] for x in v} == {'PASS', 'FAIL'}]
    nf = sum(r['label'] == 'FAIL' for r in rows); np_ = len(rows) - nf
    print('%d paragraphs (%d failed, %d passed) in %d families; %d families have both' % (len(rows), nf, np_, len(fam), len(mixed)))
    json.dump([{k: r[k] for k in ('file', 'label', 'pct', 'fam', 'text')} for r in rows], open(a.out + '/rows.json', 'w'), indent=1)

    with open(a.out + '/features.tsv', 'w') as fh:
        fh.write('feature\tfamilies_higher_in_FAIL\tfamilies_higher_in_PASS\tsign_p\tFAIL_mean\tPASS_mean\n')
        res = []
        for k in rows[0]['f']:
            d = []
            for v in mixed:
                fa = [x['f'][k] for x in v if x['label'] == 'FAIL']; pa = [x['f'][k] for x in v if x['label'] == 'PASS']
                d.append(sum(fa) / len(fa) - sum(pa) / len(pa))
            up = sum(x > 1e-9 for x in d); dn = sum(x < -1e-9 for x in d)
            fm = sum(r['f'][k] for r in rows if r['label'] == 'FAIL') / nf; pm = sum(r['f'][k] for r in rows if r['label'] == 'PASS') / np_
            res.append((sign_p(up, up + dn), k, up, dn, fm, pm))
        for p, k, up, dn, fm, pm in sorted(res):
            fh.write('%s\t%d\t%d\t%.3f\t%.3f\t%.3f\n' % (k, up, dn, p, fm, pm))

    random.seed(7)
    allf = list(fam.values())

    def wrate(name, lab, fams):
        vals = [sum(x['h'][name] for x in v if x['label'] == lab) / sum(1 for x in v if x['label'] == lab)
                for v in fams if any(x['label'] == lab for x in v)]
        return sum(vals) / len(vals) if vals else 0

    def within(name, labs):
        d = []
        for v, ls in zip(mixed, labs):
            f = [x['h'][name] for x, l in zip(v, ls) if l == 'FAIL']; p = [x['h'][name] for x, l in zip(v, ls) if l == 'PASS']
            d.append(sum(f) / len(f) - sum(p) / len(p))
        return sum(d) / len(d)
    base = [[x['label'] for x in v] for v in mixed]
    with open(a.out + '/candidates.tsv', 'w') as fh:
        fh.write('candidate\tFAIL_paragraphs\tPASS_paragraphs\tFAIL_family_rate\tPASS_family_rate\tdiff_95pct_low\tdiff_95pct_high\twithin_family_diff\twithin_family_p\n')
        out = []
        for name in CANDIDATES:
            bs = []
            for _ in range(400):
                s = [random.choice(allf) for _ in allf]
                bs.append(wrate(name, 'FAIL', s) - wrate(name, 'PASS', s))
            bs.sort()
            obs = within(name, base)
            ge = sum(abs(within(name, [random.sample(c, len(c)) for c in base])) >= abs(obs) - 1e-12 for _ in range(a.perms))
            out.append((name, sum(r['h'][name] for r in rows if r['label'] == 'FAIL'), sum(r['h'][name] for r in rows if r['label'] == 'PASS'),
                        wrate(name, 'FAIL', allf), wrate(name, 'PASS', allf), bs[10], bs[389], obs, (ge + 1) / (a.perms + 1)))
        for x in sorted(out, key=lambda x: -(x[3] - x[4])):
            fh.write('%s\t%d\t%d\t%.3f\t%.3f\t%+.3f\t%+.3f\t%+.3f\t%.3f\n' % x)

    def sim(x, y):
        return difflib.SequenceMatcher(None, x.split(), y.split(), autojunk=False).ratio()
    pairs, last = [], []
    for v in mixed:
        pl = [x for x in v if x['label'] == 'PASS']
        for f in (x for x in v if x['label'] == 'FAIL'):
            best = max(pl, key=lambda b: sim(f['text'], b['text']))
            r_ = sim(f['text'], best['text'])
            if r_ < 0.5:
                continue
            aw, bw = f['text'].split(), best['text'].split()
            ops = difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_opcodes()
            pairs.append(dict(fail=f['file'], passed=best['file'], ratio=round(r_, 2),
                              cut=[' '.join(aw[i1:i2]) for op, i1, i2, j1, j2 in ops if op in ('delete', 'replace')],
                              added=[' '.join(bw[j1:j2]) for op, i1, i2, j1, j2 in ops if op in ('insert', 'replace')]))
            if r_ >= 0.6:
                A, B = TL.sentences(f['text']), TL.sentences(best['text'])
                if A and max((sim(A[-1], t) for t in B), default=0) < 0.5:
                    last.append((f['file'], best['file'], A[-1]))
    json.dump(pairs, open(a.out + '/pairs.json', 'w'), indent=1)
    close = sum(p['ratio'] >= 0.6 for p in pairs)
    with open(a.out + '/last_sentence.tsv', 'w') as fh:
        fh.write('# %d of %d close pairs (similarity >= 0.6): the passing draft dropped the failing one\'s last sentence\n' % (len(last), close))
        fh.write('fail\tpass\tdropped last sentence\n')
        for x in last:
            fh.write('%s\t%s\t%s\n' % x)
    print('close pairs %d; last sentence dropped in %d' % (close, len(last)))


if __name__ == '__main__':
    main()
