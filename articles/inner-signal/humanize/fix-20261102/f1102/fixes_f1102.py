"""The windows of the whole guide's free check of 2 November (../free-whole/read/WINDOWS.md; Joel's two result pages,
his message of 21:57 UTC) that read AI or Human (Low), fixed: gate E306, every one, where a fix keeps his meaning and
form; E321's order first (a specific example; cut the closer; cut the summing up; fold the explanation in; join short
sentences; plain words), E324 (a run of short sentences of one shape is still a list; a joke-shaped or explaining closer
is still a closer), and what his two accounts' histories showed (E321, E326, E327).

Whose words (read_free1102.py, then read by the lead session against his published version and his inner child guide):
- OURS, fixed here and checked in place (each stretch of at most six paragraphs through the API, E325) before it goes in.
- CARDS (his words): his inner child guide's rent line (block 92) and his own Core prompts line (block 480), each with a
  suggestion checked the same way, for the owner-delivery gate and then his page; his Troubleshooting version of 20:38
  UTC (blocks 380 to 382), which he checked himself, as a stretch for him to look at (advice "edit"), no suggestion.
- KEPT: the four one-word windows of the countdown ("4.", "3.", "2.", "1."), which are list numbers.

  python3 articles/inner-signal/humanize/fix-20261102/f1102/fixes_f1102.py
Prints each edit; import it for EDITS and apply().
"""
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

GUIDE_SHA = 'a9b7061be2c0507a76eca9b74286c105838d81cf5b39d9a1290bc1c824decb27'

# (id, block, kind, old (exact, in the block's Markdown), new, why)
EDITS = [
    ('F-61', 61, 'ours',
     "The body can have a voice - saying yes or no or not yet. The imagination can open up the field, and then the adult can "
     "choose what to do next in the real world. You can be at peace and still be precise.",
     "Your body has its own yes and no, and sometimes a not yet. Your imagination can open things up before the adult in you "
     "decides what to do in real life.",
     'AI (Low) from the third "The X can ..." on: a run of one shape is a list (E324), and the closer "You can be at peace and '
     'still be precise." restates the first sentence\'s "warm and clear-headed at once" (E321: cut the closer); the body and '
     'the imagination folded into one sentence of another shape'),
    ('F-62', 62, 'ours',
     "Without the mind of love, the mind of analysis can be sterile. Without the mind of analysis, the mind of love can lead "
     "to fantasy. Without testing, intuitive signals can become delusions. Without intuitive signals, the testing can be "
     "dead. So these modes can correct each other.",
     "Analysis with no love in it gets sterile, and love that never stops to analyze anything drifts off into fantasy. The "
     "same goes for intuition and testing: signals you never test can turn into delusions, and testing with nothing "
     "intuitive to test is dead.",
     'Human (Low) on the first two and the last: four sentences of one frame ("Without X, Y can be Z") and a summing-up '
     'closer ("So these modes can correct each other."); two sentences of different shapes, his own "The same goes for" (his '
     'inner child guide has it), the closer cut since the pairs say it'),
    ('F-119', 119, 'ours',
     "Keep breathing gently through the whole practice. It works as an induction too: the Sober induction below has it as "
     "one of the anchors you can pick.",
     "Keep breathing gently the whole way through. The Sober induction below lists this practice as one of its anchors, so it "
     "works as an induction too.",
     'Human (Low) on the short instruction at the start; the next sentence said the other way round, its reason last, and '
     'without the coach phrases ("if you like", "you can pick") the linter counts (E41)'),
    ('F-216', 216, 'ours',
     "Anyone worth following leaves your adult self more present. The more powerful the state you’re in, the stronger the "
     "boundaries you’ll need.",
     "And afterwards: do I come away from them more present and grown up, or less? Be extra careful with all this when "
     "you’re in a deep or powerful state, because that’s when you need your boundaries most.",
     'Human (Low) on both maxims, the section\'s closers; the first said as one more question to ask yourself (F-216\'s '
     'question read Human in its section in w1102f), the second plainly, without the seatbelt simile that read AI (High) in '
     'the whole and without "the more ..., the more ..."'),
    ('F-361', 361, 'ours',
     "There is no need to learn a second script. The process is the same: gather your attention, notice what is here, "
     "respond, wait, and come all the way back. You are simply practicing for fifteen minutes or so.",
     "You don't need to learn a second script for this. It's the same process (gather your attention, notice what's here, "
     "respond, wait, and come all the way back), just for fifteen minutes or so.",
     'AI (Low) on all three: stiff ("There is no need", "You are simply practicing"), and three short sentences; joined, '
     'with contractions (E321)'),
    ('F-527', 527, 'ours',
     "Milton Model language opens things up, and Meta Model questions ask what exactly someone means. If you want to be "
     "ethical with people, you need both.",
     "Milton Model language opens things up, and Meta Model questions ask what exactly someone means.",
     'AI (Low) from the closer "If you want to be ethical with people, you need both." into the questions; the closer becomes '
     'the questions\' lead-in (F-528), so his point that ethics needs both stays, and nothing ends on it (E321); F-527\'s '
     'explaining clause and F-528\'s example read AI before (w1102f), so neither is tried again'),
    ('F-528', 528, 'ours',
     'When something sounds true but vague, ask: "What do you mean, specifically?',
     'You need both to be ethical with people, so when something sounds true but vague, ask: "What do you mean, specifically?',
     'with F-527'),
    ('F-762', 762, 'ours',
     "The information on these techniques comes from these sources, but that doesn't mean they validate every NLP claim, or "
     "that every example suits trauma work (Nimja did not write or endorse this guide).",
     "That's where these techniques come from, but don't blame them for every NLP claim here, or for an example that "
     "doesn't suit trauma work (Nimja didn't write or endorse this guide).",
     'Human (Low): a disclaimer in the "doesn\'t mean X, or that Y" frame; said the way he talks, both caveats and the '
     'Nimja line kept'),
    # cards: his words, the suggestion checked in place before it reaches him (applied to the check texts only)
    ('C-92', 92, 'card',
     "That’s one grown-up doing three jobs, not three more people moving in to help with the rent, and each job keeps the "
     "others in balance.",
     "That’s one grown-up doing three jobs, not three more people moving in to help with the rent.",
     'AI (Low) on his inner child guide\'s rent line with its last clause; the clause sums up what his party example right '
     'after it shows (E321, the closer cut; his first account\'s "This relationship-building takes warmth" cut, the same kind)'),
    ('C-480', 480, 'card',
     "Used together properly, the subconscious can feel safer in giving its response. That doesn't make the answers any more "
     "true, though.",
     "Used together properly, the subconscious can feel safer in giving its response, though that doesn't make the answers "
     "any more true.",
     'Human (Low) on his last line by itself, a short closer; joined to the sentence before it (E321), his words otherwise '
     'as they are'),
]


def apply(md, kinds=('ours',)):
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == GUIDE_SHA, 'the guide changed since these edits were written'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    for eid, b, kind, old, new, why in EDITS:
        if kind not in kinds:
            continue
        assert raw[b].count(old) == 1, (eid, raw[b][:80])
        raw[b] = raw[b].replace(old, new)
    return '\n\n'.join(raw) + '\n'


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    for eid, b, kind, old, new, why in EDITS:
        print('%s (%s, %s)\n  - %s\n  + %s\n  why: %s\n' % (eid, kind, sr.where(bl, b), old, new, why))
    apply(md, ('ours', 'card'))


if __name__ == '__main__':
    main()
