#!/usr/bin/env python3
"""abstract_agents_prompt.py - the judgment step for the linter's O6 candidates (a feeling or idea doing what a person
does): a prompt that has a fresh agent sort each one into everyday speech, in between, or an AI quip.

Usage (from the repo root):
  python3 tools/humanization/abstract_agents_prompt.py DRAFT --out PROMPT.txt [--owner OWNER] [--report PATH]

  DRAFT    the text to judge (Markdown or plain text)
  --owner  the author's own lines, one per line or paragraph: the agent labels them too, marked as his, and proposes
           nothing for them
  --report where the agent writes its answer; without it, the agent returns it as its final message
  --out    the prompt file to write

Why (Joel, 2026-10-07 23:50 UTC, on the linter's parsed O6 flagging "Modern life trains us to perform competence"):
"'modern life trains us' is actually very human to say, so it seems we need an exception to the rule. not a brittle one.
you don't understand just intuitively which abstractions are normally used and which are not? like modern life trains
us... is so common it's almost cliche, it's not a witty AI quip, you know? i'm confused why you can't simply look at a
word and know it's an abstract concept, isn't that what LLMs are great at?" A script finds the grammar (an abstraction
as the subject of a person's verb); only a reader can tell an everyday phrase from a quip. So the linter collects
candidates and this prompt has an LLM judge them, with Joel's own ratings as the calibration. Nothing here is an
exception list: the agent judges every candidate, and reads the whole text for ones the script missed.

Give the prompt to a fresh agent: "Read PROMPT.txt and do what it says."
"""
import argparse, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tells_lint  # noqa: E402

CALIBRATION = HERE / 'calibration' / 'ABSTRACT-AGENTS-RATINGS-20261002.md'

INSTRUCTIONS = """You're judging sentences from an essay by Joel for one AI-writing tell: a feeling, an idea, a quality or another abstraction doing what a person does (wanting, deciding, answering, teaching, arriving, trying). The tell isn't the grammar. People give abstractions a person's moves all the time, and that is ordinary speech. The tell is the neat, efficient, quotable version, the line built to sound wise, which models write far more often than people do. Joel's words: "the usage of abstract concepts or feelings as agents is one AI tell because it permits high efficiency of words"; and on "Modern life trains us to perform competence": "actually very human to say ... so common it's almost cliche, it's not a witty AI quip".

Joel's own ratings follow (1 = a person would say it, 5 = AI). Judge the way he does.

{calibration}

For each numbered CANDIDATE below (found by a script that reads the grammar, so some are misreadings), write one line:
  N. EVERYDAY | BETWEEN | QUIP | NOT ONE - five to fifteen words on why
- EVERYDAY: the way people actually talk or write, including clichés, idioms, reported beliefs ("believing love can heal anyone") and plain description ("interest climbed sharply").
- BETWEEN: partly a neat line, partly ordinary (like "Nobody's status buys silence", which Joel left in).
- QUIP: polished, aphoristic, efficient; the abstraction is doing a person's job to make the line land ("Grief doesn't keep a schedule", "goodwill doesn't answer those questions").
- NOT ONE: the subject is a person or a group, or the script misread the sentence.
A line marked [JOEL'S] is the author's own: label it, but propose nothing.

Then, under "MISSED:", list any other sentence in THE TEXT where an abstraction does a person's job and you'd judge it BETWEEN or QUIP, quoted, with the same labels. Leave out the EVERYDAY ones there.

End with one line: the counts of QUIP and BETWEEN, candidates and missed together. Don't suggest rewrites."""

TAIL_RETURN = "Use no tools except reading this one file. Return your answer as your final message."
TAIL_WRITE = "Use no tools except reading this one file and writing your answer to {report} with one Write call. Then return it as your final message."


def candidates(text, owner=()):
    """The linter's O6 candidates: [(sentence, is_owner)], in order, by the parse when it's installed, else the list."""
    own = {re.sub(r'\s+', ' ', o).strip() for o in owner if o.strip()}
    out = []
    for p in tells_lint.paragraphs(tells_lint.clean(text)):
        for s in tells_lint.sentences(p):
            ag = tells_lint.abstract_agents(s)
            hit = ag if ag is not None else re.search(tells_lint.ABSTRACT_AGENT, s, re.I)
            if hit:
                flat = re.sub(r'\s+', ' ', s).strip()
                out.append((flat, any(flat in o for o in own)))
    return out


def build(text, owner=(), report=None):
    cal = CALIBRATION.read_text(encoding='utf-8').strip()
    cands = candidates(text, owner)
    listed = '\n'.join('%d. %s%s' % (i + 1, '[JOEL\'S] ' if mine else '', s) for i, (s, mine) in enumerate(cands)) or '(none)'
    tail = TAIL_WRITE.format(report=report) if report else TAIL_RETURN
    return (INSTRUCTIONS.format(calibration=cal) + '\n\nCANDIDATES:\n' + listed + '\n\nTHE TEXT:\n'
            + tells_lint.clean(text).strip() + '\n\n' + tail + '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('draft')
    ap.add_argument('--out', required=True)
    ap.add_argument('--owner')
    ap.add_argument('--report')
    a = ap.parse_args()
    owner = pathlib.Path(a.owner).read_text(encoding='utf-8').split('\n') if a.owner else ()
    p = build(pathlib.Path(a.draft).read_text(encoding='utf-8'), owner, a.report)
    out = pathlib.Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(p, encoding='utf-8')
    n = len(candidates(pathlib.Path(a.draft).read_text(encoding='utf-8')))
    print('%s: %d candidates, %d words%s' % (out, n, len(p.split()), '' if tells_lint.parser() else
                                             ' (no parser installed: the candidates come from the word list)'))


if __name__ == '__main__':
    main()
