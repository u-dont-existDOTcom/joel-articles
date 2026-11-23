#!/usr/bin/env python3
"""questions_x1123a.py - put questions 34 to 55 (the contradictions check run again, x1123a) and this turn's report on
OWNER-QUESTIONS.md. Idempotent: refuses to add the questions twice."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
P = ROOT / 'OWNER-QUESTIONS.md'
B = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/neuro-de-armoring/humanize/'
L = B + 'fix-20261108/coherence/x1123a/EXTRACT.md'
CHECK = B + 'fix-20261108/coherence/x1123a/CHECK.md'
H = 'https://www.pangram.com/history/'


def lines(n):
    return '([the lines](%s), item %s)' % (L, n)


HEADER = """Last updated 2026-11-23, after your message of 17:25 UTC.
**Open questions: 22** (34 to 55, from the contradictions check run again). **For you to do**: card W35 on the cards
page, your version of the Weeks 3–5 line."""

OPEN = """## Open questions

The contradictions check ran again over the whole article: a fresh reader found 35 pairs of statements that can't both
hold ([the list](%(L)s), [what became of each](%(CHECK)s)). The article explains 4 of them, your answers settled 2, 2 wait on
work of mine for your answers (below), 3 turned out not to be contradictions (after the questions), and the other 24 are
questions 34 to 55. Each has my pick where I have one: if most are right, answer "picks" and name only the ones you'd
change (like "picks, but 38b, 43: your words").

**🟣 34. Agmatine with psychedelics: what does "psych" mean in the warning?** The warning at the top says not to use
agmatine with other complex "psych" stacks without a physician who can weigh the interactions; your paragraph (33b) says
you can try it with a trip; Weeks 1–2 says not to add it on a day you microdose %(l2)s.

- a) Psychiatric drugs: the warning says "psychiatric drug stacks", and the Weeks 1–2 line stays, since it's about the day
  you start agmatine. (My pick: then all three hold, and it matches your answer 23.)
- b) Psychedelics too: your paragraph says to try agmatine with a trip only with such a physician.
- c) Your words.

**🟣 35. Agmatine's stop signs: one list, said once?** The warning at the top, the Shield's cycle rule and Weeks 1–2 each
list them, and each list has signs the others leave out (palpitations and new depression only in the first, apathy only in
the second, no stomach signs in the third) %(l3)s.

- a) One list with every sign from the three, in the warning at the top; the other two say to stop at any of its stop
  signs. (My pick: said once, with nothing lost.)
- b) The same full list in all three places.
- c) Your words.

**🟣 36. 5-HTP with serotonergic drugs or iboga: never, or after a clinician's review?** The warning at the top allows it
after a clinician's review (and near iboga, after a medical review of the whole plan); the 5-HTP line in the Shield and
Weeks 3–5 say never, with no exception %(l5)s.

- a) Never: the warning at the top drops its two review clauses. (My pick: it matches the other two lines and your answer
  17, "except iboga with 5htp, no".)
- b) After a clinician's review: the other two lines say so too.
- c) Your words.

**🟣 37. "4 specific problems", but five sections (A to E)?** The opening says the protocol goes after 4 problems; Part 1
has five lettered sections and doesn't say which four %(l7)s.

- a) Five: "go after 5 specific neuro-biological problems (A to E below)". (My pick: each section is one thing that goes
  wrong.)
- b) A is the rule behind the other four: the opening says so.
- c) Your words.

**🟣 38. When, and in what state, is a D-Serine session?** The science says processing trauma above the red line adds
armor, and that a session that ends overwhelmed can lock the fear in; the opening drops long sessions "temporarily", with
no end given; and the D-Serine tactic sits in Scenario A, the Glutamate Storm, whose instruction is for when the wave hits
([the lines](%(L)s), items 9 and 11). The 10–20 minutes of the Color-Path game isn't trauma processing, so that part holds.

