# Joel Articles agent map

## Authority

1. Current owner instructions and the article-specific acceptance criteria
2. `articles/INDEX.json` for registered article authority and exact hashes
3. `docs/INDEX.md` and the registered article's current-state read order
4. The registered master, owner-lock manifest, and exact source evidence
5. Exact citation/editorial/detector records and Git history
6. Relevant current patterns from `u-dont-existDOTcom/universal-dev-architecture`

This repository is active and currently registers Romance, Somatic Therapies, Inner Child Therapy, Inner Signal, and Nibbāna as working canonical articles. Do not substitute historical branches, chat reconstruction, detached packets, or filenames for a registered article family.

## Recovery before editing

Read `state/CODEX-CURRENT-STATE.md`, `articles/INDEX.json`, and the target article's registered current state before changing prose. Verify every registered SHA-256 first. If the registry is empty, stop content editing: governance work may continue, but no article master may be inferred from chat, filenames, summaries, or an external packet.

## Validation

- Unit and policy regressions: `python -m unittest discover -s tests`
- Authority, hash, privacy, and export checks: `python scripts/validate_content_repository.py --root .`
- Repository and workflow audit: `python scripts/audit_codex_github.py --root . --fail-on error`
- Patch hygiene: `git diff --check`

The validator proves registered structure and hashes, not article truth or editorial quality. Run the registered article's semantic, source, citation, detector, publication, and lesson-closeout checks in addition.

## Workflow

Use one article-scoped task branch/worktree and a pull request. Keep owner-final prose, reconstruction state, source evidence, detector experiments, and promoted lessons distinguishable. Persist decisions and recovery state in Git before ending a substantive pass.

When parallel chats/agents may touch the same article task, the article task branch becomes an integration branch, not a shared writer branch. Before any mutation, check the target article for an active `PARALLEL-WRITE-LOCK.json`; if present, each writer must use a unique child branch/worktree with its own writer lease and only the designated integrator may mutate the integration branch. Follow the fresh universal `patterns/parallel-chat-write-isolation.md` rule. Unexpected branch advancement fails closed and must be reconciled explicitly.

For P2S/P3/P4 humanization, D3/D4 reconstruction, or detector-driven semantic edits, `docs/HUMANIZATION-PRESERVATION-GATE.md` is blocking **before detector submission**. Freeze the authoritative changed scope, enumerate preservation units and the authorized-change whitelist before drafting, then require bidirectional source↔candidate traceability with **zero unexplained substantive deltas**. Re-run that proof after every detector-driven semantic edit. A detector-green candidate that fails preservation is fidelity-rejected and cannot be promoted.

For humanization/detector work, `docs/HUMANIZATION-ARCHITECTURE-GATE.md` is also blocking: re-run the article-wide architecture regression after every detector-driven edit. Do not narrow the editorial field of view to the last detector window.

**One set of humanization rules for every article (Joel, 2026-09-30).** Any humanization or detector-driven pass, in any chat, on any article, runs the same shared rules. That covers registered articles, unregistered ones, experiments, and work that uses Emulate. The rules are the gates in `docs/INDEX.md` and the working gate `docs/HUMANIZATION-GATE.md` with its tools.
- A chat, lane, experiment or directive may add owner rulings for its own article, in that article's folder. It may not replace, weaken or skip the shared rules.
- A lesson that applies beyond one article goes into the shared files in the same turn, not into a chat's own file.
- The order: the system first (sense, preservation, fresh writers, the linter and tell ledger, the reviewer-writer loop), then Pangram as the outside check. Emulate goes first on the flagged paragraphs of a published article being humanized, and only after the reviewer-writer loop has failed on new writing (Joel, 2026-09-30; `docs/EMULATE-FALLBACK.md`).
- Pangram and Emulate stay fallbacks until the system is shown to be enough on its own.

Use `docs/EDITORIAL-SCOPE-AND-PLACEMENT.md` when deciding where protected invitation/de-escalation language belongs or when an owner-approved AI/synthetic draft carries useful thought architecture. Protected function and correct placement are separate judgments.

