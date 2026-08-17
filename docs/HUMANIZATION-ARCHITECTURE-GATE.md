# Humanization architecture gate

Humanization does not suspend ordinary article-level editorial reasoning. Pangram and other detectors are secondary evidence about a candidate, not a substitute for deciding what the section is supposed to do.

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
- fidelity against the highest-authority baseline, including lines that appear inferable or redundant.

A local detector-red span can be a symptom of wrong routing or duplicate realization rather than bad syntax. Search article-wide before paraphrasing locally.

A **100% Human** detector result is still editorially invalid if this architecture regression fails. Detector green cannot repair a broken heading promise, paragraph chain, lost protected function, displaced owner thought, or fidelity loss.

## Idiolect preservation after detector edits

Run `IDIOLECT-PRESERVATION.md` alongside this regression for Joel-byline humanization. A detector-driven repair must not needlessly normalize real Joel-specific word choice, contractions, function-word patterns, punctuation, sentence joins, rhythm, uneven emphasis, register, or visible thought movement merely to improve Pangram.

Prefer the minimum transformation that fixes the diagnosed problem. A generic `preserve voice` instruction is not evidence that the output preserved voice, and a Pangram pass does not prove that the prose remains distinguishably Joel-like.

The quantitative authorship layer remains provisional until `u-dont-existDOTcom/pangram-humanization-lab/docs/IDIOLECT-PRESERVATION-PROTOCOL.md` has a validated Joel-specific baseline, held-out source splits, topic/content controls, and register handling. Until then, apply the guard qualitatively through source provenance, minimum edit dose, the voice reference, architecture, and cold audit.

## Provenance

The architecture rule was promoted from the 2026-08-14 Spiritual Bypassing incident. A reader-visible article reached 100% Human while its first section no longer fulfilled `A Primer on Spiritual Bypassing`. The successful repair came from recovering an existing Joel realization elsewhere in the article and routing it into the primer rather than continuing to paraphrase detector windows. A later cold audit also restored an inherited line that detector-focused editing had silently dropped.

The idiolect guard was added from Malik and Awan's 2026 Idiolect Erasure Rate research, which showed that semantically similar AI rewrites can materially weaken computational authorship signals and that explicit voice-preservation prompting does not by itself preserve deep authorship signal.

Exact detector evidence and the IER adaptation protocol remain canonical in `u-dont-existDOTcom/pangram-humanization-lab`.