- a) The D-Serine tactic gets its own short section after the scenarios, for a planned session once you can stay under the
  red line through one, whatever the week. (My pick: that's the article's own rule, and it says when "temporarily" ends.)
- b) It stays in Scenario A, saying it's for a planned session once the storm has passed.
- c) Your words.

**🟣 39. Section B repeats section A's red line, hedged: keep one?** Section A says it flatly (a raised heart rate shifts
blood away from the cortex, and DeltaFosB is the armor); a paragraph in section B, also called "The Metabolic Red Line",
says Perry's data "proves" it, then gives the same points as "often", "may" and "the research isn't settled" %(l10)s.

- a) B's copy goes, and the two things in it that A lacks move to A: the "window of tolerance" many trauma therapies keep
  to, and that the DeltaFosB research isn't settled. (My pick: said once, with nothing lost.)
- b) Keep both, with A hedged like B.
- c) Your words.

**🟣 40. Has D-serine itself been tested with exposure therapy?** The science part says the drug tested alongside exposure
therapy is DCS, not D-serine; Scenario A says D-serine itself has worked in exposure-therapy studies of social anxiety, PTSD
and fear of public speaking %(l13)s. What I found in PubMed and ClinicalTrials.gov: the exposure-therapy trials for social
anxiety and public speaking used DCS. D-serine itself has one small trial in chronic PTSD, where it was given on its own,
without exposure therapy (anxiety scores fell, and the PTSD scale trended better: [Heresco-Levy, et al,
2009](https://doi.org/10.1017/S1461145709000339)), and mouse studies where it helped fear extinction ([Balu, et al,
2018](https://doi.org/10.1016/j.biopsych.2017.08.012)).

- a) Scenario A says what's known: exposure therapy was tested with DCS, and D-serine has one small PTSD trial on its own
  and the mouse studies. (My pick: it's what the studies show.)
- b) That sentence goes, since the science part already says it.
- c) Your words.

**🟣 41. L-serine and the Repair Stack: daily, or for attacks?** Leucine is out by your SB-42 cut, so "Leu" leaves the
Weeks 1–2 Rescue line's "Repair Stack (Zn/Leu/Ser)" either way. That leaves zinc and L-serine for acute attacks, while the
science part has zinc as the Lock with magnesium, and Scenario A says L-serine is for daily maintenance, yet neither is in
the daily list ([the lines](%(L)s), items 14 and 15).

- a) Daily: zinc goes with the nightly magnesium, L-serine joins the daily list, and the Rescue line drops the stack. (My
  pick: Scenario A already says daily.)
- b) For attacks: the Rescue line says "zinc + L-serine", and "daily maintenance" goes from Scenario A.
- c) Your words.

**🟣 42. Agmatine before a session: one timing rule?** Your answer 23 was about agmatine with psychedelics (it went in as
33b), so this part of question 23 is still open. One line says not to take agmatine "immediately before" a session for
reconsolidation, with no gap given, while the timing rule says to avoid it that whole day or keep it hours away from the
session %(l17)s.

- a) The first line points to the timing rule. (My pick: one rule, said once.)
- b) Keep both as they are.

**🟣 43. If dynorphin clears quickly, what keeps the Void going for weeks?** Your paragraph in section C says dynorphin
clears relatively quickly and DeltaFosB is what keeps the learning from clicking; the timeline calls Weeks 3–5 "The
Dynorphin Void", and Scenario C says "The Dynorphin block is active" %(l18)s. No pick: it's your science.

- a) The names stay, and Weeks 3–5 says the Void outlasts the dynorphin because DeltaFosB still holds the armor, as your
  paragraph has it.
- b) "Dynorphin" leaves the Void's names: Weeks 3–5 is "The Void (Depression Phase)", and Scenario C drops "The Dynorphin
  block is active".
- c) Your words.

**🟣 44. SSRIs: trials "mixed", then "don't work"?** The trials paragraph says results in veterans have been mixed since;
the next asks why these drugs don't work on calcified PTSD %(l19)s.

