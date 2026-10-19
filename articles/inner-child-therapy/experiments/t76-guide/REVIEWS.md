# Turn 76 (2026-10-19): the slow wrap-up, and innerSignalGraph's queue r12

His message of 00:55 UTC, word for word, is in `experiments/t76-answers/JOEL-20261019-0055.md`: "well that's crazy it took you 14m to put one line in... def need to fix that right? start workin on the innerSignalGraph queue i guess, altho i already forgot what all that is".

## Where turn 75's 14 minutes went (commit times and Pangram's own stamps)

| From | To | What |
|---|---|---|
| 00:26:00 his message | 00:27:50 round a pushed | his message recorded, the turn tool copied, the draft, lint, march, the batch |
| 00:27:50 | 00:29:07 | the browser run (Pangram's results 00:29:04 and 00:29:07) |
| 00:29:07 | 00:30:29 install commit | the read, save, score and install |
| 00:30:29 | 00:31:55 | OWNER-EDITS, the questions page, the records, CURRENT-STATE, the pull request |
| 00:31:55 | 00:35:45 review map commit | the article page, a review-page builder written by hand, a screenshot (a context summary came in here) |
| 00:35:45 | 00:40:21 the stamp | files sent, the handoff note's method looked up again, credits (two calls), a second rules pull, the link checks one at a time |

So the sentence was in after four and a half minutes, and the wrap-up took ten. The fix is lesson E199 (`docs/HUMANIZATION-GATE.md`) and five scripts in `tools/humanization/` with tests: `lane_push.py`, `lane_state.py`, `review_rows.py`, `pangram_js.py`, `handoff_note.py`. Measure the next small turn the same way.

Two things this turn's use of them taught:
- The browser tool stops a call after 45 seconds, and one read of the results can take ten seconds or more, so a call can't run a batch and wait for it. `pangram_js.py` now prints a run call per tab and a separate single read, which keeps its results in `window.__res`.
- In round b one of my read calls stored its results in `window.__t76b`, the reverse lane's own log, and that tab stopped after six checks; the forward lane finished the rest. Reads never write a round's variable now.

## The queue

innerSignalGraph's `authoring/PENDING-PUBLIC-GUIDE-CHANGES.md`, version 2026-10-18-r12, at 55b2b0dd (unchanged when fetched this turn). PGQ-018 to PGQ-026 are the T1 to T9 points he OK'd on 2026-10-09, all in (023's list with his 54, 11 in turn 74). PGQ-027 to PGQ-039 are new to the article. The pain and medical-care entries were also checked against the guide's own paragraphs (innerSignalGraph `guides/inner-child-guide-2026-10-11-r6.txt`, "If the urge to escape comes during severe physical pain", "If severe pain attacks happen almost every day" and "Past coercive or frightening medical treatment"), as the grounding advised.

| Entry | What | Where it went | Status |
|---|---|---|---|
| 027 | urgent medical care during unbearable pain | When the Urge to Escape Arrives P13, end of the h3 (P2's "that part" points back at P1) | in (ue27-f), with PGQ-030's pain-thought point |
| 028 | support isn't a shortcut to romance | Borrowed Adulthood in Relationship, after his P2 | in (ba3-e) |
| 029 | frequent severe pain: a specialist and a written flare plan | When the Urge to Escape Arrives P14 | in (ue29-b) |
| 030 | care after coercive or harmful care | Also Look Outward, after P10 | not yet: with its real-danger sentence the h1 reads Mostly Human, a window on his When Healing Turns Into Checking P1 (question 68) |
| 031 | gratitude as ongoing cultivation | his Ask God for a Loan already carries it | question 67 |
| 032 | a drug peak that changes nothing | Altered States Can Deepen the Therapy, after the Kornfield paragraph | in (as4b-f), no one named (question 64) |
| 033 | "if only I had X" | Ask God for a Loan, after his P5 | in (ag5b-c), no source (question 65) |
| 034, 035, 036 | gratitude without pushing; gratitude in a calm altered state; hypnosis with grief or an altered state | his to write (the queue: "The owner will write this himself") | question 66 |
| 037 | reparenting isn't an exercise | The Chicken-and-Egg Problem, a short paragraph after my PGQ-012 one | in (cs57x-a) |
| 038 | keeping yourself safe is part of the work | Not Every Hero Wears A Cape, a short last paragraph | in (hero6-e) |
| 039 | before sharing something legally or personally sensitive | Also Look Outward, after 030 | not yet: P1 reads Human alone, P2 AI in six versions (question 69, with the legal review) |

## Grounding (`GROUNDING-t76.md`, a Sonnet reader, on round a's versions)

MUST fixes, all made: the pain paragraph's last line sent any thought of dying to crisis steps ahead of the medical route (now only a fear of acting goes there), and its flare plan dropped the new or severe signs that still mean going in; the care paragraph spoke of "a pain attack" before the article has any physical pain (that point moved to the pain paragraph) and never said to tell someone when the danger is real; the privacy paragraphs didn't separate an urge never acted on from something done. SHOULD fixes, all made: "You're lovable already" read as romance being owed; the drug-peak paragraph's "or the anger" had nothing before it; "if only I had X" lacked its point that gratitude waiting on the list never shows up; "won't make you anonymous" was more certain than the entry; the privacy paragraph read as a checklist. Kept from the guide paragraph, as it advised: "a relative who has not respected your wishes".

## Rounds (Pangram's stamps, UTC)

- **t76a** (01:25:44 to 01:27:00, 15 checks). Human: 032 alone (0.0078) and in its h1 (0.070, high); 033 in its h1 (0.052, high). AI alone: 028 (0.67; its h1 0.83), 027 and 029 as one paragraph (0.80), 030 (0.99), 039 (0.89, 0.66), 037 inside my PGQ-012 paragraph (0.73), 038 (0.99). Before You Try to Go Deep had a 591-word window from the graded-disclosure paragraph's middle through the new ones.
- **t76b** (01:34:26 to 01:39:29, 18 checks; second versions in his voice: scenes, "I'd", asides). Human: 028 v3, the dating app in the night (alone 0.105; its h1 0.059, high). Still AI alone: 027 and 029 (0.785), 030 (0.96, 0.99), 039 (0.77, 0.90), 037 (0.95), 038 (0.98, 0.98), though both 038 versions read Human in their h1.
- **t76c** (01:45:18 to 01:46:38, 16 checks; the grounding's fixes, the pain item split in two as in the guide). In: 028 (ba3-e, alone 0.134, h1 0.082 high), 032 (as4b-f, alone 0.031, h1 0.073 high), 033 (ag5b-c, h1 0.052 high). 029 alone 0.22 (Human). Still AI alone: 027 (0.65), 030 (0.95), 037 (0.92), 038 (0.99); 039 P1 read Human for its first 58 words and AI for the last 88 (0.55), P2 0.77.
- **t76d** (01:51:51 to 01:52:37, 10 checks). 030 short (lo-med-g, 54 words) alone Human (0.124). 037 and 038 as the queue asks, one or two sentences each, under the gate's 50 words, so their checks are their sections': The Chicken-and-Egg Problem 0.031, high; Not Every Hero Wears A Cape 0.094, high; Building Trust With Your Little One 0.032, high. Still AI: 027 (0.86); 039 P1 Human for 91 words, AI for its last 55 (0.41); P2 0.997. Also Look Outward with 030 and 039 read AI from "The same goes for doctors" on (416 words).
- **t76e** (01:58:30 to 01:59:04, 7 checks). Before You Try to Go Deep with 030 alone (lo-med-g) Human (0.084, high); its h3, Also Look Outward, read AI Detected (0.19), windows on P10's second half with 030 and on T9's last lines (P11 of the old order). 027 v5 AI (0.71); 039 P1 v5 AI (0.62, worse than v4), P2 v5 0.994.
- **t76f** (02:02:20 to 02:02:41, 5 checks). 027 v6 (ue27-f, without my "even" and "actually") Human alone (0.221) and When the Adult Voice Feels Fake with it and 029 Human (0.072, high): in. 039 P1 v6 (round d's Human part kept, a plainer last part) Human alone (0.193, high); P2 v6 AI (1.00); the h1 with both had windows on them and on his When Healing Turns Into Checking P1.
- **t76g** and **t76h** (02:04:59 to 02:07:46, 6 checks). 030 with the guide's real-danger sentence, three wordings (lo-med-h, -i, -j), Human alone (0.32, 0.13, 0.22), and each time Before You Try to Go Deep read Mostly Human (0.10, 0.097, 0.094) with the same 95-word window on his When Healing Turns Into Checking P1, "You can get hooked on healing too. The wound can be completely real ..."; without the sentence the h1 read Human (round e). That opening is the one that kept a window in turns 72 and 73 until his 62, C, so E198 says it's that paragraph's, and it's his text: question 68. 030 stays out rather than going in without the sentence (E168).

## Installed (turn 76)

PGQ-028 (ba3-e), 032 (as4b-f), 033 (ag5b-c), 027 (ue27-f) and 029 (ue29-b), 037 (cs57x-a), 038 (hero6-e): installs76.py, `t76.py install ba3,as4b,ag5b,ue2,cs57,hero6 RESULTS-final.json`; owner edits 188 pass. The cold read of the seven in place is `COLD-READ-t76.md`.

## Delegations (UDA `patterns/delegate-easy-work-to-cheaper-models.md`)

- Sonnet subagent, the trace of PGQ-027 to 039 against the article and his decisions (`TRACE-PGQ-r12.md` when it reports).
- Sonnet subagent, the grounding of round a's drafts against the queue (`GROUNDING-t76.md`): checked by reading each finding against the entry and the guide; every MUST and SHOULD taken.
