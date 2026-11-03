"""Put batch f1102's fixes that read Human in their stretch into the hypnosis guide, record each edit's fate, and write the
read record and RESULTS.md (every check of batches f1102 and f1102b, with its link and windows).

In (ours, each read Human Written in its stretch through the API): F-61 and F-62 (Forget the left-brain/right-brain
cartoon), F-216 (If you sense you are being influenced), F-361 (The 15-minute daily practice), F-527 and F-528 (Pattern
10). Not in: F-119 and F-762, whose stretches still read Human (Low) on them, and their second tries F-118 and F-762b,
which read AI Detected (E324: a fix that makes its stretch worse comes out); those two stretches go on his page as
stretches to edit. The cards C-92 (the C-92b wording) and C-480 wait for the owner-delivery gate and his answer.

  python3 articles/inner-signal/humanize/fix-20261102/f1102/apply_f1102.py [--check]
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import compare_read as cr  # noqa: E402
import fixes_f1102 as fx  # noqa: E402
import suggestion_review as sr  # noqa: E402

TAKE = ['F-61', 'F-62', 'F-216', 'F-361', 'F-527', 'F-528']
FATES = {
    'F-61': 'in: f1102-61 Human Written (3 High, 2 Medium; the new sentences in a Medium window with F-62)',
    'F-62': 'in: with F-61',
    'F-119': 'not in: f1102-119 Human Written but a Human (Low) window still over the breathing line and the two sentences before it; its second try (F-118 with it) read AI Detected; a stretch to edit on his page',
    'F-216': 'in: f1102-216 Human Written, one window, High',
    'F-361': 'in: f1102-361 Human Written, one window, High',
    'F-527': 'in: f1102-527 Human Written (3 High, 2 Medium; the question run Medium)',
    'F-528': 'in: with F-527',
    'F-762': 'not in: f1102-762 Human Written but the new disclaimer sentence Human (Low); its second try (F-762b) read AI Detected; a stretch to edit on his page',
    'C-92': 'card: c1102-92b (the bracket wording) Human Written, one window, High; c1102-92a (the clause cut) Human (Medium) on his rent line; to the owner-delivery gate, then his page',
    'C-480': 'card: c1102-480 Human Written, the joined sentence High; to the owner-delivery gate, then his page',
}


def results_md():
    out = ['# Batches f1102 and f1102b: the free whole check\'s windows, fixed and checked', '',
           'Each stretch (at most six paragraphs with its heading, E325) through the API with a public link, my prediction '
           'written first (the ledger). Windows are label (confidence) and words.', '']
    for name in ('API-F1102.jsonl', 'API-F1102B.jsonl'):
        for l in (HERE / name).read_text(encoding='utf-8').splitlines():
            r = json.loads(l)
            ws = '; '.join('%s (%s) %d' % ('AI' if str(w[0]).startswith('AI') else 'Human', w[1], w[2]) for w in r['windows'])
            out.append('- **%s**, %d words: [%s, %.1f%% AI](%s). Windows: %s' % (r['name'], r['words'], r['headline'],
                                                                              r['fraction_ai'] * 100, r['dashboard_link'], ws))
    out += ['', 'Fates:', ''] + ['- %s: %s' % (k, v) for k, v in FATES.items()]
    return '\n'.join(out) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    before = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert before == fx.GUIDE_SHA
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    for eid, b, kind, old, new, why in fx.EDITS:
        if eid in TAKE:
            assert raw[b].count(old) == 1, eid
            raw[b] = raw[b].replace(old, new)
    new_md = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(new_md.encode('utf-8')).hexdigest()
    old_bl, new_bl = sr.blocks(md), sr.blocks(new_md)
    assert len(old_bl) == len(new_bl)
    changed = [b['i'] for b, c in zip(old_bl, new_bl) if b['text'] != c['text']]
    rec = {'before_sha256': before, 'after_sha256': after, 'taken': TAKE, 'fates': FATES, 'changed_blocks': changed,
           'blocks': len(new_bl)}
    print(json.dumps(rec, indent=1))
    (HERE / 'RESULTS.md').write_text(results_md(), encoding='utf-8')
    if a.check:
        return
    (H / 'HUMANIZED-SO-FAR.md').write_text(new_md, encoding='utf-8')
    (HERE / 'APPLIED-F1102.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(new_bl[i]['text']) for i in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs batch f1102\'s fixes changed (ours), read by the lead '
                      'session in place beside the words they replace, every point kept (E284, E294)' % (after[:8], len(changed)))


if __name__ == '__main__':
    main()
