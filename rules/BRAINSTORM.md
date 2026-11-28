# Brainstorm: one rule tree for joel-articles (2026-11-28)

Joel, 2026-11-28 10:25 UTC, after answering the rules audit: "i also feel like there are a lot of rules that are
overlapping and there's not very good organization of the rules like you should have some kind of rule tree or something
idk how brainstorm it (and many of these are referencing other things that iw asn't clear on, but hopefully clear for
you, altho there should be a human view of the rule tree where everything makes sense, maybe with graphical links)". On
the audit's cards he also asked to "merge any rules that could be merged", to check "if lessons interact or contradict
each other", to do "periodic reviews to see which lessons are overall helping", to make his fixes searchable, and to keep
"the rules that help the reader up front before the hacks".

## What's wrong now

- **One rule, five places.** The same rule sits in AGENTS.md, SKILL.md, a brief, a lesson and the old gate, each worded
  differently; fixing it in one leaves the others (the audit's 404 flags were mostly duplicates of a few dozen rules).
- **No shape.** 116 lesson files (2026-11-28) and the old gate's 380 gates are ordered by date, not by what they're for, so nobody can
  see which rules belong together, which come first, or which contradict.
- **Private shorthand.** Rules cite each other by codes (E278, bad-trips-2026-11-12g, O71, "the ledger") that mean
  nothing to a reader who wasn't there.

## Ways to organize it (the options)

1. **By purpose: what the rule protects.** Five branches: the reader; his words and meaning; passing Pangram; working with
   Joel; how the lanes work. The reader comes first, Pangram later, and hacks last, as he asked.
2. **By stage: when you need the rule.** Starting an article → making it make sense → humanizing → checking in Pangram →
   showing Joel → recording. Good for a worker mid-task; but the same rule (payoff first) belongs to several stages.
3. **By question: a decision tree.** "A paragraph reads AI: what now?", "When do I ask Joel?", "Can I cut this?" Each
   question walks to the rules that answer it. Good for hard moments; poor as a home for every rule.
4. **By source: one branch per article or lane.** Matches how the rules were made, and is exactly what made them
   overlap. Not this.

**My pick: 1 as the home, with 2 and 3 as views.** Every rule lives once, in its purpose branch (option 1). Each rule is
also tagged with its stages, so the same tree can be shown by stage (option 2), and a few decision paths link rules in the
order to use them (option 3). One source, three ways to look at it.

## What a rule looks like in the tree

- **A plain title and the rule in one to three sentences**, no codes.
- **Why: his words**, quoted exactly, with the date.
- **An example**: a before and after from his fixes where there is one.
- **How it's checked**: "a reader's judgment", or the tool that flags it and whether it blocks or only warns.
- **Links**: builds on, goes with, comes before, replaces (the old lessons and gates it stands for). A "conflicts with"
  link is not allowed: the build fails, so a contradiction can't hide.
- **Track record**: when he approved or changed it, and, over time, whether it helped (his checks, Pangram before and
  after), for the periodic review he asked for.

## The human view

One page, three tabs: **Tree** (branches you open, each rule's card beside it, with search), **Map** (all the rules as a
graph, colored by branch, the links drawn, click a rule to open its card), and **Words** (what every internal term means:
lane, card, window, near miss, ledger, receipt, gate, lesson, tell...). A toggle shows the tree by stage instead of by
purpose. The same tree renders on GitHub as Markdown with a Mermaid map.

## How the lanes use it

The tree is the first rule file every lane reads; where older text disagrees with the tree, the tree wins. Old rules are
moved in branch by branch; each old place gets a pointer to the tree node that replaces it. A new lesson goes into the
tree the turn it is made (as a new node or a change to one), after the rules check against his words, which also checks it
against its neighbors for overlap and contradiction.

## Later, from his notes on the cards

- **His fixes, searchable** ("i'm not sure how to make the fixes searchable exactly"): every before-and-after of his, tagged
  with the tree rules it shows, so a rule's card lists its examples and a search finds fixes for a kind of problem.
- **What Pangram reads** ("i'm curious how we can mimic the way pangram analyzes text statistically"): the ledgers hold
  thousands of checked texts with Pangram's windows; a small local model trained on them could predict which sentences
  read AI before spending a check. Worth a test.
- **Human tell attempts** (card C15) and **the humor lesson** (card C29): rules in the tree marked "to build".
