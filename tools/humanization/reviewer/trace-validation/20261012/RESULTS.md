# Trace and cold-read validation, 2026-10-12

After Joel's message of 2026-10-12 05:33 UTC on community section 12 ("p3 got b roken ... then you broke p7 ... p16 also broke the meaning ... debug the error so it doesn't happen again"), three checks changed:
`trace_brief.md` ("The words a claim rests on are never just conversational"), the referent rule in `sense_section.txt` and `sense.txt`, and a new mechanical check, `tools/humanization/preservation_keys.py`.
All agent runs below were fresh Sonnet agents, one run per prompt file.

## 1. The new trace brief on the section-12 paragraphs he named (TV1, TV2)

Input: the v9 paragraphs he said broke (published P3, P6 and P15; page P3, P7 and P16), with two paragraphs he didn't flag (P4, P10) and P14.
This is an echo test: the brief quotes his breaks as its examples, so catching them shows the brief is read, not that it generalizes.

| Pair | His finding | TV1 | TV2 |
|---|---|---|---|
| P3 | "good enough" lost "for community" | LOST "for community" | (not in this run) |
| P6 (page P7) | "But it's not infinite." | SHIFT "it", LOST "absorbent" | SHIFT "it", LOST "absorbent" |
| P15 (page P16) | "this language of capacity", "it", "remains" | all three, and LOST "still" | all three, LOST "still", ADDED "and all of that" |
| P4 | none | OK | (not in this run) |
| P10 | none | (not in this run) | OK |
| P14 | none | (not in this run) | LOST "available" |

Two findings go past his examples: "still" in "I still don't know" (v9 had dropped it) and "available" in P14 ("more available resource than acute need"). Both were real, and both are fixed in v10c (P16g is the guide's sentence; P14p4 has "more available resource").

## 2. The new trace brief, blind, on held-out pairs (HV1, HV2)

Input: `heldout/trace-in-HV1.md` and `trace-in-HV2.md`, eight published paragraphs from sections 13 and 14 (not yet humanized), each with a rewrite I wrote.
Six rewrites carry one planted break of the three kinds the brief names, on words its examples don't use. Two are conversational rewording only.
The key (`heldout/KEY.md`) was outside the folder while the agents ran.

| Pair | Planted | Result |
|---|---|---|
| A1 | "over it" for "over the community" | SHIFT, fix "over the community" |
| A2 | "the money you put in" for "everything contributed" | SHIFT, fix "everything you put in" |
| A3 | control | OK |
| A4 | "costs a lot less", without "than a six-month misunderstanding" | LOST, fix restores it |
| B1 | "It's also" for "The power to remove somebody is also" | SHIFT, fix the published noun |
| B2 | "whether they say “namaste” a lot" for "spiritual vocabulary or therapeutic fluency" | SHIFT and LOST |
| B3 | control ("a couple of weeks", "So congratulations") | OK |
| B4 | "after he left it", without "long" | LOST "long" |

8 of 8: every planted break found with the planted reason, and no finding on either control. The controls' "But", "So" and "a couple of" were called EQUIVALENT, so the new rule didn't undo "Conversational is not a shift" (2026-10-09).

## 3. The cold-read referent rule (SV1 to SV4)

| Run | Prompt | Text | Result |
|---|---|---|---|
| SV1 | first (broad) rule | section 12, v9 | flags P7's "it", P16's "it" and "the power"; also P3, P12, P17 |
| SV2 | first (broad) rule | section 11, Joel's own text | 4 flags on his text (P12, P14, P15, P16) |
| SV3 | narrowed rule | section 12, v9 | flags P16's "it" and "the power" |
| SV4 | narrowed rule | section 11 | no flags |

The first rule asked about every pronoun and flagged his own section-11 paragraphs, so it was narrowed: a word gets a line when it could be either of two things and the sentence would say something different with each, or a "the" phrase whose thing the text never names (his "what power?").
The narrowed rule catches P16 and leaves his text alone. It missed P7's "But it's not infinite." in SV3, which the trace caught in both runs. So the trace is the check for a meaning lost against the published text, and the cold read is a second net.
(SV4's first run stopped at the 64,000-token output limit with no report; the rerun had "keep your working short" and finished.)

### After merging with main's general-reference line (`merged/`)

Main had added, the same morning, a line that a general reference ("their excuses") needs no setup (`sense-validation/RESULTS-20261012b.md`). With both rules in the prompts:

| Run | Text | Result |
|---|---|---|
| SVm1 | section 12, v9 | P16's "it" and "the power" flagged, as in SV3 |
| SVm2 | section 11 | no flags |
| SVm3 | inner child, Also Look Outward | flagged P5's "it" and P7's "the complaint", which main's line had stopped (0 of 3) |

So the "the" phrase rule had reopened a false flag: "the complaint" points back to P1's "you bring up something that hurt", four paragraphs up. The rule now says a thing named earlier in other words counts as named, and that an "it" summing up everything just described isn't two things (each with an example that isn't the tested sentence). Then:

| Run | Text | Result |
|---|---|---|
| SVn1 | section 12, v9 | P16's "it" and "the power" flagged |
| SVn2 | section 11 | no flags |
| SVn3 | inner child, Also Look Outward | no flags ("their prior promises" OK, as main's runs) |
| SVn4 | the same, with main's planted "the promise they made at the lake" | the planted reference caught |

Each run is one fresh Sonnet agent, so these are single readings, not rates. The stored prompts are what the agents read, except that trailing spaces from the inner child article's list lines are stripped (`git diff --check`). They were built with `reviewer.py --article ARTICLE sense-section OUT --section HEADING [--draft FILE]`; SVn4's draft is `sense-validation/20261012b/section-planted-lake.md`.

## 4. The mechanical check

`preservation_keys.py` with `candidate/s12/preservation-keys.json` (35 units, each with the words its meaning rests on): v9 fails 8 units (U7, U8, U11, U26 to U30), and v10 fails U26 ("available"). v10c passed the file as first written; then the sweep of sections 1 to 12 for the same kinds of break (community lane, `sweep-20261012/SWEEP-RESULTS.md`) found two more narrowings in it, "fix the cars" for "equipment repaired" and P22's "people who fall into these categories" for "every limit". U24 and U32 now carry those words, v10c fails them, and v10f passes. Tests: `tests/test_humanization_tools.py`, `PreservationKeys`.
Matching is per paragraph, because a whole-section match passed U26 on a "free resource" in another paragraph.

## 5. Author marks in the sweep (Joel, 17:23)

Joel: "rather than just ignoring rules that fail my prose, we should fix the rules so they don't fail my prose". `tools/humanization/meaning_sweep.py` builds the sweep from the published and rewritten article and wraps his sentences (the owner-edits ledger's applied entries, and his own texts) in ⟦author⟧ marks, which the reader is told to leave alone; the trace brief honors the same marks.
Blind runs on the sections where the first sweep had flagged his paragraphs, with one break planted in my text in each (`sweep-marks/`, key in `sweep-marks/KEY.md`):

| Run | Sections | First sweep, flags in his text | With marks, flags in his text | Planted break in mine |
|---|---|---|---|---|
| M1 | 1 and 2 | 6 | 0 | caught ("can't tolerate it anymore") |
| M2 | 8 | 4 | 0 | caught ("principles about bedtime") |

Whether those 10 flags were right about the meaning is Joel's to score (the community lane's Rule Scoring Sheet). His "it" ruling is in the brief too: an "it" that is clear in its place is fine.