- a) The question matches the trials: "Why do these drugs so often fail on calcified PTSD?" (My pick.)
- b) Keep it as it is.
- c) Your words.

**🟣 45. Week 8+: "Hardware reset complete"?** The science part says DeltaFosB fades slowly, the same fears keep making
more, and nobody has tested whether iboga or psilocybin loosen it; Week 8+ says it's degraded "if the animal timelines carry
over", then "Hardware reset complete" %(l20)s.

- a) "Hardware reset complete" goes, and the "if" stays. (My pick: then the line says only what's known.)
- b) Keep it.
- c) Your words.

**🟣 46. The Jammer: right after a trigger, or after Steps 1 and 2?** Section E says to play the game for 10–20 minutes
immediately after a trigger; Scenario A puts it third, after five minutes of rhythm and once your heart rate is back to
normal %(l21)s.

- a) Section E says to play it as soon as your heart rate is back down after a trigger (Scenario A's Steps 1 and 2). (My
  pick: Scenario A's order comes with its reason, rhythm first.)
- b) Scenario A plays the game first.
- c) Your words.

**🟣 47. Cortisol before ketones, or BHB salts for everyone from week 1?** Part 2 says to address cortisol before ketones,
and gives PQQ with ketones as the path when cortisol isn't high; Weeks 1–2 starts everyone on BHB salts, in the same list as
PS %(l22)s.

- a) Weeks 1–2 says it: if you're the high-cortisol type, start PS first and add the BHB salts once you know how PS sits;
  if not, take PQQ with the salts from the start. (My pick: it's what Part 2 says, one change at a time.)
- b) Part 2's "before ketones" means first in importance, not first in time: it says so, and Weeks 1–2 stays.
- c) Your words.

**🟣 48. 5-HTP: the lower start for everyone, or only if you're sensitive?** The 5-HTP section starts lower only "if
you're sensitive" (otherwise at Scott's dose); Weeks 3–5 starts everyone lower %(l24)s.

- a) Everyone starts lower: the 5-HTP section drops "If you're sensitive". (My pick: the trial then reads the same in both
  places, and it costs a couple of nights.)
- b) Only if you're sensitive: Weeks 3–5 says so.
- c) Your words.

**🟣 49. Vivid dreams on 5-HTP: a good sign, or a stop sign?** The 5-HTP section names more vivid or memorable dreams as a
sign it's the right tool; the next paragraph lists vivid or intense dreams as a stop sign %(l25)s.

- a) The stop sign becomes "dreams so intense they disturb your sleep", and vivid dreams stay a good sign. (My pick.)
- b) Your words.

**🟣 50. One name for each ketone strategy?** Part 2 calls them "Crisis Mode" and "Resilience Mode", and Strategy A's diet
"a standard low-sugar diet"; the Shield's headings say "Quick Fix" and "Deep Fix", and "Standard Diet" %(l26)s.

- a) "Crisis Mode" and "Resilience Mode" everywhere, and "Low-Sugar Diet" in the Shield's heading. (My pick: Part 2 is
  where they're explained.)
- b) "Quick Fix" and "Deep Fix" everywhere.
- c) Your words.

**🟣 51. The long-run diet: strict keto, or low carb with keto seasons?** Part 2 gives Strategy B, strict keto, as the
long-run plan; Week 8+ says to keep up low carb, with keto only seasonally %(l27)s.

- a) Part 2 says strict keto is for the repair weeks, and low carb with keto seasons is for after them. (My pick: then both
  hold.)
- b) Strict keto stays the long-run plan: Week 8+ says so.
- c) Your words.

**🟣 52. The potato as "the King of Potassium"?** The same list gives beet greens and salmon more potassium than the
potato %(l28)s.

- a) The label goes. (My pick: the numbers beside it say otherwise.)
- b) Your words.

**🟣 53. Weeks 3–5: "The anxiety stops", yet agmatine stays for storms?** The phase's State line says the anxiety stops,
and its Transition line says the acute storm has passed, while your 22a rule keeps agmatine in this phase if it's still
helping acute glutamate storms %(l30)s.

