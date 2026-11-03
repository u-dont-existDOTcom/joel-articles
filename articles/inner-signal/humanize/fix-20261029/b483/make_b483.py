"""Batch 483's candidates, with batch 482's versions that read Human, in place: the guide for the next recheck.

From the working copy (HUMANIZED-SO-FAR.md, unchanged until Joel answers his page):
- batch 482's 11 versions that read Human in place (../b482/recheck/read/SPOTS.json, "human": true), exactly as they were
  checked;
- batch 483's picks (CHOICES.json: {id: {"pick": "v1"|"v2"|"none", "why": ..., "fix": [[old, new, why], ...]}}) of the
  writers' versions (writers/VERSIONS-W<k>.json) of the stretches in TARGETS.json. Items J<n> are suggestions for his own
  words: in only so the recheck can measure them, and on his page beside his words.

  python3 articles/inner-signal/humanize/fix-20261029/b483/make_b483.py  -> CANDIDATES.json, CANDIDATE-MASTER.md
"""
import hashlib
import json
import pathlib
import re
import sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
ROOT = H.parents[2]
P482 = B.parent / 'b482'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

MASTER = H / 'HUMANIZED-SO-FAR.md'


def main():
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    # what goes in: batch 482's Human ones, then batch 483's picks
    kept = {s['id'] for s in json.loads((P482 / 'recheck' / 'read' / 'SPOTS.json').read_text(encoding='utf-8'))['spots']
            if s.get('human')}
    todo = []
    for s in json.loads((P482 / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots']:
        if s['id'] in kept:
            todo.append({'id': s['id'], 'batch': 482, 'block': s['block'], 'where': s['where'], 'whose': s['whose'],
                         'old': s['old'], 'new': s['new'], 'pick': s['pick'], 'why': 'read Human in place in batch 482\'s '
                         'recheck (%s)' % next(x['now'] for x in json.loads((P482 / 'recheck' / 'read' / 'SPOTS.json')
                                                                             .read_text(encoding='utf-8'))['spots']
                                                 if x['id'] == s['id']),
                         'fixes': s.get('fixes', []), 'readings': s['readings']})
    targets = {t['id']: t for t in json.loads((B / 'TARGETS.json').read_text(encoding='utf-8'))['items']}
    versions = {}
    for f in sorted((B / 'writers').glob('VERSIONS-W*.json')):
        versions.update(json.loads(f.read_text(encoding='utf-8')))
    choices = json.loads((B / 'CHOICES.json').read_text(encoding='utf-8'))
    left = []
    for tid, ch in choices.items():
        t = targets[tid]
        if ch['pick'] == 'none':
            left.append({'id': tid, 'batch': 483, 'where': t['where'], 'block': t['block'], 'pick': 'none', 'why': ch['why']})
            continue
        words = versions[tid][ch['pick']]
        for old, new, _why in ch.get('fix', []):
            assert words.count(old) == 1, (tid, old)
            words = words.replace(old, new)
        todo.append({'id': tid, 'batch': 483, 'block': t['block'], 'where': t['where'], 'whose': t['whose'],
                     'old': t['flagged_stretch'], 'new': words, 'pick': ch['pick'], 'why': ch['why'],
                     'fixes': ch.get('fix', []), 'readings': t['readings_before']})
    new_raw, spots, lost = {}, [], []
    for s in sorted(todo, key=lambda x: (x['block'], x['id'])):
        i = s['block']
        cur = new_raw.get(i)
        text = sr.blocks(cur)[0]['text'] if cur else bl[i]['text']
        assert text.count(s['old']) == 1, (s['id'], 'its stretch is not once in its paragraph')
        after = text.replace(s['old'], s['new'])
        new_raw[i] = set_block_text(cur if cur else raw[i], after, lost)
        spots.append(dict(s, paragraph_before=bl[i]['text'], paragraph_after=after))
    # every spot of a paragraph gets the paragraph as it finally is
    final = {i: sr.blocks(r)[0]['text'] for i, r in new_raw.items()}
    for s in spots:
        s['paragraph_after'] = final[s['block']]
    out = [new_raw.get(j, r) for j, r in enumerate(raw)]
    cand = '\n\n'.join(out) + '\n'
    (B / 'CANDIDATE-MASTER.md').write_text(cand, encoding='utf-8')
    rec = {'master_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'candidate_sha256': hashlib.sha256(cand.encode('utf-8')).hexdigest(), 'links_dropped': lost,
           'spots': spots + left}
    (B / 'CANDIDATES.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d in (%d from batch 482, %d from batch 483), %d left; links dropped: %s' % (
        len(spots), sum(1 for s in spots if s['batch'] == 482), sum(1 for s in spots if s['batch'] == 483), len(left), lost))


if __name__ == '__main__':
    main()
