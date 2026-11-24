# The Substack system lane: start here

A lane of its own, handed off by the bad trips lane on 2026-11-20 at Joel's request ("you can hand all this work off to a
separate lane so you can continue on bad trips humanization"). To start it, paste into a new chat:

> Read https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/proposals/2026-11-20-substack-system-HANDOFF.md and start the Substack system lane from it.

The brainstorm it starts from, with what others already use and the three ways it weighed:
[the proposal](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/proposals/2026-11-20-substack-system.md).

## What Joel asked for, in his words

2026-11-20 22:40 UTC: "i'm also wondering if we should create or adopt some system for my whole substack so we can ensure
we keep track of stuff like this. like if i have a vid on systema breathing, anytime i mention it in any article you
already know to link that one, or if any article mentions another, it links that, or if there are things that should be
like snippets that are the same in different articles we can store them once rather than twice or link snippets if they
depend on each other, stuff like that. can we brainstorm how to design or adopt that system?"

2026-11-20 23:40 UTC, answering the proposal's four questions:

> 1. b, i don't want to write stuff in obsidian, not sure how that would transfer to substack with embeds and such, but
> open to your suggestions
> 2. substack has includes but they aren't synced
>
> substack has Notes, which are synced, so we can link to notes or we can embed notes (not the full note gets shown).
> However, it may not always be appropriate to embed a note instead of directly putting the text tehre, since the full
> note isn't shown in the article until they click it.
> idk if you can find all my notes, most of them were jst one time things that would not be included in articles, and i
> think all the ones that would be included already are included in some article or another.
> 3. your pick yes
> 4. yes. we should also have a substack-wide conflict checker. so for example my hypnosis guide and my hearthwork guide
> are heavily based on my inner child guide. when i update my inner child guide, those should also be updated (but
> carefully so as not to break pangram score if they are humanized already). if i say something new about any topic that
> i've already covered, you should ask if i'd like to add that where it belongs in that other topic or how to handle that.
> like if i make a new post talking about a nibbana meditation i found, you might ask if i'd like to add that into my
> nibbana guide in the relevant section or update the part that it would change. I'm also hoping this system will help in
> case substack bans me, then i can just copy to a new substack or put on my vps.
>
> you can hand all this work off to a separate lane so you can continue on bad trips humanization

## What that settles

1. **Where it lives: a registry in Git** (the proposal's B), read by a check every lane runs. No Obsidian: he doesn't
   want to write there, and it isn't clear how its embeds would reach Substack. He is open to suggestions, so a tool that
   would only be a view of the same Git files can still be suggested, with how it carries his embeds to Substack.
2. **Shared passages:** one home article that the others link to, with the text copied into a post where the reader needs
   the words in place. Substack's own includes aren't synced. A Note is: a post can link to it or embed it, but an embed
   shows only part of the Note until the reader clicks, so it fits only where a short synced pointer is enough. Don't
   hunt for all his Notes: most were one-offs, and the ones that matter are already in some article.
3. **Links:** the first mention of a thing or a post in each post, and in a long guide the first in each section (a
   reader in an emergency lands in the middle of the bad trips guide).
4. **Scope:** every post on ibogaqueen.substack.com and his u-dont-exist.com guides; his own things first (videos,
   guides, apps, products), then the outside sources he cites often. And three things he added:
   - **A conflict checker across posts.** Some posts are built on others: his hypnosis guide and his Hearthwork guide are
     heavily based on his inner child guide. When the source changes, the posts built on it are updated too, carefully,
     so a post that is already humanized keeps its Pangram readings.
   - **A new point on a covered topic gets a question.** When he says something new about a topic one of his posts
     already covers, ask whether to add it there, where it belongs, or to update the part it changes. His example: a new
     post about a Nibbāna meditation he found → his Nibbāna guide's section on it.
   - **Everything can move.** If Substack bans him, he can copy it all to a new Substack or put it on his VPS.

## The design, with his additions

The proposal's B, plus:

- **The lists.** THINGS (each thing he links: names and aliases, its one link; the Systema video, linked in the bad trips
  guide on 2026-11-20, is the first), ARTICLES (every post: title, Substack address, his short address, post id, its
  section-links file if it has one), PASSAGES (each passage two posts share, its home, where else it is used, what it
  depends on), and two new ones from his answers: **BUILT-ON** (which sections of which post are built on which sections
  of another: hypnosis and Hearthwork on inner child first) and **TOPICS** (each topic his posts cover, and the post and
  section that covers it). BUILT-ON has started, as [articles/BUILT-ON.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/BUILT-ON.json)
  (the contents lane, 2026-11-24, lesson toc-2026-11-24b, after he added the somatic guide as a source of the hypnosis
  guide and asked why he had to say it again): extend that file rather than starting another, and `lane_push.py` already
  prints its entries for the article it pushes.
- **The check**, in every article pass (code finds the candidates, a fresh model judges each in its sentence): a mention
  with no link or the wrong one; another post named without its link; a shared passage that has drifted from its home; a
  section whose source changed since it was last brought in line (BUILT-ON); and a new point on a topic another post
  covers (TOPICS), which goes to him as a question: add it there, update the part it changes, or leave it.
- **Bringing a built-on post in line.** When the source post changes, list the sections built on the changed ones. Each
  change goes through the humanization rules of the post it lands in: a changed paragraph is checked by itself and goes
  in only at Human High ([tools/humanization/apply_gate.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/apply_gate.py)); his own words go to him; the post on Substack is updated only
  with his yes (gate E323). A paragraph that reads Human High now and would only gain a fact may be better left with a
  link to the source than rewritten.
- **Contradictions across posts.** The contradictions check (gate neuro-2026-11-20a, [tools/humanization/contradictions.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/contradictions.py))
  run on posts that share a topic, so two posts can't give two doses or two rules for the same thing without the text
  saying why.
- **Everything can move.** Substack's own export (Settings, then Exports, then "Create new export") builds a zip of the
  posts (as HTML), the subscriber list and the stats. Ghost, which is open source and can run on his VPS, has a Substack
  migrator for posts and members; WordPress has a Substack Importer; or a static site can be built from the Markdown in
  Git. The lane keeps a current copy of every post with its images and embeds listed, and shows once that it rebuilds.
  **The subscriber list is private data: it never goes into this public repository** ([AGENTS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/AGENTS.md), stop conditions); it
  lives where he says (his VPS, his computer). Where the posts' copies and images live is his call (this repository, a
  private one, his VPS): ask before making one.

