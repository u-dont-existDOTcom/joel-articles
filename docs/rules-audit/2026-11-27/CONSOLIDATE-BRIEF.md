# Consolidate the rules audit's flags

An audit of the rules an AI editor wrote for itself (from Joel's corrections of his articles) produced 404 flags. What
a flag is, and what makes a rule sus: `/home/claude/work/audit/CHECKER-BRIEF.md`. The flags: `/home/claude/work/audit/out/B01.md`
to `B35.md`, one line each (`- ID: rule | Joel said | why sus | it should say | high or medium`). The batches they came
from: `/home/claude/work/audit/batches/B01.md` to `B35.md` (B01 to B11: AGENTS.md, SKILL.md, the briefs in
tools/humanization, docs/FIXING-AN-ARTICLE.md, docs/MAKING-SENSE.md, docs/CLARITY-READ.md, the Pangram budget and other
docs; B12 to B20: the lesson files of 6 to 27 November; B20 to B32: the old gate, docs/HUMANIZATION-GATE.md, with gates
E1 to E380 from September to early November; B33 to B35: the tells registry). The repository as the rules stood:
`/home/claude/work/audit/snapshot/`.

Joel will be asked about the rules that really look sus. He can't answer 400 questions, so:

1. **Merge flags about the same rule.** One rule often sits in AGENTS.md, SKILL.md, a brief, a lesson file and the old
   gate at once; that is one rule.
2. **Group rules that go wrong the same way into themes**, so one answer of his can settle many. Themes seen so far
   (use others if the flags show them): a feature that merely happened to be true of his fix made into the method; a
   mechanical test (word count, word list, string match, percentage, fixed number) standing in for a judgment of
   meaning; an always/never made from one case; a word banned where he said "overused" or "high frequency"; steps,
   checks, refusals or questions to him that nobody asked for and that slow the work; his words stretched to cover
   something he didn't say; rules that contradict each other; stale text (a rule superseded or retired, such as the
   Emulate rules, that still reads as active).
3. **Tell active from historical.** Active: the rule steers today's work (it is in AGENTS.md, SKILL.md, a brief in
   tools/humanization, docs/FIXING-AN-ARTICLE.md, docs/MAKING-SENSE.md, docs/PANGRAM-PRODUCTION-BUDGET-20261020.md, a
   November lesson, or a tool's refusal). Historical: it lives only in the old gate's sections or a retired document.
   You may open snapshot files to settle this, briefly.
4. **Rank** by how much following the rule could hurt his articles or slow the work today, times how sure the flags are.
   Drop a flag that looks wrong to you, and say so in one line.

Write `/home/claude/work/audit/CLUSTERS.json`:
`{"clusters": [{"id": "C01", "theme": "...", "title": "a few words", "active": true, "impact": "high|medium|low",
"rules": [{"id": "the rule's name (lesson, gate, way)", "file": "..."}], "says": "what the rules say, one sentence",
"joel_said": "his words, quoted exactly from the flags", "why_sus": "one or two sentences", "fix": "what the rule
should say, one or two sentences", "flags": ["B19:1", ...]}], "stale": [{"title", "rules", "why", "fix"}],
"dropped": [{"flag": "B07:3", "why": "..."}]}` (a flag's id is its batch and its line number in that file).

And `/home/claude/work/audit/CLUSTERS.md`, at most 15 KB: the clusters in rank order, a line or two each, then the
stale list, then the dropped flags. Every flag ends up in a cluster, the stale list, or the dropped list. Be brief.
Your final message: the number of clusters, active and historical, and the ten top titles.
