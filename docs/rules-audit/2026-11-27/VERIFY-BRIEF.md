# Double-check the rules audit's clusters against the sources

An audit of the rules an AI editor wrote for itself, from Joel's corrections of his articles, found rules that look sus
(`/home/claude/work/audit/CHECKER-BRIEF.md` says what that means). The flags were merged into clusters:
`/home/claude/work/audit/CLUSTERS.json`. Before Joel is asked about them, each cluster is checked against the sources.
The repository as the rules stood: `/home/claude/work/audit/snapshot/` (search it with grep; the old gate is
`docs/HUMANIZATION-GATE.md`, lessons are in `docs/lessons/`). His saved preferences, the latest word on many points:
`/home/claude/work/audit/memory/preferences.md`.

The calibration case, for what a real one looks like: lesson bad-trips-2026-11-27j said to replace a word that pulls
against the paragraph "with a word the passage already has, as he did", because his fix "smooth" happened to be a word
the sentence already had; his own words were "smooth the trip makes more sense, and is more accurate also", and he has
now said: "it's not about using the same word. it's about using a word that's accurate". A feature of his fix had been
made the method. He corrected the same mistake on 2026-11-04 ("don't make a rule not to move paragraphs ... you do
whatever you need to do get it to read well").

Your clusters: {CLUSTERS}. For each one:

1. **Find the rule's text** in its main file (the one lanes read first: AGENTS.md, SKILL.md, a brief, FIXING-AN-ARTICLE,
   MAKING-SENSE, the budget, a lesson), and quote the sentence that says it, with the file and line.
2. **Find his words** it rests on, in context (the message or answer quoted in the lesson or gate). Does the rule carry
   his point and his reason, or something that merely happened to be true of his fix, or more or less than he said?
3. **Check the cluster's proposed fix against what he said later** (the preferences file, later lessons, AGENTS.md). A fix
   that undoes something he asked for later is wrong: rewrite it so it keeps his later word. Example: he said on
   2026-11-23 that Medium windows are work to do, so a fix that lets Medium stand is wrong.
4. **Verdict**: `confirmed` (the rule as written could make the editor act against what he said or wants), `partly`
   (say which part), or `not sus` (say why). Where rules in the cluster go different ways, say which one matches his
   latest word.

Write `/home/claude/work/audit/verify/{NAME}.md`, per cluster at most 12 lines:

```
## C01 title: confirmed | partly | not sus
- Rule: "quoted sentence" (file:line)
- He said: "his words" (where, when)
- Check: one or two sentences
- Fix: what the rule should say, in one or two plain sentences, keeping his later words
- Question for Joel (only if his answer is needed: something only he can decide): one plain sentence
```

Be brief and exact; quote, don't paraphrase, where you say what a rule or he says. Change no file but your answer. Your
final message: each cluster's id and verdict, nothing else.
