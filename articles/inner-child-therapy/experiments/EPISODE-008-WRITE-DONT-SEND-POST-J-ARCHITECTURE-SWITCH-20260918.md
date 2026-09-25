# Episode 008 — Write It. Don't Send It Yet — post-J architecture switch

Date: 2026-09-18
Status: **TWO OPENING-ONLY REGRESSIONS / SAME-METHOD THRESHOLD REACHED / MOVE OWNER ANCHOR EARLIER**

Best anchored control:
- H: AI 0.3021335304 / Human 0.6978664994.

Opening-only mutations:
- I: AI 0.4466216266;
- J: AI 0.5706174374.

Both regressed.

## Structural inference

H's Human share (~69.8%) is very close to the combined share of:
- the 113-word owner anchor;
- the unchanged post-anchor model region.

Its report also says AI appears in the earlier part.

This supports treating H's opening as the remaining dominant red surface.

Two attempts to make that opening stylistically more Human failed.

## New architecture

Do not write another 70–80 word opening.

Move the owner Human anchor much closer to the beginning:

1. one minimal private-draft sentence before the anchor;
2. exact owner anchor;
3. one compact post-anchor editing sentence carrying apology/no/request/no-send functions;
4. preserve H's already successful inward-care ending.

This changes the geometry rather than paraphrasing the same opening.

The owner anchor remains byte-for-byte exact.