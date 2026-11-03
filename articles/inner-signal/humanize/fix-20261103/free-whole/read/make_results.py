"""RESULT-A.json and RESULT-B.json for the whole guide's third free check (3 November, after his answers of 00:39 UTC and
the 70 overcompletion cuts; guide 7e77327d), from Joel's two result pages (his message of 11:19 UTC,
../joel-20261103-1119-message.txt: "recheck b https://www.pangram.com/feed/75baa67a-... recheck a
https://www.pangram.com/feed/4796254d-..."), read with tools/humanization/pangram_feed_read.js in compact mode in the app's
browser (WINDOWS-A/B.txt, META-A/B.json; each line's SHA-256 is the page's compact_sha256).

The text each page checked: part A's is ../TEXT-A.txt (the payload's first 99,999 characters); part B's is
../RENDERED-B.txt, TEXT-B.txt with the three differences the rendered draft showed (../RECHECK-POST-B.json). Each page's
text_sha256 is checked against them, and the windows against the text (no gap, no overlap, the page's word sums and counts).

  python3 articles/inner-signal/humanize/fix-20261103/free-whole/read/make_results.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
X = HERE.parent
ROOT = X.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

TEXTS = {'A': X / 'TEXT-A.txt', 'B': X / 'RENDERED-B.txt'}


def main():
    for part in ('A', 'B'):
        meta = json.loads((HERE / ('META-%s.json' % part)).read_text(encoding='utf-8'))
        compact = (HERE / ('WINDOWS-%s.txt' % part)).read_text(encoding='utf-8')
        text = TEXTS[part].read_text(encoding='utf-8')
        C.checked_text = lambda h, limit=99999, embeds=None, _t=text: _t
        d = C.result('', compact, meta)
        d['text_source'] = '%s, whose SHA-256 is the page\'s text_sha256' % TEXTS[part].name
        (HERE / ('RESULT-%s.json' % part)).write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        ai = [w for w in d['windows'] if w['label'].startswith('AI')]
        low = [w for w in d['windows'] if not w['label'].startswith('AI') and w['confidence'] == 'Low']
        print(part, d['headline'], '%.2f%% AI;' % (d['fraction_ai'] * 100), len(d['windows']), 'windows,', len(ai), 'AI,',
              len(low), 'Human (Low)')


if __name__ == '__main__':
    main()
