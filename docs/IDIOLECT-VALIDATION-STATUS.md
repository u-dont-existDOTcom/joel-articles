# Idiolect validation status

Status: **operational directional proxy; Tier-B LUAR evidence exists, but no Joel register is validated. Exact-50 unique-Joel attribution is disconfirmed for the current matched-Dharma condition.**

The canonical editorial protocol remains `../project-sources/IDIOLECT-PRESERVATION-PROTOCOL.md`. Do not replace or duplicate it.

## Current operational state

For D3 sectional reconstruction and D4 article-wide rewriting, the Pangram lab provides the dependency-free `idiolect-retention` comparison alongside closed-set research tooling.

Those tools remain useful under the canonical limits:

- semantic/editorial fidelity, article architecture, Pangram status, and authorship-signal retention are separate results;
- the single-author command is a directional retention proxy, not IER;
- no universal profile-similarity or margin threshold exists;
- owner authority and fidelity outrank the metric;
- workers must not insert errors, fake specificity, memories, catchphrases, slang, unusual punctuation, or corpus tics to improve a score.

### Production stop rule

Closed-set LUAR/SVM/IER calibration is **research tooling, not a routine humanization stage**. Do not launch a new multi-author attribution experiment, recruit additional comparison authors, or expand a calibration corpus merely to decide whether current Joel-byline prose is acceptable.

The default production path is meaning/architecture → minimum coherent edit → cold review → Pangram under its own boundary rules. Idiolect evidence may be consulted when already available and genuinely decision-relevant, but an unvalidated instrument must not create another repair loop.

The dependency-free single-author proxy is also optional rather than blocking. Use it only when it is cheap, the comparison boundary is meaningful, the reference corpus is relevant, and the result could change a real editorial decision. Otherwise record that no validated retention gate is available and proceed under owner authority, fidelity, architecture, and detector evidence.

A new LUAR or other Tier-B run requires an explicit research purpose or a predeclared calibration question whose answer would materially improve the reusable humanization system. Once a condition is shown too unstable to be operational, stop trying to rescue it with more controls, shorter windows, or article-specific experiments.

## Tier-B evidence now available

The earlier statement that no durable LUAR or topic-matched control-author evidence existed is obsolete.

The Pangram lab now contains frozen, source-hash-conditioned LUAR evidence using the pinned `rrivera1849/LUAR-MUD` model and topic/platform-matched Dharma Connection controls. Stian Gudmundsen Høiland is explicitly treated as Joel's owner-identified hard negative rather than an arbitrary control; David Vardy and Greg Goode are ordinary matched controls.

The current decisive exact-50 result is:

- candidate set: Joel / Stian / David / Greg;
- each evaluated target boundary: exactly 50 original words;
- primary matched-Dharma stratum: Joel top-ranked on **2 of 4** natural Joel originals;
- the two errors went to **Stian once and Greg once**;
- therefore exact-50 LUAR is **not reliable enough to serve as an operational unique-Joel retention gate** for this named matched-Dharma condition.

That result is frozen in Pangram lab at:

`state/IDIOLECT-FOUR-AUTHOR-TARGET-VERIFICATION-RESULT-2026-08-19.json`

The same experiment preserved a separate independent-TAFKA sensitivity stratum: two of two held-out Joel originals ranked Joel first. This is positive evidence, but it is too small and changes platform/register relative to the control profiles. It must **not** be averaged with the matched-Dharma result or used to declare exact-50 validation.

Earlier three-author whole-document LUAR evidence was more promising: Joel was top-ranked on 3 of 4 held-out whole documents. That sample was small and shared-thread/candidate-set limited. It does not establish a validated longer-boundary condition.

## Consequences for interpretation

The research now supports several narrower conclusions:

1. **Fifty words is not a validated sweet spot.** It was previously only a lower weak-evidence boundary. The matched four-author experiment now directly disconfirms unique-Joel exact-50 attribution for its named condition.
2. **A Joel → Stian nearest-author flip is not, by itself, idiolect erasure.** Stian is a genuine hard negative, and the current four-author result also shows ambiguity beyond Stian: Greg wins one natural Joel target, while David can outrank Joel without becoming the top prediction.
3. **Joel-only similarity still cannot certify retention.** A candidate can move closer to Joel while moving as much or more toward plausible alternatives.
4. **Short-text candidate-set geometry is instrument/corpus specific.** The current profile cosine matrix does not establish a general real-world “Joel–Stian neighborhood”; in one frozen profile set Stian–David similarity is higher than Joel–Stian similarity.
5. **No register is `validated-for-register`.** The routine proxy therefore remains directional evidence only.

## Live-use rule

Do **not** use a 50-word LUAR unique-author result as an acceptance gate for Joel prose under the current evidence, and do not run LUAR merely because a rewrite is substantial.

If an existing authorship-retention result is relevant to a real editorial choice:

- prefer the longest coherent reader-visible boundary that matches the editorial unit actually changed, rather than shrinking to a 50-word test window;
- use a register-relevant held-out corpus when one is already available;
- report model/instrument, corpus identity, original baseline, candidate movement, competing-author evidence, and limitations;
- if no longer/register-matched condition has been separately validated, continue to label the result directional rather than converting it into a pass/fail threshold.

The appropriate default report remains:

> `Idiolect retention: directional evidence only; no validated-for-register operational threshold is currently established.`

A 50-word result may still be recorded as a diagnostic, especially for research, but it must not override a larger coherent boundary, owner judgment, semantic fidelity, or article architecture.

## Cross-repository authority

Research-grade calibration belongs in `u-dont-existDOTcom/pangram-humanization-lab`. Current relevant evidence includes:

- `docs/IDIOLECT-RETENTION-PROTOCOL.md` — operational proxy and local closed-set research contract;
- `docs/IDIOLECT-VALIDATION-PROTOCOL.md` — validation architecture, including surface SVM, LUAR, topic/content controls, register stratification, and disagreement handling;
- `state/IDIOLECT-SYNCHRONIZED-AUTHORSHIP-RESULT-2026-08-18.json` — frozen three-author synchronized baseline and content controls;
- `state/IDIOLECT-STIAN-NEAR-NEIGHBOR-CORRECTION-2026-08-18.md` — owner correction and hard-negative interpretation;
- `state/IDIOLECT-FOUR-AUTHOR-TARGET-VERIFICATION-RESULT-2026-08-19.json` — current four-author exact-50 target-verification result.

`joel-articles` continues to own editorial authority, edit-dose decisions, source/corpus provenance policy, article acceptance, and the rule that no metric can silently alter Joel's argument.

## Remaining calibration gap

The remaining question is no longer “does any LUAR evidence exist?” It is narrower:

- can substantially longer, coherent, register-matched Joel boundaries be attributed reliably enough for useful retention comparison;
- can that result reproduce across independent source groups and more than one small target set;
- how does the fast local proxy agree or disagree with that stronger evidence by register and edit dose.

These are research questions, not production prerequisites. Do not launch more short-text or Romance rewrite experiments merely to rescue exact-50 attribution. Future calibration should address the longer-boundary question only when there is a concrete reusable-research reason to do so.