## Rules this lane follows

[AGENTS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/AGENTS.md) at the root, in full: the mailbox check every turn, merging main first, pushing only with
[tools/humanization/lane_push.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/lane_push.py), each lesson in a file of its own, links for him and never repository paths, Markdown in
Git for anything he will come back to. In particular:

- [articles/INDEX.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/INDEX.json) registers only articles whose master he has named: copies of his posts made for the backup are
  not registered articles, and go where he says.
- Lists find candidates; meaning goes to a model (UDA's [reasoning-selection pattern](https://github.com/u-dont-existDOTcom/universal-dev-architecture/blob/main/patterns/reasoning-selection.md), the pattern-matching fit check).
- Pangram checks run in his account in the web app, never handed to him; no whole-article check of a Substack post; every
  result with each window's confidence and its link.
- Section links follow gate inner-child-2026-11-20c ([tools/humanization/section_refs.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/section_refs.py),
  [tools/humanization/section_links.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/section_links.py), [articles/inner-child-therapy/SECTION-LINKS.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-child-therapy/SECTION-LINKS.json) as the model).

## First steps

1. Set up the lane: a branch `claude/substack-system-<date>` from main's tip, its mailbox record
   ([tools/humanization/lane_mailbox.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/lane_mailbox.py)), and a home for its state, handoff and questions page (where, decided with the
   validator: `python3 scripts/validate_content_repository.py --root .` checks only registered articles' folders).
2. The inventory: every post (title, address, post id, date), from the publication's public archive, and each
   u-dont-exist.com address resolved to the post it opens.
3. The copy that can move, first, since it protects everything else: ask him where it lives and whether he will run
   Substack's export or wants it run in his signed-in browser.
4. THINGS from every link in every post, grouped by thing; where one thing has two links, or a mention has none, a short
   question list for him (the bad trips guide had his Self-Hypnosis guide as both `hypnosis.u-dont-exist.com` and
   `hypnoisis.u-dont-exist.com`).
5. BUILT-ON: hypnosis and Hearthwork on inner child, from his words; ask him which others; a fresh reader pairs their
   sections.
6. TOPICS, then the check (a new tool beside the others, with tests), then its step in [docs/FIXING-AN-ARTICLE.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/FIXING-AN-ARTICLE.md), and a first
   run on one article with its lane.

## Questions to ask him first

- Where does the copy of everything live (his VPS, a private repository, this one for the posts but never the subscriber
  list)?
- Will he run Substack's export, or should the lane run it in his browser while he is signed in?
- Which posts besides his hypnosis and Hearthwork guides are built on another post?
