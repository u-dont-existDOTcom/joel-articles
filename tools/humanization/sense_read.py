#!/usr/bin/env python3
"""sense_read.py - the word-for-sense read: fresh readers each read one part of an article and ask, of every content
word, whether it is the word a careful writer meant; and the read itself is tested with planted errors of the same kind.

Joel, 2026-11-03 13:46 UTC, on his hypnosis guide: "the tag questions part above says "oily" instead of old. do we have
more nonsense in here? how are you not catching this?" "Oily" is a real word in a grammatical sentence, so the spell
checks, the AI-text detector and the "whose words is this" checks all passed it (lesson E331 in
docs/HUMANIZATION-GATE.md). Only a reader who asks "is this the word meant?" of each word catches it, and a reader's
silence means nothing unless the reader is shown to catch such errors. So the master is cut into parts, each part gets a
few planted errors ("deceptive" for "receptive", "ointment" for "appointment"), the list of them is kept where readers
can't see it, every reader must list every block it read, and the recall on the planted errors says how far the
reader's other findings, and its silence, can be trusted. The first version was made by hand for one article
(articles/inner-signal/humanize/fix-20261103/nonsense/); this is the general tool.

  python3 tools/humanization/sense_read.py make MASTER.md OUTDIR [--parts N] [--plant K] [--seed S] [--style STYLE.md] [--pairs PAIRS.json]
  python3 tools/humanization/sense_read.py score OUTDIR
  python3 tools/humanization/sense_read.py nonwords MASTER.md [--known FILE ...] [--out FILE]

`make` splits the master's blocks (suggestion_review.blocks: headings are blocks too, numbered with the rest) into --parts
contiguous parts of about equal word counts (default: one per ~10,000 words, at least one), cutting just before a heading
when one is near the ideal cut. OUTDIR/parts/PART-k.md has one line per block, "[i] " plus the text (headings keep their
# marks), the two blocks before and after as context the reader must not report on. --plant errors per part (default 3,
spread through the part, never in a heading, never twice in one block) are made by swapping a whole word for its
confusable (built-in pairs, or --pairs, a JSON list of [a, b]), keeping the first letter's case; --seed makes the choice
repeatable. Written next to parts/, never in it: CANARIES.json (the planted errors), BRIEF.md (sense_read_brief.md with
--style, the article's own "what is not wrong here", put in), TASKS.json (the part file, the read file and the one-line
task for each fresh reader), META.json. The master is only read.

`score` reads OUTDIR/reads/READ-*.json ({"part", "read": [block numbers], "findings": [{block, text, kind, what, fix,
confidence}], "notes"}) and reports per part the blocks missing from the read list and the planted errors found (a
finding at the planted block whose text has the planted word), the overall recall, SCORE.json, and FINDINGS-RAW.json:
every finding that is not a planted error, one entry per block and text, with the readers that reported it, for the lead
session to read in place and trace. Exit 0 when every read list is complete and every planted error was found, 3 when
not (the read can't be trusted yet), 2 for a missing or malformed read.

`nonwords` lists the tokens of the master that are not dictionary words (pyspellchecker), not in the --known files, and
not names in mid-sentence, with their block numbers: the mechanical net under the read, for typos and run-together words.
"""
import argparse
import collections
import hashlib
import json
import pathlib
import random
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import suggestion_review as sr  # noqa: E402

BRIEF_TEMPLATE = HERE / 'sense_read_brief.md'
STYLE_PLACEHOLDER = '{{STYLE_NOTES}}'
GENERIC_STYLE = ("No style notes were given for this article. Treat the writer's informal voice, casual grammar, jokes, "
                 "asides, made-up words and pet names, and the technical terms of the subject as deliberate when they "
                 "are used consistently and mean what they should; a phrase that is unusual but means exactly what it "
                 "should is not wrong.")

