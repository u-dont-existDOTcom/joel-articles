# CHAT-TO-CODEX EXECUTION DIRECTIVE — SOMATIC-R15-WHOLE-ARTICLE-REVOICE-001

Task: `somatic-r15-clean-continuation-20260830`

Strategy: `somatic-r15-whole-article-fresh-pro-revoice-v1`

Role: **mechanical Codex executor only**

## Required source state

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Required strategy packet ancestor: `4c6ceb3625326547877608ca92af664e44c5afbc`

Read and obey:

1. `tasks/somatic-r15-clean-continuation-20260830/SUPERVISOR-DECISION-SOMATIC-R15-PROCESS-FAILURE-033.md`
2. `tasks/somatic-r15-clean-continuation-20260830/OUTCOME-PROGRESS-RECEIPT-PROCESS-FAILURE-033.json`
3. `tasks/somatic-r15-clean-continuation-20260830/FRESH-PRO-WHOLE-ARTICLE-REVOICE-001.md`
4. this directive.

The live execution head is the commit containing this directive. Do not reset or discard the process-failure evidence.

## Exact article input

Path:
`articles/somatic-therapies/experiments/R15-EFT-SHAKING-SOCIAL-REPAIR-CANDIDATE-20260831.md`

Expected Git blob:
`22126723d8c585ca8bde54f00c4ade6c925f354e`

Expected UTF-8 SHA-256:
`1e08284ce544b851b516eebdf38f3f8efb2497e477a0104270880f49aab7d81e`

Extract exactly from the first line equal to `# Introduction` through and including the final line equal to:

`**[EXISTING SKY HYPNOSIS NATIVE EMBED — exact object retained in HTML promotion]**`

Do not include the experimental status header before `# Introduction`.

Fail closed if either boundary is absent, duplicated, or reversed.

## Exact prompt construction

Construct one immutable prompt artifact by concatenating, in order:

1. the complete UTF-8 bytes of `FRESH-PRO-WHOLE-ARTICLE-REVOICE-001.md`;
2. two linefeeds;
3. the literal line `--- BEGIN EXACT ARTICLE ---`;
4. two linefeeds;
5. the exact extracted article bytes;
6. two linefeeds;
7. the literal line `--- END EXACT ARTICLE ---`;
8. one terminal linefeed.

Write the exact prompt to:

`tasks/somatic-r15-clean-continuation-20260830/fresh-pro-whole-article-revoice-001/PROMPT.md`

Record its Git blob, UTF-8 SHA-256, byte count, Unicode-character count, whitespace-word count, and terminal-newline state before browser transmission.

Do not alter, normalize, summarize, or annotate the prompt.

## Fresh Pro chat transport

Required capability: browser automation to create and use a genuinely fresh ChatGPT Pro reasoning chat.

Why Codex is required: the current reasoning chat cannot itself operate the local authenticated Brave session or durably capture the external chat response. Codex performs transport and exact evidence capture only.

Requirements:

- create a new ChatGPT conversation, not another turn in the saturated current supervisor chat;
- select Pro / highest-reasoning mode available on the logged-in account;
- do not send prior Pangram scores, fragment results, tail experiments, failed phrasings, or the current conversation history beyond the exact prompt artifact;
- submit the exact prompt once;
- do not add commentary before or after it;
- wait for the complete response;
- preserve the conversation URL;
- do not ask the new chat to inspect GitHub;
- do not ask it to run tools or Pangram.

If the response visibly stops before the required final Sky placeholder, one and only one continuation message is authorized:

`Continue exactly where you stopped. Output only the remaining article through the required final Sky Hypnosis placeholder. Do not repeat earlier text and do not add commentary.`

No other follow-up, repair, critique, or rewrite prompt is authorized.

## Exact response capture

Persist each raw assistant response separately and without normalization under:

`tasks/somatic-r15-clean-continuation-20260830/fresh-pro-whole-article-revoice-001/`

Required files:

- `RAW-RESPONSE-1.md`
- `RAW-RESPONSE-2.md` only if the authorized continuation was used
- `TRANSPORT-RECEIPT.json`

The receipt must record:

- starting and ending article branch heads;
- exact input-candidate identity;
- exact prompt path/blob/SHA/counts;
- fresh chat URL;
- account alias if the local controller uses one, without credentials;
- model/mode visibly selected;
- request submission time and response completion time;
- number of user messages sent;
- every raw response path/blob/SHA/counts;
- whether continuation was required;
- whether response 1 begins with `# Introduction`;
- whether the captured response sequence contains the final required placeholder;
- Markdown heading sequence as observed;
- URL multiset count and the seven native-placeholder strings as observed;
- `article_candidate_created: false`;
- `registered_master_mutations: 0`;
- `detector_actions: 0`;
- `whole_document_calls: 0`;
- `surface_014_packaging_resumed: false`;
- privacy confirmation that no credentials, cookies, storage values, or unrelated chat content were persisted.

Do not concatenate, repair, edit, or promote the response into an article candidate. The current reasoning supervisor owns that decision.

## Forbidden actions

Do not:

- generate or revise article prose;
- choose wording;
- diagnose the article or detector;
- package or continue Surface-014;
- open another fragment experiment;
- run Pangram through API or GUI;
- create a Pangram reservation;
- measure the current candidate;
- modify any article candidate;
- modify `master.html`;
- modify article authority or publication state;
- decide that the response is preservation-clean, detector-ready, or complete;
- ask Joel for new source material.

## Stop boundary

After exact prompt transmission and response capture:

1. commit and push only the prompt, raw response artifact(s), and transport receipt;
2. return one mechanical execution receipt containing exact identities and any transport deviation;
3. set `WAITING_FOR_REASONING_REVIEW`;
4. stop.

No paid or irreversible detector action is authorized by this directive.
