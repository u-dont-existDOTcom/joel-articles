# Review Package Regression and Definition of Done

Use this for every substantial annotated article revision. Test the exact files placed in the delivered ZIP, not an earlier working copy.

## Required base package

```text
article/<article-rNN-candidate.html>
review/<commentable-diff-rNN.html>
review/<full-draft-commentable-rNN.html>
review/source-comments.json
project/PROJECT_STATE.md
project/CHANGELOG.md
project/README.md
project/MANIFEST.json
project/SHA256SUMS.txt
```

Add the comment-resolution ledger, browser-test report, artifact-family ledger, transfer helper/report, second review baseline, or other family members when applicable. Do not reconstruct an unavailable authoritative artifact merely to fill the package.

For substantial review work, one ZIP is the authoritative delivery unless Joel explicitly requests a different form. Do not scatter a family across several unrelated downloads or provide a large browser preview.

## Fixed interface contract

The review file must retain the `joel-commentable-diff-review-v4`-compatible data structure and all of these functions:

- focus-safe selected-text and whole-cell comments with preserved exact quote and offsets;
- Keep, Remove, and Brainstorm with decision history;
- reasoning;
- Humor, Technical detail, Length, and Bluntness controls on a separate second line;
- Copy JSON and Copy Markdown;
- Export JSON and Export Markdown;
- local persistence;
- source/revised labels, revisions, and SHA-256 values;
- search and changed-only filtering.

For large articles, generate changed passages only while retaining the full interface. Performance work never authorizes removing controls or changing the export schema.

## Exact-file regression sequence

1. Build the candidate package.
2. Unzip it into a new empty directory.
3. Verify every entry in `project/SHA256SUMS.txt`.
4. Open the packaged article from the clean directory.
5. Open the packaged comparison review with network access blocked.
6. Add, reopen, edit, and delete a whole-cell comment.
7. Select text, press the comment control, deliberately clear the live browser selection before click completes, and verify that the exact quote and character offsets still survive.
8. Verify the four sliders begin below the ID/action row, are not clipped, and the second label reads `Technical detail`.
9. Exercise Keep, Remove, and Brainstorm; confirm decision history survives.
10. Move all four sliders and confirm their values survive reload.
11. Exercise reasoning, search, changed-only filtering, and any moved/consolidated destination jump present in the file.
12. Test Copy JSON and Copy Markdown.
13. Download JSON and Markdown exports; parse the JSON and confirm comments remain verbatim.
14. Reload the local file and confirm persistence.
15. Verify the review has no external scripts, stylesheets, CDNs, or network dependency.
16. Audit article and review links: no empty targets, internal fragments resolve, and each consequential link remains attached to the intended text.
17. Confirm source and revised hashes in each review match the declared baseline and packaged candidate.
18. Confirm required package members and optional declared members are present exactly once.
19. Open the packaged full-draft commentable review; confirm one column, one commentable cell per semantic block, no empty comparison cells, focus-safe selected-text notes, exports, and persistence.
20. Record load and interaction timing on the available test machine; do not claim a modest-laptop result unless that class of machine was actually tested.
21. Recompute and verify checksums after final assembly.

## Reporting terms

- **Generator-selftested:** static generator assertions passed.
- **Interaction-tested:** controls, exports, and persistence were exercised in a browser automation run.
- **Local-file confirmed:** the exact packaged `file://` artifact passed in the tested browser.
- **Offline confirmed:** the review passed with network requests blocked.
- **Destination-confirmed:** the real publication or target-browser path was tested.

Do not collapse these statuses. `page.set_content`, a source hash, a successful ZIP build, or a `Copied` message proves only its own validation plane.

## Definition of done

A candidate is ready for delivery only when:

- the last approved baseline is named and hashed;
- the candidate revision is named monotonically and is not called final;
- every raw comment has a ledger status;
- unresolved issue count is zero or explicitly accepted;
- adjacent transitions and global terminology were rechecked;
- links and citations were verified;
- the full interface contract is present;
- exact packaged files passed the claimed tests;
- the ZIP opens cleanly and checksums match;
- the response distinguishes completed, tested, pending, and unavailable work;
- approval, not delivery, changes the candidate to `rNN-approved`.
