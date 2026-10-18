# Triage of a second reader's findings on a rewrite that reads Human (2026-10-18)

The rewrite (the CHANGED stretches) is Emulate's rewrite of a guide's text. A detector already reads it as 100% human.
Every word changed risks that: in 33 earlier edits, the ones that changed under 18% of a section's words stayed human
(3 of 3) and those that changed more mostly didn't (2 of 30). So fix only what matters, with as few words as possible.

For each finding in the findings file (lines "B<n>: <TYPE> <what>" and "R: ..." repeats), compare the CHANGED stretch with
the PUBLISHED blocks it replaces (both are in the prompt file) and decide:

**FIX** (major): a reader of the rewrite would do or believe something the published text doesn't say, or miss something
it needs:
1. a safety instruction, caution, limit, warning or "get help" advice that is weakened, softened, reversed, made
   conditional, or lost;
2. a step, condition or order of a procedure or script that is lost or changed, so the reader would do it differently;
3. an invented fact, claim, study, number, person, quotation, attribution, promise or reassurance; a quotation of
   someone that isn't word for word;
4. a claim made stronger or weaker in a way that changes what the reader would believe ("may support" -> "treats",
   "resembles" -> "is", "some" -> "all");
5. a point the published text makes that is gone entirely (not just shortened);
6. a repeat (an "R:" line) where the rewrite says one point twice that the published text says once.

**LET STAND** (minor): wording, emphasis or tone; a casual aside in the author's voice that claims nothing new ("Have
fun!"); an elaboration or example that fits the published meaning; steps merged or reordered with every step kept;
synonyms; a list shortened without changing its sense (unless a lost item matters for safety); "UNCLEAR" about who "it"
is when the next sentence says.

**How to fix**:
- "replace": copied exactly, character for character (curly or straight quotes as they are), from that CHANGED stretch,
  occurring exactly once in it. Keep it short: the phrase or clause that is wrong, not a whole paragraph.
- "with": the same phrase with as few words changed as possible, in the stretch's own voice (its contractions, plain
  words and sentence shape). Don't paste the published sentence unless the fix is a few words: in 454g the only two AI
  windows of a triaged section (HG37) were exactly the two fixes that pasted published sentences ("Pride gives it an
  opponent, and panic gives it your nervous system."). Say the published point the way the stretch talks ("if you're
  proud you give it an opponent"). Don't fix anything else,
  don't polish, don't correct the author's casual grammar or typos.
- If one stretch would need more than about a quarter of its words changed, don't fix it: list its first block under
  "resample" (a new sample is better than many fixes).

**Write** one JSON file per section, exactly this shape (no other text in the file):

```json
{"key": "HG22",
 "fixes": [{"block": 1, "problems": [{"type": "WRONG", "what": "a few words on what was wrong",
            "replace": "exact words from the stretch", "with": "the fixed words", "round": 1,
            "from": "second reader of the refix (rf), triaged"}]}],
 "let_stand": [{"finding": "the finding line as given", "why": "a few words"}],
 "resample": []}
```

"block" is the stretch's first block: the n of its "[CHANGED, replaces Bn...]" header. Every finding line goes either
into a fix (named in its "what") or into "let_stand".
