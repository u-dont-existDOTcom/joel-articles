# CHAT-TO-CODEX EXECUTION DIRECTIVE — SOMATIC-R15-BUILD-PROVENANCE-SEMANTIC-PACKET-001

Task: `somatic-r15-clean-continuation-20260830`

Strategy: `somatic-r15-extra-high-semantic-packet-reconstruction-v1`

Role: **mechanical Codex executor only**

## Required source state

Repository: `u-dont-existDOTcom/joel-articles`

Branch: `task/somatic-r15-clean-continuation-20260830`

Required decision/prompt ancestor: `1bd6301410f08ed6e005fd4f2bd74fbcf14d43bb`

Read and obey:

1. `tasks/somatic-r15-clean-continuation-20260830/SUPERVISOR-DECISION-SOMATIC-R15-DIRECT-EXTRA-HIGH-RESULT-035.md`
2. `tasks/somatic-r15-clean-continuation-20260830/HUMANIZATION-FAIL-CLOSED-CONTROL-20260831.md`
3. `tasks/somatic-r15-clean-continuation-20260830/HUMANIZATION-CONTROL-STATE-20260831.json`
4. `tasks/somatic-r15-clean-continuation-20260830/FRESH-EXTRA-HIGH-PROVENANCE-SEMANTIC-PACKET-001.md`
5. this directive.

The live execution head is the commit containing this directive. Do not reset or discard prior artifacts.

## Required capability

Use browser automation only to create a genuinely fresh ChatGPT **Extra High** reasoning chat and transmit/capture exact bytes.

Codex is not the packet reasoner. Codex may only extract the authorized source boundary, compute identities, construct the immutable prompt, perform browser transport, capture the raw response, and persist evidence.

Do not use Pro. If Extra High is not visibly available, stop with `EXTRA_HIGH_MODE_UNAVAILABLE`.

## Exact source article

Path:
`articles/somatic-therapies/experiments/R15-EFT-SHAKING-SOCIAL-REPAIR-CANDIDATE-20260831.md`

Expected Git blob:
`22126723d8c585ca8bde54f00c4ade6c925f354e`

Expected UTF-8 file SHA-256:
`1e08284ce544b851b516eebdf38f3f8efb2497e477a0104270880f49aab7d81e`

The exact Introduction source boundary for this packet is:

- begin at the line exactly `# Introduction`;
- include that heading and the first four prose paragraphs;
- stop immediately before the line exactly `## Your Physical State Can Change What Therapy Does`;
- do not include the `## Your Physical State Can Change What Therapy Does` heading or any later prose.

Fail closed if either heading is absent, duplicated, reversed, or the boundary does not contain exactly four nonempty prose paragraphs beneath `# Introduction`.

Write the exact extracted boundary, without normalization, to:

`tasks/somatic-r15-clean-continuation-20260830/semantic-packet-introduction-001/INTRO-SOURCE.md`

## Mechanical source manifest

Before browser transport, create:

`tasks/somatic-r15-clean-continuation-20260830/semantic-packet-introduction-001/INTRO-SOURCE-MANIFEST.json`

Record:

- source article path/blob/SHA-256;
- exact extracted boundary path/blob/SHA-256 once committed or staged identity where applicable;
- boundary UTF-8 bytes, Unicode characters, whitespace words, terminal-newline state;
- exact heading text;
- four paragraph IDs `INTRO-P1` through `INTRO-P4`;
- for each paragraph: exact UTF-8 SHA-256, byte count, Unicode-character count, whitespace-word count, and exact first/last 32 UTF-8 characters or shorter full text when shorter;
- exact count and identity of Markdown links in the four paragraphs;
- confirmation that no later article material is present.

This is deterministic evidence only. Do not classify provenance yourself.

## Authority bundle

Construct the immutable reasoning prompt using complete UTF-8 contents of the following exact files from the live branch, in this order:

