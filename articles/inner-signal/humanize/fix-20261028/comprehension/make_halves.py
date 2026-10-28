"""Parts 2, 3, 4, 6, 8 and 10 of the comprehension audit again, each in two halves (2026-10-28).

Their first readers ran out of room: parts 8, 10 and 6 stopped at the 64,000-token limit on a reply after about 26 minutes
of reading, with nothing written, and 2, 3 and 4, at the same point, were stopped. The five parts that came back had taken
11 to 13 minutes. So each of these parts goes to two readers, about 1,250 words of the guide each, with the same brief and
one more line: work in one pass and write findings as you go.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/make_halves.py  -> CHUNK-<k>a/b.txt, BRIEF-<k>a/b.txt
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_chunks as mc  # noqa: E402

PARTS = (2, 3, 4, 6, 8, 10)
EXTRA = '''
Work in one pass: read NOW once from the top, and write each finding down as you reach it. Don't draft rewrites, and
don't weigh a borderline case at length: if you can't say in one sentence why a reader would stumble, leave it out.
'''


def main():
    meta = json.loads((HERE / 'CHUNKS.json').read_text(encoding='utf-8'))
    sp, sn = mc.sections(mc.PUB), mc.sections(mc.NOW)
    import difflib
    sm = difflib.SequenceMatcher(a=[s[0] for s in sp], b=[s[0] for s in sn], autojunk=False)
    match = {}
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            match[blk.b + k] = blk.a + k
    # which NOW sections each part holds (by its first and last block)
    out = []
    for m in meta:
        if m['chunk'] not in PARTS:
            continue
        lo, hi = m['now_blocks']
        secs = [j for j, s in enumerate(sn) if lo <= s[2][0] <= hi]
        total = sum(mc.words(mc.NOW, sn[j][2]) for j in secs)
        half, acc, cut = total / 2, 0, len(secs)
        for n, j in enumerate(secs):
            acc += mc.words(mc.NOW, sn[j][2])
            if acc >= half:
                cut = n + 1
                break
        for tag, group in (('a', secs[:cut]), ('b', secs[cut:])):
            if not group:
                continue
            pubs, last = set(), None
            for j in group:
                if j in match:
                    last = match[j]
                elif last is None:
                    last = max([match[x] for x in match if x < j] or [0])
                pubs.add(last)
            now_idx = [i for j in group for i in sn[j][2]]
            pub_idx = [i for j in sorted(pubs) for i in sp[j][2]]
            k = '%d%s' % (m['chunk'], tag)
            body = ('=== PUBLISHED (as Joel published it) ===\n\n' + mc.text_of(mc.PUB, pub_idx) +
                    '\n\n=== NOW (the rewrite to check) ===\n\n' + mc.text_of(mc.NOW, now_idx) + '\n')
            (HERE / ('CHUNK-%s.txt' % k)).write_text(body, encoding='utf-8')
            brief = (mc.BRIEF.replace('__OUT__', str(HERE / ('READER-%s.md' % k))).replace('__K__', k)
                     .replace('__CHUNK__', str(HERE / ('CHUNK-%s.txt' % k))))
            brief = brief.replace("Don't rewrite anything.\n", "Don't rewrite anything.\n" + EXTRA)
            (HERE / ('BRIEF-%s.txt' % k)).write_text(brief, encoding='utf-8')
            out.append({'half': k, 'chunk': m['chunk'], 'now_words': mc.words(mc.NOW, now_idx),
                        'pub_words': mc.words(mc.PUB, pub_idx), 'first': sn[group[0]][0], 'last': sn[group[-1]][0]})
    (HERE / 'HALVES.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for o in out:
        print(o)


if __name__ == '__main__':
    main()
