"""Joel's answers to the DeltaFosB cards (REVIEW-X1105D, built by the separate DeltaFosB lane; answered 2026-11-06
16:35 UTC, ANSWERS-X1105D-20261106-1635.json beside this file).

- DFB-1, revise. His version keeps the Nestler 2008 citation and "for weeks after the cycles stop", and adds the point
  the card had missed: the loop, not the protein, is what is permanent. His comment: "you didn't understand my point,
  and you already explained that you didn't understand it in the old lane, and now this new lane forgot what the old
  lane knew".
- DFB-3 and DFB-4, approved as his own versions ("the catecholamines that transcribe", and Week 8+ hedged with "if the
  animal timelines carry over").
- DFB-2, revise, with no version of his: he sent the paragraph back to its original wording, because the card's added
  sentence ("The two aren't one mechanism, though") did not tell the reader what each of the two does. That block stays
  as it is and the point goes to a new card this turn.

Placed edits by block, his text copied as he wrote it (UDA patterns/safety-layer-cuts.md, steps 1 to 3).

  python3 articles/neuro-de-armoring/humanize/fix-20261106/apply_dfb.py
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ANS = HERE / 'ANSWERS-X1105D-20261106-1635.json'
HIS_IN = ('DFB-1', 'DFB-3', 'DFB-4')          # the three where his own version goes in
STARTS = {
    'DFB-1': 'The Hardening: Chronic cycles lead to the accumulation of DeltaFosB',
    'DFB-3': 'In this state, functional IQ drops substantially',
    'DFB-4': 'Week 8+: The BaselineState',
    'DFB-2': 'The Problem: To protect itself from the Glutamate storm',
}


def plain(t):
    """The block as the card shows it: links to their text, emphasis markers gone."""
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    return re.sub(r'(\*{1,3}|_{1,3})(?=\S)(.+?)(?<=\S)\1', r'\2', t)


def main():
    md = ARTICLE.read_text(encoding='utf-8')
    answers = json.loads(ANS.read_text(encoding='utf-8'))
    assert answers['article']['sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), \
        'the article changed since his page'
    A = {x['id']: x for x in answers['items']}

    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    applied = []
    for cid in HIS_IN:
        card = A[cid]
        his = (card['your_version'] or card['my_version']).strip()
        (i,) = [k for k, b in enumerate(raw) if b.startswith(STARTS[cid])]
        assert plain(raw[i]) == card['before'], (cid, plain(raw[i])[:90])
        assert plain(his) != card['before'], cid
        raw[i] = his
        applied.append({'card': cid, 'status': card['status'], 'block_starts': STARTS[cid],
                        'whose_words': 'his', 'after': plain(his)})

    # DFB-2: unchanged, by his answer.
    card = A['DFB-2']
    (j,) = [k for k, b in enumerate(raw) if b.startswith(STARTS['DFB-2'])]
    assert plain(raw[j]) == card['before'] == (card['your_version'] or '').strip(), 'DFB-2 is not back at its original'

    ARTICLE.write_text('\n\n'.join(raw) + '\n', encoding='utf-8')
    (HERE / 'APPLIED-DFB.json').write_text(json.dumps({
        'review_id': answers['review_id'],
        'answered_utc': '2026-11-06T16:35Z',
        'applied': applied,
        'untouched': {'DFB-2': 'he sent block %d back to its original wording; its point goes to a new card' % j},
        'article_sha256_after': hashlib.sha256(ARTICLE.read_bytes()).hexdigest(),
    }, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for a in applied:
        print(a['card'], 'his version in')
    print('DFB-2 unchanged (his answer)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
