# Love, Honestly v0.3.0 Release Manifest

Release date: 2026-08-17

## Git identity

- Release commit: `66dba59994e3fe67f7158aac940015057c252aaa`
- Annotated release tag: `v0.3.0`
- Annotated tag object: `31241f3b91b1a316076003da4c5b7fa44de7ee1a`
- Final release-bundle head: `4ab6fdf07351767807ba95bd60012f2303d742be`
- Previous release tag: `v0.2.1`
- Previous release commit: `7f56a441b1ccb61520711c67dbb2ae6d46098ceb`
- Article Edition tag: `v0.1.0`

## Downloadable artifacts

```text
7c7049812d60853c814d221335dd68467d5e6dceedbf332fe6e4d29398eaded1  Love-Honestly-Game-v0.3.0.html
f431f9df8f96dbf3e89ce1a50f270b6697106b92290982b28a6e9704c41ee66b  Love-Honestly-Welcome-v0.3.0.png
571f00dbd87e1d51e60d9727b9247d02a59c02e23ca032cbadefba0a7fb0b924  Love-Honestly-Comparison-v0.3.0.png
588e5e22253daee2bc0d89935c6bfacb2cae84694a87c2d4df7f70e5e2320af0  Love-Honestly-Article-Edition-v0.1.0.html
ea84d786e596b1ce435167346e80be519d44209b27eaf767e0c108d63161141e  FRESH-CONVERSATION-HANDOFF-v0.3.0.md
b0ec795e9c4bd8ba2b8437977dbeca61419ea6215a51cd49836c3c260a60b829  RELEASE-MANIFEST-v0.3.0.md
ce1ccacd29324150c4633dbfd8c7ff71ee97ce700ca67f6f0791fa50ae152574  Love-Honestly-Card-Game-v0.3.0.zip
991b21d3766756032b73eef26aa3853015cebed9ce2fea64ba77f10d9f00a8bd  Love-Honestly-Card-Game-v0.3.0.bundle
```

## Product acceptance

- 79 substantive cards, 8 rhythm cards, and 15 substantive categories.
- Five overlapping cards revised and seven distinct cards added.
- Twelve unique update functions and twelve explicit card-level experiments.
- Exact first-screen linked text remains `Based on the U-Dont-Exist Romance Guide` → `https://romance.u-dont-exist.com`.
- Source disclosure credits Doug Toft, Kim Anami, and Buddhist/lived material as sources, not co-authors.
- All optional categories, including Spiritual Practice, begin disabled.
- All v0.2.1 card IDs and storage schema v2 remain stable.
- Spoken answers, card prose, and source metadata remain outside local serialization.
- The one guide link is user-initiated navigation; no automatic external runtime request occurs.

## Verification evidence

- `npm run verify:release` passed with 34/34 Node tests.
- Standalone build completed at 169,987 bytes.
- Normal, private safety-stop, anonymous not-safe, storage-boundary, two-person revisit, source-disclosure, optional-topic, and demo/browser flows passed.
- Browser request monitoring observed no automatic HTTP or HTTPS request.
- Source ZIP passed `unzip -t`.
- Git bundle passed `git bundle verify` and cloned successfully.
- Bundle clone contained `v0.1.0`, `v0.2.0`, `v0.2.1`, and `v0.3.0`.
- Bundle clone head resolved to `4ab6fdf07351767807ba95bd60012f2303d742be`.
- `v0.3.0^{}` resolved to exact release commit `66dba59994e3fe67f7158aac940015057c252aaa`.
- Every downloadable artifact matched `Love-Honestly-v0.3.0-SHA256.txt`.

## Bundle authority

The Git bundle is the complete source-history carrier. This branch stores architecture and recovery metadata only. Do not infer source bytes from screenshots, standalone output, or this manifest when the verified bundle is available.
