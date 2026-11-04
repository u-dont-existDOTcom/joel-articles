# The stacks section, fixed before any article check (r08, 2026-11-04)

Joel, 14:41 UTC: "no the whole article doesn't decide, we need to first fix any windows we can see before we check the article" (gate E354). In its own API check (r07) the section read [AI, 5% human](https://www.pangram.com/history/5b33aa60-158a-4edd-b58a-04762dbc2786): 12 of its 13 windows were AI, his three-category paragraph's included.

**What found the fixes**
- `links/`: a newcomer read of the section, with the phases and the Leaky gut item as context (29 questions). `hidden_links.py check` is clean on `DRAFT-SECTION.md`; the questions about his paragraph are dropped with a note and go to him on card F6-2.
- `panel/`: the tell panel (Codex, Sonnet, Haiku). Its agreed tells were his "three categories:" lead-in, his butyrate and "or similar compounds" items, my Ruscio blurb and my red-flag list. Codex's whole-section read: "The progression from opening caveat through categories, product comparisons, dosing guidance and a comprehensive safety disclaimer resembles an AI-polished explainer."
- The kits were checked against the makers' pages: [Total Gut Restoration](https://fullscript.com/catalog/products/total-gut-restoration-kit-1), [Ruscio's kit](https://store.drruscio.com/products/leaky-gut-support-kit), [GI Revive](https://www.priceplow.com/designs-for-health/gi-revive).
- The safety reasons were checked against [NCCIH](https://content.govdelivery.com/accounts/USNIHNCCIH/bulletins/378abdf) (probiotics and a weak immune system) and [NCCAM](https://webarchive.library.unt.edu/web/20121017011343/http://nccam.nih.gov/health/goldenseal) (goldenseal and berberine in pregnancy). [ECCO](https://ecco-ibd.eu/publications/ecco-news/item/is-the-low-residue-diet-still-relevant.html) doesn't support saying fiber worsens an IBD flare, so the draft doesn't say it.
- Every changed paragraph passed the blind meaning check (`MEANING-VERDICTS.json`, `-2`, `-3`).

**The checks**

They ran in the Pangram web app: the API account answered "HTTP 402: Insufficient credits" at the first text, so nothing was charged there. Each prediction was frozen first (ledger #106 to #112).

| paragraph | read | link |
| --- | --- | --- |
| P1, first try (an explainer) | AI (Medium 18, High 104) | [result](https://www.pangram.com/history/31a8b177-a934-4175-9514-18276fc6a374) |
| P1, second try (his brackets, pointing back) | Human (High, 83) | [result](https://www.pangram.com/history/4c5c8973-ece2-4ce4-be73-35d40c8520d4) |
| his three categories + my kits | AI Detected 64% (his: AI High 50, AI Low 47; my kits: Human High 28, Human Low 31, AI High 63) | [result](https://www.pangram.com/history/38b2da46-e72e-429a-8568-076737a8976f) |
| P80, the cleanse stacks | Human (High, 94) | [result](https://www.pangram.com/history/8c033529-f8b4-4d6f-adfe-0704d4ba6478) |
| P81, start low and the doctor, first try | AI (High, 162) | [result](https://www.pangram.com/history/4a617063-c5be-4d4a-8cb2-afc19152d7a2) |
| P81, second try | AI (High, 158) | [result](https://www.pangram.com/history/291631e3-f16c-4de2-af42-8b4099133719) |
| the glutamine caution, alone | Human (Low, 63) | [result](https://www.pangram.com/history/2f0c9ce2-3bb6-4167-a237-2c15ed823533) |

The misses are explained in the ledger as "explainer structure". My first answers to the newcomer's questions came as a dictionary-style definition, the phases recapped in brackets, and "so" clauses pairing each item with its use. His versions that read Human answer the same questions in a talking order, point back instead of recapping, and define in brackets.

**Where it stands**
- `../r08.md` has the clear versions (E291).
- The marking page `../b6/REVIEW-CARDS.md` (artifact https://claude.ai/artifact/Q4Y1wy3G1ZPMfx5Ly9xGc4) has six cards:
  - two changed points that read Human (High): F6-1 and F6-4;
  - his three-category paragraph with my suggestion: F6-2;
  - help requests for the kits (F6-3, one try left) and for the start-low paragraph (F6-5);
  - the caution: F6-6. It was checked without the dosing paragraph it leans on, so its Low isn't comparable with the earlier check.
- The section gets its own check once these are settled, and the article after that (E354).
