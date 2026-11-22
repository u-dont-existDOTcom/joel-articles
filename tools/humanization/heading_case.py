#!/usr/bin/env python3
"""heading_case.py - every heading in AP title case, and the headings that don't follow it.

Lesson inner-child-2026-11-20j. Joel, 2026-11-20 22:32 UTC: "Earning Trust, Day to Day should be title case... i mean,
there should be a rule that the headings follow. I'm still not sure what the best rule is but they should follow a rule."
The rule is the Associated Press's (the one his headings already mostly follow: "Journal With Each Hand", "Ask God for a
Loan", "If You Want to Kill Yourself"): capitalize every word except articles (a, an, the) and conjunctions and
prepositions of three letters or fewer (and, but, for, if, nor, or, so, yet, as, at, by, in, of, off, on, per, to, up,
via); those are lower case unless they are the first or last word, or start what follows a colon. Words of four letters
or more ("With", "From", "Into") are capitalized. A word with capitals inside it (AI, IFS, iPhone) is left as it is, and
so is the part of a hyphenated word after the hyphen ("Re-do", "Chicken-and-Egg").

"in", "on", "up", "off" and "by" can also be part of a verb ("Dip Your Toes In First", "Show Up Just for Joy"), and
"so" and "yet" can be adverbs ("And So That's the Way It Happened!"); then they are capitalized. The code can't tell which, so it lists those as AMBIGUOUS: a reader decides (AGENTS.md, "Method
fit": code finds the candidates, meaning goes to a reader).

  python3 tools/humanization/heading_case.py "Earning trust, day to day"     # prints the AP title case
  python3 tools/humanization/heading_case.py --catalog SECTION-LINKS.json     # every heading that doesn't follow it
"""
import argparse
import json
import pathlib
import re
import sys

MINOR = {'a', 'an', 'the', 'and', 'but', 'for', 'if', 'nor', 'or', 'so', 'yet', 'as', 'at', 'by', 'in', 'of', 'off',
         'on', 'per', 'to', 'up', 'via', 'vs', 'vs.'}
PARTICLE = {'in', 'on', 'up', 'off', 'by', 'so', 'yet'}   # also adverbs: "And So That's...", "Not Yet"
WORD = re.compile(r"[A-Za-z][A-Za-z'’]*")


def _cap(w):
    return w[0].upper() + w[1:]


def title_case(heading):
    """(AP title case of the heading, [ambiguous words left as written])."""
    tokens = re.split(r'(\s+)', heading.strip())
    words = [i for i, t in enumerate(tokens) if WORD.search(t)]
    out, ambiguous = list(tokens), []
    for n, i in enumerate(words):
        tok = tokens[i]
        m = WORD.search(tok)
        word = m.group(0)
        first, last = n == 0, n == len(words) - 1
        after_colon = n > 0 and re.search(r'[:.?!]["”’)]*$', tokens[words[n - 1]])
        lead = tok[:m.start()]
        quoted_start = bool(re.search(r'["“‘(]$', lead))
        if any(c.isupper() for c in word[1:]):
            continue                                    # AI, IFS, iPhone
        low = word.lower()
        if low in MINOR and not (first or last or after_colon or quoted_start):
            if low in PARTICLE and word[0].isupper():
                ambiguous.append(word)                  # leave it: verb particle or preposition?
                continue
            new = low
        else:
            new = _cap(word)
        out[i] = tok[:m.start()] + new + tok[m.end():]
    return ''.join(out), ambiguous


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('heading', nargs='?')
    ap.add_argument('--catalog', help="an article's SECTION-LINKS.json")
    args = ap.parse_args(argv)
    if args.heading:
        new, amb = title_case(args.heading)
        print(new + ('    AMBIGUOUS: ' + ' '.join(amb) if amb else ''))
        return 0
    cat = json.loads(pathlib.Path(args.catalog).read_text(encoding='utf-8'))
    changes = 0
    for h in cat['headings']:
        new, amb = title_case(h['text'])
        if new != h['text'] or amb:
            changes += new != h['text']
            print('%s  %s  ->  %s%s' % (h.get('id', ''), h['text'], new, ('    AMBIGUOUS: ' + ' '.join(amb)) if amb else ''))
    print('%d heading(s) to change' % changes)
    return 1 if changes else 0


if __name__ == '__main__':
    sys.exit(main())