1. `tasks/somatic-r15-clean-continuation-20260830/FRESH-EXTRA-HIGH-PROVENANCE-SEMANTIC-PACKET-001.md`
2. `tasks/somatic-r15-clean-continuation-20260830/SUPERVISOR-DECISION-SOMATIC-R15-DIRECT-EXTRA-HIGH-RESULT-035.md`
3. `tasks/somatic-r15-clean-continuation-20260830/HUMANIZATION-FAIL-CLOSED-CONTROL-20260831.md`
4. `tasks/somatic-r15-clean-continuation-20260830/HUMANIZATION-CONTROL-STATE-20260831.json`
5. `tasks/somatic-r15-clean-continuation-20260830/OWNER-CORRECTION-CHAT-OWNS-HUMANIZATION-20260831.md`
6. `tasks/somatic-r15-clean-continuation-20260830/OWNER-CORRECTION-THIN-AUTOMATION-20260831.md`
7. `tasks/somatic-r15-clean-continuation-20260830/DIRECT-OWNER-SOURCE-RECOVERY-MATRIX-20260831.md`
8. `tasks/somatic-r15-clean-continuation-20260830/R15-DIRECT-OWNER-VOICE-WHITELIST-20260830.md`
9. `tasks/somatic-r15-clean-continuation-20260830/R15-ARTICLE-WIDE-HUMANIZATION-WHITELIST-20260830.md`
10. `tasks/somatic-r15-clean-continuation-20260830/OWNER-SOURCE-RECEIPT.json`
11. the generated `INTRO-SOURCE-MANIFEST.json`
12. the exact generated `INTRO-SOURCE.md`

For files 2 through 12, surround each exact content payload with these literal markers, replacing PATH with the exact repository-relative path:

`--- BEGIN AUTHORITY FILE: PATH ---`

one linefeed, then exact file bytes, then one linefeed, then:

`--- END AUTHORITY FILE: PATH ---`

Use two linefeeds between complete file blocks.

For file 1, place its exact bytes first without an opening marker, then two linefeeds before file 2.

Write the resulting immutable prompt to:

`tasks/somatic-r15-clean-continuation-20260830/semantic-packet-introduction-001/PROMPT.md`

Record its SHA-256, byte count, Unicode-character count, whitespace-word count, and terminal-newline state before browser transmission.

Do not normalize, summarize, annotate, or reorder any authority content.

## Fresh Extra High packet-builder transport

- create a new ChatGPT conversation;
- visibly select GPT-5.6 Sol Extra High / highest available Extra High reasoning setting, not Pro;
- do not reuse the prior Extra High writer conversation;
- do not transmit the prior Extra High or Pro rewritten articles;
- submit the exact `PROMPT.md` once, with no commentary before or after it;
- wait for the complete structured response;
- preserve the conversation URL;
- do not ask the chat to inspect GitHub, run tools, write prose, or run Pangram.

If the response visibly truncates before `## Packet verdict`, exactly one continuation message is authorized:

`Continue exactly where you stopped. Output only the remaining provenance/semantic packet through the required final packet-verdict line. Do not repeat earlier material and do not write publication prose.`

No other follow-up is authorized.

## Exact response capture

Persist raw assistant response(s) without normalization under:

`tasks/somatic-r15-clean-continuation-20260830/semantic-packet-introduction-001/`

Required files:

- `RAW-PACKET-RESPONSE-1.md`
- `RAW-PACKET-RESPONSE-2.md` only if the one authorized continuation was used
- `TRANSPORT-RECEIPT.json`

The receipt must record:

- starting and ending article branch heads;
- exact source article identity;
- exact Introduction source/manifest identities;
- exact prompt path/blob/SHA/counts;
- fresh chat URL;
- visible model/mode selection proving Extra High and not Pro;
- request submission/completion times;
- number of user messages;
- raw response paths/blobs/SHA/counts;
- whether continuation was used;
- whether response 1 begins exactly `# INTRODUCTION PROVENANCE + SEMANTIC PACKET`;
- whether the final captured response sequence ends in one required packet verdict;
- `publication_prose_generated_by_codex: false`;
- `article_candidate_created: false`;
- `article_candidate_mutations: 0`;
- `registered_master_mutations: 0`;
- `detector_actions: 0`;
- `pangram_reservations: 0`;
- `whole_document_calls: 0`;
- `fragment_detector_families_opened: 0`;
- privacy confirmation that no credentials, cookies, storage values, authorization headers, or unrelated chat content were persisted.

## Forbidden actions

Do not:

- classify provenance yourself;
- create semantic packets yourself;
- generate, revise, repair, or choose article prose;
- concatenate the packet response into a publication candidate;
- use the raw Extra High writer response as source material;
- use the raw Pro response as source material;
- run any detector or Pangram action;
- open a fragment experiment;
- modify any article candidate;
- modify `master.html`;
- update registered article authority/publication state;
- route to Pro;
- ask Joel for new source material.

## Stop boundary

After exact prompt transport and raw packet-response capture:

1. commit and push only the Introduction source/manifest, prompt, raw packet response(s), and transport receipt;
2. return one mechanical execution receipt with exact identities and deviations;
3. set `WAITING_FOR_REASONING_REVIEW`;
4. stop.

The current reasoning supervisor must review and freeze the provenance/semantic packet before any prose writer is invoked. No detector action is authorized by this directive.
