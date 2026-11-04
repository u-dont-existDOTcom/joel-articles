#!/usr/bin/env python3
"""Turn 120: the fate of every entry in the InnerSignal map's queue of guide changes, for the queue's reset.

Joel, 2026-11-04 10:02 UTC: "make sure you clear the humanization queue". The queue is
authoring/PENDING-PUBLIC-GUIDE-CHANGES.md in u-dont-existDOTcom/innerSignalGraph, queue version 2026-10-31-r20 (the file as
of cb2008ce6; the map's main at ca535c0e9 when this was built): 52 entries, PGQ-001 to PGQ-055 (there is no PGQ-044 to
PGQ-046). Its consumption contract: an entry is consumed when its reader-facing meaning is incorporated or deliberately
dispositioned, and once all are, the file goes back to its EMPTY sentinel with authoring/public-guide-sync.json updated, in
one reviewed change. That change is the map lane's (UDA's suggested-fix rule), so this record is what its UDA lane item
points to.

Sources: PGQ-018 to PGQ-055 from turn 119's reading against his reorganized guide (experiments/t119-queue/QUEUE-COVERAGE.json,
with turn 120's two changes: PGQ-054 in, his own line; PGQ-036 left out, as recommended); PGQ-001 to PGQ-017 from this
turn's reading of the same guide (QUEUE-001-017.json: those went in by turn 71, before he reorganized and edited the guide
himself, so they were read again). Fates: "in" (the reader-facing meaning is there), "core point in" (the core point is
there in his words; what the entry adds beyond it is left out, his call: 00:56 UTC "i think i already put them in if they
were important points", and 10:02), "left out" (not in the guide, with the reason). Every quote is checked to be his
guide's own words, verbatim. Writes QUEUE-CLEARED.json and QUEUE-CLEARED.md."""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
GUIDE = ART / 'HUMANIZED-ARTICLE-SO-FAR.md'
T119 = HERE.parent / 't119-queue' / 'QUEUE-COVERAGE.json'
T120 = HERE / 'QUEUE-001-017.json'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/'
FATE = {'in': 'in', 'partly': 'core point in', 'not in': 'left out'}
# The two whose extra went in an edit of his inside a paragraph: the turn-116 card (A6) asked him about whole sections he
# cut, so these were never confirmed as meant (the subagent's reading, which I checked against EDITS.json). Asked in turn 120.
UNCONFIRMED = {
    'PGQ-009': ('The rest went in his own edit inside the paragraph (his sentence "Other jobs can go to friends or community, outsource to '
                'the tools or pros, whatever works."), which no card asked him to confirm; asked in turn 120, my recommendation: leave it out, '
                'since the core point is there in his words.'),
    'PGQ-016': ('The rest went in his own edit inside the paragraph (what a memory aid can be, and that it needn\'t explain your life), '
                'which no card asked him to confirm; asked in turn 120, my recommendation: leave it out, since the core point is there in '
                'his words.'),
    'PGQ-015': ('The rest went when he removed its paragraph himself in turn 106 ("it seemed extra"); left out, his call (00:56 and 10:02 '
                'UTC).'),
    'PGQ-017': ('The rest was never written into the guide (turn 71 counted this entry in with PGQ-014); I\'d leave it out, his call (00:56 '
                'and 10:02 UTC).'),
}
OWNER = [
    ['2026-11-04 00:56 UTC', 'make sure you check the lane bc you were sent some things to put into the guide, but i think i already put them in if they were important points'],
    ['2026-11-04 10:02 UTC', 'make sure you clear the humanization queue'],
]


