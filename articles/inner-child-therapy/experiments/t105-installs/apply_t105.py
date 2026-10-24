#!/usr/bin/env python3
"""Turn 105: Joel's answer of 2026-10-24 18:40 UTC to 101.1 (experiments/t105-answers/JOEL-20261024-1840.md).

- 101.1: GPT's rewrite of 97.8's paragraph (When Escape Leaves Reality Behind), word for word as he pasted it, in place of
  mine ("it got human high conf on pangram"). It keeps every point of the guide's line 505 that the paragraph carried.
The changed paragraph gets a note above it. The script asserts the old text occurs once, so it can't run twice.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SRC = 'experiments/t105-answers/JOEL-20261024-1840.md'
OLD_START = 'Milder reactions afterward count as caution signs too'
GPT_978 = ("Say you keep coming back from trips confused or spaced out. Maybe nothing worse happens, but after several trips like "
           "that I'd be concerned. If you're having episodes when you're sober, or any of them are severe, see a psychiatrist. And "
           "don't suddenly stop a medication just because you suspect it's involved. Talk to the doctor who prescribed it. Benzos can "
           "be dangerous to quit cold turkey. Alcohol withdrawal can be dangerous if you're physically dependent.")


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')
    hits = [k for k, l in enumerate(lines) if l.startswith(OLD_START)]
    assert len(hits) == 1, hits
    k = hits[0]
    lines[k] = GPT_978
    lines[k:k] = ['<!-- Turn 105 (his answer of 2026-10-24 18:40 UTC, ' + SRC + '): 101.1, GPT\'s rewrite of my paragraph, word for word as he '
                  'pasted it ("GPT was able to fix that paragraph on its first try, it got human high conf on pangram"). It carries the guide\'s '
                  'line 505 points the paragraph had: repeated milder confusion or spacing out, help when it\'s severe or happens sober, and '
                  'no sudden stop of a medication or a substance the body depends on. What my four drafts got wrong is gate E256. -->', '']
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('applied: 101.1')


if __name__ == '__main__':
    main()
