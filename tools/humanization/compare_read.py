#!/usr/bin/env python3
"""compare_read.py - the comparative comprehension read: a rewrite of Joel's text read beside his own version, part by
part and sentence by sentence, by fresh readers who write down every place the rewrite is harder to understand than what
he wrote.

Joel, 2026-10-28 15:20 UTC, on the hypnosis guide after Emulate's rewrites: "the guide itself is now too
incomprehensible, we went wrong somewhere", and on a card: "didn't you already do a comprehension check? the AI guide was
making more sense by far". The clarity read (`docs/CLARITY-READ.md`) reads an article on its own and readers flag what
stands out; it had passed "As associated with the Silva Mind Control method:" (his "A line associated with the Silva Mind
Control tradition says it plainly:") and a list of four nouns with no verb that had been his "Conscious agreement is one
thing. Unconscious receptivity is another. ..." This read gives each reader both versions of the same part and asks for
every place the rewrite reads worse: garbled, unclear, lost (a point, step, condition or contrast gone) or vaguer. It is
the read after any rewrite of his text, by Emulate or anyone (gate E284).

  python3 tools/humanization/compare_read.py make REWRITE.md ORIGINAL.md DIR [--words 1300] [--about "..."]
  python3 tools/humanization/compare_read.py collect DIR [--git-path REPO_RELATIVE_REWRITE_PATH] [--owner FILE ...]
  python3 tools/humanization/compare_read.py record DIR                    -> DIR/READ-RECORD.json
  python3 tools/humanization/compare_read.py gate --config COMPARE-GATE.json

`make` splits both versions at the h1 and h2 headings they share (a heading only the rewrite has goes with the shared
heading before it) into parts of about --words words of the rewrite (1,300 by default: six of the hypnosis guide's
eleven first readers, given about 2,500 words each, ran out of room before writing anything), and writes PART-k.txt (ORIGINAL then REWRITE),
BRIEF-k.txt for each part, and PARTS.json. The reader is the lead session's model itself (Opus), reading every part
beside his: never a cheaper model (gate E294; Joel, 2026-10-30: "is it because you are using dumb readers? not reading it
yourself?", "looks like you need to read everything again yourself (not sonnet)"; the Sonnet reads of 29 October
had passed "in waking life" for "to waking life" and "the verb" for "one central verb"). A cheaper model may only lay
out the pairs. Each part's findings go in READER-k.md.

`collect` reads every READER-k.md into FINDINGS.json: each finding's quote found in the rewrite (its block and paragraph
number, as the marking page numbers them) and in the original; "same_as_original" when the flagged words are word for
word his (they aren't a regression, and don't count); "owner_words" when they are in his own texts (--owner: his messages,
his answers files; those are his to rewrite, never a writer's); and, with --git-path, the first commit of the rewrite whose
text has them (when the spot came in). Check every finding yourself against the whole article before acting on it: a
reader sees one part, and a point it calls lost may be elsewhere.

`record` writes READ-RECORD.json: the paragraphs the readers read (each by a hash of its words, so any later change to a
paragraph makes it unread again), every finding with the paragraph it is in, and DIR/DISPOSITIONS.json, what became of
each finding ({"F3.2": ["fixed" | "his" | "not" | "kept" | "done", "why", my severity if lower]}). "his" is his call
(his own words, or a fix waiting on his marking page); "kept" never covers a garbled or unclear sentence a reader rated 2
or 3 unless my check put it at 1, on record (gate E285). A lane's own read (a check of fixed paragraphs, say) can write a
record of the same form.

`gate` is the check that makes the read binding (gate E284, Joel 2026-10-28 16:05 UTC: "let's repair the process durably
so that can't happen again also"). With a lane's COMPARE-GATE.json ({"article", "original", "records": [...], "owner":
[globs of his texts: messages, answers files]}), every paragraph of the article must be his as published, his own words
(a version he gave, word for word), or read beside his text in a record at its present words; and every finding of
severity 2 or 3 whose words are still in the article needs a fate with a reason (a "fixed" finding whose words are still
there is open). tools/humanization/lane_push.py runs it before every push of an article that has a COMPARE-GATE.json and
stops on a failure, unless --unread-ok "reason" is given, which goes into the commit message.
"""
import argparse
import collections
import difflib
import glob
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import suggestion_review as sr  # noqa: E402

FIELDS = ('NOW', 'PUBLISHED', 'KIND', 'SEVERITY', 'WHY')
KINDS = ('garbled', 'unclear', 'lost', 'vaguer')

