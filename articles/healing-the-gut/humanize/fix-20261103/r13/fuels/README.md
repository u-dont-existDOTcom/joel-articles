# r13: the fuels stretch, paragraph by paragraph (2026-11-04)

Joel, 22:35 UTC: "then the fuels stretch" (`../../../../experiments/t12-answers/`). The live post's check (`../../r12/live-check/`) read P20's three glutamine-mechanism sentences AI Low, and P19's last two sentences and P20's first Human Low. The r12 cut of the stretch (#140) had also read the caution's last two sentences AI Low.

## P20, glutamine: fixed on the first try

- **The newcomer read** (`links/`, a fresh reader with P19 as context): 15 questions. Five are about the three AI sentences:
  - what the digestive steps are, and why glutamine skips them;
  - whose mitochondria, and how the glutamine gets into them;
  - what alpha-ketoglutarate is;
  - what goes round in the citric acid cycle;
  - whose energy.
  The other ten are about his kept sentences. Two of them are real logic gaps in his words, which go to him: "faster" against the paragraph before's "not enough", and "extra" against "faster".
- **The draft** (`DRAFT-P20-v1.txt`) changes only the three AI sentences and states those links in that order:
  - most food has to be digested, and for protein that means amino acids;
  - glutamine already is one, so the enterocytes take it in as soon as it reaches them;
  - their mitochondria turn it into a-KG, one of the acids in the citric acid cycle itself.
  - "straight" goes, since it takes two steps: glutamine becomes glutamate, then a-KG ([Frontiers in Medicine 2022](https://www.frontiersin.org/articles/10.3389/fmed.2022.1035335/full); [Nutrients review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6834172)).
  - "α-KG" becomes his own spelling, "a-KG" (his card of 11:32 UTC).
- The fresh read of the draft (`links/draft/`) found nothing in the new sentences. `hidden_links.py check` passes. The blind meaning check passed (`MEANING-VERDICTS.json`), with each link checked against a source.
- **The check**, with P19, the explanation it leans on (E349), prediction #144 Human at 0.55: [Human Written, 100%](https://www.pangram.com/history/e28d97cb-50c2-4f13-89b9-ea19f2507a23), one window, Human High, 244 words. P19's Low windows went too.

## P22, the caution

- **Its own pair first** (E343), with P21, the dose it points at, unchanged. Prediction #145, Human at 0.5: [AI Detected, 36%](https://www.pangram.com/history/8563cfe5-5f52-43ad-903c-f5e1fdae01ca), a miss.
  - P21's first two sentences: Human Low. Its last: Medium.
  - P22's first sentence: Human Low. "So if you have an active colon or liver cancer, don't raise the dose that high.": AI Low. The liver sentence: AI Medium.
  - So the caution's windows are its own, not P20's.
- **The newcomer read** (`links-p22/`): 7 questions.
  - What "that high" means, how the glutamine gets into the blood if the gut cells burn it, and why the liver getting it first matters: the draft answers these.
  - Why the colon: the original gives no reason. Swallowed glutamine is mostly taken up in the small intestine, not the colon ([human splanchnic study, Amino Acids 2017](https://link.springer.com/content/pdf/10.1007/s00726-016-2344-7.pdf)). Many colorectal cancers do depend heavily on glutamine ([Cancers 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10930819)). That's his call: card.
  - Whether the 5g baseline is fine with an active cancer: the original doesn't say. Card.
- **The draft** (`DRAFT-P22-v2.txt`): the warning and its reason in one sentence, "don't go up to the 10-30g", then why the liver. Sources:
  - The gut and liver take up most of a small swallowed dose on its first pass (74% in [Hankard 1995](https://pubmed.ncbi.nlm.nih.gov/7485479/)), and less of a large one (53%), so more of a big dose gets past them.
  - Bigger oral doses raise blood glutamine ([Ziegler 1990](https://scilit.com/publications/3818c7c307b06a89e57d20b459c23ead)).
  - These links come from search results; the session couldn't open PubMed itself this turn (the fetch needed an approval nobody was there to give).
- **Its second try** (`DRAFT-P22-v3.txt`; the v2 draft's own fresh read showed "more than your gut cells can use" made P21's 10-30g sound wasted, so v3 says "passes through"). Both drafts passed the blind meaning check. Prediction #146, Human at 0.5: [AI Detected, 26%](https://www.pangram.com/history/84f98fca-d6d3-42b8-b14e-9b8e888e5601), a miss.
  - The warning, now joined to its reason, reads Human Medium (it was AI Low). P21's last sentence went from Medium to High.
  - The liver sentence reads AI High: v3 made it one long mechanism chain, the shape P20's AI sentences had.
- **The tell panel** (E346, since the pair had read AI twice; `panel-p22/PANEL.md`): Sonnet and Haiku. Codex wasn't asked: it runs on his laptop, and nobody was there to approve the route this turn.
  - Agreed: the closing payoff ("so a cancer there would get it first, while it's still concentrated"), the step-by-step chain with its relative clause, and the "CAUTION:" label.
  - The label stays: it's his own device. His original post has "CAUTION :" over his diverticulosis note.
  - Called human: "don't go up to the 10-30g", "grab glutamine too", "With a dose that big".
- **The third try** (`DRAFT-P22-v4.txt`): the claim before its reason, no closing payoff, and no second "so": "a tumor in your liver gets to it first, because the blood from your gut goes to your liver before anywhere else (through the portal vein)". "Don't go up to" became "stay off".
- **Stopped before a third try:** v4's blind meaning check failed it (`MEANING-VERDICTS-P22-v4.json`). "A tumor in your liver gets to it first" moves the original's claim from the liver to a tumor in it, and that link is wrong. Liver tumors get nearly all their blood from the hepatic artery, not the portal vein ([hepatic microcirculation review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3036477): "predominantly supplied by the hepatic artery and not or only minimally by the portal vein"; [embolotherapy review](https://pmc.ncbi.nlm.nih.gov/articles/PMC7437993)). v3's checker had passed the same link in "a cancer there would get it first".
  - v5 (`DRAFT-P22-v5.txt`) has the same link, so it wasn't checked either.
  - The caution's own reasons don't hold up well. The colon has none, and swallowed glutamine mostly doesn't reach it. The liver's reason is true of the organ, but a tumor there is fed mainly by the hepatic artery.
  - What does hold: many tumors use glutamine avidly ([Souba 1993](https://pubmed.ncbi.nlm.nih.gov/8257221/)), KRAS-mutant colorectal cancers among them ([Cancers 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10930819)). Yet in most clinical studies glutamine supplements haven't sped tumor growth (the review summarized at [iris.uniroma1.it](https://iris.uniroma1.it/handle/11573/74944)).
  - Changing what a warning says is his call (E348), so the caution goes to him on the next marking page (`CARDS-DRAFT.md`) before any rewrite. Its lineage stays at 2 tries.
- The links in this README come from search results and the readers' own checks. The session couldn't open PubMed itself this turn: the fetch needed an approval nobody was there to give.

