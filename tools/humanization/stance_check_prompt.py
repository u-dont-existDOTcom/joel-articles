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
  --images   a JSON file mapping an image's label ("image 7") to what it shows; such an image appears to the agent as
             "[an image: …]" instead of "[an image]"
  --positions  a text file of the author's positions stated since publication (dated, his words quoted); they win over
             the essay where the two differ (2026-10-07)
  --owner    a text file of the rewrite's paragraphs the author wrote himself (blank lines between them): his current
             position, never reported as conflicting with the published passage they replace (2026-10-07 20:21)
  --out      the prompt file to write

The agent also lists, separately, the places where the published text contradicts itself or the rest of the essay,
even where the rewrite fixed them (Joel, 2026-10-07 15:05, on a published paragraph that told children their words
carry weight and then said the teaching had nothing to do with dismissing a report: "Totally contradicting itself ...
The reviewer didn't notice that?").

Images carry content (Joel, 2026-10-02 23:49, on "These categories" in community section 4 P5: "they are the four parts
from the prior section. the actual article uses an image."). Three cold reads had flagged the four parts as never
named, because the prompts showed the diagram that names them as "[an image]". describe_images() is shared with the
other review prompts.

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
import argparse, json, pathlib, re

INSTRUCTIONS = """You're checking a rewrite of {scope} of an essay by {author} about {topic} against everything the published essay says. Some sentences in the rewrite were produced by a paraphrasing tool or by an editor, and a paraphrase can turn an author's position into its opposite without anyone noticing. It has happened: in another section of {author}'s essay on intentional communities, the published "distributed authority without pretending that people arrive emotionally finished" became "where people don't come in pre-healed", while the essay elsewhere tells readers to start their own healing practice first. {author} does want people to arrive largely healed, without pretending they're finished. Nobody caught it, because each check compared a paragraph only with its own published version.

Your job: for every sentence in THE REWRITE that states the author's position, a wish, a rule, an assessment of a community or a person, or a claim about how things work, check it against THE WHOLE PUBLISHED ESSAY, especially the parts the rewrite doesn't cover. Report every sentence that:
- contradicts or reverses something the essay says elsewhere;
- softens, strengthens or narrows a position the essay states elsewhere, in a way a reader would notice (a hedge such as "probably" or "may" dropped or added counts, and so does "should not automatically" becoming "must never");
- attributes to {author} a view, feeling, experience or fact the essay doesn't support (in the first person, or about people in his life);
- turns a personal practice or choice into a rule for the group, or a rule into a description, where the essay says otherwise.
- blurs the essay's specific claims into a vaguer general one: separate pairings (X becomes Y, A becomes B) turned into everything being "intertwined" with one thing counts as a changed claim, not lost detail.

For each, quote the rewrite's sentence, quote the essay's passage it conflicts with (and say which section that passage is in), and say in one line what a reader would wrongly come away believing. Don't report style, wording that keeps the meaning, or things that are merely missing. If a sentence is fine, don't list it. Don't suggest rewrites. Keep each quote under 25 words.

Then, in a separate part headed "Contradictions in the published text", list every place where the published version of {scope} contradicts itself (one sentence takes back what another says) or contradicts the rest of the essay, even where the rewrite has already fixed it, and say whether the rewrite still has it. The published text isn't the authority here: {author} wrote it with an AI's help, and has had to fix contradictions in it that every check before this one missed. On 2026-10-07 he found a published paragraph that said children's words carry weight, so they must learn to be honest, then said the teaching had nothing to do with dismissing a report: "Totally contradicting itself ... The reviewer didn't notice that?"{positions_job}

Keep the whole report under 1,500 words. Then end with one line: the number of conflicts you found in the rewrite, and the number of contradictions in the published text."""

POSITIONS_JOB = """

{author} has also stated positions since the essay was published (THE AUTHOR'S STATED POSITIONS, below the rewrite). They win over the essay where the two differ. Report a rewrite sentence that conflicts with one of them as a conflict like the others, and list a published passage that conflicts with one of them under the contradictions part. On 2026-10-07, a published sentence said a dangerous child's case needs review "that the home community does not control", and {author} answered: "Why should the home community not control the interaction they have with outside? That would violate my entire guide to force communities to accept outside intervention." """.rstrip()

OWNER_JOB = """

The paragraphs listed under THE AUTHOR'S OWN REWRITES (below the rewrite) are {author}'s own words, written after the essay was published: they are his current position. Don't report one of them as conflicting with the published version of the same passage, or with a published passage he cut. Before calling one narrower or weaker than the published text, check what it adds: a condition or a reason can be the explanation the published sentence lacked. Report one of them only where it conflicts with a part of the essay he hasn't rewritten, and put it as a question for him in a part of its own headed "Questions on the author's own paragraphs". On 2026-10-07 this check called his new paragraph narrower than the published one, and he answered: "you're wrong, it says more than the published version. The published version says the community can do much of the fathering, but why does it say that? doesn't explain. My version explains." """.rstrip()

TAIL_RETURN = "Use no tools except reading this one file: don't open, list or search anything else, don't run commands, and don't use the web. Return the report as your final message."
TAIL_WRITE = "Use no tools except reading this one file and writing your report to {report} with one Write call: don't open, list or search anything else, don't run commands, and don't use the web. Then return the report as your final message."


def describe_images(md, images=None):
    """Replace each image line with "[an image]", or "[an image: description]" when `images` describes it."""
    images = images or {}
    def one(m):
        d = images.get(m.group(1).strip())
        return '[an image: %s]' % d if d else '[an image]'
    md = re.sub(r'(?m)^\[(image \d+)\]\(.*?\)\s*$', one, md)
    return re.sub(r'(?m)^!\[([^\]]*)\]\(.*?\)\s*$', one, md)


def clean(md, images=None):
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    md = describe_images(md, images)
    return re.sub(r'\n{3,}', '\n\n', md).strip()


def build(essay, rewrite, scope='the rewritten sections', topic="the article's subject", author='Joel', report=None, images=None,
          positions=None, owner=None):
    """`positions`: the author's dated statements of his views, newer than the essay (2026-10-07), or None.
    `owner`: the paragraphs of the rewrite that the author wrote himself, one per paragraph, or None (2026-10-07 20:21)."""
    pj = (POSITIONS_JOB.format(author=author) if positions else '') + (OWNER_JOB.format(author=author) if owner else '')
    head = INSTRUCTIONS.format(scope=scope, author=author, topic=topic, positions_job=pj)
    tail = TAIL_WRITE.format(report=report) if report else TAIL_RETURN
    stated = ("THE AUTHOR'S STATED POSITIONS (newer than the essay):\n" + positions.strip() + '\n\n') if positions else ''
    own = ("THE AUTHOR'S OWN REWRITES (his words; they appear in the rewrite above too):\n" + clean(owner, images) + '\n\n') if owner else ''
    return (head + '\n\nTHE WHOLE PUBLISHED ESSAY:\n' + clean(essay, images) + '\n\nTHE REWRITE (' + scope + '):\n'
            + clean(rewrite, images) + '\n\n' + stated + own + tail + '\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--essay', required=True)
    ap.add_argument('--rewrite', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--scope', default='the rewritten sections')
    ap.add_argument('--topic', default="the article's subject")
    ap.add_argument('--author', default='Joel')
    ap.add_argument('--report')
    ap.add_argument('--images', help='JSON: image label -> what it shows')
    ap.add_argument('--positions', help="a text file of the author's stated positions since publication, dated, his words quoted")
    ap.add_argument('--owner', help="a text file of the rewrite's paragraphs the author wrote himself")
    a = ap.parse_args()
    p = build(pathlib.Path(a.essay).read_text(encoding='utf-8'), pathlib.Path(a.rewrite).read_text(encoding='utf-8'),
              a.scope, a.topic, a.author, a.report,
              json.loads(pathlib.Path(a.images).read_text(encoding='utf-8')) if a.images else None,
              pathlib.Path(a.positions).read_text(encoding='utf-8') if a.positions else None,
              pathlib.Path(a.owner).read_text(encoding='utf-8') if a.owner else None)
    out = pathlib.Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(p, encoding='utf-8')
    print('%s: %d words' % (out, len(p.split())))


if __name__ == '__main__':
    main()
