"""A fresh read of the paragraphs whose words came from my advice (2026-10-29), beside his published text.

Joel, 2026-10-29 17:21 UTC: "approve all the cards and where there's no "approve" option just take the advice given".
The four cards in his own words had no Approve button; taking my advice put my wording into five paragraphs (C-59's
wording also stands in Working with your guards, P6, and two of the paragraphs carry an approved fix as well). New words
get a read beside his published version before they stay (gate E288), like the fixes did on 28 October.

  python3 articles/inner-signal/humanize/fix-20261029/comprehension/read_advice.py make     -> verify/PAIRS-1.txt, BRIEF-1.txt
  python3 articles/inner-signal/humanize/fix-20261029/comprehension/read_advice.py collect  -> verify/VERIFY.json, READ-RECORD.json

The paragraphs read are the ones where HUMANIZED-SO-FAR.md differs from fix-20261028/comprehension/CANDIDATE.md (the
guide with every fix approved, whose fixed paragraphs the 28 October readers checked). verify/READ-RECORD.json is one of
the records COMPARE-GATE.json reads (its glob fix-2026*/comprehension/verify/READ-RECORD.json).
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
import suggestion_review as sr  # noqa: E402

C28 = H / 'fix-20261028' / 'comprehension'
OUT = HERE / 'verify'


def load():
    now = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    cand = sr.blocks((C28 / 'CANDIDATE.md').read_text(encoding='utf-8'))
    base = sr.blocks((C28 / 'BASE-ANSWERS.md').read_text(encoding='utf-8'))
    assert len(now) == len(cand)
    changed = [i for i in range(len(now)) if now[i]['text'] != cand[i]['text']]
    return now, cand, base, changed


def make():
    now, cand, base, changed = load()
    pub = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
    F = {r['id']: r for r in json.loads((C28 / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']}
    review = json.loads((C28 / 'REVIEW-28.json').read_text(encoding='utf-8'))
    decisions = json.loads((H / 'fix-20261029' / 'DECISIONS-20261029.json').read_text(encoding='utf-8'))
    cards = {}   # BASE block -> findings of every card on it, and of a card whose answer also goes there
    for s in review['suggestions']:
        cards.setdefault(s['spans'][0]['block'], []).extend(s.get('findings', []))
    for x in decisions['items']:
        for al in x.get('also', []):
            s = [s for s in review['suggestions'] if s['id'] == x['id']][0]
            cards.setdefault(al['block'], []).extend(s.get('findings', []))
    # the lists split on 28 October come after every paragraph read here, so CANDIDATE and BASE indices agree
    assert all(i < 649 for i in changed), changed
    brief = (C28 / 'verify' / 'BRIEF-1.txt').read_text(encoding='utf-8')
    brief = brief.replace('Each paragraph below\nhas been fixed.', 'Each paragraph below\nhas been changed.')
    lines = []
    for i in changed:
        pubs = sorted({j for f in cards.get(i, []) for j in F[f]['pub_blocks']})
        lines += ['=' * 70, 'P%d (%s)' % (i, sr.where(now, i)), '',
                  'PUBLISHED:', '\n\n'.join(pub[j]['text'] for j in pubs) or '(none)', '',
                  'BEFORE:', base[i]['text'], '', 'AFTER:', now[i]['text'], '']
    OUT.mkdir(parents=True, exist_ok=True)
    pairs = OUT / 'PAIRS-1.txt'
    pairs.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    # the 28 October brief names its own files by absolute path (written in another checkout): point it at these
    brief, n1 = re.subn(r'`[^`]*/verify/VERIFY-1\.md`', '`%s`' % (OUT / 'VERIFY-1.md'), brief)
    brief, n2 = re.subn(r'`[^`]*/verify/PAIRS-1\.txt`', '`%s`' % pairs, brief)
    assert n1 == 1 and n2 == 1, (n1, n2)
    (OUT / 'BRIEF-1.txt').write_text(brief, encoding='utf-8')
    (OUT / 'VERIFY-PARTS.json').write_text(json.dumps([{'reader': 1, 'paragraphs': changed,
                                                        'after': [now[i]['text'] for i in changed]}], indent=1) + '\n',
                                           encoding='utf-8')
    print(len(changed), 'paragraphs for one reader:', changed)


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
    res, after = {}, {}
    for m in meta:
        got = parse((OUT / ('VERIFY-%d.md' % m['reader'])).read_text(encoding='utf-8'))
        for i, t in zip(m['paragraphs'], m['after']):
            res[i] = got.get(i, {'clear': '', 'says': '', 'better': '', 'problem': 'not answered'})
            after[i] = t
    fails = {i: r for i, r in res.items()
             if not (r['clear'].lower().startswith('yes') and r['says'].lower().startswith('yes')
                     and r['better'].lower().split()[0:1] in (['yes'], ['same']))}
    (OUT / 'VERIFY.json').write_text(json.dumps({'read': len(res), 'failed': fails, 'results': res},
                                                ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    findings = [{'id': 'V%d' % i, 'severity': 2,
                 'kind': 'unclear' if not r['clear'].lower().startswith('yes') else
                 'lost' if not r['says'].lower().startswith('yes') else 'vaguer',
                 'block_hashes': [cr.phash(after[i])], 'now': r['problem']} for i, r in sorted(fails.items())]
    dfile = OUT / 'DISPOSITIONS.json'
    disp = json.loads(dfile.read_text(encoding='utf-8')) if dfile.exists() else {}
    cr.record(OUT, findings=findings, coverage=[cr.phash(t) for t in after.values()], dispositions=disp,
              article='HUMANIZED-SO-FAR.md after Joel\'s answers of 2026-10-29 (the paragraphs with my advised wording)')
    print('%d paragraphs read, %d failed' % (len(res), len(fails)))
    for i, r in sorted(fails.items()):
        print('  P%d  clear %s, says %s, better %s: %s' % (i, r['clear'], r['says'], r['better'], r['problem']))


if __name__ == '__main__':
    {'make': make, 'collect': collect}[sys.argv[1]]()
