# Proposed rule for innerSignalGraph: every guide addition is explained

From the joel-articles humanization lane, 2026-10-08. This is a suggested fix for innerSignalGraph, written so it can go into universal-dev-architecture's `suggested-fixes/innerSignalGraph/` lane (innerSignalGraph's `AGENTS.md`: "Before starting other fixes here, read this repository's lane in `u-dont-existDOTcom/universal-dev-architecture`: `suggested-fixes/innerSignalGraph/`"). It was not filed: this session couldn't get write access to either repository without the owner's OK.

**Marked as an owner request.** Joel, 2026-10-08 02:23 UTC: "maybe we should somehow implement a rule that guide additions can't be suggested by other owrkers unless they are explained, what map change caused them, and how they are really needed vs superfluous to the guide."

## What happened

- Pull request #126 ("Refine InnerSignal continuity scaffolding", 2026-10-04) fixed the app after a new-client test. Its plan includes "Create a new canonical guide text version derived from the current 2026-10-03 r3 text with minimal additions", so the app's new rules went into the canonical guide as prose:
  - handling a client's no to inner-child work;
  - recording a pause and its re-entry level;
  - judging workable challenge;
  - diversified community support.
- The prose kept the app's point of view. The guide tells the reader not to "sneak it back in through “gentler” exercises", which is the app's rule about re-offering (the owner asked: "who is gonna be "sneaking reparenting in" thru some gentler version?"). One paragraph names "this app".
- None of it went on `authoring/PENDING-PUBLIC-GUIDE-CHANGES.md`. That matches this repository's contract ("Runtime-only mechanics do not require a public-guide entry"). But the guide text gave no sign that it was runtime-only.
- The humanization lane read the guide's diff, treated the unqueued paragraphs as reader-facing (its own error, now fixed on its side), and drafted them for the public article. The owner then couldn't tell where they came from or what they were for.

## The rule

1. **A reader-facing guide addition carries its reasons.** A change that adds or changes prose in a canonical guide (`guides/inner-child-guide-*.txt`, and the other families) goes on `authoring/PENDING-PUBLIC-GUIDE-CHANGES.md` in the same reviewed change, with three fields:
   - **Caused by:** the pull request, the owner amendment and node or route IDs, and the owner outcome in one line.
   - **Reader need:** what a reader of the public guide would miss or get wrong without it.
   - **Not superfluous:** where the guide already covers nearby ground (and the public article, when known), and what this adds.
2. **App rules stay app rules.** A rule written for the app's behavior (routing, state, re-entry, labeling, re-offers) lives in the map, the rules and the prompts. It goes into canonical guide prose only if it passes rule 1. If the app's source needs prose for it, mark that prose runtime-only (an inline marker, or an appendix the humanizer skips), and write it in the guide's own voice, not as an instruction about the app's moves.
3. **Not queued means runtime-only.** A guide-text change that isn't on the queue is runtime-only. Humanizers don't carry it into the public guide.
4. **Existing entries.** Bundles A to D name their upstream authority but not the reader need. Add the two missing fields when an entry is next touched; a humanizer asks for them before drafting an entry that lacks them.
5. **The October 4 #126 paragraphs.** Either queue each with the three fields, or mark them runtime-only. The humanization lane has parked them until then:
   - depth and pause: "That means turning the depth down…", "If you do want the relationship but a particular depth…", "A complete tolerance pause…";
   - pleasantness: "Do not use pleasantness…", "If those answers are not known yet…", "Dreams and imagery…";
   - isolation and community: "If isolation itself…", "Look for more than one door…", "Use the Protector here too…";
   - the difficult-dream paragraph.

## Where it would change text

- `docs/PUBLIC-GUIDE-HUMANIZATION.md`, "Pending change queue": rules 1 to 3.
- `authoring/PENDING-PUBLIC-GUIDE-CHANGES.md`: the entry template gets the three fields, and the header says an unqueued change is runtime-only.
- `AGENTS.md`, where it points humanizers at the queue: one sentence for rule 3. Its edit rule applies: update the reviewed SHA-256 bindings in `scripts/audit-repository.mjs` in the same change.

## On the humanization side (done)

In joel-articles, `tools/humanization/reviewer/reviewer.py` won't build a draft or dedup prompt for a guide passage with sentences that aren't in the article's original guide, unless the target explains them (`"provenance"`: `"map_change"`, `"why_reader_needs_it"`). Its gate says an unqueued guide change is runtime-only by default (E155).