BRIEF = '''You are checking part of __ABOUT__ for comprehension. You get the same part in two versions:
- PUBLISHED: the text as Joel published it (clear);
- NOW: a rewrite of it, which was meant to keep every point and stay clear.

Your job: find EVERY place where NOW is harder for a reader to understand than PUBLISHED, or doesn't make sense on its
own. Go through NOW paragraph by paragraph and sentence by sentence; don't skim. Content may have moved between sections
or been added; judge NOW as a reader would read it, and use PUBLISHED as the reference for what it should say.

Flag a sentence (or a few together) when it is one of these:
- garbled: ungrammatical, a fragment standing as a sentence, a word that doesn't fit, a sentence that doesn't parse, a
  list with no verb that doesn't say what it's for (for example "Apples, pears, plums. Can fruit be bought?" where the
  published text said "Apples are one thing. Pears are another." and the point was that they differ);
- unclear: a reader would have to reread it, or guess what it means or what "it", "this" or "that" refers to;
- lost: NOW drops or changes a point, a step, a condition or a contrast that PUBLISHED made, so the passage no longer says
  it (for example "one thing ... another" becoming a plain list loses the point that the things differ);
- vaguer: NOW says the same thing less exactly, in a way a reader would notice (a concrete step becomes general, a
  strong rule becomes a hint, or the reverse).

Don't flag: a plainer, more casual or more personal wording that is just as clear; a heading change; a change of order; a
typo that doesn't hide the meaning; new material in NOW that is clear. Don't rewrite anything.

Write your findings with a single Write call to `__OUT__`, in exactly this form, one block per finding, in NOW's order:

## F__K__.1
NOW: <the exact sentence(s) from NOW, copied character for character>
PUBLISHED: <the matching sentence(s) from PUBLISHED, copied exactly, or "none">
KIND: garbled | unclear | lost | vaguer
SEVERITY: 3 (a reader won't get it, or it now says something else) | 2 (most readers would stumble) | 1 (a small snag)
WHY: <one sentence>

(number them F__K__.1, F__K__.2, ...). After the last block add a line "TOTAL: n". Read only the file below, don't run
commands, don't use the web. Reply with only the TOTAL line.

The part to check is in `__PART__`.
'''


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


def phash(text):
    """A paragraph's words as a short hash (quote marks, dashes and case aside): the same words, the same hash."""
    return hashlib.sha256(loose(text).encode('utf-8')).hexdigest()[:16]


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


def _find(ps, norms, lo=False):
    if not ps:
        return 0.0, []
    hits, idx = 0.0, []
    for p in ps:
        js = [j for j, t in enumerate(norms) if p in t]
        if not js:
            ss = [loose(x) for x in sentences(p)] if lo else sentences(p)
            found = [x for x in ([j for j, t in enumerate(norms) if s in t] for s in ss) if x]
            if ss and found:
                hits += len(found) / len(ss) - 1
                js = sorted({x[0] for x in found})
        if js:
            hits += 1
            idx += [j for j in js if j not in idx]
    return round(hits / len(ps), 2), idx


def find_blocks(text, bl):
    """(share of the quote found, [block indices]) for a quote: exact (as normalized) first, then letters and digits."""
    norms = [norm(b['text']) for b in bl]
    share, idx = _find(pieces(text), norms)
    if share < 1:
        share2, idx2 = _find([loose(p) for p in pieces(text)], [loose(t) for t in norms], lo=True)
        if share2 > share:
            share, idx = share2, idx2
    return share, [bl[j]['i'] for j in idx]


def sections(bl):
    """[(heading text or None, [block indices])], split at h1 and h2 headings."""
    out, cur = [], [None, []]
    for b in bl:
        if b['level'] and b['level'] <= 2:
            out.append(tuple(cur))
            cur = [b['text'], [b['i']]]
        else:
            cur[1].append(b['i'])
    out.append(tuple(cur))
    return [s for s in out if s[1]]


def text_of(bl, idx):
    """The part as the page shows it: headings with their #, and a list item with its number or bullet, a quote with its
    >, since a reader given the bare text reads "Let your attention come back..." as a countdown with no 5 (lesson E290)."""
    lines = []
    for i in idx:
        b = bl[i]
        if b['level']:
            lines.append('#' * b['level'] + ' ' + b['text'])
        elif b['text'].strip():
            lead = {'oli': b.get('marker', '') + ' ', 'li': '- ', 'quote': '> '}.get(b['kind'], '')
            lines.append(lead.lstrip() and lead + b['text'] or b['text'])
    return '\n\n'.join(lines)


