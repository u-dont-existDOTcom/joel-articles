# Somatic Therapies — live merge + canonical Substack helper execution receipt

Date: 2026-09-05
Status: **EXECUTED WORKING MERGE / CANONICAL STATIC HELPER VERIFY PASS / DESTINATION RETEST PENDING**

## Owner request

Joel supplied a fresh raw Substack editor fragment and asked to merge the accepted best-of live-source plan, then generate a new Substack clipboard helper using the latest validated `joel-articles` helper implementation, explicitly forbidding an improvised helper. Humanization is the next pass, not part of this execution.

## Source authority for this execution

- User-supplied raw Substack editor fragment SHA-256: `14197e5e9aeea2ca4809da7b8186c69c12c0b86f4f81f30ec75ed2a52fd69fa4`
- Source bytes: 59,639
- The supplied raw source superseded stale `articles/somatic-therapies/master.html` for this merge operation only; the registered master remains intentionally stale until a later authority/final-assembly decision.
- The source outer editor root is the current Substack form `data-testid="editor"`; the canonical parser classifies this supplied file as `fragment` mode. No transport code was patched or improvised to change that behavior.

## Executed merge

Merged raw editor working artifact SHA-256: `357703d0156dec663a57713affc4b2e60dbca4d0393fbdffa6afcee460a1fb5c`

Merge followed the owner-accepted best-of direction in `SOMATIC-LIVE-SOURCE-BEST-OF-MERGE-PROPOSAL-20260905.md`:

- keep the live owner Introduction / five-stage map / Professor Baby Sheep / Jules-MCT / accepted trauma-memory architecture;
- remove the redundant post-map Introduction sentence;
- restore continuous older Stage 1–4 prose where the live source had been converted into repeated `Goal / Best use / Mechanism / Warning` cards;
- preserve the newer routed Nurturer/Protector, self-hypnosis, solar-plexus/heart-loop, Brainspotting-dose, and EMDR transition functions;
- use current Stage terminology and owner map headings;
- do not add Sensorimotor Psychotherapy or Focusing in this merge;
- remove the redundant later arrow recap and add the Jules/MCT outcome criterion in the working merged prose;
- leave the optional high-intensity section structurally unchanged.

Exact model-written surface introduced by the merge remains working and is scheduled for the requested humanization pass; this receipt does not promote those bytes to owner-final.

## Native/editor object fidelity

Canonical parser: `project-sources/html_islands.py.txt`

Git blob SHA verified locally against GitHub: `46a85cae623f3e8e6282c6d3d6d87ccb57b90aa5`

The uploaded original was frozen with the canonical parser, then the merged raw editor artifact was verified against that original island manifest.

Result: **PASS — 10 exact source islands preserved in order.**

Object inventory in both source and merged artifacts:

1. image
2. image
3. Substack video-post embed — Professor Baby Sheep
4. image
5. Share control
6. YouTube — Somatic Experiencing
7. YouTube — TRE/shaking
8. YouTube — Brainspotting
9. YouTube — EMDR
10. Substack video-post embed — Sky Hypnosis

Counts: 3 images, 4 YouTube, 2 Substack video-post embeds, 1 Share control. There are **0 standalone native uploaded-video objects**.

All ten source-island SHA-256 signatures remained byte-identical; surrounding heading anchors changed only where the accepted prose merge changed headings.

## Canonical helper implementation

No helper code was invented.

Exact current generator:
`project-sources/substack_transfer_helper.py.txt`

- Git blob SHA verified locally against GitHub: `b8df54fa82c4f7754df5a80ab66d1eebbf0ad3fd`
- local SHA-256 of exact materialization: `322e4738243806570fd01de4389150144f13f959de30d78579b69fb57c9352f4`

Exact current parser:
`project-sources/html_islands.py.txt`

- Git blob SHA: `46a85cae623f3e8e6282c6d3d6d87ccb57b90aa5`
- local SHA-256: `e82e5b862e197adb56bfd484c453433d11b8b2cad0dcf45d5bf3280b9f24ddc9`

Exact compatibility profile:
`project-sources/CONFIRMED-SUBSTACK-HELPER.json`

- Git blob SHA verified locally against GitHub: `35688fdddc690b8bdc9c3c8dbbe258000061c086`
- SHA-256: `c58bf6928274eb9734194c280a8a5f3b53be50d0e913e7cfb24c23593af05734`

Canonical generator self-test: **PASS**.

## Canonical build sequence

Executed exactly:

1. `init`
2. `build`
3. `verify`

Canonical verify result: **PASS**.

Helper manifest format: `joel-substack-transfer-helper-v4`

Helper SHA-256: `5ba905b6d760ac4a7d6639d34eebd0c766721cc4b538b7de66ee6e78861a889a`

Transfer plan SHA-256: `0c745723f89e2fad82506064850bc21baccd44b42713dd0f7d6adda0ad482230`

Native-object inventory SHA-256: `6e21c2bbb3ca4961734b00f2297c81a6b7eefbce75795e13444e7416db2ef913`

Transfer report SHA-256: `58f58471f1c705220c774f57f70426b22449fcf4c85a1e39e9338d6c849381d5`

Compatibility report SHA-256: `309c79764039b18f99b7748c185744c3dc697d0b0424146af3dfa877e1163e0b`

## Helper manifest summary

- payload mode: `single_rich_html`
- segment count: 1
- visible control: `Copy Article`
- native uploaded-video count: 0
- native-video manual steps: 0
- Substack video-post embed count: 2
- both Substack video-post embeds are converted to their canonical post URLs in the same current payload segment, as required by the confirmed profile
- object types in order: image, image, substack_video_post_embed, image, share, youtube, youtube, youtube, youtube, substack_video_post_embed
- payload SHA-256: `de4ffef8c6bd436ac515fd1451de0d3bea36a910b1580d02724201e176b459b0`

## Validation boundary

Static canonical source/conversion verification passed. Per the repository delivery gate, this does **not** prove final Opera clipboard behavior or destination reconstruction in Substack.

Destination status remains:
`pending_final_opera_to_substack_retest`

A successful `Copied` status proves clipboard completion only. The normal disposable-draft check should confirm images, YouTube, Share, and reconstruction of the two video-post cards.

## Next editorial action

Humanize the merged reader-visible article in bounded natural sections, applying Joel's 2026-09-05 standing instruction to humanize every new model-written article sentence before owner delivery. Do not add Sensorimotor/Focusing unless reopened separately.
