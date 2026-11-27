# Romance current state

Updated: 2026-11-27

## Goal

Joel, 2026-11-07 13:13 UTC: "start working on fixing the romance article, pangram 4.1 found some ai spans". The live post
reads Human in Pangram 4.1, with no AI window and no Low, its argument, memories and locks kept; then his post is updated,
with his OK and no email.

## Authority / baseline

- The live post as his extension read it on 2026-11-05: [Romance Advice I Wish My Parents Taught Me](https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents)
  ("Updated Aug 27, 2026"), [Mostly Human Written](https://www.pangram.com/feed/9e40aa8f-317c-4490-893d-9e99c839de88),
  4.2% AI, document confidence Medium: 741 words in AI windows over 21 spots (170 High, 169 Medium, 402 Low) and 911 words
  Human Low (`humanize/fix-20261107/live-check/`).
- `master.md` (2026-08-24) is not the live post: 125 of the live post's 355 lines differ (his update of 27 August among
  them). The live text was not copied into the repository whole; each paragraph being fixed is in its check text.
- `OWNER-LOCKS.json` still applies (protected functions). Its Two Pillars lock text differs from the live post's version
  of that paragraph ("without much outside support"), so the live post is his later word there; nothing is changed in it.

## Completed

- 2026-11-07: the live post's result recorded; the romance lane added to `tools/humanization/pangram_lanes.json` with its
  ledger `humanize/pangram-ledger.jsonl`.
