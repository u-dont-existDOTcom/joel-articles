# Humanization architecture gate

Humanization does not suspend ordinary article-level editorial reasoning. Pangram and other detectors are secondary evidence about a candidate, not a substitute for deciding what the section is supposed to do.

## Preservation proof comes first

For substantive P2S/P3/P4 reconstruction or detector-driven semantic edits, `HUMANIZATION-PRESERVATION-GATE.md` is blocking before detector submission. The worker must freeze the changed-scope preservation units and authorized-change whitelist before drafting, then prove bidirectional source↔candidate traceability with **zero unexplained substantive deltas**. A detector-green candidate that fails that proof is fidelity-rejected.

Architecture review is a separate gate. Preservation can pass while the candidate is badly routed or model-shaped; architecture can look good while a claim or provenance unit was silently lost. Both must pass.

## Required three-scale editorial ledger

For any substantial sectional or article-wide humanization/reconstruction, the worker must maintain a concrete editorial ledger at three scales. A Mermaid map, preservation receipt, or statement that the architecture was checked does **not** substitute for this ledger.

1. **Global/article scale:** record the article's governing movement and the job of every consequential section, including the primary home of recurring ideas. For every recurring idea, distinguish `setup`, `primary exposition`, `application`, `payoff/callback`, and `true duplicate`. A repeated topic is not automatically redundant, but a second passage performing the same job must be consolidated, cut with authority, or justified explicitly.
2. **Section/subsection scale:** for each edited natural section, record the heading promise, entry state, exit state, subsection jobs, dependencies, and the exact reason for the current order. A subsection may not survive merely because its prose is good; it must perform a distinct job at that location.
3. **Paragraph scale:** record one job/live-question movement per paragraph in the changed natural boundary. Flag paragraphs that only recap, restate an inference, repeat a prior paragraph's function, answer a question already closed, depend on a missing antecedent, or end in an unfulfilled colon/list/setup.

Use the existing purposeful-recurrence, source–meaning–context–destination, dependency, and orphan controls in `../project-sources/EDIT-CONTRACT-AND-LEDGERS.md`; do not create a competing taxonomy when those controls already cover the problem.

After assembly, perform one literal top-to-bottom proofread of the complete natural boundary **without consulting detector windows**. This pass must check heading-level continuity, empty headings, unfinished bullets/lists/colons, dangling transitions, broken referents, orphaned examples, duplicated function, and whether each paragraph earns the next paragraph. Do not certify this from a section map alone.

The ledger is an editorial control surface, not an instruction to create a paragraph-by-paragraph Mermaid mega-graph. Keep the Mermaid map at the useful structural level and use the ledger for finer-grained proof.

## Blocking architecture regression

Before the first detector call and **after every detector-driven edit**, re-read from the article-wide architecture rather than the latest detector window. Check:

- article title vs section heading vs subheading identity;
- the heading promise and whether the section fulfills it;
- paragraph jobs and whether each paragraph changes the reader's state or live question;
- the curious-reader chain / live question;
- actor → action → object, mechanism, chronology, and causality;
- protected rhetorical functions, owner-final claims, and severe-claim agency;
- article-wide duplication, misplaced evidence, and pre-completed reasoning;
- whether an existing owner realization elsewhere in the article/source pool belongs in the failing function before generating fresh explanatory prose or asking Joel again;
- real stopping point;
- fidelity against the highest-authority baseline, including lines that appear inferable or redundant;
- preservation-proof status for the exact candidate being considered, including any new substantive deltas introduced since the last proof;
- three-scale editorial-ledger status and the post-assembly literal proofread result.

A local detector-red span can be a symptom of wrong routing or duplicate realization rather than bad syntax. Search article-wide before paraphrasing locally.

A **100% Human** detector result is still editorially invalid if preservation proof or this architecture regression fails. Detector green cannot repair an unexplained semantic delta, broken heading promise, paragraph chain, lost protected function, displaced owner thought, or fidelity loss.

## Authorship-signal regression

For `D3` sectional reconstruction and `D4` article-wide regeneration, also apply `../project-sources/IDIOLECT-PRESERVATION-PROTOCOL.md`. Compare the authoritative original and candidate with a held-out, genre-relevant corpus only after corpus provenance and target voice are explicit. Narrow `D1` correction and ordinary `D2` local repair do not automatically require measurement.

Keep four results separate:

1. semantic/editorial fidelity and preservation proof;
2. article architecture/coherence;
3. exact-boundary detector status;
4. authorship-signal retention under a named instrument and corpus.

A preserve-voice prompt is not validation. Pangram Human does not prove Joel's idiolect survived. A higher profile-similarity score does not prove fidelity, authorship, or quality. Do not impose a universal threshold or manufacture errors, memories, catchphrases, fake specificity, unusual punctuation, or corpus tics to improve the measurement. When a substantial rewrite drifts, first restore owner wording or thought routes, reduce the edit dose, or localize the repair.

## Provenance

The architecture rule was promoted from the 2026-08-14 Spiritual Bypassing incident. A reader-visible article reached 100% Human while its first section no longer fulfilled `A Primer on Spiritual Bypassing`. The successful repair came from recovering an existing Joel realization elsewhere in the article and routing it into the primer rather than continuing to paraphrase detector windows. A later cold audit also restored an inherited line that detector-focused editing had silently dropped.

The preservation-proof layer was added after repeated Romance repairs showed a second failure mode: the worker could catch its own semantic/provenance losses only after generating or even submitting the candidate. The new gate moves traceability and authorized-delta checking before detector eligibility.

The three-scale ledger and literal proofread requirement were added after Joel's 2026-08-27 manual Romance cleanup exposed a third failure mode: section-level architecture and preservation checks could pass while repeated functions, empty headings, and an unfinished paragraph-level setup survived. The repair composes the repository's existing architecture map, purposeful-recurrence ledger, paragraph-job check, dependency audit, and orphan audit rather than inventing a parallel framework.

The authorship-signal layer is grounded in Malik and Awan's 2026 Idiolect Erasure Rate study and the implementation/limitations recorded in `u-dont-existDOTcom/pangram-humanization-lab`.

Exact detector evidence and case-specific incident records remain canonical in `u-dont-existDOTcom/pangram-humanization-lab` and article task branches.
