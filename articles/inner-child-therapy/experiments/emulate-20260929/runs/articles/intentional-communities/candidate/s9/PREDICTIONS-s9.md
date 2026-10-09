# Section 9 ("The Best Model I've Seen: Zapatistas"): predictions and Pangram results

Written before each call. Result times come from the History data of Joel's Pangram account (`s8/gui/helpers-hist.js`: server timestamp, verdict, windows), matched to each item by the text's sha-12.

The published section (`../../sections/010-original.md`): one h1, 17 paragraphs, two images with captions (884 words in the markdown). Blocks: `original-blocks.json`, `plain-blocks.json` (`build_blocks.py`). P1 to P5 are Joel's 2005 trip to Oventik; P6 on is about the Zapatista model.

Baseline, batch 147g (written 23:57 UTC by `date -u`, before the call; `v147.json`): the published text in the web app. Paragraphs under 50 words go with a neighbor.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 147g-pub-S9 (879) | Mixed | your story (P1 to P5) beside expository paragraphs that carry the published article's polish || AI (96%, 887 words scanned), 23:58:18: one AI window, P1's second sentence to the end (847 words) |
| 147g-pub-P1P2P3 (116) | Human (weak) | your 2005 trip; but "a nice combination when you're trying to visit a revolution" reads like a polished quip || AI (100%), 23:58:21 |
| 147g-pub-P4 (57) | AI | ends "to make the communities less easy to attack in silence" || **Human (100%)**, 23:58:26 |
| 147g-pub-P4P5 (90) | AI | P5 (33 words) needs a neighbor; "not as fact" tail || **Human (100%)**, 23:58:31 |
| 147g-pub-P6P7 (70) | AI | "not merely a voting method", the list of six || AI (100%), 23:58:35 |
| 147g-pub-P8 (83) | AI | the book summary || **Human (100%)**, 23:58:44 |
| 147g-pub-P9 (60) | AI |  || AI (100%), 23:58:50 |
| 147g-pub-P9P10 (98) | AI | P10 (38) beside P9 || AI (100%), 23:58:54 |
| 147g-pub-P11P12 (82) | AI | "The useful thing is not their diagram. It is how they learn" || AI (100%), 23:58:59 |
| 147g-pub-P13 (87) | AI |  || AI (100%), 23:59:03 |
| 147g-pub-P14P15 (94) | AI | "The point is not to make people feel transformed for a week. It is to teach" || AI (100%), 23:59:13 |
| 147g-pub-P15 (56) | AI |  || AI (100%), 23:59:17 |
| 147g-pub-P16 (90) | AI | "not claiming the Zapatistas already proved my whole model" || AI (100%), 23:59:22 |
| 147g-pub-P16P17 (131) | AI | P17 (41) beside P16 || AI (100%), 23:59:26 |

147g (submitted 23:58:18 to 23:59:26 UTC): mine 9 of 14. The section reads AI (96%). Only P4, P4 with P5, and P8 (the book summary) pass; the 2005 trip (P1 to P3) reads AI as published, and so does everything from P6 on except P8.

