---
name: joel-articles
description: Write, edit, reconstruct, fact-check, humanize, review, publish, and detector-audit Joel Rosenblum's articles while preserving his actual thought, claims, provenance, links, media, and voice.
version: 4.13.1-candidate
---

# Joel Articles Skill — 4.13.1-candidate

This repository is canonical for the Joel Articles **workflow, editorial protocols, tools, and registered article authority**. Workflow authority does not create article-content authority by itself. `articles/INDEX.json` remains the repository-wide article registry: if an article is not registered there with its required authority family, do not invent, reconstruct, or declare a canonical article master. Follow `AGENTS.md` and the article import protocol for article authority.

## Instruction priority

Use only for Joel Rosenblum's byline. Priority:

1. the current request and Joel's direct owner-final corrections;
2. registered article state, owner locks, master, authority, and ledgers in this repository;
3. `project-sources/CANON-FACTS.md` and `project-sources/ARTICLE-INDEX.md` where applicable;
4. this skill and the task-specific protocols named by `CANONICAL-REPO-MAP.md`;
5. voice references, examples, and corpus material.

Direct Joel rewrites supersede model candidates. A detector-passing model or model-assisted passage never outranks owner-final prose.

## GitHub-first execution

At the start of substantial work, read this file and `CANONICAL-REPO-MAP.md` fresh, then load the smallest set required by the task. Resolve current article authority through `articles/INDEX.json` and the article-local state named by the registry. Do not use Project memory, old Project Sources, web search, or model memory as substitutes for current private GitHub authority.

For detector/humanization work also read private repository `u-dont-existDOTcom/pangram-humanization-lab` fresh: its README, current `state/WORKING-LESSONS.md`, relevant case study, and latest relevant case/history. Inspect its cache/history before proposing paid Pangram calls so completed or ambiguous runs are not duplicated.

After any substantive owner-final correction, accepted section, authority/state change, durable detector lesson, case-study finding, or tooling repair, update the appropriate GitHub repository before claiming durable completion. `joel-articles` holds editorial protocols, registered article authority/state, publishing tooling, and promoted editorial lessons. `pangram-humanization-lab` holds the detector harness, raw/cached evidence, experiment histories, and detector research. Never commit secrets.

## Task loading

Before substantial article work, read `project-sources/MASTER-INSTRUCTIONS.md` and choose the least invasive mode from `project-sources/TASK-MODES.md`.

For P2S/P3/P4, author-intent recovery, reconstruction, or detector work also read:

- `project-sources/HUMANIZATION-AND-COHERENCE.md`
- `project-sources/EDIT-CONTRACT-AND-LEDGERS.md`
- `project-sources/FINGERPRINT-PASS.md`

For research-heavy/contested claims read `project-sources/ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md`; use the deterministic argument ledger only at the threshold specified by its quickstart. For Substack source/publishing work read `project-sources/INTERLINKING-AND-HTML-SOURCE.md` and `project-sources/CONFIRMED-SUBSTACK-HELPER.json`. Load only what the task actually needs.

## Execution gate — repair the thought before the prose

Never draft merely because the task says rewrite, humanize, polish, or fix.

Before writing, inspect the exact source passage and relevant neighbors:

- What exactly is being claimed, questioned, inferred, remembered, or recommended?
- Does it survive ordinary reality?
- Does a premise already answer the supposed question?
- Is a contradiction manufactured by an unstated assumption?
- Are actor → action → object, cause, chronology, certainty, attribution, heading, and link referent coherent?
- What would an ordinary person actually feel, do, fear, hope for, or respond to here? What feedback loop exists?
- Is the paragraph needed in anything like its inherited form?
- What is the source provenance: owner-authored, natural owner rewrite/publication prose, detector-targeted owner edit/minimal pair, assistant-produced owner-accepted, owner-final scan/PDF, superseded assistant candidate, or synthetic probe?
- Should the inherited architecture survive at all?

If the thought fails this gate, do not draft prose. Repair/recover the thought first or ask only the irreducible authorial question. Do not ask Joel to repeat information already available in authoritative source material.

## Strong claims

Do not flatten prose merely to avoid ever being wrong. Never invent facts or fake certainty, but worthwhile writing may make empirical or judgment claims strong enough to be contestable. Flag or qualify a claim when there is a concrete material reason, not merely because it is empirical. Preserve severe-claim agency exactly.

## Coherence architecture before sentences

Privately establish:

- heading promise;
- real pressure/question and reader stake;
- claim and certainty;
- motive/obligation where relevant;
- lived/intellectual route;
- actor → action → object;
- causality/chronology;
- source landscape and unequal roles;
- strongest complication;
- governing movement;
- paragraph jobs;
- real stopping point;
- exact language retained and why.

If inherited architecture is globally model/content-writer shaped, reject it. Reconstruct from the richest Joel/source pool rather than polishing an AI-compressed claim summary or question-order outline.

## Curious-reader chain

Sentence by sentence ask:

> What do I actually want to know next?

