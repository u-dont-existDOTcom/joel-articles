# Idiolect validation status

Status: **operational directional proxy; research-grade Joel-register calibration pending.**

The canonical editorial protocol remains `../project-sources/IDIOLECT-PRESERVATION-PROTOCOL.md`. Do not replace or duplicate it.

## Current operational state

For D3 sectional reconstruction and D4 article-wide rewriting, the Pangram lab now provides a dependency-free `idiolect-retention` comparison alongside its closed-set local `idiolect-ier` research command.

Those tools are useful immediately under the limits already stated in the canonical protocol:

- semantic/editorial fidelity, article architecture, Pangram status, and authorship-signal retention remain separate results;
- the single-author command is a directional retention proxy, not IER;
- no universal profile-similarity threshold exists;
- owner authority and fidelity outrank the metric;
- workers must not insert errors, fake specificity, memories, catchphrases, slang, unusual punctuation, or corpus tics to improve a score.

## What is not yet established

The fast local proxy has not yet been validated for Joel's distinct writing registers against the paper's stronger attribution setup.

In particular, no durable evidence yet establishes:

- paper-faithful TF-IDF character 2–4 + word 1–2 linear-SVM baseline accuracy on a Joel/control-author corpus;
- LUAR held-out authorship attribution for Joel;
- topic-matched negative authors sufficient to separate subject matter from style;
- register-specific proxy agreement for research-conversational, practical, personal/tender, or polemical prose;
- a held-out calibration showing that any numeric local-proxy threshold is justified.

Therefore the routine result remains **directional evidence only**.

## Cross-repository authority

Research-grade calibration belongs in `u-dont-existDOTcom/pangram-humanization-lab`:

- `docs/IDIOLECT-RETENTION-PROTOCOL.md` — current operational proxy and local closed-set IER contract;
- `docs/IDIOLECT-VALIDATION-PROTOCOL.md` — Tier-A/Tier-B validation architecture, including surface SVM, LUAR, topic/content controls, register stratification, and disagreement handling;
- `state/IDIOLECT-PROXY-VALIDATION-GAP-2026-08-17.md` — exact current evidence gap.

`joel-articles` continues to own editorial authority, edit-dose decisions, source/corpus provenance policy, article acceptance, and the rule that no metric can silently alter Joel's argument.

## Live-use rule

Before treating an idiolect-retention result as more than a directional diagnostic, check whether the Pangram lab records `validated-for-register` status for the relevant register and instrument version.

If it does not, report:

> `Idiolect retention: directional proxy only; research-grade calibration for this register is not yet established.`

If the fast proxy later disagrees materially with a research-grade instrument, do not average the scores and do not optimize the prose toward either one. Treat authorship measurement as inconclusive, preserve the counterexample in the lab, and return to owner authority, semantic fidelity, article architecture, and the minimum coherent edit.
