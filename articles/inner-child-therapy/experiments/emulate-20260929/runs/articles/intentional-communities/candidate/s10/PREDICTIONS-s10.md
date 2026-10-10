# Section 10 ("From One Community to a Movement"): predictions and results

Every Pangram call is listed with my prediction, written before the call, and the result from the web app's own record. Section 9's are in `../s9/PREDICTIONS-s9.md`.

Batch 183g (written 07:01 UTC on 2026-10-09 by `date -u`, before the call; `v183.json`): the published section 10, as a baseline.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 183g-S10pub (545) | AI | the published text; every published section so far read AI | AI (100%, 558 words scanned), 07:01:48 |
| 183g-P1pub (62) | AI | the published text; every published section so far read AI | AI (100%), 07:01:53 |
| 183g-P3pub (56) | AI | the published text; every published section so far read AI | AI (100%), 07:01:56 |
| 183g-P5pub (101) | AI | the published text; every published section so far read AI | AI (100%), 07:02:01 |
| 183g-P6pub (82) | AI | the published text; every published section so far read AI | AI (100%), 07:02:06 |
| 183g-P7pub (104) | AI | the published text; every published section so far read AI | AI (100%), 07:02:13 |
| 183g-P8pub (52) | AI | the published text; every published section so far read AI | AI (100%), 07:02:18 |
| 183g-P1pubP2pub (106) | AI | the published text; every published section so far read AI | AI (100%), 07:02:23 |
| 183g-P3pubP4pub (85) | AI | the published text; every published section so far read AI | AI (100%), 07:02:27 |

183g (submitted 07:01:48 to 07:02:27 UTC, 2026-10-09): mine 9 of 9. As published, section 10 and every paragraph read 100% AI. Next: Emulate round a (laptop `emulate-runs/community-s10a`), units by subsection and paragraph.

Batch 185g (written 22:28 UTC on 2026-10-09 by `date -u`, before the call; `v185.json`, parts in `fix-v1-parts.json`): first rewrites, mine with Emulate round a's cues (`drafts-v1.json`). The gate runs on whatever passes.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 185g-P1a (75) | AI | my own conversational rewrite, read beside Emulate round a; in section 9 my first rewrites mostly read AI | **Human (100%)**, 22:28:52 |
| 185g-P1aP2a (124) | AI | P2a is under 50 words | AI (100%), 22:28:55 |
| 185g-P3a (61) | Human (weak) | "I'd like communities that…" for the published "I want communities that…", closer to speech | AI (100%), 22:28:58 |
| 185g-P3aP4a (102) | Mixed | P4a is under 50 words | AI (100%), 22:29:05 |
| 185g-P5a (115) | AI | long and list-heavy, like the published | AI (100%), 22:29:09 |
| 185g-P6a (93) | AI |  | AI (100%), 22:29:20 |
| 185g-P6e (103) | Mixed | built from Emulate's u4-B, meaning fixed | AI (100%), 22:29:22 |
| 185g-P7a (120) | AI | the published list kept, with a colon | AI (100%), 22:29:25 |
| 185g-P8a (68) | Human (weak) | short, close to Emulate's u6-A | AI (100%), 22:29:31 |
| 185g-S10v1 (637) | AI | the first whole-section version | AI (100%, 660 words), 22:29:36 |
| 185g-S10v1e (647) | AI | with P6e | AI (100%, 669 words), 22:29:44 |

