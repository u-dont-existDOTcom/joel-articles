# Turn 38 reviews: what each found, and what I did with it (2026-10-09)

Every reviewer was a fresh subagent that read one prompt file and nothing else (`tools/humanization/reviewer/reviewer.py`). Opus for the dedup, cold reads and groundings; Sonnet for the march reads. Targets: `../../tools/targets/t38-depth.json`, `t38-pleasant.json`, `t38-isolation.json`, `t38-isolation2.json` (each with `provenance`: innerSignalGraph #126 and its amendment, and the teaching points as the reader need). Drafts: `DRAFTS.md`.

## Whole-article dedup (`reviewer.py dedup`, all three groups with the first drafts)

Counts: 43 guide points (depth 12, pleasantness 20, isolation 11): 1 SAID, 25 PARTLY, 17 NEW; 39 draft sentences, 5 carrying no guide point (the writer's own); 4 repeats between the groups' drafts; 8 points two groups share. The reader couldn't save its report to a file (subagents return text), so the findings are summarized here.

| Finding | What I did |
|---|---|
| SAID: intensity isn't progress (the crying story; "Going at it harder isn't as useful…"; "A lot of people's first guess is that they didn't go deep enough") | Nothing carries it. Turn 34's "A session can also be really intense and get you nowhere." stays cut. |
| PARTLY, close to said: not-evidence ("They can feel totally real, but that alone doesn't prove they happened", for memories in an altered state) | Kept for dreams and session images only, which is new; that line comes later in the article, so a reader meets this one first. |
| Repeat between drafts: "try something gentler" (depth) and "make the next one a little easier" (pleasantness) | Kept both: the first is during a session, the second the next session (the dedup's own split by when it happens, turn 35). |
| Repeat between drafts: the eyes-open hello and "keeping your eyes open" | The pleasantness example became timing ("a time when you're not already worn out"); later the rebuilt pleasantness group has no eyes-open line at all. |
| Two instructions for getting worse (come out to the room; change several things) | Different times (during a session; from one session to the next). The rebuilt P2 says "the next one", so the second reads across sessions. |
| Return condition and stepping back up said in both groups | T3 (after a full break) and P3 (after a hard session) are different situations; kept. |
| Not carried: a full pause as the last resort, safety forcing a pause, no peeks during a pause, the choice not to use inner-child language | Out by the teaching points Joel approved (the pause bookkeeping and the no to inner-child work stay in the AI guide). |

## Cold reads (sense)

| Round | Group | UNCLEAR | What I did |
|---|---|---|---|
| 1 | depth | "the Protector" isn't introduced | Answered: the article names the three jobs in The Chicken-and-Egg Problem ("The Protector gets you both out of there"); a core term, not a pointer back. The cold-read prompt now says so (`sense.txt`), since it came up four times. |
| 1 | pleasantness | none; "Here's a map of what to try when:" seems to promise a map | Answered: the Substack card with the map sits there; the prompt doesn't show embeds. |
| 1 | isolation | "the good ones" read as places; T8 felt like a step backward after C2 | "the good people"; T8 moved before C2 (the guide's order too). |
| 2 | depth | the Protector again | As above. |
| 2 | pleasantness | none | |
| 2 | isolation (C1, T8, C2, T9) | "which places will work for you": places not set up | "where to look for people who fit you". |
| 3 | depth (T2 rebuilt) | "stop in the middle and come back" could mean another day; the Protector | "stop partway through and come back out to the room"; the Protector answered. |
| 3 | pleasantness (rebuilt from turn 34) | "Those dreams and images that come up": images hadn't come up | "And what about those hard dreams, or images that pop up during a session?" |
| 4 | depth (T2 try 3) | the Protector | Answered. |

## Groundings

| Group | Flag | What I did |
|---|---|---|
| depth, round 1 | MUST: T3 let you come back just because you want to; the guide's return needs the reason for the pause to have changed too | "So once that reason has changed and you want to come back" |
| depth, round 3 | CHANGED: T2's protective act lost "ordinary", leaving room for a big move after a session that stirred old hurt | "one small, everyday thing the Protector would do" (T2 later folded away; T1's hello doesn't carry the act) |
| pleasantness, rounds 1 and 3 | none open; "just by" keeps the guide's "only" | |
| isolation, round 1 | CHANGED: "where you'll find your people" promised it | "where to look for people who fit you" |
| isolation, round 1 | MUST: only a group could want to be your only one; a partner or one friend can too | "if any group, or any one person, starts acting like they should be your only one" |

GREAT lines offered and not taken (each adds a sentence; for Joel if he wants them):
- depth: the eyes-open hello practises what was missing, being in the room while you reach in;
- depth: saying "that's enough" is itself something your little one sees, so a session cut short still counts (I tried it in T2 try 3, which failed);
- pleasantness: past the hard-but-doable edge you're flooded, and flooded protectors won't let your little one out, so pushing gets you less;
- pleasantness: dreams and session images are built from present feelings out of borrowed pieces;
- isolation: why "your only one" is the warning sign: leaving would mean being alone again, the old hurt.

## March reads (`reviewer.py march`)

- Round 1: T1, T2, P1, P2, P3 had a break. My concatenation merged T3 with P1 and P4 with T8, so those two pairs were read as one paragraph each; the parts with no break were T3, P4, T8 and T9.
- Round 2 (the changed ones): T3, P4, T8 and T9 had a break; P3 didn't (the first reader had counted "That's a lot to hang on one session" as one).
- Round 3: T2 rebuilt, P1 and P2 from turn 34 had breaks; P3 from turn 34 without its wait line had none, and with the hard-dreams question it passed.

## Linter (`tells_lint.py`), each paragraph alone

FAILs, rewritten before any check: T3's first version (coach register 3.2 per 100: "you might", "you can") and P3's (2.3). REVIEW items kept, with why:
- lists the linter counted in a quoted line or a two-item phrase ("Okay, that's enough for today"; "call somebody or show up somewhere, mess and all"): not lists;
- P1's "grief and fear, and sometimes hard dreams, or stuff you'd rather never have met": turn 34's text, which passed with it;
- P3's "Or to suggest one." (a short landing): turn 34's text, which passed with it; it splits the guide's three verbs, Joel's own move for a list of three;
- "everyday" (a caution word) in T2 try 3: the grounding's fix, so it says something;
- heavy second person (6 to 10 per 100): advice to the reader, like the paragraphs around it.
