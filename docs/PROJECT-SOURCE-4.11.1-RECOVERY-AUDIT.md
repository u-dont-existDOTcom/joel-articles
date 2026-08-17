# Project Source recovery audit — 4.11.1 baseline

Date: 2026-08-17

Owner direction: `Joel-Articles-4.11.1-Project-Sources.zip` is the complete historical 40-source baseline. The newer current Project/GitHub versions supersede same-named older files.

Status: **the exact 40-source recovery is complete.** Reference integrity has
one unresolved optional tool source that was not present in the owner package.

## Finding

- Historical baseline: **40 files**.
- Current active `project-sources/` before this recovery: **9 files**.
- Historical files with newer active replacements: **9**.
- Historical files absent from active `project-sources/` and requiring restoration: **31**.
- Historical exact sources archived after recovery: **40**.
- Historical sources restored active after recovery: **31**.
- Historical sources retained archive-only because current files supersede them: **9**.
- Current ChatGPT Project source count: **10**; this recovery did not write old
  files back to the Project.
- Unresolved repository-local source references: **1**.
- Exact owner ZIP SHA-256:
  `c0b6b0ce4d95b303a00cc44d75fdf54e4433fa72e39e9e866c84b856fde965b1`.
- `GITHUB-BOOTSTRAP.md` and `EMERGENCY-FALLBACK.md` are later additions and are not members of the 4.11.1 forty-file baseline.

Nothing in this audit changes article authority. The repository article registry remains controlling.

## Disposition ledger

