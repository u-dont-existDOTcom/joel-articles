#!/usr/bin/env python3
"""questions_lint.py - fail the questions page when a question hides outside "Open questions" (2026-10-17).

Joel, 2026-10-16 23:38 UTC: "i have no been seeing the coming up section bc it's at the bottom... those coming up questions
also not numbered with options for some reason so harder to asnwser. why are questions about the sections that are now
finished still "coming up" rather than being asked before you move to next section?" The page said "Open questions: 0" while
"Coming up" held decisions about finished sections ("kept unless you say otherwise", "Say if you'd like either side changed",
"no answer needed"). UDA patterns/owner-questions-page.md keeps "Coming up" for work that is not a question yet.

The checks:
- the header's "Open questions: N" is the number of numbered questions (**🟣 NN. ...**) under "Open questions";
- every numbered question offers at least two lettered options ("- a) ...");
- nothing under "Coming up" asks for an answer: no question mark outside quotes, and none of the phrases that hand Joel a
  decision ("unless you say", "say if", "no answer needed", ...).

render_questions.py runs this and refuses to write the page when it fails.
Usage: python3 tools/questions_lint.py OWNER-QUESTIONS.md
"""
import re
import sys

ASKS = ('unless you say', 'say if', 'say otherwise', 'no answer needed', 'yours to write', 'yours to decide', 'fine by me',
        "if you'd rather", 'if you would rather', 'tell me if', 'let me know', 'your call', 'up to you')
QUOTED = re.compile(r'"[^"\n]*"|“[^”\n]*”|\([^()\n]*\?\)')


def sections(md):
    out = {}
    for part in re.split(r'(?m)^## ', md)[1:]:
        head, _, body = part.partition('\n')
        out[head.strip()] = body
    return out


def problems(md):
    out = []
    secs = sections(md)
    open_q = next((b for h, b in secs.items() if h.startswith('Open questions')), None)
    coming = next((b for h, b in secs.items() if h.startswith('Coming up')), '')
    if open_q is None:
        return ['no "Open questions" section']
    if list(secs)[0] != next(h for h in secs if h.startswith('Open questions')):
        out.append('"Open questions" has to be the first section')
    qs = re.findall(r'(?m)^\*\*🟣 (\d+)\. ', open_q)
    m = re.search(r'Open questions: (\d+)', md.split('\n## ')[0])
    if not m:
        out.append('the header has no "Open questions: N"')
    elif int(m.group(1)) != len(qs):
        out.append('the header says %s open questions, and "Open questions" holds %d' % (m.group(1), len(qs)))
    blocks = re.split(r'(?m)^(?=\*\*🟣 \d+\. )', open_q)[1:]
    for b in blocks:
        n = re.match(r'\*\*🟣 (\d+)\.', b).group(1)
        opts = re.findall(r'(?m)^- ([a-z])\) ', b)
        if len(opts) < 2:
            out.append('question %s has %d lettered options ("- a) ..."); a question needs at least two' % (n, len(opts)))
    for item in re.findall(r'(?m)^- (.+)$', coming):
        bare = QUOTED.sub('', item)
        low = item.lower()
        hits = [a for a in ASKS if a in low]
        if '?' in bare or hits:
            out.append('"Coming up" asks for an answer (%s): %s. Make it a numbered question with options under "Open '
                       'questions", or decide it and report it under "Decided"' % (
                           ', '.join(hits + (['a question mark'] if '?' in bare else [])), item[:120]))
    return out


def main():
    md = open(sys.argv[1], encoding='utf-8').read()
    ps = problems(md)
    for p in ps:
        print('FAIL:', p)
    print('questions_lint: %s' % ('FAIL' if ps else 'PASS'))
    sys.exit(1 if ps else 0)


if __name__ == '__main__':
    main()
