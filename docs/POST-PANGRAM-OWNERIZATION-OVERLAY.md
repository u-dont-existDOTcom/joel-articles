# Post-Pangram Ownerization / Improvement Overlay

Status: **CAPTURED ON CURRENT TASK BRANCH; reusable workflow awaiting canonical promotion**

Owner correction: 2026-09-16.

## Purpose

Pangram-Human is Target #1, not the end of editorial work. Once an article or substantial section passes its intended Pangram boundary—or when the humanization lane is genuinely exhausted—run a separate Target #2 review for improvements that should **not** be folded into detector-driven generation.

The output is an HTML review overlay on the complete reader-visible article/section. It must keep two classes of suggestions visibly separate.

## A. OWNER-ONLY AUTHORSHIP SUGGESTIONS

Use this class when a stronger realization would require facts, memories, judgments, relationships, anecdotes, private language, social knowledge, or lived cognition that the model does not possess and must not invent.

Examples:

- a real memory or scene that only Joel can supply;
- how a specific friend, partner, teacher, family member, client, or community actually talks or reacted;
- a personal comparison, joke, irritation, emotional contradiction, local phrase, or remembered detail not in the source pool;
- Joel's actual ranking, uncertainty, disagreement, embarrassment, attraction, fear, or reason for caring when it is not already documented;
- a better reader-facing example that depends on Joel's real life rather than synthetic specificity.

For every owner-only suggestion, the overlay should state:

1. exact span/section;
2. what feels generic, thin, or unlike fully authored prose;
3. what kind of authorial input would improve it;
4. one narrow question Joel could answer if he wants to supply that input;
5. **never fabricate the answer**.

A Pangram-Human passage may still receive owner-only suggestions. Detector status and authorship richness are separate axes.

## B. ASSISTANT-/RESEARCH-CAPABLE SUGGESTIONS

Use this class for improvements Chat can potentially implement without inventing Joel's life.

Examples:

- draw more from an already-authorized source or owner passage;
- research a factual/evidentiary gap when Joel authorizes research;
- adjust section architecture, stopping point, transition, or audience targeting;
- reduce repetition or restore a source function lost elsewhere;
- make the practical instruction more executable;
- improve title/heading fit, links, source placement, or media relationship;
- adapt register for the actual audience;
- compare a claim with existing article evidence or a named source;
- propose an image, diagram, table, or example based only on already-supported material.

Each suggestion must say whether it is safe to implement automatically, requires factual research, requires source recovery, or still requires owner approval because it changes substance.

## Timing

- Default: run after the section/article reaches its Pangram acceptance target.
- If humanization cannot reach the target after the current stop rule, run the overlay anyway so useful non-detector improvements are not lost.
- During humanization, **bank** Target #2 suggestions rather than distracting the production detector loop.
- Review the accumulated bank at the end of each substantial section and again at whole-article closeout.

## HTML overlay behavior

The overlay should preserve the full article text and mark suggestions without replacing the prose automatically.

Suggested visual controls:

- toggle `Owner-only authorship`;
- toggle `Assistant/research-capable`;
- filter by section;
- status: `open`, `accepted`, `implemented`, `rejected`, `banked`;
- click a highlighted span to open the suggestion, rationale, input needed, and implementation authority;
- a clean-reading mode with all annotations hidden.

The overlay is a review surface, not article authority. Accepted changes must still flow through the normal source/preservation/authority gates before entering publication copy.

## Separation from humanization

Do not use owner-only suggestions as covert Pangram optimization. If detector repair can be done faithfully from existing source meaning, do it normally. If a genuinely stronger version needs new Joel cognition, bank it for Target #2 unless that missing cognition is necessary to solve the current section and Joel chooses to provide it.

Do not let a Target #2 suggestion reopen a known-green passage merely because the model can imagine a different style. The suggestion should identify a real authorship/editorial opportunity, not detector superstition.