## Reader-facing realization gate

Owner interviews, chat answers, editorial explanations, and research notes are **source pools, not publication transcripts**. Exact owner wording can be authoritative as thought without being publication-ready as a sentence.

Before reusing source-pool wording verbatim, test it in its literal article location:

- Does the first sentence make sense to a reader who never saw the private conversation?
- Are every `this`, `that`, `it`, `here`, `earlier`, `what I mean`, and named concept anchored by visible article context?
- Is the sentence explaining something to the reader, or explaining to the editor/model why the material matters?
- Does a heading open by fulfilling its public-facing promise rather than continuing a private-chat thought?
- Is a technical or article-specific term introduced before the prose refers back to it?

If a source sentence contains editor-facing rationale (`this is important because it connects with my other articles`), private conversational deixis, an undefined referent, or a continuation that only made sense in the interview, **recover the thought and rewrite it as self-contained reader-facing prose**. Preserve meaning/provenance; do not preserve the conversational wrapper merely because the words came directly from Joel.

Apply this check especially to the **first paragraph under every heading** and every paragraph created by moving source material to a new location. A preservation-clean sentence can still fail publication flow if its antecedent disappeared.

## Research-process compression gate

By default, publish the best current conclusion—not the backstage sequence by which it was reached.

Do not automatically convert research notes such as `I thought X`, `I had heard Y`, `I checked it`, `I wasn't sure what the term was`, or `the check I did here showed...` into article narration. Collapse them to the reader-relevant result, including uncertainty or evidence limits where needed.

Keep the inquiry/correction process only when **the process itself performs a real article function**: for example, the article is explicitly methodological, the change of mind is evidence for the argument, the original misconception is common and worth correcting, or the provenance of the uncertainty materially matters. Otherwise, research workflow is source metadata, not prose.

## Method fit and switching

For every substantive or iterative task, apply the strategy fit and efficacy rule in `u-dont-existDOTcom/universal-dev-architecture`, `patterns/reasoning-selection.md` (Universal core). Before you choose or build a method, say what the task has to decide or produce, and pick the capability that fits it: a model reads and judges language, meaning, tone and intent; code computes exact, structural and repeatable things; a test or a measurement (Pangram, here) answers what can be observed. Don't build a brittle stand-in for a capability you already have. Judge progress by the owner's outcome, not by the work done. When the same kind of fix keeps being needed, attempts fail the same way, or the outcome stays flat, say why and switch to a causally different approach, not the same one renamed. Report a lack of progress yourself and keep going; ask Joel early, and only for decisions or knowledge that are his.

Joel asked for this as a universal rule (2026-10-09 05:02 UTC: "the MC rule should have been a UDA rule actually. so fix that. and it's not specific to this exact case."). The cases that led to it, all from the community lane:
- Checks that judge text. The linter's abstract-agent check matched a word list of abstract nouns; he called the list brittle ("abstract nouns are a real vast open-ended list in my mind"). It became a parser and a dictionary lookup, another list in effect, until he asked: "why can't you simply look at a word and know it's an abstract concept, isn't that what LLMs are great at?" (2026-10-07). Now the parser only finds candidates and a fresh model judges them against his ratings (`tools/humanization/abstract_agents_prompt.py`). Before you write or extend anything that decides something about text, apply the pattern-matching fit check in the same UDA file: lists and patterns fit exact questions (a fixed string, a count, a hash, a heading's place); meaning goes to a model; a list at most lists candidates for it.
- The unit of testing. In section 9 a paragraph read AI as part of a five-paragraph group in six wordings in a row; the whole section with it in read 100% Human (2026-10-09). The section and each paragraph are the test (`docs/HUMANIZATION-GATE.md`); a seventh wording of the group would not have helped.
- Reasoning only Joel has. When every faithful wording of a group had failed, he rewrote its reasoning links himself in minutes (2026-10-09). Ask him as soon as the first method is spent, with the page.

## Code review rules

