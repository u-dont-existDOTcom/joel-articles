"""The comprehension audit's findings gathered (2026-10-28): READER-1..11.md -> FINDINGS.json and AUDIT.md.

Each finding's NOW quote is looked up in the working copy (HUMANIZED-SO-FAR.md, read as blocks the way his pages number
them), its PUBLISHED quote in his published guide, and its words in his own texts (his messages, every version of his
that went into the guide, every "your version" and comment in his answers files). Its origin is the first commit of the
working copy whose text holds it, so the audit can say when each spot came in.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/collect.py
"""
import collections
import difflib
import json
import pathlib
import re
import subprocess
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

GUIDE = 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md'
# the guide as it was when he wrote (2026-10-28 15:20 UTC), the version every reader read: commit 0a44911d, sha256
# c38ca36f..., before his six answers of that afternoon went in
AUDITED = subprocess.run(['git', 'show', '0a44911d:articles/inner-signal/humanize/HUMANIZED-SO-FAR.md'],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
NOW = sr.blocks(AUDITED)
PUB = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
CHUNKS = json.loads((HERE / 'CHUNKS.json').read_text(encoding='utf-8'))
FIELDS = ('NOW', 'PUBLISHED', 'KIND', 'SEVERITY', 'WHY')


def norm(s):
    s = unicodedata.normalize('NFKC', s or '')
    for a, b in (('\u2019', "'"), ('\u2018', "'"), ('\u201c', '"'), ('\u201d', '"'), ('\u2014', '-'), ('\u2013', '-'),
                 ('\u00a0', ' ')):
        s = s.replace(a, b)
    s = re.sub(r'[*_`]', '', s)
    return re.sub(r'\s+', ' ', s).strip()


def loose(s):
    """Letters, digits and single spaces only, lowercased: a quote matches whatever its quote marks or dashes."""
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', norm(s).lower())).strip()


def pieces(text):
    """A quote split where a reader may have joined paragraphs or skipped words ('...')."""
    out = []
    for line in re.split(r'\n+|\s*(?:\.\.\.|…|\[\.\.\.\])\s*', text or ''):
        line = norm(line).strip(' "\'')
        if len(line) >= 8:
            out.append(line)
    return out


def sentences(text):
    return [s for s in (norm(x).strip(' "\'') for x in re.split(r'(?<=[.!?:;])\s+', text or '')) if len(s) >= 8]


def find_blocks(text, bl, norms):
    """(share of the quote found, [block indices]) for a quote in a list of blocks: exact (as normalized) first, then
    letters and digits only."""
    share, idx = _find(pieces(text), bl, norms)
    if share < 1:
        share2, idx2 = _find([loose(p) for p in pieces(text)], bl, [loose(t) for t in norms], lo=True)
        if share2 > share:
            return share2, idx2
    return share, idx


def _find(ps, bl, norms, lo=False):
    if not ps:
        return 0.0, []
    hits, idx = 0, []
    for p in ps:
        js = [j for j, t in enumerate(norms) if p in t]
        if not js:
            ss = [loose(x) for x in sentences(p)] if lo else sentences(p)
            sj = [[j for j, t in enumerate(norms) if s in t] for s in ss]
            found = [x for x in sj if x]
            if ss and len(found) == len(ss):
                js = sorted({x[0] for x in found})
            elif found:
                hits += len(found) / len(ss) - 1  # partly found
                js = sorted({x[0] for x in found})
        if js:
            hits += 1
            idx += [j for j in js if j not in idx]
    return round(hits / len(ps), 2), [bl[j]['i'] for j in idx]


def reader_files(k):
    """A part's reader files: READER-k.md, or, for a part read again in two halves (make_halves.py), READER-ka.md and
    READER-kb.md. Returns [(label, path or None)]."""
    f = HERE / ('READER-%d.md' % k)
    if f.exists() and re.search(r'^TOTAL:', f.read_text(encoding='utf-8'), re.M):
        return [(str(k), f)]
    halves = [('%d%s' % (k, t), HERE / ('READER-%d%s.md' % (k, t))) for t in 'ab']
    if any(h.exists() for _, h in halves) or (HERE / ('BRIEF-%da.txt' % k)).exists():
        return [(lab, h if h.exists() else None) for lab, h in halves]
    return [(str(k), None)]


def parse_reader(f, k):
    raw = f.read_text(encoding='utf-8')
    total = re.search(r'^TOTAL:\s*(\d+)', raw, re.M)
    out = []
    for m in re.finditer(r'^## (F\d+[ab]?\.\d+)[^\n]*\n(.*?)(?=^## F\d+[ab]?\.\d+|^TOTAL:|\Z)', raw, re.M | re.S):
        body = m.group(2)
        rec = {'id': m.group(1), 'chunk': k}
        for i, name in enumerate(FIELDS):
            rest = '|'.join(FIELDS[:i] + FIELDS[i + 1:])
            mm = re.search(r'^%s:\s*(.*?)(?=^(?:%s):|\Z)' % (name, rest), body, re.M | re.S)
            rec[name.lower()] = mm.group(1).strip() if mm else ''
        sev = re.match(r'\d', rec['severity'])
        rec['severity'] = int(sev.group(0)) if sev else 0
        rec['kind'] = (re.match(r'[a-z]+', rec['kind'].lower()) or [''])[0] if rec['kind'] else ''
        out.append(rec)
    return out, int(total.group(1)) if total else None


def _his_runs(old, new, n=3):
    """The runs of at least n words that NEW has and OLD doesn't (his words, where NEW is his version of OLD)."""
    a, b = loose(old).split(), loose(new).split()
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if tag in ('replace', 'insert') and j2 - j1 >= n:
            out.append(' '.join(b[j1:j2]))
    return out


def joel_corpus():
    """His own words, as runs of text: his messages as he wrote them, and, where he gave a version of a paragraph (his
    edits, his "your version" in an answers file), only the words his version has that the one before it didn't. A
    paragraph he pasted back with a quote mark taken out is not his writing (2026-10-28: the first count called
    "As associated with the Silva Mind Control method:" his, from his quote-mark answer of 25 Oct)."""
    parts = [p.read_text(encoding='utf-8') for p in sorted(H.rglob('joel-*-message.txt'))]
    for f in sorted(H.rglob('EDITS-joel-*.json')) + [H / 'fix-20261020' / 'EDITS41.json']:
        if not f.exists():
            continue
        d = json.loads(f.read_text(encoding='utf-8'))
        items = d if isinstance(d, list) else d.get('edits', d.get('items', []))
        for x in items:
            if isinstance(x, dict) and (f.name.startswith('EDITS-joel-') or
                                        str(x.get('source', '')).startswith(("Joel's own words", "Joel's own edit"))):
                parts += _his_runs(x.get('old') or '', x.get('new') or '')
    for f in sorted(H.rglob('ANSWERS-*.json')):
        d = json.loads(f.read_text(encoding='utf-8'))
        for x in d.get('items', []):
            if x.get('your_version'):
                parts += _his_runs(x.get('my_version') or x.get('before') or '', x['your_version'])
            if x.get('comment'):
                parts.append(x['comment'])
    return loose('\n'.join(parts))


def his_share(text, corpus):
    """The share of a quote's word triples that are in his own words."""
    t = loose(text).split()
    tri = [' '.join(t[i:i + 3]) for i in range(len(t) - 2)]
    if not tri:
        return 0.0
    return round(sum(1 for x in tri if x in corpus) / len(tri), 2)


def history():
    """[(sha, date, subject, joined normalized text of the guide at that commit)], oldest first."""
    log = subprocess.run(['git', 'log', '--reverse', '--format=%H\t%cI\t%s', '--', GUIDE], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout.splitlines()
    out = []
    for line in log:
        sha, date, subj = line.split('\t', 2)
        md = subprocess.run(['git', 'show', '%s:%s' % (sha, GUIDE)], cwd=ROOT, capture_output=True, text=True).stdout
        out.append((sha, date, subj, '\n'.join(loose(b['text']) for b in sr.blocks(md))))
    return out


def origin(text, hist, pub_joined):
    ps = [x for x in (loose(p) for p in pieces(text)) if x]
    if not ps:
        return None
    if all(p in pub_joined for p in ps):
        return {'sha': None, 'date': '2026-09-28', 'subject': 'as published'}
    for sha, date, subj, joined in hist:
        if all(p in joined for p in ps):
            return {'sha': sha[:8], 'date': date[:10], 'subject': subj[:140]}
    for sha, date, subj, joined in hist:  # a quote only partly found: the commit that holds most of it
        if sum(p in joined for p in ps) * 2 >= len(ps):
            return {'sha': sha[:8], 'date': date[:10], 'subject': subj[:140], 'partial': True}
    return None


def let_stand_quotes():
    """The quoted words of every finding the triage of 2026-10-18 let stand, with its file, so a finding today can say
    whether that spot was seen then and left."""
    out = []
    for f in sorted((H / 'fix-20261018').rglob('*.triage.json')):
        d = json.loads(f.read_text(encoding='utf-8'))
        for x in d.get('let_stand', []):
            line = x.get('finding', '')
            for q in re.findall(r'"([^"]{12,})"|“([^”]{12,})”', line):
                q = loose(q[0] or q[1])
                if len(q) >= 12:
                    out.append((q, str(f.relative_to(H)), line[:300], x.get('why', '')[:200]))
    return out


def strict_check_25oct():
    """The 25 October strict Emulate check's reader findings (fix-20261025/emulate-check/READS-ALL.json): its readers
    compared each Emulate paragraph with his and rated what they found "matters" or "small"; 20 went to him as cards."""
    f = H / 'fix-20261025' / 'emulate-check' / 'READS-ALL.json'
    out = []
    for x in json.loads(f.read_text(encoding='utf-8')):
        q = loose(x.get('new') or '')
        h = loose(x.get('his') or '')
        out.append((q, h, x))
    return out


def cuts_25oct():
    """{block: [card ids]} for the 25 October page's cuts that went in (a caveat or a repeat taken out, his answer or my
    advice he accepted): a point a reader calls lost today may be one he chose to cut."""
    rv = json.loads((H / 'fix-20261025' / 'review' / 'REVIEW.json').read_text(encoding='utf-8'))
    fates = json.loads((H / 'fix-20261025' / 'review' / 'APPLIED.json').read_text(encoding='utf-8'))['fates']
    out = collections.defaultdict(list)
    now_l = [loose(b['text']) for b in NOW]
    for s in rv['suggestions']:
        if s['type'] in ('caveat', 'repeat') and fates.get(s['id'], '').startswith(('approved', 'revised', 'accepted')):
            for e in s.get('edits', []):
                # the paragraph as the cut left it, found again in today's guide (its block number may have moved)
                after = loose(e['after'])
                best, bi = 0.0, None
                for j in range(max(0, e['block'] - 8), min(len(NOW), e['block'] + 9)):
                    r = difflib.SequenceMatcher(a=after, b=now_l[j], autojunk=False).ratio() if after else 0
                    if r > best:
                        best, bi = r, j
                if bi is not None and best >= 0.6:
                    out[bi].append(s['id'])
    return out


def where(i):
    return sr.where(NOW, i)


def bucket(o):
    if not o:
        return 'not traced'
    d = o['date']
    if o['subject'] == 'as published':
        return 'as he published it'
    if d == '2026-10-18':
        return '18 Oct (the overnight Emulate run)'
    if d <= '2026-10-23':
        return '20-23 Oct (fixes and his answers)'
    return '25-27 Oct (his answers, the guard sweep)'


def main():
    now_norm = [norm(b['text']) for b in NOW]
    pub_norm = [norm(b['text']) for b in PUB]
    pub_joined = '\n'.join(loose(t) for t in pub_norm)
    joel = joel_corpus()
    hist = history()
    ls_quotes = let_stand_quotes()
    strict = strict_check_25oct()
    cuts = cuts_25oct()
    findings, totals, missing = [], {}, []
    for c in CHUNKS:
        recs = []
        for lab, f in reader_files(c['chunk']):
            if f is None:
                missing.append(lab)
                continue
            got, total = parse_reader(f, c['chunk'])
            totals[lab] = {'parsed': len(got), 'total_line': total}
            recs += got
        for r in recs:
            share, idx = find_blocks(r['now'], NOW, now_norm)
            r['now_found'] = share
            r['now_blocks'] = idx
            r['where'] = [where(i) for i in idx]
            if r['published'] and r['published'].lower() != 'none':
                r['pub_found'], pidx = find_blocks(r['published'], PUB, pub_norm)
                r['pub_blocks'] = pidx
            else:
                r['pub_found'], r['pub_blocks'] = None, []
            ps = [x for x in (loose(p) for p in pieces(r['now'])) if x]
            r['his_share'] = his_share(r['now'], joel)
            r['his_words'] = r['his_share'] >= 0.5
            r['same_as_published'] = bool(ps) and all(p in pub_joined for p in ps)
            r['origin'] = origin(r['now'], hist, pub_joined)
            r['bucket'] = 'his own words' if r['his_words'] else bucket(r['origin'])
            nl = loose(r['now'])
            r['let_stand_18oct'] = [{'file': f, 'finding': line, 'why': why} for q, f, line, why in ls_quotes if q in nl][:3]
            npub = loose(r['published']) if r['published'].lower() != 'none' else ''
            r['cut_25oct'] = sorted({c for i in r['now_blocks'] for c in cuts.get(i, [])})
            near = lambda x: any(abs(int(x.get('block', -99)) - i) <= 2 for i in r['now_blocks'])  # noqa: E731
            r['seen_25oct'] = [{'id': x['id'], 'kind': x['kind'], 'severity': x['severity'], 'why': x['why']}
                               for q, h, x in strict if near(x) and (
                                   (len(q) >= 20 and (q in nl or (len(nl) >= 20 and nl in q)))
                                   or (not q and len(h) >= 20 and npub and (h in npub or npub in h)))][:3]
            findings.append(r)
    paras = [b for b in NOW if not b['level']]
    hit = collections.defaultdict(int)
    for r in findings:
        for i in r['now_blocks']:
            hit[i] = max(hit[i], r['severity'])
    words_hit = {s: sum(len(NOW[i]['text'].split()) for i, v in hit.items() if v >= s) for s in (1, 2, 3)}
    summary = {
        'readers_missing': missing, 'totals': totals, 'findings': len(findings),
        'by_severity': dict(collections.Counter(r['severity'] for r in findings)),
        'by_kind': dict(collections.Counter(r['kind'] for r in findings)),
        'by_bucket': dict(collections.Counter(r['bucket'] for r in findings)),
        'by_bucket_sev2plus': dict(collections.Counter(r['bucket'] for r in findings if r['severity'] >= 2)),
        'quotes_found_exactly': sum(r['now_found'] == 1 for r in findings),
        'quotes_not_found': [r['id'] for r in findings if r['now_found'] == 0],
        'same_as_published': [r['id'] for r in findings if r['same_as_published']],
        'seen_and_let_stand_18oct': [r['id'] for r in findings if r['let_stand_18oct']],
        'seen_25oct': [r['id'] for r in findings if r['seen_25oct']],
        'paragraphs': len(paras), 'words': sum(len(b['text'].split()) for b in paras),
        'paragraphs_hit': {s: sum(1 for v in hit.values() if v >= s) for s in (1, 2, 3)},
        'words_hit': words_hit,
    }
    (HERE / 'FINDINGS.json').write_text(json.dumps({'summary': summary, 'findings': findings}, ensure_ascii=False,
                                                   indent=1) + '\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
