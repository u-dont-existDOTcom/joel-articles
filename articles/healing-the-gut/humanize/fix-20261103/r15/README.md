# r15: his batch-9 answers, every term introduced at first use, the repeats cut

Joel, 2026-11-05 18:43 UTC (`../../../experiments/t14-answers/`): his batch-9 answers (`REVIEW-ANSWERS-b9.json`), "pr has
conflicts", "are you making sure this article is not redundant?", and "make sure every term is introduced once at first,
like enterocytes my readers won't know what those are ... you don't need to ask me when making those obvious changes ...
assume they have some basic knowledge of like a high school graduate".

`r15.md` is r12 (the text in his post) with the changes in `CHANGES.json`, built by `build_r15.py` (35 changes, 3,998
words). Nothing here is in his post yet.

## His answers

- **F9-1 (revise):** his own version of glutamine's paragraph goes in as he wrote it: "converted into" for my "turned
  straight into", the α-KG sentences joined, and the payoffs moved up. With F9-2's clause ("on top of what they get from
  their meals"), which he approved.
- **F9-2 (approved):** in, inside his F9-1 paragraph.
- **F9-3 (approved, "incorporate your research to make this more accurate and useful"):** the dose paragraph, reworded
  with the research; on the batch-10 page as F10-1, each change with its source.
- **F9-4 (approved):** the caution as approved (any active cancer, the oncologist, the 5g too, no portal vein), with what
  to do moved up to right after the warning, the payoff first; on the batch-10 page as F10-2. His own caution in his F9-1
  version (intestinal or liver cancers, the portal vein) was his fix of the old paragraph in his post, written before he
  approved F9-4; the card says so and invites him to Revise with his if he meant it.
- **F9-5 (answered):** glutamine left as a powder unsaid; away from meals, with why; an acute exposure is to toxins or
  pathogens; stress is every kind, said once where stress first comes up (block 3); start at 5g and add 1g a day in case
  of sensitivity.

## Sources for the dose paragraph (F9-3)

- Glutamine two hours before a 60-minute run at 30 C cut the gut's leak at every dose tested, the lowest 0.25 g per kg of
  fat-free mass, about 15g for a 70kg man: Pugh 2017, https://pmc.ncbi.nlm.nih.gov/articles/PMC5694515/
- 14g a day is the observed safe level for the long run; higher intakes were tested only briefly: Shao and Hathcock 2008,
  https://www.nutraingredients.com/Article/2008/04/18/crn-authors-risk-assessment-for-key-amino-acids/
- Amino acids share transporters, so labels say to take them without food:
  https://www.consumerlab.com/answers/must-i-take-amino-acid-supplements-on-an-empty-stomach/how_to_take_amino_acid
- Glutamine for active Crohn's: two small trials, no benefit: Cochrane 2016, https://www.cochrane.org/CD007348

## Terms (his rule, applied without asking)

