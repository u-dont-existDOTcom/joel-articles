# Custom GPT configuration

## Recommended name
**Romance Advice Q&A — Joel Rosenblum**

Alternative:
**Romance Advice I Wish My Parents Taught Me — Q&A**

## Description
Ask questions about Joel Rosenblum’s long-form romance guide. The GPT answers from the guide first, connects ideas across sections, points you to relevant passages and resources, and clearly labels anything that goes beyond the article.

## Conversation starters
- What does the guide say about whether I should be in a relationship at all?
- How does community change romantic relationships according to the guide?
- What does Joel mean by idealization done right?
- I’m stuck in a recurring conflict with my partner. Which parts of the guide are relevant?

## Knowledge files to upload
Upload exactly these three files from the `knowledge/` folder:
1. `01-ROMANCE-GUIDE-R7.md`
2. `02-SECTION-INDEX.md`
3. `03-MEDIA-AND-LINK-MAP.md`

Do **not** upload the raw Substack HTML as Knowledge. It is useful as publication/archive authority, but the native markup makes it a worse retrieval source than the clean Markdown package.

## Instructions
Paste the complete contents of `GPT-INSTRUCTIONS.md` into the GPT’s **Instructions** field.

## Capabilities
Recommended:
- **Web search: ON** — useful when a reader explicitly asks to verify a claim, inspect linked research/video, compare frameworks, or get current information.
- **Image generation: OFF** — not needed for guide Q&A.
- **Code Interpreter / Data Analysis: OFF** — not needed for the ordinary reader use case.
- **Actions/Apps: none**.

If you want the GPT to be a *strict closed-book companion* that never goes beyond the article, turn Web search OFF. I recommend leaving it ON because the Instructions already force a clear “guide vs outside guide” boundary.

## Sharing
Use the GPT’s share/publish control to create the reader-facing link.

Before sharing publicly, test in Preview using `TEST-PROMPTS.md`.

## Optional current-article link
If you have the final public Substack URL, add it to the GPT description or append this line to the Instructions:

`Current published guide: YOUR_URL_HERE`

That gives readers an escape hatch when the Knowledge package becomes older than the live article.
