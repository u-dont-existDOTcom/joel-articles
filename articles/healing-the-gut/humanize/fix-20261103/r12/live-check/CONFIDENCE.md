# Every window that isn't High-confidence Human

Made by `tools/humanization/window_confidence.py`. A window that reads Human at Medium or Low confidence is listed with the AI ones: less than High is what a later Pangram version is likeliest to read AI (Joel, 2026-10-26; gate E278). "Calibrated" is Pangram's calibrated confidence for the window, where the result gives it.

## RESULT.json

Mostly Human Written (https://www.pangram.com/feed/e3a65841-a626-4b34-aad7-62b9dfa48ada).

Windows: Human High 11, Human Medium 11, Human Low 7, AI Low 14, AI Medium 2, AI High 2.

| # | read | calibrated | words | where | text | whose |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Human Low | 0.783 | 49 | Some Causes of poor gut health, P19 | If the cells lining your small intestine (called enterocytes) or the colonocytes lining your large intestine don't get that energy, the barrier loosens up. Then | approved wording, r10 |
| 2 | Human Medium | 0.914 | 4 | Some Causes of poor gut health, P20 | L-Glutamine (watch Dr. | r10 |
| 3 | Human Low | 0.727 | 18 | Some Causes of poor gut health, P20 | Rhonda vid) is the main fuel for your enterocytes, and for your immune cells when they're activated. | r10 |
| 4 | AI Low | 0.503 | 14 | Some Causes of poor gut health, P20 | It doesn't have to go through the complicated digestive steps other nutrients do. | r10 |
| 5 | AI Low | 0.503 | 13 | Some Causes of poor gut health, P20 | Inside the mitochondria, it gets turned straight into alpha-ketoglutarate, or α-KG. | r10 |
| 6 | AI Low | 0.503 | 17 | Some Causes of poor gut health, P20 | The α-KG goes into the citric acid cycle, which is how the mitochondria make their energy. | r10 |
| 8 | Human Medium | 0.975 | 61 | Phase 1: The Pre-Flight Safety Check, P1 | This protocol is meant to be done in phases. Don't skip ahead, since you only move on to the next phase if the one you're on doesn't clear up your symptoms. / B | approved wording, r10 |
| 10 | Human Medium | 0.971 | 62 | Phase 1: The Pre-Flight Safety Check, P2 | Are your pupils dilated all the time? Are you missing your gag reflex? Then according to Hale, you're stuck in fight or flight mode (which in medical lingo is c | r10 |
| 11 | Human Low | 0.575 | 20 | Phase 1: The Pre-Flight Safety Check, P2 | Both of those help to mechanically release the vagus nerve so your body can switch into rest and digest mode. | r10 |
| 12 | Human Low | 0.761 | 23 | Phase 1: The Pre-Flight Safety Check, P3 | Now let's have a look at your bile function. Do you burp extra (not just like one little burp) after fatty meals? | r10 |
| 13 | Human Medium | 0.963 | 14 | Phase 1: The Pre-Flight Safety Check, P3 | Do your stools float (like it's hard to flush), or look like clay? | r10 |
| 14 | Human Low | 0.700 | 73 | Phase 1: The Pre-Flight Safety Check, P3 | Then your bile is stagnant (not flowing well), and Hale says if you take antimicrobials now, you'll get a herx reaction: the dying microbes release toxins you c | approved wording, r10 |
| 15 | AI Low | 0.503 | 3 | Phase 2: The Reset, P1 | This is Dr. | r10 |
| 16 | AI Low | 0.649 | 8 | Phase 2: The Reset, P1 | Michael Ruscio (Healthy Gut, Healthy You) and Dr. | r10 |
| 17 | AI High | 0.992 | 28 | Phase 2: The Reset, P1 | Mark Pimentel (The Microbiome Connection): calm the inflammation down and starve the overgrowths, no harsh chemicals. / Diet-wise, go Paleo-Low FODMAP (Ruscio)  | r10 |
| 18 | AI Low | 0.855 | 11 | Phase 2: The Reset, P2 | Either way you stop feeding the bacteria in your small intestine. | r10 |
| 19 | AI Low | 0.566 | 3 | Phase 2: The Reset, P3 | And no snacking! | r10 |
| 20 | Human Medium | 0.982 | 22 | Phase 2: The Reset, P3 | Pimentel wants meals 4-5 hours apart, strictly, so the Migrating Motor Complex (MMC) gets to sweep your gut clean in between. | r10 |
| 22 | Human Medium | 0.983 | 2 | Phase 3: The Purge, P1 | Michael Ruscio. | r10 |
| 24 | Human Medium | 0.914 | 5 | Phase 3: The Purge, P5 | boulardii, and Soil-Based organisms. | r10 |
| 25 | Human Low | 0.690 | 47 | Phase 3: The Purge, P6 | That's to maintain diversity and prevent opportunistic infections (like C. diff) during the kill phase. / And if all that failed, the overgrowth is too severe o | approved wording, r10 |
| 26 | AI Low | 0.575 | 20 | Phase 3: The Purge, P6 | That's a 2-3 week liquid-only diet (predigested nutrients), which starves the bacteria completely while still nourishing you. | r10 |
| 28 | Human Medium | 0.985 | 5 | Phase 4: The Investigation, P2 | So check your organs (Brown). | r10 |
| 29 | Human Low | 0.680 | 5 | Phase 4: The Investigation, P2 | Is it Exocrine Pancreatic Insufficiency? | r10 |
| 30 | AI Low | 0.575 | 31 | Phase 4: The Investigation, P2 | You'd test for that with Stool Elastase, and treat it with high-dose enzymes. Or is it Bile Acid Diarrhea? That test is SeHCAT, and the treatment is bile binder | r10 |
| 32 | AI Low | 0.503 | 16 | Phase 5: Restoration & Maintenance (Let's Play Gardener!), P1 | Once you're clear of infection, you have to rebuild a diverse ecosystem to prevent relapse. | r10 |
| 33 | AI Low | 0.503 | 1 | Some Causes of poor gut health, P20 | Dr. | his |
| 34 | AI Low | 0.503 | 9 | Phase 5: Restoration & Maintenance (Let's Play Gardener!), P1 | William Davis is back for that, along with Dr. | r10 |
| 35 | AI Low | 0.531 | 4 | Phase 5: Restoration & Maintenance (Let's Play Gardener!), P1 | Will Bulsiewicz (Fiber Fueled). | r10 |
| 36 | AI Low | 0.791 | 18 | Phase 5: Restoration & Maintenance (Let's Play Gardener!), P2 | Start by re-seeding with Davis's high-dose "SIBO Yogurt", fermented for 36 hours. It contains L. | r10 |
| 37 | AI Medium | 0.962 | 23 | Phase 5: Restoration & Maintenance (Let's Play Gardener!), P2 | reuteri, to heal the lining and boost oxytocin, and L. gasseri, to produce bacteriocins that kill SIBO. / Then feed the new healthy bacteria. | r10 |
| 38 | AI High | 0.994 | 18 | Phase 5: Restoration & Maintenance (Let's Play Gardener!), P3 | Bulsiewicz says to slowly titrate plant diversity back into your diet, aiming for 30+ different plants per week. | r10 |
| 39 | AI Medium | 0.951 | 24 | Phase 5: Restoration & Maintenance (Let's Play Gardener!), P4 | Does anyone count their plants? / Continue Pimentel's strict meal spacing from Phase 2 (4+ hours), forever, to keep the MMC cleaning wave active. | r10 |
| 41 | Human Medium | 0.974 | 4 | Phase 6: Refractory Cases, P2 | Check your environment (Nathan). | r10 |
| 43 | Human Medium | 0.970 | 4 | Phase 6: Refractory Cases, P3 | Then check the brain. | r10 |
| 45 | Human Medium | 0.933 | 1 | Some Causes of poor gut health, P20 | Dr. | his |

