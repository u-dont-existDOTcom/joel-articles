# Inner Child Therapy opening — assembled-boundary screenshot audit

Date: 2026-09-17

Status: **REVISIT AFTER CURRENT EPISODE 008 SUBSECTION / NO EVIDENCE OF LOST PROSE / ASSEMBLED-BOUNDARY CERTIFICATION GAP**

Authority boundary: Inner Child Therapy remains unregistered/non-authoritative.

## New owner evidence

Joel supplied a Pangram screenshot from the beginning of the humanized article showing:

- document display: `1 of 2 segments is AI`;
- first segment: **Human Written / Medium**, 54 UI words, beginning `The Chicken-and-Egg Problem Céline’s...`;
- second segment: **AI / Medium**, 99 UI words, beginning `So I stopped asking the child to heal it...`;
- total displayed boundary: 153 UI words.

The screenshot does not expose the complete submitted text or exact segment endpoints, so do **not** reconstruct an exact SHA or claim exact byte boundaries from the image alone.

## Was previously humanized prose lost?

**No lost accepted rewrite is currently evident.** The exact current prose can be traced to durable earlier humanization artifacts:

1. The current Céline paragraph is the repaired Episode 001 endpoint after deletion of the tidy close `The difference is that the child doesn’t have to run the show.` Its exact no-terminal-newline SHA is `48e2c8a7089c2a22975d3f75ec09d041a41f5a3a26584fd76ca1f1fe770b5905`.
2. The current next paragraph beginning `So I stopped asking the child to heal itself...` is the Episode 002 model paragraph. Episode 002 recorded the Céline paragraph + this paragraph as owner-reported **Human / low confidence** on that exact two-paragraph boundary.
3. The current chicken-and-egg paragraph is Joel's Episode 003 aligned rewrite, owner-reported **Human / low confidence**.
4. Episode 004 already proved that locally Human short paragraphs can combine into an **AI / medium** larger boundary.
5. The current chicken-and-egg paragraph + current borrowed-adulthood paragraph were then repaired as Episode 005. The exact 166-word boundary was owner-reported Human on five checks, with the first explicitly **Human / medium**.

Therefore the durable prose history is present. The new screenshot is more consistent with a **boundary-integration/certification failure** than with a missing rewrite.

## What appears to have gone wrong in the bookkeeping

The early workflow certified overlapping local boundaries in sequence:

- Céline alone / Céline + adult-role paragraph;
- chicken-and-egg paragraph locally;
- chicken-and-egg + borrowed-adulthood boundary;

but did not leave a durable record proving that the **assembled opening beginning at the article heading and continuing through all of those accepted pieces** was detector-stable as one natural delivery boundary.

The current rolling article and writer state later compressed those local results into labels such as `Episode 005 natural boundary: Human`, which can be misread as certification of the whole opening. It was not.

This is a state/reporting failure: component humanization evidence was recorded, but assembly-level certification was not clearly distinguished from component-level certification.

## Interpretation of the new screenshot

The screenshot's split is compatible with the already-known boundary-interaction behavior:

- the opening Céline material is recognized as Human/medium;
- a larger continuation beginning with `So I stopped asking the child to heal itself...` is recognized as AI/medium in this assembled context.

Because the screenshot gives only segment starts, not exact ends, the present audit does not claim whether the AI segment stops after the adult-role paragraph, includes the chicken-and-egg paragraph, or extends farther.

Do not edit the prose from this screenshot alone. First bind the exact submitted opening boundary when revisiting it.

## Required later repair task

After the current Episode 008 subsection decision is resolved:

1. recover/freeze the exact opening boundary that produced this screenshot if Joel still has the exact pasted text; otherwise freeze the current reader-visible assembled opening as the next test boundary and clearly mark the evidentiary difference;
2. compare exact current bytes against Episodes 001–005 to confirm no prose drift;
3. distinguish local known-Human components from the assembled red interaction;
4. audit the assembled thought movement before any Pangram call;
5. repair only the actual cross-boundary failure without reopening known-good component prose gratuitously;
6. update rolling-state labels so `component Human` can never again be mistaken for `assembled boundary Human`.

## Current disposition

- **No evidence that a humanized paragraph was lost.**
- **Yes, there was an early evidence/state-integration failure:** the whole assembled opening was not durably certified or clearly marked as uncertified.
- Queue this opening-boundary repair immediately after the current Episode 008 subsection lane.