PAIRS = [
    ('receptive', 'deceptive'), ('warmth', 'wealth'), ('remove', 'remodel'), ('listen', 'glisten'),
    ('appointment', 'ointment'), ('grounding', 'grinding'), ('stay', 'stray'), ('closed', 'cloaked'),
    ('specific', 'pacific'), ('old', 'oily'), ('calm', 'clam'), ('trust', 'thrust'), ('breath', 'breadth'),
    ('loose', 'lose'), ('affect', 'effect'), ('elicit', 'illicit'), ('discreet', 'discrete'),
    ('compliment', 'complement'), ('principle', 'principal'), ('accept', 'except'), ('peace', 'piece'),
    ('gentle', 'genteel'), ('quiet', 'quite'), ('advice', 'advise'), ('then', 'than'),
    ('adapt', 'adopt'), ('council', 'counsel'), ('device', 'devise'), ('whether', 'weather'),
]
# Not farther/further or ensure/insure: many writers use either, so a swap there may be no error at all, and a planted
# error that isn't one would count against the readers' recall.

# a whole word: not part of a longer word, not joined by a hyphen or an apostrophe
TOKEN = re.compile(r"(?<![\w'’-])[A-Za-z]+(?![\w'’-])")
URL = re.compile(r"(?:https?://|www\.)\S+|\]\([^)]*\)")
SENT_END = re.compile(r'(?<=[.!?])["”’)\]]*\s+')


def line(b):
    return '[%d] %s%s' % (b['i'], ('#' * b['level'] + ' ') if b['level'] else '', b['text'])


def words(b):
    return len(b['text'].split())


# ---- splitting -------------------------------------------------------------------------------------------------

def cut_points(bl, n):
    """Start indexes (into bl) of the n parts: the cut nearest each ideal word count, moved to a heading if one is within
    15% of a part's size of it."""
    n = max(1, min(n, len(bl)))
    cum = [0]
    for b in bl:
        cum.append(cum[-1] + words(b))
    total = cum[-1]
    size = total / n
    starts = [0]
    for k in range(1, n):
        ideal = total * k / n
        lo, hi = starts[-1] + 1, len(bl) - (n - k)    # leave a block for each later part
        cand = range(lo, hi + 1)
        best = min(cand, key=lambda c: (abs(cum[c] - ideal), c))
        heads = [c for c in cand if bl[c]['level'] and abs(cum[c] - ideal) <= 0.15 * size]
        if heads:
            best = min(heads, key=lambda c: (abs(cum[c] - ideal), c))
        starts.append(best)
    return starts


# ---- planting --------------------------------------------------------------------------------------------------

def pair_map(pairs):
    m = collections.defaultdict(list)
    for a, b in pairs:
        a, b = a.lower(), b.lower()
        if a != b:
            m[a].append(b)
            m[b].append(a)
    return m


def matches(text, pmap):
    """Every (start, end, word, replacement) in text where a whole word has a confusable partner, outside URLs."""
    skip = [m.span() for m in URL.finditer(text)]
    out = []
    for m in TOKEN.finditer(text):
        s, e = m.span()
        if any(a <= s < b for a, b in skip):
            continue
        w = m.group(0)
        for other in pmap.get(w.lower(), []):
            if w.isupper() and len(w) > 1:
                rep = other.upper()
            elif w[0].isupper():
                rep = other[0].upper() + other[1:]
            else:
                rep = other
            out.append((s, e, w, rep))
    return out


def sentence_around(text, s, e):
    """The sentence of text holding the span s..e."""
    start = 0
    for m in SENT_END.finditer(text):
        if m.start() >= e:
            return text[start:m.start()].strip()
        start = m.end()
    return text[start:].strip()


def plant(bl, start, end, k, pmap, rng, taken):
    """k planted errors in blocks start..end-1 of bl: [(block index, s, e, original, planted)], spread by position.
    The pair is chosen before the place, so a very common pair (then/than) doesn't crowd out the rest, and a pair is
    used twice in a part only when no other is left."""
    cands = []      # (block, match, pair key)
    for i in range(start, end):
        b = bl[i]
        if b['level'] or i in taken:
            continue
        for m in matches(b['text'], pmap):
            cands.append((i, m, frozenset((m[2].lower(), m[3].lower()))))
    chosen, used = [], set()

    def pick(pool):
        fresh = [c for c in pool if c[2] not in used] or pool
        keys = sorted({tuple(sorted(c[2])) for c in fresh})
        key = frozenset(rng.choice(keys))
        c = rng.choice([c for c in fresh if c[2] == key])
        chosen.append(c)
        used.add(c[2])

    span = end - start
    for j in range(k):
        lo, hi = start + span * j // k, start + span * (j + 1) // k
        pool = [c for c in cands if lo <= c[0] < hi and all(c[0] != x[0] for x in chosen)]
        if pool:
            pick(pool)
    while len(chosen) < k:
        pool = [c for c in cands if all(c[0] != x[0] for x in chosen)]
        if not pool:
            break
        if chosen:
            far = max(min(abs(c[0] - x[0]) for x in chosen) for c in pool)
            pool = [c for c in pool if min(abs(c[0] - x[0]) for x in chosen) == far]
        pick(pool)
    return [(c[0],) + tuple(c[1]) for c in sorted(chosen, key=lambda c: c[0])]


