# CHAT-TO-CODEX EXECUTION DIRECTIVE — SOMATIC-R15-DIRECT-EXTRA-HIGH-WHOLE-ARTICLE-001

Task: `somatic-r15-clean-continuation-20260830`

Strategy: `somatic-r15-direct-extra-high-whole-article-v1`

Role: **mechanical Codex executor only**

## Required source state

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Required decision/prompt ancestor: `5edd8853ad858970509f409bd6c6703ea93a2ca2`

Read and obey:

1. `tasks/somatic-r15-clean-continuation-20260830/OWNER-CORRECTION-THIN-AUTOMATION-20260831.md`
2. `tasks/somatic-r15-clean-continuation-20260830/SUPERVISOR-DECISION-SOMATIC-R15-WHOLE-ARTICLE-REVOICE-RESULT-034.md`
3. `tasks/somatic-r15-clean-continuation-20260830/FRESH-EXTRA-HIGH-WHOLE-ARTICLE-001.md`
4. this directive.

The live execution head is the commit containing this directive. Do not reset or discard the preserved Pro artifact or process-failure evidence.

## Exact article input

Path:
`articles/somatic-therapies/experiments/R15-EFT-SHAKING-SOCIAL-REPAIR-CANDIDATE-20260831.md`

Expected Git blob:
`22126723d8c585ca8bde54f00c4ade6c925f354e`

Expected UTF-8 file SHA-256:
`1e08284ce544b851b516eebdf38f3f8efb2497e477a0104270880f49aab7d81e`

Expected exact extracted article SHA-256 from the prior successful transport:
`7b96aa6e4218039b57016b48019f44c84d3b4df957ff1b483ee540e8ba74101a`

Extract exactly from the first line equal to `# Introduction` through and including the final line equal to:

`**[EXISTING SKY HYPNOSIS NATIVE EMBED — exact object retained in HTML promotion]**`

Do not include the experimental status header before `# Introduction`.

Fail closed if either boundary is absent, duplicated, reversed, or the extracted SHA differs.

## Exact prompt construction

Construct one immutable prompt artifact by concatenating, in order:

1. complete UTF-8 bytes of `FRESH-EXTRA-HIGH-WHOLE-ARTICLE-001.md`;
2. two linefeeds;
3. literal line `--- BEGIN EXACT ARTICLE ---`;
4. two linefeeds;
5. exact extracted article bytes;
6. two linefeeds;
7. literal line `--- END EXACT ARTICLE ---`;
8. one terminal linefeed.

Write:

`tasks/somatic-r15-clean-continuation-20260830/fresh-extra-high-whole-article-001/PROMPT.md`

Record Git blob, UTF-8 SHA-256, bytes, Unicode characters, whitespace words, and terminal-newline state before browser transmission.

Do not normalize, summarize, annotate, or repair the prompt.

## Fresh Extra High writer transport

Required capability: browser automation to create and use a genuinely fresh ChatGPT reasoning chat with **Extra High** thinking selected.

Why Codex is required: only for local authenticated browser transport and durable exact response capture. Codex is not the writer or supervisor.

Requirements:

- create a new ChatGPT conversation;
- explicitly select Extra High thinking/reasoning mode, not Pro;
- if Extra High is not visibly available, stop and report `EXTRA_HIGH_MODE_UNAVAILABLE`; do not substitute Pro or another mode;
- do not use or reopen the prior Pro writer conversation;
- do not send the prior Pro response;
- do not send prior Pangram scores, fragment results, red windows, failed phrasings, or process history beyond the exact frozen prompt;
- submit the exact prompt once with no surrounding commentary;
- wait for the complete response;
- preserve the conversation URL;
- do not ask the writing chat to inspect GitHub, run tools, or run Pangram.

If response visibly stops before the final Sky placeholder, one and only one continuation message is authorized:

`Continue exactly where you stopped. Output only the remaining article through the required final Sky Hypnosis placeholder. Do not repeat earlier text and do not add commentary.`

No other follow-up, critique, repair, detector feedback, or rewrite prompt is authorized in this execution cycle.

## Exact response capture

Persist each raw assistant response separately without normalization under:

`tasks/somatic-r15-clean-continuation-20260830/fresh-extra-high-whole-article-001/`

Required:

- `RAW-RESPONSE-1.md`
- `RAW-RESPONSE-2.md` only if the authorized continuation was required
- `TRANSPORT-RECEIPT.json`

Receipt must record:

- starting and ending article branch heads;
- exact source-candidate and extracted-article identities;
- exact prompt path/blob/SHA/counts;
- fresh chat URL;
- visible model/mode selection proving Extra High;
- request submission and completion times;
- number of user messages sent;
- raw response paths/blobs/SHA/counts;
- whether continuation was required;
- whether response 1 begins with `# Introduction`;
- whether response sequence contains the final required placeholder;
- heading sequence observed;
- URL multiset count and seven native-placeholder strings observed;
- `prior_pro_response_transmitted: false`;
- `article_candidate_created: false`;
- `registered_master_mutations: 0`;
- `detector_actions: 0`;
- `whole_document_calls: 0`;
- `fragment_experiments_opened: 0`;
- privacy confirmation that no credentials, cookies, storage values, or unrelated chat content were persisted.

Do not concatenate, repair, edit, compare stylistically, promote, or materialize the response into an article candidate. The reasoning supervisor owns preservation/editorial adjudication.

## Forbidden actions

Do not:

- generate or revise article prose;
- choose wording;
- use the prior Pro response as a style or sentence donor;
- diagnose the article or detector;
- resume Surface-014 or package it as progress;
- open any fragment experiment;
- run Pangram through API or GUI;
- create a Pangram reservation;
- measure either the current candidate or the prior Pro response;
- modify any article candidate;
- modify `master.html`;
- modify article authority/publication state;
- decide whether the new Extra High response is preservation-clean, detector-ready, or complete;
- ask Joel for new source material.

## Stop boundary

After exact prompt transmission and raw response capture:

1. commit and push only prompt, raw response artifact(s), and transport receipt;
2. return one mechanical execution receipt with exact identities and deviations;
3. set `WAITING_FOR_REASONING_REVIEW`;
4. stop.

No paid or irreversible detector action is authorized by this directive.
