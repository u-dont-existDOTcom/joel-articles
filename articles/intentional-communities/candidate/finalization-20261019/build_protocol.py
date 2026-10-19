from pathlib import Path
import mistune, html, json, hashlib
B=Path(__file__).resolve().parent
s=(B/'EDITORIAL-DEDUP-EXECUTION-v0.1.md').read_text()
s=s.replace('# Structural deduplication and sequencing — execution draft v0.1','# Structural deduplication and sequencing — execution v0.2 candidate')
s=s.replace('Status: proposed shared workflow for owner review and a source-only replay; not evidence of improved editing performance.', 'Status: the v0.1 principles were accepted in Joel’s 2026-10-19 owner-review answers. This v0.2 candidate incorporates his scope, sequencing, visual-review and enforcement corrections and awaits final approval. Neither approval of the rules nor a passing package check establishes improved editing performance.')
s=s.replace('A paragraph containing one useful sentence need not survive whole.', 'When overcompletion may contain an independent claim or procedure—especially in a draft built from AI research—ask the owner about the intended scope, using the exact passage and a specific retain/condense/relocate choice. AI origin is not deletion authority. Keep that content while the question is unresolved; do not turn every obvious duplicate into a new approval request.\n\nA paragraph containing one useful sentence need not survive whole.')
s=s.replace('## 4. Implement the smallest wording change that completes the chosen edit', '''### Reader decisions, argument and conceptual order are different

Map what a reader needs to decide, and what each section enables. Distinguish (a) a prerequisite to understanding the next passage, (b) a prerequisite to taking an action, (c) an argument–counterargument or problem–antidote pair, and (d) an optional cross-reference. A conceptual list is not automatically a chapter sequence, and reading about an activity early does not authorize doing it before its stated prerequisites. Keep a distinctive, owner-identified reason to read visible rather than burying it beneath generic process detail.

When plausible routes compete, compare them on the actual audience, promise, decision progression, important adjacencies, reference burden and cognitive load. Use no invented numerical quality score. Resolve ordinary choices yourself; ask only when changing the audience, promise, position or scope would appropriate an authorial decision.

### Keep the visual outline synchronized with the literal text

For substantial resequencing advice or delivery, provide an interactive before/after diagram. It must show section and subsection purposes, meaningful dependencies, exact old/new locations, and the pros and cons of the selected route. Default to a readable overview; reveal connections when a section is selected instead of drawing every edge at once. Link a node to its actual text, not merely a remembered title.

Generate the heading tree from the current candidate and maintain editorial purposes alongside stable source IDs. After each assembly, check the diagram against the literal headings, parents and passage locations. The map describes the prose; it must not become an obsolete outline or a compulsory sentence-writing template. An operation comment belongs to the move/consolidation relation shared by both sites.

## 4. Implement the smallest wording change that completes the chosen edit''')
s=s.replace('Verify the delivered files themselves and give usable files, not repository navigation.', 'Verify the delivered files themselves and give usable files, not repository navigation. For this workflow, use the artifact-binding and delivery checks in `EDITORIAL-EXECUTION-ENFORCEMENT.md`. A successful fidelity or clipboard check cannot substitute for the explicit article-wide repetition and sequencing judgment.')
s=s.replace('The proposed workflow is unvalidated until the replay and owner scoring are complete;', 'The generalization of this workflow remains unvalidated until an appropriately isolated evaluation on other material;')
(B/'EDITORIAL-DEDUP-EXECUTION.md').write_text(s)
enforce='''# Editorial execution enforcement — implementation and limits

Status: implementation candidate for owner approval. The local gate and its service adapter are tested on the article package and deliberate failures. No new hosted service, global ChatGPT interception, managed Claude hook or protected-branch rule is claimed to be deployed.

## A failure diagnosis more precise than “execution failure”

The earlier passes show a chain of distinct problems. The exact original request allowed mergers while asking for restraint in wording. Repository rules already required global organization and primary homes for recurring ideas. Some retrievals displayed only prefixes; that is a possible exposure gap, not proof of what the model internally read. The delivered r02 still treated a three-way practice cluster as a two-way merger. Fidelity, word counts and derivative tests were reported without an equally specific remaining-duplication result. Those are observable scope and completion-evidence gaps. The retrospective explanation that preservation anxiety caused them remains an interpretation.

The repair therefore addresses different boundaries rather than adding another promise to “be a better editor.”

| Boundary | What changes | What this can actually establish |
|---|---|---|
| Task admission | Bind exact owner source, answer file, scope and source-specific constraints. | Prevent working against a different revision or an old answer set without detection. |
| Developmental reasoning | Read the whole article, inventory complete overlap clusters, compare reader routes and retain source/owner boundaries. | Produces inspectable editorial judgments; code cannot prove their quality. |
| Assembly | Keep stable IDs, exact edit chains, native islands and link counts; rebuild the heading tree from the candidate. | Detect missing blocks, undocumented changes, lost media, stale outlines and violated declared ordering. |
| Reader review | Keep full-read evidence and any subsequent delta rechecks bound to the exact versions reviewed. | Establishes what was reviewed and by which available route, not correctness or independent identity. |
| Artifact delivery | `editorial_gate.py package` runs the gate and refuses a mismatched or incomplete bundle before writing the ZIP. | The tested packaging route cannot silently produce the marked review package after those failures. Unrelated routes remain outside it. |
| Service-side finalization | `RegisteredService` resolves the server-enrolled task and contract, accepting only task ID and expected candidate hash. | Rejects client-supplied PASS/approval fields, paths, unknown tasks, stale enrollment and stale candidates. It uses the same gate as local packaging. |

## What the gate checks

The candidate must match its source/owner binding; every source top-level block must survive exactly once or have an exact authorized omission disposition; the candidate must equal the literal ledger assembly; each changed block must have an exact before→after edit chain. Whole-block consolidation/deletion is supported when its exact source ID, reason, authority reference and semantic-review disposition are recorded. Empty spacers can be verified mechanically. Current r03 uses no whole-block omissions; this is not a general command to preserve inherited paragraphs. Native source objects remain byte-identical, while their intentional new positions are tracked. The ordinary link destination multiset is unchanged.

The diagram must include every real heading in order, with the correct level and parent. Every heading has an editorial purpose and reader question. Source-specific hard constraints are data, not universal title rules: for this article, Founderism and Movement remain adjacent, readiness and membership share the Practice parent, commitments precede exit, values precede visiting advice, and the medicine heading loses its stray number.

Every independently inventoried overlap cluster needs a disposition for every known occurrence. A two-of-three accounting fails. Every reported move needs both vacated-location and arrival-location audit entries. Required forward references must occur in the actual passage and point forward to an existing target. Pending scope choices must still have their original content present.

A candidate-bound editorial review and explicit scope/limits are required. Known blocking defects cannot be hidden by a PASS label. Finally, each delivered artifact must match its registered hash, and the canonical transfer receipt must bind the exact candidate. `REVIEW_PACKAGE_READY` does not mean owner-approved, newly Pangram-certified, fact-checked, published or perfectly deduplicated.

## Which checks are judgments rather than code proofs?

Discovery of all conceptual duplicates, importance of a qualification, a section’s purpose, adequacy of a bridge and the quality of the chosen order remain language/authorial judgments. The gate checks completeness and identity of their recorded evidence. It cannot detect a confidently wrong but well-formed judgment, authenticate the reviewer from a model-written receipt, or prove that an undiscovered cluster does not exist.

That is why the package includes the actual source comparison and the fresh-reader scope, not just a ticked checklist. A local writer with filesystem access can alter a local contract; a meaningful production service must isolate registration and record-writing permissions from the client. This prototype rejects mutations after enrollment, but it is not an independently administered security boundary when both processes share one OS account.

## How server-side enforcement differs from a stronger prompt

AskRigor’s inspected finalization implementation verifies server-issued research receipts against the research target and returns explicit readiness states. The transferable feature is the location and provenance of the check: the model’s statement that it completed research is not the only evidence. Its source also explicitly leaves some semantic applicability and advice-quality declarations to the model. That is not a reason to call every server receipt a proof of judgment.

This editorial implementation adopts a smaller version appropriate to a local review package: a registered immutable contract, exact artifact identities, named review evidence, strict request schema and a blocked output operation. The localhost test demonstrates this adapter; it does not claim that AskRigor’s deployed authentication or signing system has been installed here.

## Stronger deployment options, not silently installed

Claude Code hooks can place a check at a supported tool or completion boundary; a hook only protects invocations that load it. A project-controlled packaging command is simpler to verify here than a global Stop hook that may obstruct unrelated work. Required GitHub status checks can protect merging, but only when the corresponding repository rule is actually enabled and the status itself tests the intended object. They cannot block a separate chat response or clipboard operation.

The recommended next deployment step, after approval, is to route each article delivery through the tested gate and verify the exact integration in the relevant client. A hosted service or managed hooks are justified when they close a demonstrated bypass, not as a substitute for better semantic judgment. This task has not modified other apps, provider configuration or global client settings.

## Current commands

Run `python editorial_gate.py check --bundle BUNDLE --phase editorial` before derivative preparation and `python editorial_gate.py package --bundle BUNDLE --out REVIEW.zip` for the final review archive. The latter requires the delivery artifact inventory and canonical helper receipt. The service adapter is exercised through the loopback HTTP regression in `test_editorial_gate.py`; it is not left running.

The same module is used for positive tests and deliberately corrupted copies. Failure cases include stale source/candidate/answers/review, missing third overlap occurrence, a missing map node, violated adjacency, lost native object, missing two-site audit, an altered artifact, client approval injection, traversal, stale server enrollment and changed bytes after enrollment. An unchanged legitimate package remains eligible. Test counts and exact outcomes are supplied separately; this text does not assert a result before the tests run.

## Primary implementation references

- AskRigor, `apps/research-mcp/src/research-finalization-gate.ts`, inspected through the connected GitHub app on 2026-10-19. The implementation’s contract label was `2026-10-07`; this is source inspection, not a new production smoke test.
- [Claude Code hooks reference](https://code.claude.com/docs/en/hooks), inspected 2026-10-19.
- [GitHub: about protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), inspected 2026-10-19.
- [Open Policy Agent documentation](https://www.openpolicyagent.org/docs/), policy-decision/enforcement separation; architectural background, not a dependency added to this tool.
'''
(B/'EDITORIAL-EXECUTION-ENFORCEMENT.md').write_text(enforce)
brief='''# For Claude — approved lessons and this finalization

Joel kept the proposed dedup principles and all 22 teaching cases. His latest answers add four controlling refinements: ask about meaningful AI overcompletion rather than silently deleting it; distinguish conceptual numbering from reading/action order; show a synchronized interactive structure/dependency diagram; and diagnose/repair enforcement boundaries rather than ending with “execution failure.”

The article candidate now puts the full medicine discussion after the early Zapatista example, so the distinctive feature is not buried. Within practice, the route is values → finding people/visiting → shared practice → capacity → staged membership. The detailed shared-life commitments then lead to money/land, Founderism, its adjacent Movement antidote, and exit. Forward pointers make the later agreements prerequisites to commitment. Existing words and native objects are retained apart from declared heading/copy edits, short navigation and one repeated self-referential preview.

`docs/EDITORIAL-DEDUP-EXECUTION.md` is the one shared workflow. The v0.2 additions and enforcement implementation await Joel’s final approval; this is not a Claude-only fork or evidence of held-out performance. The gate runs at the actual review-package operation and checks source/answer/candidate binding, complete known-cluster dispositions, literal outline sync, reference audits, review evidence and exact delivery files. Its local HTTP adapter refuses client PASS/approval fields. The tests and limitations are in the enforcement report. No hosted service or global Stop hook is claimed installed.

The new source C remains the owner reference; no replay replaces it. The later original-source replay remains NOT RUN. The Inner Child article must not be edited until Joel approves this work and supplies or identifies its then-current owner revision. Do not restore content he already deleted merely to match old corpus counts.
'''
(B/'CLAUDE-FINALIZATION-BRIEF.md').write_text(brief)
css='body{max-width:1020px;margin:35px auto;padding:0 22px;font:17px/1.65 system-ui,sans-serif;color:#19313d;background:#fbfaf7}h1{line-height:1.2}h2{margin-top:2em}a{color:#176576}table{border-collapse:collapse;font-size:15px}th,td{border:1px solid #cdd9dc;padding:10px;vertical-align:top}th{background:#edf2f2}code{overflow-wrap:anywhere}nav{padding:15px;background:#edf2f2;position:sticky;top:0}blockquote{border-left:3px solid #a87836;padding-left:16px}'
md=mistune.create_markdown(plugins=['table'])
body='<nav><a href="Structure-and-Decisions-r03.html">Article map and approval</a> · <a href="#enforcement">Enforcement implementation</a></nav>'+md(s)+'<hr><div id="enforcement">'+md(enforce)+'</div><hr>'+md(brief)
(B/'Editing-Protocol-r03.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Editing protocol and enforcement · r03</title><style>'+css+'</style><body>'+body+'</body></html>')
print('Protocol',len(s.encode()),'enforcement',len(enforce.encode()))
