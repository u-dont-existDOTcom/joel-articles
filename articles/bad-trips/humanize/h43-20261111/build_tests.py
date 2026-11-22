#!/usr/bin/env python3
"""build_tests.py - the humanize fixes of turn 34 (2026-11-11), each as the h42a unit it sits in with the fix in place,
written as TEST-<key>.txt for a Pangram check of the whole unit (the lineage's second try; his answer 28a's --after-fix
past that).

The Low windows of batch h42a in sections with no AI window come first (his: a Low window always gets fixed), each with
his five fixes ("Writing for Pangram" in SKILL.md): the point first, a term explained where first used, what belongs
together joined, the plain word, a long list taken apart.

  python3 build_tests.py      write TEST-*.txt and print each fix
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
UNITS = HERE.parent / 'h42-20261111/pass'
FIXES = {
    # Active Seizure (2 of 2): Human Low 20 on its last sentence
    'h42-08': [
        ("I'd treat it as a plausible experimental adjunct remedy rather than something to wait on while a seizure "
         "continues.",
         "So it might help alongside rescue medicine, but it's still experimental, and I wouldn't wait on it while a "
         "seizure keeps going."),
    ],
    # Nausea Smoothers: Human Low 22 on its last sentence (the Medium "It may also extend the trip." is his to fix)
    'h42-17': [
        ("That can be useful and healthy when planned, but I wouldn't reach for it first when somebody is already "
         "becoming manic.",
         "I wouldn't reach for coffee cherries first if somebody is already becoming manic, though a longer trip can be "
         "useful and healthy when it's planned."),
    ],
    # Grounding Menu (2 of 2): Human Low 29 on its last two items (his Medium lines left for him)
    'h42-30': [
        ("Go outside only away from roads, heights, crowds, and water.",
         "Going outside can help too, if it's somewhere quiet with nothing high to fall from, away from roads and "
         "water."),
        ("Avoid strenuous exercise with overheating, chest pain, faintness, severe confusion, stimulant use, an unknown "
         "mixture, or any medical concern.",
         "Avoid strenuous exercise if you're overheating or have chest pain, and hold off too if you feel faint or badly "
         "confused. The same goes after a stimulant or an unknown mixture, or with any medical concern."),
    ],
    # Mental Stabilizers (3 of 6), DMSO's contraindications: AI Medium 15 and AI High 20 on the seizure item. Its second
    # sentence repeats Active Seizure's DMSO paragraph (the same two animal models, "a plausible experimental adjunct
    # remedy"), so it goes as a repeat (gate E378); what stays is the contraindication itself, the point first, with a
    # pointer to where the guide says the rest
    'h42-20': [
        ("DMSO has produced both anticonvulsant and proconvulsant effects depending on dose and seizure model. I consider it "
         "a plausible adjunct for excitotoxic or temporal-lobe-type seizure activity, not a proven universal seizure "
         "rescue.",
         "With seizures it can go either way: in animal studies it calmed one kind and, at some doses, made another kind "
         "worse (more on that in Active Seizure)."),
    ],
    # Mental Stabilizers (5 of 6), ocean water: AI Low 19, AI Low 6 and AI Medium 17 on its last paragraph
    'h42-22': [
        ("It has a grounding, cooling, organizing effect different from DMSO, aged ozonated-charcoal water, zeolite, or "
         "beach morning glory. I don't understand the mechanism. I only know that it has repeatedly felt like a powerful "
         "natural remedy for excessive psychedelic intensity.",
         "It feels grounding and cooling, and there's something organizing about it too that I don't get from DMSO or "
         "my other remedies. I don't "
         "understand the mechanism, I just know that again and again it's felt like a powerful natural remedy for a trip "
         "that's too intense."),
    ],
    # When the Goal Is to Stop a Psychedelic Trip (2 of 2): AI High 32 on the bridge to tripsitting, a five-item list
    'h42-25': [
        ("Once the body is stable and those tools have done what they can, fear, grief, memory, certainty, and whatever "
         "else the altered mind has opened still need somebody to sit with them.",
         "Even once the body is stable and those tools have done what they can, somebody still needs to sit with whatever "
         "the altered mind has opened up, the fear or grief, an old memory, a sudden certainty..."),
    ],
}


# Second tries (his answer 28a: one more check of the whole section after each fix), named KEY-fix2
FIXES2 = {
    # Active Seizure (2 of 2): fix1 ("So it might help ..., but it's still experimental, and I wouldn't wait on it ...")
    # read AI Low (a0b91061); this takes the shape of his Human High line in the part before ("I'd also try sniffing
    # humic/fulvic acid powder, although that's just a hunch ..."): the point first (the rescue medicine first while a seizure continues, said as what to do, not "don't wait on it": his X1), then one first-person act and one candid hedge
    'h42-08': [
        ("I'd treat it as a plausible experimental adjunct remedy rather than something to wait on while a seizure "
         "continues.",
         "While a seizure continues, the rescue medicine comes first, and I'd still consider DMSO alongside it, although "
         "that's experimental."),
    ],
}

# Active Seizure 2's third try: fix2 read Human Medium (83f4caef) but dropped "adjunct remedy", which is his (KEEP-AS-IS
# K12, round 5: "the one thing that flipped it was adding 'remedy' to 'adjunct'"); this keeps those words and fix2's
# order (the rescue medicine first, then his act and its hedge)
FIXES3 = {
    'h42-08': [
        ("I'd treat it as a plausible experimental adjunct remedy rather than something to wait on while a seizure "
         "continues.",
         "While a seizure continues, the rescue medicine comes first, and I'd treat DMSO as a plausible adjunct remedy, "
         "although that's experimental."),
    ],
}


def build3(key):
    text = (UNITS / 'units' / (key + '.txt')).read_text(encoding='utf-8').rstrip('\n')
    for old, new in FIXES3[key]:
        assert text.count(old) == 1, (key, old)
        text = text.replace(old, new)
    return text


def build2(key):
    text = (UNITS / 'units' / (key + '.txt')).read_text(encoding='utf-8').rstrip('\n')
    for old, new in FIXES2[key]:
        assert text.count(old) == 1, (key, old)
        text = text.replace(old, new)
    return text


def build(key):
    text = (UNITS / 'units' / (key + '.txt')).read_text(encoding='utf-8').rstrip('\n')
    for old, new in FIXES[key]:
        assert text.count(old) == 1, (key, old)
        text = text.replace(old, new)
    return text


# Paragraph tests (E343: a section whose last try read Mixed is narrowed to its paragraphs first, each checked by itself,
# with the paragraph it leans on when it is too short for the web app's 50-word minimum, E349), cut from the fixed unit:
# KEY-p is the paragraph run [first, last] of TEST-KEY.txt's paragraphs (blank-line blocks), 1-based
PARAS = {
    'h42-20': (3, 4),    # "Contraindications:" and its three items (the seizure item is 25 words)
    'h42-22': (3, 4),    # "When a trip is too strong ..." and the fixed paragraph after it
    'h42-25': (7, 8),    # the B3 forms paragraph and the bridge after it
}


# Tests written whole: a paragraph's next try with the paragraph it leans on, or a teaching candidate with its heading
# (gate bad-trips-2026-11-07c: my best tested tries before a paragraph goes to him)
FORMS = ("Other forms of vitamin B3 seem less reliable for relaxation. Niacinamide sometimes relaxes people and sometimes "
         "creates hyperfocus, depending on their state. Avoid sustained-release niacin and the useless non-flush "
         "hexanicotinate form.")
WHOLE = {
    # the bridge's second and third tries: fix1's list taken apart still read AI High (fd6713de); these drop the list,
    # which only previews what the sections after it say in full (lesson 06a), and say what is left plainly
    'h42-25-p2': FORMS + "\n\nOnce the body has settled and those tools have done what they can, whatever the trip stirred up "
                         "still needs somebody to sit with it.",
    'h42-25-p3': FORMS + "\n\nEven when the body's calm again and the remedies have done what they can, the trip may have "
                         "stirred something up, and somebody still needs to sit with that.",
    # Get One Human Anchor, its first two paragraphs (38 tries of earlier wordings; h42a: AI Generated, 100%): his five
    # fixes, the alone-or-crowd point said as what makes a trip worse, the crowd's four acts taken apart, the hand-off's
    # conditions said with the firm one last (W079's keys kept: fatigue, logistics, risk)
    'anchor-a1': "Get One Human Anchor\n\n"
                 "Being alone with a frightened or over-certain mind can make a bad trip worse. So can a crowd of people "
                 "telling them what it all means, or panicking right along with them.\n\n"
                 "So have one calm person be the anchor and take the lead. One person can only handle so much, though. If "
                 "fatigue or logistics start getting to be too much for them, or keeping everyone safe does, bring in one "
                 "more calm adult or a crisis professional to back them up, and do it right away if there's any risk of "
                 "violence or self-harm.",
    # Risk of Harm, its first paragraph (h42a: AI Generated, 100%): one sentence of nine conditions, taken apart (his
    # fifth fix), firm since someone could get hurt; W002's keys kept (dangerous, unreachable, severely)
    'harm-b1': "Risk of Harm: When Peer Support Isn't Enough\n\n"
               "Get urgent help the moment somebody might hurt themselves or anyone else, or you can't keep them physically "
               "safe, like when they keep heading for roads and high places, or water for that matter. Voices telling them "
               "what to do are a reason too, and so is a fixed, terrifying belief they've started acting on. Get help just "
               "as fast if they turn violent or they're so severely confused they're unreachable. Dangerous physical "
               "symptoms count, and so does going so long without sleep that their judgment is falling apart. And if it's "
               "more than you can safely handle, call for help then too.",
    # Dealing With Shadow Thoughts (Mostly Human, 8%): its two AI Low windows are the during-a-trip lines; checked with the
    # paragraph before them (E343, E349). The don't-list said in his frame (J69: a condition, a hedged don't, plain verbs,
    # a trailing "..."), W120's keys kept (don't, suppress, permanent); the script line said as what to notice
    'h42-41-p': "I am not repeating the simplistic Hermetic claim that opposites are required to understand anything. A hated "
                "baby does not feel love, and a loved baby does not feel hate. In the subconscious world of concepts, however, "
                "two sides are often considered together.\n\n"
                "While you're still tripping, maybe don't take every shadow thought as the truth about you, or try to suppress "
                "it either. Confessing it to everyone in the room can wait, and so can turning it into some permanent "
                "diagnosis... You can just notice it instead, something like \"this is a thought and a feeling, and it's "
                "intense, but it isn't the whole of me.\" Then return to room, body, human, time, and love.",
    # Risk of Harm's third try, after the tell panel on the second (panel-harm-b2/PANEL.md: every sentence AGREED; WHOLE,
    # both readers: an even run of "if X, call" triggers, a thesis opener and a summary closer, a checklist turned into
    # prose). This drops the thesis and the closer, varies how each reason is said, names the body's signs instead of a
    # pointer ("listed above", a template slot), and ends on the reader's own doubt (E135: a within-the-thought turn).
    # W002's keys kept (dangerous, unreachable, severely)
    'harm-b3': "Risk of Harm: When Peer Support Isn't Enough\n\n"
               "You can sit through a lot with someone, but not everything. The moment you think they might hurt themselves "
               "or anybody else, get urgent help, even if you're not sure. I'd get help too if I couldn't keep them "
               "physically safe, like when they keep heading for the road or the water, or trying to get up somewhere high. "
               "It's time as well when voices are telling them what to do, or they've started acting on some terrifying "
               "belief they won't let go of, and any violence means calling right away. Someone so severely confused that "
               "they're unreachable needs more than a friend can give. So does someone whose body is showing dangerous "
               "signs, like trouble breathing or overheating, or who hasn't slept in so long that their judgment is going. "
               "If you find yourself wondering whether this is more than you can safely handle, it probably is, so call.",
    # Risk of Harm's second try: b1 (the list taken apart into five sentences) still read AI Generated 100% (4c6f1bf6), a
    # march of conditions. Lesson 06a's look across the guide: "dangerous physical symptoms" is the whole Call medics list
    # just above it, so it points there (W002's key "dangerous" kept); the rest said the way his first five minutes are
    # (Human High): what peer support can carry first, then the moment to call, one case at a time with a small scene
    'harm-b2': "Risk of Harm: When Peer Support Isn't Enough\n\n"
               "Peer support only goes so far. If it looks like someone might hurt themselves or anyone else, or you can't "
               "keep them physically safe, say they keep making for the road or the water, or climbing somewhere high, get "
               "urgent help right then. Voices telling them what to do are a reason to call, and so is a fixed, terrifying "
               "belief they've started acting on. If it turns violent, call right away. If they're so severely confused "
               "they're unreachable, or "
               "they haven't slept in so long their judgment is falling apart, that's past what a sitter can carry too, and "
               "so are the dangerous physical symptoms listed above. And if it's more than you can safely handle, call.",
}


def para_text(key):
    blocks = (HERE / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').rstrip('\n').split('\n\n')
    a, b = PARAS[key]
    return '\n\n'.join(blocks[a - 1:b])


if __name__ == '__main__':
    for key in FIXES3:
        t = build3(key)
        (HERE / ('TEST-%s-fix3.txt' % key)).write_text(t + '\n', encoding='utf-8')
        print(key + '-fix3', len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
    for key in FIXES2:
        t = build2(key)
        (HERE / ('TEST-%s-fix2.txt' % key)).write_text(t + '\n', encoding='utf-8')
        print(key + '-fix2', len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
    for key in FIXES:
        t = build(key)
        (HERE / ('TEST-%s.txt' % key)).write_text(t + '\n', encoding='utf-8')
        print(key, len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
    for key in PARAS:
        t = para_text(key)
        (HERE / ('TEST-%s-p.txt' % key)).write_text(t + '\n', encoding='utf-8')
        print(key + '-p', len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
    for key, t in WHOLE.items():
        (HERE / ('TEST-%s.txt' % key)).write_text(t + '\n', encoding='utf-8')
        print(key, len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
