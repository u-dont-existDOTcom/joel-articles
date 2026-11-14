"""Put his x1113b answers into HUMANIZED-SO-FAR.md (his answers file of 2026-11-14 22:04 UTC: ANSWERS-X1113B-20261114-2204.json;
the cards page's stored answers say the same: ../CARDS-PAGE-DECISIONS-20261114-2204.json).

- SC-95b, approved: block 95 becomes his version without his PTSD line (texts_x1113b.K95, with its link).
- SC-DMSOc, revise: his version goes in as a new item of four paragraphs before the Dynorphin Bridge. It is the card's
  text with one clause of his added after the young-mouse study ("although so far there's no proof it's harming
  children, and many people use it on their children for injuries, infections, and so forth with good results in
  practice"); the cards page showed the text without links, so the links go back on its citations (the card's Markdown,
  texts_x1113b.DMSO), and the script checks that the result, read as plain text, is his version word for word.
- SC-54, approved: block 54 is a paragraph of mine, so it goes in only with --with-54=VERSION (the texts_x1113b name of
  the version), after a Pangram check of that version by itself read Human High in every window (gate
  bad-trips-2026-11-12l, tools/humanization/apply_gate.py). As approved it read AI Detected (checks-1114).

His versions don't go through that gate; they are his.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1113b/apply_x1113b.py [--write] [--with-54=K54C]

Each card goes in once: a card already in the article is skipped, so SC-54 can follow the other two.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import apply_gate  # noqa: E402
import texts_x1113b as T  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
LEDGER = H / 'pangram-ledger.jsonl'
ANSWERS = HERE / 'ANSWERS-X1113B-20261114-2204.json'
HIS_CLAUSE = (', although so far there\'s no proof it\'s harming children, and many people use it on their children for '
              'injuries, infections, and so forth with good results in practice')
AT = '([Hanslick, et al, 2009](%s))' % T.HANSLICK


def his_dmso(item):
    """His version with the card's links back on its citations; checked word for word against what he saved."""
    m3 = T.DMSO[2]
    assert m3.count(AT + '.') == 1
    paras = [T.DMSO[0], T.DMSO[1], m3.replace(AT + '.', AT + HIS_CLAUSE + '.'), T.DMSO[3]]
    want = [p.strip() for p in item['your_version'].split('\n\n')]
    got = [T.plain(p) for p in paras]
    assert got == want, [(g[:60], w[:60]) for g, w in zip(got, want) if g != w]
    return paras


def main(write=False, with54=None):
    """with54: the name of the texts_x1113b variable holding the version of SC-54 that read Human High (K54, K54C, ...)."""
    md = ARTICLE.read_text(encoding='utf-8')
    a = json.loads(ANSWERS.read_text(encoding='utf-8'))
    items = {x['id']: x for x in a['items']}
    assert items['SC-95b']['status'] == 'approved' and items['SC-54']['status'] == 'approved'
    assert items['SC-DMSOc']['status'] == 'revise'
    before = hashlib.sha256(md.encode('utf-8')).hexdigest()
    lines = md.split('\n')
    applied = []
    # SC-95b
    if T.K95 not in lines:
        (i,) = [k for k, l in enumerate(lines) if l.startswith('You must pick one of two ketone strategies')]
        assert lines[i] == T.OLD95
        applied.append({'card': 'SC-95b', 'status': 'approved', 'line': i + 1, 'old': lines[i], 'new': T.K95,
                        'whose': 'his version (2026-11-12 20:16 UTC) less his PTSD line, with the trials\' link'})
        lines[i] = T.K95
    # SC-DMSOc
    paras = his_dmso(items['SC-DMSOc'])
    if paras[0] not in lines:
        (b,) = [k for k, l in enumerate(lines) if l.startswith(T.BEFORE)]
        assert lines[b - 1] == '' and lines[b - 2].startswith(T.AFTER)
        lines[b:b] = [x for p in paras for x in (p, '')]
        applied.append({'card': 'SC-DMSOc', 'status': 'revise', 'line': b + 1, 'inserted': paras,
                        'whose': 'his version (2026-11-14 22:04 UTC): the card\'s text and his clause on children, links back'})
    # SC-54
    if with54:
        new54 = getattr(T, with54)
        ok, why = apply_gate.check(__import__('pangram_ledger').read(LEDGER), T.plain(new54))
        for w in why:
            print('SC-54:', w)
        assert ok, 'SC-54 has no check of it by itself at Human High in every window'
        (j,) = [k for k, l in enumerate(lines) if l.startswith('The Fix: If the brain is burning less sugar')]
        assert lines[j] == T.OLD54
        applied.append({'card': 'SC-54', 'status': 'approved', 'line': j + 1, 'old': lines[j], 'new': new54,
                        'version': with54, 'gate': why})
        lines[j] = new54
    out = '\n'.join(lines)
    rec = {'about': 'his answers on x1113b (exported 2026-11-14 22:04 UTC)', 'answers': ANSWERS.name,
           'applied': applied, 'held': [] if with54 else ['SC-54: waits for a version that reads Human High by itself'],
           'before_sha256': before, 'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()}
    print('after', rec['after_sha256'][:8], [x['card'] for x in applied])
    if write and applied:
        ARTICLE.write_text(out, encoding='utf-8')
        name = 'APPLIED-X1113B%s.json' % ('-54' if with54 else '')
        (HERE / name).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    w54 = [x.split('=', 1)[1] for x in sys.argv if x.startswith('--with-54=')]
    main('--write' in sys.argv, w54[0] if w54 else None)