The next sentence must answer, complicate, or naturally redirect that live curiosity. Do not answer questions the reader no longer has. Do not turn the rule into fake suspense or mechanical Q&A. A thought may be logically complete without verbalizing every implication; if genuine curiosity remains, do not amputate it merely because a detector is green.

## Overcompletion

Optimize for the next necessary move, not for less explanation. Keep sentences that change time, case, premise, causal state, consequence, or the live question. Cut sentences that merely explain why the author just said something, restate an inference already available, diagnose a dynamic already demonstrated, or complete conceptual space because the model can. A bridge may be necessary; judge function, not sentence type. If downstream prose seems forced to repair an earlier paragraph, inspect upstream logic and stopping point first.

## Owner prose versus generation training

In real article work, reuse good owner prose freely; it need not be only “better” to deserve preservation. In explicit generation-training experiments, first recover the thought and generate fresh syntax without borrowing Joel's realization, then compare. Keep owner authorship, owner acceptance, detector status, and natural-human provenance separate.

Treat interviews and notes as source pools, not transcripts. Preserve raw answers in the ledger/bank, but reuse them in publication prose when they are owner-final/locked, exact memory/quotation/formula/title, identity-bearing, semantically precise, or functionally superior. Give every substantive item a disposition: use now; bank to a named destination; preserve as context/evidence; or omit with reason. Owner-deleted material is resolved, not silently resurrected.

## Mandatory cold audits

Never show Draft 0 by default. After drafting, inspect the literal completed prose as if someone else wrote it. Run two cold audits normally; run a third only if the second still finds a real defect. Stop when a pass finds no legitimate weakness; never paraphrase for novelty.

Audit:

- semantic sanity and ordinary reality contact;
- curious-reader continuity;
- unnecessary recap and interpretive aftercare;
- functional redundancy even when wording differs;
- pre-completed/content-writer sequencing;
- generic bridges and false symmetry/completeness;
- heading promise and paragraph progression;
- exact claims, certainty, actors, chronology, causality, attribution, memories, quotations, links, media, source roles, and owner corrections;
- the real stopping point.

If an audit finds a legitimate weakness, fix it before showing Joel or explicitly justify why preservation is necessary. Never knowingly ship a weakness and call the audit complete.

## Detectors

Coherence, fidelity, article function, and editorial quality pass first. Pangram is secondary evidence, never authorship or quality authority.

Preserve complete detector boundaries, exact text hashes, detector/model/version/date, repeats, nulls, counterexamples, and interaction tests. Short text is less reliable. Never infer magic words from one result. Never add irrelevant material, delete true evidence, weaken a claim, or accept worse prose merely to improve a detector. A detector-targeted owner edit is not automatically natural-human gold.

For repetitive manual variants, use the Pangram Humanization Lab rather than asking Joel to run one-off paid tests; inspect GitHub cache/state first.

## Article authority and repository governance

This skill does not override `AGENTS.md`, `articles/INDEX.json`, article-local owner locks, article current state, registered masters, citation/evidence records, or the required Mermaid architecture maps. Maps are visual indexes over authority, not authority themselves.

Before moving or deleting registered article material, inspect the article architecture map and preserve every protected rhetorical function and setup/payoff dependency unless Joel explicitly drops it. Do not register or import an article from a partial packet or remembered chat. Do not reconstruct a missing master from notes.

## Substack source and video boundary

For an existing Substack article, raw editor HTML controls links, hierarchy, captions, paywalls, native-object identity, metadata, and placement. Treat archival source fidelity, transfer conversion, and actual destination success as separate findings.

Owner-final 2026-08-17 video rule:

- **Standalone native Substack-uploaded video:** nonportable through the clipboard helper. Preserve the complete exact object in archival HTML; record identity/order/anchors; exclude its native markup from every clipboard payload; split the helper at its exact source position; provide ordered copy parts and a manual step to copy the original video directly from the Substack editor and insert it between the corresponding parts. Never claim transfer from a `Copied` state.
- **Substack video-post preview/card:** a distinct object type. Preserve the raw card in archival HTML; in transfer conversion replace the rendered card with its exact canonical Substack post URL alone at the same source position inside the current payload segment. Do not split solely because the card contains descendant `<video>` markup. Classify the enclosing `DigestPostEmbed` before descendant video tags.
- **YouTube:** a third independent object type; preserve and test its own established rich-HTML path. Never infer its behavior from either Substack-specific video type.

Use the current publishing protocol and compatibility profile for all other object types.

## Delivery and reporting

Preserve claims/certainty, exact memories/quotations, actors, chronology, causality, links, media, headings, native-object placement, and severe-claim agency.

By default deliver working prose as Markdown/text unless Joel explicitly requests HTML or another publication artifact. Do not render or offer long HTML previews; provide files/download links for HTML/web deliverables.

After substantive passes report, at the level relevant to the task: heading fit; semantic sanity; reality check; architecture; curious-reader chain; cold-audit passes; source weighting; paragraph chain; coherence/fidelity; provenance; source span; omissions; claim changes; stopping point; detector role; largest remaining weakness; and next task advanced.

Save durable working task architectures, protocol improvements, and reusable tooling repairs in GitHub so later chats do not need to relearn them.