- 2026-11-07: first tries at 13 of the 21 spots (`humanize/fix-20261107/r01/`, `r02/`), each paragraph checked in the web
  app with its making-sense receipt. Human in its own check: S1 the casual-sex turn (#1), S3 the support paragraph's
  summary cut (#3), S4 the provider question (#4), S5 Bee's shoes (#5), S9 the bed line (#10, its line Low), S12 the
  patient paragraphs (#13), S13 teacher and student (#14).
- 2026-11-07 (13:39 UTC pickup): tell panels on S2, S7, S10, S11, S17 and S21 (`humanize/fix-20261107/r03/panel-s2/`,
  `r04/panel-*`, `r05/panel-*`); second and later tries at S2, S6 to S11, and first tries at S14 to S21 (`r03/`, `r04/`,
  `r05/`). Human in their own checks, no Low: S6 bundling (#30), S8 idealization (#18), S11 her as Mom (#37), S14
  polarity inside the safety (#21), S15 proving I'm the man (#31), S16 the fantasy lines (#23), S18 the backup system
  (#25), S19 the confidants' side of the story (#32), S20 the agreement questions (#27).
- 2026-11-07 (14:27 UTC pickup): four sections checked whole with the best tries in them (`humanize/fix-20261107/r06/`):
  S10 alone time read Human (High) in its section (#44), so it is done. The post's last 2,871 words, which his extension
  never read, checked as they stand (#47): Mostly Human, 4.8% AI, with a new spot, S22, and 8 Human Low windows. The live
  post's 54 Human Low windows saved (`live-check/LOW-WINDOWS.json`): 19 already rechecked by a fix, 35 (673 words) open.
- 2026-11-07 (14:49 UTC pickup): S22's first try inside "After leaving" (#50, `humanize/fix-20261107/r08/`): one
  sentence fixed, the rest still AI. The marking page for S2 and S17 published
  ([the page](https://claude.ai/artifact/CMRNDtBm4bBRB3741geGoY), its cards in `review/teach-20261107/REVIEW-T1.md`).
  The first Low-window section, "Holding up a leaky dam" (#51, `r09/`): its short sentences joined read Human Medium, but
  the want list joined to its reason read AI Medium.
- 2026-11-07 (15:09 UTC pickup, `humanize/fix-20261107/r10/` to `r12/`): S22's paragraphs checked by themselves
  (#54 to #56), then its section a second time (#62): Human, no AI window left (41% AI in #50), two Human Low windows.
  "Holding up a leaky dam" (#57, #63): Human, one Low window left, on the want list. Three more sections with open
  Low windows read Human with no Low: "My flaws" (#61), "Peeking thru the window" (#67) and "Things get tricky fast"
  (#68). "The window of clarity" (#60, 15% AI) and "Situationships" (#59, 31% AI) narrowed to their paragraphs:
  paragraph 33 (#64) and the oxytocin paragraph (#66) read Human High by themselves, paragraph 34 Human Low (#65).
- 2026-11-07 (15:09 UTC pickup, `r13/`): after one fix each (his answer 28a), S22's section (#69) and "Holding up a
  leaky dam" (#70) read Human with no Low window, and "The window of clarity" read Human with no Low on its second try
  (#71). "Anti-PTSD Can Be Just As Dangerous As PTSD" read Human with no Low on its first (#73). Paragraph 34 of
  "Situationships" still reads Low on his three claims (#72); "Slow & steady" read 34% AI on its five-part list (#74);
  "Disconnect to connect" read Human with four Low windows by itself (#75).
- 2026-11-07 (15:57 UTC pickup, `r14/`, `r15/`): "Disconnect to connect" read Human with no Low on its second try,
  after its paragraphs read High by themselves (#77 to #80, #88). "Muses & Directors" (#81), "The Queen of Orgasms"
  (#82) and "Labels Are Descriptive, Not Prescriptive" (#84) read Human with no Low on their first try. The tell panel
  ran on "Situationships" paragraph 34 (`r14/panel-sit34/`); with its agreed tells fixed the paragraph still read Low
  (#85), and the section read 15% AI on its last try (#86). "Slow & steady" (#87) and "It always goes deeper" (#91,
  with S4 and S5 in) read Human with Low windows; "Jealousy on trial" read 16% AI (#83), then its two pairs read High
  by themselves (#89, #90); "Beware idealization in either direction" (#92, with S8 in) read 9.6% AI.
- 2026-11-07 (16:24 UTC pickup, `r16/`, every try linted first): "Slow & steady" (#96, after one more fix), "It
  always goes deeper" (#97, one High window, with S4 and S5 in) and "Fantasy" (#99, with S16 in) read Human with no
  Low. "Situationships" paragraph 34 read Human with no Low by itself (#95: his fun line left a little unbalanced,
  "without (most of) the responsibility", bad-trips-2026-11-07g). "Jealousy on trial" read 28% AI on its last try
  (#94), "Romance Shouldn't Be Adjudicated" 37% AI on its first (#98), and 147 with 148 37% AI (#93).
- 2026-11-07 (16:41 UTC pickup, `r17/`, every try linted first): "Situationships" read Human with no Low after its
  fix (#100, his answer 28a: paragraph 34 as #95 read, and 36's closing line said once, in its opener). "Some babies
  grow up faster" (#101, with S11 and S12 in), "Different levels in different domains can be complementary" (#102,
  with S13 in) and "Gaslighting in the dark" (#105) read one Human High window each, and "Why all of this sounds
  artificial" (#104) read Human with no Low. "What are you actually choosing together?" (#103, with S20 in) read Human
  with three Low windows, all in S20's questions, which had read High as a pair by themselves (#27).
- 2026-11-07 (17:07 UTC pickup, `r18/`, `r19/`, every try linted first): "What are you actually choosing together?"
  read Human with no Low on its second try (#106: S20's opener joined to its first question with a colon, the either/or
  question left a little unbalanced, the rethink question joined to the split-up one). "The conversation about flaws"
  (#107, with S7 in), "Which marriage vows are honest?" (#110, S21's closing said first, in the verse sentence: the
  verses "make the wedding vow itself look even more suspicious (to me, anyway)") and "What I gained from loss" (#109,
  one High window) read Human with no Low. "From flow to nitty gritty" (S9's line said inside the bed paragraph) read 33%
  AI on 201's closing list (#108); 201 by itself read Human Low with the list re-shaped (#111) and Human High with it cut
  to two items (#112); in the section that sentence still reads Human Low (#113, and #114 after one more fix).
- 2026-11-07 (17:34 UTC pickup, `humanize/fix-20261107/whole/`): the fixed version assembled for the whole-article
  check: the live post with every section's and spot's best tested text in place, 40 changes to 66 paragraphs, each
  aligned with the live post by fingerprints (`whole/CHANGE-MAP.md`). The compare read of every changed paragraph beside
  the live one found 7 small snags, each kept with its reason; the word-for-sense read found its three planted errors and
  nothing else. Its two temporary Substack drafts are made (draft A to "Primal attraction", draft B from there; numbers
  and checked-text hashes in `whole/DRAFTS.json`, links kept out of Git), and each secret link's rendered text matched
  the built text. They aren't sent for the check yet: the ledger's gate (gut-2026-11-07a) holds a whole-article check
  until every window a smaller check read AI reads Human in a later smaller check, and S2, S17, the three S2-pattern
  stretches and three more windows in "Can making love be a spiritual practice?" (#45) still read AI there.
- 2026-11-07 (18:08 UTC pickup, `humanize/fix-20261107/r20/`): "Can making love be a spiritual practice?" narrowed
  (gate gut-2026-11-07a), S17's paragraphs (310, 311) left as the live post has them: 304 to 309 read one Human High
  window (#115: 304's two denials said as one sentence with what the texts do show, 305's stages of awakening named where
  the stream-enterers are listed, 306's short opener joined with a colon), and so did 312 with 313 (#116: 312's point
  said first). The fixed version now has 42 changes to 70 paragraphs; the compare read of the new ones found nothing,
  and their word-for-sense read found its two planted errors and nothing else.
- 2026-11-07 (22:57 UTC pickup, `humanize/fix-20261107/r21/` to `r26/`): his marking-page answers saved
  (`review/teach-20261107/ANSWERS-T1.json`); his S2 and S17 go in as he wrote them, with only "you're attention" made
  "your attention". With them, "Spirituality to bypass intimacy" read one Human High window (#117, 484 words) and "Can
  making love be a spiritual practice?" read one Human High window (#118, 772 words). His lessons are
  `docs/lessons/2026-11-07-2257-romance.md` (romance-2026-11-07a to d). Carried to the S2-pattern stretches: Romance
  285 to 287 read Human, High and Medium, alone (#120) and in its section (#122, no Low); Idealization 147 and 148 read
  Human after a tell panel (#123), and the section reads Mostly Human with no AI window, five Low windows left (#132).
  Jealousy 367 to 369: each new paragraph reads Human alone (#124, #127, #128) and the three read AI together (#119,
  #131) and in the section (#133 26%, #134 31.7% after the links a fresh sense read asked for); they went to him on a
  second marking page (`review/teach-20261107/REVIEW-T2.md`, `ARTIFACT.md`). The fixed version now has 45 changes to 82
  paragraphs (`whole/`); my compare read of the new ones (147, 148, 151, 285 to 287) found one softened point, 148's
  "rewriting the whole past", now carried by "faking it all along", and 285's "cuteness", now carried by "play the
  damsel"; the word-for-sense read of the new paragraphs waits for the jealousy answer, with the whole-article check.

- 2026-11-08 (his message of 15:07 UTC, `humanize/fix-20261107/r27/`): his T2 answer saved
  (`review/teach-20261107/ANSWERS-T2.json`): he rewrote all of Jealousy 366 to 370 ([Human, High, alone](https://www.pangram.com/history/8f1e5924-1921-4136-8815-d09f45d295e5)).
  With three slips fixed (a missing "than", "also ... too", a curly apostrophe) the section read
  [Human, 0% AI, one Medium window on the live 361](https://www.pangram.com/history/d00216d9-49ef-4351-bfd1-df2165ff14da) (#135).
  His correction of S17 ("the couple I really liked as an example"): the section read [one Human High window](https://www.pangram.com/history/2c67fdaa-6753-4d00-8f49-0f66f7d286d5) (#136).
  "Beware idealization": its five Low windows of #132 fixed; 14% AI on the first try (#138), then
  [Human, High and Medium, no Low](https://www.pangram.com/history/1ef0b91c-6a89-4c35-b4b9-c46f1f54276d) (#143), after
  the compare read put 151's ending back to his boundary. Lessons: `docs/lessons/2026-11-08-1507-romance.md`
  (romance-2026-11-08a to c); the sense-read brief now names a doubled word that isn't next to its twin. The fixed
  version (46 changes, 88 paragraphs) has no window a smaller check read AI or Low; drafts A and B were re-pasted and
  their secret links rendered the built text exactly (`whole/DRAFTS.json`). The whole-article check went to him.

- 2026-11-08 (his message of 16:47 UTC): his yes to 366's fix ("they can put it to work.", #137) is in. His
  whole-article check read both halves Human Written (A [0.17% AI](https://www.pangram.com/feed/87029c8c-313d-436c-b885-e76466096da6),
  B [~0%](https://www.pangram.com/feed/5b03d47c-4290-42e5-8693-688418a08a68), document confidence High), with one AI Low
  and seven Low windows (`humanize/fix-20261107/r27/checks/RESULTS-whole-r27.json`). Six of the seven sections they sat
  in now read Human with no Low (`humanize/fix-20261107/r28/`, #144 to #148, #150) and are in the fixed version; "Slow &
  steady" 181 read AI in both my tries (#149, #151) and went to him on the third marking page
  ([the page](https://claude.ai/artifact/CjEzvMG4wFZDxmqrvwjaGC), `review/teach-20261107/REVIEW-T3.md`), with a question
  on the college friend his new 369 retells from Labels. Push access granted; pull request 401 holds both turns' work
  (labelled "hold": this session's auto mode refused a self-merge into main).

- 2026-11-08 (his message of 17:20 UTC, `humanize/fix-20261107/r29/`): his third page's answers in: "Slow & steady"
  as he rewrote it ([one Human High window](https://www.pangram.com/history/e05bf34d-fbdd-454a-a6c3-c7abde583a56), #153),
  and 369 pointing back to the college friend Labels tells (#152, Human, High and one Medium). Lesson romance-2026-11-08d.
  On his ask to see every Medium window, the fourth marking page ([the page](https://claude.ai/artifact/AXKm7ijCpHzVwQ4mQUYi5Q),
  `review/teach-20261108/REVIEW-T4.md`): 62 paragraphs, 70 windows, each with the tells I see and a fresh sense read's
  finding (`review/teach-20261108/sense-t4/`: "traditonal" in 173, "natural" twice in 338).

- 2026-11-22 (his message of 22:24 UTC, `humanize/fix-20261107/r30/`): his Medium-page answers saved word for word
  (`review/teach-20261108/MESSAGE-T4-20261122-2224.md`, `ANSWERS-T4.json`, matched against the page's database item by
  item): 59 versions in as he wrote them (`r30/HIS-T4.json`, laid over the checks' replacements by `whole/build.py`),
  three cards rejected as Pangram bugs (264, 338, 405), eleven obvious slips fixed and listed (`r30/README.md`), and
  his new "Two Pillars" 332 in place of the locked live paragraph (his own decision; `OWNER-LOCKS.json` still holds the
  old master's text, which this lane doesn't edit). His links: "breathwork" to breathwork.u-dont-exist.com, "Systema
  breathing" to his Systema video, the Instagram reel at 149 (live) after its paragraph for the live update. The live
  post's copy of 2026-11-22 is in `humanize/fix-20261107/live-check/LIVE-POST-BLOCKS-20261122.jsonl` (all 457 paragraphs
  match LIVE-INDEX.txt), and the whole fixed article is one file, `humanize/fix-20261107/whole/FIXED.md` (20,927 words).
  The BPD splitting video in the post is the right one (pvN8QgGatew), public and allowed in embeds, and plays in the
  post in the app's browser: where it broke for him is asked in chat. Lessons `docs/lessons/2026-11-22-2224-romance.md`
  (romance-2026-11-22a to e): marking pages show the whole article (suggestion_review.py 1.12), what doesn't make sense
  is fixed or named to him, every section is checked by itself (E307, missed on this article), four new ways in the
  read against his fixes (18 to 21). The fifth page, the whole article with two questions on his own new sentences:
  [the page](https://claude.ai/artifact/DByVjvbstJ9UmFnSsK2dyc), `review/teach-20261122/REVIEW-T5.md` (four questions:
  M-14's "they", M-409's "literally diagnosed", "my first wife, Bee" against Ann, "H.D." against "H."). His "other junk
  like this?": four fresh readers reported 84 passages as bad as the old "Romance Shouldn't Be Adjudicated"; vetted, 11
  are real and 33 partly, clustered in "Slow & steady" to "Different levels in different domains" and in the closing
  advice from "Psychedelic Timing" to "Tough Love"; none of those in his own voice is real (`r30/junk/VETTED.md`). The
  blind test of the lessons (`r30/replay/RESULTS.md`): a fresh writer with them fixed 5 of 14 of his paragraphs his way,
  half-fixed 5, missed 4 (lists of three kept, vague questions kept, details added), so the brief got three more lines
  (lesson romance-2026-11-22f). Pangram: Claude in Chrome wasn't connected and the app's browser pane is signed out of
  Pangram, so none of his 75 links could be read and no check ran (asked in chat).
- 2026-11-22 23:43 to 2026-11-23 UTC (his message: "i signed into pangram in your cloud browser on my main acct", his
  rule to test every lesson blind on the paragraphs he fixed, and his fifth-page answers). His four answers are in
  (`r31/HIS-T5.json`): Q-14 in his own words ("pressuring men into making it look like men know what they want"),
  "literally defined as" (409), "my second wife, Bee" (314), "H." again for H.D. (392). His 75 Pangram links all read
  from his main account (`r30/HIS-CHECKS.txt`); none needed his nobodytobe account. His rule is in `AGENTS.md`
  (lesson romance-2026-11-22h). The blind test, round 1 (`r30/replay/RESULTS.md`): 6 of 14 rewrites read Human High by
  themselves; round 2 with "add nothing" (`r30/replay2/RESULTS.md`): 2 more High (125, 343) and 437 Human with a Medium
  window, so 8 of 14 High over both rounds; the four still short (73, 214, 252 with 253, 346) point to three ways the
  brief didn't say (lesson romance-2026-11-23a), which round 3 tests (`r30/replay3/`). The section pass (E307,
  `r32/`): 93 sections by themselves, 92 Human with 0% AI (72 High in every window, 20 with Medium windows only), all
  in the ledger. The one Mixed section, "The conversation about flaws" (`r33/README.md`): its opener joined and in the
  fixed version (High with the next paragraph); its end left as it stands after three tries read worse than it, the
  tell panel's rule for the next draft (a Codex writer from his laptop) refused by this session's safety check, so it
  goes on the next page (lesson romance-2026-11-23b). Every push this turn was held back by the auto-mode refusal
  below; the work is in the bundle sent in chat.
- 2026-11-23 15:35 UTC (his message: the pushes should merge by the robot; his bundle fetch failed; "i approve codex
  sure"; he added pictures to the post and the splitting video shows again; his fix of "The conversation about flaws").
  The push went through this time (pull request 401, ca6f3eae); taking off its "hold" label so the lane workflow merges
  it was refused by this session's safety check, so he removes the label or merges it. His bundle fetch had run in his
  askrigor clone, which lacks this repository's commits; with the push it isn't needed. His OK for Codex on his laptop
  (the tell panel's reader and its other-family writer) is recorded here. The post now has five more pictures (alt texts
  "if she likes me its a red flag", "brain heart and penis asking what's the plan", "when she understands you because you
  don't understand yourself", "self help for men", "lying to avoid conflict"); its text is unchanged since 2026-11-22
  (`humanize/fix-20261107/live-check/LIVE-POST-BLOCKS-20261123.jsonl`, which the fixed version is now built from, so its
  Markdown has them). His flaws fix is in (`r33/HIS-FLAWS.json`), and the section with it and my opener reads Human High
  (0% AI, one Medium window): every section of the article now reads Human with no Low window. Lesson romance-2026-11-23c
  (a run of questions: order, one plain statement, one frame); round 3 of the blind test runs it on that stretch too.
  Round 3 of the blind test (`r30/replay3/RESULTS.md`, a Sonnet writer after three Opus writers gave no answer): over
  the three rounds 9 of his 14 paragraphs read Human High by themselves from the lessons alone and two more Human with a
  Medium window; 346 (the dilemma question) and the flaws stretch (reported questions) still read AI (lesson
  romance-2026-11-23d). `tools/humanization/his_fixes_brief.md` has ways 22 and 23 and the concrete-list line in way 19
  (tells J82 and J83).
- 2026-11-23 16:58 UTC (his message: why Opus wasn't working, Fable, whether Sonnet is good enough; he merged pull
  request 401). Opus agents answer in seconds but never finished the blind test with the full brief (five tries, up to
  27 minutes); Fable answered in 45 seconds and wrote the best rewrites (`r30/replay3/MODELS.md`), so blind writers are
  Fable now (`AGENTS.md`). With Fable, round 3 has 73 and 252 with 253 Human High, 214's own window High and the flaws
  stretch Human (High, Medium); 346 still read AI until one word of his, "compassionately" for "honestly", took it to 0%
  (`r30/replay4/`; way 21 of `tools/humanization/his_fixes_brief.md`). Straight quote marks changed no label
  (`r30/typo3/`). Lesson romance-2026-11-23e.
- 2026-11-23 17:27 UTC (his message: "honestly is a high freq ai word ... so if another word fits we can use that";
  "continue"). The article's five uses of "honestly" got the word that fits, each Human High by itself (`r34/`); the
  linter flags it (O77, W132; lesson romance-2026-11-23f). The eleven vetted junk passages (`r35/README.md`): seven
  fixes read Human High by themselves; B473 of them went in without a card, and the other six are cards on the sixth
  marking page (https://claude.ai/artifact/MZidQtzYFkWfAd1snh75zu, `review/teach-20261123/REVIEW-T6.md`), with B84,
  whose rewrite read AI (Low), as a card that cuts the line; the three (B257, B442, B480) whose fixes read AI are
  questions on it while the tries go on. (The commit of 76fd3fc8 counted eight read High: B84's cut rests on his own
  check of the paragraph before it, not a new one.)
- 2026-11-23 19:36 UTC (his sixth-page answers, and "you can't just switch honestly for compassionately always that's
  working sometimes, but like authentically, genuinely, those are more real synonyms, and honestly is also ok sometimes
  just it's overused"). The seven cards he approved and his own versions of B442 and B257 are in the fixed version
  (`humanize/fix-20261107/r36/HIS-T6.json`); B480 stays as the post has it ("makes sense to me as is"), on the new
  keep-as-is list (`whole/KEEP-AS-IS.json`). "honestly" is overused, not banned (lesson romance-2026-11-23g; O77, W132,
  way 21, AGENTS.md): his own word is back in 366 and 440, and 455 says "genuinely", Human High by itself. His two
  versions became way 24 and new lines of way 10 (lesson h); a Fable writer given them rewrote both passages blind, and
  both read Human High (`r30/replay5/RESULTS.md`). The fourteen sections that changed since the section pass were
  rechecked: thirteen Human High, and "Talk about making love", part 2, Human with three Medium one-sentence windows and
  no Low one (`r36/README.md`). His record now counts answered questions as answered (`approval_record.py`).
- 2026-11-23 23:49 UTC ("actually i don't like the medium windows ... i often find the medium windows indicate other
  issues also. i fixed that talk about making love section"). A Medium window is work to do, not done (AGENTS.md, the
  gate's E278, lesson romance-2026-11-23i). His fix of section 05 is in (`humanize/fix-20261107/r37/HIS-S05.json`, his
  check Human High); a Fable writer given lesson i without his version took the section to Human High
  (`r30/replay6/RESULTS.md`). The Medium pass on the other 21 sections (`r37/README.md`, every check linked): 19 read
  Human High in every window. Ten changed only model text and are in (`r37/MINE-R37.json`, with the model parts of the
  other nine); nine change his fourth-page versions or a line he kept there (two he had called a Pangram bug) and are
  cards on the seventh marking page (https://claude.ai/artifact/2YcdQ9tPPdAeEV1ZtU13NW, `review/teach-20261124/REVIEW-T7.md`).
  "From flow to nitty gritty" (42) and "Two Pillars", part 1 (67) are still below High after three tries each and are
  questions on it: 42's last clause is junk-read B210, which a reader couldn't parse (its best try is in, High 108 words
  and Medium 35); every change to 67 read worse. Lesson romance-2026-11-23j records what the pass showed (one-word and
  short lines standing alone; a list said as parallel clauses reading AI).
- 2026-11-24 02:06 UTC (his seventh-page answers, `review/teach-20261124/ANSWERS-T7.json`). The nine cards he approved
  are in (`humanize/fix-20261107/r38/HIS-T7.json`), and his own fix of "Two Pillars", part 1 ("damn this was an absolute
  disaster. i fixed it"; his check Human High, one window), from the text his check holds (`r38/his-67.txt`). His answer
  to Q-42 says what the clause meant; said plainly, with his story of Bee in his words, section 42 read Human High
  (`r38/MINE-R38.json`). Every one of the fixed version's 93 section checks now reads Human High in every window, 91 in
  my checks and 05 and 67 in his (`r38/README.md`). His Two Pillars fix, tested blind: the order alone read AI (47%),
  and with leave to cut unneeded lines Human with Medium and Low windows (`r30/replay7/`, `r30/replay8/`); lesson
  romance-2026-11-24a and way 28 of the brief say what his fix did and where a blind writer stops; lesson b, that a
  clause a reader can't parse is fixed by its meaning, his to give.
- 2026-11-24 (same turn): the junk pass. Of the 30 partly real passages of `r30/junk/VETTED.md`, 21 still stood; fixed his
  way (only the flagged words, nothing added) and checked in their 16 sections, all read Human High in every window, four
  after a second try that joined a short line the fix had left by itself (`humanize/fix-20261107/r38/junk/README.md`,
  lesson romance-2026-11-24c). 14 fixes keep the meaning and are in (`r38/junk/MINE-R38J.json`); three are cards on the
  eighth marking page (https://claude.ai/artifact/BfqATtsRc1ciJZSfmAjv8f, `review/teach-20261124b/REVIEW-T8.md`), with
  two questions on what he meant (B476, B478); B391 stays as it was. Every section check of the fixed version reads Human
  High in every window.
- 2026-11-24 12:34 UTC (his eighth-page answers, `review/teach-20261124b/ANSWERS-T8.json`). J-B217 and J-B255 approved
  and in (`humanize/fix-20261107/r39/HIS-T8.json`); J-B54 left undecided, so it stays as it was. B476 and B478 said from
  his answers, in his words (a passionate romantic relationship that's also stable; Somé and his parents trusting the
  universe): "Tough Love" read Human High, one window (`r39/MINE-R39.json`, `r39/README.md`). Every section check of the
  fixed version (93, 21,101 words) reads Human High in every window.
- 2026-11-24 (same turn): the reads of everything changed since the drafts were last pasted (r27). The word-for-sense
  read (150 paragraphs, three fresh readers, 9 of 9 planted errors found) left nothing to fix: its twelve other findings
  are his own words or fine in place (`r39/sense/TRACE.md`). The compare read of the 53 paragraphs I last wrote, by the
  lead model itself, found five severity-1 snags, each kept with its reason (`r39/compare/DISPOSITIONS.json`). Drafts A
  and B pasted again at 12:56 UTC from e07b733f; each secret link's rendered text matched (`whole/DRAFTS.json`, "r39").
  The builder now leaves out the four empty paragraphs his update of 2026-11-23 left by the embeds.
- 2026-11-24 16:23 UTC (his message: his whole-article check of the r39 drafts, J-B54 approved, "senegal should be
  corrected", the double full stop kept, his new opening of "Primal attraction", and the card game). Both drafts read
  Human with every window Human; three one-sentence windows of his live text read Medium at window edges
  (`humanize/fix-20261107/r40/RESULTS-whole-r39.json`). J-B54, Senegal, his new opening (live 252 to 260, with his video
  and links) and a pointer's section name are in (`r40/HIS-T9.json`); their sections read Human High, and every section
  check of the fixed version does. The first contradictions check: seven items, three explained, two not real, two to
  him; with two words a reader stumbled on, they are the ninth marking page (https://claude.ai/artifact/U6WQyL8B7ELEdDzHYbBeHk,
  `review/teach-20261124c/REVIEW-T9.md`). The card game, "Love, Honestly" on his innerself site: `r40/CARD-GAME.md`.
- 2026-11-24 18:14 UTC (his ninth-page answers, `review/teach-20261124c/ANSWERS-T9.json`; "no point checking the drafts
  until we are done"; the game stays private). His version of "Muses & Directors" (Q-C7), "in recent years" (Q-S5) and
  "worth doing" kept (Q-S12) are in; Q-C1 said in the Labels paragraph, whose section then read Human High after its short
  line was run on and its opener started on the case (`humanize/fix-20261107/r41/README.md`). The contradictions check is
  done. Every section check reads Human High in every window except his one-word "Woops...". First batch of new and
  corrected cards for the game: `r40/CARD-GAME.md`.
- 2026-11-24 19:58 UTC ("cards look good, you could keep the money card"): the first batch of cards is approved, and
  polarity-01 is kept with a "why" that no longer says the guide says it. The second batch (twelve cards for what the deck
  doesn't cover yet, his clarifications of this week included) is in `humanize/fix-20261107/r40/CARD-GAME.md` for his
  approval.
- 2026-11-24 21:31 UTC ("looks all good, i assume you are making sure they are only used when relevant right ... and if you
  have any other ideas to make game better lmk ... it should prob have a slider control for like how deep people want to
  go"): the second batch is approved. The game's next version, "Love, Honestly" v0.6.0, is built as a candidate in his
  love-honestly repository (a draft pull request, merged only when he approves the version) and went to him as a file to
  try: 17 new cards, each dealt only on its routes and at or above its depth, and 19 existing cards corrected in their
  "why" or section line after a fresh reader read all 95 against the article as it is now. Nothing on his site changed.
  The game already has the depth choice he thought of ("How deep?": Warm, Deep, Unfiltered); what it lacks is Warm cards
  (9 of 104). Six ideas went to him. `articles/BUILT-ON.json` now says the game is built on this article. The record:
  `humanize/fix-20261107/r42/README.md` and `r40/CARD-GAME.md`. Nothing in the article changed this round.

- 2026-11-25 (01:23 UTC, `humanize/fix-20261107/r43/`): his answer on the game ("yes tick attraction and polarity from
  the start, and i approve all 6 of your ideas"). "Love, Honestly" v0.7.0 built as a candidate on top of v0.6.0 (no card
  changed): Attraction & Polarity ticked from the start, a line under "How deep?", "A lighter one instead", a memory of
  played cards in the browser, two phones joined by a code; 30 engine checks (six deliberate breakages caught) and 42
  browser checks pass; the file went to him. The three ideas that need card texts written and put to him on one page,
  204 items: 28 Warm cards, a plain-words pass (92 lines on 62 older cards), a one-person route (its design, 41 cards
  turned toward one person, 14 new cards, 15 steps), and the 9 changes of v0.6.0 he had not seen. Nothing in the article
  changed. Lessons romance-2026-11-25a (the page tool's "Pending" button, fixed) and b (a rewording brief says that
  nothing is removed; every batch is read beside its originals).

- 2026-11-25 (17:20 UTC, `humanize/fix-20261107/r44/`): his message on the game ("200 cards is too much for me to read
  can you just tell me if any of them look like i should check? ...", "can we make spiritual practice personal instead of
  optional?", "i tried to biuld the game but build button did nothing (one phone)"). The button: a chat app shows the
  file in a frame that blocks form submission, where the form never sent "submit"; fixed in v0.7.1 (the tap starts the
  game), which also makes Spiritual Practice a personal topic that begins ticked. The 204 card texts: all read against
  the cards he approved and against the guide; four put to him (one Warm card with his "sex dolls" line, three points of
  the one-person route's design), three lines corrected before they went in. v0.8.0 built as a candidate on v0.7.1: 27
  Warm cards and 92 plainer lines on 62 older cards (131 cards, 36 Warm); 30 deck checks with six deliberate breakages
  caught, and 59 browser checks. Both files went to him. Nothing in the article changed. Lessons romance-2026-11-25c (a
  file he opens from the chat is tested in the frame he opens it in) and d (a batch for his approval is read for him
  first).

- 2026-11-26 (22:17 UTC, sent again at 22:43; `humanize/fix-20261107/r45/`): his four answers. The game's v0.8.1 keeps
  "Why this card?" on the 5 cards whose question needs it (134 lines out) and adds W03 without its "why"; v0.9.0 is the
  game for one person ("Who is playing? Two of us / Just me" first; the first screen as written; "I need to watch what I
  do" renamed "Life will show me", every label with its explanation; 95 cards with one-person text). The couples' game
  unchanged. v0.8.1: 25 deck checks with seven deliberate breakages caught, 66 browser checks; v0.9.0: 28 and eight, 91
  browser checks. The file went to him. Nothing in the article changed. Lessons romance-2026-11-26a (an attached
  explanation earns its place), b (a short name is read alone) and c (what he judges goes to him whole).
- 2026-11-26 (23:26 UTC, `humanize/fix-20261107/r46/`): he played on his own and wrote "the top text should be the
  biggest heading, because people read the biggest one first". The game's v0.9.1: the one-person label screen's heading
  is "Where does this card leave you?", with "Pick the one that fits best." in the line under it; on left-aligned cards
  that line starts where the heading starts. No card, label or rule changes. 104 browser checks, run twice. Put to him:
  the same rule on the "What is this answer based on?" step (my recommendation: apply it). The file went to him.
  Nothing in the article changed. Lesson romance-2026-11-26d (the biggest text says what the screen is about).
- 2026-11-27 (15:45 UTC, `humanize/fix-20261107/r47/`): "YES" to the evidence step. The game's v0.9.2: step 2, for two
  people and for one, opens with its heading "What is this answer based on?", the biggest text; the card's question is
  under it, smaller, after "Your answer to"; the instruction keeps its words as the line above the labels. No card,
  label or rule changes. Seven deliberate breakages caught; 146 browser checks (43 new), run twice. The file and a
  before-and-after picture went to him, and the game as a private page of this account. Nothing in the article
  changed. No lesson: his answer took the recommendation as it was.

## Next step

His OK on a version of the game (v0.9.2 carries v0.9.1's changes), or his changes to it (`r40/CARD-GAME.md`, "Still to
do"; `r47/README.md`). Then the pull request is merged, the innerself site vendors the file, and the site is deployed
with his go-ahead. From now on, a turn that changes the article
checks the cards that name the changed section (`articles/BUILT-ON.json`). When nothing else is pending: the drafts pasted
again for his whole-article check (not before: "no point checking the drafts until we are done"), then his post updated
with his OK (no email): 366's link to Esther Perel's post, the reel embedded after 149, his new opening's video and
links, the typography swap and the "Updated" date; he deletes the two drafts.

### Before 2026-11-07 (the registered master, as recorded then)

#### Goal

Maintain the exact owner-authorized Romance working master as registered GitHub authority, preserving its argument, owner-final language, memories, native-object placement, source provenance, architecture, and detector evidence while keeping citation, publication, and whole-article owner-final status explicit and separate.

#### Authority / baseline

- Article id: `romance`
- Article status: **working**
- Canonical master on `main`: `articles/romance/master.md`
- Master SHA-256: `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`
- Master word count (Markdown whitespace): **20,364**
- Candidate id: `romance-r23r2-owner-final-20260824`
- Promotion PR: #46, merged to `main` as merge commit `1abe38d2d3cd85e35ce1fbeb46217cb5cf89ff59`
- Source candidate: exact r23 at `u-dont-existDOTcom/pangram-humanization-lab@f4f2d6404e7362441c9ac0969dfc79313bea6ba1`, branch `evidence/romance-r23-gui-20260824-a`
- Materialization: `work/romance-r22-reconciliation-20260823/materialized-r23r2-owner-final/`
- Preservation receipt: `work/romance-r22-reconciliation-20260823/R23R2-PRESERVATION-RECEIPT-20260824.md`

Joel's 2026-08-24 direct correction makes the exact r23r2 Two Pillars local realization owner-final, including its double space after `rare.` and capitalized `If`. Joel reports the exact local realization tested Human / low confidence and explicitly accepts that result as `good enough`. This is sufficient bounded detector acceptance for working-master promotion; it does not mark the whole article owner-final or published.

#### Completed

- Preserved the earlier registered master, exact r22 known-green rollback, exact r23 GUI candidate, rejected r23r1 proposal, and unused R23R1-R03 fallback as durable provenance.
- Reproduced exact r23 source identities before materialization:
  - master `322953b5d6f6ad49f7a3b41e5c6795b36404508f7768669cdcc72223f2f21a0d`, 20,364 words;
  - Part 1 `620972febec1957403d261c4426c8fbba58763df2c0b78eb87a79da368f1f50b`, 10,296 words;
  - Part 2 `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`, 9,917 words.
- Materialized r23r2 with one exact operation inside Two Pillars and no other r23 change.
- Locked the exact owner-final span at SHA-256 `cd8de93fda39fcdf13c4b1f6ba2f9250c11c40f8c8298f281055e37bafed6291`.
- Proved forward traceability, reverse traceability, and zero unexplained substantive deltas.
- Preserved heading order, all 11 native objects, all 22 Markdown links, protected anchors, section topology, architecture dependencies, and terminal stopping point.
- Deterministic rematerialization PASS.
- Machine preservation receipt PASS.
- Content repository validator PASS.
- Architecture-map validator PASS.
- `python -m unittest discover -s tests`: 99 tests PASS.
- Repository audit: 0 errors; 4 pre-existing governance warnings.
- `git diff --check` PASS.
- Hosted exact-byte/hash readback PASS.
- PR #46 merged successfully into `main` at `1abe38d2d3cd85e35ce1fbeb46217cb5cf89ff59`.

#### Current checkpoint

2026-11-07, the 17:07 UTC pickup. 20 of the 22 spots read Human with no Low window (S1, S3 to S16, S18 to S22; S7 in
its section, #107, S9 in its section's High window, #113, S20 in its section, #106, S21 in its section, #110, S22 in its
section, #69). S2 and S17 wait on the marking page for Joel's versions.

Twenty-two sections that had Low windows or spots in the live post now read Human with no Low window in their own
check: "My flaws" (#61), "Peeking thru the window" (#67), "Things get tricky fast" (#68), "Holding up a leaky dam"
(#70), "The window of clarity" (#71), "Anti-PTSD Can Be Just As Dangerous As PTSD" (#73), "Muses & Directors" (#81),
"The Queen of Orgasms" (#82), "Labels Are Descriptive, Not Prescriptive" (#84), "Disconnect to connect" (#88), "Slow &
steady" (#96), "It always goes deeper" (#97), "Fantasy" (#99), "Situationships" (#100), "Some babies grow up faster"
(#101), "Different levels in different domains can be complementary" (#102), "Why all of this sounds artificial"
(#104), "Gaslighting in the dark" (#105), "What are you actually choosing together?" (#106), "The conversation about
flaws" (#107), "What I gained from loss" (#109) and "Which marriage vows are honest?" (#110); so does "After leaving",
with S22 in it (#69). "From flow to nitty gritty" reads Human with one Low window, on 201's closing sentence, which
reads High by itself (#112); its tries are spent (#108, #113, #114), so that window is named for the whole-article
check. So is "Two Pillars Don't Hold The Roof Up" 332, the paragraph the owner lock keeps as the live post has it.

"Can making love be a spiritual practice?" read 14.8% AI with S17's best try in it (#45). Its AI and Low windows outside
S17's own lines (its card on the marking page) now read Human High in their own checks (#115, #116). "Spirituality to
bypass intimacy" (#48) reads AI only on S2's own lines. So every window a smaller check read AI that is still in the
fixed version is S2's, S17's or one of the three stretches that share S2's pattern: all wait on Joel's answers.

Still AI: "Jealousy on trial" (367 to 369, #94), "Romance Shouldn't Be Adjudicated" (285 to 287, #98) and "Beware
idealization" (148, #93). All three are his general claims about men, women, monogamy and idealization, said evenly.
Each reads High by itself and AI in its section, his live wording included, and my joins don't move them. That is the
pattern of S2's card on the marking page, so his answer there is the likeliest way to learn how he'd say these.

What these checks showed: a section checked by itself reads harsher than the whole post did, and his general claims
read AI there whatever the joins. His short sentences joined to what they belong with, a paragraph's point said first,
a claim left a little unbalanced ("without (most of) the responsibility"), a repeat cut, and a list cut to the items
it needs read High (a list only re-shaped read Low, #111, #112). A run of short questions reads one window per
question inside its section, even where the pair read High by itself; joined into fewer questions, they read High.

## Remaining

1. S2 and S17: Joel's versions on the marking page; then carry what he did to the lines each card names, and to the
   stretches that share S2's pattern ("Jealousy on trial" 367 to 369, "Romance Shouldn't Be Adjudicated" 285 to 287,
   "Beware idealization" 148), each checked in its section until it reads Human.
2. The whole-article check, once 1 reads Human: rebuild the fixed version with those changes (`whole/assemble.py`,
   `whole/build.py`), read the new paragraphs for sense, paste it again into the two temporary drafts
   (`whole/DRAFTS.json`; `whole/build_draft.js` at the new commit), make each secret link, check its rendered text, and
   give Joel the two links to open and run his extension on. The windows named for that check: "From flow to nitty
   gritty" 201's closing sentence and "Two Pillars" 332. Then his post updated with his OK, no email.

## Blockers / unresolved

- Publication remains blocked on the owner decisions recorded in `review/FINAL-CORRECTIONS-20260824.md`, including factual and citation corrections that require owner-approved prose.
- Copyright and license posture remain separate owner decisions.

#### Evidence / artifacts

- Canonical working master: `articles/romance/master.md`
- Owner locks / protected functions: `articles/romance/OWNER-LOCKS.json`
- Source/evidence index: `articles/romance/SOURCE-EVIDENCE.json`
- Architecture map: `articles/romance/ARCHITECTURE.md`
- Citation state: `articles/romance/CITATIONS.json`
- Detector evidence: `articles/romance/DETECTOR-EVIDENCE.json`
- Editorial state: `articles/romance/EDITORIAL-STATUS.json`
- r23r2 delta: `work/romance-r22-reconciliation-20260823/R23R2-OWNER-FINAL-DELTA.json`
- r23r2 machine-readable preservation receipt: `work/romance-r22-reconciliation-20260823/R23R2-PRESERVATION-RECEIPT.json`
- r23r2 preservation receipt: `work/romance-r22-reconciliation-20260823/R23R2-PRESERVATION-RECEIPT-20260824.md`
- r23r2 materialized master/halves/receipt: `work/romance-r22-reconciliation-20260823/materialized-r23r2-owner-final/`

#### Next safe action

Use exact r23r2 on `main` as the sole current Romance working authority. The next substantive publication-preparation work is a fresh whole-article editorial pass and citation review when requested. Do not equate the r23r2 merge with publication, licensing, completed citation review, whole-article owner-final acceptance, or a whole-article detector pass.

## Current checkpoint

2026-11-07, the 22:57 UTC pickup. Every spot and section his extension or a section check read AI now reads Human in its
section, except "Jealousy on trial" 367 to 369, which wait for his version on the second marking page. S2 and S17 are
his versions (#117, #118, one Human High window each). "Romance Shouldn't Be Adjudicated" reads Human with no Low (#122).
"Beware idealization" reads Mostly Human with no AI window and five Low windows (#132): S8's 145 opener, 147's
disclaimer, 148's first two sentences and 151's two sentences.

What his versions taught (romance-2026-11-07a to d): lists of abstract nouns become particular things said different
ways; someone's teaching is said as what they say; a rhetorical question becomes its reason; plain words and his
register. They fixed Romance and Idealization. On Jealousy they fixed each paragraph alone and not the three together,
and neither did idioms, scenes, people doing things, or the links a sense read asked for.

## Remaining

1. Jealousy 367 to 369: his version on the second marking page (REVIEW-T2); then its section check.
2. "Beware idealization": its five Low windows (#132), after the fix.
3. "Situationships": one more check of the section after the fix (28a), with paragraph 34 as it read in #95.
4. The sections with a fixed spot and open Low windows ("Some babies grow up faster", "Different levels in different
   domains", "De-ontologizing Twin Flames"); the 8 Low windows of the post's last part (#47); S7's and S9's Low lines;
   S21's section.
5. The word-for-sense read of the fixed version's new paragraphs, then a whole-article check (the two temporary drafts
   re-pasted from `whole/REPLACEMENTS.json`, for his extension), then his post updated with his OK, no email.

## Blockers / unresolved

- None blocking. Kim Anami's linked page could not be read from here (the fetch waited for an approval nobody
  answered), so her claims are kept as the live post words them.

## Evidence / artifacts

- `humanize/fix-20261107/live-check/META.json`, `AI-WINDOWS.json`, `LOW-WINDOWS.json`; `humanize/fix-20261107/r01/` to
  `r26/` (check texts, receipts, predictions, results, tell panels); `humanize/fix-20261107/whole/` (the fixed version);
  `review/teach-20261107/` (the marking pages: `build_t1.py`, `REVIEW-T1.md`, his `ANSWERS-T1.json`, `build_t2.py`,
  `REVIEW-T2.md`, `SENSE-T2.md`, `ARTIFACT.md`); `humanize/pangram-ledger.jsonl`; `humanize/SCORECARD.md`.

## Next safe action

Remaining 2 (the idealization Low windows) can go on without him; Remaining 1 waits for his answer on REVIEW-T2. Read his
answers when he gives them, put his version in, check the jealousy section, then Remaining 5.
