# Tooling Stored in Project Sources

The Python utilities are uploaded once as plain-text Project Sources (`*.py.txt`) alongside the Markdown references, because text files are the most reliably accepted source format. They remain available as source files for future chats in the Project.

They are not background services and are not executed merely because they are present. When a task requires a utility, use Data Analysis/code execution to access the stored file, save the exact contents under its real `.py` filename in the active runtime, keep dependent scripts together, and run it. Do not ask Joel to upload the script again unless the Project source is inaccessible, the file was removed, or code execution is unavailable in the selected chat/model.

## Thresholds

- `argument_ledger.py.txt` → `argument_ledger.py`: only for medium/high premise risk with material dependencies. Propose none/minimal/standard/full scope first; ask only when two scopes are genuinely reasonable.
- `substack_transfer_helper.py.txt` → `substack_transfer_helper.py`: final Substack HTML with native objects. Extract the raw editor body, build the separate confirmed one-paste Opera payload from the exact final archival HTML, consume the compatibility profile, and compare against the last confirmed helper. It records source fidelity and transfer conversion but cannot prove destination reconstruction.
- `html_islands.py.txt` → `html_islands.py`: inventory/freeze/restore/verify fragile native objects by semantic type, source identity, anchors, and placement; source fidelity only.
- `interactive_review.py.txt` + `review_interface_template.html.txt` → `interactive_review.py` + `review_interface_template.html`: mandatory interactive side-by-side review for substantial revisions; preserves `joel-commentable-diff-review-v4`, focus-safe exact selected-text/whole-cell comments, decisions, second-line sliders labeled Humor/Technical detail/Length/Bluntness, Copy/Export, persistence, search, filtering, exact hashes, and both review baselines. Use `--changed-passages-only` for large comparisons rather than removing features. Use `--full-draft current.html` to generate the complete one-column commentable current draft.
- `html_diff.py.txt` → `html_diff.py`: optional quick static yellow/collapsed diff only; never substitutes for or overwrites the interactive review.
- `html_publish_modes.py.txt` → `html_publish_modes.py`: conservative self-hosted or Ghost adaptation and validation.
- `review_interface_browser_test.py.txt` → `review_interface_browser_test.py`: first attempts the exact local review in headless Chromium with external HTTP(S) blocked; exercises comments, focus-safe selected-text offsets, second-line slider layout, comparison and full-draft modes, decisions, Copy/Export, persistence, reasoning, search, filtering, and JSON parsing. When the environment blocks navigation, it uses exact-HTML injection with a deterministic Storage shim and reports local-file confirmation as unavailable rather than overstating the result.
- `review_package.py.txt` → `review_package.py`: builds one portable review ZIP with candidate article, immutable source comments, project state, changelog, README, manifest, checksums, and optional ledgers/test reports; statically verifies structure, hashes, review format/features, offline dependencies, and candidate-hash identity.

Use `PROJECT-STATE-TEMPLATE.md`, `COMMENT-RESOLUTION-LEDGER-TEMPLATE.md`, `WORKER-CHAT-HANDOFF-RULES.md`, and `REVIEW-PACKAGE-REGRESSION.md` for the state, reconciliation, and exact-file test contracts.

A script's output is bookkeeping or validation evidence, not permission to alter prose. A generator selftest or static package verification does not replace exact-file browser interaction or destination testing.
