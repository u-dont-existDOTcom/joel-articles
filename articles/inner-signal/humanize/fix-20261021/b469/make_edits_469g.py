"""Batch 469g's edits for the 4.1 list (fix-20261020/EDITS41.json), written from meta.json (make_b469.py), 2026-10-21.

Each edit went through the gate's meaning reviews (march, cold read, meaning check, stance, and for the sweep's five
fixes the review of each fixed paragraph in its context; gate-answers.json answers what was answered rather than fixed).
Under the rule of 2026-10-21 (gate E200: many paragraphs are read in the real article through free Substack posts, not
one by one on pangram.com), they go into the working copy before their Pangram reading, which is the whole-guide recheck;
"paragraph_result" says so until the recheck's segments are read. A paragraph the recheck flags is fixed with a diagnosis
or taken back out (its old text is here).

  python3 articles/inner-signal/humanize/fix-20261021/b469/make_edits_469g.py   (from the repo root)
  python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --add articles/inner-signal/humanize/fix-20261021/b469/EDITS-469g.json
"""
import json, pathlib

B = pathlib.Path(__file__).resolve().parent
PENDING = 'pending: read in the whole-guide recheck through Substack (gate E200), fix-20261020/substack41r/'


def main():
    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    out = []
    for e in meta['edits']:
        out.append({'key': 'b469-' + e['key'], 'section': e['section'], 'batch': '469g', 'old': e['old'], 'new': e['new'],
                    'diagnosis': e['diagnosis'], 'paragraph_check': None, 'paragraph_result': PENDING,
                    'section_check': None, 'section_result': None,
                    'reviews': 'fix-20261021/b469/ (r1/, the round-2 files, gate-answers.json, GATE.json)'})
    (B / 'EDITS-469g.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(out), 'edits ->', B / 'EDITS-469g.json')


if __name__ == '__main__':
    main()