Plan (section 8's order): Emulate first on the flagged paragraphs (everything but P4, P5 and P8), in seven units (`emu-units.json`). Round a (`community-s9a` on the laptop, started 00:01:37 UTC) gets the published text (`emu-inputs-a.json`); round b (`community-s9b`, queued after a) gets my faithful plain version m1 (`mine-m1.json`, `emu-inputs-b.json`): each published sentence with the same claims, connectives and modals, lists of three split, and the published "not merely", "not their diagram" and "the point is not" turned around where the contrast survives without the x-not-y frame. Then: splice Emulate's sentences with word fixes back to the published meaning, lint, gate (traces, logic audits, cold read, stance), and check pairs and the whole section in the web app. P4, P5 and P8 stay as published unless the section's windows say otherwise.

## Draft v2 (`drafts-v2.json`)

Spliced from Emulate's rounds a and b (`emu/s9a-emu-all.json`, `emu/s9b-emu-all.json`) and m1, with word fixes back to the published meaning and the linter's FAILs fixed (two lists in P13, repeated openers): Emulate's outputs drifted as in section 8 (an invented "5 minutes", "the only white man there", a US-government aside, "I am impressed by what I see"), so only their phrasing is used. P4, P5 and P8 are as published.

Batch 148g (written 00:08 UTC by `date -u`, before the call; `v148.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 148g-S9-v2 (1012) | Mixed | new P1–P3 and P6–P17 beside the published P4, P5 and P8 || AI (86%, 1,034 words scanned), 00:09:07: one window, P4's second sentence to the end (872 words) |
| 148g-v2-P1P2P3 (129) | Human (weak) | Emulate's "college buddies", "on its last legs", "grilled us"; your jokes kept || **Human (100%)**, 00:09:10 |
| 148g-v2-P6P7 (100) | Mixed | P7's list split into sentences || AI (100%), 00:09:15 |
| 148g-v2-P7 (61) | Mixed |  || **Human (100%)**, 00:09:20 |
| 148g-v2-P9 (64) | AI | the 2023 change is official names and a description; hard to make plain || **Human (100%)**, 00:09:25 |
| 148g-v2-P9P10 (104) | Mixed |  || AI (100%), 00:09:34 |
| 148g-v2-P11 (57) | Human (weak) | the list split || **Human (100%)**, 00:09:38 |
| 148g-v2-P11P12 (97) | Mixed |  || AI (100%), 00:09:45 |
| 148g-v2-P13 (95) | AI | the economic path sentence and the outside-help warning stay abstract || AI (100%), 00:09:49 |
| 148g-v2-P14P15 (122) | Mixed |  || AI (100%), 00:09:53 |
| 148g-v2-P15 (76) | Mixed | "It shouldn't be about … It should teach" || AI (100%), 00:10:04 |
| 148g-v2-P16 (104) | Mixed | the research trail kept || AI (100%), 00:10:08 |
| 148g-v2-P16P17 (164) | Mixed |  || AI (100%), 00:10:12 |
| 148g-v2-P17 (60) | Human (weak) |  || AI (100%), 00:10:18 |

148g (submitted 00:09:07 to 00:10:18 UTC): mine 5 of 14. The trip (P1 to P3), P7, P9 and P11 pass; the section reads 86% AI. P6 (with P7), P10 (with P9), P12 (with P11), P13, P15, P16 and P17 read AI. Round c (`community-s9c`) gives Emulate the v2 text of those, one or two paragraphs per unit.

Round c's outputs (`emu/s9c-emu-all.json`; u1 ran as P6 with P7, since Emulate refused P6's 39 words) drift as before ("to fight off the scum that would oppress them", "for people to go and tell their friends about", "there is no research"); used for phrasing only. A trace of the six passing paragraphs (`review-d2/changes-passed.md`) found P1 to P3 clean and three shifts: P7 ("their own" no longer reached every item, "while" became a new item, "They're" after a paragraph about representatives), P9 (the "rather than superior to them" description became a bare claim), P11 ("share a language": the communities speak several). Fixed in P7f, P9f and P11f (`fix-v3-parts.json`).

Batch 149g (written 00:26 UTC by `date -u`, before the call; `v149.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 149g-P6aP7f (98) | Mixed |  || Mixed (38% AI), 00:27:23 |
| 149g-P6bP7f (99) | Mixed | Emulate c's "Basically," || AI (100%), 00:27:28 |
| 149g-P7f (61) | Human (weak) | the trace's fixes on a passing P7 || **Human (100%)**, 00:27:31 |
| 149g-P9f (61) | Human (weak) | the published last clause back || **Human (100%)**, 00:27:35 |
| 149g-P9fP10a (101) | Mixed |  || AI (100%), 00:27:41 |
| 149g-P9fP10b (107) | Mixed | Emulate c's "The pattern in most institutions" || AI (100%), 00:27:49 |
| 149g-P11f (56) | Human (weak) | "share language" || **Human (100%)**, 00:27:54 |
| 149g-P11fP12a (100) | Mixed | Emulate c's "It's okay to copy how they learn, though" || AI (100%), 00:27:59 |
| 149g-P11fP12b (99) | Mixed |  || AI (100%), 00:28:03 |
| 149g-P13a (111) | Mixed |  || AI (100%), 00:28:08 |
| 149g-P13b (106) | Mixed |  || AI (100%), 00:28:13 |
| 149g-P14P15a (114) | Mixed | Emulate c's "a performance of community" || AI (100%), 00:28:25 |
| 149g-P14P15b (117) | Mixed |  || AI (100%), 00:28:29 |
| 149g-P16a (96) | Mixed |  || **Human (100%)**, 00:28:34 |
| 149g-P16b (101) | AI | close to the published || **Human (100%)**, 00:28:38 |
| 149g-P17a (55) | Mixed | Emulate c's "landed on" || AI (100%), 00:28:43 |
| 149g-P17b (52) | Mixed |  || AI (100%), 00:28:48 |

149g (submitted 00:27:23 to 00:28:48 UTC): mine 3 of 17 (most were "Mixed" guesses that came back one way or the other). The trace's fixes keep P7, P9 and P11 passing; both P16s pass. P6 with P7 came close (38%). P10, P12, P13, P15 and P17 read AI in every wording. Round d (`community-s9d`, 00:29:52 UTC) asks Emulate for fresh samples of the published text.

Batch 150g (written 00:30 UTC by `date -u`, before the call; `v150.json`, parts in `fix-v4-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 150g-P6cP7f (98) | Human (weak) | P6 plainer, "the people who sent them" || AI (100%), 00:30:42 |
| 150g-P6dP7f (94) | Mixed |  || AI (100%), 00:30:47 |
| 150g-P10aP11f (96) | Mixed | P10 beside its other neighbor, which passes alone || AI (100%), 00:30:51 |
| 150g-P10bP11f (102) | Mixed |  || AI (100%), 00:30:56 |
| 150g-P10cP11f (100) | Mixed |  || AI (100%), 00:31:00 |
| 150g-P9fP10c (105) | Mixed |  || AI (100%), 00:31:07 |
| 150g-P11fP12c (105) | Mixed | Emulate c's "have been clear about", "It's okay to copy how they learn, though" || **Human (100%)**, 00:32:42 |
| 150g-P13c (106) | AI |  || AI (100%), 00:32:46 |
| 150g-P15a (68) | Mixed | P15 alone (66 words) || **Human (100%)**, 00:32:51 |
| 150g-P15b (71) | Mixed |  || AI (100%), 00:32:56 |
| 150g-P15e (78) | Human (weak) | Emulate c's sentence with its meaning fixed || **Human (100%)**, 00:33:01 |
| 150g-P17c (58) | Mixed |  || AI (100%), 00:33:05 |

150g (submitted 00:30:42 to 00:33:05 UTC): mine 2 of 12. P12 passes beside P11 (Emulate c's "have been clear about" and "It's okay to copy how they learn, though"), and P15 passes alone in two wordings (a, and Emulate c's e). P6, P10, P13 and P17 read AI in every wording again; P10 fails beside both neighbors. Before adopting: P12c's "It's okay to copy" turns the published "the useful thing" into a permission, and its "when the practice isn't working" drops "discover where"; P15a's "people's lives" loses "residents"; P15e turns "teach enough of the system" into teaching about how it works. Those get word fixes and a recheck.

Round d's outputs (`community-s9d`, read at 00:35 UTC) drift as before ("always have to obey", "charge people to attend", "closer to the people", "a lot of similar forms"); used for phrasing only.

Batch 151g (written 00:43 UTC by `date -u`, before the call; `v151.json`, parts in `fix-v5-parts.json`, built by `build_batch.py`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 151g-P6eP7f (102) | Mixed | closest to 149g's 38% (P6a), "are in charge of carrying out" from Emulate d || AI (100%), 00:43:43 |
| 151g-P6fP7f (101) | AI | "which they call" || Mixed (60% AI), 00:43:47: P7 |
| 151g-P6gP7f (102) | Human (weak) | "how they do authority", a colon || **Human (100%)**, 00:43:52 |
| 151g-P6hP7f (96) | AI |  || Mixed (42% AI), 00:43:57: P7 from its second sentence |
| 151g-P9fP10d (108) | AI | P10 fails beside P9 in every wording so far || AI (100%), 00:44:02 |
| 151g-P9fP10e (105) | AI | Emulate d's "took stock of what they'd built" || AI (100%), 00:44:12 |
| 151g-P9fP10f (105) | AI |  || AI (100%), 00:44:16 |
| 151g-P10dP11f (103) | Mixed | "more and more layers", a comma splice || AI (100%), 00:44:21 |
| 151g-P10eP11f (100) | AI |  || AI (100%), 00:44:26 |
| 151g-P10fP11f (100) | AI | "Usually the older an institution gets" || AI (100%), 00:44:30 |
| 151g-P11fP12d (107) | AI | the published "isn't their diagram" back, as its own sentence || **Human (100%)**, 00:44:37 |
| 151g-P11fP12g (106) | Human (weak) | 150g's passing P12c with "The useful thing to copy" and "find out where" || AI (100%), 00:44:42 |
| 151g-P13d (110) | AI | lists split; "the one where … come first" || AI (100%), 00:44:46 |
| 151g-P13f (104) | AI |  || AI (100%), 00:44:51 |
| 151g-P13h2 (104) | AI | the path in parentheses || AI (100%), 00:44:57 |
| 151g-P13i (102) | AI | closest to the published || AI (100%), 00:45:03 |
| 151g-P13k (110) | Mixed | "off the market"; the specialist, donor and organization split || AI (100%), 00:45:09 |
| 151g-P15f (68) | Human (weak) | 150g's passing P15a with "residents' lives" || **Human (100%)**, 00:45:13 |
| 151g-P15g (69) | Human (weak) | and "visitor business" back || AI (100%), 00:45:18 |
| 151g-P14xP15f (115) | Mixed | P14 from Emulate d: "day to day life there" || **Human (100%)**, 00:45:22 |
| 151g-P14y2P15f (114) | Mixed |  || **Human (100%)**, 00:45:29 |
| 151g-P16aP17d (144) | Mixed | P17 beside a passing P16 || AI (100%), 00:45:33 |
| 151g-P16bP17d (149) | AI |  || AI (100%), 00:45:40 |
| 151g-P16aP17e (145) | AI |  || AI (100%), 00:45:43 |
| 151g-P16bP17e (150) | AI |  || AI (100%), 00:45:47 |

151g (submitted 00:43:43 to 00:45:47 UTC): mine 14 of 25. Now passing: P6 beside P7 (g: "how they do authority"), P12 beside P11 with the published "The useful thing isn't their diagram" as its own sentence (d; the version without it, g, failed), P15 alone with "residents' lives" (f; "visitor business" back, g, failed), and P14 beside that P15 in both wordings (x and y2). P10 (beside either neighbor), P13 and P17 (beside either P16) read AI 100% in every wording: twelve P10s, ten P13s and eight P17s so far. Round e (`community-s9e`, started 00:47:33 UTC) gives Emulate my faithful plain versions of those three.

Round e's outputs (`community-s9e`, read 01:19 UTC) drift as before ("a natural tendency for entropy", "decided to simplify", "while angry and upset", "often created problems"); used for phrasing only. A trace agent run on the newly passing paragraphs hit its output limit after 30 minutes and wrote nothing (00:48 to 01:18 UTC); rerun in smaller pieces with a word cap.

Batch 152g (written 01:22 UTC by `date -u`, before the call; `v152.json`, parts in `fix-v6-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 152g-P10oP11f (104) | AI | Emulate e's order (the Zapatistas first, "unlike most institutions"), its "Note that" || AI (100%), 01:22:48 |
| 152g-P10o2P11f (102) | AI | the same without "Note that" || AI (100%), 01:22:53 |
| 152g-P10pP11f (102) | AI | Emulate e's "there's a tendency" || AI (100%), 01:22:56 |
| 152g-P10nP11f (103) | Mixed | a question and "No," || Mixed (66% AI), 01:23:01: from "No, they changed" to the end |
| 152g-P9fP10n (108) | AI |  || AI (100%), 01:23:06 |
| 152g-P9fP10o2 (107) | AI |  || AI (100%), 01:23:16 |
| 152g-P13o (111) | Mixed | the last two sentences plainer: "stop buying … on the market", "make a community more capable" || AI (100%), 01:23:20 |
| 152g-P13p (111) | Mixed | "Now," and the path in parentheses || Mixed (75% AI), 01:23:25: from "Their communities use" to the end |
| 152g-P16a3 (96) | Human (weak) | the trace's fixes I made myself: "alone" back, "replicate" without "it", "clear" for the linter's "clean" || Mixed (53% AI), 01:23:29: the first 55 words |
| 152g-P16b3 (103) | Human (weak) | the same fixes on P16b || **Human (100%)**, 01:23:34 |
| 152g-P16b3P17f (152) | AI | Emulate e's "on the fly" || AI (100%), 01:23:42 |
| 152g-P16b3P17g (155) | AI | Emulate e's "origin story", "arrived at" || AI (100%), 01:23:46 |
| 152g-P16b3P17h (158) | Mixed | a question and "No." || AI (100%), 01:23:50 |
| 152g-P16a3P17g (148) | AI |  || AI (100%), 01:23:55 |
| 152g-P16a3P17h (151) | Mixed |  || AI (100%), 01:23:59 |

152g (submitted 01:22:48 to 01:23:59 UTC): mine 11 of 15. P16b with its fixes passes alone (b3); P16a with the same fixes doesn't (53%). Two partial passes show what reads human here: P10's question ("Did they put out a book…?") passes until "No, they changed…", and P13's opening ("Now, the Zapatistas also don't prove… (That's the one that goes…)") passes until "Their communities use collective work". P10, P13 and P17 still fail whole. P17 variants of 50 words or more can be checked alone, since only a paragraph under 50 words may lean on a neighbor.

Batch 153g (written 01:26 UTC by `date -u`, before the call; `v153.json`, parts in `fix-v7-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 153g-P10r (50) | Mixed | 50 words, so it has to pass alone; "Nope", "just went and changed" || **Human (100%)**, 01:26:38 |
| 153g-P10rP11f (106) | Mixed |  || not sent (the page had no submit button) |
| 153g-P10sP11f (101) | Mixed | "right?", "No, they changed" || not sent (no submit button) |
| 153g-P9fP10r (111) | AI |  || not sent (the text box didn't match) |
| 153g-P13q (114) | Mixed | a question and "Yes." for the support sentence; "sure" || Mixed (47% AI), 01:26:39: from "What they do show" to the end |
| 153g-P13s (110) | AI | "yes" tacked on; "off the market" || AI (100%), 01:26:46 |
| 153g-P13t (111) | Mixed | Emulate b's "by pooling their work", "make money selling" || Mixed (75% AI), 01:26:51: from "Their communities support" to the end |
| 153g-P13u (111) | Mixed | and "Outside help is double-edged, though" || AI (100%), 01:26:55 |
| 153g-P17g (52) | AI | 52 words: alone || AI (100%), 01:27:00 |
| 153g-P17h (55) | AI | 55 words: alone || AI (100%), 01:27:04 |
| 153g-P17j (57) | Mixed | "Then there's sociocracy", the question || AI (100%), 01:27:12 |
| 153g-P17l (62) | Mixed | "Now, the resemblance" || AI (100%), 01:27:17 |
| 153g-P16b3P17j (160) | AI |  || AI (100%), 01:27:21 |

153g (submitted 01:26:38 to 01:27:21 UTC; three P10 pairs didn't go through, a page glitch, and weren't needed): mine 5 of 10. P10 passes alone at 50 words (r: "Did they put out a book on leadership and open a certification program? Nope. They just went and changed…"), so it no longer needs a neighbor. P13 with the support sentence as a question ("Do their communities use collective work…? Yes.") reads human up to "What they do show" (q, 47%). P17 fails alone in four wordings of 50 words or more.

Batch 154g (written 01:29 UTC by `date -u`, before the call; `v154.json`, parts in `fix-v8-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 154g-P13v (112) | Mixed | 153g's q with "you can stop buying" and the last sentence's condition first || **Human (100%)**, 01:35:54 |
| 154g-P13w (109) | Mixed | a second question ("So what do they show?") || **Human (100%)**, 01:35:57 |
| 154g-P13y (113) | Mixed | q with only the last sentence changed || **Human (100%)**, 01:36:03 |
| 154g-P17m (61) | Mixed | the four forms split into two sentences || AI (100%), 01:36:07 |
| 154g-P17r (62) | Mixed | "anyway", "Nope." || **Human (100%)**, 01:36:12 |
| 154g-P16b3P17p (152) | AI |  || AI (100%), 01:36:16 |

154g (submitted 01:35:54 to 01:36:16 UTC): mine 1 of 6. P13 passes alone in all three wordings (v, w, y); y changes only 153g's last sentence ("Outside help can make a community more capable, sure. But if the specialist or the donor or the organization stays indispensable, it can also…"). P17 passes alone at 62 words with its four forms in two sentences, "anyway" and "Nope." (r).

Traces (fresh Sonnet agents, `review-d3/trace-A.md` and `trace-B.md`, 01:30 to 01:36 UTC): P10r and P14y2 clean. Fixes adopted: P6g "carry out" back to the published "carry" (carrying decisions isn't only executing them); P12d without the added "though", and with "themselves" back; P14x dropped for y2 ("As part of celebrating" implies a wider celebration); P15f with the residents as the ones performing ("residents spend their lives performing community", for "residents' lives turn into a performance"); P16b3 optionally "and then evidence" for "with evidence" (the published sequence). A gap in my own checks: v2's P1 is 52 words, so it has to pass alone (148g only checked P1 to P3 together), P3 has to lean on P4, and P12d at 51 words has to pass alone too.

Batch 155g (written 01:37 UTC by `date -u`, before the call; `v155.json`, parts in `fix-v9-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 155g-P1v2 (55) | Human (weak) | passed inside P1 to P3 (148g); never alone || **Human (100%)**, 01:38:19 |
| 155g-P1v2P2v2 (102) | Human (weak) |  || **Human (100%)**, 01:38:23 |
| 155g-P3v2P4 (84) | Human (weak) | P3 leaning on P4, which passes alone || **Human (100%)**, 01:38:27 |
| 155g-P6g2P7f (101) | Human (weak) | 151g's passing pair with "carry" for "carry out" || **Human (100%)**, 01:38:32 |
| 155g-P12d2 (51) | Mixed | 51 words, alone for the first time; "themselves" back, "though" out || **Human (100%)**, 01:38:36 |
| 155g-P15f2 (66) | Human (weak) | "residents spend their lives performing community" || **Human (100%)**, 01:38:44 |
| 155g-P14y2 (46) | Human (weak) | 46 words: checks whether Pangram scans it alone || not scanned: the web app gives no button, so it's under its 50-word minimum and leans on P15 |
| 155g-P14y2P15f2 (112) | Human (weak) |  || **Human (100%)**, 01:38:49 |
| 155g-P16b4 (104) | Human (weak) | "and then evidence" || **Human (100%)**, 01:38:54 |
| 155g-S9v3 (1040) | Mixed | every paragraph's current pick; P4, P5 and P8 published || AI (82%, 1,063 words scanned), 01:38:58: two windows, P4's second sentence to the end of P13 (601 words), and the end of P14 to the end of P17 (254 words) |

155g (submitted 01:38:19 to 01:38:58 UTC): mine 7 of 9 scanned. Every paragraph now passes alone, or beside a neighbor that does when it's under 50 words: P1 alone, P2 beside P1, P3 beside P4, P6 beside P7, P12 alone at 51 words with the trace's fixes, P14 beside P15, P15 and P16 (b4) alone with theirs. The whole section still reads 82% AI, in two windows: P4's second sentence to the end of P13, and the end of P14 to the end of P17. The first holds the three published paragraphs I'd kept (P4, P5, P8), which pass alone but read as AI prose; round f (`community-s9f`, started 01:40:00 UTC) gives Emulate P4 with P5, and P8. Next: windows of the section checked on their own, to find what tips them.

Batch 156g (written 01:40 UTC by `date -u`, before the call; `v156.json`): windows of the section, to find what tips them.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 156g-W-P4toP8 (274) | AI | the published P4, P5 and P8 around two passing rewrites || **Human (100%)**, 01:40:43 |
| 156g-W-P9toP13 (331) | Human (weak) | five passing rewrites, no published paragraph || AI (100%), 01:40:48 |
| 156g-W-P6toP13 (515) | AI | with the published P8 || AI (100%), 01:40:54 |
| 156g-W-CAP2toP17 (291) | AI | the second window as in the section || AI (100%), 01:40:58 |
| 156g-W-P15toP17 (232) | Mixed |  || AI (100%), 01:41:04 |
| 156g-W-CAP2toP16 (229) | Mixed |  || **Human (100%)**, 01:41:09 |
| 156g-W-CAP2toP17-b3 (290) | AI | P16 as b3 ("with evidence") || AI (100%), 01:41:15 |
| 156g-W-P16toP17 (166) | Mixed |  || AI (100%), 01:41:18 |

156g (submitted 01:40:43 to 01:41:18 UTC): mine 3 of 8. The published P4, P5 and P8 aren't the problem: P4 to P8 passes as a group. P9 to P13 reads AI as a group though each passes alone, and P16 with P17 reads AI though each passes alone; the caption to P16 passes, so P17 tips the second window.

Batch 157g (written 01:41 UTC by `date -u`, before the call; `v157.json`): smaller windows inside P9 to P13, and P16 with P17.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 157g-P9fP10r (111) | AI | P9 is the most formal of the five || AI (100%), 01:42:12 |
| 157g-P10rP11f (106) | Mixed |  || Mixed (47% AI), 01:42:17: P11 from its second sentence |
| 157g-P11fP12d2 (107) | Human (weak) | 151g passed with "though" || AI (100%), 01:42:22 |
| 157g-P12d2P13y (164) | Mixed |  || AI (100%), 01:42:26 |
| 157g-P9toP11 (167) | AI |  || AI (100%), 01:42:31 |
| 157g-P11toP13 (220) | Mixed |  || AI (100%), 01:42:38 |
| 157g-P10toP12 (157) | Mixed |  || AI (100%), 01:42:44 |
| 157g-P16b3P17r (165) | AI |  || AI (100%), 01:42:49 |
| 157g-P15f2P16b4 (170) | Human (weak) | inside the passing caption-to-P16 window || Mixed (54% AI), 01:42:53: P16 from its second sentence |

157g (submitted 01:42:12 to 01:42:53 UTC): mine 4 of 9. Every pair inside P9 to P13 reads AI (P10 with P11 at 47%), and so do the triples; P15 with P16 reads 54% AI. Each of these paragraphs passes alone, so each pass is close to the line, and two of them together cross it.

Fresh writers (`review-d4/`, the gate's reviewer-writer order: three fresh Opus writers per group from the published text, Joel's own paragraphs for voice, the owner bans and what Pangram has shown; 01:52 to 02:15 UTC) redrafted the two groups that read AI: P9 to P13, and P16 with P17.

Batch 158g (written 02:16 UTC by `date -u`, before the call; `v158.json`, parts in `fix-d4-parts.json`): each writer's group whole.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 158g-wA1 (313) | AI | fresh writer 1, P9 to P13 as a group; close to the published wording || AI (100%), 02:17:24 |
| 158g-wA2 (315) | AI | writer 2; sentences reordered || AI (100%), 02:17:28 |
| 158g-wA3 (319) | AI | writer 3; "I mean," || AI (100%), 02:17:33 |
| 158g-wB1 (155) | AI | writer 1, P16 with P17; P17 ends on the caveat || AI (100%), 02:17:38 |
| 158g-wB2 (162) | Mixed | writer 2; P16 opens with the borrowing || AI (100%), 02:17:42 |
| 158g-wB3 (157) | AI | writer 3 || AI (100%), 02:17:47 |

158g (submitted 02:17:24 to 02:17:47 UTC): mine 5 of 6. All six fresh writers' groups read AI (100%). Held to the published sentences, they wrote close to the published wording, and the writers took 12 to 28 minutes each.

Batch 159g (written 02:18 UTC by `date -u`, before the call; `v159.json`): a diagnostic. Does Emulate's own unedited output read human as a group? If it doesn't either, more splicing from it won't get these groups through.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 159g-emuG-u1A (336) | Human (weak) | Emulate g's raw output for P9 to P13, unedited: a diagnostic, not a candidate (it invents and drops claims) || **Human (100%)**, 02:19:16 |
| 159g-emuG-u1B (361) | Human (weak) | the same, sample B || **Human (100%)**, 02:19:19 |
| 159g-emuG-u2A (200) | Human (weak) | raw, P16 with P17 || **Human (100%)**, 02:19:24 |
| 159g-emuG-u2B (184) | Human (weak) |  || **Human (100%)**, 02:19:29 |

159g (submitted 02:19:16 to 02:19:29 UTC): mine 4 of 4. Emulate's own groups read human whole, invented claims and all, so its texture survives at group length where my word-level rebuilds didn't.

Batch 160g (written 02:22 UTC by `date -u`, before the call; `v160.json`, parts in `fix-v10-parts.json`): Emulate's raw groups read human, so this time its whole text is kept and only the meaning errors are fixed in place (its added "This is interesting", "most", "etc.", "Of course not", the invented book topic and teaching motto out; the published names, modals and claims back), with splits to find any fix that breaks it.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 160g-gA-fixed (329) | Mixed | Emulate g's raw B for P9 to P13 (100% Human) with every meaning error fixed in place, its own syntax kept || AI (100%), 02:22:49 |
| 160g-gA-fix9to10 (344) | Human (weak) | a split to find which fixes break it: P9 and P10 fixed, P11 to P13 raw || **Human (100%)**, 02:22:53 |
| 160g-gA-fix11to13 (346) | Mixed | P9 and P10 raw, P11 to P13 fixed || AI (91%), 02:22:58: P9 raw (58 words), and from P10's "And did they publish" to the end |
| 160g-gB-fixed (177) | Mixed | raw B for P16 with P17, every error fixed || AI (100%), 02:23:03 |
| 160g-gB-fixed-17e2 (173) | Mixed | P17 from raw A instead || **Human (100%)**, 02:23:07 |
| 160g-gB-fix16 (167) | Human (weak) | split: P16 fixed, P17 raw || **Human (100%)**, 02:23:12 |
| 160g-gB-fix17 (194) | Human (weak) | split: P16 raw, P17 fixed || **Human (100%)**, 02:23:17 |

160g (submitted 02:22:49 to 02:23:17 UTC): mine 3 of 7. P16 with P17 passes as a group with every meaning error fixed in place (P17 from raw A: e2). For P9 to P13, the fixes to P9 and P10 keep the group human, and the fixes to P11 to P13 break it.

Batch 161g (written 02:23 UTC by `date -u`, before the call; `v161.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 161g-gA-fix9to11 (336) | Human (weak) | split: P11's fixes alone added || Mixed (52% AI), 02:23:57: from P11's second sentence into P13 |
| 161g-gA-fix9to10-12 (349) | Human (weak) | split: P12's fixes alone || **Human (100%)**, 02:24:02 |
| 161g-gA-fix9to10-13 (332) | AI | split: P13's fixes alone; the most changed || AI (100%), 02:24:07 |
| 161g-gA-fixed-13y (323) | Mixed | all fixed, with my P13y (passes alone) for P13e || AI (100%), 02:24:11 |
| 161g-P16e (114) | Human (weak) | alone: 114 words || **Human (100%)**, 02:24:16 |
| 161g-P17e2 (59) | Human (weak) | alone: 59 words || **Human (100%)**, 02:24:20 |

161g (submitted 02:23:57 to 02:24:20 UTC): mine 4 of 6. P16e and P17e2 each pass alone too, so P16 and P17 are settled for Pangram (the trace comes next). In P9 to P13, P12's fixes are safe; P11's (52%) and P13's (100%) break the group, so both get smaller fixes that keep more of Emulate's sentences.

Batch 162g (written 02:25 UTC by `date -u`, before the call; `v162.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 162g-gA-11e3 (349) | Mixed | P11 with Emulate's "long periods of defending what they have" and "in terms of" kept || AI (100%), 02:26:20 |
| 162g-gA-11e4 (347) | Human (weak) | the same with Emulate's "a note of caution here" kept too || AI (100%), 02:26:23 |
| 162g-gA-13e4 (350) | Mixed | P13 fixed in place sentence by sentence, its lists split (e3 failed the linter with two lists of three; e4 pairs the four items) || Mixed (29% AI), 02:26:28: from P13's second sentence |
| 162g-gA-full-11e3 (350) | AI |  || AI (100%), 02:26:33 |
| 162g-gA-full-11e4 (348) | Mixed |  || AI (100%), 02:26:38 |

162g (submitted 02:26:20 to 02:26:41 UTC): mine 2 of 5. Both P11 fixes still break the group; P13 fixed sentence by sentence gets to 29%, flagged from its second sentence. Next: split P11's fixes (the three invented qualifiers out vs. the dropped trust clause back) and keep more of Emulate's P13 sentences.

Batch 163g (written 02:27 UTC by `date -u`, before the call; `v163.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 163g-gA-11x1 (364) | Human (weak) | diagnostic: raw P11 with only the trust clause added back || AI (100%), 02:27:55 |
| 163g-gA-11x2 (339) | AI | diagnostic: raw P11 with only its three invented qualifiers out || AI (100%), 02:27:59 |
| 163g-gA-11e5 (354) | Mixed | both, the trust clause as a plain last sentence || AI (100%), 02:28:04 |
| 163g-gA-13e5 (350) | Mixed | P13 keeping Emulate's parenthesis and "on the market" placement || Mixed (29% AI), 02:28:08: from P13's second sentence |
| 163g-gA-full5 (355) | AI |  || AI (100%), 02:28:13 |

163g (submitted 02:27:55 to 02:28:13 UTC): mine 1 of 5. Any change to Emulate's P11 flips the group: adding back only the dropped trust clause (x1) and removing only its three invented qualifiers (x2) each take it from 100% Human to 100% AI. P13 stays at 29% AI from its second sentence. The group passes only while it carries Emulate's inventions ("while in theory applicable to many contexts", "very strong communities", "etc."), so word-level fixing is done here. Under the gate's stop rule this goes to Joel as a structure question (`docs/HUMANIZATION-GATE.md`, step 6).

## Where section 9 stands (02:30 UTC)

- Passes alone, or beside a neighbor that does when under 50 words: every paragraph (155g, 161g).
- Passes as groups: P1 to P3, P4 to P8, the caption to P16, and P16 with P17 in Emulate-based wordings fixed in place (P16e with P17e2, 160g; each alone too, 161g). Not yet traced: P16e, P17e2.
- Fails as a group: P9 to P13, in every version tried (my word-level splices, three fresh writers, Emulate's raw output with its errors fixed). So the whole section fails (155g: 82% AI).
- Traced clean or fixed: P1 to P3, P6, P7, P9f, P10r, P11f, P12d2, P14y2, P15f2, P16b3/b4 (review-d2, review-d3). Not yet run: stance, cold read and the abstract-agent judge on the assembled section.

Trace of P16e and P17e2 (`review-d3/trace-C.md`, a fresh Sonnet agent, 03:41 to 03:47 UTC, 2026-10-09): three SHIFTs (P16e "long-term impact" for "what happened after", an added "Nonetheless"; P17e2 merged two of the four forms) and two judgments (the attendee made the founder; "they" with no noun antecedent). All five fixed in P16e2 and P17e3.

Batch 164g (written 03:44 UTC on 2026-10-09 by `date -u`, before the call; `v164.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 164g-P16e2 (114) | Human (weak) | the trace's fixes: "what happened after" for "long-term impact", "Nonetheless" out, the founder left open, "the Zapatistas'" back || **Human (100%)**, 03:44:34 |
| 164g-P17e3 (59) | Human (weak) | four forms again ("distributed authority, and linking between the levels") || **Human (100%)**, 03:44:38 |
| 164g-P16e2P17e3 (173) | Mixed | the group that passed before the fixes (160g) || **Human (100%)**, 03:44:43 |
| 164g-W-CAP2toP17 (298) | Mixed | the caption to the end, as in the section || **Human (100%)**, 03:44:51 |

164g (submitted 03:44:34 to 03:44:51 UTC, 2026-10-09): mine 2 of 4. With the trace's five fixes, P16 and P17 still pass alone, together, and from the caption to the end. (The history list also holds checks from another session on the same account at the same minutes, other texts; matched by hash, not by position.)
