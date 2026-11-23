#!/usr/bin/env python3
"""Put his answers of 2026-11-23 into HUMANIZED-SO-FAR.md: his version of the Weeks 3-5 line (card W35, exported
20:11 UTC, which he checked himself: Human Written, one window, High) and his answers 34 to 56 (his message of 20:40 UTC:
../joel-20261123-2040-message.txt; the questions: ../../OWNER-QUESTIONS.md). Each change is his line with the words the
option he picked gave, fitted where it goes, or his own words; none is a paragraph of mine.

- W35: his line goes at the top of the Void phase, before its Protocol line, with "the 5-HTP section" linked to it.
- 34: the agmatine warning's "psych" stacks are psychoactive ones, in his words: anything that works on the brain.
- 35a: one list of agmatine's stop signs, every sign from the three, in the warning at the top; the cycle rule and Weeks
  1-2 point to it. (His lasting-anhedonia sentence for agmatine is mine to write and check: it waits.)
- 36a: no 5-HTP with serotonin-raising drugs or near ayahuasca/harmalas or iboga, with no review clause.
- 37a: five problems, A to E.
- 38a: the D-Serine tactic gets its own section after the scenarios, for a planned session once you can stay under the
  red line through one, whatever the week; its "acute sessions" become planned ones.
- 39a: section B's copy of the red line goes; its window of tolerance and its DeltaFosB caveat move to section A.
- 40b: Scenario A's sentence on D-serine and exposure therapy goes (the science part says what was tested); "The idea
  is that it" names D-serine, since the sentence before it went; "ssuggested" is spelled right.
- 41a: zinc with the nightly magnesium and L-serine in the daily list (the article gives neither an amount: question 58);
  the Rescue line drops the Repair Stack (leucine was cut on his word, card SB-42).
- 42a: agmatine's conflict line points to its timing rule.
- 43b: the Void loses "Dynorphin" in its names (Weeks 3-7, Scenario C's mechanism line, and "entering the Void").
- 44a, 45a, 46a, 47a, 48a, 49a, 50a, 51a, 52a, 53a, 54a, 55a, 56b: as the options said.
- 26a (x1123a item 29): Weeks 1-2's agmatine takes the agmatine section's "once or twice daily".

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1123b/apply_x1123b.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
U = 'https://ibogaqueen.substack.com/i/181671197/'
TOP = U + 'a-complete-guide-to-bio-de-armoring'
P1, A = U + 'part-1-the-science-why-we-do-this', U + 'a-the-metabolic-red-line'
HTP, GS = U + 'serotonin-bottleneck-pattern-5-htp-low-dose-p5p', U + '2-the-glutamate-shield-anxiety'
SA, SC, P5 = U + 'scenario-a-the-glutamate-storm', U + 'scenario-c-the-void', U + 'part-5-the-timeline-the-8-week-path'

W35 = ("So you can tell what each new thing does, add them one at a time, starting with the UMP trial and working down "
       "the list below to the keto diet. 5-HTP could help your mood here, though iboga acts on serotonin too, so don't "
       "take 5-HTP at all while you're microdosing iboga or elliptica. There isn't enough data to say you should or "
       "shouldn't use UMP with any microdose, nor whether 5-HTP would be good with a mushroom microdose, so try those "
       "combos if you want and see how it feels. If you're too numb to tell, compare your sleep and dreams on the nights "
       "after each kind of day. Mushrooms act on serotonin too, just not the way iboga does, so stop the 5-HTP if you get "
       "any of the stop signs [the 5-HTP section](" + HTP + ") lists.")
DSERINE_HEADING = '### D-Serine for a Planned Session'

# (answer, old words, new words): each old string must be in the article exactly once
EDITS = [
    ('34', 'or other complex "psych" stacks without having a physician',
     'or other complex psychoactive stacks (anything that works on the brain) without having a physician'),
    ('35a', 'Stop immediately if it causes flatness, anhedonia, emotional blunting, new depression, agitation, insomnia, '
            'dizziness, palpitations,',
     'Stop immediately if it causes flatness, anhedonia, apathy, emotional blunting, new depression, agitation, '
     'irritability, insomnia, dizziness, palpitations,'),
    ('35a', 'without worsening flatness. Stop if flatness, anhedonia, apathy, irritability, insomnia, dizziness, nausea, '
            'loose stools, diarrhea, or increased craving appears.',
     'without worsening flatness. Stop at any of the stop signs in [the Agmatine Warning at the top](' + TOP + ').'),
    ('35a', 'If agmatine leaves you flat, anhedonic, dizzy, nauseous, sleepless, irritable, or more craving-prone--drop it.',
     'If agmatine gives you any of its stop signs ([the Agmatine Warning at the top](' + TOP + '))--drop it.'),
    ('36a', 'or other serotonin-raising stacks without clinician review.', 'or other serotonin-raising stacks.'),
    ('36a', 'anywhere near ayahuasca/harmalas or iboga unless the whole medicine plan has been medically reviewed.',
     'anywhere near ayahuasca/harmalas or iboga.'),
    ('37a', 'to go after 4 specific neuro-biological problems before you go working',
     'to go after 5 specific neuro-biological problems ([A to E below](' + P1 + ')) before you go working'),
    ('39a', 'adding to the armor instead of taking it off. In that state your functional IQ drops a lot, and the Nucleus '
            'Accumbens gets flooded with the catecholamines that transcribe new DeltaFosB proteins, the "armor" itself.',
     'adding to the armor instead of taking it off. That\'s why many trauma therapies emphasize staying within a '
     'manageable "window of tolerance" rather than overwhelming activation. In that state your functional IQ drops a lot, '
     'and the Nucleus Accumbens gets flooded with the catecholamines that transcribe new DeltaFosB proteins, the "armor" '
     'itself (DeltaFosB may be the master switch, but the research isn\'t settled).'),
    ('42a', 'Use agmatine for storm control, not immediately before a session where the goal is deliberate reconsolidation.',
     'Use agmatine for storm control, and keep it away from a session where the goal is deliberate reconsolidation '
     '([its timing rule](' + GS + ') says how far).'),
    ('44a', "Why don't these drugs work on calcified PTSD?", 'Why do these drugs so often fail on calcified PTSD?'),
    ('46a', 'You must do this for 10–20 minutes immediately after a trigger to "jam" the memory reconsolidation.',
     'You must do this for 10–20 minutes as soon as your heart rate is back down after a trigger ([Scenario A](' + SA +
     ")'s Steps 1 and 2), to \"jam\" the memory reconsolidation."),
    ('48a', "If you're sensitive, start lower and do the trial with just 50mg 5-HTP",
     'Start lower and do the trial with just 50mg 5-HTP'),
    ('49a', 'headache, vivid or intense dreams, insomnia,', 'headache, dreams so intense they disturb your sleep, insomnia,'),
    ('51a', 'For the long run there\'s Strategy B, the "Resilience Mode"',
     'For the repair weeks (Weeks 3–7 of [the timeline](' + P5 + ')) there\'s Strategy B, the "Resilience Mode"'),
    ('51a', 'refer to my [Keto Adaptation Guide](http://ketoflu.u-dont-exist.com/).',
     'refer to my [Keto Adaptation Guide](http://ketoflu.u-dont-exist.com/). Low carb, with keto seasons, is for after '
     'them (Week 8+).'),
    ('50a', 'If on Quick Fix, Strategy A (BHB Salts / Standard Diet):', 'If on Crisis Mode, Strategy A (BHB Salts / Low-Sugar Diet):'),
    ('50a', 'If on Deep Fix, Strategy B (Keto Diet):', 'If on Resilience Mode, Strategy B (Keto Diet):'),
    ('52a', 'Potato (Baked with skin): ~925 mg (The King of Potassium).', 'Potato (Baked with skin): ~925 mg.'),
    ('43b', 'sedated, or entering the Dynorphin Void.', 'sedated, or entering the Void.'),
    ('43b', 'Mechanism: The Dynorphin block is active. You feel "dead."', 'Mechanism: You feel "dead."'),
    ('54a', 'on an empty stomach before a de-armoring session',
     'on an empty stomach (no meal; the PQQ and ketones are fine) before a de-armoring session'),
    ('38a', 'Advanced tactic: The D-Serine Memory Re-consolidator. While L-Serine',
     'Advanced tactic: The D-Serine Memory Re-consolidator, for a planned session once you can stay under [the red '
     'line](' + A + ') through one, whatever the week. While L-Serine'),
    ('40b', 'D-serine has shown efficacy in studies where it was used to augment exposure therapy for treating a variety '
            'of conditions such as social anxiety, PTSD, and fear of public speaking. The idea is that it facilitates',
     'The idea is that D-serine facilitates'),
    ('40b', 'Some studies ssuggested that d-serine', 'Some studies suggested that d-serine'),
    ('38a', 'Use D-Serine for acute sessions where you need to "force" memory reconsolidation.',
     'Use D-Serine for planned sessions where you need to "force" memory reconsolidation.'),
    ('41a', '+ Magnesium Glycinate 400 mg + NAC 1.8–2.4 g divided.',
     '+ Magnesium Glycinate 400 mg with zinc at night + L-Serine + NAC 1.8–2.4 g divided.'),
    ('26a', 'then increasing to 500 mg twice daily only if', 'then increasing to 500 mg once or twice daily only if'),
    ('47a', 'Fuel: Start with BHB Salts (Strategy A) to manage initial fog.',
     "Fuel: BHB Salts (Strategy A) manage the initial fog. If you're the high-cortisol type, start PS first and add the "
     "salts once you know how PS sits; if not, take PQQ with the salts from the start."),
    ('41a', '+ The Repair Stack (Zn/Leu/Ser) + Tetris/Color Path for acute attacks.', '+ Tetris/Color Path for acute attacks.'),
    ('43b, 53a, 55a', 'Weeks 3–5: The Dynorphin Void (Depression Phase)State: The anxiety stops, but the world turns gray/boring.',
     'Weeks 3–7: The Void (Depression Phase)State: The anxiety mostly stops, but the world turns gray/boring.'),
    ('56b', 'Hot & cold showers, alternating, ending on cold). *No hot showers',
     'Hot showers for the numbness, with [Scenario C](' + SC + ")'s hot and cold routine as the stronger option. *No hot showers"),
    ('53a', 'now that the acute storm has passed.', 'now that the worst of the storm has passed.'),
    ('45a', 'DeltaFosB degraded, if the animal timelines carry over. Hardware reset complete.',
     'DeltaFosB degraded, if the animal timelines carry over.'),
]


def main(write):
    text = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode('utf-8')).hexdigest()
    applied = []
    for ans, old, new in EDITS:
        if text.count(old) != 1:
            if text.count(new.split('](')[0]) and old not in text:
                continue  # already in
            sys.exit('%s: %d matches for %r' % (ans, text.count(old), old[:70]))
        text = text.replace(old, new, 1)
        applied.append({'answer': ans, 'old': old, 'new': new})
    lines = text.split('\n')
    # 39a: section B's copy of the red line goes
    red = [i for i, l in enumerate(lines) if l.startswith("The Metabolic Red Line: We often assume we can 'think'")]
    if red:
        (i,) = red
        assert lines[i + 1] == ''
        applied.append({'answer': '39a', 'removed': lines[i]})
        del lines[i:i + 2]
    # W35: his line at the top of the Void phase, before its Protocol line
    if W35 not in lines:
        (j,) = [k for k, l in enumerate(lines) if l.startswith('Weeks 3–7: The Void (Depression Phase)State:')]
        assert lines[j + 1] == '' and lines[j + 2].startswith('Protocol:Reduce or stop phosphatidylserine here.')
        lines[j + 1:j + 1] = ['', W35]
        applied.append({'answer': 'W35', 'inserted': W35, 'after': lines[j]})
    # 38a: the D-Serine tactic (its five paragraphs) moves to its own section after the scenarios
    if DSERINE_HEADING not in lines:
        (s,) = [k for k, l in enumerate(lines) if l.startswith('Advanced tactic: The D-Serine Memory Re-consolidator')]
        (e,) = [k for k, l in enumerate(lines) if l.startswith('Warning: High doses of D-Serine damaged the kidneys')]
        assert lines[s - 1] == '' and lines[e + 1] == '' and e - s == 8
        block = lines[s:e + 1]
        del lines[s:e + 2]
        (p5,) = [k for k, l in enumerate(lines) if l.startswith('## Part 5: THE TIMELINE')]
        assert lines[p5 - 1] == '' and lines[p5 - 2].startswith('Activate the "Inner Father"')
        lines[p5:p5] = [DSERINE_HEADING, ''] + block + ['']
        applied.append({'answer': '38a', 'moved': 'the D-Serine tactic\'s five paragraphs, from Scenario A to a section of '
                        'their own after Scenario C', 'heading': DSERINE_HEADING})
    out = '\n'.join(lines)
    rec = {'about': 'his card W35 (his version, exported 2026-11-23 20:11 UTC) and his answers of 2026-11-23 20:40 UTC: '
                    '34, 35a, 36a, 37a, 38a, 39a, 40b, 41a, 42a, 43b, 44a to 55a, 56b; and his 26a for Weeks 1-2\'s agmatine',
           'message': '../joel-20261123-2040-message.txt', 'card': '../x1123a/ANSWERS-X1123A-20261123-2011.json',
           'his_check_w35': 'https://www.pangram.com/history/dd9b04f2-605a-4d05-a1fc-256ad186a83e (Pangram 4.1, Human '
                            'Written, one window of 147 words, High)',
           'whose': 'his lines and his words, with the words of the option he picked fitted where they go',
           'applied': applied,
           'held': ["his lasting-anhedonia sentence for agmatine: mine to write, in the stop-signs paragraph question 35 "
                    "changed, which reads AI with it: humanized and checked by itself first",
                    'amounts for zinc and L-serine in the daily list: question 58'],
           'before_sha256': before, 'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], len(applied), sorted({a['answer'] for a in applied}))
    if write and applied:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1123B.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
