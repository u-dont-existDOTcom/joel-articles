"""Put his answers on Neuro De-Armoring Cards, 8 November (2) (x1108b, exported 2026-11-08 11:59 UTC, sent 15:08 UTC) into
HUMANIZED-SO-FAR.md.

- Approved (SC-24, SC-52, SC-53, SC-56, SC-57): the card's text, with its links, from texts_cde.py (the same as <key>.md).
- Revised (SC-47, SC-48, SC-50): his version, read from his answers file, never retyped (UDA patterns/safety-layer-cuts.md,
  rule 3). What I fix in his words without a card (lesson bad-trips-2026-11-07e: his typos are fixed, the fixed version
  checked, and it goes in), each listed in APPLIED-X1108B.json:
  - the citation links his plain-text paste drops, put back to the sources they had on the card (Hertzberg 2000,
    VA/DoD 2023, Shimazu 2013, Whittle & Singewald 2014, "slowly" to Robison 2022, He 2005, Shao 2021);
  - SC-48: "Why don't these drugs on calcified PTSD?" to "Why don't these drugs work on calcified PTSD?" (the word his
    post had); "That's like a bit like" to "That's a bit like"; "leg.This" to "leg. This";
  - SC-50: "principle ones" to "principal ones"; his three new links written without "http://", and the last with a
    space between its text and its address, written the way his other links to his guides are; the trailing space.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-cde/apply_x1108b.py [--write]
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
sys.path.insert(0, str(HERE))
import texts_cde as T  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ANS = HERE / 'ANSWERS-X1108B-20261108-1508.json'
CARD = {'SC-24': 'S24', 'SC-47': 'S47', 'SC-48': 'S48', 'SC-50': 'S50', 'SC-52': 'S52', 'SC-53': 'S53', 'SC-56': 'S56',
        'SC-57': 'S57'}

# (old, new, why): exact strings in his version, each must occur once
FIXES = {
    'SC-47': [('(Hertzberg, et al, 2000)', '([Hertzberg, et al, 2000](%s))' % T.HERTZBERG, 'citation link put back'),
              ('(VA/DoD, 2023)', '([VA/DoD, 2023](%s))' % T.VADOD, 'citation link put back')],
    'SC-48': [("Why don't these drugs on calcified PTSD?", "Why don't these drugs work on calcified PTSD?",
               'the missing word, as his post had it'),
              ("That's like a bit like", "That's a bit like", 'a doubled word'),
              ('broken leg.This protocol', 'broken leg. This protocol', 'the missing space'),
              ('(Shimazu, et al, 2013)', '([Shimazu, et al, 2013](%s))' % T.SHIMAZU, 'citation link put back'),
              ('(Whittle & Singewald, 2014)', '([Whittle & Singewald, 2014](%s))' % T.WHITTLE, 'citation link put back')],
    'SC-50': [('on its own, but slowly,', 'on its own, but [slowly](%s),' % T.ROBISON, 'citation link put back'),
              ('(He, et al, 2005)', '([He, et al, 2005](%s))' % T.HE, 'citation link put back'),
              ('(Shao, et al, 2021)', '([Shao, et al, 2021](%s))' % T.SHAO, 'citation link put back'),
              ('which DeltaFosB plays a role in. \n', 'which DeltaFosB plays a role in.\n', 'the trailing space'),
              ('apart from the principle ones studied', 'apart from the principal ones studied', 'a misspelling'),
              ('[my iboga guide](iboga.u-dont-exist.com)', '[my iboga guide](http://iboga.u-dont-exist.com/)',
               'the address as his other links to the guide have it'),
              ('[loveyhuasca](soma.u-dont-exist.com)', '[loveyhuasca](http://soma.u-dont-exist.com/)',
               'the address as his other link to soma has it'),
              ('[Altered States Guide] (badtrips.u-dont-exist.com)', '[Altered States Guide](http://badtrips.u-dont-exist.com/)',
               'a space that broke the link, and the address')],
}


def main(write=False):
    ans = json.loads(ANS.read_text(encoding='utf-8'))
    md = ARTICLE.read_text(encoding='utf-8')
    assert ans['article']['sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), 'article changed since his page'
    entries = {e['key']: e for e in T.T}
    lines = md.split('\n')
    done = {}
    for it in ans['items']:
        sid, key = it['id'], CARD[it['id']]
        e = entries[key]
        if it['status'] == 'approved':
            assert it['my_version'] == T.plain(e['md']), '%s: the card he approved is not texts_cde.py\'s' % sid
            new, fixes = e['md'], []
        elif it['status'] == 'revise':
            new, fixes = it['your_version'], []
            for old, rep, why in FIXES[sid]:
                assert new.count(old) == 1, (sid, old)
                new = new.replace(old, rep)
                fixes.append({'was': old, 'now': rep, 'why': why})
            new = new.strip()
        else:
            sys.exit('%s: status %s' % (sid, it['status']))
        hits = [i for i, l in enumerate(lines) if l.startswith(e['start'])]
        if len(hits) != 1:
            sys.exit('%s: %d lines start with %r' % (sid, len(hits), e['start']))
        i = hits[0]
        done[sid] = {'status': it['status'], 'line': i + 1, 'old': lines[i], 'new': new, 'fixes': fixes,
                     'comment': it.get('comment', '')}
        lines[i] = new
    out = '\n'.join(lines)
    rec = {'about': 'his answers on x1108b (2026-11-08): five approved, three his versions', 'answers': ANS.name,
           'before_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest(), 'cards': done}
    print('\n'.join('%s %s line %d, %d fixes' % (k, v['status'], v['line'], len(v['fixes'])) for k, v in done.items()))
    print('after', rec['after_sha256'][:8])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1108B.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
