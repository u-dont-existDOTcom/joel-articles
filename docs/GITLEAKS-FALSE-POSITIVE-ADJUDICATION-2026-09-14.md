# Gitleaks finding-level false-positive adjudication

Date: 2026-09-14

Status: **APPROVED EXACT-FINGERPRINT SUPPRESSIONS**

The publication audit reported six historical `generic-api-key` findings. Each finding was inspected at its exact commit and is not a credential:

- the four findings in the historical infographic workflow and receipt are UUID-style infographic object/file identifiers;
- the two findings in the historical current-state commits are SHA-256 provenance hashes.

The root `.gitleaksignore` contains the six exact Git-history fingerprints approved for those findings, plus two exact hosted-log fingerprints for the same first two reviewed identifiers as echoed by historical Actions run `34550531021`. It does not suppress the rule, any whole path, any whole commit, any whole run, or any history range. A new occurrence receives a different fingerprint and remains detectable.

## Approved fingerprints

```text
9b85154309c90bef820923b43d44ea1222b4a91d:.github/workflows/update-inner-signal-infographics.yml:generic-api-key:67
9b85154309c90bef820923b43d44ea1222b4a91d:.github/workflows/update-inner-signal-infographics.yml:generic-api-key:73
defc51d43fa291dcb00c93468e111c967094164a:articles/inner-signal/INFOGRAPHIC-UPDATE-RECEIPT.json:generic-api-key:10
defc51d43fa291dcb00c93468e111c967094164a:articles/inner-signal/INFOGRAPHIC-UPDATE-RECEIPT.json:generic-api-key:19
4229009b35f9cdff71d835d2a6c7df398fa15206:state/CODEX-CURRENT-STATE.md:generic-api-key:31
0ff49c99fdfe275b596bda72c1338f80fec14941:state/CODEX-CURRENT-STATE.md:generic-api-key:31
hosted/actions/run-34550531021.log:generic-api-key:330
hosted/actions/run-34550531021.log:generic-api-key:336
```

The hosted audit now scans from its temporary root so hosted fingerprints are stable and relative. Diagnostic run `34859376003` established that hosted lines 330 and 336 are the log echoes of source lines 67 and 73 in commit `9b85154309c90bef820923b43d44ea1222b4a91d`; both are the already-reviewed UUID-style infographic filenames.

## Required proof

Release evidence must show that pinned Gitleaks 8.29.1 reports no findings for full repository history with this file, that deleting any one approved fingerprint restores its corresponding historical finding, and that a fresh synthetic credential fingerprint in a disposable repository still fails the scan.