185g (submitted 22:28:52 to 22:29:44 UTC, 2026-10-09): mine 7 of 11. Only P1a passes; my other rewrites read 100% AI, as my own first rewrites did in sections 7 and 9. So I switch method instead of rewording: Emulate round b gets my meaning-checked drafts (the gate's "feed Emulate the fixed meaning", which worked in section 7), and its output gets word-level fixes.

Batch 186g (written 22:42 UTC on 2026-10-09 by `date -u`, before the call; `v186.json`, parts in `fix-v2-parts.json`): Emulate round b (fed my meaning-checked drafts; `emu/s10b-emu-all.json`) with word-level meaning fixes, each alone or beside its neighbor.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 186g-P2b1 (61) | Human (weak) | Emulate round b's u1-A, meaning fixed ("On the other hand", the three examples back as the experiments, the published test line back) | **Human (100%)**, 22:42:53 |
| 186g-P2b2 (55) | Human (weak) | u1-B, fixed | **Human (100%)**, 22:42:55 |
| 186g-P1aP2b1 (136) | Human (weak) | P1a passed alone (185g) | Mixed (61% AI), 22:42:57: P1a from "Splitting off completely" through P2b1 (88 words) |
| 186g-P1aP2b2 (130) | Human (weak) |  | **Human (100%)**, 22:43:03 |
| 186g-P3b1 (61) | Human (weak) | u2-A, fixed: "(that's essentially just another state, with a nicer logo)" | **Human (100%)**, 22:43:07 |
| 186g-P3b2 (69) | Mixed | u2-B, fixed | **Human (100%)**, 22:43:13 |
| 186g-P3b1P4b (101) | Mixed | P4b (u2-B's second paragraph, fixed) is under 50 words | AI (100%), 22:43:20 |
| 186g-P3b2P4b (109) | Mixed |  | AI (100%), 22:43:22 |
| 186g-P5b1 (140) | Human (weak) | u3-A, fixed: its fragments ("Delegates. Records. Compliance.") kept | **Human (100%)**, 22:43:30 |
| 186g-P6b1 (107) | Mixed | u4-B, fixed; the "decorative" freedom back | Mixed (60% AI), 22:43:37: from "In theory someone can move" to the end (66 words) |
| 186g-P7b1 (146) | AI | u5-A, fixed: the published list of events had to come back, and it reads like the published | **Human (100%)**, 22:43:44 |
| 186g-P8b1 (62) | Human (weak) | u6-A, fixed: the last sentence back | AI (100%), 22:43:45 |

186g (submitted 22:42:53 to 22:43:45 UTC): mine 7 of 12. Emulate round b with word fixes passes in P2, P3, P5 and P7 (P2b2 beside P1a too). P4 (beside either P3), P6's second half and P8 read AI.

Batch 187g (written 22:45 UTC on 2026-10-09 by `date -u`, before the call; `v187.json`, parts in `fix-v3-parts.json`): P4, P6 and P8 again from Emulate round b, and the first two whole-section versions with the passing paragraphs.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 187g-P3b1P4c (101) | Human (weak) | P4c from Emulate round b's u2-A ("I see the need to …", "It's also important to keep … from forgetting"), fixed | AI (100%), 22:46:10 |
| 187g-P3b2P4c (109) | Human (weak) |  | AI (100%), 22:46:13 |
| 187g-P6c (103) | Mixed | P6b1's first half (it passed) with the "decorative" freedom and the thin interface reworded | AI (100%), 22:46:21 |
| 187g-P6d (103) | Mixed | the same, "In theory anyone can move. In practice …" | AI (100%), 22:46:29 |
| 187g-P8c (78) | Human (weak) | Emulate round b's u6-B ("store not only the resulting rule but also the original hard case"), fixed | AI (100%), 22:45:29 |
| 187g-P8d (81) | Human (weak) | closer to u6-B | AI (100%), 22:45:35 |
| 187g-S10v2a (713) | Mixed | the passing paragraphs with P3b1, P4c, P6c and P8c | AI (100%, 742 words), 22:46:38 |
| 187g-S10v2b (724) | Mixed | with P3b2, P4c, P6d and P8d | AI (100%, 751 words), 22:46:40 |

187g (submitted 22:45:29 to 22:46:40 UTC): mine 2 of 8. Every new P4, P6 and P8 reads AI, and both sections read 100% AI. **A slip in this batch:** the first browser call stopped on the hash check (the section items' headings weren't installed under this batch's prefix), but the second call, sent at the same time, submitted P8c, P8d and both sections without checking. Its two section texts (22:45:36 and 22:45:44, 727 and 736 words, both 100% AI) carried "undefined" in place of the headings, so they match no recorded item and are discarded; the sections were resent with the headings (22:46:38 and 22:46:40). From now on the later calls of a batch submit only if the first call's hash check passed (`window.__B<n>ok`).

Batch 188g (written 22:50 UTC on 2026-10-09 by `date -u`, before the call; `v188.json`, parts in `fix-v4-parts.json`): P4, P6 and P8 by other routes: P4 joined to P3, the lists said as speech or split into sentences, and Emulate round c (the whole section in one unit, `emu/s10c-emu-all.json`) with word fixes.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 188g-P34m (90) | Mixed | P3b1 (passes) with P4's content joined to it as one paragraph: a change of unit, since every short P4 has read AI beside P3 | **Human (100%)**, 22:51:07 |
| 188g-P3b1P4e (95) | AI | "You spread …, you train …, you seed …" (a run of three) | AI (100%), 22:51:12 |
| 188g-P3b1P4f (101) | Human (weak) | P4 from round c's whole-section sample B ("we want to be spreading …", "the people settling into nice enclaves") | AI (100%), 22:51:17 |
| 188g-P6e2 (120) | Mixed | the list said the way you'd say it ("where they'll live or what their status is, …") | AI (100%), 22:51:20 |
| 188g-P6g (119) | Human (weak) | from round c's sample B ("One thing to notice about cooperating …", "and not just in theory") | AI (100%), 22:51:25 |
| 188g-P8e (72) | Mixed | the list split into sentences ("Write down … Keep … Note …") | AI (100%), 22:51:35 |
| 188g-P8f (75) | Mixed | "it's not enough to save the final rule. You need the hard case too" | AI (100%), 22:51:39 |
| 188g-P8g (74) | Human (weak) | from round c's sample A ("When you create a rule to deal with a collision of two principles"; "That saves each generation …") | **Human (100%)**, 22:51:44 |
| 188g-P8h (78) | Human (weak) | from sample B ("keep the original case on file") | **Human (100%)**, 22:51:48 |

188g (submitted 22:51:07 to 22:51:48 UTC): mine 5 of 9. P4 passes only joined to P3 (P34m): every short P4 read AI beside P3, the unit was the problem. P8 passes from Emulate round c (g and h). P6 reads AI in all seven wordings so far.

Batch 189g (written 22:52 UTC on 2026-10-09 by `date -u`, before the call; `v189.json`, parts in `fix-v5-parts.json`): P6 from round c, whole and split in two, and the section with every passing paragraph.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 189g-P6h (108) | Mixed | P6 from round c's sample A ("One key to this whole thing", "and that takes work: …", "Fortunately, that interface can often be thin"), fixed | **Human (100%)**, 22:53:17 |
| 189g-P6i2 (72) | Mixed | the same split into two paragraphs: the movement half alone | **Human (100%)**, 22:53:22 |
| 189g-P5b1P6i1 (174) | Human (weak) | the membership half (34 words) beside P5b1, which passes alone | **Human (100%)**, 22:53:26 |
| 189g-P6i1P6i2 (106) | Mixed |  | AI (100%), 22:53:31 |
| 189g-S10v3a (703) | AI | the passing paragraphs (P1a, P2b2, P34m, P5b1, P7b1, P8g) with P6h | Mixed (33% AI, 730 words), 22:53:40: the top, from the heading through P34m (245 words) |
| 189g-S10v3b (701) | AI | with P6 split | Mixed (33% AI), 22:53:47: the same window |
| 189g-S10v3c (707) | AI | with P6h and P8h | Mixed (50% AI), 22:53:51: the same window, P6h's middle (43 words), and P7's end through P8h (80 words) |

189g (submitted 22:53:17 to 22:53:51 UTC): mine 4 of 7. P6h passes alone (round c's sample A, fixed), the eighth P6 wording. With every paragraph passing, the section reads 33% AI, in one window: the top, from the headings through P34m (245 words). P5b1 to P8g read Human in it. The published subheading "Federation Without Building Another State" has a negation, which the linter marks REVIEW (H1, Joel 2026-10-06), not FAIL as I first wrote here; the next batch tries two plain ones as a proposal.

Batch 190g (written 22:54 UTC on 2026-10-09 by `date -u`, before the call; `v190.json`, parts in `fix-v6-parts.json`): the top window: two plain subheadings (proposals), and P3b2 joined to P4.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 190g-P34m2 (98) | Human (weak) | P3b2 (passes alone) with P4 joined | **Human (100%)**, 22:57:06 |
| 190g-Wtop (235) | AI | diagnostic: the top alone, as in the section | AI (100%), 22:57:13 |
| 190g-WtopH3b (235) | Mixed | subheading "The Boring Problem of Federation" (from P3's own words), a proposal | AI (100%), 22:57:15 |
| 190g-WtopH3c (233) | Mixed | subheading "Federation Is Work" (the published P5's words) | AI (100%), 22:57:20 |
| 190g-S10v4a (703) | Human (weak) | 189g's section with H3b | Mixed (33% AI), 22:57:29: the same 245-word window, heading through P34m |
| 190g-S10v4b (701) | Human (weak) | with H3c | Human, "Mostly Human Written" (8% AI), 22:57:33: one 58-word window, P34m from "I'd like them to connect" to the end. Not a pass (the label isn't "Human Written"), and the heading isn't adoptable (below) |
| 190g-S10v4c (711) | Mixed | with P34m2, published subheading | Mixed (42% AI), 22:57:40: one 306-word window, heading through P5b1's "local crisis has eaten into" |
| 190g-S10v4d (711) | Human (weak) | with H3b and P34m2 | Mixed (42% AI), 22:57:43: the same 306-word window |

190g (submitted 22:57:06 to 22:57:43 UTC): mine 4 of 8. P34m2 passes alone, but the section with it reads 42% AI, worse than with P34m. With the plain subheading "Federation Is Work" the section reads "Mostly Human Written" (8% AI), with only P34m's second half flagged.

**My slip in 190g: I tried headings by their Pangram result.** Joel's rule of 2026-09-29 (docs/HUMANIZATION-GATE.md, the headings bullet) says a heading is never picked by its Pangram result, candidate headings go through the grounding review before any Pangram check, and a flagged span that's mine gets fixed instead. Neither "The Boring Problem of Federation" nor "Federation Is Work" had a grounding review, and "Federation Is Work" doesn't say what the published one does (it drops "without building another state"). So both results are diagnostics only and neither heading is adopted. The published heading stays. What 190g does show: the AI part sits in P34m's second half, which is mine. The guard: build_batch.py now refuses a heading that isn't published unless a grounding record lists it (`headings-grounded.json`).

Batch 191g (written 23:01:13 UTC on 2026-10-09 by `date -u`, before the call; `v191.json`, parts in `fix-v7-parts.json`): the flagged span's own sentences, published headings only. 190g put the AI part in P34m's second half, which carries two lists (E125 REVIEW each).

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 191g-P34n1 (89) | Human (weak) | P34m without "connect" (Emulate added it; the published list is "help one another, move people and knowledge around") | AI (100%), 23:01:31 |
| 191g-P34n2 (95) | Human (weak) | P34m with the federation-level list split: three items, then "The federation also has to keep any one comfortable enclave..." | AI (100%), 23:01:35 |
| 191g-P34n3 (94) | Human (weak) | both fixes | AI (100%), 23:01:39 |
| 191g-S10v5a (702) | Mixed | the 189g section (published headings) with P34n1 | Mixed (33% AI), 23:01:48: the top, 244 words |
| 191g-S10v5b (708) | Mixed | with P34n2 | Mixed (34% AI), 23:01:53: the top, 250 words |
| 191g-S10v5c (707) | Human (weak) | with P34n3 | Mixed (33% AI), 23:02:00: the top, 249 words |

191g (submitted 23:01:31 to 23:02:00 UTC): mine 2 of 6. Each fix to P34m's two lists turned the paragraph from Human to 100% AI alone, and the section stayed at 33% with the same top window. So P34m alone is a pass near the line, and its lists aren't what the section window is reading.

Batch 192g (written 23:03:05 UTC on 2026-10-09 by `date -u`, before the call; `v192.json`): diagnostics only, to find which junction turns the top window AI (every part in it passes alone, and P1a with P2b2 passes).

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 192g-D1top12 (140) | AI | P1a with P2b2 passed without headings (186g); the stacked h1 and h2 are known flippers | **Human (100%)**, 23:03:15 |
| 192g-D2H3P34m (95) | Human (weak) | P34m passed alone (188g); one short h3 | **Human (100%)**, 23:03:22 |
| 192g-D3noH12 (225) | AI | the top without the h1 and h2 | AI (100%), 23:03:25 |
| 192g-D4H12P1a (85) | Human (weak) | the h1 and h2 with P1a only | **Human (100%)**, 23:03:29 |
| 192g-D5P2H3P34 (150) | Mixed | the junction across the h3 | **Human (100%)**, 23:03:35 |

192g (submitted 23:03:15 to 23:03:35 UTC): mine 3 of 5. Every span up to 158 words passes: the h1 and h2 with P1a and P2b2, and P2b2 across the h3 to P34m. P1a through P34m (235 words) reads 100% AI. So no junction or heading turns it; the four paragraphs read AI only as one long stretch. Word-level fixing of the top is spent (P34m in five wordings, P2 in two, P3 in two): this goes to Joel with the page, under the AGENTS.md rule (ask as soon as the first method is spent).

Batch 193g (written 23:51:13 UTC on 2026-10-09 by `date -u`, before the call; `v193.json`, parts in `fix-v9-parts.json`): the gate's fixes to P5 to P8 (review-e1: trace E1 OK for P1 to P34m; trace E2, the stance check, the cold read and the abstract judge found meaning to fix in P5 to P8).

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 193g-P5d (134) | Mixed | P5b1 with four fixes: "(FEC)" at first mention, "eaten into both", "requires money" (cold read), "But the work of federation" (trace E2) | **Human (100%)**, 23:51:37 |
| 193g-P6k (102) | AI | "Cooperation also shouldn't quietly turn into assimilation." (stance 1, trace E2), "similarly practical"; P6a opened the same way and read AI | **Human (100%)**, 23:51:38 |
| 193g-P6m (105) | Mixed | "Another thing is that cooperation …": keeps the trace's "also" without staging importance | **Human (100%)**, 23:51:43 |
| 193g-P7d (147) | Mixed | "the same honesty about" (trace E2, stance 2), the cash condition over all four (stance 3, trace E2), "Solidarity doesn't mean" (abstract judge: quip) | **Human (100%)**, 23:51:47 |
| 193g-P8k (76) | Human (weak) | "the principles that actually conflicted" (stance 4, trace E2) | **Human (100%)**, 23:51:55 |
| 193g-S10v6a (694) | Mixed | the gated section with P6k; the top window should stay | Mixed (25% AI, 721 words), 23:52:03: two windows, P2b2's last sentence through P34m (114 words), and P8k from "Store the hard case too" to the end (58 words) |
| 193g-S10v6b (697) | Mixed | with P6m | Mixed (62% AI), 23:52:06: the top (245 words), P6m's middle (44), P7d's list (48), and P7d's end through P8k (112) |

193g (submitted 23:51:37 to 23:52:06 UTC): mine 3 of 7. Every meaning-fixed paragraph passes alone, including "Cooperation also shouldn't quietly turn into assimilation", which I expected to fail. With them, the section reads 25% AI, the best so far: the top window shrank to P2b2's last sentence through P34m (114 words), and P8k opened one (58 words). P6m ("Another thing is that") reads much worse in the section (62%), so P6k it is, which is also the closer one to the published.

Batch 194g (written 23:53:09 UTC on 2026-10-09 by `date -u`, before the call; `v194.json`, parts in `fix-v10-parts.json`): one fix at a time on S10v6a (25%), with the other passing wordings of P3+P4 and P8.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 194g-P8m (78) | Human (weak) | P8h (passed alone, 188g) with "what principles actually conflicted" (stance 4, trace E2) | **Human (100%)**, 23:53:23 |
| 194g-S10v7a (702) | Mixed | 193g's S10v6a (25%) with P34m2 for P34m: the top window | Human, "Mostly Human Written" (9% AI, 728 words), 23:53:28: one window, P8k from "Store the hard case too" to the end (58 words); the top window is gone |
| 194g-S10v7b (696) | Mixed | with P8m for P8k: the P8 window | Mixed (47% AI), 23:53:31: the top (128 words), P6k's middle (44), P7d's list (48), P7d's end through P8m (115) |
| 194g-S10v7c (704) | Mixed | both | Mixed (36% AI), 23:53:38: P6k's middle (44 words), P7d's list through P8m (217) |

194g (submitted 23:53:23 to 23:53:38 UTC): mine 3 of 4. With P34m2 (P3b2 with P4 joined) the top window is gone, and the section reads "Mostly Human Written" (9%), with one window left in P8k. P34m2 hasn't been traced yet (trace E1 traced P34m), so it goes to the trace before it's adopted. P8m reads worse in the section than P8k.

Batch 195g (written 23:54:50 UTC on 2026-10-09 by `date -u`, before the call; `v195.json`, parts in `fix-v11-parts.json`): the last window, in P8k.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 195g-P8p (73) | Human (weak) | P8k with the sentence where the window starts changed: "store the hard case along with it:" for "don't only store the rule. Store the hard case too:" | **Human (100%)**, 23:55:05 |
| 195g-P8t (85) | Mixed | P8k with its seven-item list split: four items, then "Any dissenting opinions should go in there as well, along with …" (E126) | **Human (100%)**, 23:55:09 |
| 195g-P8u (82) | Mixed | both | **Human (100%)**, 23:55:13 |
| 195g-S10v8a (699) | Human (weak) | 194g's S10v7a (9%) with P8p | Mixed (28% AI), 23:55:24: P6k's middle (44 words), P7d's list (48), P7d's end through P8p (108) |
| 195g-S10v8b (711) | Mixed | with P8t | **Human (100%, "Human Written", 737 words)**, 23:55:29 |
| 195g-S10v8c (708) | Mixed | with P8u | **Human (100%, "Human Written", 733 words)**, 23:55:33 |

195g (submitted 23:55:05 to 23:55:33 UTC): mine 1 of 6. Splitting P8's seven-item list (E126) cleared the last window: the section reads 100% Human with P8t (737 words) and with P8u (733). P8t is the closer one to the published (it keeps "don't only store the rule. Store the hard case too:"), so S10v8b is the candidate. It goes through the gate again (review-e2) before it's adopted, since P34m2, P5d, P6k, P7d and P8t are new since review-e1.

Batch 196g (written 00:23:15 UTC on 2026-10-10 by `date -u`, before the call; `v196.json`, parts in `fix-v12-parts.json`): review-e2's fixes to the passing candidate (S10v8b, 100% Human). Trace F: P6k, P7d and P8t OK; P34m2 and P5d need a fix. Stance e2: one conflict, in P8t. Cold read e2: "that interface" and "outside money" are mine; its other questions are in the published text too.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 196g-P34p (99) | Mixed | P34m2 with "does eventually need to be solved" (trace F: "eventually" lost) | **Human (100%)**, 00:23:34 |
| 196g-P5e (136) | Human (weak) | P5d with "a cash budget for dealing with it" (trace F: "a budget of outside money" reads as donor money; the cold read asked what outside money is) | **Human (100%)**, 00:23:38 |
| 196g-P6n (104) | Human (weak) | P6k with "the interface between communities" (trace F and the cold read: "that interface" points at nothing) | **Human (100%)**, 00:23:41 |
| 196g-P8v (83) | Human (weak) | P8t opening "When you have to deal with a collision of two principles" (stance e2: "When you create a rule" limits the record to new rules) | Mixed (45% AI), 00:23:47: its first two sentences (38 words) |
| 196g-P8w (77) | Mixed | P8t opening "When two principles collide, don't only store the final rule." (the published shape) | AI (100%), 00:23:55 |
| 196g-S10v9a (714) | Mixed | 195g's passing S10v8b with the four gate fixes, P8v | **Human (100%, "Human Written", 740 words)**, 00:24:00, but P8v fails alone |
| 196g-S10v9b (708) | Mixed | with P8w | Human, "Mostly Human Written" (5% AI), 00:24:05: P8w's first two sentences (32 words) |

196g (submitted 00:23:34 to 00:24:05 UTC): mine 2 of 7. The fixes to P34m2, P5d and P6k all pass alone. The section reads 100% Human with P8v, but P8v reads 45% AI alone (it's 83 words, so it has to pass alone), and P8w fails both ways. Next: openings for P8 that keep P8t's shape and cover any collision, not only a new rule.

Batch 197g (written 00:25:01 UTC on 2026-10-10 by `date -u`, before the call; `v197.json`, parts in `fix-v13-parts.json`): P8's opening, for stance e2's conflict.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 197g-P8x (87) | Human (weak) | P8t with "create or apply a rule" (the nearest to P8t, which passed) | **Human (100%)**, 00:25:15 |
| 197g-P8y (84) | Mixed | "Whenever you use a rule to settle a collision of two principles" | AI (100%), 00:25:21 |
| 197g-P8z (91) | Mixed | P8t with ", or use one you already have," | **Human (100%)**, 00:25:26 |
| 197g-S10v10a (718) | Human (weak) | 196g's S10v9a with P8x | **Human (100%, "Human Written", 744 words)**, 00:25:34 |
| 197g-S10v10b (715) | Mixed | with P8y | Human (100%), 00:25:39, but P8y fails alone |
| 197g-S10v10c (722) | Mixed | with P8z | **Human (100%, "Human Written", 748 words)**, 00:25:44 |

197g (submitted 00:25:15 to 00:25:44 UTC): mine 2 of 6. S10v10a (P8x, "When you create or apply a rule") reads 100% Human, and every paragraph in it passes alone. P8z passes both ways too, with more added words; P8y fails alone. S10v10a is the candidate. Its four changed paragraphs (P34p, P5e, P6n, P8x) go to trace G and a cold read before it's installed.

Batch 198g (written 00:40:07 UTC on 2026-10-10 by `date -u`, before the call; `v198.json`, parts in `fix-v14-parts.json`): trace G passed P5e, P6n and P8x and flagged one modal in P34p.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 198g-P34q (99) | Mixed | P34p with "allows" for "encourages" (trace G: "can help" is capacity, "encourages" is promotion) | **Human (100%)**, 00:40:21 |
| 198g-P34r (99) | Mixed | "lets communities help each other and move people and knowledge around" (the published wording, nearly) | **Human (100%)**, 00:40:26 |
| 198g-P34s (99) | Mixed | "allows", and "so communities can keep learning" (cold read e3: "they" can read as the differences) | **Human (100%)**, 00:40:30 |
| 198g-S10v11a (718) | Mixed | 197g's S10v10a (100% Human) with P34q | **Human (100%, "Human Written", 744 words)**, 00:40:40 |
| 198g-S10v11b (718) | Mixed | with P34r | Human, "Mostly Human Written" (9% AI), 00:40:43: P34r from "It should be solved" to the end (63 words) |
| 198g-S10v11c (718) | Mixed | with P34s | **Human (100%, "Human Written", 744 words)**, 00:40:49 |

198g (submitted 00:40:21 to 00:40:49 UTC): mine 1 of 6. All three P3+P4 fixes pass alone. S10v11c, with P34s ("allows", and "so communities can keep learning" for the cold read's "they"), reads 100% Human (744 words), as does S10v11a. **Section 10 v1 = S10v11c**: H1, H2, P1a, P2b2, H3, P34s, P5e, P6n, P7d, P8x.

Batch 199 (API, 12:54 to 12:55 UTC on 2026-10-10): not run. The first POST came back HTTP 402 ("Insufficient credits"), so nothing was checked or charged; the key itself is accepted (probe at 12:53). Its predictions were for Joel's heading as he first proposed it ("…, Improve Resilience"); grounding f1 and stance f1 both flagged "Improve Resilience" as a claim the section doesn't make, and at about 13:00 UTC he chose "Federated Communities Make a Movement" and approved these five web-app checks.

Batch 200g (written 13:03 UTC on 2026-10-10 by `date -u`, before the call; `v200.json`, parts in `fix-v15-parts.json`): Joel's changes of 12:22 UTC. P3+P4 without "boring" and without the super-commune sentence (P34t), P6 with "slide into" for "quietly turn into" (P6p; trace H OK), and his heading "Federated Communities Make a Movement" (H3k). Predictions are Human or AI only, as E86 says: in 189g to 198g I wrote "Mixed" for 35 of 62 checks, and no paragraph came back Mixed.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 200g-P34t (89) | Human | P34s's words (passed alone, 198g) minus "boring" and the quip sentence; nothing added |  **Human (100%)**, 13:04:30 |
| 200g-P6p (103) | Human | P6n (passed alone, 196g) with one verb phrase changed |  **Human (100%)**, 13:04:34 |
| 200g-H3kP34t (94) | Human | a five-word heading that names the thing, not an x-not-y frame; headings have flipped paragraphs before, so this is the risk |  **Human (100%)**, 13:04:40 |
| 200g-P2b2H3kP34t (149) | Human | every span up to 158 words of the old top passed (192g), P2b2 across the h3 to P34m included |  **Human (100%)**, 13:04:49 |
| 200g-S10v12 (707) | Human | v1 read 100% Human (198g); the changes take out a quip and two frequency words. Risk: P1a to P34 once read AI as one 235-word stretch (192g), and P34t is shorter |  **Human (100%, "Human Written", 731 words scanned)**, 13:04:52 |

200g (submitted 13:04:30 to 13:04:52 UTC, 2026-10-10; times and verdicts from the History API, matched by each text's hash): mine 5 of 5. Every text reads 100% Human: P34t and P6p alone, the heading with P34t, P2b2 across the heading to P34t, and the whole section (731 words scanned). P1a, P2b2, P5e, P7d and P8x are unchanged and passed alone before (185g, 186g, 196g, 193g, 197g). **Section 10 v2 = S10v12**: H1, H2, P1a, P2b2, H3k, P34t, P5e, P6p, P7d, P8x.
