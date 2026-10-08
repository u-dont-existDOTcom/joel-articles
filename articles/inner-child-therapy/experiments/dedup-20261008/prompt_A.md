# Task: find the repeats in a long article

You are checking a long self-help article (about inner child work) for points it makes more than once. More text is about to be added to it, and the author asked that nothing be duplicated. Nobody has checked the article as a whole for this before; earlier checks only compared a paragraph with its neighbors.

Read the whole of ./article_blocks.md with the Read tool (about 11,000 words; read every block, in several calls if needed). Each block is numbered [B#]. Headings start with #, ##, ###. Two bracketed notes stand in for embedded posts.

## What counts

A repeat is the same point made twice: the same claim, instruction, caution, reassurance, example or permission, in the same situation or close enough that a reader would feel told the same thing again. It can be far apart (different sections) or adjacent. Shared words alone don't count, and neither does a theme the article keeps developing, if each passage adds a distinct step. A deliberate callback that a reader would recognize as one ("like the seat belt earlier") is not a repeat, but list it separately if it relies on something sections back.

Also list any two passages that contradict each other or pull in opposite directions without saying why.

## Where to look hardest

Everything under "# Before You Try to Go Deep" ([B32] to [B77]) was put together from several sources at different times (the author's own paragraphs, paragraphs written from his guide, and his recent rewrites), so check every block there against every other block there, and against the rest of the article. Then check the rest of the article against itself.

## Output

Write your findings to ./OUT_FILE with the Write tool, in plain English:

1. A numbered list of repeats, in article order. For each: the block numbers; a short exact quote from each instance (under 25 words each); the shared point in a few words; whether the later instance adds something the earlier one doesn't (say what) or a reader would feel told the same thing again; and which instance carries the point better or sits in the more natural place, with a one-line reason.
2. Contradictions, the same way.
3. The five repeats a reader would most notice, by number.

Don't suggest rewrites and don't comment on style or quality. Don't invent quotes: every quote must be copied exactly from the file. When you're done, reply with one line: how many repeats and contradictions you found.
