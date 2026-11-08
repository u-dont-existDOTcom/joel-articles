"""Put his answers on Neuro De-Armoring Cards, 8 November (3) (x1108c, exported 2026-11-08 15:45 UTC) into
HUMANIZED-SO-FAR.md.

- SC-97, approved: the card's text, with its link, from texts_p23.py (the same as SP97.md).
- SC-106, revise: his box holds GPT's critique of the card ("look at what gpt is saying: ..."), not a version for the
  article, so nothing of blocks 106 and 115 changes here. Each of GPT's points was checked against its source
  (SCIENCE-P23.md, "SC-106 revised"), and what holds is the new card SC-106b on x1108d (build_x1108d.py).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/apply_x1108c.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
sys.path.insert(0, str(HERE))
import texts_p23 as T  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ANS = HERE / 'ANSWERS-X1108C-20261108-1545.json'
CARD = {'SC-97': 'SP97', 'SC-106': 'SP106'}


def main(write=False):
    ans = json.loads(ANS.read_text(encoding='utf-8'))
    md = ARTICLE.read_text(encoding='utf-8')
    assert ans['article']['sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), 'article changed since his page'
    entries = {e['key']: e for e in T.T}
    lines = md.split('\n')
    done = {}
    for it in ans['items']:
        sid = it['id']
        if it['status'] == 'approved':
            e = entries[CARD[sid]]
            new = (HERE / ('%s.md' % e['key'])).read_text(encoding='utf-8').strip()
            assert it['my_version'] == T.plain(new), '%s: the card he approved is not %s.md' % (sid, e['key'])
            hits = [i for i, l in enumerate(lines) if l.startswith(e['start'])]
            if len(hits) != 1:
                sys.exit('%s: %d lines start with %r' % (sid, len(hits), e['start']))
            i = hits[0]
            done[sid] = {'status': 'approved', 'line': i + 1, 'old': lines[i], 'new': new}
            lines[i] = new
        elif it['status'] == 'revise':
            assert it['your_version'].startswith('look at what gpt is saying'), sid
            done[sid] = {'status': 'revise', 'applied': False,
                         'why': 'his box holds GPT\'s critique of the card, not text for the article; its points checked '
                                'against their sources and what holds put on SC-106b (x1108d)',
                         'his_box_sha256': hashlib.sha256(it['your_version'].encode('utf-8')).hexdigest()}
        else:
            sys.exit('%s: status %s' % (sid, it['status']))
    out = '\n'.join(lines)
    rec = {'about': 'his answers on x1108c (2026-11-08 15:45 UTC): SC-97 approved; SC-106 revise, with GPT\'s critique',
           'answers': ANS.name, 'before_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest(), 'cards': done}
    for k, v in done.items():
        print(k, v['status'], 'line %d' % v['line'] if 'line' in v else 'not applied')
    print('after', rec['after_sha256'][:8])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1108C.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