- a) The State line says "The anxiety mostly stops", and the Transition line "now that the worst of the storm has
  passed". (My pick: then your rule has storms to be for.)
- b) Your words.

**🟣 54. D-serine "on an empty stomach", after PQQ and ketones?** Scenario A says to take it on an empty stomach, and your
order (27a) has PQQ and ketones 45 minutes before it %(l31)s.

- a) "On an empty stomach (no meal; the PQQ and ketones are fine)". (My pick.)
- b) Your words.

**🟣 55. "The 8-Week Path" skips weeks 6 and 7.** Its stages are Weeks 1–2, Weeks 3–5 and Week 8+ %(l35)s.

- a) The Void phase runs to the baseline: "Weeks 3–7". (My pick: Week 8 stays where the DeltaFosB line puts it.)
- b) The baseline starts sooner: "Week 6+".
- c) Your words.

- 🟢 **Not contradictions after all** (say if you see one otherwise): starving the brain of excitement at the top and the
  Void's "force a spark" (the first is about the dopamine of novelty and the chase, like romance and drama; the spark comes
  from showers and microdoses); "not trip enhancers" and UMP's hoped-for return of psychedelic sensitivity (the first is
  about making a trip stronger, the second about tolerance coming back down in someone whose tolerance was abnormally high,
  which is why it says to lower the old dose); cold as a stress spike in the Void and your cold showers for anxiety (one
  is why cold ends the Void routine, the other what people use it for, and neither forbids the other).
