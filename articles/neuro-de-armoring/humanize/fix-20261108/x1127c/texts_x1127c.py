#!/usr/bin/env python3
"""This turn's texts (2026-11-27, after his cards-page export of 22:59 UTC): the Psychology section's two abbreviation
splits, and the start of Part 1 (THE SCIENCE). OLD is the article at 9383da82 (OLD-X1127C.json), so it doesn't move once
a paragraph goes in; NEW holds each paragraph as it will be checked, with why each change was made.

The Psychology section's check (SEC-PSYCH#332, https://www.pangram.com/history/85991f56-54f1-4d71-a3e2-7bdab75f2e90) read
Human Written with every paragraph High and two short Medium windows, each a segment Pangram split off at an
abbreviation: 'The Modern "Role-Self" vs.' (5 words) and 'As Dr.' (2 words). The article already writes "vs" with no
full stop in its own heading "Agmatine vs PS vs Phosphatidylcholine", and the section already calls him "Bruce Perry"
("Bruce Perry compares") and "Perry" ("Perry finds"): taking "Dr." off "Perry finds" merged the window Pangram had split
there last turn (P-SW22 step 1, https://www.pangram.com/history/97d19f12-4aa9-4349-ae0f-ac29b81f1e72), as his 71 had it
for Epley ("71 ok", 2026-11-26).

Part 1's opening (old blocks 30, 32, 33): the intro line (27 words, so checked with the paragraph after it), and "A. The
Metabolic Red Line"'s two paragraphs. P032 read Human at Medium by itself (#130,
https://www.pangram.com/history/eeb2d730-ca9e-41ea-815e-6163350f8aee); P033 has never been checked as it stands (the
window-of-tolerance sentence and the DeltaFosB bracket came in from his answers after the stretch check #134).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127c/texts_x1127c.py      (prints each text)
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
OLD = json.loads((HERE / 'OLD-X1127C.json').read_text(encoding='utf-8'))['old']


def plain(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    s = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)
    return s.replace('**', '')


def change(k, *pairs):
    t = OLD[k]
    for a, b in pairs:
        assert t.count(a) == 1, (k, a)
        t = t.replace(a, b)
    return t


NEW = {
    # the splits: "vs" as the article's own heading writes it; "Bruce Perry" as the section's Principle names him
    'sub': change('sub', ('"Role-Self" vs. The', '"Role-Self" vs The')),
    'sw18': change('sw18', ('As Dr. Bruce Perry explains,', 'As Bruce Perry explains,')),
}

# Part 1's intro line (p030). The reads (v1/*/p030): it opens on a rule ("you must understand ... before applying the
# tools") before why the reader needs it, and the fit reader took it to mean the breathing waits until the science is
# read; "the tools" twice; "Hardware Failures" hung on the end as a label, and it sounds permanent; "actually" says
# nothing. So: what the reader gets first (what each tool is for), the label tied in as what the protocol fixes.
NEW['p030'] = ('To see what each tool in this protocol does, let\'s look first at what goes wrong in the brain under '
               'trauma, withdrawal or chronic stress, since those "Hardware Failures" are what it\'s built to fix.')

# The Metabolic Red Line's first paragraph (p032). The reads (v1/*/p032): "anatomy overrides intellect" is two abstract
# nouns acting, reads as always (so years of therapy could never have worked), and S2 says it again; S2 opens on Perry
# and his term before what happens to the reader; "resting heart rate goes up" mixes a baseline with the moment, and
# nothing says past what; "(a state of "Fear")" is a label with nobody's name on it; the two glosses are built alike;
# "blood flow shifts away from the Cortex" sounds like damage, not a passing state; nobody can feel their HRV. So: the
# reader's failure first, said as what happens while triggered; the crossing in the reader's terms (above your usual
# resting rate, the test the protocol uses: his 62a); the shift as something that lasts until you calm down; then the
# names, Perry's, as the post had them (whether "Metabolic Red Line" is Perry's own term goes to Joel as a question:
# one search found his name for it is state-dependent functioning, and "Fear" one of its states).
NEW['p032'] = ('If you\'ve tried to talk yourself out of a trigger and couldn\'t, it\'s because blood flow in your brain '
               'shifts away from the Cortex, which handles logic and reasoning, toward the Brainstem, the part that keeps '
               'you alive. That happens once your heart rate climbs above its usual resting rate, or its variability drops '
               '(a smartwatch shows both), and it lasts until you calm down. Perry describes the point where that happens '
               'as a "Metabolic Red Line" for the traumatized brain, and calls the state past it "Fear".')
# The humanizing pass on it (his moves, SKILL.md "Writing for Pangram"): the reason the reader asks for comes straight
# after their own failure, in the same sentence ("it's because blood flow ... shifts"), where the draft said it twice
# ("goes offline", then the blood flow); when it happens and that it passes in the next, tied by "That happens"; the
# glosses built differently (a "which" clause, then "the part that"); Perry's names last, once the reader has the
# thing they name.

# The Metabolic Red Line's second paragraph (p033). The reads (v1/*/p033): "That's why" gives the advice before the
# mechanism it rests on, and "In that state" then reads as inside the window of tolerance; the advice opens on "many
# trauma therapies" with the reader outside it, and "rather than overwhelming activation" is a contrast nobody needs;
# catecholamines don't "transcribe" proteins (they set off the making of DeltaFosB); DeltaFosB is "the armor itself"
# and "the master switch" at once, and the doubt is said twice. His 39a moved the window of tolerance and the DeltaFosB
# caveat here from section B, so both stay, said once. So: the claim, then why (above the line), then what to do.
NEW['p033'] = ('So if you try to process trauma while you\'re above this red line, you\'re adding to the armor instead of '
               'taking it off. Above the line your functional IQ drops a lot, and stress chemicals called catecholamines '
               'flood the Nucleus Accumbens, a reward center deep in the brain. There they set off the making of DeltaFosB, '
               'a protein that may be what holds the armor in place, though the research on that isn\'t settled. Only work '
               'on your trauma while you\'re under that line, which trauma therapists call staying in your "window of '
               'tolerance".')
# The humanizing pass on it: the packed second sentence split where "There they" carries the reader on; the Nucleus
# Accumbens explained where it is first used in the article (gate E369); the advice last, after the reason it rests
# on, and not a second "So" (as "I'd only work on your trauma" it read as the writer working on the reader's trauma, the
# parse of lesson neuro-2026-11-27s, so it is an order).

# Try 1 (checks-1127ah, ledger #333 to #335):
#  - PAIR-030-032#333 (https://www.pangram.com/history/31cf2d57-7b85-46e3-951b-613e14624ca3): Human Written, Low 37 over
#    the intro line, High, Medium 27 over "That happens once ...", High;
#  - P032#334 (https://www.pangram.com/history/aaa3e455-0e33-4f11-afd3-63fd85cfe36f): Human Written, High, Low 27 over
#    "That happens once ...", High;
#  - P033#335 (https://www.pangram.com/history/58a89835-e138-4a23-b512-6369e1c9eda9): AI Detected 25.7%, High, Low over
#    the catecholamine sentence, AI Low over the DeltaFosB sentence, Low over the advice.
# Each has a Human window, so each next try changes only what a reader could take two ways (the near-miss rule):
TRY1 = {k: NEW[k] for k in ('p030', 'p032', 'p033')}
# the intro's "it" can be the brain ("what goes wrong in the brain ..., since those "Hardware Failures" are what it's
# built to fix"): the protocol, named, where "it" was
NEW['p030'] = change('p030', ('Before applying the tools, you must understand what actually goes wrong in the brain during '
                              'trauma, withdrawal or chronic stress, the "Hardware Failures" the tools are for.',
                              'To see what each tool does, let\'s look first at what goes wrong in the brain under trauma, '
                              'withdrawal or chronic stress, since those "Hardware Failures" are what this protocol is built '
                              'to fix.'))
# "and it lasts" can be the heart rate climbing or the shift: "the shift", the word the sentence before has
NEW['p032'] = TRY1['p032'].replace('and it lasts until you calm down.', 'and the shift lasts until you calm down.')
# the doubt said twice ("may be what holds ..., though the research on that isn't settled"), as the read against his
# fixes marked (x1127c/v1/his-fixes/p033, S3: 9, 16): said once, up front, in the word that carries it ("suspect"), his
# 39a caveat (not settled) kept in it
NEW['p033'] = TRY1['p033'].replace('a protein that may be what holds the armor in place, though the research on that isn\'t '
                                   'settled.', 'the protein researchers suspect holds the armor in place.')
assert all(NEW[k] != TRY1[k] for k in TRY1)

# Try 2 (checks-1127ai, ledger #336 to #338):
#  - PAIR-030-032#336 (https://www.pangram.com/history/34468ef6-941a-440d-ac18-5ec048a9f604): AI Detected 81%, AI Medium
#    over the intro and the paragraph's first sentence: naming "this protocol" at the end (and taking "in this protocol"
#    from the start) read worse than try 1;
#  - P032#337 (https://www.pangram.com/history/ed515fbb-e7ef-4f9a-8da5-982e87ea6b54): AI Assisted 5.8%, Medium, Low, Low:
#    "the shift lasts" read worse than try 2's "it lasts", whose first and last windows were High;
#  - P033#338 (https://www.pangram.com/history/f55e9c83-ee35-48be-973e-ace0616ee952): Human Written, High 50 over the first
#    two sentences, Low 17 over the DeltaFosB sentence, Medium 21 over the advice: the doubt said once took the AI window
#    to Human and the sentence before it to High.
# So each lineage's best is its try 1 (the pair), try 2 (P032), try 2 (P033), and try 3 starts from it.
TRY2 = {k: NEW[k] for k in ('p030', 'p032', 'p033')}
# P032, from try 2 (#334): "its variability drops" leaves heart-rate variability unexplained for a reader who can't place
# it (the fit read: "I can't feel my heart-rate variability"); said in plain words where it is first used (gate E369)
NEW['p032'] = TRY1['p032'].replace('or its variability drops (a smartwatch shows both)',
                                   'or the time between its beats varies less (a smartwatch shows both)')
# the intro, from try 1: the label hung on the end ("since those "Hardware Failures" are what it's built to fix", way 21)
# said as the thing it names, "that's what they're built to fix", with "the tools" as its one "they" (the label is used
# nowhere else in the article)
NEW['p030'] = TRY1['p030'].replace('To see what each tool in this protocol does,', 'To see what the tools in this protocol '
                                   'do,').replace('since those "Hardware Failures" are what it\'s built to fix.',
                                                  'since that\'s what they\'re built to fix.')
# P033, from try 2 (#338): "set off the making of" is a paraphrase where the plain verb belongs (his rule: the plain word
# stays); "switch on"
NEW['p033'] = TRY2['p033'].replace('There they set off the making of DeltaFosB,', 'There they switch on DeltaFosB,')
assert all(NEW[k] not in (TRY1[k], TRY2[k]) for k in ('p030', 'p032', 'p033'))

# Try 3 (checks-1127aj, ledger #339 to #341): PAIR-030-032#339 (https://www.pangram.com/history/af3159d7-72d3-403f-9b5b-90a4965fcaf7)
# and P032#340 (https://www.pangram.com/history/ef537748-af2f-4cc0-92ee-80d4cb5bd35a) read Human Written, one window, High:
# they go in. P033#341 (https://www.pangram.com/history/7d009652-86c5-4ca7-a8d3-35ac5cbf28b3): Human Written, High 50 over
# the first two sentences, Low 35 over the last two.
TRY3 = {'p033': NEW['p033']}
# P033, from try 3: the advice ends on a label hung on the end ("which trauma therapists call staying in your "window
# of tolerance"", way 21); the thing first, the label as an aside after it, in brackets
NEW['p033'] = TRY3['p033'].replace('Only work on your trauma while you\'re under that line, which trauma therapists call '
                                   'staying in your "window of tolerance".', 'Only work on your trauma while you\'re under '
                                   'that line (what trauma therapists call your "window of tolerance").')
assert NEW['p033'] != TRY3['p033']

# Try 4 (checks-1127ak, P033#342, https://www.pangram.com/history/d9eb7768-b356-42f7-985c-ba0dc2911d16): Human Written,
# High 50, Low 14 over the DeltaFosB sentence, Medium 19 over the advice: the best so far (fewest words below High).
TRY4 = {'p033': NEW['p033']}
# P033, from try 4: the DeltaFosB sentence has read Low in three tries; it is a short sentence that only continues the
# one before through two pointers ("There they"): joined to it, the way he joins (gate E368), "where they"
NEW['p033'] = TRY4['p033'].replace('a reward center deep in the brain. There they switch on DeltaFosB,',
                                   'a reward center deep in the brain, where they switch on DeltaFosB,')
assert NEW['p033'] != TRY4['p033']

# The comparison read beside his post (read-1127g, a fresh Fable reader, three findings): F1.1 (lost, 2): "climbs above
# its usual resting rate" reads as any rise, exercise included, where the post means a raised rate at rest, and "varies
# less" has nothing to compare against; F1.3 (lost, 2): the post says the new DeltaFosB proteins are the armor and more
# get made, and "the protein researchers suspect holds the armor in place" leaves the armor undefined, so "adding to the
# armor" loses its reason; F1.2 (unclear, 1): "So" before the reason comes, kept (the paragraph before gives the line).
INNOW = {k: NEW[k] for k in ('p032', 'p033')}
NEW['p032'] = INNOW['p032'].replace('That happens once your heart rate climbs above its usual resting rate, or the time between '
                                    'its beats varies less (a smartwatch shows both),',
                                    'That happens once your heart rate stays above its usual resting rate even while you sit '
                                    'still, or the time between its beats varies less than usual (a smartwatch shows both),')
NEW['p033'] = INNOW['p033'].replace('where they switch on DeltaFosB, the protein researchers suspect holds the armor in place.',
                                    'where they build up DeltaFosB, the protein this protocol treats as the armor itself, '
                                    'though the research on that isn\'t settled.')
assert all(NEW[k] != INNOW[k] for k in INNOW)

# The second comparison read (read-1127h, a fresh Fable reader): F1.1 and F1.3 of read-1127g fixed (now "unclear", 1);
# F1.2 (unclear, 2): "So if you try ..." presents the paragraph's point as following from the paragraph before, though
# its reason comes only in the next sentence: without "So" the point comes first and its reason right after, his order.
# Two two-way words it noted (1): "its beats" (the heart rate's?), and "the research on that" (on what?).
INNOW2 = {k: NEW[k] for k in ('p032', 'p033')}
NEW['p032'] = INNOW2['p032'].replace('or the time between its beats varies less than usual',
                                     'or the time between beats varies less than usual')
NEW['p033'] = (INNOW2['p033'].replace('So if you try to process trauma while', 'If you try to process trauma while')
               .replace('the protein this protocol treats as the armor itself, though the research on that isn\'t settled.',
                        'the protein this protocol treats as the armor itself, though research hasn\'t settled whether it '
                        'is.'))
assert all(NEW[k] != INNOW2[k] for k in INNOW2)

# After the comparison read's fixes (checks-1127am, ledger #344 to #346): PAIR-030-032#344 AI Detected 82%
# (https://www.pangram.com/history/07fa6dcf-eef0-45d0-8de7-133568a045a3), P032#345 AI Detected 37%, AI Low over the
# changed sentence (https://www.pangram.com/history/7b799d18-507a-4e06-b96d-2d2e5f16f56e), P033#346 Human Written, High,
# Low 47 over the DeltaFosB sentence, High (https://www.pangram.com/history/a8485271-f241-43e8-8977-24921d310ab5).
# Sense first: the High versions with the comparison read's severity-2 losses (#340, #343) can't stay. P033's six tries
# are spent (a teaching card). P032's last try: the post's own condition in plain words ("when the resting heart rate is
# elevated", the post) instead of my "stays above its usual resting rate even while you sit still".
AFTER_CR = {k: NEW[k] for k in ('p032', 'p033')}
NEW['p032'] = AFTER_CR['p032'].replace('That happens once your heart rate stays above its usual resting rate even while you sit '
                                       'still, or the time between beats varies less than usual',
                                       'That happens once your resting heart rate is higher than usual, or the time between '
                                       'beats varies less than usual')
assert NEW['p032'] != AFTER_CR['p032']

if __name__ == '__main__':
    for k in OLD:
        print('==', k, '(old)'); print(plain(OLD[k]))
        if k in NEW:
            print('==', k, '(new)'); print(plain(NEW[k]))
