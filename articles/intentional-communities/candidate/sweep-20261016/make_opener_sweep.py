"""The opener rule of 2026-10-16, swept over the installed sections (Joel, 18:22 UTC, on section 13's "How do you know?":
"what's that? know what? doesn't seem to follow..."; the lane's rule: each new rule is swept over the candidate sections in
the turn it's made). Builds two reader prompts from HUMANIZED-SO-FAR.md: sections 1 to 6 and 7 to 12, each paragraph
numbered under its section, Joel's own sentences in author marks (meaning_sweep.py: the owner-edits ledger and his texts in
joel-2026*/), and the rule's own words from tools/humanization/reviewer/sense_section.txt. Run from this folder:
python3 make_opener_sweep.py"""
import glob, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import meaning_sweep as ms  # noqa: E402

rule = (REPO / 'tools' / 'humanization' / 'reviewer' / 'sense_section.txt').read_text(encoding='utf-8')
rule = [p for p in rule.split('\n\n') if p.startswith("A paragraph's first sentence has to follow")][0].strip()
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
owners = ms.owner_strings(str(C / 'OWNER-EDITS.json'), sorted(glob.glob(str(C / 'joel-2026*' / '*.txt'))))
secs = ms.h1_sections(art)
BRIEF = '''You are reading part of a blog article about building intentional communities: {which}. Each section is given whole, its paragraphs numbered under it ([P1], [P2] ...), with any subheading where it falls.

Check one thing only, the first sentence of each paragraph:

{rule}

Text between {o} and {c} is the author's own; he wrote or approved it. Report nothing whose first sentence is inside those marks. A paragraph right after a subheading follows when it fits the subheading.

Write your report to `{report}` with one Write call: "# Openers" then, for each paragraph whose first sentence doesn't follow, one line: the section's first words, the paragraph number, the first sentence in quotes, and what a reader can't tell until reading on. If there are none, write "None." Read only this file. Reply with only the number of lines you reported.

{text}'''


def section_text(h, body):
    out, n = [h], 0
    for b in body.split('\n\n'):
        b = b.strip()
        if not b:
            continue
        if b.startswith('#'):
            out.append(b)
            continue
        n += 1
        out.append('[P%d] %s' % (n, ms.mark_author(b, owners)))
    return '\n\n'.join(out)


for name, rng in (('G1', range(0, 6)), ('G2', range(6, 12))):
    text = '\n\n----\n\n'.join(section_text(*secs[k]) for k in rng)
    which = 'sections %d to %d, %s to %s' % (rng[0] + 1, rng[-1] + 1, secs[rng[0]][0][2:], secs[rng[-1]][0][2:])
    p = BRIEF.format(which=which, rule=rule, o=ms.MARK_OPEN, c=ms.MARK_CLOSE, report=str(HERE / ('OPENERS-%s.md' % name)),
                     text=text)
    (HERE / ('OPENERS-PROMPT-%s.txt' % name)).write_text(p, encoding='utf-8')
    print(name, which, len(p.split()), 'words,', text.count(ms.MARK_OPEN), 'author marks')
