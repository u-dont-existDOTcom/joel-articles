# One system for the whole Substack: links, articles and shared passages (a brainstorm)

Joel, 2026-11-20 22:40 UTC: "i'm also wondering if we should create or adopt some system for my whole substack so we can
ensure we keep track of stuff like this. like if i have a vid on systema breathing, anytime i mention it in any article you
already know to link that one, or if any article mentions another, it links that, or if there are things that should be
like snippets that are the same in different articles we can store them once rather than twice or link snippets if they
depend on each other, stuff like that. can we brainstorm how to design or adopt that system?"

Status: decided (his answers of 2026-11-20 23:40 UTC, at the end) and handed to a lane of its own: [the lane's handoff](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/proposals/2026-11-20-substack-system-HANDOFF.md), which carries his answers and the three things he added (a conflict checker across posts, asking where a new point belongs, and a copy of everything that can move to a new Substack or his VPS). Nothing is built yet.

## What it has to do

1. **One link for each thing he mentions.** A video he likes (the Systema breathing one), each of his guides, apps and
   products, the outside sources he keeps citing. Any article that mentions one links that one, the same address every
   time. The bad trips guide shows why: it linked his Self-Hypnosis guide as `hypnosis.u-dont-exist.com` in one place and
   `hypnoisis.u-dont-exist.com` in another, and only the contradictions check (2026-11-20) caught it.
2. **Every article that mentions another links to it**, and to the section meant, when a section is meant.
3. **A passage said in several articles is kept once.** Either it lives in one article and the others link to it, or it
   is stored once and copied into each post from that one copy. When one passage depends on another (a dose and the
   warning that goes with it), that is written down, so changing one flags the other.

## What already exists in his repository

- Inside one post, point 2 is done: every mention of a section links to it (gate inner-child-2026-11-20c).
  [tools/humanization/section_refs.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/section_refs.py) finds the mentions, and a section-links file beside the article (the inner child
  guide's, [articles/inner-child-therapy/SECTION-LINKS.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-child-therapy/SECTION-LINKS.json), so far) holds every heading's anchor and every link to it,
  changed only through [tools/humanization/section_links.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/section_links.py) (its rename command).
- Inside one post, point 3 is done too: a repeat can become a pointer with a link to the first telling (gate
  inner-child-2026-11-20h).
- [ARTICLE-META-MAP.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/ARTICLE-META-MAP.md): a map of the registered articles and the links between them, kept by hand.
- Per article: a keep-as-is list (the bad trips guide's: [articles/bad-trips/KEEP-AS-IS.json](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/KEEP-AS-IS.json); what he says stays), fidelity keys (doses and the warnings that go with them, which must
  not change), [tools/humanization/post_embeds.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/post_embeds.py) (a post's pictures and videos), the contradictions check.

What's missing is the same thing across posts: nothing lists the things he links, his posts, or the passages two posts
share.

## What others already do (adopt rather than invent)

- **Technical writers' single sourcing.** DITA, the documentation standard, has two ideas that fit exactly: a *key* (a
  name defined once as a link or a term; every page uses the name, so changing the link changes it everywhere) and a
  *content reference* (a passage written once and pulled into every page that needs it). Docs tools carry the same ideas
  under other names: Sphinx substitutions and includes, Hugo and Eleventy "partials", MDX imports.
- **Note apps.** Obsidian gives each note aliases, lists the "unlinked mentions" of a note's name across the vault (point
  1, found for you), shows backlinks (point 2), and embeds one note's section or paragraph inside another (point 3).
  Logseq and Roam do the same with block references; Notion's synced blocks show one block in many pages, edited once.
- **Substack itself** (corrected by Joel, 2026-11-20 23:40 UTC): "substack has includes but they aren't synced".
  Notes are synced: a post can link to a Note or embed it, but an embed shows only part of the Note until the reader
  clicks it, so it isn't always right in place of the text. So a passage kept once is either copied into each post
  when the post is updated, linked to one place, or, where a short synced pointer is enough, an embedded Note.

## Three ways to build it

**A. An Obsidian vault as the home of everything.** His articles, the things he links and the shared passages as notes,
with aliases, embeds and backlinks doing the tracking, and a step that turns a note into a post for Substack. Pro: the
tracking comes built in, and it is pleasant to browse. Con: it changes where and how he writes; the Substack editor is
still where posts go out, so the embeds need an export step anyway; every lane's tools would have to read the vault.

**B. A registry in Git, checked by a tool every lane runs** (the DITA ideas, done the light way, in joel-articles):
- a THINGS list: each thing he links, with its names and aliases, its one link, and a note on when to link a
  section of it instead. The first entry would be the Systema video, which went into the bad trips guide by hand today:
  names "Systema breathing", "Systema continuous partial breathing"; link `https://www.youtube.com/shorts/Nar2-nvomAk`.
- an ARTICLES list: every post, with its title, Substack address, his short address, its post id and its section-links
  file if it has one. [ARTICLE-META-MAP.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/ARTICLE-META-MAP.md) would be built from it instead of by hand.
- a PASSAGES folder: each passage two or more posts share, once, with where it is used and what it depends on. A term
  he explains the same way in several posts (DMSO, humic acid, the Hunter criteria) can be one of these too, so each post
  explains it his way where it first uses it (his rule: every term explained once, where first used).
- A check (a new tool, substack_check) in every article pass. Code finds the candidates (each
  registered name or alias, each post title, each passage's first words); a fresh model reads each candidate in its
  sentence and judges it, since "systema" in a sentence about something else isn't a mention (the repository's own rule:
  lists find candidates, meaning goes to a model). It flags: a mention with no link, or with an old or wrong link; a
  mention of another post with no link; a passage whose copy has drifted from its stored version; a passage that looks
  like one another post already has; and, when a stored passage changes, every post that now needs updating.
- A stored passage copied into a new post gets its own Pangram check there: windows change with their neighbours (gate
  E197: a moved section gets its own check).

Pro: nothing changes in how he writes; Git stays the one place both accounts share; every lane gets it with its next
merge of main. Con: a first pass over all his posts to fill it.

**C. Link more, copy less.** Most shared passages get one home article; every other post says it in a line and links to
that section ("more on that in X"), the inner child rule made Substack-wide. A passage is stored and copied only where a
reader needs the words in front of them, such as a call-for-help list in an emergency section. Pro: the least to keep in
step. Con: readers click away for anything not copied.

## My pick

B, with C as its rule for passages: the registry and the check in Git, starting with links and posts, which are cheap and
catch the most (the Systema video, the misspelled address); shared passages mostly as links to one home, stored and copied
only where a reader needs the words in place. If he'd like to browse it all, an Obsidian vault can later open the same
files as a view.

For links, the first mention in each post, and in a long guide the first mention in each section, since a reader in an
emergency lands in the middle of the bad trips guide, not at its top.

How it would start:
1. **Seed it from his posts.** List every post (title, address, post id), pull every link out of each, and group them by
   thing. Where one thing has two links (like the hypnosis address), or a mention has none, that goes to him as a short
   question list: the conflicts are his to settle, once.
2. **Run the check on one article** (the bad trips guide, before its post is updated), then make it a standard step in
   [docs/FIXING-AN-ARTICLE.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/FIXING-AN-ARTICLE.md), the way the contradictions check became one.
3. **Find the shared passages** with a repeats read across posts (the same read each article already gets inside itself):
   each shared passage gets a home, and the others a linked line or a stored copy.

## Questions for him

1. **Where it lives:** the registry in Git (B, my pick), or an Obsidian vault as the home (A)?
2. **Shared passages:** link to one home by default and copy only where the reader needs the words in place (my pick), or
   store and copy every shared passage?
3. **Which mentions get the link:** the first in each post, and the first in each section of a long guide (my pick), or
   every mention?
4. **Scope of the first pass:** every post on ibogaqueen.substack.com and his u-dont-exist.com guides, registering his own
   things first (videos, guides, apps, products) and the outside sources he cites often after. Anything to add or leave
   out?

## His answers (2026-11-20 23:40 UTC)

"1. b, i don't want to write stuff in obsidian, not sure how that would transfer to substack with embeds and such, but open to your suggestions / 2. substack has includes but they aren't synced / substack has Notes, which are synced, so we can link to notes or we can embed notes (not the full note gets shown). However, it may not always be appropriate to embed a note instead of directly putting the text tehre, since the full note isn't shown in the article until they click it. / idk if you can find all my notes, most of them were jst one time things that would not be included in articles, and i think all the ones that would be included already are included in some article or another. / 3. your pick yes / 4. yes. we should also have a substack-wide conflict checker. ... / you can hand all this work off to a separate lane so you can continue on bad trips humanization" (whole, in the handoff).
