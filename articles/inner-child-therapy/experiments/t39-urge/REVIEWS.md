# Turn 39 reviews: When the Urge to Escape Arrives (2026-10-09)

Fresh subagents, each reading one prompt file and nothing else (`tools/humanization/reviewer/reviewer.py`; Opus for the dedup, cold reads and groundings; Sonnet for the march reads and the O6 judgment). Targets: `../../tools/targets/t39-urge.json`, `t39-intensive.json`, `t39-history.json`, `t39-gentle.json` (for the dedup) and `t39-section.json` (the whole h3, for the cold reads and groundings; it carries the provenance of PGQ-006). Every version: `DRAFTS.md`.

## The dedup (`reviewer.py dedup`, with the first drafts)

| Guide point | Verdict | Where the article has it | What I did |
|---|---|---|---|
| The pull toward anything that moves attention from pain | SAID | Two Common Protective Patterns: "a sudden pull to do anything but feel it" | P1 opens on its bigger forms only |
| Its examples: a substance, a relationship, a new project | NEW | (the article's are a yawn, the phone, the laundry) | P1: a drink, the ex, a new business |
| Don't shame the urge | SAID | "If you treat either one like an enemy, or like proof that something's wrong with you" | cut ("I wouldn't beat yourself up over it") |
| What it signals: something painful came close | SAID | "shows up when you get close to something painful" | kept only as the reason for the next point |
| That can be progress | PARTLY (said only for the yawn) | "That yawn might actually be the opposite of checking out" | P1: "that's kind of progress, honestly!" |
| Thank the protective part | NEW | | P1: "I'd thank whatever part of you came up with the escape plan." |
| Slow down; support when it's bigger than you can hold | SAID | "I'd go shallower"; "somebody steady there with you" | cut |
| Listening to the guards is part of the therapy | SAID | "Usually your little one only comes forward after that part feels heard." | cut |
| Don't force intensive meditation or plant medicine before enough Nurturer and Protector | PARTLY | the general caution ("leave the deeper conversation until later") | P2 |
| Aggressive trauma processing | SAID | the EMDR line; the cauldron line | cut ("Same with digging into trauma full force.") |
| They break through faster than you can build the capacity to hold what comes | PARTLY | Joel's "there wasn't a grown-up me around anymore" | P2, with his San Pedro line |
| PGQ-006, all eight points (one episode is enough; other reality-bending substances; not every drug; milder reactions; prompt professional help; sober recurrence; don't stop prescribed or dependence-producing substances cold; medical help to stop) | NEW (prompt help PARTLY) | | two drafts, not in (below) |
| Gentle meditation or self-hypnosis still helps; the heart-connected mantra; not a continuous cope; Joel's mantra and video | NEW or PARTLY | music for feeling love; loving-kindness | P3, mostly his published wording |

## Cold reads

| Round | UNCLEAR | Fix |
|---|---|---|
| 1 | "a lot bigger than a yawn": the yawn is two sections back | dropped |
| 1 | "Milder stuff counts too" read as milder drugs | "Milder reactions" |
| 2 | "that ex didn't seem so bad" (a tense shift) | "doesn't seem" |
| 2 | "It's also why": "it" pointed at nothing | P2 opens "That part with the escape plan is guarding something that hurts." |
| 2 | "once is enough" for what? | the rule comes first, then "I know that sounds strict for one time" |
| 3 | "plant medicine" could be herbs | "psychedelic plant medicine" |
| 3 | "broke your hold on what's real" repeated the psychotic-type case | cut |
| 3 | "If any of it is severe": which, and when? | "If one of these reactions ever gets severe" |
| 4 | "San Pedro" not introduced | "San Pedro cactus" |
| 4 | "That's why I'm careful about those" read as the author's habit, and "those" had no plural | "That's why I'd be careful with both" |
| 4 | "is a different story": different from what, after the drug paragraphs? | answered by the order: with the PGQ-006 paragraphs out, P3 follows the intensive caution directly |
| 4 | the colon at the end | the video follows it in the article |

## Groundings

| Round | Flag | Fix |
|---|---|---|
| 1 | MISSING: the relationship form of escape | "that ex doesn't seem so bad after all" (not the kind of reaching out the article recommends) |
| 1 | DUPLICATE ×2: not shaming it; the part managing it | cut (the dedup said the same) |
| 1 | CHANGED: "retreats" narrowed "intensive meditation" | "pushing into intensive meditation" |
| 1 | CHANGED: "help" lost "professional" and "or make safety uncertain" | "get professional help right away", "or you can't tell whether you're safe" |
| 2 | UNCLEAR: "Getting past the protective layers is kind of what they're for" ("they" after Nurturer and Protector; "protective layers" next to "Protector") | the guards, and the tools named |
| 2 | CHANGED: dropped "treat that history as a vulnerability" | "A reaction like that says something about how your own mind handles those states" |
| 2 | MISFIRES: sober recurrence only as a reason for urgency | "If it keeps coming back when you're sober, even mildly, get it looked at too." |
| 2 | CHANGED: gentle practice promised to work | "often", and "can" |
| 1 and 2 | ASK AUTHOR, MUST: does a rough trip with paranoia count, or only a psychotic-type reaction beyond what the drug usually does? | for Joel (the drafts follow his queue's "psychotic-type") |
| 1 and 2 | ASK AUTHOR, MUST: which other drugs count as reality-bending (cannabis, ketamine, MDMA)? | for Joel (the guide names none) |

GREAT lines offered, not taken: why the urge is progress (a guard only scrambles near what it guards); why gentle practice is different (the guards ease at a pace the grown-up can match; P3 has a hedged form of it).

## The linter's O6 candidates

Two, judged by a fresh agent (`abstract_agents_prompt.py`, main's rule since 2026-10-07): "That part with the escape plan is guarding something that hurts." and "A reaction like that says something about how your own mind handles those states": both EVERYDAY (therapy vocabulary; a stock idiom). Nothing changed.

## March reads

P1 had breaks each round. P2 had none until try 2 (the reader's question and Joel's San Pedro line), which is when it passed. The PGQ-006 pair had none or one each round (runs of conditions), and both failed twice.

## Tools

The linter's parsed O6 check, its spelling check and WordNet are installed in this container now (spaCy with en_core_web_sm, NLTK's WordNet through the agent proxy, pyspellchecker), so its notes about falling back to word lists are gone.
