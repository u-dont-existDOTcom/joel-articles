#!/usr/bin/env python3
"""stance_check_prompt.py - the whole-article stance check: a prompt that has a fresh agent check a rewrite against
everything the published article says.

Usage (from the repo root):
  python3 tools/humanization/stance_check_prompt.py --essay PUBLISHED.md --rewrite REWRITE.md --out PROMPT.txt
          [--scope TEXT] [--topic TEXT] [--author NAME] [--report PATH]

  --essay    the whole published article (Markdown); image links become "[an image]"
  --rewrite  the rewritten sections being checked (Markdown; HTML comments are dropped)
  --scope    what the rewrite covers, for the agent: default "the rewritten sections"
  --topic    the article's subject, in a few words: default "the article's subject"
  --author   default "Joel"
  --report   where the agent writes its report; without it, the agent returns the report as its final message
  --out      the prompt file to write

Give the prompt to a fresh agent (Opus) that hasn't seen the drafting: "Read PROMPT.txt and do what it says."
Run it before any Pangram call on a candidate, and again after any edit that changes what a sentence claims.

Why (Joel, 2026-10-02 00:52, on the community article's section 3): "Emulate changed 'without pretending that
people arrive emotionally finished' into 'where people don't come in pre-healed' which is nearly the opposite of
what i want. I DO want people to come in largely pre-healed, which is why I talk about that in the article. Did the
reviewers not look at the article?" The blind trace compared each paragraph only with its own published version,
and flagged the change as a shift; the cold read saw only the section; the grounding reviewer had the whole article
and missed it; and the gate's stance-ledger step had been skipped. This check gives one agent a single job: hold
each stance-bearing sentence of the rewrite against the whole published article. Its first run, over sections 1
to 3, found no other reversal.
"""
import argparse, pathlib, re

INSTRUCTIONS = """You're checking a rewrite of {scope} of an essay by {author} about {topic} against everything the published essay says. Some sentences in the rewrite were produced by a paraphrasing tool or by an editor, and a paraphrase can turn an author's position into its opposite without anyone noticing. It has happened: in another section of {author}'s essay on intentional communities, the published "distributed authority without pretending that people arrive emotionally finished" became "where people don't come in pre-healed", while the essay elsewhere tells readers to start their own healing practice first. {author} does want people to arrive largely healed, without pretending they're finished. Nobody caught it, because each check compared a paragraph only with its own published version.

Your job: for every sentence in THE REWRITE that states the author's position, a wish, a rule, an assessment of a community or a person, or a claim about how things work, check it against THE WHOLE PUBLISHED ESSAY, especially the parts the rewrite doesn't cover. Report every sentence that:
- contradicts or reverses something the essay says elsewhere;
- softens, strengthens or narrows a position the essay states elsewhere, in a way a reader would notice (a hedge such as "probably" or "may" dropped or added counts, and so does "should not automatically" becoming "must never");
- attributes to {author} a view, feeling, experience or fact the essay doesn't support (in the first person, or about people in his life);
- turns a personal practice or choice into a rule for the group, or a rule into a description, where the essay says otherwise.

For each, quote the rewrite's sentence, quote the essay's passage it conflicts with (and say which section that passage is in), and say in one line what a reader would wrongly come away believing. Don't report style, wording that keeps the meaning, or things that are merely missing. If a sentence is fine, don't list it. Don't suggest rewrites. Keep each quote under 25 words.

Keep the whole report under 1,200 words. Then end with one line: the number of conflicts you found."""

TAIL_RETURN = "Use no tools except reading this one file: don't open, list or search anything else, don't run commands, and don't use the web. Return the report as your final message."
TAIL_WRITE = "Use no tools except reading this one file and writing your report to {report} with one Write call: don't open, list or search anything else, don't run commands, and don't use the web. Then return the report as your final message."


def clean(md):
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    md = re.sub(r'(?m)^\[image \d+\]\(.*?\)\s*$', '[an image]', md)
    md = re.sub(r'(?m)^!\[[^\]]*\]\(.*?\)\s*$', '[an image]', md)
    return re.sub(r'\n{3,}', '\n\n', md).strip()


def build(essay, rewrite, scope='the rewritten sections', topic="the article's subject", author='Joel', report=None):
    head = INSTRUCTIONS.format(scope=scope, author=author, topic=topic)
    tail = TAIL_WRITE.format(report=report) if report else TAIL_RETURN
    return (head + '\n\nTHE WHOLE PUBLISHED ESSAY:\n' + clean(essay) + '\n\nTHE REWRITE (' + scope + '):\n'
            + clean(rewrite) + '\n\n' + tail + '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--essay', required=True)
    ap.add_argument('--rewrite', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--scope', default='the rewritten sections')
    ap.add_argument('--topic', default="the article's subject")
    ap.add_argument('--author', default='Joel')
    ap.add_argument('--report')
    a = ap.parse_args()
    p = build(pathlib.Path(a.essay).read_text(encoding='utf-8'), pathlib.Path(a.rewrite).read_text(encoding='utf-8'),
              a.scope, a.topic, a.author, a.report)
    out = pathlib.Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(p, encoding='utf-8')
    print('%s: %d words' % (out, len(p.split())))


if __name__ == '__main__':
    main()
