# Status: hypnosis guide humanization (newest on top)

## 2026-10-18, after batch 454g (its checks ran from 07:33 to 07:52 UTC)

**Where it stands.** 23 keys are installed in `HUMANIZED-SO-FAR.md` (26 of the guide's 40 h1 sections), every paragraph
checked alone, and three more sections read Human as published (HG05, HG08, HG09): 29 of 40 done. One caveat: HG36's last
three paragraphs (B10-B12) are in the article as published and were never checked (see Tools below); their repair is in
`fix-20261018/rf-p/`. Open: HG06, HG14, HG15, HG17, HG24, HG26, HG31, HG33, HG37 (in meaning or paragraph checks), HG18 and
HG32 (AI in every version; for Joel).

**What the batches showed (446g to 454g).**
- **The triage holds.** Triaged edits read Human whole in 20 of 24 checks (449g to 454g); the four that didn't (HG14, HG18,
  HG26, HG33 in 449g or 451g) had small AI windows, and three of them read Human after a new sample of those windows.
- **Pasted published wording reads AI, even in a small fix.** HG37's edit (454g) read AI in exactly two windows, both
  triage fixes that pasted the published sentences ("what response makes you safer, clearer, more loving, more grounded, and
  less hooked"; "Pride gives it an opponent, and panic gives it your nervous system"). They are reworded in the stretch's
  voice now. The triage brief already says so; the readers will be reminded.
- **A paragraph alone reads Human when Emulate wrote it.** Of 235 paragraph checks (442g to 453g), those under 5% not
  Emulate's words read Human 99% of the time (141 checks); 5-15%, 93%; 15-30%, 70%. That is now how a paragraph check is
  predicted (`tools/para_chance.py`).
- **Several samples at once.** Instead of one sample, one screen, one reading at a time, two or three samples of each window
  went to Emulate together (emu-ac, emu-ad, emu-ae, emu-af, emu-ag, emu-ah, emu-ai) and the second reader read all of them;
  the one that kept the meaning best is triaged. For HG26's get-help paragraphs, one of three samples kept every safety
  item (one fix: "concerning" physical symptoms).
- **Emulate can't keep a long script.** HG17's listening script (B17-B31) lost 11 to 26 steps in each of three samples as one
  window; it is now in seven small windows (emu-af, emu-ag).
- **HG24's "Refrain."** My meaning fix for "Don't pry." was the verb "Refrain."; two samples read it as a song's refrain
  ("(VOCAL) REFRain: Just shew me first your CAPACItY"). B36-B37 are as published now.
- 453g: HG16, HG35 and HG38+39 passed every paragraph and were installed; HG06's fourth paragraph (my fix) and HG26's two
  get-help paragraphs together read AI. 454g: HG02+03 read 100% Human whole for the first time (Joel's table-of-contents
  note too), every paragraph Human: installed. HG14 and HG33's new window samples read Human whole; five of HG14's 59
  paragraph checks read AI.

**Predictions.** 447g 6 of 9, 448g 8 of 9, 449g 9 of 12, 450g 91 of 92, 451g 49 of 52, 452g 25 of 30, 453g 39 of 43,
454g 99 of 107. Brier score (my chance of a 100% Human result against the result): 0.134 over the lane's 445 checks to
453g; 0.076, 0.112, 0.147 and 0.109 for 450g to 453g.

**Tools.** `tools/refix_runs.py`: `units_fixed` and `assembled_fixed` dropped every block after the first when a run's output
came back one segment per block for a stretch that was one unit (HG36 lost B10-B12 from its checked text that way; the
install left them as published; HG24's second reader never saw B43, B44, B47, B48). Both now take every segment, keep the
unit's own paragraphs where they line up one per block, and stop with an error otherwise (`tests/test_hypnosis_refix_merge.py`).
`tools/para_chance.py` (paragraph-check chances); `make_b446.collect()` reads only each section's newest version (an older
`rf-a` file had reused a newer check's result); `make_verify_samples.py` (the second reader for several samples);
`make_emu_ac.py`, `make_emu_af.py`, `make_emu_ah.py` (sample sets); `march_pairs.py` reads a hand-made map.

### Sections

| section | state | newest whole check | paragraph checks | earlier |
|---|---|---|---|---|
| HG01 | **installed** (fixed) | [434g HG01-fix](https://www.pangram.com/history/b5dc548b-e3f5-427f-8270-f1da2afb8d54) | 1 of 1 Human | 429g published AI 0.98; 431g screen H 0.00 |
| HG02+03 | **installed** (triaged) | [454g HG02+03-rfix](https://www.pangram.com/history/94dc9298-fb41-497c-a71a-8666a6c0df7f) | 8 of 8 Human | 429g published AI 1.00; 431g screen AI 0.05; 434g fixed AI 0.99; 435g screen H 0.06; 443g refix AI 0.03 |
| HG04 | **installed** (triaged) | [450g HG04-rfix](https://www.pangram.com/history/bf1c1412-591e-4c11-a5ba-3bfb565fb0bd) | 2 of 2 Human | 429g published AI 1.00; 431g screen AI 0.36; 433g screen AI 0.95; 436g screen AI 1.00; 437g screen H 0.00; 441g fixed H 0.04; 445g refix H 0.11 |
| HG05 | Human (published) | [429g HG05](https://www.pangram.com/history/5028ad7e-4df3-476d-b580-1d5eee5eb68d) | - | - |
| HG06 | Human (triaged) | [453g HG06-rfix](https://www.pangram.com/history/80bf4ff5-088b-4a3f-a447-f3b0c942b713) | 0 of 3 Human | 429g published AI 0.89; 430g screen H 0.10; 434g fixed H 0.20; 445g refix H 0.00; 448g refix H 0.00; 451g refix H 0.00 |
| HG07 | **installed** (fixed) | [434g HG07-fix](https://www.pangram.com/history/ca3cf277-8622-4f71-8405-22406e199488) | 3 of 3 Human | 429g published AI 0.25; 430g screen H 0.00 |
| HG08 | Human (published) | [429g HG08](https://www.pangram.com/history/971cfbf5-1485-4266-903a-f49145a75aa3) | - | - |
| HG09 | Human (published) | [429g HG09](https://www.pangram.com/history/7a521519-0ecc-4adc-9c04-c9ee182b3fd8) | - | - |
| HG10 | **installed** (refix) | [443g HG10-refix](https://www.pangram.com/history/4c169e15-7347-45e9-8581-c6f830c6663a) | 4 of 4 Human | 429g published AI 1.00; 430g screen H 0.05; 434g fixed AI 0.15 |
| HG11 | **installed** (refix) | [443g HG11-refix](https://www.pangram.com/history/c5ab4670-be7b-444e-83ef-545b54412dc5) | 4 of 4 Human | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 0.98 |
| HG12 | **installed** (fixed) | [434g HG12-fix](https://www.pangram.com/history/781080d2-867c-4e50-9250-c8a6899036b8) | 7 of 7 Human | 429g published AI 0.63; 431g screen H 0.03 |
| HG13 | **installed** (triaged) | [449g HG13-rfix](https://www.pangram.com/history/12e8c230-f460-4cc4-b1a2-63ef3aafd796) | 11 of 11 Human | 429g published AI 1.00; 432g screen H 0.04; 434g fixed AI 0.73; 443g refix H 0.00 |
| HG14 | Human (refix) | [454g HG14-refix2](https://www.pangram.com/history/06d1ce83-4310-473f-8153-6e4cff193db5) | 54 of 59 Human | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.70; 443g refix H 0.03; 451g triaged AI 0.09 |
| HG15 | Human (triaged) | [451g HG15-rfix](https://www.pangram.com/history/105ec30f-5031-4998-85a2-7540fb64af91) | 15 of 20 Human | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.79; 443g refix H 0.00 |
| HG16 | **installed** (triaged) | [452g HG16-rfix](https://www.pangram.com/history/94cb4b13-f089-4a11-bf19-28672a8fbba4) | 16 of 16 Human | 429g published AI 1.00; 431g screen AI 0.55; 433g screen AI 0.97; 436g screen AI 0.30; 437g screen H 0.01; 444g fixed AI 0.69; 447g refix H 0.01 |
| HG17 | Human (refix) | [451g HG17-refix3](https://www.pangram.com/history/0dfd0e10-5b95-4c30-ab76-31cd9d8a66ed) | - | 429g published AI 1.00; 433g screen AI 0.48; 436g screen AI 0.36; 437g screen AI 0.23; 438g screen AI 0.05; 439g screen AI 0.11; 440g screen H 0.01; 444g fixed AI 0.78; 447g refix AI 0.27; 449g refix AI 0.18 |
| HG18 | AI 1.00 (triaged) | [451g HG18-rfix](https://www.pangram.com/history/a4847ac0-004c-4b1b-92f7-6a103c7e595a) | - | 429g published AI 1.00; 431g screen H 0.07; 434g fixed AI 1.00; 443g refix AI 0.25; 445g refix AI 0.35; 448g refix AI 0.94 |
| HG19 | **installed** (triaged) | [449g HG19-rfix](https://www.pangram.com/history/9bf6d74c-d3f0-428c-bf23-babac94186b1) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.99; 443g refix H 0.00 |
| HG20 | **installed** (triaged) | [452g HG20-rfix2](https://www.pangram.com/history/3531dc12-7906-464c-bb23-15b0ed812ebb) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.00; 434g fixed AI 0.88; 443g refix H 0.00; 449g triaged H 0.00 |
| HG21 | **installed** (triaged) | [450g HG21-rfix](https://www.pangram.com/history/dfe80d81-9e35-479b-bb70-d0474b847d2b) | 4 of 4 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.98; 443g refix H 0.00 |
| HG22 | **installed** (triaged) | [449g HG22-rfix](https://www.pangram.com/history/bdcc3330-4a5b-4ed7-b9d8-cadce5cf5f89) | 2 of 2 Human | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 1.00; 443g refix H 0.00 |
| HG23 | **installed** (triaged) | [450g HG23-rfix](https://www.pangram.com/history/668653c1-9c71-444e-ae0f-35e17f3efc6b) | 8 of 8 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.68; 443g refix AI 0.20; 445g refix H 0.01 |
| HG24 | Human (refix) | [448g HG24-refix2](https://www.pangram.com/history/266d8b09-d06e-4e40-a595-c87acb623fe3) | - | 429g published AI 0.98; 433g screen AI 0.18; 435g screen AI 0.43; 437g screen H 0.02; 441g fixed AI 0.74; 445g refix AI 0.11 |
| HG25 | **installed** (triaged) | [449g HG25-rfix](https://www.pangram.com/history/691c0bdd-383a-48e3-80b5-562d8a5a9fb8) | 11 of 11 Human | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.90; 443g refix H 0.00 |
| HG26 | Human (triaged) | [453g HG26-rfix](https://www.pangram.com/history/2dba6402-6101-4e5d-b28e-ca03db166edd) | 7 of 8 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.69; 443g refix H 0.00; 449g triaged AI 0.23; 451g refix H 0.09 |
| HG27 | **installed** (triaged) | [450g HG27-rfix](https://www.pangram.com/history/11d866c6-0604-4a4b-bccd-0f49a397bc98) | 2 of 2 Human | 429g published AI 1.00; 430g screen H 0.03; 434g fixed AI 0.45; 435g screen H 0.00; 443g refix H 0.00 |
| HG28 | **installed** (triaged) | [450g HG28-rfix](https://www.pangram.com/history/2f048f61-2981-4376-9909-131d705ce07f) | 5 of 5 Human | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.26; 443g refix H 0.12 |
| HG29+30 | **installed** (triaged) | [449g HG29+30-rfix](https://www.pangram.com/history/48b4dfd2-abd1-4157-b04d-16ba3bf10c20) | 17 of 17 Human | 429g published AI 1.00; 431g screen AI 0.29; 433g screen AI 0.56; 436g screen AI 0.26; 437g screen AI 0.30; 438g screen H 0.12; 439g screen H 0.03; 441g fixed AI 0.69; 445g refix H 0.00 |
| HG31 | Human (refix) | [451g HG31-refix3](https://www.pangram.com/history/12d15b76-fec4-498b-9de9-e279687197db) | - | 429g published AI 1.00; 433g screen AI 0.32; 435g screen AI 0.16; 436g screen AI 0.18; 437g screen AI 0.18; 438g screen AI 0.18; 439g screen AI 0.12; 440g screen H 0.07; 444g fixed AI 0.81; 447g refix AI 0.26; 449g refix AI 0.28 |
| HG32 | AI 1.00 (screen) | [435g HG32-emuF](https://www.pangram.com/history/5a25465d-60b9-4bea-a03a-011b2ecdcb1a) | - | 429g published AI 1.00; 432g screen AI 0.99 |
| HG33 | Human (refix) | [454g HG33-refix2](https://www.pangram.com/history/eb55c9b5-7ce3-4a53-a669-c40abeb5ae0e) | 13 of 13 Human | 429g published AI 1.00; 432g screen AI 0.28; 434g fixed AI 0.99; 435g screen H 0.01; 443g refix H 0.08; 451g triaged AI 0.28 |
| HG34 | **installed** (triaged) | [451g HG34-rfix](https://www.pangram.com/history/e8d1cf1d-b3d2-4357-9ace-f11319f30be9) | 6 of 6 Human | 429g published AI 1.00; 431g screen H 0.11; 434g fixed AI 0.69; 443g refix H 0.00 |
| HG35 | **installed** (triaged) | [453g HG35-rfix](https://www.pangram.com/history/0bbc85f4-a5d1-4383-b09d-447f3a7d7f30) | 1 of 1 Human | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.50; 443g refix H 0.04; 451g refix H 0.06 |
| HG36 | **installed** (triaged) | [449g HG36-rfix](https://www.pangram.com/history/fa11a700-2004-412b-bc7e-8f9a27e83937) | 5 of 5 Human | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.80; 443g refix AI 0.55; 445g refix H 0.03 |
| HG37 | Mixed, AI 0.18 (triaged) | [454g HG37-rfix](https://www.pangram.com/history/17263cdd-3367-485c-947b-a2f46020d00f) | 22 of 23 Human | 429g published AI 1.00; 433g screen AI 0.64; 436g screen AI 0.66; 437g screen AI 0.53; 438g screen AI 0.12; 439g screen H 0.08; 444g fixed AI 0.99; 447g refix AI 0.18; 449g refix H 0.03 |
| HG38+39 | **installed** (triaged) | [452g HG38+39-rfix](https://www.pangram.com/history/729996a1-aa2c-4cc5-80fd-d2493917a8a1) | 12 of 12 Human | 429g published AI 1.00; 433g screen AI 0.59; 436g screen AI 0.18; 437g screen AI 0.15; 438g screen AI 0.16; 439g screen H 0.03; 444g fixed AI 1.00; 447g refix H 0.00 |
| HG40 | **installed** (triaged) | [449g HG40-rfix](https://www.pangram.com/history/1626b3a6-281b-4eef-b363-076dd0b73919) | 9 of 9 Human | 429g published AI 1.00; 432g screen H 0.00; 434g fixed AI 0.93; 443g refix H 0.00 |

## 2026-10-18, after batch 445g (its checks ran at 05:44 UTC)

**Where it stands.** Three sections are installed in `HUMANIZED-SO-FAR.md` with every paragraph checked alone: HG01 (the
guide's opening), HG07 and HG12 (442g). Three more read Human as published (HG05, HG08, HG09). Twenty-two others have a
version that reads 100% Human whole and are in meaning checks or paragraph checks; the rest are in refix runs.

**What the batches showed.**
- 441g: of the three fixed sections, HG04 stayed Human (17% of its words changed); HG24 and HG29+30 read AI.
- 442g, the first paragraph checks (23 texts of the five fixed sections that read Human): 17 Human. HG01, HG07, HG12 passed
  every paragraph; HG04's first two paragraphs and HG06's last four didn't.
- 443g, Plan B (Emulate rewrites my meaning-fixed text in the windows that read AI): **17 of 21 Human**.
- 444g: HG16, HG17, HG31, HG37 and HG38+39 with my fixes: all AI, as predicted. Their refix runs (emu-t) are running.
- 445g: refix screens of HG23, HG36, HG29+30 Human; HG04 and HG06 Human whole with their new paragraphs (HG06's new
  third paragraph reads AI alone); HG18 and HG24 still have AI windows.
- **The changed share decides.** Of 33 fixed sections, those whose fixes changed under 18% of the words stayed Human (3 of 3);
  those that changed more mostly didn't (2 of 30). That is why a refix's meaning problems now go through a triage
  (`fix-20261018/rf-a/TRIAGE-BRIEF.md`): only what changes what a reader would do or believe is fixed, in few words.
- **Emulate bends meaning again in a refix.** The second readers found 0 (HG10) to 71 (HG14) problems a section. HG26, the
  "when to get help" section, softened "get urgent help now"; every safety point there will be fixed.

**Predictions.** 441g 2 of 3 right, 442g 17 of 23, 443g 17 of 21, 444g 3 of 5 (I said "Mixed" where two read all AI),
445g 10 of 13.

**Tools.** `tools/install_fixed.py` (the Markdown to install, its paragraph-check texts, the install itself);
`tools/refix_runs.py` (`window_runs`, `assembled_fixed`, `units_fixed`, `hit_published`, `fixed_draft_blocks`);
`faithful.py verify-chunks` (a long section's second reader in parts); `paragraphs_alone.tries_for` (what the check looks
for, for batch builders); the block map reads the published copy, so an installed section never moves it;
`tools/lane_status.py` names each check's stage and the installed sections.

**Sections.**

| section | state | newest whole check | paragraph checks | earlier |
|---|---|---|---|---|
| HG01 | **installed** (fixed) | [434g HG01-fix](https://www.pangram.com/history/b5dc548b-e3f5-427f-8270-f1da2afb8d54) | 1 of 1 Human | 429g published AI 0.98; 431g screen H 0.00 |
| HG02+03 | Mixed, AI 0.03 (refix) | [443g HG02+03-refix](https://www.pangram.com/history/67524dc3-d41b-4330-89fc-7e579024cede) | - | 429g published AI 1.00; 431g screen AI 0.05; 434g fixed AI 0.99; 435g screen H 0.06 |
| HG04 | Human (refix) | [445g HG04-refix](https://www.pangram.com/history/0d852f81-ed67-4424-8e4d-491ea72d0e99) | - | 429g published AI 1.00; 431g screen AI 0.36; 433g screen AI 0.95; 436g screen AI 1.00; 437g screen H 0.00; 441g fixed H 0.04 |
| HG05 | Human (published) | [429g HG05](https://www.pangram.com/history/5028ad7e-4df3-476d-b580-1d5eee5eb68d) | - | - |
| HG06 | Human (refix) | [445g HG06-refix](https://www.pangram.com/history/9e338eee-a171-49d8-82ff-bae6f547ec49) | - | 429g published AI 0.89; 430g screen H 0.10; 434g fixed H 0.20 |
| HG07 | **installed** (fixed) | [434g HG07-fix](https://www.pangram.com/history/ca3cf277-8622-4f71-8405-22406e199488) | 3 of 3 Human | 429g published AI 0.25; 430g screen H 0.00 |
| HG08 | Human (published) | [429g HG08](https://www.pangram.com/history/971cfbf5-1485-4266-903a-f49145a75aa3) | - | - |
| HG09 | Human (published) | [429g HG09](https://www.pangram.com/history/7a521519-0ecc-4adc-9c04-c9ee182b3fd8) | - | - |
| HG10 | Human (refix) | [443g HG10-refix](https://www.pangram.com/history/4c169e15-7347-45e9-8581-c6f830c6663a) | - | 429g published AI 1.00; 430g screen H 0.05; 434g fixed AI 0.15 |
| HG11 | Human (refix) | [443g HG11-refix](https://www.pangram.com/history/c5ab4670-be7b-444e-83ef-545b54412dc5) | - | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 0.98 |
| HG12 | **installed** (fixed) | [434g HG12-fix](https://www.pangram.com/history/781080d2-867c-4e50-9250-c8a6899036b8) | 7 of 7 Human | 429g published AI 0.63; 431g screen H 0.03 |
| HG13 | Human (refix) | [443g HG13-refix](https://www.pangram.com/history/51d47dc8-838d-4ae5-8340-42f46de2731c) | - | 429g published AI 1.00; 432g screen H 0.04; 434g fixed AI 0.73 |
| HG14 | Human (refix) | [443g HG14-refix](https://www.pangram.com/history/60e741f3-8543-4c65-9c28-357e6bb6b204) | - | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.70 |
| HG15 | Human (refix) | [443g HG15-refix](https://www.pangram.com/history/df417394-281f-4c3b-a1c8-018bb4cc115b) | - | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.79 |
| HG16 | Mixed, AI 0.69 (fixed) | [444g HG16-fix](https://www.pangram.com/history/219af50c-bf82-41ab-9325-b7a4b8e82180) | - | 429g published AI 1.00; 431g screen AI 0.55; 433g screen AI 0.97; 436g screen AI 0.30; 437g screen H 0.01 |
| HG17 | Mixed, AI 0.78 (fixed) | [444g HG17-fix](https://www.pangram.com/history/7022d346-a8e2-42a4-aec7-a590e7f8ac35) | - | 429g published AI 1.00; 433g screen AI 0.48; 436g screen AI 0.36; 437g screen AI 0.23; 438g screen AI 0.05; 439g screen AI 0.11; 440g screen H 0.01 |
| HG18 | Mixed, AI 0.35 (refix) | [445g HG18-refix2](https://www.pangram.com/history/83f75339-363d-429a-b377-c6339d236f5d) | - | 429g published AI 1.00; 431g screen H 0.07; 434g fixed AI 1.00; 443g refix AI 0.25 |
| HG19 | Human (refix) | [443g HG19-refix](https://www.pangram.com/history/8b56e974-fdf2-4a32-9a91-664f56592d85) | - | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.99 |
| HG20 | Human (refix) | [443g HG20-refix](https://www.pangram.com/history/6e72bc49-4c63-45e3-9b1a-6fd38a074db3) | - | 429g published AI 1.00; 433g screen H 0.00; 434g fixed AI 0.88 |
| HG21 | Human (refix) | [443g HG21-refix](https://www.pangram.com/history/ecb5e201-3788-4d72-b017-05e4810477d5) | - | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.98 |
| HG22 | Human (refix) | [443g HG22-refix](https://www.pangram.com/history/2131d174-4dfb-4032-888c-ae335dee75d0) | - | 429g published AI 1.00; 430g screen H 0.00; 434g fixed AI 1.00 |
| HG23 | Human (refix) | [445g HG23-refix2](https://www.pangram.com/history/98f81bd1-01ea-484f-ad25-750093862233) | - | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.68; 443g refix AI 0.20 |
| HG24 | Mixed, AI 0.11 (refix) | [445g HG24-refix](https://www.pangram.com/history/9ce7c56c-5dbc-4e10-9897-788b4f9b4ad8) | - | 429g published AI 0.98; 433g screen AI 0.18; 435g screen AI 0.43; 437g screen H 0.02; 441g fixed AI 0.74 |
| HG25 | Human (refix) | [443g HG25-refix](https://www.pangram.com/history/eed35961-98d1-4370-bd77-57f7f56a5b76) | - | 429g published AI 1.00; 431g screen H 0.00; 434g fixed AI 0.90 |
| HG26 | Human (refix) | [443g HG26-refix](https://www.pangram.com/history/1cca1598-4345-4927-8a24-04e3d5fdcab2) | - | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.69 |
| HG27 | Human (refix) | [443g HG27-refix](https://www.pangram.com/history/942920c5-fb3b-4f62-aca9-db6d08951a34) | - | 429g published AI 1.00; 430g screen H 0.03; 434g fixed AI 0.45; 435g screen H 0.00 |
| HG28 | Human (refix) | [443g HG28-refix](https://www.pangram.com/history/5fbf9cc2-3e0c-41e0-a3ec-e03736c21b16) | - | 429g published AI 1.00; 431g screen H 0.01; 434g fixed AI 0.26 |
| HG29+30 | Human (refix) | [445g HG29+30-refix](https://www.pangram.com/history/19b268b0-7b72-441d-a943-2d18c193a976) | - | 429g published AI 1.00; 431g screen AI 0.29; 433g screen AI 0.56; 436g screen AI 0.26; 437g screen AI 0.30; 438g screen H 0.12; 439g screen H 0.03; 441g fixed AI 0.69 |
| HG31 | Mixed, AI 0.81 (fixed) | [444g HG31-fix](https://www.pangram.com/history/7421d3fc-5d39-4fec-b60d-b8c258c9dd30) | - | 429g published AI 1.00; 433g screen AI 0.32; 435g screen AI 0.16; 436g screen AI 0.18; 437g screen AI 0.18; 438g screen AI 0.18; 439g screen AI 0.12; 440g screen H 0.07 |
| HG32 | AI 1.00 (screen) | [435g HG32-emuF](https://www.pangram.com/history/5a25465d-60b9-4bea-a03a-011b2ecdcb1a) | - | 429g published AI 1.00; 432g screen AI 0.99 |
| HG33 | Human (refix) | [443g HG33-refix](https://www.pangram.com/history/6a7651a6-31f8-4396-b96c-da16b8febbb9) | - | 429g published AI 1.00; 432g screen AI 0.28; 434g fixed AI 0.99; 435g screen H 0.01 |
| HG34 | Human (refix) | [443g HG34-refix](https://www.pangram.com/history/71ba9c12-8313-48dd-a719-defee4f45d41) | - | 429g published AI 1.00; 431g screen H 0.11; 434g fixed AI 0.69 |
| HG35 | Human (refix) | [443g HG35-refix](https://www.pangram.com/history/5e037240-6d96-4ee8-85be-3a91aafe47a9) | - | 429g published AI 1.00; 433g screen H 0.03; 434g fixed AI 0.50 |
| HG36 | Human (refix) | [445g HG36-refix2](https://www.pangram.com/history/2d675dff-0550-4b3c-8b68-89c42ebb66f5) | - | 429g published AI 1.00; 431g screen H 0.02; 434g fixed AI 0.80; 443g refix AI 0.55 |
| HG37 | AI 0.99 (fixed) | [444g HG37-fix](https://www.pangram.com/history/81c9c3f6-f069-440a-a383-2a34871a89d9) | - | 429g published AI 1.00; 433g screen AI 0.64; 436g screen AI 0.66; 437g screen AI 0.53; 438g screen AI 0.12; 439g screen H 0.08 |
| HG38+39 | AI 1.00 (fixed) | [444g HG38+39-fix](https://www.pangram.com/history/f913c9f0-6243-4965-89b6-801690910ca6) | - | 429g published AI 1.00; 433g screen AI 0.59; 436g screen AI 0.18; 437g screen AI 0.15; 438g screen AI 0.16; 439g screen H 0.03 |
| HG40 | Human (refix) | [443g HG40-refix](https://www.pangram.com/history/52af1c90-5e5c-4286-907d-2a8cc9a43646) | - | 429g published AI 1.00; 432g screen H 0.00; 434g fixed AI 0.93 |

## 2026-10-18, after batch 440g (its checks ran at 04:26 UTC)

**Where it stands.** Every section but the de-hypnosis checklist (HG32) now has a version that reads 100% Human: 3 as
published, 33 as Emulate rewrote them. None is installed yet. Meaning work: 25 sections are done (my review, a second
reader, my answers to its findings, round-two and round-three fixes; `fix-20261018/meaning-status.json`, answered
findings in `fix-20261018/dispositions.json`); 8 more are in review (HG04, HG16, HG24: second reader running; HG29+30,
HG37, HG38+39: second reader running; HG17 and HG31: first review in parts). March reads of every unread stretch are
running (march-d, march-e). Then batch 434g: the corrected versions in Pangram.

**What worked for the failing sections (436g to 440g).** Second samples of short pieces fixed none (436g, 0 of 7). Sending
each AI window whole, with its headings, as one run did: 437g 3 of 8, 438g 1 of 5, 439g 3 of 5, 440g 2 of 2. A window
that keeps reading AI gets smaller with each whole-window sample (the induction: 1,283 AI words, then 950, 589, 117,
304, 0).

**Tools changed.** The window mapper reads the reader's short forms; the run mapper knows rewritten headings and, with
`--align`, cuts a run whose headings Emulate dropped by word overlap (it once took "Iteration (revise the prompt...)" for
the heading "Core prompts", now ruled out); a later folder's segment replaces every earlier one it overlaps;
`faithful.py chunks` cuts a long review into parts and `merge` adds later rounds of fixes; the gate no longer holds an
edit of an Emulate text for a linter FAIL its screen also had (57 of 59 screens FAILed, 28 of the 30 that read Human).

**Sections.**

| section | state | newest check | before |
|---|---|---|---|
| HG01 | Human | [431g HG01-emuA](https://www.pangram.com/history/82a93d2f-944b-4cf4-8d12-3d234c672f2a) | 429g AI 0.98 |
| HG01+TOC | Human as published | [432g HG01+TOC-probe](https://www.pangram.com/history/9e73b7bd-6a1b-4196-8ea4-cd6f6645b4c3) | - |
| HG02+03 | Human | [435g HG02+03-emuF](https://www.pangram.com/history/d0b61522-6920-41bf-9696-9d9e691a61a4) | 429g AI 1.00; 431g AI 0.05 |
| HG04 | Human | [437g HG04-emuH](https://www.pangram.com/history/7c55545c-f99e-468f-950b-5afd045339ff) | 429g AI 1.00; 431g AI 0.36; 433g AI 0.95; 436g AI 1.00 |
| HG05 | Human as published | [429g HG05](https://www.pangram.com/history/5028ad7e-4df3-476d-b580-1d5eee5eb68d) | - |
| HG06 | Human | [430g HG06-emuA](https://www.pangram.com/history/027a8de9-0e95-486c-8116-537066acdf77) | 429g AI 0.89 |
| HG07 | Human | [430g HG07-emuA](https://www.pangram.com/history/58314327-d533-40a5-9e6e-54ace93e3864) | 429g AI 0.25 |
| HG08 | Human as published | [429g HG08](https://www.pangram.com/history/971cfbf5-1485-4266-903a-f49145a75aa3) | - |
| HG09 | Human as published | [429g HG09](https://www.pangram.com/history/7a521519-0ecc-4adc-9c04-c9ee182b3fd8) | - |
| HG10 | Human | [430g HG10-emuA](https://www.pangram.com/history/c2963511-eeda-40d8-91a5-cb8859e3be6d) | 429g AI 1.00 |
| HG11 | Human | [430g HG11-emuA](https://www.pangram.com/history/157ed130-e3fe-4599-9810-5d07db9d3d0a) | 429g AI 1.00 |
| HG12 | Human | [431g HG12-emuA](https://www.pangram.com/history/0a29db60-da17-4708-b755-811072c8d3c2) | 429g AI 0.63 |
| HG13 | Human | [432g HG13-emuB](https://www.pangram.com/history/d274cdbe-9dc2-4bf5-8709-1812a07d9df7) | 429g AI 1.00 |
| HG14 | Human | [433g HG14-emuC](https://www.pangram.com/history/8455a492-80e6-434f-a267-9489485a05e6) | 429g AI 1.00 |
| HG15 | Human | [431g HG15-emuA](https://www.pangram.com/history/83cea455-7d6f-4096-8c0d-075a002fa8a0) | 429g AI 1.00 |
| HG16 | Human | [437g HG16-emuH](https://www.pangram.com/history/eadab2ae-1ca7-4401-bf43-c9d905943ede) | 429g AI 1.00; 431g AI 0.55; 433g AI 0.97; 436g AI 0.30 |
| HG17 | Human | [440g HG17-emuK](https://www.pangram.com/history/fdb72264-85fb-4259-986e-ab29176e6f19) | 429g AI 1.00; 433g AI 0.48; 436g AI 0.36; 437g AI 0.23; 438g AI 0.05; 439g AI 0.11 |
| HG18 | Human | [431g HG18-emuA](https://www.pangram.com/history/f7bfaff5-7844-44b8-b4ae-5cad302c5141) | 429g AI 1.00 |
| HG19 | Human | [431g HG19-emuA](https://www.pangram.com/history/ab3dac21-a2a4-4f59-8a06-1453cb61cfdd) | 429g AI 1.00 |
| HG20 | Human | [433g HG20-emuC](https://www.pangram.com/history/41c0e263-0634-4582-affa-dd9ce4f1a398) | 429g AI 1.00 |
| HG21 | Human | [431g HG21-emuA](https://www.pangram.com/history/3dcb39d2-f19e-47f8-b88a-40db881f3a00) | 429g AI 1.00 |
| HG22 | Human | [430g HG22-emuA](https://www.pangram.com/history/966ede09-185e-4eed-a1bb-d8e5048c2979) | 429g AI 1.00 |
| HG23 | Human | [431g HG23-emuA](https://www.pangram.com/history/57f9ffc1-d21b-4098-afca-272ea42bd7b0) | 429g AI 1.00 |
| HG24 | Human | [437g HG24-emuH](https://www.pangram.com/history/e270cbd7-3272-446d-8042-771294c32b77) | 429g AI 0.98; 433g AI 0.18; 435g AI 0.43 |
| HG25 | Human | [431g HG25-emuA](https://www.pangram.com/history/c67eef25-4a2b-46ad-b693-7a8b5564708c) | 429g AI 1.00 |
| HG26 | Human | [431g HG26-emuA](https://www.pangram.com/history/7d2d5e40-6356-4aca-b56c-c799d7599c06) | 429g AI 1.00 |
| HG27 | Human | [435g HG27-emuF](https://www.pangram.com/history/d3b20b3a-4da8-4e6f-ad46-9228719a9453) | 429g AI 1.00; 430g H 0.03 |
| HG28 | Human | [431g HG28-emuA](https://www.pangram.com/history/0c6cef60-62d0-4dd4-a5ef-7cd324102183) | 429g AI 1.00 |
| HG29+30 | Human | [439g HG29+30-emuI2](https://www.pangram.com/history/c26e0b02-5d1b-46c9-b266-01cf35a95498) | 429g AI 1.00; 431g AI 0.29; 433g AI 0.56; 436g AI 0.26; 437g AI 0.30; 438g H 0.12 |
| HG31 | Human | [440g HG31-emuK](https://www.pangram.com/history/79d0de8c-c05a-47ae-bd75-3b6a41725a57) | 429g AI 1.00; 433g AI 0.32; 435g AI 0.16; 436g AI 0.18; 437g AI 0.18; 438g AI 0.18; 439g AI 0.12 |
| HG32 | AI (1.00) | [435g HG32-emuF](https://www.pangram.com/history/5a25465d-60b9-4bea-a03a-011b2ecdcb1a) | 429g AI 1.00; 432g AI 0.99 |
| HG33 | Human | [435g HG33-emuF](https://www.pangram.com/history/a117d978-81e6-471a-b69a-ef650de6bd61) | 429g AI 1.00; 432g AI 0.28 |
| HG34 | Human | [431g HG34-emuA](https://www.pangram.com/history/393c3a23-f072-46b9-bbbd-3b073cb56b87) | 429g AI 1.00 |
| HG35 | Human | [433g HG35-emuC](https://www.pangram.com/history/30bbefef-30dd-4839-8310-faed3b8c9a77) | 429g AI 1.00 |
| HG36 | Human | [431g HG36-emuA](https://www.pangram.com/history/e4da8a40-1ed7-448d-878f-135793d37bd5) | 429g AI 1.00 |
| HG37 | Human | [439g HG37-emuJ](https://www.pangram.com/history/c79fca14-43f7-4f65-9328-30172dbf33f7) | 429g AI 1.00; 433g AI 0.64; 436g AI 0.66; 437g AI 0.53; 438g AI 0.12 |
| HG38+39 | Human | [439g HG38+39-emuJ](https://www.pangram.com/history/33b4df99-cdfd-4b05-b795-e1c6162ea422) | 429g AI 1.00; 433g AI 0.59; 436g AI 0.18; 437g AI 0.15; 438g AI 0.16 |
| HG40 | Human | [432g HG40-emuB](https://www.pangram.com/history/9c0b1518-c6fb-4ba2-89fd-4d8037aa1bcb) | 429g AI 1.00 |

## 2026-10-18 04:00 UTC

**Where it stands.** 37 sections (a section under 50 words checked with the next). 3 read 100% Human as published. 25 more
read 100% Human as Emulate rewrote them (their screens), but those are not installed yet: Emulate bends the meaning (it
invented a "Sarah", quotations, studies' conclusions, turned the inner child into "her", reversed cautions), so each
went through my meaning review against the published text, then a second reader (verify), then a march read. Batch 434g
is the test of whether the meaning-fixed versions still read Human. 9 sections still read AI somewhere (table).

**Running now.**
- Second reader (verify-b) for HG14, HG20, HG35, HG02+03, HG27 and HG33.
- Emulate third samples (`fix-20261018/emu-h/`, 12 runs, 2,988 words) on the laptop: each AI window of 436g (and 435g
  for HG24) sent whole, with its headings, as one run.

**Learned today.**
- Emulate's text reads Human far more often than mine: 25 of 34 sections on the first or second screen.
- Second samples of short pieces (40 to 180 words) inside an AI window don't help: 436g, 0 of 7 Human (HG04 got worse:
  its one 108-word AI window became the whole text).
- My meaning fixes take breaks out: march-c found 6 stretches where the published words I put back read flat
  (HG14 B6, B38, B42, B51, B60; HG35 B2); the gate holds those until a break is back.
- The de-hypnosis checklist (HG32) reads AI in every version (published, Emulate whole, Emulate in six pieces): a list
  of short questions. It needs Joel's call (questions page).
