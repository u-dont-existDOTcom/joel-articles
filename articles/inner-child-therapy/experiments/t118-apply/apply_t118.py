#!/usr/bin/env python3
"""Turn 118: the four pairs back under Four Pairs That Commonly Hook the Child.

  python3 articles/inner-child-therapy/experiments/t118-apply/apply_t118.py      (after turn 117's install; once)

Joel, 2026-11-04 00:43 UTC (experiments/t118-answers/JOEL-20261104-0043.md): "i guess you should restore the four pairs i
dleeted then i didn't realize they wer eimportant for that part." He had cut them as redundant (card P11, rejected in turn
117: "to me it looked like redundancy so i cut it as it's said next"), and turn 117's message asked about the heading
that still promised them. The two sentences go back where they were, right after "Pema Chödrön has a quick map for
finding the bargain.", in his words from the last guide (turn 114, commit b3a1f54c: his straight apostrophe, which the
standard swap keeps). KEEP-AS-IS.json loses the meant cut X2 and gains K18, so no later pass cuts them as redundant again;
OWNER-EDITS.json gains joel-118-four-pairs."""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
ROOT = HERE.parents[3]
ARTICLE = ART / 'HUMANIZED-ARTICLE-SO-FAR.md'
KEEP = ART / 'KEEP-AS-IS.json'
LEDGER = ART / 'OWNER-EDITS.json'
LAST = subprocess.run(['git', '-C', str(ROOT), 'show', 'b3a1f54c:articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'],
                      capture_output=True, text=True, check=True).stdout
PAIRS = re.search(r"Pema Chödrön has a quick map for finding the bargain\. (It's four pairs[^\n]*?disgrace\.)", LAST).group(1)
AFTER = 'Pema Chödrön has a quick map for finding the bargain.'
JOEL = "i guess you should restore the four pairs i dleeted then i didn't realize they wer eimportant for that part."


def main():
    md = ARTICLE.read_text(encoding='utf-8')
    if PAIRS in md:
        print('already in:', PAIRS[:40])
        return 0
    assert md.count(AFTER + ' Your little one can panic') == 1
    md = md.replace(AFTER + ' Your little one can panic', AFTER + ' ' + PAIRS + ' Your little one can panic')
    ARTICLE.write_text(md, encoding='utf-8')
    keep = json.loads(KEEP.read_text(encoding='utf-8'))
    keep['cuts'] = [c for c in keep['cuts'] if c['id'] != 'X2']
    keep['keep'].append({
        'id': 'K18', 'kind': 'choice', 'quote': PAIRS,
        'what': ('Pema Chödrön\'s four pairs, under Four Pairs That Commonly Hook the Child. He cut them as redundant (card P11), '
                 'then asked for them back: they matter for that part. Don\'t cut them as a repeat of what follows.'),
        'joel': JOEL, 'when': '2026-11-04 00:43 UTC', 'where': 'his message after turn 117 (experiments/t118-answers/JOEL-20261104-0043.md)',
        'basis': 'his answer'})
    KEEP.write_text(json.dumps(keep, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    led = json.loads(LEDGER.read_text(encoding='utf-8'))
    led['entries'].append({
        'id': 'joel-118-four-pairs', 'status': 'applied',
        'what': ('The four pairs back under Four Pairs That Commonly Hook the Child, in his words from the last guide, after he had '
                 'cut them (card P11): "i didn\'t realize they wer eimportant for that part".'),
        'joel': '2026-11-04 00:43 UTC (experiments/t118-answers/JOEL-20261104-0043.md)',
        'where': 'Untangling the Belonging Bargains, Four Pairs That Commonly Hook the Child',
        'must_contain_exact': [AFTER + ' ' + PAIRS + ' Your little one can panic'],
        'must_have_line': ['#### Four Pairs That Commonly Hook the Child']})
    LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('four pairs back; KEEP-AS-IS X2 out, K18 in; OWNER-EDITS joel-118-four-pairs')
    return 0


if __name__ == '__main__':
    sys.exit(main())
