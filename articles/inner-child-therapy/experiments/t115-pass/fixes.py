#!/usr/bin/env python3
"""Turn 115: the one pass Joel asked for (2026-10-26 12:24 UTC: "try to get it all high conf human with one more pass, then
whatever remains you can just give me as highlighted in a docx so i can see what to work on directly").

The method is turn 93's, which he set (his answer to question 83, 2026-10-22 19:01 UTC): I find the tells in my own
paragraphs and take them out, adding nothing. Each item names its round-8 windows (experiments/t115-results/WINDOWS.json),
the tell (docs/HUMANIZATION-GATE.md, "What Pangram 4.1 flagged") and the change: a cut where the sentence restates, sums up
or reassures, or where another line already says it; otherwise its point said once, plainly, about the people. His words,
and the version of Untangling the Belonging Bargains he approved word for word, are left for him: the docx highlights them.

The fixes that read High-confidence Human when checked (experiments/t115-api/) go in, each with a turn-115 note, and the
docx shows them as tracked changes he can reject. One fix is a suggestion only, because it is in a paragraph he approved
as it is (OWNER-EDITS.json, entry c2-after-c1): SUGGEST below, a comment in the docx. A cut adds no words, so it is
outside the owner-delivery gate; a reworded paragraph goes through it (experiments/t115-gate/).

Order of work: AI windows, then Low, then Medium below 0.985 calibrated confidence. Medium windows at 0.985 or above
(High starts near 0.99) stay as they are and are highlighted as nearly High.

  fixes.py      writes CANDIDATE-ARTICLE.md (the installed guide with every fix in) and FIXES.json (with SUGGEST)"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'

FIXES = [
    # ---- AI windows ----
    dict(id='F02', pid='p16', kind='reword', where='Borrow Love P4 (after his Solomon\'s paradox paragraph)',
         block='Borrow Love—or Borrow the Perspective of Care',
         windows='r8w022 AI, Low (0.668), its first two sentences; r8w023 Human, Medium (0.933), "That\'s how you learn as a kid, and it works now, too."',
         round6='Human, Medium and Human, High: these words read lower in round 8 with his new paragraph before them',
         tells='an instruction wrapped in an image ("hand it to yourself"), filler ("then for now just try"), the example packaged as '
               '"If the advice was ..." and a reassuring follow-up ("and it works now, too")',
         old="Then take a small piece of whatever you'd tell them and hand it to yourself. If the advice was \"get more sleep,\" then for now just try brushing your teeth before midnight instead of at two. That's how you learn as a kid, and it works now, too. The technical term",
         new="Then take a small piece of whatever you'd tell them and do it yourself. If it's \"get more sleep,\" that could be brushing your teeth before midnight instead of at two. The technical term",
         keeps='the step (one small piece of the advice you\'d give them, done yourself), the sleep example with its numbers, and scaffolding with its link',
         loses='"That\'s how you learn as a kid, and it works now, too." The scaffolding link says what it said: small steps are how people learn.'),
    dict(id='F04', pid='p36', kind='reword', where='If You Want to Kill Yourself P1 (safety)',
         block='If You Want to Kill Yourself',
         windows='r8w048 Human, Low (0.503) "Can\'t tell if that\'s you?"; r8w049 to r8w051 AI, Low (0.503 to 0.595), its last three sentences',
         round6='Human, Low: the same words, unchanged since',
         tells='a question answered with a short knock-down ("Can\'t tell if that\'s you? Treat it like it is."), and a disclaimer '
               'followed by a reframe ("None of that is me answering ... It just keeps ..."), the not-X, it-just-Y shape',
         old="Do the same if you can't stop yourself, or you're badly disoriented or intoxicated. Can't tell if that's you? Treat it like it is. None of that is me answering whether life is worth living. It just keeps the question open long enough to look at.",
         new="Do the same if you can't stop yourself, and also when you're badly disoriented or intoxicated, or can't tell whether any of this is you. Getting safe first keeps the question of whether life is worth living open long enough to look at.",
         keeps='every safety instruction and its order; the grounding\'s MUSTs (a crisis line counts; if you can\'t tell whether it\'s you, '
               'do the same, as if it is); his guide\'s two points, that this isn\'t an answer to whether life is worth living and that it keeps the question open long enough to look at',
         loses='nothing; "That isn\'t my answer" is now said by "keeps the question ... open"'),
    # ---- Low windows ----
    dict(id='F01', pid='p15', kind='cut', where='Borrow Love P2', block='Borrow Love—or Borrow the Perspective of Care',
         windows='r8w021 Human, Low (0.829) "And if nothing moves at all, don\'t push it."; r8w020 Human, Medium (0.980) "Watch how it lands, though." stays',
         round6='Human, Medium',
         tells='a short tidy instruction between the image and the reassurance, the shape image, advice, comfort',
         old="who's just sitting there. And if nothing moves at all, don't push it. Knowing that love",
         new="who's just sitting there. Knowing that love",
         keeps='the aunt and the uncle (the one who just sits there is the one the child climbs on: no pushing), and "Knowing that love is in you somewhere counts for a lot", which is what counts when nothing moves',
         loses='the words "don\'t push it", which the aunt and the uncle already show'),
    dict(id='F03', pid='p22', kind='cut', where="Love Doesn't Have to Wait for Trust P7",
         block="Love Doesn't Have to Wait for Trust ❤️",
         windows='r8w030 Human, Low (0.503), its second and third sentences; r8w031 Human, Low (0.848) "The complaint might only be one sentence, once the swearing runs out."',
         round6='Human, Low and Human, High',
         tells='a short balanced instruction ("If it\'s something serious, answer it seriously.") and a tidy prediction that the next sentence explains anyway',
         old="without fighting the yelling and swearing around it. If it's something serious, answer it seriously. The complaint might only be one sentence, once the swearing runs out. Like the anger",
         new="without fighting the yelling and swearing around it. Like the anger",
         keeps='listening for the concrete complaint without fighting the swearing, and why the swearing stops; answering what\'s serious is said by P5 ("take whatever\'s true in the anger seriously") and shown by Mr. Rogers in the next paragraph ("he does answer what\'s worth answering in it")',
         loses='the hedged prediction that the complaint might only be one sentence, which nothing relies on (the three reviewers\' note: the record first said nothing was lost)'),
    dict(id='F05', pid='p55', kind='reword', where="Write It. Don't Send It Yet., its last paragraph",
         block="Write It. Don't Send It Yet.",
         windows='r8w076 Human, Low (0.868) "What felt scared when I wrote it can read like a threat from over there."',
         round6='Human, Low',
         tells='a balanced inversion closer (felt scared here, reads like a threat over there)',
         old="What felt scared when I wrote it can read like a threat from over there.",
         new="Stuff I wrote while I was scared can sound like a threat to them.",
         keeps='the reason to read it as them: what was fear when you wrote it can land as a threat',
         loses='nothing'),
    dict(id='F06', pid='p59', kind='reword', where='How to Forgive Without Forgetting P3', block='How to Forgive Without Forgetting',
         windows='r8w082 Human, Low (0.855) "Seeing how they got there doesn\'t make it okay."; r8w081 Human, Medium (0.961), its first sentence; r8w083 Human, Medium (0.984) stays',
         round6='Human, Low and Human, Medium',
         tells='a short knock-down sentence after a balanced "still ... still" sentence',
         old="They still have to answer for what they did, and it still hurt. Seeing how they got there doesn't make it okay. It's just that",
         new="They still have to answer for what they did, and it still hurt, even if you see how they got there. It's just that",
         keeps='accountability, the hurt, and that understanding how they got there doesn\'t excuse it, said about the people in one sentence',
         loses='nothing'),
    dict(id='F07', pid='p63', kind='cut', where='You Are Worthy of Love. Always.', block='You Are Worthy of Love. Always.',
         windows='r8w088 Human, Low (0.829) "That\'s easy to lose sight of when you\'ve spent so long looking at them."; r8w089 Human, Medium (0.909) "And you aren\'t alone."; r8w087 Human, Medium (0.989), his guide\'s "You are more than your pain and your past.", stays',
         round6='Human, Low',
         tells='a follow-up that explains the line before it, and a short reassurance the next sentence says concretely',
         old="You are more than your pain and your past. That's easy to lose sight of when you've spent so long looking at them. And you aren't alone. There's help",
         new="You are more than your pain and your past. There's help",
         keeps='his guide\'s line, being patient and gentle, and that there\'s help and other people doing the same work (you aren\'t alone)',
         loses='the explanation of why that\'s hard to see, and "And you aren\'t alone.", which the next sentence says concretely'),
    # ---- Medium windows below 0.985 ----
    dict(id='F08', pid='p03', kind='cut', where='Five Stages of Reparenting, after the stages', block='Five Stages of Reparenting',
         windows='r8w005 Human, Medium (0.950) "The cushion was practice for it."; r8w004 Human, Medium (0.982) "Say your boss asks you to stay late again." stays',
         round6='Human, Medium',
         tells='an aphoristic closer that sums up',
         old="nobody had to cry on a meditation cushion for that to happen. The cushion was practice for it.",
         new="nobody had to cry on a meditation cushion for that to happen.",
         keeps='that reparenting goes on in ordinary life, and the boss example',
         loses='the cushion\'s credit as practice for that moment'),
    dict(id='F09', pid='p10', kind='cut', where="If the Love Isn't Coming Yet P1", block="If the Love Isn't Coming Yet",
         windows='r8w013 Human, Medium (0.986) "That doesn\'t close the door, though, it just means you start smaller."',
         round6='Human, Medium',
         tells='"not X, it just Y" (it doesn\'t close the door, it just means)',
         old="That doesn't close the door, though, it just means you start smaller.",
         new="That just means you start smaller.",
         keeps='feeling none of the warmth means starting smaller, a way in that stays open',
         loses='the words "doesn\'t close the door", which "you start" still says'),
    dict(id='F10', pid='p12', kind='reword', where='Remember When You Already Did It', block='Remember When You Already Did It',
         windows='r8w015 Human, Medium (0.981) "Maybe you\'re more worn out now, or missing whatever helped back then. (No example? Try another doorway.)"',
         round6='Human, Medium',
         tells='a question answered with a short knock-down, in parentheses',
         old="(No example? Try another doorway.)",
         new="(If no example comes to mind, try another doorway.)",
         keeps='the pointer to the other doorways for a reader with no example; "Maybe you\'re more worn out now ..." stays, the grounding\'s point that past strength doesn\'t cancel today\'s limits',
         loses='nothing'),
    dict(id='F11', pid='p13', kind='cut', where='Notice the Part That Came Here P1', block='Notice the Part That Came Here',
         windows='r8w016 Human, Medium (0.943) "I hate myself." If that\'s what you find, it deserves an honest hearing. Just listen to it, without arguing back."',
         round6='Human, Medium',
         tells='a stock phrase ("deserves an honest hearing") and a follow-up that restates it',
         old="If that's what you find, it deserves an honest hearing. Just listen to it, without arguing back.",
         new="If that's what you find, just listen to it, without arguing back.",
         keeps='listening to the "I hate myself" part without arguing back, which is what an honest hearing is',
         loses='nothing'),
    dict(id='F12', pid='p14', kind='cut', where='Notice the Part That Came Here P2', block='Notice the Part That Came Here',
         windows='r8w019 Human, Medium (0.974) "You don\'t need to decide which."',
         round6='Human, Medium',
         tells='a reassuring permission ("You don\'t need to ...") between the list and the step',
         old="And maybe it was love. You don't need to decide which. Ask that part",
         new="And maybe it was love. Ask that part",
         keeps='the list of what brought you here, and asking that part what it hoped for, which needs no decision first',
         loses='the explicit permission'),
]

# a suggestion only: Joel approved this paragraph as it is (OWNER-EDITS.json, c2-after-c1), so the docx comments on it
SUGGEST = [
    dict(id='F13', pid='p49', kind='cut', where='Opening up honestly to the right people at the right pace P1',
         block='Opening up honestly to the right people at the right pace',
         windows='r8w066 Human, Medium (0.975) "And reaching out doesn\'t mean telling strangers everything. Privacy isn\'t fakery."; r8w067 Human, Medium (0.955) stays (the danger line is a safety line)',
         round6='Human, Medium',
         tells='an aphorism that sums up ("Privacy isn\'t fakery.")',
         old="telling strangers everything. Privacy isn't fakery. People can earn",
         new="telling strangers everything. People can earn",
         keeps='that you don\'t tell strangers everything, and the contrast with keeping up a fake version of yourself, which the paragraph makes later in its own words',
         loses='the four-word summary'),
]


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def apply(md):
    for f in FIXES:
        assert md.count(f['old']) == 1, (f['id'], md.count(f['old']))
        md = md.replace(f['old'], f['new'])
    return md


def main():
    md = ART.read_text(encoding='utf-8')
    new = apply(md)
    (HERE / 'CANDIDATE-ARTICLE.md').write_text(new, encoding='utf-8')
    out = {'article_sha256': sha(md), 'candidate_sha256': sha(new), 'fixes': FIXES, 'suggest': SUGGEST}
    (HERE / 'FIXES.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for f in FIXES:
        def words(t):
            return [re.sub(r'^\W+|\W+$', '', w).lower() for w in t.split()]
        added = [w for w in words(f['new']) if w not in words(f['old'])]
        print('%s %-6s %-48s new words: %s' % (f['id'], f['kind'], f['where'][:48], ' '.join(added) or '-'))
        if f['kind'] == 'cut':
            assert not added, f['id']


if __name__ == '__main__':
    main()
