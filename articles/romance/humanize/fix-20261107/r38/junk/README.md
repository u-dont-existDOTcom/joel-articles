# The junk pass: the partly real passages that still stood (2026-11-24)

The vetted junk read (`../../r30/junk/VETTED.md`) found 30 passages partly real. Of those, nine no longer stood in the
fixed version: later fixes had changed their flagged words (B87, B155, B210, B331, B363, B414, B435, B459's "honestly",
B482), and B22's sentence is one his own fix of section 05 kept. [build_items.py](build_items.py) put the other 21 in
their 16 sections, each flagged sentence marked with what the readers found ([PARAS.md](PARAS.md),
[ITEMS.json](ITEMS.json)).

A Fable writer given [BRIEF.md](BRIEF.md) (his way with such passages, lesson romance-2026-11-23h: only the flagged
words and their order, with words the passage already has, nothing added; and the ways of `his_fixes_brief.md`) wrote
[OUT.md](OUT.md). Three fresh Sonnet readers filled the receipts ([receipts.py](receipts.py), FILL-1 to 3); their reads
found four of the fixes still at fault, which I fixed before any check (B47's "about all that" now names the
conversation in the sentence it joins; B128's packed list is two clauses; B178's "Although" became a "though" joined to
the advice it qualifies; B459's "those friends" became "when you do ask friends for help"), and my verdict on every
question they failed is in each receipt with its evidence ([fix_receipts.py](fix_receipts.py)).

## The checks (predicted first, ledger batch romance-r38j)

12 of the 16 sections read Human High in every window at once. The other four each had one short window of the
article's own text that the fix had moved into a window of its own; three second tries joined it to the sentence it
belongs to (t2/), and all read Human High:

| Section | Items | Its check |
|---|---|---|
| Labels Are Descriptive, Not Prescriptive | B47 | [High](https://www.pangram.com/history/d350c49e-7388-4195-9c0e-d68d1a7d06c1) |
| Should you be in a relationship at all? | B50, B54 (card) | [High](https://www.pangram.com/history/14dd222c-80ab-4081-8c71-22c7f7b8ef8a) |
| Peeking thru the window, part 1 | B123 | [High](https://www.pangram.com/history/83f2bd73-ac4a-45e6-a812-25d6593e9d78) |
| Peeking thru the window, part 2 | B128 | [High](https://www.pangram.com/history/389d4b27-460e-41f4-95d1-b7a19ebcc09a) |
| Things get tricky fast | B148 | [High](https://www.pangram.com/history/8d300648-e283-4b37-842c-ff05f7caeaf5) |
| Anti-PTSD Can Be Just As Dangerous As PTSD, part 2 | B170, B173 | [High](https://www.pangram.com/history/f6992267-1ad3-4d02-812b-4b8049fc7455) |
| Seeing idealization right | B178 | first [Medium on "Your mom and dad?"](https://www.pangram.com/history/242a5f1f-dab7-491b-8a27-427c1f4d88a5), joined: [High](https://www.pangram.com/history/4fca819f-3ceb-4696-9101-4cad8af7c8ae) |
| Don’t make your partner your whole world, part 1 | B217 (card) | [High](https://www.pangram.com/history/48f4f1be-52c4-4b12-bfcc-fd3a822766a4) |
| Disconnect to connect | B230 | [High](https://www.pangram.com/history/8adb74f8-50a4-44bb-bc10-a791b91a8969) |
| Babies growing up again | B232, B234 | [High](https://www.pangram.com/history/6581e774-d26b-4cff-b3f5-0dae7f0746b3) |
| Different levels in different domains, part 2 | B255 (card) | [High](https://www.pangram.com/history/d76c7885-a0df-4467-ab2e-66c7100182cc) |
| Twin Flames? | B330 | [High](https://www.pangram.com/history/02df440f-5b80-48d2-aa8f-33d2ced8a343) |
| Jealousy on trial, part 2 | B391 | [Medium on another line](https://www.pangram.com/history/bc5d9d43-c6f8-4c06-ba1b-e73a724f2e91): left as it was (the fix narrowed the generic close's meaning, and the section read High without it) |
| Gaslighting in the dark | B459 | first [Medium on the sentence after it](https://www.pangram.com/history/87c5a922-f042-4ac2-a048-818c3a571b63), joined with a colon: [High](https://www.pangram.com/history/62a78ddb-899a-4516-97bc-07c037572eac) |
| After leaving | B465 | [High](https://www.pangram.com/history/8078da4a-e14e-412d-9a7c-f81454fe4558) |
| Tough Love, part 1 | B476, B477, B478 | first [Medium on "They’re suspicious of romance."](https://www.pangram.com/history/8b841491-e2ea-425e-8951-e0783d57d29c); with B477 only and that line joined: [High](https://www.pangram.com/history/85106123-7f10-4138-b9bd-ccb72ddfc237); B476 and B478 are questions |

## Where each went

[build_layer_j.py](build_layer_j.py) writes [MINE-R38J.json](MINE-R38J.json), 15 paragraph changes that keep the
meaning (B47, B123, B128, B148, B170, B173, B178, B230, B232, B234, B330, B459, B465, B477, and the two joins), the layer
`../../whole/build.py` applies last, and [CARDS-T8.json](CARDS-T8.json), the three that might change it (B50 with B54,
B217, B255). Those three and the questions on B476 and B478 are the eighth marking page
(`../../../../review/teach-20261124b/`, https://claude.ai/artifact/BfqATtsRc1ciJZSfmAjv8f); each card's paragraph has
its receipt in `para/`.

After the layer, `../sections.py --again` cut the fixed version again: every one of its 93 section checks is a text a
check read Human High in every window (91 mine, 05 and 67 his own).