| Historical file | Bytes | SHA-256 | Disposition |
|---|---:|---|---|
| `ARGUMENT-AND-EVIDENCE-ARCHITECTURE.md` | 18707 | `102da3aa74c974cc939123e2fb5201506f4964d70f95342686b1445506ac7e14` | archive only — newer active version supersedes |
| `ARGUMENT-LEDGER-QUICKSTART.md` | 5931 | `c3bf7b39093b946f0df79798838e3ae3a5e935a3d3ceb0c36f47e6af6ef2911b` | archive only — newer active version supersedes |
| `ARTICLE-INDEX.md` | 16088 | `1bd1f154699580a34f431052844b8dcf8fee3141276bf5155bf21d10e1414998` | restore active + archive exact historical copy |
| `ARTIFACT-FAMILY-LEDGER-TEMPLATE.md` | 6442 | `532f440c7aec51b30c7ab433c5313c61e57a86173197d2de5a9ce834431c9ec7` | archive only — newer active version supersedes |
| `BANNED-PATTERNS.md` | 34363 | `1d8e829f0b351ee1fd7c3d563c6869ac667f9e5c044464b81afdbf194e570557` | restore active + archive exact historical copy |
| `CANON-FACTS.md` | 9279 | `c544535d80737c7fc3b1ba2be6fb08c02ce319aee9329fe297a501555dddcd95` | archive only — newer active version supersedes |
| `COMMENT-RESOLUTION-LEDGER-TEMPLATE.md` | 2538 | `2857b4fc200b0b4e80ee19fd23532ecd2e9644660aea03dea75331abd06e69fc` | restore active + archive exact historical copy |
| `CONFIRMED-SUBSTACK-HELPER.json` | 3468 | `b9132116432fc2e37ff47dacf7794f98c1a3e1ef906fd6baed1fac85075a9342` | archive only — newer active version supersedes |
| `CONTROVERSIAL-TOPIC-EVIDENCE-AUDIT.md` | 2638 | `0b6620a20abcd195092e54395266c44bf365e9b0756328f3925a164da831a276` | restore active + archive exact historical copy |
| `EDIT-CONTRACT-AND-LEDGERS.md` | 40745 | `3530160be4eed2a1c77d2602c61dda90baed9b482d3e0588f542fd7f1399f884` | restore active + archive exact historical copy |
| `FACTS-HEALTH-FORMATTING.md` | 13157 | `35c11c27c77efd363d9955d7b9cb31749d1e0f381f6c010db301d7d0b4edb986` | restore active + archive exact historical copy |
| `FINGERPRINT-PASS.md` | 36594 | `c05ccbd4ea16bedaf54f7b6428f09f1dfe3635c9976aa3d62cbdba43b40e0b4f` | restore active + archive exact historical copy |
| `HUMANIZATION-AND-COHERENCE.md` | 22986 | `0f2bddf8fc1b8011a1424cb760ef497cb9bec9e50000a338e9636db0180d797a` | restore active + archive exact historical copy |
| `INTERLINKING-AND-HTML-SOURCE.md` | 17315 | `5ec47f956d88f8fb1de010777dc52814acfd8a359348737bf1b39f4eaf9430df` | archive only — newer active version supersedes |
| `MASTER-INSTRUCTIONS.md` | 46850 | `4a747158a5ef5c53830d8fa339bf3d785bdc58f58aa7ead1a8266fdb226a05c2` | restore active + archive exact historical copy |
| `PROGRESSIVE-DISCLOSURE-EXAMPLES.md` | 5091 | `caf573ce8ecc1a38eb1456ea19d131582224846da03a5da23aad995fed9e82df` | restore active + archive exact historical copy |
| `PROJECT-STATE-TEMPLATE.md` | 10427 | `a07b8c17a56761cc91bce23c7d14c1a7052f41d606c41eb9bd8e3a22fa2f8d55` | restore active + archive exact historical copy |
| `QUALITY-FORECAST-AND-PASS-REVIEW.md` | 17007 | `288b8d4eb6f2013504ffaccf4c87ef0e9704edced35ef6da4b2075783f51d813` | restore active + archive exact historical copy |
| `REVIEW-INTERFACE-SPEC.md` | 7796 | `e77f1c138fb44bc89f7209b2ae4916100650ee0f51cfbcff2ff5641bb65faeba` | restore active + archive exact historical copy |
| `REVIEW-PACKAGE-REGRESSION.md` | 4897 | `8549348ff36eb19291496cbbfc1ee6e11e02af003e9f18cc1deff2686d518a1e` | restore active + archive exact historical copy |
| `REVIEW-WORKFLOW-RULES.md` | 16062 | `3307fc89beadd1e78e02e612ba9673457c2433c0851e2f85471b1ad04da698ec` | restore active + archive exact historical copy |
| `STRUCTURAL-HUMANITY.md` | 43254 | `3e7a9360b5ade7a89ca843cbcfeffbe0c6fcd2b633e67e9cef6092a280f4296e` | restore active + archive exact historical copy |
| `TASK-MODES.md` | 24909 | `0d3e77b688814767ad43b0053310b753e832ab71c96d128196fd5b3f26a1898e` | restore active + archive exact historical copy |
| `TOOLING-IN-PROJECT-SOURCES.md` | 3810 | `7de902181d952f65772d109fef0fce3efc981aab0d9586f1ad5d4e47239bd221` | restore active + archive exact historical copy |
| `TRANSFORMATION-CASE-STUDY.md` | 46716 | `b2a040e0ee99b65fa44b7b05e48eb2f1957f07ae29b5495238abe241c330d6f3` | restore active + archive exact historical copy |
| `VISUAL-EDITORIAL-PROTOCOL.md` | 4910 | `e4dcd12948cd435a80d553b72f8768cb953fec88ed999ce389bfd05632049f28` | restore active + archive exact historical copy |
| `VOICE-LEXICON.md` | 3259 | `440133624cf60e9455d91208790694e37dac46173e57dae904754a7195d0584b` | restore active + archive exact historical copy |
| `VOICE-REFERENCE(1).md` | 15347 | `e360690fb34f49d01c000b3bd552324281207b6c55699c4794fd9512680d2342` | restore active + archive exact historical copy |
| `WORKER-CHAT-HANDOFF-RULES.md` | 5180 | `91d6da5100675047b8728ec9d7e5154a67111a5df96305b4f66e2a87c61fdca3` | restore active + archive exact historical copy |
| `argument_ledger.py.txt` | 51359 | `777fbf9d564aa95c62345a889b9c448d8fa1c087bcdc92be3cb2d57fbedafd77` | restore active + archive exact historical copy |
| `cancer-and-research-samples.txt` | 86094 | `9c082d52fe6a6e5ed242ac2af0a17981e6f1a6d4b7f1bd7e57cb643c5dabd0dd` | restore active + archive exact historical copy |
| `community-before.txt` | 45852 | `a230d45d1ec7fa3140bd6543a06b1042ad02b4068728398b6caf381ae8e9808f` | restore active + archive exact historical copy |
| `html_islands.py.txt` | 19904 | `9e9411e5959ea610c4f4fc2f11f7f6d72a0afe2f8cb7ff63a96dc4af7cdbf6b3` | archive only — newer active version supersedes |
| `html_publish_modes.py.txt` | 19673 | `2ae9877823ffb11aebd10611662c11a4a70a2429ea76e4c082c3d2a9e1bafd8e` | restore active + archive exact historical copy |
| `interactive_review.py.txt` | 35782 | `2ed2731a4fd03bec3d945724644ea8b1eddbf0d090c17cba3fd9e8f4f1838af2` | restore active + archive exact historical copy |
| `review_interface_browser_test.py.txt` | 29920 | `efdf285a3e37fbf45cc9fb2f74174b4b3bd2d873a362a0730f5368cd55363658` | restore active + archive exact historical copy |
| `review_interface_template.html.txt` | 28676 | `cc3907f13c8739b4e740872f7460fa2ebb9f6395f7378f31c0c48f40883dced0` | restore active + archive exact historical copy |
| `review_package.py.txt` | 20569 | `624cc7e76a493e9bee63af69f212967a49321958145e841dba963e65f141cda7` | archive only — newer active version supersedes |
| `substack_transfer_helper.py.txt` | 36050 | `62d4df1557f75f19f0e1d0f3a2471a932e5f8211547a9e6e56dd6401e9c47908` | archive only — newer active version supersedes |
| `tender-video-transcript.txt` | 11399 | `a12d8b699aa19723f819dc324d2107b03d9d7db919a2997283ccb73069094f1f` | restore active + archive exact historical copy |

## Canonical-path note

