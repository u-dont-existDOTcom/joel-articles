#!/usr/bin/env python3
"""Turn 100: put in the four drafts that read 100% Human alone and in their stretch (experiments/t100-api/API-CHECKS.md).

- PGQ-046 (innerSignalGraph authoring/PENDING-PUBLIC-GUIDE-CHANGES.md, branch task/guide-semantic-review-20261022, his
  amendment AMEND.IC.COMPASSION_WITHOUT_REQUIRED_MISERY_20261022): turn 99's f01 with a new last sentence (g01) and turn 99's
  f02 unchanged, after his memoir paragraph in Untangling the Belonging Bargains and before the small good thing.
- The Inner Guide P5 (g02), When One Life Has Ended P1 (g03) and How This Relates to IFS P7 (g04), each in place of the
  paragraph that had a Low window in round 5, with a turn-100 note above it; the older notes stay.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
D = HERE.parent / 't100-tries' / 'drafts'
D99 = HERE.parent / 't99-tries' / 'drafts'
REC = 'experiments/t100-api/API-CHECKS.md'
read = lambda p: p.read_text(encoding='utf-8').strip()
H = 'https://www.pangram.com/history/'


def note(what):
    return '<!-- Turn 100 (Joel, 2026-10-23 12:28 UTC: "carry on from its next step"; ' + REC + '): ' + what + ' -->'


def main():
    text = ART.read_text(encoding='utf-8')
    lines = text.split('\n')

    def one(start):
        hits = [i for i, l in enumerate(lines) if l.startswith(start)]
        assert len(hits) == 1, (start, hits)
        return hits[0]

    edits = []
    i = one("That's exactly why I was crying for 14 years.")
    assert lines[i + 1] == '' and lines[i + 2].startswith('<!-- Turn 93') and lines[i + 4].startswith("I'd still try a small good thing")
    edits.append((i, 1, [lines[i], '', note(
        "PGQ-046, his amendment of 2026-10-22 (compassion without required misery), as two paragraphs after his memoir "
        "paragraph: his finding that cultivating his own happiness made him better at helping others toward theirs (not true "
        "for everyone, and unhappy people can still help), doing your part without having to be miserable; then the social "
        "loss taken seriously, what they do and what you owe them looked at before calling it envy. Turn 99's f01 read AI "
        "(Medium 27) on its last sentence, a three-part concession; g01 has a new last sentence. Alone 100% Human, " + H +
        "72df4253-a0b1-4895-921b-6fb88a762bbd; f02 alone 100% Human (turn 99), " + H + "5a276026-12c9-4528-8df4-93ddbf904692; "
        "both with the bargain line, his paragraph and the small good thing 100% Human, " + H + "2b561f5f-5956-4cef-b521-6b11efb84767."),
        '', read(D / 'g01-bargain-new1.txt'), '', read(D99 / 'f02-bargain-new2.txt')]))
    i = one('Once a need does show, after all that hiding')
    edits.append((i, 1, [note(
        "my fourth try at this paragraph, in place of turn 57's, whose \"The texts and the sulking aren't, and the Guide can "
        "help you find something ..., like a hug at the door and a 'see you in an hour.' But hear your little one out first.\" "
        "read Low 42 in rounds 4 and 5. The same points (wanting closeness is fine; the other person gets their walk; your little "
        "one heard first; the Guide finds a way for both of you) without the help-you-find-something-like-A-and-B shape. Alone "
        "100% Human, " + H + "5ee698a9-da9c-4ca9-80ee-9866cfab16ef; with P3, P4, his P6 and P7 Mostly Human (9.1% AI), "
        + H + "c101212c-912c-4223-a994-77b40547ae84, its only windows on the last three sentences of P7, the stretch's end "
        "(Human inside the halves of rounds 4 and 5), and this paragraph Human there."), '', read(D / 'g02-guide-P5.txt')]))
    i = one('Your little one can get really loud in the gap after one life ends')
    edits.append((i, 1, [note(
        "my third try at this paragraph, in place of the turn-65 one with his 77.6 helper line, which read Low 14 and Low 61 "
        "in round 5 from \"So can leaving\" on. The same list, the helper stepping back once you've grown (77.6, as a small "
        "scene), the stretch with no old you and no new one, and the bardo with its teachings left to you, without the chain "
        "of expository steps. Alone 100% Human, " + H + "50f027e5-f84e-47d9-bbc0-43ee045bea9c; the h1's heading, P1, P2 and "
        "P3 100% Human, " + H + "2e42b03b-65f0-4caf-955c-4c6863925169."), '', read(D / 'g03-ended-P1.txt')]))
    i = one('And the parts just keep coming: managers, firefighters')
    edits.append((i, 1, [note(
        "my fourth try at this paragraph, in place of turn 93's, whose last two sentences read Low 9 and Low 30 in round 5 and "
        "ran on into Related Clinical Work's first line (Low 14). The guide's point that a big institute doesn't make a model "
        "truer or safer, said once as my stance, with no pair. Alone 100% Human, " + H + "b7311406-1ae8-4279-8791-fa3e66734bb2; "
        "P3 to P7 of the section 100% Human, " + H + "c4e53e05-a8e2-4090-861c-abbf245babc5."), '', read(D / 'g04-ifs-P7.txt')]))
    for k, n, new in sorted(edits, reverse=True):
        lines[k:k + n] = new
    ART.write_text('\n'.join(lines), encoding='utf-8')
    print('installed: PGQ-046 (g01, f02), The Inner Guide P5 (g02), When One Life Has Ended P1 (g03), How This Relates to IFS P7 (g04)')


if __name__ == '__main__':
    main()
