"""Batch 482: the windows the recheck of 2026-10-29 read below High, sorted by whose words they are, and Emulate's bundle.

Joel, 2026-10-29 17:21 UTC, on question 25: "we never publish nonsense because it passes pangram. we come back and we try
again if clarity loses on pangram." (gate E291); and 2026-10-26 12:43 UTC: "fix any segments that are not high confidence
human if you can" (gate E278). The windows are ../recheck/read/CONFIDENCE.json (window_confidence.py): every AI one, every
Low one of 5 words or more, every Medium one of 10 words or more. Each flagged sentence is sorted:
- his own words (his messages and answers, every version he gave of a paragraph: the comparison gate's owner texts, and
  his inner child guide, articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md): never sent to Emulate; the span goes
  to him (docs/EMULATE-FALLBACK.md section 2);
- the hypnosis audit he kept as a list (his answer 2c): left, as in every recheck since B2;
- everything else (the fixes of 28 October he approved, wording he approved on earlier pages, the rest of the rewrite):
  Emulate first (E235, E237), its paragraph with the one before it where it is short (Emulate refuses under 40 words),
  adjacent targets of one section in one item. Only the flagged sentences come back from a sample, and only where it
  keeps their meaning and form; then the comparative read beside his published text (E284, E288) before any card.

  python3 articles/inner-signal/humanize/fix-20261029/b482/make_bundle.py   (from the repo root)
Writes BUNDLE.json (the items, plain text), BUNDLE-RECORD.json (each item's paragraphs and windows) and SORTED.json
(every flagged sentence and where it went).
"""
import hashlib
import json
import pathlib
import re
import sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
import window_confidence as wc  # noqa: E402

MASTER = H / 'HUMANIZED-SO-FAR.md'
CONF = B.parent / 'recheck' / 'read' / 'CONFIDENCE.json'
IC_GUIDE = ROOT / 'articles' / 'inner-child-therapy' / 'HUMANIZED-ARTICLE-SO-FAR.md'
AUDIT_FIRST = 'Before accepting a recording or live suggestion, ask:'


def wanted(x):
    return x['label'] == 'AI' or (x['confidence'] == 'Low' and x['words'] >= 5) or \
        (x['confidence'] == 'Medium' and x['words'] >= 10)


def main():
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    conf = json.loads(CONF.read_text(encoding='utf-8'))
    gate = json.loads((H / 'COMPARE-GATE.json').read_text(encoding='utf-8'))
    # his texts, with the one obvious typo fixed when HG-S15 went in ("can are" -> "are")
    mine = [m.replace('all of these can are separate', 'all of these are separate') for m in cr.owner_paragraphs(gate['owner'], ROOT)]
    ic = [cr.loose(b['text']) for b in sr.blocks(IC_GUIDE.read_text(encoding='utf-8')) if not b['level']]
    # their sentences, so that a sentence of his with a few words cut or a typo fixed is still his (IC-A2's "That's one
    # grown-up doing three jobs" is his inner child guide's sentence with its middle cut, batch 479's S1)
    split = lambda t: [s for s in re.split(r'(?<=[.!?])\s+', t) if len(s.split()) >= 4]
    his_s = [s for m in mine for s in split(m)]
    ic_s = [s for m in ic for s in split(m)]

    def near(lt, pool):
        import difflib
        return any(difflib.SequenceMatcher(a=lt, b=s, autojunk=False).ratio() >= 0.85 for s in pool
                   if abs(len(s) - len(lt)) <= 0.6 * max(len(s), len(lt)))
    paras = [(b['i'], wc.norm(b['text'])) for b in bl if not b['level']]
    audit = next(b['i'] for b in bl if b['text'].startswith(AUDIT_FIRST))
    audit_end = audit
    while audit_end + 1 < len(bl) and not bl[audit_end + 1]['level']:
        audit_end += 1
    sorted_, tg = [], {}
    for name in ('RESULT-A.json', 'RESULT-B.json'):
        for x in conf[name]['rows']:
            if not wanted(x):
                continue
            for s in x['sentences']:
                ns = wc.norm(s['text'])
                i = next((i for i, pt in paras if ns and ns in pt), None)
                lt = cr.loose(s['text'])
                if i is None:
                    fate = 'not placed (a heading, or text across two paragraphs)'
                elif audit <= i <= audit_end:
                    fate = 'left: the hypnosis audit he kept as a list (2c)'
                elif lt and (cr.is_his(lt, mine) or (len(lt.split()) >= 4 and near(lt, his_s))):
                    fate = 'his own words: to him'
                elif lt and (any(lt in p for p in ic) or (len(lt.split()) >= 4 and near(lt, ic_s))):
                    fate = 'his inner child guide: to him'
                else:
                    fate = 'Emulate'
                    tg.setdefault(i, [])
                    if x not in tg[i]:
                        tg[i].append(x)
                sorted_.append({'part': name[7], 'window': x['window'], 'reading': '%s (%s)' % (x['label'], x['confidence']),
                                'words': x['words'], 'block': i, 'where': sr.where(bl, i) if i is not None else None,
                                'sentence': s['text'], 'fate': fate})
    head = {}
    for b in bl:
        head[b['i']] = b['i'] if b['level'] else head.get(b['i'] - 1)
    ranges = []
    for i in sorted(tg):
        a = z = i
        words = len(bl[i]['text'].split())
        while words < 40 and a - 1 >= 0 and not bl[a - 1]['level']:
            a -= 1
            words += len(bl[a]['text'].split())
        while words < 40 and z + 1 < len(bl) and not bl[z + 1]['level']:
            z += 1
            words += len(bl[z]['text'].split())
        while words < 40 and a - 1 >= 0:
            a -= 1
            words += len(bl[a]['text'].split())
        if ranges and a <= ranges[-1][1] + 1 and head[i] == head[ranges[-1][1]]:
            ranges[-1][1] = max(ranges[-1][1], z)
        else:
            ranges.append([a, z])
    bundle, rec = {}, {'master_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(), 'items': {}}
    for a, z in ranges:
        sec = bl[head[z]]['text'] if head[z] is not None else 'the opening'
        key = 'HG-' + re.sub(r'[^A-Za-z0-9]+', '-', sec)[:28].strip('-') + '-%d' % a
        text = '\n\n'.join(bl[j]['text'] for j in range(a, z + 1))
        n = len(text.split())
        assert 40 <= n <= 3000, (key, n)
        bundle[key] = text
        rec['items'][key] = {'paragraphs': [sr.where(bl, j) for j in range(a, z + 1)], 'blocks': list(range(a, z + 1)),
                             'targets': [sr.where(bl, j) for j in range(a, z + 1) if j in tg], 'words': n,
                             'windows': sorted({'%s %s %s %d words' % (x['label'], x['confidence'], x['window'], x['words'])
                                                for j in range(a, z + 1) for x in tg.get(j, [])})}
    out = json.dumps(bundle, ensure_ascii=False, indent=1) + '\n'
    (B / 'BUNDLE.json').write_text(out, encoding='utf-8')
    rec['bundle_sha256'] = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec['words'] = sum(v['words'] for v in rec['items'].values())
    (B / 'BUNDLE-RECORD.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'SORTED.json').write_text(json.dumps(sorted_, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    from collections import Counter
    print(Counter(s['fate'] for s in sorted_))
    for k, v in rec['items'].items():
        print('%-40s %4d words  %s' % (k, v['words'], v['targets']))
    print(len(bundle), 'items,', rec['words'], 'words a sample;', rec['bundle_sha256'])


if __name__ == '__main__':
    main()
