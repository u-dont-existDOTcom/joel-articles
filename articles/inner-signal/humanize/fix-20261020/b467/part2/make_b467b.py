"""Batch 467g, part 2 (2026-10-20): the fixes from part B of the whole guide's 4.1 reading (substack41/RESULT-41b.json):
one instruction in Appendix D (HG33, "Reduced breathing / Buteyko-style breathing") and the signpost question with its
colon list in Appendix F (HG35, "Forgiveness without bypass"). Built the same way as ../make_b467.py (which it imports),
into this folder.

  python3 articles/inner-signal/humanize/fix-20261020/b467/part2/make_b467b.py   (from the repo root)
"""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import make_b467 as M  # noqa: E402

M.OUT = HERE
M.EDITS = [
    {'key': 'HG33-buteyko-e', 'section': 'HG33', 'kind': 'edit',
     'old': "Inhale small amounts through your nose, exhale quietly through it, and pause only if comfortable.",
     'new': "Breathe in small amounts through your nose and let it out quietly, through your nose too. Only pause if that's "
            "comfortable.",
     'window': 'part B 12 (AI-Generated, Low, 15 words)',
     'diagnosis': 'pattern 4: three steps in one parallel list ("Inhale ..., exhale ..., and pause ..."); two sentences of '
                  'different shapes, every step and the caution kept'},
    {'key': 'HG35-forgive-e2', 'section': 'HG35', 'kind': 'edit',
     'old': "We simply remember that it can all be true: the harm happened, the boundary still matters, the person is still "
            "accountable, and forgiveness may come later on its own.",
     'new': "We just remember that it can all be true at once. The harm happened, and the boundary still matters. The person is "
            "still accountable, and forgiveness may come later on its own.",
     'window': 'part B 19 (AI-Generated, Low, 8 words) and 20 (AI-Generated, High, 29 words)',
     'diagnosis': 'pattern 4: a colon list of four parallel clauses after "We simply remember that"; the four points in two '
                  'sentences of two points each, "simply" said the way the guide says it ("just"). The question before it '
                  'stays: round 1 cut it, the march found the paragraph left with no break (r1/march.json) and the meaning '
                  'check found its framing lost (r1/VERIFY.md); it read red only at low confidence, so the list is taken to be '
                  'what made the run AI'},
]
M.SECTIONS = {'HG33': 'Appendix D: Anxiety — body first', 'HG35': 'Appendix F: Self-trust, outside guidance, and oracle-like states'}

if __name__ == '__main__':
    M.main()
