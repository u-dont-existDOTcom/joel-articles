"""Sections 15 and 16, exclamations, Joel's way (his 43 of 2026-10-17 17:16 UTC, joel-20261017/joel-20261017-1716-message.txt):
"you can't just change ! to . if the actual wording was put in as an exclamation. you can't change "That's it!" to "that's it."
... so either take out the exclamation phrases themselves, replace the exclamation marks alone only if it makes sense to, or ...
ask me ... if you feel that the exclamation isn't really fitting but it's needed to pass pangram, see if there's a better way."
Each change below says which of his three it is. Tried and taken back: "That's fine." for "That's fine!" (the tone check,
fix-20261017b/TONE-excl.md: on its own after the list of reasons it reads curt, the shape of his "That's it!" example), and
cutting "One disagreement is enough!" and "Really, go!" (each was its paragraph's only break in both march reads,
march-r1/, so the cut would make a paragraph of steps: what he means by fixing the structure, not the mark). Those two go to
him (question 47). And cutting "That's it!" (his own example): the tone check found the cut fine, but Pangram read the
paragraph with its neighbor 88% AI without it (415g, S16v29-H2P4+prev), so it's a real emphasis the paragraph needs: kept.
And "Less cinematic, I know." and "in one go.": each paragraph read Human, but section 16 read AI across the two (415g, a
94-word window from "It would be better to get together" to "a common purse"): back to "!", and to him with question 47,
since the window is the "and ... and ... and" list Emulate built (O14), which is his order in its words. Kept, as real reactions or his own: section 15's "And the humor!", "No, not
that either!", "Every morning!" (published), "they won't let me pay rent!"; section 16's quoted founders' lines ("First let's
get land!" ...), "money is impure!" (a quoted slogan), and his "studio apartments!" and "any of that!" (his 42).
Writes s15/v14.md and s16/v29.md from v13 and v28. Run from candidate/: python3 fix-20261017b/make_excl.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
CHANGES = {
    's15': [
        ('H1P2', 'period', 'I find them so soothing!', 'I find them so soothing.',
         'a calm feeling about the prayers; the sentence reads right with a period (published: "I find them deeply soothing.")'),
        ('H1P5', 'period', 'Spiritual graffiti still surprises me!', 'Spiritual graffiti still surprises me.',
         'it follows five quoted exclamations, and the next sentence says why it surprises him (published: a period)'),
        ('H2P6', 'period', 'Everybody here has sheep (even me!), and they are super cute!',
         'Everybody here has sheep (even me), and they are super cute.',
         'two in one sentence, between "Every morning!" and the sheep video\'s title; a plain statement reads right '
         '(published: "and they are extremely cute.")'),
        ('H3P4', 'period', 'but it does mean someone has to handle it!', 'but it does mean someone has to handle it.',
         'a point of logistics, not a reaction; the question after it ("Who\'s that going to be?") carries the turn'),
        ('H3P8', 'period', "and don't expect anyone to hand you a spiritual service package!",
         "and don't expect anyone to hand you a spiritual service package.",
         'advice; the "!" made it scold (published: "and do not arrive expecting a spiritual service package.")'),
    ],
    's16': [
        ('H2P5', 'period', 'Or a sauna!', 'Or a sauna.', 'deadpan reads right; the sauna is the joke'),
        ('H3P1', 'period', 'And practice before you have an audience!', 'And practice before you have an audience.',
         'advice (published: "Practice before you have an audience.")'),
    ],
}
SRC = {'s15': (C / 's15' / 'v13.md', C / 's15' / 'v14.md'), 's16': (C / 's16' / 'v28.md', C / 's16' / 'v29.md')}
for s, (src, dst) in SRC.items():
    md = src.read_text(encoding='utf-8')
    for where, kind, old, new, why in CHANGES[s]:
        assert md.count(old) == 1, (s, where, old)
        md = md.replace(old, new)
    dst.write_text(md, encoding='utf-8')
    print(dst.name, 'written:', md.count('!'), 'exclamation marks in the file')
(HERE / 'excl-changes.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
