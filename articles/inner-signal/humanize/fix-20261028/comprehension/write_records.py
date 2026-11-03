"""The comprehension audit's and the fix check's records for the comparison gate (gate E284, E285), and the lane's
COMPARE-GATE.json.

READ-RECORD.json: every paragraph the audit's readers read (the guide as it was when Joel wrote, commit 0a44911d), every
finding, and its fate from my check (CHECKED.json) and the fix page (REVIEW-28.json): a real problem or a snag with a fix
on his page is "his" (his answer decides), one he settled himself is "done", one that isn't a problem is "not", a snag
with no fix is "kept" at my severity 1, his own words are "his"; once his answers are in (APPLIED-28.json), an approved
card's findings are "fixed" and a card he answered otherwise is "his". verify/READ-RECORD.json: the fixed paragraphs as the
fresh readers of the fixes read them (make_verify.py, collect_verify.py).

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/write_records.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import compare_read as cr  # noqa: E402
import collect as c  # noqa: E402

GATE = {
    'about': 'The hypnosis guide\'s comparison gate (compare_read.py gate, run by lane_push.py; gates E284, E285): every '
             'paragraph of the guide so far is his as published, his own words, or read beside his text at its present '
             'words, and every finding a reader rated 2 or 3 has a fate.',
    'article': 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md',
    'original': 'articles/inner-signal/humanize/source/published-20260928.md',
    'records': ['articles/inner-signal/humanize/fix-2026*/comprehension/READ-RECORD.json',
                'articles/inner-signal/humanize/fix-2026*/comprehension/verify/READ-RECORD.json',
                # a batch's comparative read of its candidates (fix-20261029/b482/read/, read_candidates.py)
                'articles/inner-signal/humanize/fix-2026*/*/read/READ-RECORD.json'],
    'owner': ['articles/inner-signal/humanize/fix-2026*/joel-*-message.txt',
              'articles/inner-signal/humanize/fix-2026*/**/ANSWERS-*.json',
              'articles/inner-signal/humanize/fix-2026*/EDITS-joel-*.json'],
}


def main():
    F = json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']
    V = json.loads((HERE / 'CHECKED.json').read_text(encoding='utf-8'))['verdicts']
    review = json.loads((HERE / 'REVIEW-28.json').read_text(encoding='utf-8')) if (HERE / 'REVIEW-28.json').exists() else None
    card = {}
    if review:
        for s in review['suggestions']:
            for f in s.get('findings', []):
                card[f] = s['id']
    # once his answers are in (apply_answers_28.py's APPLIED-28.json), a card's findings take his answer as their fate
    applied = json.loads((HERE / 'APPLIED-28.json').read_text(encoding='utf-8')) if (HERE / 'APPLIED-28.json').exists() else None
    answered = applied['fates'] if applied else {}
    # a fix that only adds or changes punctuation (C-54's quote marks round a line said to oneself) leaves the words the
    # gate compares, so its finding stays on record as kept at my severity, with the approved fix named
    kept_fixes = json.loads((HERE / 'fix' / 'KEPT.json').read_text(encoding='utf-8'))['fixes']
    marks_only = {f for f in {g for x in kept_fixes for g in x.get('findings', [])}
                  if all(cr.loose(x['replace']) == cr.loose(x['with']) for x in kept_fixes if f in x.get('findings', []))}
    disp = {}
    for r in F:
        r['block_hashes'] = [cr.phash(c.NOW[i]['text']) for i in r['now_blocks']]
        r['same_as_original'] = r.get('same_as_published', False)
        v = V[r['id']]
        note = v[-1]
        if v[0] == 'done':
            disp[r['id']] = ['done', note]
        elif v[0] == 'not':
            disp[r['id']] = ['not', note]
        elif r['id'] in card and card[r['id']] in answered:
            ans = answered[card[r['id']]]
            if (ans.startswith('approved') or ans.startswith('accepted')) and r['id'] in marks_only:
                disp[r['id']] = ['kept', 'card %s, %s (%s); the fix changes only punctuation, which the comparison '
                                 'leaves out, so the words stay on record: %s' % (card[r['id']], ans, applied['answers'], note),
                                 v[1] if isinstance(v[1], int) else 1]
            elif ans.startswith('approved') or ans.startswith('accepted'):
                disp[r['id']] = ['fixed', 'card %s, %s (%s): %s' % (card[r['id']], ans, applied['answers'], note)]
            else:
                disp[r['id']] = ['his', 'card %s, his answer: %s (%s)' % (card[r['id']], ans, applied['answers'])]
        elif v[0] == 'his':
            disp[r['id']] = ['his', '%s%s' % (note, ' (card %s on his fix page)' % card[r['id']] if r['id'] in card else '')]
        elif r['id'] in card:
            disp[r['id']] = ['his', 'a fix is on his fix page, card %s; his answer decides: %s' % (card[r['id']], note)]
        elif v[0] == 'minor':
            disp[r['id']] = ['kept', 'a small snag with no fix worth its cost: %s' % note, 1]
        else:
            disp[r['id']] = [None, 'a real problem with no fix yet: %s' % note]
    coverage = [cr.phash(b['text']) for b in c.NOW if not b['level']]
    cr.record(HERE, findings=F, coverage=coverage, dispositions=disp,
              article='articles/inner-signal/humanize/HUMANIZED-SO-FAR.md at 0a44911d')
    (H / 'COMPARE-GATE.json').write_text(json.dumps(GATE, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    open_ = [k for k, d in disp.items() if d[0] is None]
    print('READ-RECORD.json: %d paragraphs read, %d findings, %d fates; with no fix yet: %s'
          % (len(set(coverage)), len(F), len(disp), ', '.join(open_) or 'none'))


if __name__ == '__main__':
    main()
