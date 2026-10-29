"""Batch 482's candidates: the writers' versions I chose, in place, for the next recheck and his page.

TARGETS.json (make_targets.py) holds each item; writers/VERSIONS-W<k>.json the writers' two versions of its flagged
stretch; CHOICES.json my pick for each item ("v1", "v2" or "none") with the reason, and any small logged fix to the
picked words ({"fix": [[old, new, why], ...]}). Items T<n> replace sentences that aren't his; items J<n> are suggestions for
his own words, which go in only with his answer (their cards show his words first).

  python3 articles/inner-signal/humanize/fix-20261029/b482/make_b482.py
Writes CANDIDATES.json and CANDIDATE-MASTER.md (HUMANIZED-SO-FAR.md with every picked version in, for the recheck that
measures them in place; the working copy doesn't change until he answers).
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
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

MASTER = H / 'HUMANIZED-SO-FAR.md'


def main():
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    targets = {t['id']: t for t in json.loads((B / 'TARGETS.json').read_text(encoding='utf-8'))['items']}
    versions = {}
    for f in sorted((B / 'writers').glob('VERSIONS-W*.json')):
        versions.update(json.loads(f.read_text(encoding='utf-8')))
    choices = json.loads((B / 'CHOICES.json').read_text(encoding='utf-8'))
    new_raw, spots, lost = {}, [], []
    for tid, ch in sorted(choices.items(), key=lambda kv: (kv[0][0], int(kv[0][1:]))):
        t = targets[tid]
        if ch['pick'] == 'none':
            spots.append({'id': tid, 'where': t['where'], 'block': t['block'], 'pick': 'none', 'why': ch['why']})
            continue
        words = versions[tid][ch['pick']]
        for old, new, _why in ch.get('fix', []):
            assert words.count(old) == 1, (tid, old)
            words = words.replace(old, new)
        i = t['block']
        cur = new_raw.get(i)
        text = sr.blocks(cur[0])[0]['text'] if cur else bl[i]['text']
        assert text.count(t['flagged_stretch']) == 1, tid
        after = text.replace(t['flagged_stretch'], words)
        new_raw[i] = [set_block_text(cur[0] if cur else raw[i], after, lost)]
        spots.append({'id': tid, 'where': t['where'], 'block': i, 'whose': 'his' if tid.startswith('J') else 'ours',
                      'pick': ch['pick'], 'why': ch['why'], 'fixes': ch.get('fix', []),
                      'old': t['flagged_stretch'], 'new': words, 'readings': t['readings'],
                      'paragraph_before': bl[i]['text'], 'paragraph_after': after})
    out = []
    for j, r in enumerate(raw):
        out += new_raw.get(j, [r])
    cand = '\n\n'.join(out) + '\n'
    (B / 'CANDIDATE-MASTER.md').write_text(cand, encoding='utf-8')
    rec = {'master_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'candidate_sha256': hashlib.sha256(cand.encode('utf-8')).hexdigest(), 'links_dropped': lost, 'spots': spots}
    (B / 'CANDIDATES.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d spots in, %d left; links dropped: %s' % (sum(1 for s in spots if s['pick'] != 'none'),
                                                       sum(1 for s in spots if s['pick'] == 'none'), lost))


if __name__ == '__main__':
    main()
