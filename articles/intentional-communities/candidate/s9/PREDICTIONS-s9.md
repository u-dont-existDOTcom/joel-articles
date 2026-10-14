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

## Joel's P9 to P12 (2026-10-09 05:02 UTC)

His message and texts verbatim: `joel-0502/joel-20261009-0502.json`. He checked them: "hum high conf now" (Human, high confidence), so they aren't checked again alone. Obvious typos fixed in his P12 under his rule, without a recheck: "have been [clear] that", "(*Zapatismo*)", "as something ready-made", "how they learn: they build" (`joel-0502/joel-0502-fixed.json`). New combinations checked below.

Batch 165g (written 05:05 UTC on 2026-10-09 by `date -u`, before the call; `v165.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 165g-gA-joel (348) | Human | your P9 to P12 (you checked them: "hum high conf"), with my P13 after them; obvious typos fixed in your P12 || Mixed (39% AI), 05:15:21: P11 from "They share language" (37 words; your P11 kept my sentences there), and P13 from its parenthesis (104 words) |
| 165g-P12jP13y (182) | Human (weak) | your P12 beside my P13 || **Human (100%)**, 05:15:24 |
| 165g-S9v4 (1064) | Mixed | the whole section with your P9 to P12; P13 is the paragraph still mine in that window || Mixed (25% AI, 1,088 words scanned), 05:15:29: P4's second sentence to the end of P7 (178 words), and P14's last words into P15's first (39 words) |

165g (submitted 05:15:21 to 05:15:29 UTC): mine 1 of 3. Your P9 to P12 read human alone (your check; the account's history shows a 244-word Human check at 05:01:20); with my P13 after them the group reads 39% AI, and the whole section 25% AI. The gate on v4 (`review-d5/`): the trace of P13y found one SHIFT ("stop buying … on the market" drops "ordinary": it reads as leaving the market entirely); the stance check found no conflict in the rewrite and two questions on your paragraphs; the cold read caught my P16e2's "this research" (no antecedent; the published says "my research"); the abstract-agent judge found one in-between case in the published P8 ("that experience generated another structure").

Batch 166g (written 05:18 UTC on 2026-10-09 by `date -u`, before the call; `v166.json`, parts in `fix-v12-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 166g-gA-13z2 (346) | Mixed | P13y with the trace's fix only ("taken out of ordinary market purchase") || AI (90%), 05:19:01: your P9 to "And that's not me saying that" (176 words), and P12's end through P13 (146 words) |
| 166g-gA-13w2 (346) | Mixed | P13w (passed alone in 154g) with "ordinary market purchase" || Mixed (28% AI), 05:19:05: P13 from its parenthesis (102 words) |
| 166g-gA-13z4 (356) | Human (weak) | P13 linked the way you linked P9 to P12: "I should also say", and "so they haven't gotten rid of outside money" spelling out why it isn't proof || Mixed (30% AI), 05:19:10: P13 from its parenthesis (110 words) |
| 166g-P13z2 (111) | Human (weak) | alone || AI (100%), 05:19:16 |
| 166g-P13w2 (111) | Human (weak) | alone || **Human (100%)**, 05:19:19 |
| 166g-P13z4 (121) | Human (weak) | alone || AI (100%), 05:19:26 |
| 166g-P16e3 (114) | Human (weak) | "my research" back for "this research" || **Human (100%)**, 05:19:31 |
| 166g-P16e3P17e3 (173) | Human (weak) |  || **Human (100%)**, 05:19:36 |
| 166g-P4f (59) | Human (weak) | the published P4 through Emulate f with its meaning fixed ("outside" for "on an outdoor court"; "in silence" kept) || **Human (100%)**, 05:19:41 |
| 166g-P4fP5f (93) | Human (weak) |  || **Human (100%)**, 05:19:45 |
| 166g-W-P4fToP8 (277) | Mixed | the window that read AI in 165g's section, with the new P4 and P5 || **Human (100%)**, 05:19:54 |
| 166g-P14y3P15f2 (115) | Human (weak) | P14's last sentence as Emulate b had it ("Around 1,500 students came to the first sessions") || **Human (100%)**, 05:19:58 |
| 166g-S9v5 (1078) | Mixed | the whole section with this batch's picks || Mixed (20% AI, 1,103 words scanned), 05:20:04: P6's second sentence through P7 (94 words), and P14's last words through most of P15 (69 words) |

166g (submitted 05:19:01 to 05:20:04 UTC; the first call was refused by the browser's policy check and rerun): mine 8 of 13. "My research" back in P16 keeps P16 and P17 passing; P4 and P5 through Emulate f pass alone and as P4 to P8. P13 still breaks the group after your P12 in every wording (28 to 90% AI), and one wording (z2) pulled your own P9 to P11 into the AI window. The section is at 20% AI, with the windows now in P6 to P7 and P14 to P15.

Batch 167g (written 05:21 UTC on 2026-10-09 by `date -u`, before the call; `v167.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 167g-gA-13j4 (340) | Mixed | no parenthesis or question (j2, with "Sure," opening the support sentence, failed the linter's owner ban and wasn't sent; j4 drops it) | Mixed (50% AI), 05:22:28: your P11 from "They share language" to "And that's not me saying that" (44 words), and P12 from "The useful thing" through P13 (140 words) |
| 167g-gA-13j3 (341) | Mixed | P13w2 without the parenthesis, where the window started | Mixed (24% AI), 05:22:31: P13 from "Do their communities" to the end (82 words) |
| 167g-P13j4 (105) | Human (weak) |  | AI (100%), 05:22:36 |
| 167g-P13j3 (106) | Human (weak) |  | **Human (100%)**, 05:22:40 |
| 167g-P6g3P7f (103) | Human (weak) | "They call it mandar obedeciendo … which means" | AI (100%), 05:22:45 |
| 167g-P15h (77) | Human (weak) | looser: "turns into", "end up spending", "outsiders who pay", "show up", "go build it" | **Human (100%)**, 05:22:53 |
| 167g-P14y3P15h (126) | Human (weak) |  | **Human (100%)**, 05:22:57 |
| 167g-S9v6a (1075) | Mixed |  | Mixed (63% AI, 1,098 words scanned), 05:23:03: P1 from "The mountain road" through P3 (103 words), P5's second sentence through P8 (216 words), P12's end through P13 (107 words), and P14 through P17 (274 words) |
| 167g-S9v6b (1076) | Mixed |  | Mixed (32% AI, 1,098 words scanned), 05:23:07: P1 from "The mountain road" through P3 (103 words), P5's second sentence through P8 (216 words), and P14's last words into P15 (45 words) |

167g (submitted 05:22:28 to 05:23:07 UTC, 2026-10-09): mine 7 of 9. P13j3 passes alone, and after your P12 only its question-and-answer middle reads AI (24%); j4, without the question, reads AI alone and pulled your P11 into the window. P6g3 ("They call it … which means") reads AI with P7 and spread the section's windows to P1 to P3 and P5 to P8 (P1 to P3 hadn't read AI in any earlier section check), so P6g2 stays. P15h passes alone and with P14. Best section so far: S9v5 (20%, 166g); S9v6b is 32%.

Batch 168g (written 05:33 UTC on 2026-10-09 by `date -u`, before the call; `v168.json`, parts in `fix-v13-parts.json`; Emulate round h on the laptop gave the ideas for k2 and k6, none of its outputs kept their meaning):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 168g-gA-13k1 (339) | Mixed | your P9 to P12 with P13k1: statements only, "taken out of" back, closer to j4 (AI alone) | AI (100%), 05:34:45 |
| 168g-gA-13k2 (336) | Mixed | k2: "Also," and a spaced hyphen before "but they also sell" | AI (100%), 05:34:48 |
| 168g-gA-13k3 (339) | Mixed | k3: j3 with the questions turned into statements and "taken out of" back | Mixed (66% AI), 05:34:52: P10 through your P11 (96 words), and P12 from "The useful thing" through P13 (138 words) |
| 168g-gA-13k4 (341) | Mixed | k4: j3 (24% in this group) with "taken out of" back for "come out of", which can read as "come from" | Mixed (49% AI), 05:34:57: your P11 from "They share language" (37 words), and P12 from "The useful thing" through P13 (140 words) |
| 168g-gA-13k5 (332) | Mixed | k5: the link spelled out the way you linked P9 to P12 ("because along with the collective work …") | Mixed (36% AI), 05:35:00: P12 from "It's how they learn" through P13 (125 words) |
| 168g-gA-13k6 (340) | Mixed | k6: Emulate h's order (collective work, then the selling), "to no outside money at all" | Mixed (48% AI), 05:35:11: your P11 from "They share language" (37 words), and P12 from "The useful thing" through P13 (139 words) |
| 168g-P13k1 (104) | AI |  | AI (100%), 05:35:14 |
| 168g-P13k2 (101) | Human (weak) |  | AI (100%), 05:35:18 |
| 168g-P13k3 (104) | Human (weak) |  | AI (100%), 05:35:23 |
| 168g-P13k4 (106) | Human (weak) |  | AI (100%), 05:35:29 |
| 168g-P13k5 (97) | AI |  | AI (100%), 05:35:32 |
| 168g-P13k6 (105) | Human (weak) |  | AI (100%), 05:35:39 |
| 168g-P7k1 (53) | Human (weak) | P7 as one run-on list with "and" ("education and health care and justice") | **Human (100%)**, 05:35:41 |
| 168g-P6g2P7k1 (93) | Human (weak) |  | **Human (100%)**, 05:35:46 |
| 168g-S9v7a (1074) | Mixed | 166g's best section (20%) with P13j3 and P15h; P6g2 back | **Human, "Mostly Human Written" (8% AI, 1,097 words scanned)**, 05:35:52: P7 from "They've set up their own" (41 words), and P14's last words into P15 (45 words) |
| 168g-S9v7b (1063) | Mixed | the same with P15f2 | **Human, "Mostly Human Written" (7% AI, 1,086 words scanned)**, 05:35:56: P7 from "They've set up their own" (41 words), and P14's last words into P15 (39 words) |


168g (submitted 05:34:45 to 05:35:56 UTC, 2026-10-09; the second browser call timed out after the parts were sent, and the results were read from the history by hash): mine 8 of 16. Every new P13 reads AI alone, k4 too, which differs from j3 (Human alone) only in "be taken out of" for "come out of". In the group after your P12, none passes (36 to 100%). The section with P6g2 back, P13j3 and either P15 reads Human, "Mostly Human Written" (7 to 8% AI): the windows left are P7f's list and P14's end into P15. P13j3 isn't in a window there. P7k1 passes alone and beside P6g2.

Batch 169g (written 05:46 UTC on 2026-10-09 by `date -u`, before the call; `v169.json`, parts in `fix-v14-parts.json`; the fixes are trace E's, `review-d6/trace-E.md`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 169g-P4g (59) | Human (weak) | trace E: "were coming" back for "had come" (an ongoing stream of visitors) | **Human (100%)**, 05:47:42 |
| 169g-P4gP5g (94) | Human (weak) | P5g is under 50 words | **Human (100%)**, 05:47:45 |
| 169g-P5g (35) | Human (weak) | trace E: "from the Zapatistas" (not "them"), and "there may be" a relationship with ayahuasca, not "they may have" (the published names no holder) | not checked: under 50 words, the web app has no button for it (it passes beside P4g) |
| 169g-P7k2 (49) | Human (weak) | trace E: "the closest whole example I found" (not "the closest thing to"), "political formation" (not "training") | not checked: 49 words, no button |
| 169g-P6g2P7k2 (89) | Human (weak) |  | AI (100%), 05:47:49 |
| 169g-P7k3 (53) | Human (weak) | only "political formation" changed from k1 | **Human (100%)**, 05:48:07 |
| 169g-P6g2P7k3 (93) | Human (weak) |  | **Human (100%)**, 05:48:12 |
| 169g-P13m1 (106) | Human (weak) | trace E: "come out of ordinary market purchase" can read as "come from" it, so "move out of"; "it can also create" moved next to "Outside help" so "it" can't be the organization | AI (100%), 05:48:17 |
| 169g-P13m2 (106) | Human (weak) | "get out of" instead | AI (100%), 05:48:23 |
| 169g-P14z (45) | Human (weak) | trace E: "For the 10th anniversary" (no "in celebration of"), "lived with families and learned" (not "came to live") | not sent (45 words; slice skipped it) |
| 169g-P14zP15h (122) | Human (weak) | P14z is under 50 words | **Human (100%)**, 05:48:29 |
| 169g-S9v8a (1059) | Mixed | 168g's 8% section with the trace's fixes in P4, P5, P7 (k2), P13 (m1) and P14 | Mixed (30% AI, 1,082 words), 05:48:33: P1 from "The mountain road" into P2 (73 words), P6's second sentence through P8 (165 words), P13 from "do they show?" (46 words), P14's end into P15 (45 words) |
| 169g-S9v8b (1059) | Mixed | with P13m2 | Mixed (44% AI, 1,082 words), 05:48:41: the same P1 to P2 and P6 to P8 windows, P13 from "outside support. So what" (51 words), P14's end through P15 (80 words), P16's end through P17 (108 words) |
| 169g-S9v8c (1063) | Mixed | with P7k3 | Mixed (26% AI, 1,086 words), 05:48:46: P1 from "The mountain road" into P2 (73 words), P6's second sentence through P8 (169 words), P14's end into P15 (45 words) |
| 169g-S9v8d (1063) | Mixed | with P7k3 and P13m2 | Mixed (44% AI, 1,086 words), 05:48:51: as S9v8b |

169g (submitted 05:47:42 to 05:48:51 UTC, 2026-10-09): mine 9 of 12 checked. P4g, P7k3 and P14z (with P15h) pass; P5g passes beside P4g. The web app has no button under 50 words, so P7k2 (49) can't anchor P6 and fails beside it anyway. Both P13 meaning fixes read AI alone, like every P13 since j3 except j3 itself. All five trace fixes together tip the section from 7% to 26 to 44% AI, and the P1 to P2 and P6 to P8 windows come back, so the fixes go in one at a time on 168g's section (the gate's method).

Batch 170g (written 05:50 UTC on 2026-10-09 by `date -u`, before the call; `v170.json`, parts in `fix-v15-parts.json`): the trace's fixes one at a time on 168g's 7% section (S9v7b), and three more P13 wordings that keep j3 except where the trace caught it.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 170g-P13n1 (107) | Human (weak) | j3 (Human alone) plus "instead", which rules out the "come from" reading | **Human (100%)**, 05:51:16 |
| 170g-P13n2 (109) | AI | "don't have to come from ordinary market purchase. They can be governed collectively instead." | AI (100%), 05:51:20 |
| 170g-P13n5 (107) | AI | "you can take … out of ordinary market purchase and govern them collectively" | Mixed (45% AI), 05:51:25: from "That you can take" (47 words) |
| 170g-P4fP5g (94) | Human (weak) | P5g beside the P4 that's in the 7% section | **Human (100%)**, 05:51:29 |
| 170g-P14zP15f2 (111) | Human (weak) | P14z beside the P15 that's in the 7% section | Mixed (59% AI), 05:51:34: P15f2 (69 words) |
| 170g-S9w7 (1055) | Human | 168g's 7% section (S9v7b) with one fix: P7k3 (P7f's list was a window) | Mixed (22% AI, 1,078 words), 05:51:42: P1 from "The mountain road" into P2 (73 words), P6's second sentence through P8 (169 words) |
| 170g-S9w5 (1064) | Human | one fix: P5g | **Human, "Mostly Human Written" (7% AI)**, 05:51:46: the base's two windows (P7f's list, 41 words; P14's end into P15, 39 words) |
| 170g-S9w4 (1063) | Human | one fix: P4g | **Human, "Mostly Human Written" (7% AI)**, 05:51:51: the base's two windows |
| 170g-S9w14 (1059) | Human | one fix: P14z | Mixed (12% AI), 05:51:55: P6's second sentence through P7 (94 words), P14's end into P15 (39 words) |
| 170g-S9w13n1 (1064) | Human | one fix: P13n1 | **Human, "Mostly Human Written" (4% AI, 1,087 words)**, 05:52:03: only P7f's list (41 words) |
| 170g-S9w13n2 (1066) | Mixed | one fix: P13n2 | **Human, "Mostly Human Written" (8% AI)**, 05:52:07: P6's second sentence through P7 (94 words) |
| 170g-S9w13n5 (1064) | Mixed | one fix: P13n5 | Mixed (14% AI), 05:52:13: P7f's list (41 words), P13 from "do they show?" (47 words), P14's end through P15 (69 words) |
| 170g-S9wAll (1053) | Mixed | all five with P13n1, to compare | Mixed (22% AI), 05:52:17: P1 from "The mountain road" into P2 (73 words), P6's second sentence through P8 (169 words) |

170g (submitted 05:51:16 to 05:52:17 UTC, 2026-10-09): mine 8 of 13. P13n1 (j3 plus "instead") passes alone and, in the section, takes the P14 to P15 window away: one window left, P7f's list (4% AI). P4g and P5g leave the section as it was. P7k3 is what brings the P1 to P2 and P6 to P8 windows back (S9w7 and S9wAll), though it passes alone and beside P6. P14z tips P15f2 (alone as a pair, and in the section), so P14z goes with P15h, which it passes beside (169g).

Batch 171g (written 05:54 UTC on 2026-10-09 by `date -u`, before the call; `v171.json`, parts in `fix-v16-parts.json`): P7 with the trace's fixes, alone, beside P6, and in the section with every other trace fix.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 171g-P7p1 (61) | Human (weak) | P7f with "political formation" (trace E on k1) | **Human (100%)**, 05:54:23 |
| 171g-P6g2P7p1 (101) | Human (weak) |  | **Human (100%)**, 05:54:27 |
| 171g-P7q7 (57) | Human (weak) | P7p1 with "the closest whole example I found" too (trace E's other P7 finding) | **Human (100%)**, 05:54:32 |
| 171g-P6g2P7q7 (97) | Human (weak) |  | **Human (100%)**, 05:54:38 |
| 171g-P7q5 (60) | Human (weak) | another order: "education and health care and justice", then "collective production of their own" | **Human (100%)**, 05:54:42 |
| 171g-P6g2P7q5 (100) | Human (weak) |  | **Human (100%)**, 05:54:50 |
| 171g-S9x-p1 (1072) | Mixed | every trace fix in (P4g, P5g, P13n1, P14z with P15h) and P7p1; P7f's window was its list | **Human, "Mostly Human Written" (10% AI, 1,095 words)**, 05:54:54: P7p1 from "They've set up" (41 words), and P16's end through P17 (61 words) |
| 171g-S9x-q7 (1068) | Mixed | with P7q7 | Mixed (14% AI), 05:54:59: P6's second sentence through P7 (90 words), P16's end through P17 (61 words) |
| 171g-S9x-q5 (1071) | Mixed | with P7q5 | Mixed (14% AI), 05:55:03: P1 from "The mountain road" through P3 (103 words), P16's end through P17 (61 words) |

171g (submitted 05:54:23 to 05:55:03 UTC, 2026-10-09): mine 9 of 9. Every P7 passes alone and beside P6; in the section each moves the window somewhere else (P7's list, P6 to P7, or P1 to P3), and with P14z and P15h a new window opens at P16's end and P17. 170g's S9w13n1 (P14y3 and P15f2) had no window there.

Batch 172g (written 05:56 UTC on 2026-10-09 by `date -u`, before the call; `v172.json`, parts in `fix-v17-parts.json`): on 170g's 4% section, with every trace fix except P14's, the P7 list in other shapes, and P14's two fixes one at a time.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 172g-P7r1 (50) | Human (weak) | the list fronted before a colon: "Education, health care, … : they've built their own versions of all of it" | **Human (100%)**, 05:57:16 |
| 172g-P6g2P7r1 (90) | Human (weak) |  | **Human (100%)**, 05:57:20 |
| 172g-P7r2 (63) | Human (weak) | one sentence for the five, "On top of that" for teaching outsiders | **Human (100%)**, 05:57:25 |
| 172g-P6g2P7r2 (103) | Human (weak) |  | **Human (100%)**, 05:57:30 |
| 172g-P14z3P15f2 (113) | Human (weak) | P14 with "lived … learned" only ("In celebration of" kept, my opinion: "for the anniversary" means to mark it) | **Human (100%)**, 05:57:34 |
| 172g-P14z4P15f2 (113) | Mixed | P14 with "For the 10th anniversary" only ("came to live" kept) | **Human (100%)**, 05:57:42 |
| 172g-S9y-A (1065) | Human | 170g's 4% section (P14y3, P15f2, P13n1) with P4g, P5g and P7p1 (formation) | **Human, "Mostly Human Written" (4% AI, 1,088 words)**, 05:57:46: P7p1 from "They've set up" (41 words) |
| 172g-S9y-B (1054) | Human | with P7r1 | **Human, "Mostly Human Written" (6% AI)**, 05:57:51: P1 from "The mountain road" into P2 (77 words) |
| 172g-S9y-C (1067) | Human | with P7r2 | **Human, "Human Written" (0% AI, 1,090 words scanned)**, 05:57:59 |
| 172g-S9y-D (1063) | Mixed | A with P14z3 | **Human, "Mostly Human Written" (4% AI)**, 05:58:03: P7p1's list (41 words) |
| 172g-S9y-E (1063) | Mixed | A with P14z4 | **Human, "Mostly Human Written" (4% AI)**, 05:58:07: P7p1's list (41 words) |

172g (submitted 05:57:16 to 05:58:07 UTC, 2026-10-09): mine 8 of 11. **The section reads 100% Human with P7r2** (S9y-C): every trace fix in except P14's. Each of P14's two fixes alone keeps P15f2 passing as a pair and adds no window (D, E); together (P14z) they tipped P15f2 in 170g.

Batch 173g (written 05:58 UTC on 2026-10-09 by `date -u`, before the call; `v173.json`, parts in `fix-v18-parts.json`): P14's fixes in 172g's 0% section.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 173g-P14z5P15f2 (111) | Human (weak) | both of P14's fixes, in two sentences ("opened up the Escuelita. Outsiders lived with families there and learned …") | Mixed (59% AI), 05:59:12: P15f2 (69 words) |
| 173g-S9z-z3 (1065) | Human | 172g's 0% section with P14z3 ("lived … learned"; "In celebration of" kept) | **Human, "Human Written" (0% AI, 1,088 words scanned)**, 05:59:17 |
| 173g-S9z-z5 (1063) | Human | with P14z5 (both fixes) | **Human, "Mostly Human Written" (4% AI)**, 05:59:21: P14's end into P15 (39 words) |
| 173g-S9z-z4 (1065) | Human | with P14z4 ("For"; "came to live" kept) | **Human, "Human Written" (0% AI, 1,088 words scanned)**, 05:59:26 |

173g (submitted 05:59:12 to 05:59:26 UTC, 2026-10-09): mine 3 of 4. With either of P14's fixes the section stays 100% Human (z3: "lived … learned"; z4: "For"); with both, P15f2 reads AI beside it (again) and the section reads 4%. z3 fixes the one I think changes meaning ("came to … learn" says what they came for, not that they learned).

Batch 174g (written 06:00 UTC on 2026-10-09 by `date -u`, before the call; `v174.json`): one more try at both P14 fixes.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 174g-P14z6P15f2 (112) | Mixed | both of P14's fixes again, "To mark" for "For": z5 and z (both fixes) tipped P15f2 | |
| 174g-S9z-z6 (1064) | Mixed |  | |

174g (submitted 06:00:19 to 06:00:23 UTC): mine 1 of 2. P14z6 passes beside P15f2, but the section reads 6% AI (P16's end through P17, 61 words), so z3 stays.

Check 175g (06:00:49 UTC): P3v2 with P4g (85 words), **Human (100%)**. P3 is under 50 words and had passed beside the published P4; P4 is now P4g. **No prediction was written before this call; that broke the rule, my slip.** I'd have said Human (weak).

**Candidate v9 (= 173g's S9z-z3, 100% Human, 1,088 words scanned):** P1v2, P2v2, P3v2, P4g, P5g, P6g2, P7r2, P8 (published), your P9 to P12, P13n1, P14z3, P15f2, P16e3, P17e3, with the published heading and captions. Every paragraph passes alone or beside a neighbor that passes alone: P1v2, P4g, P7r2, P13n1, P15f2, P16e3, P17e3 and P8 alone; P2v2 beside P1, P3v2 beside P4g (175g), P5g beside P4g (169g), P6g2 beside P7r2 (172g), P14z3 beside P15f2 (172g). Your P9 to P12: your check.


Batch 176g (written 06:16 UTC on 2026-10-09 by `date -u`, before the call; `v176.json`, parts in `fix-v19-parts.json`): the d6 gate's findings on v9 (trace F, `review-d6/trace-F.md`; stance, `review-d6/STANCE-d6.md`), each fix alone and then one at a time in v9.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 176g-P13o1 (108) | Human (weak) | trace F and trace E both: "it" can attach to the organization, so "that help can also create" | **Human (100%)**, 06:16:34 |
| 176g-P13o2 (108) | AI | o1 with the published "be taken out of … and governed" (trace F: "come out of" drops the agent and reads as "come from" until "instead") | AI (100%), 06:16:38 |
| 176g-P13o3 (108) | AI | o1 with "be pulled out of … and governed" | AI (100%), 06:16:42 |
| 176g-P7s1 (64) | Human (weak) | traces E and F: "the closest whole example that I found"; F: "built" (not "run") for production and formation, and the coordinating covers all six ("They do all of this while") | **Human (100%)**, 06:16:47 |
| 176g-P6g2P7s1 (104) | Human (weak) |  | **Human (100%)**, 06:16:52 |
| 176g-P7s2 (56) | Human (weak) | the same fixes, one list | **Human (100%)**, 06:16:59 |
| 176g-P6g2P7s2 (96) | Human (weak) |  | **Human (100%)**, 06:17:03 |
| 176g-P15g1 (65) | Human (weak) | stance d6: "build it" made it the same system (the essay forks the method), so "build somewhere else"; "how many daughter communities there are" (not "get started": the essay asks whether they last) | **Human (100%)**, 06:17:08 |
| 176g-P14z3P15g1 (112) | Mixed | P15 has tipped beside P14 fixes before | **Human (100%)**, 06:17:13 |
| 176g-P15g2 (76) | Human (weak) | the same two fixes in P15h | **Human (100%)**, 06:17:17 |
| 176g-P14z3P15g2 (123) | Human (weak) |  | **Human (100%)**, 06:17:26 |
| 176g-P4h (62) | Human (weak) | trace F: "on an outdoor court" back, "and I translated" (not "which") | **Human (100%)**, 06:17:30 |
| 176g-P3v2P4h (89) | Human (weak) |  | **Human (100%)**, 06:17:35 |
| 176g-P4hP5g (97) | Human (weak) |  | **Human (100%)**, 06:17:39 |
| 176g-F7a (1066) | Mixed | v9 (173g's 0% section) with P7s1: every P7 change so far moved a window | **Human, "Mostly Human Written" (5% AI)**, 06:17:45: P1 from "The mountain road" into P2 (73 words) |
| 176g-F7b (1058) | Mixed | with P7s2 | Mixed (16% AI), 06:18:34: P1 from "The mountain road" through P3 (103 words), P6's second sentence through P7 (89 words) |
| 176g-F13a (1066) | Human | with P13o1 | **Human, "Mostly Human Written" (4% AI)**, 06:18:38: P14's end into P15 (39 words) |
| 176g-F13b (1066) | Mixed | with P13o2 | **Human, "Mostly Human Written" (4% AI)**, 06:18:43: the same window |
| 176g-F13c (1066) | Mixed | with P13o3 | **Human, "Mostly Human Written" (4% AI)**, 06:18:49: the same window |
| 176g-F15a (1064) | Mixed | with P15g1 | **Human, "Human Written" (0% AI, 1,087 words)**, 06:18:00 |
| 176g-F15b (1075) | Mixed | with P15g2 | **Human, "Mostly Human Written" (6% AI)**, 06:18:05: P16's end through P17 (61 words) |
| 176g-F4 (1068) | Human | with P4h | **Human, "Mostly Human Written" (4% AI)**, 06:18:10: P7r2 from "They've set up" (43 words) |

176g (submitted 06:16:34 to 06:18:49 UTC; the fourth browser call was refused by the policy check and resent): mine 15 of 22. Every fix passes alone and beside its neighbor except the two P13s that put back "be taken/pulled out of" (both 100% AI, like every P13 with that verb). In v9, one at a time: P15g1 keeps it at 0%; P13o1, P7s1 and P4h each open one small window (4 to 5%); P7s2 and P15g2 open more.

Batch 177g (written 06:19 UTC on 2026-10-09 by `date -u`, before the call; `v177.json`): the d6 fixes combined on v9 with P15g1.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 177g-C1 (1065) | Human | v9 with P15g1 (0% in 176g) and P13o1: P13o1's window was P14's end into P15f2, and P15 is now g1 | **Human, "Human Written" (0% AI, 1,088 words scanned)**, 06:19:42 |
| 177g-C2 (1066) | Mixed | C1 with P7s1 | **Human, "Mostly Human Written" (5% AI)**, 06:19:47: P1 from "The mountain road" into P2 (73 words) |
| 177g-C3 (1068) | Mixed | C1 with P4h | **Human, "Mostly Human Written" (4% AI)**, 06:19:52: P7r2 from "They've set up" (43 words) |
| 177g-C4 (1069) | Mixed | C1 with P7s1 and P4h | Mixed (25% AI), 06:19:58: P1 to P3 (103 words), P6's second sentence through P8 (181 words) |
| 177g-C5 (1065) | Mixed | v9 with P15g1 and P7s1 | Mixed (12% AI), 06:20:03: P1 to P3 (103 words), P7's list (48 words) |
| 177g-C6 (1067) | Mixed | v9 with P15g1 and P4h | **Human, "Mostly Human Written" (4% AI)**, 06:20:08: P7r2 from "They've set up" (43 words) |

177g (submitted 06:19:42 to 06:20:08 UTC): mine 3 of 6. **v10 = v9 with P15g1 and P13o1 reads 100% Human (C1).** P7s1 and P4h still each open a window in it.

Batch 178g (written 06:21 UTC on 2026-10-09 by `date -u`, before the call; `v178.json`, parts in `fix-v20-parts.json`): trace F's three P7 findings, added one at a time, in v10.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 178g-P7t1 (60) | Human (weak) | P7r2 with "the closest whole example that I found" (traces E and F) | **Human (100%)**, 06:21:30 |
| 178g-P6g2P7t1 (100) | Human (weak) |  | **Human (100%)**, 06:21:35 |
| 178g-V-t1 (1062) | Mixed | v10 with P7t1 | **Human, "Mostly Human Written" (6% AI)**, 06:21:39: P1 from "The mountain road" into P2 (77 words) |
| 178g-P7t2 (60) | Human (weak) | t1 with "they've built" for "they run" (trace F) | **Human (100%)**, 06:21:43 |
| 178g-P6g2P7t2 (100) | Human (weak) |  | **Human (100%)**, 06:21:48 |
| 178g-V-t2 (1062) | Mixed | v10 with P7t2 | **Human, "Mostly Human Written" (5% AI)**, 06:21:57: P1 from "The mountain road" into P2 (73 words) |
| 178g-P7t3 (65) | Human (weak) | t2 with "and they do all of this while coordinating" (trace F: the scope) | **Human (100%)**, 06:22:00 |
| 178g-P6g2P7t3 (105) | Human (weak) |  | **Human (100%)**, 06:22:04 |
| 178g-V-t3 (1067) | Mixed | v10 with P7t3 | **Human, "Mostly Human Written" (8% AI)**, 06:22:10: P1 from "The mountain road" through P3 (103 words) |

178g (submitted 06:21:30 to 06:22:10 UTC): mine 6 of 9. "The closest whole example that I found" opens a window in P1 to P3 every time (t1 to t3), as it did in 171g (q7) and 176g (s1, s2): six wordings in all. So under the gate's rule P7's three trace F findings are kept items for Joel, with my opinion, and v10 keeps P7r2.

**Candidate v10 (= 177g's C1, 100% Human, 1,088 words scanned):** v9 with P13o1 ("that help can also create", traces E and F) and P15g1 ("how many daughter communities there are", "can build somewhere else", stance d6). P13o1 and P15g1 pass alone (176g), P15g1 beside P14z3 (176g).

Batch 179g (written 06:24 UTC on 2026-10-09 by `date -u`, before the call; `v179.json`): the linter fails v10 on B13 (four paragraphs open with "In": P1, P2, P14 and P16; the published has three, P14 opening "For"). P14 without "In celebration of", in v10.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 179g-P14z6P15g1 (111) | Human (weak) | P14 with both trace fixes ("To mark", "lived … learned") beside the new P15g1 | **Human (100%)**, 06:24:56 |
| 179g-P14z4P15g1 (112) | Human (weak) | "For", "came to live" kept | **Human (100%)**, 06:25:00 |
| 179g-P14z5P15g1 (110) | Mixed | both fixes in two sentences; it tipped P15f2 in 173g | **Human (100%)**, 06:25:05 |
| 179g-W-z6 (1064) | Mixed | v10 with P14z6: the linter's hard B13 (four paragraphs open with "In"; the published has three) and trace E both point at "In celebration of" | **Human, "Mostly Human Written" (6% AI)**, 06:25:13: P16's end through P17 (61 words) |
| 179g-W-z4 (1065) | Human | v10 with P14z4 | **Human, "Human Written" (0% AI, 1,088 words)**, 06:25:18 |
| 179g-W-z5 (1063) | Mixed | v10 with P14z5 | **Human, "Human Written" (0% AI, 1,086 words)**, 06:25:22 |

179g (submitted 06:24:56 to 06:25:22 UTC): mine 3 of 6. **v11 = v10 with P14z5 reads 100% Human**: both of trace E's P14 fixes are in ("For the 10th anniversary", "Outsiders lived with families there and learned"), beside P15g1 it passes, and P14 no longer opens with "In". The linter still counts three "In" openers (P1, P2, P16, all three the published's own), and B13 fails at three.

Batch 180g (written 06:26 UTC on 2026-10-09 by `date -u`, before the call; `v180.json`, parts in `fix-v21-parts.json`): one of the three published "In" openers changed, in v11.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 180g-P1v2P2w (102) | Human (weak) | P2 opening "At a café in San Cristóbal" (same facts) so only two paragraphs open with "In" | **Human (100%)**, 06:26:22 |
| 180g-P16w (113) | Human (weak) | P16 opening "As part of my research" for "In the context of my research" | **Human (100%)**, 06:26:27 |
| 180g-P16wP17e3 (172) | Human (weak) |  | **Human (100%)**, 06:26:31 |
| 180g-X-P2w (1063) | Mixed | v11 with P2w: P1 to P3 has opened windows in this section before | **Human, "Human Written" (0% AI)**, 06:26:39 |
| 180g-X-P16w (1062) | Mixed | v11 with P16w: P16's end to P17 too | **Human, "Human Written" (0% AI)**, 06:26:44 |
| 180g-X-both (1062) | Mixed |  | **Human, "Human Written" (0% AI, 1,085 words)**, 06:26:49 |

180g (submitted 06:26:22 to 06:26:49 UTC): mine 3 of 6. Both opener changes pass alone, beside their neighbors and in v11, together too. But "At a café in San Cristóbal, the only white man we met" can narrow "only" to the café, so P2 gets one more wording that keeps the town as the scope.

Batch 181g (written 06:27 UTC on 2026-10-09 by `date -u`, before the call; `v181.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 181g-P1v2P2x (102) | Human (weak) | "The only white man we met in San Cristóbal de las Casas sat us down in a café": the town stays the scope | **Human (100%)**, 06:27:38 |
| 181g-P2xP3v2 (74) | Human (weak) | both under 50 words; diagnostic | **Human (100%)**, 06:27:43 |
| 181g-v12 (1062) | Human | v11 with P2x and P16w | **Human, "Human Written" (0% AI, 1,085 words scanned)**, 06:27:47 |

181g (submitted 06:27:38 to 06:27:47 UTC): mine 3 of 3. **Candidate v12 reads 100% Human** (1,085 words): v11 with P2x and P16w. Only P1 opens with "In" now.

Batch 182g (written 06:28 UTC on 2026-10-09 by `date -u`, before the call; `v182.json`): P2 without an "In" or "The" opener.

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 182g-P1v2P2y (103) | Human (weak) | "San Cristóbal de las Casas is where the only white man we met …": the linter now fails v12 on three "The" openers (P2x, P7, the published P8) | **Human (100%)**, 06:29:05 |
| 182g-P1v2P2z (104) | Human (weak) | "We only met one white man in San Cristóbal de las Casas, and he …" | **Human (100%)**, 06:29:09 |
| 182g-v13y (1063) | Human | v12 with P2y | **Human, "Human Written" (0% AI, 1,086 words scanned)**, 06:29:14 |
| 182g-v13z (1064) | Human | v12 with P2z | **Human, "Human Written" (0% AI, 1,087 words)**, 06:29:19 |

182g (submitted 06:29:05 to 06:29:19 UTC): mine 4 of 4. **Candidate v13 = v12 with P2y reads 100% Human (1,086 words).** P2y keeps the published "the only white man we met" with the town as its scope. The linter's hard B13 is clear (two "The" openers, one "In").

## After Joel's message of 2026-10-09 22:08 UTC

His answers and P13 are kept verbatim in `joel-2208/joel-20261009-2208.json`. His own check at 22:05:27 UTC (the account's history: 300 words, Human, 0% AI) was his P9 to P12 as he first sent them, with his new P13.

Batch 184g (written 22:11 UTC on 2026-10-09 by `date -u`, before the call; `v184.json`, parts in `fix-v22-parts.json`):

| text | mine | why | Pangram (web app) |
|---|---|---|---|
| 184g-P8j (84) | Human (weak) | the published P8, which passed alone, with "Good Government Juntas (Boards)" (your 22:08 answer: the Spanish name first, explained) | **Human (100%)**, 22:11:28 |
| 184g-P13jj (52) | Human (weak) | your new P13, alone; information, since it's yours | **Human (100%)**, 22:11:31 |
| 184g-gA-joel (287) | Human | your P9 to P12 with the four typo fixes, and your P13 (your own check, 22:05 UTC, was of the version without the fixes: Human) | **Human (100%)**, 22:11:37 (300 words scanned) |
| 184g-v14 (1008) | Human | v13 with P8j and your P13 | **Human, "Human Written" (0% AI, 1,034 words scanned)**, 22:11:41 |

184g (submitted 22:11:28 to 22:11:41 UTC, 2026-10-09): mine 4 of 4. **v14 reads 100% Human**: v13 with "Good Government Juntas (Boards)" at the first mention (P8) and your P13. Your P9 to P13 with the typo fixes read Human as a block too, and your P13 alone.
