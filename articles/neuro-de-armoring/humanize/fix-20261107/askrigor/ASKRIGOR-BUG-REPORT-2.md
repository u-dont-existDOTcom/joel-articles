# Bug report for AskRigor: in this app the AI never sees the protocol, the records or the papers

Joel asked for this on 2026-11-07 at 11:58 UTC: "send askrigor a bug report when you figure out why it's not working
for you, then continue working". It goes to AskRigor's lesson queue with `submit_lesson_candidate`. His message gives
the yes, so it is sent as written below.

## What I found (2026-11-07, about 12:00 UTC)

Calls from this session (Claude's agent harness in a cloud session started from the Claude app, built on Claude Code):

| Call | What reached me |
| --- | --- |
| `manage_research_access` inspect | the full status text (active, free contributor mode) |
| `get_protocol_manifest` universal / hrp | versions and SHA-256 in the text (Universal 20.5.46 `e313306b…`, HRP 20.6.40 `afd3d881…`) |
| `verify_protocol_integrity` universal | "verified", with the SHA-256 |
| `load_protocol` universal, index | one sentence naming the core sections; no section list |
| `load_protocol` universal, core | "Loaded … page 1 of 1 (exact canonical bytes of each, in this order, a blank line between two)." **and no protocol text** |
| `fetch_pubmed_record` 40957579 | the access status and the research_receipt; **no title, authors or abstract** |

The cause, in AskRigor's public source (main `ac93e5c9`, 2026-11-07 01:11 UTC):

- `apps/research-mcp/src/tool-result.ts`, `successfulToolResult(text, structuredContent)` returns
  `content: [{ type: "text", text }]` with the one-line summary, and puts the payload (`text: textPage.text` for
  `load_protocol`, the section list for the index) only in `structuredContent`.
- The open full-text route (`invokeOpenFullTextMcp` in `register-tools.ts`) does the same: its text is
  "acquire open full text completed." plus notes and the receipt; the page text is in `structuredContent` only.
- This app passes the AI only the `content` text blocks. So the AI reads "exact canonical bytes" loaded, and none
  arrived.
- The MCP specification says a tool that returns structured content SHOULD also return the serialized JSON in a
  TextContent block, for backwards compatibility: https://modelcontextprotocol.io/specification/draft/server/tools
- AskRigor's own code already knows part of this: a comment in `youtubeToolResult` says clients such as Claude show
  only the text of an *error* result. Here it holds for successful results too.

Meanwhile: the protocol files in AskRigor's public repository (`protocols/Universal_Instructions.xml`,
`protocols/HRP_Full.xml`) have the same SHA-256 as the running versions, so this session can read the canonical text
there. Citation records and abstracts come from Europe PMC through the browser.

## The report, as sent

- **Category:** tool_semantics
- **General lesson:** When an app passes only a tool result's text blocks to the AI, AskRigor should put what the AI
  must read (protocol text, citation records, full-text pages, the section index) in the text as well as in the
  structured part, because otherwise the AI sees only a line saying the content was loaded and cannot load the
  protocol, read a record or audit a paper.
- **What happened:** see the table above. The load_protocol summary says the canonical bytes were loaded, which invites
  an AI to believe it read the protocol when it did not.
- **What should happen:** load_protocol's text carries the page's canonical bytes (as its summary already promises);
  fetch_pubmed_record and the searches carry each record's title, authors, journal, date, identifiers and abstract;
  acquire and continue_open_full_text carry the page text; the index carries the section names and summaries. If a
  result must stay in the structured part only, the text says so, so a text-only app reports a failed load instead.
- **Why:** successfulToolResult and the full-text and PubMed result builders put a one-line summary in the text and
  the payload only in the structured part, and this app shows the AI only the text.
- **Part to change:** tool: successfulToolResult and the load_protocol, PubMed and open full-text result text.
- **Existing rules:** HRP AuthoritativeProtocolLoad (applied but insufficient: it needs load_protocol's exact canonical
  text, which a text-only app never receives); HRP NoSilentAccessFailure (applied but insufficient: disclosure depends
  on the AI noticing, and the summary says the bytes were loaded).
- **Made-up test:** a test client keeps only `content[].text`, calls load_protocol (universal, core) and
  fetch_pubmed_record for a fixture PMID. Expected: the text holds the core sections' canonical bytes (their SHA-256
  matches scope_sha256) and the fixture's title and abstract. Control: a client reading the structured part gets the
  same payload there, unchanged.
- **Detailed report** (detailed reports are on for this account): the steps, the cause (high confidence), the
  proposed change (serialize what the AI needs into the text, per the MCP spec; keep the text from claiming a load the
  text does not carry; point to the public protocol file at the matching SHA-256 as a fallback; a text-only client
  test), and what stays uncertain (which other apps drop the structured part).

## Outcome

**Sent** at about 12:06 UTC with `submit_lesson_candidate` (category tool_semantics, evidence tool_receipt_conflict,
consent once, with the detailed report). AskRigor's answer: "Lesson saved for review as ARL-0059."