def words(bl, idx):
    return sum(len(bl[i]['text'].split()) for i in idx if not bl[i]['level'])


def parts(rew, orig, target):
    """[{'rew': [rewrite block indices], 'orig': [original block indices], 'first', 'last'}] in the rewrite's order."""
    sr_, so = sections(rew), sections(orig)
    sm = difflib.SequenceMatcher(a=[s[0] for s in so], b=[s[0] for s in sr_], autojunk=False)
    match = {}
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            match[blk.b + k] = blk.a + k
    chunks, cur, last = [], {'rew': [], 'orig': set()}, 0
    for j in range(len(sr_)):
        last = match.get(j, last)
        cur['orig'].add(last)
        cur['rew'].append(j)
        if sum(words(rew, sr_[x][1]) for x in cur['rew']) >= target:
            chunks.append(cur)
            cur = {'rew': [], 'orig': set()}
    if cur['rew']:
        chunks.append(cur)
    out = []
    for c in chunks:
        out.append({'rew': [i for j in c['rew'] for i in sr_[j][1]],
                    'orig': [i for j in sorted(c['orig']) for i in so[j][1]],
                    'first': sr_[c['rew'][0]][0], 'last': sr_[c['rew'][-1]][0]})
    return out


def make(rewrite, original, outdir, target=1300, about='a long guide by Joel, a Substack writer'):
    rew = sr.blocks(pathlib.Path(rewrite).read_text(encoding='utf-8'))
    orig = sr.blocks(pathlib.Path(original).read_text(encoding='utf-8'))
    outdir = pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    meta = []
    for k, p in enumerate(parts(rew, orig, target), 1):
        f = outdir / ('PART-%d.txt' % k)
        f.write_text('=== PUBLISHED (as Joel published it) ===\n\n' + text_of(orig, p['orig']) +
                     '\n\n=== NOW (the rewrite to check) ===\n\n' + text_of(rew, p['rew']) + '\n', encoding='utf-8')
        (outdir / ('BRIEF-%d.txt' % k)).write_text(
            BRIEF.replace('__ABOUT__', about).replace('__OUT__', str(outdir / ('READER-%d.md' % k)))
            .replace('__K__', str(k)).replace('__PART__', str(f)), encoding='utf-8')
        meta.append({'part': k, 'rewrite_words': words(rew, p['rew']), 'original_words': words(orig, p['orig']),
                     'first': p['first'], 'last': p['last'], 'rewrite_blocks': [p['rew'][0], p['rew'][-1]],
                     'coverage': [phash(rew[i]['text']) for i in p['rew'] if not rew[i]['level']]})
    (outdir / 'PARTS.json').write_text(json.dumps({'rewrite': str(rewrite), 'original': str(original), 'parts': meta},
                                                  ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return meta


def parse_reader(raw, part):
    out = []
    for m in re.finditer(r'^## (F\d+\.\d+)[^\n]*\n(.*?)(?=^## F\d+\.\d+|^TOTAL:|\Z)', raw, re.M | re.S):
        rec = {'id': m.group(1), 'part': part}
        for i, name in enumerate(FIELDS):
            rest = '|'.join(FIELDS[:i] + FIELDS[i + 1:])
            mm = re.search(r'^%s:\s*(.*?)(?=^(?:%s):|\Z)' % (name, rest), m.group(2), re.M | re.S)
            rec[name.lower()] = mm.group(1).strip() if mm else ''
        sev = re.match(r'\d', rec['severity'])
        rec['severity'] = int(sev.group(0)) if sev else 0
        kind = re.match(r'[a-z]+', rec['kind'].lower())
        rec['kind'] = kind.group(0) if kind else ''
        out.append(rec)
    total = re.search(r'^TOTAL:\s*(\d+)', raw, re.M)
    return out, int(total.group(1)) if total else None


def history(git_path, cwd):
    """[(sha, date, subject, the rewrite's text at that commit, loosened, its paragraphs as written)], oldest first."""
    log = subprocess.run(['git', 'log', '--reverse', '--format=%H\t%cI\t%s', '--', git_path], cwd=cwd,
                         capture_output=True, text=True, check=True).stdout.splitlines()
    out = []
    for line in log:
        sha, date, subj = line.split('\t', 2)
        md = subprocess.run(['git', 'show', '%s:%s' % (sha, git_path)], cwd=cwd, capture_output=True,
                            text=True).stdout
        bl = [b['text'] for b in sr.blocks(md) if not b['level']]
        out.append((sha, date, subj, '\n'.join(loose(b['text']) for b in sr.blocks(md)), bl))
    return out


def changes(text, hist, min_overlap=0.4):
    """Every commit that changed the paragraph TEXT is in, newest first, with the sentences it dropped and added (gate
    E301: before a lost point comes back, see whether a card of his, or an earlier read, took it out). The paragraph is
    followed back through HIST (history(), oldest first) by its words: at each older commit, the paragraph sharing most
    words with the one after it, if they share at least MIN_OVERLAP of their words."""
    def wset(s):
        return set(loose(s).split())

    versions, cur = [], wset(text)
    for entry in reversed(hist):
        paras = entry[4] if len(entry) > 4 else []
        best, score = None, 0.0
        for p in paras:
            w = wset(p)
            if w and cur:
                j = len(w & cur) / len(w | cur)
                if j > score:
                    best, score = p, j
        if best is None or score < min_overlap:
            break
        versions.append((entry[0], entry[1], entry[2], best))
        cur = wset(best)
    out = []
    for newer, older in zip(versions, versions[1:]):
        if loose(newer[3]) == loose(older[3]):
            continue
        ns = {loose(s) for s in sentences(newer[3])}
        os_ = {loose(s) for s in sentences(older[3])}
        out.append({'sha': newer[0][:8], 'date': newer[1][:10], 'subject': newer[2][:140],
                    'dropped': [s for s in sentences(older[3]) if loose(s) not in ns],
                    'added': [s for s in sentences(newer[3]) if loose(s) not in os_]})
    if versions:
        first = versions[-1]
        out.append({'sha': first[0][:8], 'date': first[1][:10], 'subject': first[2][:140], 'first_seen': True,
                    'text': first[3]})
    return out


def origin(text, hist, orig_joined):
    ps = [x for x in (loose(p) for p in pieces(text)) if x]
    if not ps:
        return None
    if all(p in orig_joined for p in ps):
        return {'sha': None, 'date': None, 'subject': 'as published'}
    for sha, date, subj, joined, *_ in hist:
        if all(p in joined for p in ps):
            return {'sha': sha[:8], 'date': date[:10], 'subject': subj[:140]}
    for sha, date, subj, joined, *_ in hist:
        if sum(p in joined for p in ps) * 2 >= len(ps):
            return {'sha': sha[:8], 'date': date[:10], 'subject': subj[:140], 'partial': True}
    return None


def owner_corpus(files):
    parts_ = []
    for f in files:
        raw = pathlib.Path(f).read_text(encoding='utf-8')
        if f.endswith('.json'):
            d = json.loads(raw)
            items = d.get('items', []) if isinstance(d, dict) else d
            for x in items:
                if isinstance(x, dict):
                    parts_ += [str(x.get(k) or '') for k in ('your_version', 'comment', 'new', 'after', 'text')]
        else:
            parts_.append(raw)
    return loose('\n'.join(parts_))


def collect(outdir, git_path=None, owner=(), cwd=None):
    outdir = pathlib.Path(outdir)
    meta = json.loads((outdir / 'PARTS.json').read_text(encoding='utf-8'))
    rew = sr.blocks(pathlib.Path(meta['rewrite']).read_text(encoding='utf-8'))
    orig = sr.blocks(pathlib.Path(meta['original']).read_text(encoding='utf-8'))
    orig_joined = '\n'.join(loose(b['text']) for b in orig)
    hist = history(git_path, cwd or '.') if git_path else []
    mine = owner_corpus(owner) if owner else ''
    findings, missing, totals = [], [], {}
    for p in meta['parts']:
        f = outdir / ('READER-%d.md' % p['part'])
        if not f.exists():
            missing.append(p['part'])
            continue
        recs, total = parse_reader(f.read_text(encoding='utf-8'), p['part'])
        totals[p['part']] = {'parsed': len(recs), 'total_line': total}
        for r in recs:
            r['now_found'], r['now_blocks'] = find_blocks(r['now'], rew)
            r['where'] = [sr.where(rew, i) for i in r['now_blocks']]
            r['block_hashes'] = [phash(rew[i]['text']) for i in r['now_blocks']]
            if r['published'] and r['published'].lower() != 'none':
                r['pub_found'], r['pub_blocks'] = find_blocks(r['published'], orig)
            else:
                r['pub_found'], r['pub_blocks'] = None, []
            ps = [x for x in (loose(q) for q in pieces(r['now'])) if x]
            r['same_as_original'] = bool(ps) and all(q in orig_joined for q in ps)
            long_ = [q for q in ps if len(q) >= 20]
            r['owner_words'] = bool(mine) and bool(long_) and all(q in mine for q in long_)
            r['origin'] = origin(r['now'], hist, orig_joined) if hist else None
            if hist and r['now_blocks']:
                r['changes'] = changes(rew[r['now_blocks'][0]]['text'], hist)
            findings.append(r)
    counted = [r for r in findings if not r['same_as_original']]
    hit = collections.defaultdict(int)
    for r in counted:
        for i in r['now_blocks']:
            hit[i] = max(hit[i], r['severity'])
    paras = [b for b in rew if not b['level']]
    summary = {'readers_missing': missing, 'totals': totals, 'findings': len(counted),
               'by_severity': dict(collections.Counter(r['severity'] for r in counted)),
               'by_kind': dict(collections.Counter(r['kind'] for r in counted)),
               'same_as_original': [r['id'] for r in findings if r['same_as_original']],
               'owner_words': [r['id'] for r in counted if r['owner_words']],
               'not_found': [r['id'] for r in counted if r['now_found'] == 0],
               'paragraphs': len(paras),
               'paragraphs_hit': {s: sum(1 for v in hit.values() if v >= s) for s in (1, 2, 3)}}
    (outdir / 'FINDINGS.json').write_text(json.dumps({'summary': summary, 'findings': findings}, ensure_ascii=False,
                                                     indent=1) + '\n', encoding='utf-8')
    return summary


FATES = ('fixed', 'his', 'not', 'kept', 'done')


def record(outdir, findings=None, coverage=None, dispositions=None, article=None):
    """READ-RECORD.json for a read: what was read (paragraph hashes), its findings, and each finding's fate."""
    outdir = pathlib.Path(outdir)
    if coverage is None:
        meta = json.loads((outdir / 'PARTS.json').read_text(encoding='utf-8'))
        coverage = sorted({h for p in meta['parts'] for h in p.get('coverage', [])})
        article = article or meta.get('rewrite')
    if findings is None:
        findings = json.loads((outdir / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']
    if dispositions is None:
        f = outdir / 'DISPOSITIONS.json'
        dispositions = json.loads(f.read_text(encoding='utf-8')) if f.exists() else {}
    rec = {'format': 'compare-read-record-v1', 'article': str(article or ''), 'coverage': sorted(set(coverage)),
           'findings': [{'id': r['id'], 'severity': r.get('severity', 0), 'kind': r.get('kind', ''),
                         'block_hashes': r.get('block_hashes', []), 'now': r.get('now', '')[:300],
                         'same_as_original': bool(r.get('same_as_original'))} for r in findings],
           'dispositions': {k: (v if isinstance(v, list) else [v.get('fate'), v.get('why', '')])
                            for k, v in dispositions.items()}}
    (outdir / 'READ-RECORD.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return rec


def owner_paragraphs(globs, root):
    """His own texts, loosened: his messages whole, and every version he gave of a paragraph (an answers file's "your
    version", an edit file's "new"), whole, so a paragraph he wrote or rewrote is his whatever words it kept."""
    out = []
    for g in globs:
        for f in sorted(glob.glob(str(pathlib.Path(root) / g), recursive=True)):
            raw = pathlib.Path(f).read_text(encoding='utf-8')
            if f.endswith('.json'):
                d = json.loads(raw)
                items = d.get('items', d.get('edits', [])) if isinstance(d, dict) else d
                for x in items:
                    if isinstance(x, dict):
                        out += [loose(str(x.get(k) or '')) for k in ('your_version', 'new')]
            else:
                out.append(loose(raw))
    return [t for t in out if t]


def is_his(text, mine):
    """TEXT (loosened) is his: inside one of his texts, or one of his paragraphs with an obvious typo fixed (nearly all
    the same words, as "All of these can are separate factors" -> "All of these are separate factors")."""
    if any(text in m for m in mine):
        return True
    for m in mine:
        if abs(len(m) - len(text)) <= max(12, 0.05 * len(text)) and \
                difflib.SequenceMatcher(a=text, b=m, autojunk=False).ratio() >= 0.97:
            return True
    return False


def gate(config, root='.'):
    """[(kind, block index, where, detail)] of what the article may not have yet: paragraphs nobody read beside his text
    (UNREAD) and findings at severity 2 or 3 with no fate, or marked fixed while their words are still there (OPEN)."""
    root = pathlib.Path(root)
    cfg = json.loads(pathlib.Path(config).read_text(encoding='utf-8'))
    art = sr.blocks((root / cfg['article']).read_text(encoding='utf-8'))
    orig = sr.blocks((root / cfg['original']).read_text(encoding='utf-8'))
    orig_joined = '\n'.join(loose(b['text']) for b in orig)
    mine = owner_paragraphs(cfg.get('owner', []), root)
    recs = []
    for g in cfg.get('records', []):
        for f in sorted(glob.glob(str(root / g), recursive=True)):
            recs.append((f, json.loads(pathlib.Path(f).read_text(encoding='utf-8'))))
    covered = {h for _, r in recs for h in r.get('coverage', [])}
    present = {}
    problems = []
    for b in art:
        if b['level'] or len(b['text'].split()) < 3:
            continue
        h = phash(b['text'])
        present[h] = b['i']
        t = loose(b['text'])
        if t in orig_joined or h in covered or is_his(t, mine):
            continue
        problems.append(('UNREAD', b['i'], sr.where(art, b['i']), b['text'][:120]))
    for f, r in recs:
        disp = r.get('dispositions', {})
        for x in r.get('findings', []):
            if x.get('severity', 0) < 2 or x.get('same_as_original'):
                continue
            here = [present[h] for h in x.get('block_hashes', []) if h in present]
            if not here:
                continue   # its words are gone from the article: fixed, or rewritten (and read again or unread above)
            d = disp.get(x['id']) or [None, '']
            fate, why = d[0], (d[1] if len(d) > 1 else '')
            mine = d[2] if len(d) > 2 else None   # my own severity, when my check put it lower than the reader's
            where_ = sr.where(art, here[0])
            if fate not in FATES or (fate != 'done' and not str(why).strip()):
                problems.append(('OPEN', here[0], where_, '%s (%s) has no fate with a reason: %s'
                                 % (x['id'], pathlib.Path(f).parent.name, x.get('now', '')[:90])))
            elif fate == 'fixed':
                problems.append(('OPEN', here[0], where_, '%s is marked fixed, but its words are still there: %s'
                                 % (x['id'], x.get('now', '')[:90])))
            elif fate == 'kept' and x.get('kind') in ('garbled', 'unclear') and mine != 1:
                # a sentence a reader can't follow is never kept on my say-so (gate E285): fix it, give it to him, or
                # say why it isn't a problem; only a snag my check put at severity 1 may stay, with that on record
                problems.append(('OPEN', here[0], where_, '%s is %s and kept: fix it, give it to him, or record why it is '
                                 'only a small snag (severity 1): %s' % (x['id'], x['kind'], x.get('now', '')[:90])))
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('rewrite')
    m.add_argument('original')
    m.add_argument('dir')
    m.add_argument('--words', type=int, default=1300)
    m.add_argument('--about', default='a long guide by Joel, a Substack writer')
    c = sub.add_parser('collect')
    c.add_argument('dir')
    c.add_argument('--git-path')
    c.add_argument('--owner', nargs='*', default=[])
    r = sub.add_parser('record')
    r.add_argument('dir')
    g = sub.add_parser('gate')
    g.add_argument('--config', required=True)
    g.add_argument('--root', default='.')
    a = ap.parse_args(argv)
    if a.cmd == 'make':
        for p in make(a.rewrite, a.original, a.dir, a.words, a.about):
            print(p['part'], p['rewrite_words'], p['original_words'], '|', p['first'], '->', p['last'])
    elif a.cmd == 'collect':
        print(json.dumps(collect(a.dir, a.git_path, a.owner), ensure_ascii=False, indent=1))
    elif a.cmd == 'record':
        rec = record(a.dir)
        print('%s: %d paragraphs read, %d findings, %d with a fate' % (
            pathlib.Path(a.dir) / 'READ-RECORD.json', len(rec['coverage']), len(rec['findings']), len(rec['dispositions'])))
    else:
        probs = gate(a.config, a.root)
        kinds = collections.Counter(p[0] for p in probs)
        for p in probs[:40]:
            print('%s  P%s  %s  %s' % p)
        if len(probs) > 40:
            print('... and %d more' % (len(probs) - 40))
        print('verdict: %s (%d unread, %d open)' % ('FAIL' if probs else 'PASS', kinds['UNREAD'], kinds['OPEN']))
        return 1 if probs else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
