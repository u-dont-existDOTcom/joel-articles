# R15 article-wide candidate — exact Pangram result

Status: **VALID NEGATIVE RESULT / OWNER OUTCOME UNMET**

Authority: `SUPERVISOR_DECISION SOMATIC-R15-OBJECTIVE-006`, response SHA-256 `10147a9654109186e913e134ac86793f421f73f8675e190e47576cb60ba3702f`.

## Exact input

- candidate: `articles/somatic-therapies/experiments/R15-ARTICLE-WIDE-HUMANIZATION-CANDIDATE-20260830.md`;
- candidate Git blob: `68d62fd3a613e2f51941da3a640bfaaeba78f0e9`;
- candidate SHA-256: `9bf286b53945c22fb57ca0e5b57c7f4c8c411de829be07bcf07d85d6f77eccd0`;
- reader-visible boundary Git blob: `10db8f1d586c5e93fe794e50f6b3e16a1bf721ee`;
- boundary SHA-256: `fc5a8e49c499c4e4165ff3e6aded4f26c88bacdd9475e9e799a482a19c7a504a`;
- 3,585 whitespace words; 20,969 Unicode characters; 21,061 UTF-8 bytes; final blank line preserved.

## Recovery and paid-action safety

Standard recovery and an exhaustive authenticated History probe were read-only. The exhaustive probe inspected 61 History candidates and 43 stored records, found no exact match, and attempted no detector submission. No cache entry, reservation, ambiguous action, GitHub result, or exact History record existed.

The deterministic local runner pushed its durable reservation before the only GUI click:

- reservation commit: `5323c33e53199c628786b4a6fe6c3c512ebe09ed`;
- completed-result commit: `a8ba76025f4baef77fb90a8a736ecbeef74ad86c`;
- detector-lab evidence integration commit: `52d43351`;
- related paid whole-document GUI call count after completion: five.

## Exact Pangram 4.0 result

- stage: `STAGE_SUCCESS`;
- headline: `AI Detected`;
- Human: `0.1231321841`;
- AI: `0.8768678308`;
- AI-assisted: `0.0`;
- record prediction probability: `0.8717445135116577`;
- History binding: exact UTF-8;
- stored text SHA-256: `fc5a8e49c499c4e4165ff3e6aded4f26c88bacdd9475e9e799a482a19c7a504a`;
- stored word count: 3,585.

No private report URL, History UUID, submitted prose body, credentials, cookies, or unrelated History content is recorded here.

## Displayed localization

The completed report said `AI-generated content appears throughout` and exposed three AI Highlight regions. A read-only dedicated-profile inspection mapped their unique start/end anchors back to the exact boundary:

1. `Introduction` through `I don't confuse that with finishing the deeper trauma work.` — words 0–1,572;
2. `Shaking Qigong / Shaking Medicine` through `...less blocking energy, in my mind.` — words 1,572–3,179;
3. `What I care about is the version of me an hour later...` through `...its intensity does not rescue it.` — words 3,179–3,585.

Together these regions cover all 3,585 whitespace words. The structured History localizer separately failed closed at exact-record rebinding after the complete result and made no detector submission. The display map is localization evidence only; `response.overall` remains score authority.

## Comparison and diagnosis

- exact clean R15 Human: `0.1547368467`;
- prior preservation-clean micro-repair Human: `0.1381948739`;
- article-wide candidate Human: `0.1231321841`;
- change from clean R15: `-0.0316046626`;
- change from the prior micro-repair: `-0.0150626898`.

The article-wide source-grounded reconstruction therefore failed its decision question. It became clearer to independent readers and preserved all registered functions, yet Pangram judged it more AI-like. Because the highlight covers the entire article, it does not authorize deletion or repair of a specific claim. The strongest negative finding is methodological: sentence-level polishing and coordinated explanatory reconstruction both increase the detector-shaped regularity of this article.

The candidate remains non-authoritative. `master.html` is unchanged. R16–R65 and PR #72 prose remain quarantined.

## Alignment

- worker-to-contract: `GREEN`;
- contract-to-owner: `MATCH`;
- completion claim: `WORKING`;
- terminal comparator: `OWNER_OUTCOME_UNMET`;
- next directive: obtain `SUPERVISOR_DECISION SOMATIC-R15-RESULT-007` before another rewrite or detector call.
