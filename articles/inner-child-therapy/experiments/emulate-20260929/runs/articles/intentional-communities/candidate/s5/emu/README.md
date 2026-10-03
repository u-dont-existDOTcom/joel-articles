# Emulate versions of section 5 (2026-10-03, API, two calls per unit)

Exact copies of the outputs on Joel's laptop (`/home/joel/ai-work/claude-dangerous-lane/emulate-runs/community-s5/`); the hash of the 24 texts matched there and here (sha256 of the sorted JSON: 836d2cfa…). Inputs are in `../emu-in/` (hash aad529ad… on both sides; units in `units.json`): e1 = P1+P2, e2 = P3–P5, e3 = P6–P8, e4 = P9–P11, e5 = P12–P14, e6 = P15–P17, e7 = P18–P20, e8 = P21–P23, e9 = P24–P26, e10 = P27+P28, e11 = P29–P31, e12 = P32+P33. Every paragraph was sent: the published section read 97% AI, Human only for 39 words in P10's middle. Last balance shown: 248,597.

What came back, before any fix:
- Facts: both e1 versions changed the dates' sense (e1-emuA: Oregon "set to start opening … in 2023", Colorado "set to begin licensing in 2025", New Mexico's Act "set to take effect in 2025"; e1-emuB: "being legalized and regulated", "a limited number of patients").
- Invented material: e2-emuA "the Rethinking Recovery posts"; e7-emuA "the traditional lineages I have worked with"; e8-emuA "I am teaching people" and "the ceremonies I lead"; e3-emuB a personal experience in Joel's voice.
- Garbage: e4-emuB opens as a reader's comment ("This is really excellent, I love that breakdown"); e5-emuB opens with "Account Type: Free Membership" and turns P13 and P14 into numbered headers; e7-emuB's "shitwomping".
- Reversals: e10-emuB's last sentence ("A good place to start might be by asking if anybody in the community has heard of it") turns P28's warning around, and puts Joel in the first person doing something illegal.
- Specific pairings flattened: e2-emuA's "for fear of scaring off potential parents, neighbors, insurance, official types" for P4's four separate reasons.

## Round 2 (2026-10-03, 02:30 UTC): the runs around the paragraphs that read AI

After round 1 of Pangram (P6, P7, P18 with its heading, P31 and P33 read 100% AI), three runs went to Emulate again, two calls each, this time with v4's text as input (the meaning already fixed): f1 = P6–P8, f2 = P18+P19, f3 = P29–P33. Inputs in `../emu-in2/` (hash dc5c1171… on both sides); outputs in `outputs2.json` (hash aaef33bd… on both sides). Balance after: 247,539.

What came back: f2-emuA declined the principle ("I won't go down the path of the need or lack thereof of shamans"); f1-emuA dated the survey ("came out recently") and garbled the severe-effects clause; f1-emuB swore ("when they've fucked up", "a bit shit") and changed P7's claim; f3-emuA's P32 garbled the order ("wait until … you have a few people who are depending on you, to read the sections"); f3-emuB's P30 to P31 and P33 kept most of the meaning, and its P32 didn't.