- 🟢 **Explained in the text, or settled by your answers**: biology before psychology ("well, alongside"), D-serine against
  the NMDA brakes, agmatine not being a daily nutrient (the 7–14 day experiment), and heat against hot baths (your "No hot
  showers if heart rate elevated"); the mackerel's PS (your 20) and the D-serine cap (your 28a).
- 🔵 **Waiting on work of mine for your answers**: the Weeks 3–5 line (your 17: card W35, below), and the agmatine dose
  in Weeks 1–2 saying "once or twice daily" like the agmatine section, since your 26a has Weeks 1–2 follow it (unless you
  say otherwise); that line goes in with your next answers, checked by itself.
- 🟢 **11, answered ("11yes add that")**: Zhong 2023 is cited after Vialou in your paragraph, with Nestler 2008 back
  beside them (below).
- 🟢 **9 and 10, answered by your paragraph**: DeltaFosB stays the armor, and what it does is keep the learning from
  clicking, with the loop as what keeps it going. Nothing else in the article changes for them.

## For you to do

- 🟠 **Card W35 on the [cards page](https://claude.ai/artifact/9nENpt9AEJCB43a9Wy5jqn)** ([the card as a page](%(B)sfix-20261108/x1123a/REVIEW-X1123A.md)): your version of
  the Weeks 3–5 line for your 16a and 17. I can't find any more AI tells in it, and I see some human tells, like your own
  "there isn't enough data" and "to see how it feels", "don't take 5-HTP at all" and "If you're too numb to tell". Can you
  help show me the tells I'm missing? It goes in as yours.
"""

TODAY = """## Your message of 2026-11-23 17:25 UTC, and what I did

- 🟠 **The Weeks 3–5 line, checked by itself: six tries, none Human High in every window, so it's card W35** (above).
  Try 1 [AI Detected, 76%% AI](%(H)s236e28ea-f8e6-494c-a722-7f6f9cff7331) (AI Low, Human Low, AI Medium, AI High, AI Medium); try 2
  [Human Written](%(H)se5176e60-7a61-4e7d-b207-2a59adff9392) (Human High, Medium, Low, Medium); try 3 [Human
  Written](%(H)sfefcb049-c5e8-46eb-9eca-fc4ffd645f98) (High, Medium, High), the closest; try 4 [Human
  Written](%(H)sdac12965-24f9-4ad6-9595-652036780499) (High, Medium, High); try 5 [Human
  Written](%(H)s56c14834-60a8-45c3-a6bb-a3dceaf51bb9) (High, Low, Medium); try 6 [Mostly Human Written, 3%% AI](%(H)s811ba601-3400-4e8e-a9ef-9b677089f177)
  (Medium, High, Low, Low, Medium). 2.2 and 2.3 are marked answered once your version is in.
- 🟢 **Your 5-HTP warning is in**: the 5-HTP stop signs end "And rarely, people report anhedonia that goes on for weeks
  after they stop 5-HTP." By itself, that paragraph read [Human Written, every window High](%(H)se48362d5-bcae-42d3-ab11-2965f7404666)
  ([what went in](%(B)sfix-20261108/x1123a/APPLIED-X1123A.json)).
- 🔵 **Lion's mane and ashwagandha**: a new item before the agmatine warning, saying you'd leave both out, with the rare
  reports of lasting anhedonia and sexual dysfunction, and SSRIs and finasteride as the known cases. Two tries read AI by
  themselves: [AI Detected, 93.5%% AI](%(H)s50622455-2e3a-482e-ac66-0ae461f68592) (AI Low, AI High) and [AI Detected, 98.1%% AI](%(H)se169798f-7c09-4000-befc-1ddd7642b40e)
  (AI Low, AI High). Next: a fresh panel reads it for the tells I'm missing, I fix it until it reads right, and only then
  check it again.
- 🔵 **Agmatine's warning**: its sentence goes in the stop-signs paragraph at the top, which read [AI Generated, 100%% AI,
  High](%(H)s1eea33ab-e9b9-4bd4-b32d-0489aec27358) with it. That paragraph is model text, so it's mine to fix, and it's the one question 35 asks
  about, so I rewrite it once you've answered 35, with your sentence in, and check it then.
- 🟢 **What's reported on both sides** for the warnings: [the sources](%(B)sfix-20261108/x1122a/WARNINGS-SOURCES.md).
- 🟢 **The contradictions check, run again**: questions 34 to 55 above ([what became of each pair](%(CHECK)s)). It also
  found that my old note on question 23 was wrong: I'd marked it answered by 33b, but your answer 23 was about
  psychedelics, so question 42 asks it again.

"""


def main():
    text = P.read_text(encoding='utf-8')
    if '**🟣 34.' in text:
        sys.exit('questions 34 to 55 are already on the page')
    head_old = text[text.index('Last updated'):text.index('\n\nColours:')]
    text = text.replace(head_old, HEADER, 1)
    a = text.index('## Open questions')
    b = text.index('## Your answers of 2026-11-22 17:39 UTC')
    keys = dict(L=L, CHECK=CHECK, B=B, H=H)
    for n in (2, 3, 5, 7, 10, 13, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 30, 31, 35):
        keys['l%d' % n] = lines(n)
    text = text[:a] + (OPEN % keys) + '\n' + (TODAY % keys) + text[b:]
    old1 = """- 🔵 **Your new warnings** (lion's mane and ashwagandha, with SSRIs and finasteride as the known cases; agmatine and 5-HTP,
  weeks of anhedonia in rare reports): next, checked against what's reported on both sides, then written and checked in
  Pangram like any text of mine.
- 🔵 **16a and 17** still wait on their line's check; then the contradictions check runs again over the new text."""
    new1 = """- 🔵 **Your new warnings** (lion's mane and ashwagandha, with SSRIs and finasteride as the known cases; agmatine and 5-HTP,
  weeks of anhedonia in rare reports): the 5-HTP one is in; the other two are in progress (your message of 23 November,
  above).
- 🟠 **16a and 17**: their line used its six tries, so it's card W35 for your version (above)."""
    if old1 not in text:
        sys.exit('the 22 November bullets changed; edit by hand')
    text = text.replace(old1, new1, 1)
    P.write_text(text, encoding='utf-8')
    print('ok', len(text))


if __name__ == '__main__':
    main()