def main():
    guide = GUIDE.read_text(encoding='utf-8')
    old = json.loads(T119.read_text(encoding='utf-8'))
    new = json.loads(T120.read_text(encoding='utf-8'))
    rows, bad = [], []
    for src, items in (('turn 120 reading', new), ('turn 119 reading', old)):
        for x in items:
            st = x.get('status_after', '').split(' (')[0] or x['status']
            fate = FATE[st] if st in FATE else {'in': 'in', 'left out': 'left out'}[st]
            basis = ''
            if x['id'] == 'PGQ-054':
                basis = 'His own line of 2026-11-04 09:42 UTC (experiments/t120-answers/JOEL-20261104-0942.md).'
                where, quote = 'Practicing With Your Little One > Journal With Each Hand', "A protective part might grab the pen first, and then it gets that hand until it's had its say, even if all it can do is scribble angrily."
            else:
                where, quote = x['where'], x['quote']
            if x['id'] == 'PGQ-036':
                basis = ('Left out: the guide never raises whether hypnosis suits someone grieving, so I recommended leaving it out (turn 119); '
                         'his reply of 09:42 took the other open item and raised no objection, and at 10:02 he asked for the queue to be cleared.')
            elif x['id'] in UNCONFIRMED:
                basis = UNCONFIRMED[x['id']]
            elif fate == 'core point in' and x.get('his_cut'):
                basis = 'The rest went with a passage he cut on purpose (KEEP-AS-IS.json %s).' % x['his_cut']
            elif fate == 'core point in' and src == 'turn 120 reading':
                basis = 'The rest went in his own edits of the guide; left out, his call (00:56 and 10:02 UTC).'
            elif fate == 'core point in':
                basis = 'The rest left out, as I recommended in turn 119; his call (00:56 and 10:02 UTC).'
            elif fate == 'left out' and x.get('his_cut'):
                basis = 'Left out: in a passage he cut on purpose (KEEP-AS-IS.json %s).' % x['his_cut']
            elif fate == 'left out' and not basis:
                basis = 'Left out: NOT DECIDED'
            if quote and quote not in guide:
                bad.append(x['id'])
            rows.append({'id': x['id'], 'title': x['title'], 'point': x['point'], 'fate': fate, 'where': where, 'quote': quote,
                         'missing': x.get('missing', '') if fate != 'in' else '', 'basis': basis, 'read': src})
    rows.sort(key=lambda r: int(r['id'].split('-')[1]))
    ids = [r['id'] for r in rows]
    assert len(ids) == len(set(ids)) == 52, (len(ids), len(set(ids)))
    if bad:
        sys.exit('quotes not in the guide verbatim: %s' % bad)
    undecided = [r['id'] for r in rows if 'NOT DECIDED' in r['basis']]
    counts = {'entries': len(rows), 'in': sum(r['fate'] == 'in' for r in rows), 'core': sum(r['fate'] == 'core point in' for r in rows),
              'out': sum(r['fate'] == 'left out' for r in rows), 'undecided': undecided}
    out = {'queue': 'u-dont-existDOTcom/innerSignalGraph authoring/PENDING-PUBLIC-GUIDE-CHANGES.md', 'queue_version': '2026-10-31-r20',
           'queue_file_commit': 'cb2008ce6', 'map_main_when_built': 'ca535c0e9',
           'guide': 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md',
           'guide_sha256': hashlib.sha256(GUIDE.read_bytes()).hexdigest(), 'owner': OWNER, 'counts': counts, 'entries': rows}
    (HERE / 'QUEUE-CLEARED.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    md = ['# The InnerSignal map\'s queue for the guide: every entry\'s fate (turn 120)', '',
          'Joel, 2026-11-04 10:02 UTC: "make sure you clear the humanization queue". The queue is `authoring/PENDING-PUBLIC-GUIDE-CHANGES.md` '
          'in u-dont-existDOTcom/innerSignalGraph, queue version 2026-10-31-r20 (the file as of cb2008ce6): %d entries, PGQ-001 to PGQ-055 '
          '(there is no PGQ-044 to PGQ-046), each read against his reorganized guide, [HUMANIZED-ARTICLE-SO-FAR.md](%sHUMANIZED-ARTICLE-SO-FAR.md). '
          'PGQ-018 to PGQ-055 were read in turn 119 ([QUEUE-COVERAGE.md](%sexperiments/t119-queue/QUEUE-COVERAGE.md)); PGQ-001 to PGQ-017 '
          'went in by turn 71, before he reorganized and edited the guide himself, so they were read again this turn (by a subagent of '
          'this session, Claude Opus 5.5, given the queue, the guide, his cuts and turn 119\'s record; I read each of its judgments, and the '
          'script checks its quotes). Built by '
          '[build_cleared.py](%sexperiments/t120-queue/build_cleared.py), which checks that every quote below is the guide\'s own words.'
          % (counts['entries'], BLOB, BLOB, BLOB), '',
          '**Counts:** %d in, %d with the core point in his words (what the entry adds beyond it is left out, his call: 00:56 UTC, "i think i '
          'already put them in if they were important points"), %d left out.%s' % (counts['in'], counts['core'], counts['out'],
          (' **Not decided yet: %s.**' % ', '.join(undecided)) if undecided else ' Every entry is consumed, so the map\'s file can go back to its EMPTY sentinel.'), '',
          'The reset is the map lane\'s own change (UDA\'s suggested-fix rule: a project\'s own agent changes its files), so its item for '
          'that lane is [UDA-ITEM.md](%sexperiments/t120-queue/UDA-ITEM.md), to go in UDA\'s `suggested-fixes/innerSignalGraph/` as his '
          'request; filing it opens a public pull request in universal-dev-architecture, which waits for his yes.' % BLOB, '',
          '| Item | Title | Fate | Where in his guide | His words that carry it | Left out | Why |', '|---|---|---|---|---|---|---|']
    for r in rows:
        md.append('| %s | %s | %s | %s | %s | %s | %s |' % tuple(str(v).replace('|', '\\|').replace('\n', ' ') for v in (
            r['id'], r['title'], r['fate'], r['where'], r['quote'], r['missing'], r['basis'])))
    (HERE / 'QUEUE-CLEARED.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(counts)
    return 1 if undecided else 0


if __name__ == '__main__':
    sys.exit(main())
