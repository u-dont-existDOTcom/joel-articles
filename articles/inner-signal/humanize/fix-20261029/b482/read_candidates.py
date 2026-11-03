"""The comparative read of batch 482's candidates (gate E284, E288): each paragraph a candidate changes, beside his published
version and the paragraph as it stands, read by a fresh reader before it becomes a card or goes into the recheck.

  python3 articles/inner-signal/humanize/fix-20261029/b482/read_candidates.py make     -> read/PAIRS-<k>.txt, read/BRIEF-<k>.txt
  python3 articles/inner-signal/humanize/fix-20261029/b482/read_candidates.py collect  -> read/VERIFY.json, read/READ-RECORD.json

A paragraph passes when its reader says CLEAR yes, SAYS yes and BETTER yes or same. read/READ-RECORD.json is one of the
records COMPARE-GATE.json reads (fix-2026*/*/read/READ-RECORD.json), so a candidate he approves is read at its words.
"""
import json
import pathlib
import re
import sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

OUT = B / 'read'
C28 = H / 'fix-20261028' / 'comprehension'
PER = 10
import difflib  # noqa: E402
import suggestion_review as sr  # noqa: E402
PUB = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))


def published_for(stretch):
    """The published paragraph holding the run of 1 to 4 sentences closest to STRETCH, when it is close (0.6 or more).
    TARGETS.json's two published paragraphs are the ones most like the whole paragraph, which can miss the very sentence
    a candidate changes (P68's "Self-hypnosis simply has one advantage ..." is in the published paragraph before)."""
    best, r = None, 0.6
    for b in PUB:
        ss = [s for s in re.split(r'(?<=[.!?”"])\s+', b['text']) if s]
        for a in range(len(ss)):
            for k in range(1, 5):
                if a + k <= len(ss):
                    x = difflib.SequenceMatcher(a=stretch.lower(), b=' '.join(ss[a:a + k]).lower(), autojunk=False).ratio()
                    if x > r:
                        best, r = b['text'], x
    return best


def make():
    cands = json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots']
    targets = {t['id']: t for t in json.loads((B / 'TARGETS.json').read_text(encoding='utf-8'))['items']}
    by_block = {}
    for s in cands:
        if s['pick'] == 'none':
            continue
        b = by_block.setdefault(s['block'], {'ids': [], 'before': s['paragraph_before'], 'after': s['paragraph_after'],
                                             'where': s['where'], 'published': []})
        b['ids'].append(s['id'])
        b['after'] = s['paragraph_after']   # the last spot's after holds every spot of the paragraph
        own = published_for(s['old'])
        for p in ([own] if own else []) + targets[s['id']]['published']:
            if p not in b['published']:
                b['published'].append(p)
    brief = (C28 / 'verify' / 'BRIEF-1.txt').read_text(encoding='utf-8')
    brief = brief.replace('Each paragraph below\nhas been fixed.', 'Each paragraph below\nhas been changed.')
    blocks = sorted(by_block)
    OUT.mkdir(exist_ok=True)
    meta = []
    for k in range(0, len(blocks), PER):
        n = k // PER + 1
        lines = []
        for i in blocks[k:k + PER]:
            b = by_block[i]
            lines += ['=' * 70, 'P%d (%s)' % (i, b['where']), '',
                      'PUBLISHED (the meaning reference; it may cover more than this paragraph):',
                      '\n\n'.join(b['published']) or '(none)', '', 'BEFORE:', b['before'], '', 'AFTER:', b['after'], '']
        pairs = OUT / ('PAIRS-%d.txt' % n)
        pairs.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        br, n1 = re.subn(r'`[^`]*/verify/VERIFY-1\.md`', '`%s`' % (OUT / ('VERIFY-%d.md' % n)), brief)
        br, n2 = re.subn(r'`[^`]*/verify/PAIRS-1\.txt`', '`%s`' % pairs, br)
        assert n1 == 1 and n2 == 1
        (OUT / ('BRIEF-%d.txt' % n)).write_text(br, encoding='utf-8')
        meta.append({'reader': n, 'paragraphs': blocks[k:k + PER], 'after': [by_block[i]['after'] for i in blocks[k:k + PER]],
                     'ids': [by_block[i]['ids'] for i in blocks[k:k + PER]]})
    (OUT / 'VERIFY-PARTS.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(blocks), 'paragraphs for', len(meta), 'readers')


def parse(raw):
    out = {}
    for m in re.finditer(r'^## P(\d+)\s*\n(.*?)(?=^## P\d+|^DONE:|\Z)', raw, re.M | re.S):
        rec = {}
        for k in ('CLEAR', 'SAYS', 'BETTER', 'PROBLEM'):
            mm = re.search(r'^%s:\s*(.*)$' % k, m.group(2), re.M)
            rec[k.lower()] = mm.group(1).strip() if mm else ''
        out[int(m.group(1))] = rec
    return out


def collect():
    meta = json.loads((OUT / 'VERIFY-PARTS.json').read_text(encoding='utf-8'))
    res, after, missing = {}, {}, []
    for m in meta:
        f = OUT / ('VERIFY-%d.md' % m['reader'])
        if not f.exists():
            missing.append(m['reader'])
            continue
        got = parse(f.read_text(encoding='utf-8'))
        for i, t in zip(m['paragraphs'], m['after']):
            res[i] = got.get(i, {'clear': '', 'says': '', 'better': '', 'problem': 'not answered'})
            after[i] = t
    fails = {i: r for i, r in res.items()
             if not (r['clear'].lower().startswith('yes') and r['says'].lower().startswith('yes')
                     and r['better'].lower().split()[0:1] in (['yes'], ['same']))}
    (OUT / 'VERIFY.json').write_text(json.dumps({'readers_missing': missing, 'read': len(res), 'failed': fails,
                                                 'results': res}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    findings = [{'id': 'B%d' % i, 'severity': 2,
                 'kind': 'unclear' if not r['clear'].lower().startswith('yes') else
                 'lost' if not r['says'].lower().startswith('yes') else 'vaguer',
                 'block_hashes': [cr.phash(after[i])], 'now': r['problem']} for i, r in sorted(fails.items())]
    dfile = OUT / 'DISPOSITIONS.json'
    disp = json.loads(dfile.read_text(encoding='utf-8')) if dfile.exists() else {}
    cr.record(OUT, findings=findings, coverage=[cr.phash(t) for t in after.values()], dispositions=disp,
              article='batch 482\'s CANDIDATE-MASTER.md (the paragraphs its candidates change)')
    print('%d paragraphs read, %d failed%s' % (len(res), len(fails), ('; readers missing: %s' % missing) if missing else ''))
    for i, r in sorted(fails.items()):
        print('  P%d  clear %s, says %s, better %s: %s' % (i, r['clear'], r['says'], r['better'], r['problem']))


if __name__ == '__main__':
    {'make': make, 'collect': collect}[sys.argv[1]]()
