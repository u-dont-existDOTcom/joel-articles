"""RESULT-A.json and RESULT-B.json for the second recheck of 30 October (the tries; try 15 and try 13), from the windows and fields read off Joel's two result
pages (pangram_feed_read.js, compact: WINDOWS-A/B.txt and META-A/B.json) and the text rebuilt from each payload
(tools/humanization/substack_check_text.py).

Part B needs the two exceptions its paste showed (../RECHECK-POST-B.json, as in ../../recheck/RECHECK-POST-B.json): the embedded post's card line ("Quick Triage
Web-App Version HERE", in META-B.json's "embeds", as on 29 October), and the straight quote after "(" in his R-561
example, which Substack's editor curled as a closing quote (the exception substack_check_text.py's notes describe from
the Inner Child guide's round 6). With both, the rebuilt text is RENDERED-B.txt and its SHA-256 is the page's.

  python3 articles/inner-signal/humanize/fix-20261030/tries/read/make_results.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
X = HERE.parent
ROOT = X.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

R561 = ('(“It’s good nobody loves me', '(”It’s good nobody loves me')


def main():
    for part in ('A', 'B'):
        meta = json.loads((HERE / ('META-%s.json' % part)).read_text(encoding='utf-8'))
        html = (X / ('PAYLOAD-%s.html' % part)).read_text(encoding='utf-8')
        compact = (HERE / ('WINDOWS-%s.txt' % part)).read_text(encoding='utf-8')
        if part == 'B':
            base = C.checked_text
            def patched(h, limit=99999, embeds=None, _base=base):
                t = _base(h, limit, embeds)
                assert t.count(R561[0]) == 1
                return t.replace(*R561)
            C.checked_text = patched
        d = C.result(html, compact, meta)
        if part == 'B':
            assert d['text'] == (X / 'RENDERED-B.txt').read_text(encoding='utf-8')
        (HERE / ('RESULT-%s.json' % part)).write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(part, len(d['windows']), 'windows', sum(w['label'].startswith('AI') for w in d['windows']), 'AI',
              d['headline'], round(d['fraction_ai'] * 100, 2), '% AI')


if __name__ == '__main__':
    main()
