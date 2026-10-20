#!/usr/bin/env python3
"""pangram41_risk_prompt.py - the prompt for a Pangram 4.1 risk read of a stretch of an article (2026-10-20).

Joel, 2026-10-20 22:01 UTC, after his and GPT's edits of the community article for Pangram 4.1: "you should learn from that
what pangram 4.1 is now calling AI, altho many of those AI windows were not detected in smaller segments, only in the full
article". The brief (tools/humanization/reviewer/pangram41_risk.md) gives a reader the patterns 4.1 marked red in his
articles, with their examples, and asks which sentences of the given text it expects red or light green, section by
section. The read is a forecast to write predictions from and to point the editor at, never a reason to skip a check, and
its lists grow when a lane learns a new 4.1 pattern.

  python3 tools/humanization/pangram41_risk_prompt.py INPUT.md PROMPT.txt --report REPORT.md --what "the hypnosis guide, part 1 of 5"

INPUT.md holds the stretch as Markdown, each section under its "#" heading, at most about 2,000 words (four Sonnet readers
given 6,800 words each spent their whole output reasoning and wrote nothing, 2026-10-20). Words allowed in the report: 100 per 1,000 words
of input, at least 400 (the report quotes each flagged sentence).
"""
import argparse, pathlib, re

BRIEF = pathlib.Path(__file__).resolve().parent / 'reviewer' / 'pangram41_risk.md'


def prompt(input_path, report, what):
    brief = re.sub(r'<!--.*?-->\n*', '', BRIEF.read_text(encoding='utf-8'), flags=re.S)
    words = max(400, 100 * len(pathlib.Path(input_path).read_text(encoding='utf-8').split()) // 1000)
    return (brief.replace('{what}', what).replace('{input}', str(input_path)).replace('{report}', str(report))
            .replace('{words}', str(words)))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('input')
    ap.add_argument('out')
    ap.add_argument('--report', required=True)
    ap.add_argument('--what', required=True)
    a = ap.parse_args(argv)
    pathlib.Path(a.out).write_text(prompt(pathlib.Path(a.input).resolve(), pathlib.Path(a.report).resolve(), a.what),
                                   encoding='utf-8')
    print(a.out)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
