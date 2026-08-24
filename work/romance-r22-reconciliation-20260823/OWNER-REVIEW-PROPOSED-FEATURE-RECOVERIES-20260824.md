# Romance r22 proposed feature recoveries — owner review — 2026-08-24

Status: **owner reconciliation has advanced to the five-feature r23 continuation candidate. Registered Romance article bytes remain unchanged. No detector call has been made on r23.**

## Baseline

- Leading known-green baseline: exact r22 Markdown SHA-256 `f0f9a47eba2ac9ab1a56bdd6793316d41e7c23072b0b0c030285caf5e12f83c9`.
- r22 Part 1 SHA-256 `5ed333800b9ae7b402f26aa03e751ef8296c7e27ab70e39bc39bb9896b23e62d`: Pangram 4.0 Human `1.0`, zero AI windows.
- retained r22 Part 2 SHA-256 `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`: Pangram 4.0 Human `1.0`.
- Registered `main:articles/romance/master.md` remains unchanged.

## Owner review source

Joel returned the review DOCX `Romance_r22_proposed_reverts_redline(1).docx` with inline owner corrections and objections. Those direct corrections outrank the earlier feature-deficit recommendations.

Joel then corrected the reconciliation method itself: do not blindly recover wording from the older version. Check whether the **function** is already realized elsewhere in the complete current section, and recover only the genuinely missing remainder. After that function-first re-audit, Joel approved continuing with the narrowed r23 work.

## Current r23 continuation set — five editorial features / six exact operations

1. **Talk about making love before you do it** — prospective libido-divergence planning in Joel's edited form: `If our libidos later diverge, it's better to talk about what we'd do before either person is already hurt.`
2. **Affection and the simmer** — Joel's edited realization adds the taking-each-other-for-granted / five-years-ago point and anti-homework joke. The separate changed-sex-life sentence adds the `new normal` warning and `one of us doesn't feel wanted` variable. Mechanical correction accepted in the materialized candidate: `keep some curiosity about why` rather than `into why`.
3. **Can making love be a spiritual practice?** — clearer student-report attribution plus Joel's jade-egg training relation. Mechanical correction accepted in the materialized candidate: `preliminary training for the cervical O`.
4. **Two Pillars Don't Hold The Roof Up** — recover only the one genuinely missing mutual-friend function. Joel's exact preferred sentence: `But sometimes a friend who actually knows us both sees the pattern before either of us does.` The older three-sentence generic block remains rejected.
5. **What are you actually choosing together?** — use the stronger image `I can hear a whole future in those two words—...` in place of `I might hear...`.

The frozen exact old/new spans and hashes are in `R23-FIVE-OWNER-EDITS-MANIFEST.json`. The six operations are `R23-01`, `R23-02A`, `R23-02B`, `R23-03`, `R23-04`, and `R23-05`.

## Closed after function-first re-audit as already covered in r22

These were not rejected because their ideas are bad. They were removed because the current article already performs their functions, often more concretely:

- **If slow isn't realistic for you** — drop `while we figure out what this actually is`; the section already opens with waiting long enough to `figure out who I'm dealing with` and later distinguishes wanting someone from knowing whether to build a life with them.
- **Muses & Directors** — drop `I also feel useful as the one who translates the poetry into function...`; r22 already says `I help give it direction and make it operational` and later has the Big Picture → workable-plan realization.
- **Psychedelics in relationship discernment** — drop the added sober stress-test list; the next paragraph already says to spend time sober in ordinary situations, and the immediately preceding Imagination section already develops money, jealousy, conflict, children, and future-life stress tests.

## Rejected proposals

- **Two Pillars — old three-sentence block** — two of its three functions are already realized more concretely through the B. and H. material. Restoring the whole block would duplicate them. Joel also reported the exact generic wording as detector-AI. Only the missing pattern-seeing function survives, in Joel's one-sentence wording above.
- **Attraction and exclusivity** — reject the history-to-modern-vow bridge. Joel's disposition: `it's just junk model explanatory prose.`
- **If you're already in it** — reject the `stay in the conversation` diagnostic. Joel's disposition: it is over-explaining. Keep the owner-final dance paragraph without it.

## Process correction — function-first reconciliation, not sentence recovery

The prior comparison method was too close to blind copying: it surfaced things the older wording did well and proposed recovering them without first checking whether the **same rhetorical/semantic function had already been re-realized elsewhere in the current section**.

From this point forward, every older→current feature comparison must use this order:

1. **Decompose the old passage into functions, not sentences.** Name each distinct claim, example, qualification, joke, transition, evidence role, diagnostic, setup/payoff, or reader-facing move separately.
2. **Search the complete current natural section for each function.** Check neighboring paragraphs and, when the function is article-wide or deliberately relocated, the relevant adjacent/linked sections too. Do not rely on phrase matching; a function may survive in completely different wording or inside a concrete story.
3. **Classify current coverage:** `absent`, `partial`, `equivalent`, or `stronger/more concrete`. Quote the current realization that carries the function when it exists.
4. **Propose only the unresolved remainder.** If two of three old functions already survive, do not paste back all three. Recover only the missing third function, and prefer the smallest realization that fits the current thought movement.
5. **Re-read the literal resulting paragraph and complete natural section.** Check for repeated conclusions, duplicated explanation, broken sequencing, abrupt insertion, and whether the proposed sentence answers a live reader question rather than merely summarizing what the section already demonstrated.
6. **Check durable detector history before proposing exact old wording into a known-green boundary.** Detector history does not decide editorial value, but known-red/AI wording cannot be presented as an uncomplicated verbatim restoration when a green realization already exists.
7. **Only then present the owner choice.** The review should show the old function, where it is already carried now, the genuinely missing remainder, the proposed integration, and the detector implication of changing the bytes.

The `Two Pillars` correction is the concrete example: the old three-sentence block contained three functions; r22 already carried two through lived material, leaving only `a mutual friend may see a pattern neither partner sees`. The correct recovery is therefore one sentence, not the old block.

Separately, every proposed integration must be cold-read as literal surrounding prose before delivery. The earlier Psychedelics proposal demonstrated a flow failure caused by inserting a sentence without re-reading the resulting paragraph as a paragraph.

This correction supplements the known-green rule: detector history is evidence, not editorial authority; semantic/editorial quality still comes first, but detector evidence already paid for and preserved must not be ignored when proposing an exact rollback.

## Current materialization state

The four exact changed natural boundaries are now materialized and read back byte-exact on this branch under `r23-boundary-candidates/`. `boundary-manifest.json` records SHA-256, Git blob identities, word counts, authorized operations, and readback proof. `R23-BOUNDARY-COLD-READ-20260824.md` records the literal boundary cold audit; all four pass with zero unexplained substantive deltas.

The complete 20k-word r23 master and its exact Part 1 / Part 2 certification boundaries have **not** yet been assembled in this connector-only runtime. Therefore r23 detector status remains **UNMEASURED**. Do not spend section-level detector calls and mistake them for certification of the resulting halves; Romance has demonstrated composition sensitivity.

## Next state

Use the five-feature/six-operation r23 whitelist above. The three functionally redundant proposals and three rejected proposal families are closed unless Joel explicitly reopens them. The next technical step is exact full r23 assembly from r22 plus the frozen six operations, followed by readback/preservation proof and composition-aware Part 1 / Part 2 detector certification if current Pangram cache/ledger/credit state permits. Do not alter registered `main:articles/romance/master.md` until that reconciliation is deliberately promoted.