Every term a high-school graduate wouldn't know is explained once, in the sentence that first uses it (28 notes, listed
in `b10/REVIEW-CARDS.md`, "Applied without a card", with the reason for each). The sources for the definitions are in the
receipts' `checked` lists (`checks/RECEIPT-*.json`): A Midwestern Doctor
(https://ibogaqueen.substack.com/p/critical-analysis-of-amd-and-their), DMSO (https://respectfulinsolence.com/?p=43510), A1 milk
(https://en.wikipedia.org/wiki/A2_milk), diosmin
(https://prolekare.cz/topic/venous-insufficiency/detail/diosmin-and-hesperidin-what-does-pharmacokinetics-show-121991),
berberine (https://en.wikipedia.org/wiki/Berberine), zonulin (https://www.ncbi.nlm.nih.gov/pubmed/28123927), colostrum
(https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1135735/1/Bovine-colostrum.pdf), liposomal
(https://neuroganhealth.com/blogs/news/liposomal-vs-capsule-supplements), BPC-157
(https://en.wikipedia.org/wiki/BPC-157), resistant starch (https://www.frontiersin.org/articles/10.3389/fnut.2024.1369950/full),
zeolite (https://pubmed.ncbi.nlm.nih.gov/30999685/), FODMAPs (https://pubmed.ncbi.nlm.nih.gov/23588241/), orthomolecular
medicine (https://www.topdoctors.co.uk/medical-dictionary/orthomolecular-nutrition?amp=1), phosphatidylcholine
(https://uofmhealth.org/health-library/hn-2873001).

Asked, because I can't introduce them without guessing: "HRP" (F10-4), and which Gemini mode readers use (F10-5).

## Repeats

Read through for repeats. Cut: the colon paragraph's restatement that the small intestine runs on glutamine (said twice
above it), Phase 5's pointer to the fuels (step 4 just above points there), and the stacks section's second definition of
H. pylori and its heartburn sign (both under Parasites). Kept, because each says something new where it is: the
diet-first line in the stacks section and in Phase 3, the butyrate line under diverticulosis, glutamine's callback in the
plant-food cause, Phase 5's meal spacing, the berberine pointers. Asked: the intro and the Gem section both say he
consolidated the books for Gemini and name different modes (F10-5).

## Checks (Pangram 4.1, the web app, his account)

Each stretch of r15 with a change in it, checked by itself (`checks/`, texts `CHECK-*.txt`, receipts `RECEIPT-*.json`):

| stretch | blocks | prediction | result |
|---|---|---|---|
| A, the intro | 1-3 | Human 0.7 (#155) | [Human Written, AI 0%](https://www.pangram.com/history/0c41b0cf-ea7c-4cfe-9898-18cbb4f08635), High |
| B, impaction to parasites | 9-14 | Human 0.6 (#156) | [Human Written](https://www.pangram.com/history/7b694c0d-d080-4b92-888f-57f4ce851842), High but a 2-word split at "For H." |
| C, plant foods and leaky gut | 16-25 | Human 0.55 (#157) | [Mostly Human, 4.7% AI](https://www.pangram.com/history/02aaf3fa-f757-426f-a6c9-0ee74b8ad0fb): a miss |
| D, the fuels | 26-31 | Human 0.6 (#158) | [Human Written, AI 0%](https://www.pangram.com/history/626fb9ca-c769-4775-bebc-2483576c71b5), one window, High |
| E, IBS and low acid | 32-33 | Human 0.6 (#159) | [Human Written](https://www.pangram.com/history/361b991e-c166-4273-bafa-fe4987e35938), High |
| F, the Gem note | 35-36 | Human 0.65 (#160) | [Human Written, AI 0%](https://www.pangram.com/history/c7976353-5728-4a11-8ad5-77db210e11a8), High |
| G, Phase 1 | 40-43 | Human 0.6 (#161) | [Human Written](https://www.pangram.com/history/50e180ec-087b-4200-9bb3-27bc289fa1dc), High |
| H, Phase 2 | 45-47 | Human 0.5 (#162) | [AI Detected, 65%](https://www.pangram.com/history/de89477f-ceb5-4762-b6d7-87601979e4d7): a miss |
| I, Phase 3 | 50-56 | Human 0.5 (#163) | [Human Written](https://www.pangram.com/history/6474197b-1c7e-41e7-b613-c915a69bbfd0), High but splits at "Dr." and "C." |
| J, Phase 4 | 58-60 | Human 0.6 (#164) | [Human Written](https://www.pangram.com/history/d22546ab-78b1-438d-8da3-19b18cf50712), two of his sentences Medium |
| K, Phase 5 | 62-67 | Human 0.6 (#165) | [Human Written](https://www.pangram.com/history/0468d290-7082-4a9b-b49c-cc83e257c2ce), High but splits at "Dr." and "L." |
| L, the stacks | 79-82 | Human 0.6 (#166) | [Human Written](https://www.pangram.com/history/a75a3ea5-13d9-420c-937a-8178a5f455ce), his pregnancy sentence Medium |

The two misses, and their second try (`checks/try2.py`, narrowed first, E343):

- **C:** my notes on colostrum and BPC-157 were sentences after the items that named them (AI-Generated Medium, Human
  Low), and the tight-junctions note sat between "signal" and "to open" (Human Medium). Each term explained in the
  sentence that first names it, his two zonulin sentences joined: the lead and colostrum alone [Human Written, AI
  0%](https://www.pangram.com/history/7218250e-561f-4d94-bc78-cbeb42cc7b97), one window, High (#167); the four items
  [Human Written](https://www.pangram.com/history/88b2cacf-5e07-499a-a89e-f38c553f28a1), one window, High (#168); the
  stretch [Human Written, AI 0%](https://www.pangram.com/history/47069558-4b1d-4701-a3f6-c712041f1866) (#170), High but
  the beta-glucans item Medium and the resistant starch item Low, each in its own short window (the same words read
  High in #168).
- **H:** the opening put the point after two doctors and their books (AI-Generated High in his post, #142), and my
  FODMAP note split his "go A or B". The point first, as Phases 1, 3 and 5 open, and the note joined to his "Either way":
  the two paragraphs [Human Written](https://www.pangram.com/history/c7517cd3-0b56-4a28-b2d0-b8c2de287a48), one window,
  High (#169); Phase 2 whole [Human Written, AI 0%](https://www.pangram.com/history/31e8d763-563d-4c55-aa5f-04218bf2a721)
  (#171), Human windows, three Medium where it splits at "Dr.". This is card F10-3: his opening, reordered.

Both stretches have now had their two tries.

## Lessons

E368 (his usual fix first on any window below High: where the point lands, the join, the plain word; enforced in
`pangram_ledger.py predict --first-fix`) and E369 (every term explained once where first used, asking only when unsure;
enforced in `sense_receipt.py check`), in `docs/HUMANIZATION-GATE.md`.

## Batch 10

The marking page: https://claude.ai/artifact/NfPt7HckprSDhtuCm84P5E (`b10/`, review id
`healing-the-gut-b10-r15-20261105`): F10-1 the dose, F10-2 the caution, F10-3 Phase 2's opening, F10-4 HRP, F10-5 the
Gemini mode.