- Never silently soften, balance, or change the owner's argument. Disagreement must be raised directly rather than hidden in an edit.
- Treat significance-staging constructions such as `That’s where X matters to me` / `That's where X matters to me`, `This is one reason I want X`, `The version I want is X`, `What matters to me is X`, and close syntactic variants as AI-shaped in Joel-byline prose when they merely announce the author's preference or importance before a general recommendation, consequence, or argument. State the concrete consequence, recommendation, distinction, or judgment directly. First-person preference remains legitimate when Joel's personal preference itself is the subject, or when the surrounding passage is explicitly about what he wants for himself or for a named relationship. Quotation or literal discussion of the construction is exempt.
- Treat `boring`, `quietly`, and `ordinary` as **AI-frequency-risk words in Joel-byline prose, not absolute bans**. Models overuse them as generic texture, understatement, or significance cues. Use one only when it is the most exact word for the actual thing being described; flag repeated, ornamental, or easily replaceable uses and prefer the concrete observation instead. Do not mechanically replace an owner-authored use that is precise or distinctive. Owner choices such as `low-key` or `surreptitiously` should be preserved when they are more exact in context; do not normalize them back to model-frequent understatement.
- Preserve every unique claim, step, joke, protected rhetorical function, and owner-final passage unless a proposed cut has explicit owner approval or genuine semantic equivalence.
- Treat deletions and consolidations as explicit proposals. Record the original text and destination or owner approval so the change is reversible; do not silently discard apparently redundant material.
- For substantial rewrites, every protected source unit must have a candidate mapping or an already-authorized non-preservation disposition, and every substantive candidate delta must map back to the change whitelist or owner authority. `Inferable`, `redundant`, `smoother`, and `better for Pangram` are never sufficient deletion authority.
- Owner-lock manifests contain exact protected passages. A passing hash check is necessary but not sufficient: review the master article-wide for function, sequence, agency, and meaning preservation.
- Keep claim-level source provenance local. Mark unsupported, inaccessible, disputed, or owner-only claims precisely; never fabricate a citation or flatten the author's position to make sourcing easier.
- During a requested editing or humanization pass, do not turn the task into unsolicited fact-checking or claim review. Research/verify when Joel asks, or flag a claim only when there is a concrete material reason under the article protocol; empirical or contestable language alone is not such a reason.
- Detector results are evidence, not editorial authority; passing a detector never licenses distortion of meaning or voice.
- A 100% Human detector result is still invalid if preservation proof, heading promise, paragraph jobs, live-question continuity, owner-realization placement, protected functions, or fidelity fail.
- A verbatim owner sentence is still invalid in publication prose if it depends on private-chat context, addresses the editor/model instead of the reader, contains an undefined antecedent, or fails its heading/paragraph job. Owner authority protects the thought; it does not waive reader-facing coherence.
- A factual/research correction should normally appear as the corrected claim, not as a diary of `I thought → I checked → I learned`, unless that epistemic sequence has an independent reader-facing purpose.

Treat chat as disposable working memory. A fresh worker must recover the correct article state, constraints, and next action from Git.

## Stop conditions

Stop and obtain an owner decision before choosing a copyright/license posture, selecting between competing canonical masters, making substantive prose changes without a registered authority package, publishing/exporting, or releasing source material that contains credentials, private third-party data, or material explicitly marked private/confidential. Joel's own working material is public-GitHub-eligible by default under `SKILL.md`; that default does not authorize external publication or override independent privacy obligations.

## Suggested fixes from other projects

Before starting other fixes here, read this repository's lane in `u-dont-existDOTcom/universal-dev-architecture`: `suggested-fixes/joel-articles/` on its default branch. Handle each item that `docs/suggested-fixes-ledger.md` doesn't list yet, along with your other work. You can adopt it, adapt it, decline it with a reason, defer it until a named trigger, or ask the owner on your owner questions page. Record the outcome in that ledger, creating the file if needed. Items are advice, and this repository's own authority decides; an item marked as an owner request goes to the owner before you decline or defer it. The method is `patterns/suggested-fix-queue.md` in that repository.
