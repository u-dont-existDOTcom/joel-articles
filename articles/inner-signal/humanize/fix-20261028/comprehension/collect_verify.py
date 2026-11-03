"""The fix check's answers (verify/VERIFY-k.md) gathered: verify/VERIFY.json, and verify/READ-RECORD.json for the
comparison gate (the AFTER text of every paragraph a reader checked, and a finding for each one that failed).

A paragraph passes when its reader says CLEAR yes, SAYS yes and BETTER yes or same. A failed one is fixed again (my
change in fix/MY-REVIEW.json, or the writer's fix dropped) and read again; its finding's fate goes in
verify/DISPOSITIONS.json.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/collect_verify.py
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

OUT = HERE / 'verify'


def parse(raw):
    out = {}
    for m in re.finditer(r'^## P(\d+)\s*\n(.*?)(?=^## P\d+|^DONE:|\Z)', raw, re.M | re.S):
        body = m.group(2)
        rec = {}
        for k in ('CLEAR', 'SAYS', 'BETTER', 'PROBLEM'):
            mm = re.search(r'^%s:\s*(.*)$' % k, body, re.M)
            rec[k.lower()] = mm.group(1).strip() if mm else ''
        out[int(m.group(1))] = rec
    return out


def after_texts():
    """{block: the AFTER text each reader read}, from the PAIRS files."""
    out = {}
    # in reader order (PAIRS-10 after PAIRS-9, not after PAIRS-1), so a paragraph read again keeps its newest AFTER
    for f in sorted(OUT.glob('PAIRS-*.txt'), key=lambda f: int(re.search(r'(\d+)$', f.stem).group(1))):
        for m in re.finditer(r'^P(\d+) \(.*?\)\n.*?^AFTER:\n(.*?)\n\n(?:=|\Z)', f.read_text(encoding='utf-8') + '\n\n=',
                             re.M | re.S):
            out[int(m.group(1))] = m.group(2).strip()
    return out


def main():
    meta = json.loads((OUT / 'VERIFY-PARTS.json').read_text(encoding='utf-8'))
    after = after_texts()
    res, missing = {}, []
    for m in meta:
        f = OUT / ('VERIFY-%d.md' % m['reader'])
        if not f.exists():
            missing.append(m['reader'])
            continue
        got = parse(f.read_text(encoding='utf-8'))
        for i in m['paragraphs']:
            res[i] = got.get(i, {'clear': '', 'says': '', 'better': '', 'problem': 'not answered'})
    fails = {i: r for i, r in res.items()
             if not (r['clear'].lower().startswith('yes') and r['says'].lower().startswith('yes')
                     and r['better'].lower().split()[0:1] in (['yes'], ['same']))}
    (OUT / 'VERIFY.json').write_text(json.dumps({'readers_missing': missing, 'read': len(res), 'failed': fails,
                                                 'results': res}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    findings = []
    for i, r in sorted(fails.items()):
        kind = 'unclear' if not r['clear'].lower().startswith('yes') else 'lost' if not r['says'].lower().startswith('yes') \
            else 'vaguer'
        findings.append({'id': 'V%d' % i, 'severity': 2, 'kind': kind,
                         'block_hashes': [cr.phash(after[i])] if i in after else [], 'now': r['problem']})
    dfile = OUT / 'DISPOSITIONS.json'
    disp = json.loads(dfile.read_text(encoding='utf-8')) if dfile.exists() else {}
    # a list given back its line breaks becomes a lead-in and one block per item when it goes in, so each line it was
    # read with counts as read too ("- " is the page's bullet, not part of the item's words)
    coverage = []
    for t in after.values():
        coverage.append(cr.phash(t))
        if '\n' in t:
            coverage += [cr.phash(re.sub(r'^-\s+', '', ln.strip())) for ln in t.split('\n') if ln.strip()]
    cr.record(OUT, findings=findings, coverage=coverage, dispositions=disp,
              article='CANDIDATE.md (the fixed paragraphs) and the two cards he approved on 2026-10-28')
    print('%d paragraphs read, %d failed%s' % (len(res), len(fails),
                                             ('; readers missing: %s' % missing) if missing else ''))
    for i, r in sorted(fails.items()):
        print('  P%d  clear %s, says %s, better %s: %s' % (i, r['clear'], r['says'], r['better'], r['problem']))


if __name__ == '__main__':
    main()
