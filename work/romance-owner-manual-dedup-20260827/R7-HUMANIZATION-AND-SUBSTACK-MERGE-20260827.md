# Romance R7 — humanization result and raw Substack merge

Status: working editorial/publishing provenance; **not registered article authority**.

## Exact prose / detector identity

- R6 owner-reviewed prose SHA-256: `00406e72b3a86977024edc8fc5a3544d2d198ee9393945c0cf6564f07110a67d`.
- R7 minimum-dose humanized prose SHA-256: `da32d34919b1f320ae79f1e89ba050590aaa5c14f0f15488beed3b5e0a5bf817`.
- Joel reports the exact R7 candidate tested **100% Human, high confidence**.
- This is owner-reported detector evidence. The exact detector model/version, numeric fractions, result path/receipt, and screenshot were not supplied here and are not inferred.

R7 changed only surviving assistant sentence realization inside eight already owner-approved R6 operations. Untouched owner prose, rejected proposals, and pending heading-only operations were not reopened. The bounded preservation/architecture receipt records zero unexplained substantive deltas.

## Reusable editorial lesson

**Structural-operation approval does not imply wording approval.** An owner-approved move, consolidation, deletion, compression, or routing change locks the operation/function, not automatically the assistant wording used to realize it. A later humanization pass should identify only surviving assistant realization, leave untouched owner prose alone, and prefer minimum-dose rollback to actual owner language wherever it can still perform the approved operation. Fresh model syntax is reserved for relations the approved operation genuinely requires.

The Pangram Humanization Lab carries the promoted cross-project lesson and detector provenance separately; the R7 Human/high result is evidence for the exact candidate, not phrase-level causality.

## Latest raw Substack source and merge

Joel supplied a fresh raw Substack editor HTML source on 2026-08-27.

- Latest raw editor HTML SHA-256: `160094d22311ca6959551dcb939241fed2ba5f4365c1b8219a2aefd13d7db3ff`.
- Merged R7 archival editor HTML SHA-256: `9740ad46709540d6f5b51c185bfb1eaa54f86a9845372a11814b1f011728a1d6`.
- R7 reader prose and merged archival reader prose were compared at the intended prose boundary: 20,002 vs 20,002 words and zero word-level diff operations after excluding the two live-only top headings/native-object text.

The raw editor HTML remained authoritative for native-object identity, attributes, links, heading markup, and placement. The merge used targeted raw-string replacement rather than whole-document DOM parse/reserialization.

The latest raw source and merged archival source each inventory 25 protected native objects in the same order:

- 13 images;
- 10 YouTube embeds;
- 1 Share button;
- 1 Subscribe button.

`html_islands.py verify` confirmed all 25 latest-source islands survive byte-for-byte and in order in the merged archival HTML. The Helen Fisher YouTube object (`PgoN0k0_0bg`) remains at the colon/anchor that looked incomplete in the prose-only export.

The two live-only top headings in the fresh Substack source were preserved rather than replaced from the prose candidate: the Claude-app guide and Couples card-game link.

## Canonical helper generation

The clipboard helper was generated with the repository's current `project-sources/substack_transfer_helper.py.txt` and `project-sources/CONFIRMED-SUBSTACK-HELPER.json`, using the mandatory `init → build → verify` path. No parallel/ad-hoc helper was invented.

- Helper format: `joel-substack-transfer-helper-v4`.
- Helper SHA-256: `ea77c437f7e8f0e6a28e619dca067ba7a0de41f1532c24a0edcc0d4b2e2f91a9`.
- Payload mode: `single_rich_html`.
- Segment count: `1`.
- Standalone native-uploaded video count: `0`.
- Manual native steps: `0`.
- Visible action: one `Copy Article` button.
- Confirmed compatibility target remains downloaded local HTML opened directly in Opera → Substack editor.

Source fidelity and transfer conversion passed statically. A real Opera → disposable Substack draft reconstruction remains destination-specific and is not claimed by this record.

## Canonical tooling repair discovered during merge

The required helper initially failed closed because current Substack markup had drifted beyond the canonical classifier:

1. YouTube blocks now use `youtube-wrap` and `youtube-nocookie.com`, so they were being classified as unverified generic iframes.
2. Subscribe now uses generic `ButtonCreateButton` markup containing `%%checkout_url%%`; generic Share detection ran first and misclassified Subscribe as Share.

PR #67 repaired `project-sources/html_islands.py.txt` and added regression coverage. The final helper was regenerated only after that canonical repair was merged. The repaired parser correctly inventories the fresh Romance source as 13 images / 10 YouTube / 1 Share / 1 Subscribe.

## Authority boundary

Registered `articles/romance/master.md` remains the current GitHub article authority. R7 and its merged archival Substack source are working publication-preparation artifacts; this record does not silently promote them, mark the whole article owner-final, or publish it.
