#!/usr/bin/env python3
"""conflation_sweep_prompt.py - a whole-article sweep for the inner figures a reader could take for each other.

Joel, 2026-10-21 17:56 UTC, on the hypnosis guide: "i fixed another part a few paras later where you conflated the
different versions of the inner adult... so we should check the guide for that conflation bc i have seen it before as
well (and send this to the inner child guide chat to make sure also)". His fix changed "Because often your inherited
parent tells your inner child ... The adult in you can answer," to "Because often your inherited inner parent tells your
inner child ..., which is humiliating. The more consciously sculpted adult in you can answer,". Right after the
inherited parent, a bare "the adult in you" could be read as that same internalized voice.

The hypnosis guide's sweep (articles/inner-signal/humanize/fix-20261021/CONFLATION-SWEEP.md) found six more and the batch's
stance check one: four came in with plainer rewrites (a lowercased role right after a guard of the same name, "a 'grown up'
voice" for the published "new adult voice", a sign of vulnerability turned into a need for protection and sent to the
Nurturer, a script line with no addressee after the inherited parent's paragraph), three were in the published text (a
guard under the role's capital P). So every article that writes about the
inner child and its adults gets this sweep on the whole article before its final check, with its own map.

Usage (from the repo root):
  python3 tools/humanization/conflation_sweep_prompt.py --article ARTICLE.md --map MAP.txt --report REPORT.md --out PROMPT.txt

  --article  the article as it now stands (Markdown); the reader counts its blocks from 0 (B0, B1, ...), one per
             blank-line-separated block, headings and image markers included
  --map      the article's own map of its figures, in its own words, quoted with their block numbers: the internalized
             caregiver voice, the adult the reader builds (and its roles, if it has them), the protective parts
  --report   where the reader writes its findings
  --out      the prompt file to write

Give PROMPT.txt to a fresh Opus agent that reads only the article. Fix each finding in the article's own terms, with as
few words as possible, and give it its own Pangram check like any edit; a finding where either reading fits the author's
map goes to him.
"""
import argparse
import pathlib
import sys

EXAMPLE = ('Joel\'s own fix of 2026-10-21, the error to look for. The hypnosis guide said: "Because often your inherited '
           'parent tells your inner child that it is supposed to be good at something as soon as it starts doing it. ... '
           'The adult in you can answer, "We\'re finding out whether we enjoy this, not proving our worth."" He changed it '
           'to: "Because often your inherited inner parent tells your inner child that it is supposed to be good at '
           'something as soon as it starts doing it, which is humiliating. The more consciously sculpted adult in you can '
           'answer, ..." His words: "i fixed another part a few paras later where you conflated the different versions of '
           'the inner adult... so we should check the guide for that conflation bc i have seen it before as well". So: with '
           'the inherited parent just named, a bare "the adult in you" could be read as that same internalized parent '
           'voice; his fix names which adult answers (the one you consciously build), and calls the internalized voice the '
           '"inherited inner parent".')

KINDS = '''Find every place where:
(a) a bare "the adult", "your adult", "the adult in you/me", "adult self", "inner adult", "grown-up", "parent" or the like stands where the internalized caregiver voice is also in play nearby, so a reader could take it for either;
(b) "inner parent", "parenting", "parent" or the like is used for the adult the reader builds in a way a reader could take for the internalized voice, or the other way round;
(c) the internalized voice is given the built adult's qualities (care, protection, direction), or the built adult is given the internalized voice's (criticism, wardenship, old rules);
(d) a role of the built adult and a protective part of the same name are mixed so a reader can't tell which is meant (a capitalized role next to a lowercase part, "a Protector" for something that surfaces like a guard), or the roles are swapped for each other (a need one role meets sent to another);
(e) a line to say, or a script, has no addressee where the figure just named is not the one it is meant for.'''

BRIEF = '''You are checking an article by {author} for one specific kind of error: places where it confuses, or lets a reader confuse, the different inner figures of its own map of the mind. Read the article in full: {article} (Markdown; blocks are separated by blank lines; count blocks from 0 as B0, B1, ... in file order, every blank-line-separated block counting, headings and image markers included).

The article's map, in its own words:
{map}

{example}

{kinds}

Don't report a use that is clear in its context (an "adult in me" that is plainly the one the reader builds, with no internalized voice in play), and don't report style. For each finding give: the block number and its section heading; the exact sentence; which figures a reader could take it for and why (what nearby text makes it confusable); and the smallest fix in the article's own terms, changing as few words as possible. Say when either reading fits the map, so the author can decide. Then list the places you checked and found clear, one line each, so the sweep's coverage can be seen.

Write your report with a single Write call to {report}, then reply with only the number of findings. Don't open any other file, don't run commands, and don't use the web. Keep your reasoning short.
'''


def build(article, map_text, report, author='Joel'):
    if not map_text.strip():
        raise ValueError('the map is empty: give the article\'s own map of its figures, in its own words')
    return BRIEF.format(author=author, article=article, map=map_text.strip(), example=EXAMPLE, kinds=KINDS, report=report)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--article', required=True)
    ap.add_argument('--map', required=True)
    ap.add_argument('--report', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--author', default='Joel')
    a = ap.parse_args(argv)
    art = pathlib.Path(a.article).resolve()
    if not art.exists():
        print('no such article: %s' % art, file=sys.stderr)
        return 2
    try:
        prompt = build(str(art), pathlib.Path(a.map).read_text(encoding='utf-8'), str(pathlib.Path(a.report).resolve()),
                       a.author)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    pathlib.Path(a.out).write_text(prompt, encoding='utf-8')
    print('%d words -> %s' % (len(prompt.split()), a.out))
    return 0


if __name__ == '__main__':
    sys.exit(main())