`VOICE-REFERENCE(1).md` is preserved under that exact filename in the historical snapshot. Its active restored path should be `project-sources/VOICE-REFERENCE.md`, matching the canonical filename referenced by the operating instructions.

## Final execution and provenance

- Recovered branch:
  `migration/restore-4.11.1-project-sources-2026-08-17`.
- Preserved pre-run branch head:
  `5fbdac8f4344a5bfeb4c96b5e0ce9a7b8f6b0837`.
- Exact ZIP is committed at
  `archive/project-source-snapshots/4.11.1/Joel-Articles-4.11.1-Project-Sources.zip`.
- `archive/project-source-snapshots/4.11.1/sources/` contains exactly 40
  byte-identical members under their original filenames.
- `MANIFEST.json` records every original filename, byte count, SHA-256,
  active destination or null, disposition, and supersession boolean.
- `SHA256SUMS.txt` covers the exact ZIP and every archived source payload.
- The 31 active restoration targets are exact ZIP-member bytes. Historical
  `VOICE-REFERENCE(1).md` remains exact in the archive and is active as
  `project-sources/VOICE-REFERENCE.md`.
- Pre/post SHA-256 comparison passed for all nine newer active successors;
  none was modified.
- `articles/INDEX.json` remained byte-identical at
  `115e2584d549884dfd31a6328d967d0df949ac3fc1719130fee59413b7980d4f`.
- The abandoned GitHub Action transport was deleted. No `.migration/4.11.1/`
  transport directory remains.
- `scripts/restore_project_sources_4_11_1.py` now accepts the exact local ZIP
  through `--zip`, refuses differing collisions, and provides idempotent
  `--check` verification. Its documented invocation is:

  ```bash
  python scripts/restore_project_sources_4_11_1.py \
    --zip /path/to/Joel-Articles-4.11.1-Project-Sources.zip
  ```

- Final recovery commit: the commit containing this report. Its exact SHA is
  recorded by the pushed branch ref and final worker handoff; a Git commit
  cannot embed its own SHA without changing that SHA.

## Reference-integrity classification

The scan covered `SKILL.md`, `CANONICAL-REPO-MAP.md`, and every active Markdown
source restored from the baseline. File-like names used only as runtime
materializations, command inputs/outputs, artifact-family placeholders, or
future release outputs were checked in context and were not treated as claims
that those generated files already exist in the repository.

- **Exists active:** every explicit local loader route and every referenced
  baseline source authority resolves. Runtime `.py` names resolve through the
  corresponding active `project-sources/*.py.txt` authority when that source
  exists.
- **Exists archived only and intentionally so:** the exact historical
  `VOICE-REFERENCE(1).md` path and all superseded historical payload bytes are
  retained under the versioned snapshot; active voice routing uses
  `project-sources/VOICE-REFERENCE.md`.
- **Superseded with current destination:** the nine historical sources listed
  in the disposition ledger route to their untouched same-named active paths.
  The loader preserves the current native-uploaded-video/video-post behavior.
- **Genuinely missing:** `html_diff.py.txt` (and therefore its runtime
  materialization `html_diff.py`) is referenced as an optional quick-diff tool
  by restored protocols, but is absent from both the exact 40-member ZIP and
  the current repository. It was not invented. **Unresolved count: 1.**

The restored stale `scripts/html_islands.py` wording is routed by the current
loader to `project-sources/html_islands.py.txt`, materialized as
`html_islands.py` only when needed. This repairs current routing without
changing the exact restored historical-source bytes.

## Validation results

All required repository gates passed on the completed worktree:

- `python -m unittest discover -s tests` — **PASS**, 84 tests.
- `python scripts/validate_content_repository.py --root .` — **PASS**;
  governance incubator, zero registered articles, canonical import still
  blocked.
- `python scripts/validate_article_architecture_maps.py --root .` — **PASS**.
- `python scripts/audit_codex_github.py --root . --fail-on error` — **PASS**;
  0 errors and 4 pre-existing governance warnings (disabled default-branch
  rules, unverified push protection, unverified secret scanning, missing
  license).
- `git diff --check` — **PASS**.
- Recovery CLI `--check` — **PASS**, exact hash and `40 / 31 / 9` counts.
- `sha256sum -c archive/project-source-snapshots/4.11.1/SHA256SUMS.txt` —
  **PASS** for the ZIP and all 40 sources.
- Pre/post checks of the nine protected successors and `articles/INDEX.json` —
  **PASS**.
- Explicit local loader-route existence check — **PASS**.
- High-confidence token/private-key pattern scan over introduced content —
  **PASS**, no matching path.

Applicable tool checks:

- `interactive_review.py.txt --selftest` — **PASS**.
- `review_package.py.txt selftest` — **PASS**.
- `substack_transfer_helper.py.txt selftest` — **PASS**.
- `argument_ledger.py.txt --help` and `html_islands.py.txt --help` — **PASS**;
  neither exposes a self-test.
- Source inspection found no self-test in `html_publish_modes.py.txt` or
  `review_interface_browser_test.py.txt`; their help imports could not run in
  this checkout because optional `tinycss2` and `playwright` dependencies are
  absent. No unsupported command was guessed, and this does not change the
  required repository-gate results above.
