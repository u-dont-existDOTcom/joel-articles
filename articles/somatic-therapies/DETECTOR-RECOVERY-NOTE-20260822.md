# Somatic Therapies detector recovery note — 2026-08-22

This note records why detector state was corrected without changing article prose.

- The registered `r01-candidate` had already been submitted to Pangram 4 through the trusted fixed-batch/private-executor route before the article-local detector ledger was updated.
- Recovery found the completed exact r01 cache record rather than repeating the paid request.
- The result was AI `0.9776151180267334`, Human `0.02238490805029869`, AI-assisted `0.0`, with two High-confidence AI windows and one short Human segment.
- Five subsequent intro probes were also already completed and each returned AI `1.0`; they are experiments, not article authority.
- One of those probes (`r07`) added first-person material for which no owner provenance was recovered, so it is explicitly barred from promotion into the article.
- A 270-word natural-owner research-conversational control returned Human `1.0`, High confidence, so current evidence does not support dismissing the Somatic result as a generic health/research-genre failure.
- The remaining intro audit budget is one new paid call. It should be used only for a materially different, source-grounded realization, not another conversational paraphrase.

Canonical raw detector evidence remains in `u-dont-existDOTcom/pangram-humanization-lab` on `automation/pangram-fixed-batch`; this note is a recovery/decision record only.