# ---- make ------------------------------------------------------------------------------------------------------

def make(master, outdir, parts=None, plant_k=3, seed=None, style=None, pairs=None):
    master = pathlib.Path(master)
    raw = master.read_bytes()
    md = raw.decode('utf-8')
    bl = sr.blocks(md)
    for n, b in enumerate(bl):
        assert b['i'] == n, 'block numbers are not 0..n-1'
    total = sum(words(b) for b in bl)
    n = parts if parts else max(1, round(total / 10000))
    starts = cut_points(bl, n)
    ends = starts[1:] + [len(bl)]
    if seed is None:
        seed = random.SystemRandom().randrange(1, 10 ** 6)
    rng = random.Random(seed)
    pl = [tuple(p) for p in json.loads(pathlib.Path(pairs).read_text(encoding='utf-8'))] if pairs else PAIRS
    pmap = pair_map(pl)

    texts = {b['i']: b['text'] for b in bl}
    canaries, taken = [], set()
    for k, (s, e) in enumerate(zip(starts, ends), 1):
        for i, a, z, w, rep in plant(bl, s, e, plant_k, pmap, rng, taken):
            old = texts[i]
            new = old[:a] + rep + old[z:]
            canaries.append({'part': k, 'block': i, 'original': w, 'planted': rep,
                             'sentence': sentence_around(new, a, a + len(rep))})
            texts[i] = new
            taken.add(i)
        got = sum(1 for c in canaries if c['part'] == k)
        if got < plant_k:
            print('part %d: only %d of %d errors could be planted (too few blocks with a pair word)' % (k, got, plant_k),
                  file=sys.stderr)

    out = pathlib.Path(outdir)
    (out / 'parts').mkdir(parents=True, exist_ok=True)
    (out / 'reads').mkdir(parents=True, exist_ok=True)

    def ln(b):
        return line(dict(b, text=texts[b['i']]))

    tasks = []
    for k, (s, e) in enumerate(zip(starts, ends), 1):
        body = ['# Part %d of the article: blocks %d to %d' % (k, s, e - 1), '']
        if s:
            body += ["## Context before this part (read it, don't report on it)", ''] + [ln(b) for b in bl[max(0, s - 2):s]] + ['']
        body += ['## The part to read', ''] + [ln(b) for b in bl[s:e]] + ['']
        if e < len(bl):
            body += ["## Context after this part (read it, don't report on it)", ''] + [ln(b) for b in bl[e:e + 2]] + ['']
        pf = out / 'parts' / ('PART-%d.md' % k)
        pf.write_text('\n\n'.join(x for x in body if x) + '\n', encoding='utf-8')
        rf = out / 'reads' / ('READ-%d.json' % k)
        task = 'Read %s, then %s, and write %s as the brief says.' % (out / 'BRIEF.md', pf, rf)
        tasks.append({'part': k, 'blocks': [s, e - 1], 'words': sum(words(b) for b in bl[s:e]),
                      'part_file': str(pf), 'read_file': str(rf), 'task': task})

    (out / 'CANARIES.json').write_text(json.dumps(canaries, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'TASKS.json').write_text(json.dumps(tasks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    style_text = pathlib.Path(style).read_text(encoding='utf-8').strip() if style else GENERIC_STYLE
    brief = BRIEF_TEMPLATE.read_text(encoding='utf-8')
    assert STYLE_PLACEHOLDER in brief, 'the brief template has no %s' % STYLE_PLACEHOLDER
    (out / 'BRIEF.md').write_text(brief.replace(STYLE_PLACEHOLDER, style_text), encoding='utf-8')
    (out / 'META.json').write_text(json.dumps({
        'master': str(master), 'master_sha256': hashlib.sha256(raw).hexdigest(), 'seed': seed, 'plant_per_part': plant_k,
        'parts': len(tasks), 'blocks': len(bl), 'words': total, 'pairs': 'built-in' if not pairs else str(pairs)},
        indent=1) + '\n', encoding='utf-8')
    return tasks, canaries, seed


# ---- score -----------------------------------------------------------------------------------------------------

class Malformed(Exception):
    pass


def load_read(path):
    try:
        d = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as ex:
        raise Malformed('%s: not readable JSON (%s)' % (path.name, ex))
    if not isinstance(d, dict):
        raise Malformed('%s: not a JSON object' % path.name)
    rd, fs = d.get('read'), d.get('findings')
    if not isinstance(rd, list) or not isinstance(fs, list):
        raise Malformed('%s: "read" and "findings" must both be lists' % path.name)
    try:
        read = {int(x) for x in rd}
    except (TypeError, ValueError):
        raise Malformed('%s: "read" must be a list of block numbers' % path.name)
    finds = []
    for f in fs:
        if not isinstance(f, dict) or not isinstance(f.get('text'), str):
            raise Malformed('%s: every finding needs a "text"' % path.name)
        try:
            blk = int(f.get('block'))
        except (TypeError, ValueError):
            raise Malformed('%s: every finding needs a numeric "block"' % path.name)
        finds.append(dict(f, block=blk))
    return read, finds


def ranges(nums):
    out, nums = [], sorted(nums)
    for n in nums:
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return out


def score(outdir):
    out = pathlib.Path(outdir)
    try:
        tasks = json.loads((out / 'TASKS.json').read_text(encoding='utf-8'))
        canaries = json.loads((out / 'CANARIES.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as ex:
        raise Malformed('%s: TASKS.json or CANARIES.json missing or unreadable (%s)' % (out, ex))
    rows, raw, planted_hit = [], collections.OrderedDict(), set()
    for t in tasks:
        k = t['part']
        rp = out / 'reads' / ('READ-%d.json' % k)
        if not rp.exists():
            raise Malformed('%s is missing' % rp)
        read, finds = load_read(rp)
        expected = set(range(t['blocks'][0], t['blocks'][1] + 1))
        mine = [c for c in canaries if c['part'] == k]
        found, used = [], set()
        for c in mine:
            hit = [n for n, f in enumerate(finds) if f['block'] == c['block'] and c['planted'].lower() in f['text'].lower()]
            if hit:
                found.append(c['block'])
                used.update(hit)
        for n, f in enumerate(finds):
            if n in used:
                continue
            key = (f['block'], ' '.join(f['text'].lower().split()))
            e = raw.setdefault(key, {'block': f['block'], 'text': f['text'], 'kind': f.get('kind'), 'what': f.get('what'),
                                     'fix': f.get('fix'), 'confidence': f.get('confidence'), 'readers': [], 'reports': []})
            if k not in e['readers']:
                e['readers'].append(k)
            e['reports'].append({'reader': k, 'kind': f.get('kind'), 'what': f.get('what'), 'fix': f.get('fix'),
                                 'confidence': f.get('confidence')})
        missing = sorted(expected - read)
        rows.append({'part': k, 'blocks': t['blocks'], 'expected': len(expected), 'read': len(expected & read),
                     'missing': missing, 'missing_ranges': ranges(missing), 'outside': sorted(read - expected),
                     'planted': len(mine), 'found': len(found),
                     'missed': [{'block': c['block'], 'planted': c['planted'], 'original': c['original']}
                                for c in mine if c['block'] not in found],
                     'findings': len(finds)})
    planted, found = sum(r['planted'] for r in rows), sum(r['found'] for r in rows)
    ok = all(not r['missing'] for r in rows) and found == planted
    res = {'parts': rows, 'planted': planted, 'found': found, 'recall': (found / planted) if planted else None,
           'reads_complete': all(not r['missing'] for r in rows), 'trusted': ok}
    (out / 'SCORE.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'FINDINGS-RAW.json').write_text(json.dumps(sorted(raw.values(), key=lambda e: (e['block'], e['text'])),
                                                      ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return res, len(raw)


def print_score(res, nraw):
    print('part  blocks      read      planted found  findings')
    for r in res['parts']:
        print('%-5d %-11s %3d/%-5d %7d %5d  %8d' % (r['part'], '%d-%d' % tuple(r['blocks']), r['read'], r['expected'],
                                                    r['planted'], r['found'], r['findings']))
        if r['missing']:
            print('      NOT READ: blocks %s' % ', '.join(str(a) if a == b else '%d-%d' % (a, b) for a, b in r['missing_ranges']))
        for m in r['missed']:
            print('      MISSED: block %d "%s" (was "%s")' % (m['block'], m['planted'], m['original']))
    rec = 'n/a (nothing planted)' if res['recall'] is None else '%d/%d = %.0f%%' % (res['found'], res['planted'], 100 * res['recall'])
    print('recall: %s; %d findings other than the planted ones (FINDINGS-RAW.json)' % (rec, nraw))
    print('verdict: %s' % ('read complete and every planted error found' if res['trusted']
                           else "the read can't be trusted yet"))


# ---- nonwords --------------------------------------------------------------------------------------------------

WORD = re.compile(r"[A-Za-z][A-Za-z'’]*[A-Za-z]|[A-Za-z]")


def nonwords(master, known_files=(), out=None):
    try:
        from spellchecker import SpellChecker
    except ImportError:
        print('pyspellchecker is not installed (pip install pyspellchecker); no non-word list made.')
        return None
    bl = sr.blocks(pathlib.Path(master).read_text(encoding='utf-8'))
    known = set()
    for f in known_files:
        known |= {w.replace('’', "'").lower() for w in WORD.findall(pathlib.Path(f).read_text(encoding='utf-8'))}
    sp = SpellChecker()
    hits = collections.defaultdict(list)
    for b in bl:
        t = b['text']
        for m in WORD.finditer(t):
            w = m.group(0).replace('’', "'")
            lw = w.lower().strip("'")
            if len(lw) < 3 or lw in known:
                continue
            base = re.sub(r"'(s|t|re|ve|ll|d|m)$", '', lw)
            if sp.known([lw]) or sp.known([base]):
                continue
            before = t[:m.start()].rstrip()
            if w[0].isupper() and not w.isupper() and before and before[-1] not in '.!?:;"“‘(':
                continue   # a name in mid-sentence
            hits[lw].append(b['i'])
    res = [{'word': w, 'blocks': sorted(set(v)), 'where': [sr.where(bl, i) for i in sorted(set(v))][:3],
            'suggest': sorted(sp.candidates(w) or [])[:5]} for w, v in sorted(hits.items())]
    if out:
        pathlib.Path(out).write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for x in res:
        print(x['word'], x['blocks'][:6], x['suggest'])
    print(len(res), 'non-words')
    return res


# ---- cli -------------------------------------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('master')
    m.add_argument('outdir')
    m.add_argument('--parts', type=int)
    m.add_argument('--plant', type=int, default=3)
    m.add_argument('--seed', type=int)
    m.add_argument('--style')
    m.add_argument('--pairs')
    s = sub.add_parser('score')
    s.add_argument('outdir')
    n = sub.add_parser('nonwords')
    n.add_argument('master')
    n.add_argument('--known', nargs='*', default=[])
    n.add_argument('--out')
    a = ap.parse_args(argv)
    if a.cmd == 'make':
        tasks, canaries, seed = make(a.master, a.outdir, a.parts, a.plant, a.seed, a.style, a.pairs)
        for t in tasks:
            print('part %d: blocks %d-%d, %d words, %d planted' % (
                t['part'], t['blocks'][0], t['blocks'][1], t['words'], sum(1 for c in canaries if c['part'] == t['part'])))
        print('seed %s' % seed)
        for t in tasks:
            print(t['task'])
        return 0
    if a.cmd == 'score':
        try:
            res, nraw = score(a.outdir)
        except Malformed as ex:
            print('malformed or missing read: %s' % ex, file=sys.stderr)
            return 2
        print_score(res, nraw)
        return 0 if res['trusted'] else 3
    nonwords(a.master, a.known, a.out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
