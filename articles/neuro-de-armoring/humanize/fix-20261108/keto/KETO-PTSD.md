# Ketosis in people with PTSD: the sources checked for SC-48b (2026-11-11)

After Joel's message of 2026-11-11 22:53 UTC ("ok and also ketones do seem to help ppl with ptsd idk why youre research
is always wrong", [word for word](../joel-20261111-2253-message.txt)), with GPT's review of ketogenic diets and ketone
salts for PTSD ([as he pasted it](../joel-20261111-2253-gpt-ketone-review.txt)). Block 48 ended on my "Whether ketosis
does that in people hasn't been tested." The card is SC-48b ([the card](REVIEW-X1111C.md); [its build](build_x1111c.py)).

## Searched

- PubMed: (ketogenic OR ketosis OR ketone OR beta-hydroxybutyrate OR "3-hydroxybutyrate") AND (PTSD OR "posttraumatic
  stress" OR "post-traumatic stress"), newest first: 109 hits; the 40 newest scanned by title, the PTSD ones read.
- ClinicalTrials.gov: PTSD with ketogenic OR ketone OR beta-hydroxybutyrate: 9 trials, 3 about ketosis.

## Human studies of ketosis in PTSD

| Study | What | Found | Checked |
|---|---|---|---|
| [Edwards, et al, 2024](https://pubmed.ncbi.nlm.nih.gov/39588043/), doi 10.3389/fnut.2024.1406366 (NCT05415982) | Keto diet with BHB salts, 4 weeks, Oslo outpatients, single-arm | 3 of 4 eligible included, 2 finished; ketosis on 87% of days; PCL-5 70 to 50 and 50 to 40, "a reliable and clinically meaningful improvement"; adverse reactions (mostly headache, fatigue) on 70% of days, none serious | Abstract, PubMed |
| [Bellamy & Laurent, 2025](https://pubmed.ncbi.nlm.nih.gov/40626225/), doi 10.3389/fnut.2025.1600123 | Case: woman, 38, PTSD with bipolar II, ADHD, binge eating; 8-week program with support, intermittent fasting | PCL-5 80 (its maximum) to 0 by week 12, every scale to 0; three years of trauma-focused therapy "did not notably improve her symptoms"; no psychiatric drugs ever; the diet was her only therapy then; on an animal-based diet for a year before; best at blood ketones of 3 to 5 mmol/L; the authors say her other conditions limit what it shows about PTSD alone | Full text, PubMed Central |
| [Laurent, 2026](https://pubmed.ncbi.nlm.nih.gov/41783812/), doi 10.3389/fnut.2026.1755107 | Case: woman, 45, PTSD from military sexual trauma, "nonresponsive to conventional interventions including psychotherapy and pharmacotherapy"; 25-week keto program | PCL-5 32 at the program's start to 2 at 27 weeks; she cut carbohydrates 9 days before it began. GPT's further points (an earlier 64 from two years before; supplements, low-dose naltrexone, exercise) are from the full text, not checked here | Abstract, PubMed |
| [Youssef, et al, 2022](https://pubmed.ncbi.nlm.nih.gov/36282607/), doi 10.12788/acp.0088 (registered as NCT04083352) | BHB salts (14 g a day) against a placebo, 6 weeks, double-blind | 21 recruited; no difference between the groups before (p = 1.00) or after (p = .60); the ketone group's median PCL-5 fell 58.5 to 54.0 (p = .0003), the placebo group's stayed at 34; the authors: "The small sample size limited the study and likely contributed to the lack of significance." GPT's reading of the full paper (group by time p = .80; 8 and 6 at follow-up; maker's funding; blood BHB not measured) not checked here | Abstract, PubMed |
| [NCT07415590](https://clinicaltrials.gov/study/NCT07415590) | Keto diet, 12 weeks, 6 adults, Munich, single-arm feasibility | Completed 7 August 2026; no results posted | ClinicalTrials.gov |
| [Integrative review, 2026](https://pubmed.ncbi.nlm.nih.gov/42780737/), doi 10.3389/fpsyt.2026.1854499 | 16 articles: 9 human, 4 animal, 3 reviews | "Preclinical data suggestive of potential efficacy were identified, while only minimal reliable information is available from human studies"; calls for randomized trials | Abstract, PubMed |

## Other side, and what wasn't used

- [A Ukrainian case-control study](https://pubmed.ncbi.nlm.nih.gov/41345238/) (doi 10.1038/s41598-025-31138-3; 698
  young adults): PTSD went with more adherence to restrictive diets, keto among them. An association, with no direction;
  it says nothing about what the diet does to PTSD. Not used.
- Rat studies: BHB in a PTSD model (PMID 41412336, 2025) and MCT oil in a single-prolonged-stress model (PMID 41942638,
  2026). They add nothing to block 48's mouse finding. Not used; GPT's 2020 rat study not checked.
- The 2026 analysis of keto-diet side effects across conditions (about 43% with at least one), from GPT's review: not
  checked; it belongs to the read of the whole protocol, with Strategy B's safety.
- The integrative review's note that a second report (Locklin and colleagues) may be the same cohort as Youssef's: not
  checked; nothing in the card rests on it.

## What changes in the article

Block 48's last sentence becomes three: the Oslo study, the two cases, and the limit (no controlled trial of the diet;
the one placebo-controlled trial of BHB salts too small to tell). The one-line summary of Youssef 2022 I gave in chat
("the two groups ended up no different") made a trial too small to tell sound like a negative: lesson neuro-2026-11-11c.
Strategy A's "need the fog gone fast" with the salts (block 95) goes to the read of the whole protocol, beside the
Youssef trial.

## His clause, checked (his version of SC-48b, answers exported 2026-11-12 18:23 UTC)

His version added to the last sentence: "although we can see some astounding BHB salt reviews on forums, like for brain
injury repair (a Reddit thread), and the salts work for rats with trauma, although not nearly as proven for humans as the
keto diet is (Engelhardt, et al 2026)". It went in as he wrote it ([apply_x1111c.py](apply_x1111c.py), with the fixes it
lists: a broken link, a typo, the citation's brackets, the full stop, the citations' links).

- **The forum reviews**: his link is to a Reddit thread, blocked to this session's tools as content, so not read. His
  point and his link, as firsthand reports.
- **Engelhardt 2026** is the integrative review above ([PubMed](https://pubmed.ncbi.nlm.nih.gov/42780737/); Engelhardt R,
  Ogedengbe JO, ... Potenza MN), cited as he cites it.
- **"the salts work for rats with trauma"**: the review's rodent studies gave BHB by injection ("directly injected
  β-hydroxybutyrate, which resulted in reduced post-traumatic anxiety-like behavior"), MCT oil, or sodium acetate.
  [Yamanashi, et al, 2020](https://pubmed.ncbi.nlm.nih.gov/33303808/) (doi 10.1038/s41598-020-78410-2; full text read in
  PubMed Central): DL-BHB in buffered saline, 250 mg/kg under the skin, eased anxiety-related behavior after single
  prolonged stress and partly lowered TNF-α. [Jung, et al, 2025](https://pubmed.ncbi.nlm.nih.gov/41412336/) (doi
  10.1016/j.jad.2025.120940; abstract): BHB 250 mg/kg by injection twice a day for a week prevented anxiety and fear
  behaviors and normalized corticosterone in male and female rats. [Yoshioka, et al, 2026](https://pubmed.ncbi.nlm.nih.gov/41942638/)
  (abstract): MCT oil by mouth raised BHB and reduced anxiety-like behavior. None gave the salts by mouth. Card SC-48c:
  "BHB injections work for rats with trauma".
- **"not nearly as proven for humans as the keto diet is"**: the review: "no efficacy for PTSD in humans was demonstrated
  against a control group", and "Another open question remains whether supplementation can achieve effects comparable to
  ketogenic diets. While supplementation may rapidly elevate circulating ketones, dietary interventions may exert more
  sustained effects". Card SC-48c: "although in humans it's still an open question whether the salts work as well as the
  keto diet".
- I had left the rat studies out of SC-48b as adding nothing to the mouse finding. They are the closer evidence, BHB itself
  in a trauma model, and his clause put them in (lesson neuro-2026-11-12a).
