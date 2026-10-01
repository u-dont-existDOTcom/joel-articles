# Humanization gate (shared by every article)

**Status: ACTIVE, 2026-09-30.** Joel: "whenever any article is being humanized the same universal joel-articles or pangram-humanization repo rules should be applied, make sure it's not just a per convo silo of rules". So this gate, built in the Inner Child lane, is the one every humanization pass runs, in any chat, on any article.

How to read it:
- **This is the only gate (2026-10-01).** It started as a copy of the Inner Child lane's gate at `35b88b5`. The lane's later rules (through `4a4c2e11`) were merged in when the lane moved over, and the lane copy is now a pointer here. Change this file, from any chat.
- **"The guide" means the article's source.** That's the guide for Inner Child, the published text for a published article being humanized, or Joel's draft. The examples come from the Inner Child article; they're evidence, not scope.
- **Paths in the body are relative to `articles/inner-child-therapy/` on that branch,** unless they start with `docs/`, `project-sources/`, `tools/humanization/` or `articles/`. Those are from the repo root, where the commands run.
  - The tools live in `tools/humanization/` (`tools/humanization/README.md`): the linter, the reviewer, the calibration texts, the owner-edits check, the Pangram batch builder, the sweep-prompt builder, the article render, the side-by-side page and the Emulate tool. Every article uses them from there, with its own files given as options.
  - The Inner Child article keeps its own reviewer targets (`tools/targets/`), side-by-side maps (`tools/in-context/`) and predictions (`tools/PREDICTIONS.md`).
- **The reviewer learned from the Inner Child article.** Before trusting its verdicts on another kind of writing, add that article's own Pangram-checked paragraphs to the calibration set and revalidate, as `tools/humanization/reviewer/README.md` says for any change.
- **Pangram and Emulate are fallbacks** (Joel, 2026-09-30). The system comes first, and Pangram is the outside check. Emulate goes first on a published article's flagged paragraphs, and only after the reviewer-writer loop has failed on new writing (`EMULATE-FALLBACK.md`). The aim is to need neither.
- **Claims in reviews, records and replies follow `SKILL.md`'s "Claims about sources and reviews of Joel's writing"** (from PR #112, adopted 2026-10-01). Every reviewer here and every record of a check: anchor what a source says in a passage, keep quotation marks for exact words, say exactly what was checked against what, and never state an inference as the source's content.
- **The lab repo has rules of its own for generation and teaching work:** `pangram-humanization-lab`'s `AGENTS.md`, with its owner-teaching corpus and lesson closeout. Keep one version of each rule, and link across instead of copying.

## Owner rulings on rewriting Joel's own words (Joel, 2026-09-30)

These came from community sections 1 and 2 and apply to every rewrite of his words, whether by Emulate, a writer or a fix:
- **Don't hype.** "Happy" doesn't become "very happy", and "this mostly meant boredom" doesn't become "boring as hell".
- **Don't flatten a mixed experience into one note.** His childhood visits meant boredom "with some adventures mixed in".
- **Don't change a fact without asking, even a small one** ("own" to "live on").
- **Don't turn his uncertainty into a stance.** "I couldn't tell whether…" doesn't become "I didn't feel like it was really…", even when a nearby line leans that way.
- **Don't give him a reaction he couldn't have had.** He was too young to find the missing therapy practice "odd".
- **Keep the exact relation.** "Needed" isn't "wanted". "Much larger" is a comparison, and "big" drops it.
- **A fact in an AI-drafted original can be wrong.** When Joel corrects one (the "complicated labor credit system"), his correction replaces it.
- **Show every proposed change side by side before asking** (`tools/humanization/render_in_context.py`). On 2026-09-30 he approved two changes from a list, then took them back once he saw them in place.
- **Every paragraph passes alone (Joel, 2026-10-01).** A section that passes with a paragraph that fails alone doesn't count, for a published article too: "otherwise we're sort of playing with pangram but usually there are still ai tells you're missing in the paragraph, and pangram 5 will catch with better localization i'm sure." His one exception is a paragraph that really looks human to him: he has "never seen any actual human paragraph labeled as AI by pangram unless it was written as an academic paper super formulaic". A paragraph under 50 words is checked with a neighbor that passes alone.
- **Wording can flex when the meaning stays (Joel, 2026-10-01).** The preservation units are meaning, not wording.
- **Emojis (Joel, 2026-09-26):** "If you see something begging for an emoji, put it, but don't put it otherwise." It applies to his article writing and to any article that's allowed to be cute. A spot begs for one when the emoji does something the words can't do quickly. His example is 😜 after a slightly awkward line, to tell the reader it's a joke. Never add one to influence a detector. (The Inner Child chat first wrote this into `project-sources/MASTER-INSTRUCTIONS.md`, but a repository test pins that file's exact bytes, so it lives here.)

---

# Humanization gate — run for every section, before any Pangram check or owner delivery

Added 2026-09-25, revised 2026-09-26. Joel: "how is it possible you're still not following the basic instructions to check the list of tells? can we fix that or is it hopeless?" and "you should fix UDA since the inherited UDA rules must have allowed you to avoid doing the actual rule gates that were obviously required. i shouldn't have had to tell you to do that."

**Why the checks got skipped.** From the 2026-09-24 handoff on, no record in this lane shows the repository's own blocking gates being run: the preservation proof, the architecture gate, the post-generation tell ledger and the owner-delivery admission in `SKILL.md`. Joel's corrections were collected in a separate rules file that I read at the start of a section and then drafted from memory. After each context compaction the summary I worked from named some of those rules but carried no obligation to run them, and I didn't re-read the universal bootstrap either. Nothing enforced a gate at the moment a draft went to Pangram. Some universal (UDA) defaults also read as permission to skip a declared gate when they're loaded. The fix for those is UDA pull request #260 ("Declared gates and owner-stated checks can't be waived by universal defaults"), merged 2026-09-26 at Joel's direction (e6eb98e). It also says that an inherited rule that looks unhelpful gets flagged to Joel with a suggested change, and followed until he decides.

**The fix.** This file is the lane's checkpoint of what has to run. Part of it is mechanical and has to happen in the open. No Pangram check without a linter report and a written ledger in the drafts file, and no prose goes to Joel until every gate below has passed.

## 0. Activation

After every context summary, and at the start of each new section, reload this file and the gate documents below from the repo (E46). A summary that names a rule doesn't activate it.

## Declared gates this lane must run

These come from the repository's own authority (`AGENTS.md`, `SKILL.md`, `CANONICAL-REPO-MAP.md`). They're blocking.

- **Preservation proof:** `docs/HUMANIZATION-PRESERVATION-GATE.md`. Freeze the preservation units and the change whitelist before drafting; afterwards, trace both ways with zero unexplained substantive deltas. No Pangram call before it passes.
- **Architecture:** `docs/HUMANIZATION-ARCHITECTURE-GATE.md`. Heading promise, entry and exit state, one job per paragraph, and a literal top-to-bottom proofread. Before the first Pangram call and after every detector-driven edit.
- **Post-generation tell ledger:** `SKILL.md`, "Post-generation tell ledger and repair". Every applicable tell gets a disposition on the literal candidate, covering both local wording and paragraph-level function topology (a scene that just skins the source's order still fails). The catalog is `project-sources/BANNED-PATTERNS.md`, `project-sources/STRUCTURAL-HUMANITY.md`, the `SKILL.md` sections, and Joel's corrections in `experiments/DANGEROUS-ADULT-SELF-AUDIT-RULES-20260924.md`.
- **Owner-delivery admission:** `SKILL.md`, "Humanization owner-delivery admission". Joel isn't an intermediate QA surface. Failed candidate prose stays internal unless he asks to see it, and AI-shaped wording is never a reason to ask him for his own experience.
- **Owner-facing turn contract:** `OWNER-FACING-TURN-CONTRACT.md` at the repo root, active since 2026-09-17. It covers:
  - the full article so far at the end of every turn;
  - how to present owner decisions;
  - audit meaning output plus method;
  - no listicles and no repeats;
  - the prediction format.

  It wasn't on this list until 2026-09-26, so I didn't load it or follow it (E73).
- **Fresh-context review:** `docs/HUMANIZATION-FRESH-CRITIC-GATE.md`, whenever fresh-model evidence is used before Pangram. It never replaces the full tell ledger.

## Steps

**Sense comes before humanization (E87; Joel, 2026-09-27 22:00: "you shouldn't be checking for humanization before you even have something that makes sense").** Nothing in steps 1 to 9 (tell inventory, linter, sweep, Pangram) runs on a paragraph until it passes this:

S1. **Start from the original, not the latest rewrite.** Read Joel's source paragraph, his own words about it (chat, notes, his edits), and the earliest humanized version that made sense. A paragraph that has been through several detector-driven rounds drifts like whispering down the lane: Also Look Outward P1 went from a coherent 2026-09-17 version to "Now the first fight has company". Rebuild from the source's meaning, not from the drifted text.
S2. **Write the sense chain.** One line per sentence:
  - what it says in plain words;
  - what it refers back to, quoted from the page, including the sentence before the paragraph;
  - why it follows from the sentence before.

  Also say what the heading and the first sentence promise, and where the paragraph delivers it. A point that can't be stated plainly, or can't be tied to what comes before, is cut or taken to Joel. It isn't smoothed over.
S3. **Cold read.** A fresh subagent that hasn't seen the source, the drafts or the plan reads the paragraph with the text before and after it. It gives the same per-sentence lines, and it lists every "what does this refer to?" and "why is this here?".
  - Its overall verdict is lenient. On 2026-09-27 it passed the Also Look Outward P1 that Joel says makes no sense, while its line notes named the same gaps he found. So the line notes are the gate: each one gets fixed, or answered in the record.
  - It did catch the old three-jobs paragraph ("No job is described").
  - **Give it what a reader has already read (2026-09-30).** Early in a section, the paragraph before isn't enough. Three cold reads called "what you promised them" a claim from nowhere, but the section before says "Keep one small promise to your little one". With `"earlier": "section"` in the target, the prompt also carries the whole section before and this section's paragraphs up to the paragraph before. Given that, the same draft read OK.
S4. **Only then humanize.** After any humanizing edit, redo S2 for the changed sentences, and S3 if a referent or the order changed.
S5. **Owner notes about sense.** When Joel says a paragraph doesn't make sense, the whole paragraph goes through S1 to S3. Fixing only the sentence he quoted isn't enough (E86).
S6. **Grounding and logic review (Joel, 2026-09-29 19:14).** Joel: "One role the reviewer instance should have is checking whether the sentence not only makes sense based on the guide but whether it goes beyond the guide in a way that needs support from the guide." He also said "An article is not just a bunch of individual paragraphs."
  - **Run it** on every new paragraph and every candidate heading, before any Pangram check: `python3 tools/humanization/reviewer/reviewer.py grounding DRAFT TARGET OUT` (the article and its source come from the target's `article` and `source`, or from `--article` and `--source`), then a fresh Opus subagent.
    - The target gives the guide passage, what comes next, and Joel's rulings on the material. His rulings override the guide's wording.
    - The prompt carries the whole guide and the article up to the new text.
  - **Every flag gets fixed, or answered in the record.** The cold read (S3) still runs: it checks what a newcomer can follow, and this checks what the text claims.
  - **What it checks:**
    - each claim rebuilt against the guide's version: who, relation, object, conditions, quantity, strength, evidence status, time;
    - new material sorted into example, aside, instruction or claim, each checked differently;
    - examples in the right job, even when the guide's own list mixes them;
    - repeats of anything already in the article;
    - claims that go beyond the guide without support;
    - instructions tested against three or four different readers and the article's own model of people, even when they carry the guide faithfully (MISFIRES, 2026-09-30). The guide's "Leave a relationship that keeps eroding safety" passed every review, and Joel showed it misfires for someone whose less-safe feeling comes from inside them, which the article itself teaches (a hook can be old material). Look hardest at costly or hard-to-undo instructions;
    - claims tested the same way, even faithful carries (2026-10-01). When a sentence says one thing doesn't need another, or is enough ("love and trust don't have to come as a pair"), the reviewer asks what has to be true for it to hold, and who could use it as written. Joel caught the one every review had passed: love "doesn't require the loved one to trust, buut it does require the lover to be honest (trustworthy objectively). otherwise can just be a dark empath pretending to love." One review had even called "the honesty condition" covered, in the other sense of honest (saying "I love you" only when you mean it). So a review that calls something covered quotes the line and checks it's the same sense, as SKILL.md's claim checks ask of any report;
    - what the guide says Joel or the people in his life did, said or felt: INVENTED unless his own words say it (2026-10-01). The guide's "She did not tell me I wasn't angry" went into his bedtime story. Joel: "not what happened (i mean it's true she didn't, altho maybe she did, you don't know)";
    - non sequiturs, and contradictions with the article's stances;
    - whether the paragraph does one guide paragraph's job;
    - the reader's open questions (2026-09-30 04:44, Joel: "not just base things on the article but on the questions the article generates for the reader"). The reviewer lists up to five questions a thoughtful reader would stop on at that point, and where each is answered: here, earlier, later in the guide (then it isn't open), or nowhere. Open ones are sorted MUST (a wrong guess could hurt them, or go against the article), SHOULD (most readers get stuck and nothing later answers it) or COULD (depth), and each gets the smallest answer and its size;
    - one good-to-great proposal (the GREAT line, 2026-10-01): where the text states something without its why, the deeper why, from the article's own model or Joel's own words. It's outside the push level, and it never adds events. P4 carried "Fights don't usually go like that" and stopped there. Joel knew why, and that was the best part: anger is a way to get more power when you feel a lack of justice or agency, and his mom's answer showed him he didn't need it to be heard;
    - the heading's promise;
    - the kind of logic the passage runs on (argument, instruction, joke).
  - **Sources:**
    - UDA `patterns/whole-argument-reconstruction.md` (never broaden scope, quantifier, modality or conditions while paraphrasing);
    - UDA's predicate-alignment requirement (don't swap a neighboring relation);
    - Grice's maxims: Quality ("Don't say what you lack adequate evidence for"), Quantity, Manner (https://plato.stanford.edu/entries/implicature/);
    - Linda Flower's reader-based prose (https://publicationsncte.org/content/journals/10.58680/ce197916016);
    - the standard informal fallacies (https://plato.stanford.edu/entries/fallacies/).
  - **Validation (`tools/humanization/reviewer/grounding-validation/`):**
    - Blind v1, on Joel's 2026-09-29 catches: it caught "proof you love them", "tends to come later" and the "Keep Your Word" heading. It missed the dropped "if they're right", and it missed the meal and the cancelled obligation twice, because it trusted the guide's own example list.
    - v2 adds Joel's rulings as an input, the sentence-shape note, the guide-list note and the figurative-heading rule. On held-out text with planted errors it caught 5 of 5: a dropped safety condition, "can" turned into "will", a hug offered as a protecting act, a repeated example, and an off-topic h2.
    - Controls: Joel's P3 came back clean, and his heading passed. The flags that recur on the current section (his self-love sentence, the moldy bread) are open questions for him, not errors.
    - v3 (2026-09-30, `RESULTS-20260930.md`) adds MISFIRES. Blind, it caught Joel's point on the old P1 ("leave it" for a reader whose "less safe" is the old alarm) and a gap in his new wording (a reader in danger told to look inward first). It gave no MISFIRES flags on two accepted controls. A referent check for Joel's "If you did it" missed 4 times out of 4, in this review and in the cold read, so it was taken out; `tells_lint.py` R1 warns on an action "it" near a paragraph's start instead.
  - **The push knob (Joel, 2026-09-30 04:44: "give the user some kind of control knob for how much to push the writing. in general we should assume the user doesn't want to massively increase the article size, but small increases or decreases may be fine if warranted. for any uncertainty ask the user").** Set it per section with `"push"` in the target, or with `--push`; the default is `default`.
    - `tight`: MUST questions only; a fix stays inside the sentences or adds a clause; the section grows by no more than about 5%.
    - `default`: MUST and SHOULD; about one short sentence per paragraph; the section may change by about ±10%.
    - `wide`: also COULD; a sentence or two per paragraph, or a suggested new paragraph.
    - At every level, anything bigger, or belonging to another section, or changing what the section is about, is ASK AUTHOR: take it to Joel, don't write it. When runs disagree on a question, that's ASK AUTHOR too.
    - Questions below the level go on the PARKED line. Copy them into `PARKED-READER-QUESTIONS.md` (next to the article), not into the article.
    - Demo and first uses: `reviewer/grounding-validation/PUSH-KNOB-20260930.md`. On the relationship paragraph, all three levels found the same MUST, and COULD came up only at wide.
  - **Treat it like the other reviewers:** a strong lead, not a verdict. Recheck it whenever the prompt, the model or the route changes.

0. **Owner edits and claims go in the ledger first (E85; Joel, 2026-09-27 21:18: "so how can we prevent that kind of error in future where you say you will write something and don't write it?").**
   - Every edit Joel gives goes into `OWNER-EDITS.json` in the same turn, as `pending`, before any drafting. The entry has his words, plus the strings the article must contain, must not contain, or must have in order once the edit is done.
   - When a sentence or heading I write promises named items ("three jobs", "two ways"), it gets a `claim` entry with a span check: each item must be in that paragraph, not just somewhere in the article.
   - `tools/humanization/check_owner_edits.py` checks the ledger against the article. `render_article_so_far.py` runs it on every render (given `--ledger OWNER-EDITS.json`); a failure goes in a red box at the top of the article and the render exits 1.
   - A note, record or message says something is in the article (installed, applied, fixed, resolved, moved, "explains…") only after its entry passes. If it exists only in a draft, a candidate or a scratch file, the note says that.

1. **Bird's-eye (D1).**
   - Reread the source beat and list its points.
   - Search the article for overlaps and callbacks.
   - Reread a stretch of Joel's own rewrite of AI prose (E43).
   - Read only the parts of the article and the rules the section needs (E47).
   - **Stance ledger (E71).** For each theme the section touches, write the article's stance and where it is: the installed text first, then the later source sections. Check every stance-bearing sentence against it before any Pangram call.
   - **Joel's first person (E71).** The source's "I" is an AI draft of his ideas. Put an experience in his voice only if his own words (the installed article, his messages) say it. Otherwise use "you" or a general voice.
     - That covers the guide's reflections on his memories and what it says his people did, not only the experiences themselves (2026-10-01). Carry only what he confirms, and ask about the rest.
2. **Preservation freeze.** Write the preservation units (what has to survive, one unit per inseparable meaning, not per sentence) and the change whitelist (what Joel has authorized: cuts, moves, research relocation). Anything not whitelisted is presumed invariant.
3. **Write inside the organization (Joel, 2026-09-26).** Keep the order the sense needs, which is usually the source's. Don't reorder, rank, cut or move material to get past the detector (inventory T14). Keep source sentences that already read right, and rewrite the ones that don't. The human part is what gets noticed while each piece is being said:
   - the reader's obvious counterexample;
   - why the thing is true, or hard;
   - an irony inside the article's own frame;
   - a callback.

   Joel's rewrite of the Borrow opening is the model. It keeps "A complete ideal parent may be impossible to imagine" and "Borrow one function at a time from a figure who embodies it" word for word, and adds The Brady Bunch, imagination getting stamped out early, and "the adult is actually a baby when it comes to power to imagine". That last one becomes the reason to start small. Organization that's "reducible to code" (T13) is the tell, not organization itself.
4. **Preservation trace.** Forward: every unit is in the draft, or has its authorized disposition. Reverse: every substantive thing in the draft maps to the source, an owner statement or the whitelist. Zero unexplained deltas. Fold a missing unit in as an aside or a single sentence, not a paragraph of its own.
5. **Linter.**

   ```
   python3 tools/humanization/tells_lint.py DRAFT.txt \
       --source SOURCE-SECTION.txt [--owner OWNER-LINES.txt]
   ```

   A FAIL means rewrite the draft, not tweak it, then rerun. Never send a FAIL to Pangram.

   When a paragraph is mostly Joel's quoted lines (his dialogue), pass them with `--owner`. Otherwise his lines count as mine. With them excluded, the frame can be 20-odd words, so one "you can" fails coach density on its own (Love Doesn't Wait P6: 4.0 per 100). There I changed "You can answer" to "You answer" (the form P2 already uses) rather than rewriting the frame, and said so in the record.

   Run it on each new paragraph alone, not only on the section. Over a section, coach density gets diluted. P5's first attempt was REVIEW inside the text up to P5 (1.8 coach phrases per 100) but hard-fails alone (2.3), and Pangram put it at 100% AI (2026-09-26).
6. **Tell ledger in the drafts file.**
   - Every REVIEW item from the linter, with a disposition (KEEP, DELETE, REWRITE, MERGE, SUBORDINATE or MOVE) and why.
   - **First, a literal sense read of the paragraph as a reader who doesn't know the point (E67).** Then check it for marching order: can every sentence be labelled with its next job (E66)?
   - **Every row of `docs/HUMANIZATION-TELL-INVENTORY.md` (T01–T29, C01–C04), on the literal draft, before every Pangram call (E65).** The linter's flags are a subset. A draft that still looks AI to me doesn't go to Pangram.
     **Row by row, with the words (E88).** Each row gets its own line: the quoted words it matches, or "no words match". No line may clear several rows at once ("every other row ABSENT" is how Also Look Outward r2 went out with 13 tells PRESENT).
     **A repair aid, not a gate (Joel, 22:53; `tools/humanization/TELL-CALIBRATION-20260927.md`).** A blind audit of 28 known texts found most rows in human prose too, and the count of PRESENT rows barely separates the groups (AUC 0.59). That reviewer turned out to be unreliable. It gave a 100%-AI paragraph no PRESENT rows, so its numbers measure it, not the tells (correction, 2026-09-28).
     **The march blocks the call (Joel, 2026-09-27 23:52).** T02 (instruction-manual cadence), T09 (equal efficiency) and T13 (nothing noticed) are the marching order: "predictable cadence with optimized structure". If one is present, rebuild before any call, and don't explain it away. The other rows are repair hints. Pangram and the sense step are the gates. Model judges (Sonnet and Opus, 18 of 28 each on known paragraphs) don't stand in for Pangram.
   - **Before a whole-section check, run the inventory on the assembled section too (E70).** T02, T03, T08 and T20 show up between paragraphs, and a flag on owner text can come from my paragraph beside it.
   - The full catalog above, including the checks the linter can't do: A1 meaning and safety, A12 referents, D2 where the draft departs from what an AI would say, E1 naming (never "the kid"), E36 details that fit every reader, E8 and E33 premises and terms not yet introduced, E29 one owner practice per section.
   - Execute the repairs, then rerun steps 4–6 on the changed text.
   - **The reviewer-writer loop (2026-09-28; Joel, 00:56: "a subagent would give the instructions for fixing each sentence and the writer would follow those like an engineering task").** This is the review and repair step before Pangram. It replaces the numbered-inventory sweep below as the verdict.
     - A fresh Opus reviewer, set up with our own Pangram-labeled paragraphs (`tools/humanization/reviewer/`), judges the draft and writes one ticket per sentence.
     - A fresh writer carries the tickets out literally.
     - A fresh reviewer judges the result. When two reviewers' tickets differ, carry out both and let the next review choose.
     - When a reviewer says HUMAN, a cold reader checks sense. Its UNCLEAR notes go back through a reviewer as sense-only tickets.

     Validation: Opus got 43 of 53 held-out paragraphs right and let no AI through, and it called all 19 of Joel's own passages Human (`tools/humanization/REVIEWER-VALIDATION-20260928.md`). It's strict. Its HUMAN has been right every time so far. Its AI at 60–65, once the march is broken, has twice been Pangram Human, so check Pangram then. First use: Also Look Outward P1 passed with sense intact after six rounds (`experiments/REVIEWER-WRITER-LOOP-20260928.md`).

     Two rules. Never tell the reviewer a Pangram result when its verdict matters: it moved to HUMAN 95. And I don't write the tickets or the sentences myself. My reads of my own drafts scored 0 of 4 (`tools/PREDICTIONS.md`).

     **Order: fast checks first** (Joel, 16:29: "2hrs to humanize one paragraph is insane"). Three fresh writers draft in parallel (`reviewer.py draft`, or start from the existing draft). A cold sense read and Pangram run on each. The reviewer runs only when nothing passes; it's the slow step, 5 to 15 minutes a run. The expectations paragraph passed on the first round this way, with no reviewer run.
   - **Fresh-context sweep before Pangram (superseded as the verdict, 2026-09-28; still usable for repair hints).** Required for every section my sentences carry (SKILL.md's owner-calibrated fresh-context tell loop; the handoff's score-blind review). Build the prompt from the numbered inventory (`docs/HUMANIZATION-TELL-INVENTORY.md`, T01–T29 and C01–C04) with `tools/humanization/build_sweep_prompt.py`, give it the previous accepted prose (and any owner paragraphs) as context and my paragraphs as the target, and send it to a fresh subagent or another fresh route. Withhold the Pangram history and my reasons. On Borrow round 6 my own ledger kept everything, the fresh sweep found T02, T09 and T12, and Pangram said 100% AI.
     **Advisory until calibrated (2026-09-26).** The fresh-critic gate lets a model sweep gate only on axes that pass known controls. The numbered-inventory sweep on this route (a fresh Claude subagent) failed its negative control:
     - it reported 10 tells on the known-Human `When Healing Turns Into Checking`;
     - it reported 7 on the known-AI Borrow round 6;
     - T02 and T09 fired on both.
     So its rows are leads for my editorial read, not blockers. The blocking check is my own disposition of each flagged span: repair the real ones (a referent slip, a packed sentence I agree with), and record the reason for the rest. Rerun the controls whenever the prompt, the model or the route changes, and let the sweep gate again only for axes that separate them.
   - **UNCERTAIN isn't a pass (E86, provisional).** More than three UNCERTAIN rows means rebuild before any Pangram call. Don't keep them with reasons.
   - **Prediction (E86).** Before each call, write Human or AI and why. Score it against the result in `tools/PREDICTIONS.md`.
   - **Retries (E86).** Each retry names its hypothesis. One that keeps the failed paragraph's skeleton, with the same order and the same moves, isn't a test.
   - **Briefs get copied, meaning and all (2026-09-30).** In Love Doesn't Wait P2, all three round-two writers followed the brief's bullet order, and the result marched: two 100% AI. Round three named that order as the one that failed, and the writers reordered on their own. In P4, the brief said "went against the feeling of the moment" for the guide's "did argue with the emotional logic of the moment". All three writers copied it, and both grounding runs flagged it as a change of meaning. Quote the guide's phrase, or say plainly what it means; don't paraphrase it loosely.
   - **Stop rule.** If fixing one tell produces another (round 7: removing landings created six packed sentences), stop polishing. Diagnose at the level of structure, and take any change that moves or cuts preservation units to Joel.
7. **Architecture.** Heading promise, entry and exit state, each paragraph's job, then one literal top-to-bottom read of the section in place.
   - **Shape questions, advisory (2026-09-26).** These come from SlopShape (Madler, [arXiv:2609.15369v2](https://arxiv.org/html/2609.15369v2)). It found AI blog posts share a structural shape that survives the model rewording them. Its core features include:
     - an ending that restates the thesis or reframes it (its strongest single signal);
     - a thesis stated before the first part;
     - a summary or synthesis stage;
     - stakes escalated;
     - the editorial-explainer voice.
   - Sonnet's 15 rounds of the paper's game add the figures and a few shared AI micro-patterns (question runs, triads, "isn't X, it's Y"): `experiments/SLOPSHAPE-GAME-FINDINGS-20260926.md`.
   - Ask these of each section and of the article, where the paragraph checks can't see. They're review questions, not a gate. The paper tested 600–2,500-word commercial posts and single-pass AI text, not Pangram or edited text like ours.
   - On Borrow round 11 every paragraph passed alone, yet the section was flagged "at the close". Its last paragraph was tying things up: a callback to an earlier line, and the section's thesis word restated in the last sentence.
8. **Pangram (E27, E37; SKILL.md owner-delivery admission).**
   - Check every paragraph I wrote on its own, and then the whole section. A section can pass while one of its paragraphs is AI, which is the cheating the per-paragraph rule exists to stop (Joel, 2026-09-26).
   - The reverse happens too. On Borrow round 11 every paragraph passed alone, P6 and P7 failed together at 100% AI, and the section failed at the close. So the whole-section check stays. When it fails, a good first try is the sentence where Pangram's flagged span starts, plus any REVIEW-level coach phrase inside the span (E62). It's a heuristic: the span moves with changes elsewhere, so if that doesn't clear it, look at what comes before the span. Choose the spot from Pangram's result, not from a theory.
   - Check the section with its headings exactly as they'll appear, the h1 and h2 together where they stack. A heading can flip a borderline paragraph. On 2026-09-28 Joel's first Make the Protector Visible paragraph was 100% Human alone and 100% AI with only its h2 above it, and five of six h2 wordings failed over both paragraphs. A heading swap that passes is probably window luck; fix the flagged span if it's mine, and take it to Joel if it's his. **Headings (Joel, 2026-09-29):** never pick a heading by its Pangram result. A heading says what the section does, in the guide's terms. Candidate headings go through the grounding review (S6) before any Pangram check. If the guide's heading fails, fix the flagged span, or take it to Joel with the span. Don't shop for headings. "Keep Your Word" was installed on 2026-09-28 as the only one of six h2s that passed. Joel: "I don't see anything about keeping your word here... This is about making the protector visible, not keeping your word."
   - Run the checks side by side in separate browser tabs.
   - No limit on checks per turn (Joel, 2026-09-26 16:57: "you don't need a 3 check rule per turn, but just don't use your checks blindly wasting time and tokens. i have plenty of credit on pangram that's not the problem"). Every check tests a recorded draft with a reason behind it. Never send rewordings to see what sticks, and never recheck unchanged text.
   - Read results from the page text.
9. **Record and deliver.** Put the preservation ledger, the linter report, the tell ledger and the Pangram results in the drafts file. Show Joel the prose only if every gate passed; otherwise report gate status and keep working.
   - **End of every owner-facing turn: the whole article (OWNER-FACING-TURN-CONTRACT; Joel, 2026-09-26 23:38: "always give me the full humanized article up til what we had, at the end of every turn").**
     - Update `HUMANIZED-ARTICLE-SO-FAR.md` with the accepted prose and the current owner-review candidate in place. The candidate goes under a `<!-- CANDIDATE: … -->` note, so it's never shown as accepted.
     - Run `tools/humanization/render_article_so_far.py OUT.html --article <the article> --ledger <its OWNER-EDITS.json>`, and send the HTML file with the reply.
     - **The in-context page too (Joel, 2026-09-30: "I like how you are doing this original vs new diff, that's good make that durable").** Write a small map for the turn in `tools/in-context/` (labels, the start of each paragraph, the guide paragraphs, a note per row). Then run `tools/humanization/render_in_context.py MAP OUT --article <the article> --source <its source> --since <the commit Joel last saw>` before committing, and send the page with the article. It sets the guide's original next to each paragraph, highlights words added since the version he last saw, strikes the words cut, and marks new paragraphs. The text comes from the article and the guide, not from the map, so the page can't show something that isn't installed.
     - **The basic version plus a proposal (Joel, 2026-10-01: "look for opportunities like that to make something go from good to great, if they require taking liberties you can make proposals (like give the basic fixed version plus a proposed improved version, which doesn't have to pass the same evidentiary checks as long as it doesn't violate what's there or confabulate actual events that weren't stated)").** The basic version goes through the whole gate and gets installed. The proposal goes in the in-context page as a row of its own, marked as a proposal, with its Pangram result for his information. It goes in only when he picks it.
     - **Emojis (Joel's standing preference).** Add well-chosen emojis where they help warmth, emphasis, finding your way or scanning: headings, practical steps, callouts, calls to action. In tender passages, only where one means something there. None in evidence-heavy passages, only ones that render everywhere (Substack email), and never inside Joel's quoted words. Propose them in the in-context page, with the section checked on Pangram with them in. (2026-10-01, Joel: "btw i don't see you using any emojis, are you ignoring the emoji guidance or you didn't see the need yet?" They weren't in this gate or the writers' briefs, so I hadn't been applying them.)
   - **Owner edits (step 0).** The render's check has to pass. A red box means something a record calls done isn't in the article: fix it before sending, or correct the record.
   - **Clock (Joel, 2026-09-26: "a quick check at beginning and then at the end so i know how long it took… nothing in the middle").** Read the clock once when a turn starts and once at the end, and report both. Date each Pangram record and name its turn; don't read the clock mid-turn to time it. Never write a minute that wasn't read.

**Repairing a failed draft (B10, Joel 2026-09-26).** Don't fix it by swapping its phrases for less likely ones. Rewording while the structure and the other tells stay is what humanizer bots do, and it's what Pangram's "paraphrased or rewritten" flag describes. A phrase from a failed draft is judged like any other phrase, on whether it looks AI. The repair has to change what the draft says and how it's built.

## Owner bans (Joel, 2026-09-28 19:51)

These go into every writer and reviewer prompt (`tools/humanization/reviewer/owner_bans.txt`), and the linter fails the first two (O1, O2).
- "doesn't get to decide" and its family (a feeling or thing that "doesn't get to", "gets to", "gets a vote"). Joel: "one of the phrases AI completely colonized", "an optimal efficiency quippy formulation which humans just rarely use for non-humans". It came into the Make the Protector Visible drafts from my own brief.
- "Fine," "Good," "Great," as a clause of their own ("Fine, they're nice boots."). Joel: "super AI", and he had said it before.
- Wry humor. Joel: "wry in a strange way which i can't pin down". His is goofy and glad.
- Too many made-up scenes: a caution, not a ban. Joel, 20:13: "i'm not saying to ban made-up scenes, they can be useful, but you're overusing them here". Carry the guide's own examples first.
- Over-explaining listicles. Lists themselves are fine: "I have human and humanized paras with instructions and lists that DO pass". His way with a list is in Borrow One Competency's first paragraph (each item its own sentence, "Perhaps… Perhaps… Maybe… Even…", ending on the oddest one).
- Show every draft in context, next to the guide's original (Joel: "from now on, you need to show me your work in context"). `tools/humanization/render_in_context.py` makes that page (step 9).

## What the linter checks

- **Hard FAIL:**
  - Joel's tics;
  - coach phrases above 2 per 100 of my words (E41);
  - half or more of the paragraphs ending on a short line (B7/B13);
  - two or more paragraphs that are strings of instructions (E23);
  - three or more paragraphs with the same opener (B13);
- **REVIEW** (flags for the tell ledger):
  - contrast constructions (B2);
  - finished principles (B1);
  - lines that announce a paragraph (B5);
  - individual coach phrases;
  - "kid";
  - packed or list sentences (B4/E15);
  - short knock-downs (B3);
  - an action "it" ("did it", "do it", "tried it") in a paragraph's first two sentences (R1, 2026-09-30): name the thing instead. Joel caught "If you did it" after a paragraph that ended on a hard conversation, and no reviewer did;
  - short paragraph-final lines;
  - second person above 6 per 100 (a review note only since 2026-09-26: density didn't separate Pangram results);
  - with `--source`: the draft follows the source's order (D9). That's a note, not a failure. Organization is fine when the prose notices things (T13); since 2026-09-26 this is no longer a hard fail.
- **Not checked, on purpose:** phrases shared with failed drafts. Reuse isn't a tell by itself (see B10).

The linter covers a handful of mechanical tells. It is not the tell ledger, and a CLEAR never skips step 6.

## Calibration (2026-09-25, rerun 2026-09-26 after the fixes, extended the same day with the one-paragraph rounds and the Borrow Love h2 body)

Eighty-four texts with known Pangram 4.0 results (the last forty-four added 2026-09-27 and 28, nine of them from the reviewer-writer loop on 2026-09-28). The files are in `tools/humanization/calibration/`. A text with a `.owner.txt` beside it is linted with `--owner` set to that file.

Not included:
- the ablation variants of Joel's P5 fix;
- the section-level diagnostics of round 12.

They're near-copies of texts already in the set and would weight one paragraph several times. Their results are in the Borrow drafts file.

| text | Pangram | linter | hard reasons |
|---|---|---|---|
| Borrow One Function r1 | 100% AI | REVIEW (miss since D9 became a note) | — |
| Borrow One Function r2 | 100% AI | FAIL | coach 3.3/100; landings 3/6 |
| Borrow One Function r3 | 100% AI | FAIL | coach 2.8/100 |
| Borrow One Function r4 | 100% AI | REVIEW (miss since D9 became a note) | — |
| Borrow One Function r5 | 100% AI, "paraphrased" | REVIEW (miss since the "Mr." splitter fix, 2026-09-26) | — |
| Borrow One Job r6 (full gate) | 100% AI | REVIEW (miss) | none; the fresh sweep found T02, T09, T12 |
| Borrow One Competency r8e (with Joel's opening) | 91% AI, "paraphrased"; my paragraphs 5 of 6 at 100% AI | REVIEW (miss) | none |
| Music r2, my lines only | 100% AI | FAIL | second person 9.9/100 |
| Dangerous-adult H2 | 100% Human | REVIEW | — |
| Music r4 (installed) | 100% Human | CLEAR | — |
| Music r4, my lines only | 100% Human | REVIEW | — |
| Noticing Counts | 100% Human | REVIEW | — |
| Your Body Might Need Some Love First | 100% Human | REVIEW | — |
| Borrow P5 r10, my first attempt | 100% AI | FAIL (alone; REVIEW inside the text up to P5) | coach 2.3/100 |
| Borrow P5 r10b, my second attempt | 100% AI | FAIL | coach 2.4/100 |
| Borrow P6 + P7 together, r12 | 100% AI | REVIEW (miss) | none |
| Borrow One Competency r11, whole section | 24% AI, "at the close" | REVIEW (miss) | none |
| Borrow P3, Joel's minimal fix | Human (Joel's check) | REVIEW | — |
| Borrow P4 r10 | 100% Human | REVIEW | — |
| Borrow P5, Joel's minimal fix | Human, medium confidence (Joel's check) | REVIEW | — (coach 1.85/100, close to the limit) |
| Borrow P6, the Guide, r8e | 100% Human | REVIEW | — |
| Borrow P7 r11 | 100% Human | REVIEW | — |
| Borrow One Competency r13, whole section with Joel's P6 + P7 | 12% AI, "at the end" | REVIEW (miss) | none |
| Borrow One Competency r14b, whole section, one P7 sentence changed | 100% Human | REVIEW | — |
| Borrow Love h2 body r1, every paragraph passed alone | 35% AI, "scattered patches" | REVIEW (miss) | none |
| Borrow Love h2 body r2, one P2 sentence swapped for a quip | 65% AI, "throughout" | REVIEW (miss) | none |
| Borrow Love P2 r3 | 100% Human | REVIEW | — |
| Borrow Love h2 body r3, with P2 r3 | 100% Human | REVIEW | — |
| Borrow Love, Goodwill P1 r1 (later fidelity-rejected, E71) | 100% Human | REVIEW | — |
| Borrow Love, Goodwill P1 r2 ("you" voice) | 100% Human | REVIEW | — |
| Borrow Love, Goodwill h3 r3 ("you" voice) | 54% AI, "in the later part" | REVIEW (miss) | none |
| Borrow Love, Ask God P1 | 100% Human | REVIEW | — |
| Borrow Love, Ask God P2 | 100% Human | REVIEW | — |
| Borrow Love, spiritual-hurt P1 r1 | 100% AI | REVIEW (miss) | none |
| Borrow Love, spiritual-hurt P1 r2 | 100% AI | REVIEW (miss) | none |
| Borrow Love, the whole section (h2, Goodwill and spiritual-hurt P1 by Joel, the rest mine) | 100% Human | REVIEW | — |
| Adult Apprentice P1 r1 | 100% AI | REVIEW (miss) | none |
| Adult Apprentice P1 r2 | 100% Human | REVIEW | — |
| Adult Apprentice section r1 (P1 r2 + P2 + P3) | 100% AI | REVIEW (miss) | none |
| Adult Apprentice section r2 (P1 r2 + P2 r2) | 100% AI | REVIEW (miss) | none |
| Adult Apprentice section r3 (P1 r2 + P2 with Joel's cut) | 100% AI | REVIEW (miss) | none |
| Three Adult Functions P1 r1b (a quip per beat) | 100% AI | REVIEW (miss) | none |
| Three Adult Functions P1 r2 | 100% AI | REVIEW (miss) | none |
| Three Adult Functions P1 r3b (a "So" conclusion at the end) | 100% AI | REVIEW (miss) | none |
| Three Adult Functions P1, Joel's minimal fix (his last sentence) | Human (Joel's check) | REVIEW | — |
| Three Adult Functions P1, r3b without its last sentence | Human (Joel's check) | REVIEW | — |
| Three Adult Functions P2 | 100% Human | REVIEW | — |
| Three Adult Functions P3 (the Nurturer) | 100% Human | REVIEW | — |
| Three Adult Functions P4 (the Protector) | 100% Human | REVIEW | — |
| Three Adult Functions P5 r1 (the Guide; a thesis opener) | 100% AI | REVIEW (miss) | none |
| Three Adult Functions P5 r2c | 100% AI | REVIEW (miss) | none |
| Three Adult Functions, heading + P1–P4 | 100% Human | REVIEW | — |
| Three Adult Functions, restored opening r1 (a claim opener) | 100% AI | REVIEW (miss) | none |
| Three Adult Functions, restored opening r2 (a situation opener) | 100% AI | REVIEW (miss) | none |
| Inner Monologue P1 with the "ask" fix (mostly accepted Episode 008 text) | 100% Human | REVIEW | — |
| Catch the Hook P1 with the hook fix (mostly accepted Episode 008 text), linted whole | 100% Human | **FAIL (false positive)** | coach 3.1/100, all three phrases in the accepted sentences |
| Also Look Outward P1 as accepted 2026-09-18 (GPT lane) | 100% AI | REVIEW (miss) | none |
| Also Look Outward P1 with the first fix | 100% AI | REVIEW (miss) | none |
| Write It P4 (Tyler) | 100% Human | REVIEW | — |
| Write It P5 (Tyler, with Joel's line) | 100% Human | REVIEW | — |
| Write It, whole section with P4–P6 | 100% Human | REVIEW | — |
| Chicken-and-Egg Guide paragraph r1 (Joel's sentences smoothed by me) | 44% AI, "in the later part" | CLEAR (miss) | none |
| Chicken-and-Egg Guide paragraph r2 (Joel's sentences as he wrote them) | 100% Human | REVIEW | — |
| Chicken-and-Egg P2 with the worth line (Joel's paragraph, one sentence mine) | 100% Human | CLEAR | — |
| Borrow One Competency with the enjoying Nurturer after the warmth paragraph (every paragraph passed alone; the section passed without it) | 47% AI, "paraphrased", "scattered patches" | REVIEW (miss) | none |
| Borrow Love, the whole section with the enjoying Nurturer at the end of the h2 body | 100% Human | REVIEW | — |
| Chicken-and-Egg three jobs r1b (a definition sentence for each job) | 100% AI | REVIEW (miss) | none |
| Chicken-and-Egg three jobs r2 (both jobs in one scene) | 100% Human | REVIEW | — |
| Chicken-and-Egg Guide paragraph alone, without its old first sentence | 100% Human | CLEAR | — |
| Chicken-and-Egg three jobs r3 (r2 with Joel's Guide sentence) | 100% Human | REVIEW | — |
| Also Look Outward P1 rewrite r1 (the installed build, new wording) | 100% AI | REVIEW (miss) | none |
| Also Look Outward r2, first paragraph (passed four cold reads for sense) | 100% AI | REVIEW (miss) | none |
| Also Look Outward section with r2 | 57% AI, "throughout" | REVIEW (miss) | none (a B1 on Joel's P2) |
| Also Look Outward r5, first paragraph (a textbook dinner vignette) | 100% AI | REVIEW (miss) | none |
| Also Look Outward r7 (a three-sentence remark, no instructions) | 100% AI | REVIEW (miss) | none |
| Also Look Outward P1, loop r3B2 (one long question, Gibson in parentheses inside it; fails the sense read) | 100% Human (short text) | REVIEW | — |
| Also Look Outward P1, loop r4sf1 (r3B2 with sense tickets) | 100% Human (short text) | REVIEW | — |
| Also Look Outward P1, loop r5v2 ("promising to be more careful how you bring things up") | 100% Human (short text) | REVIEW | — |
| Also Look Outward P1, loop r6b (r4sf1 with a two-word sense fix; passes the sense read) | 100% Human (short text) | REVIEW | — |
| Also Look Outward section with r6b as P1 | 100% Human (313 words, full confidence) | REVIEW | — |
| Also Look Outward P1, Joel's final (r6b with his three edits) | Human, medium (Joel's check) | REVIEW | — |
| Also Look Outward expectations paragraph d2 (a fresh writer's first draft) | 100% Human (short text) | REVIEW | — |
| Also Look Outward expectations paragraph d3 (a fresh writer's first draft) | 100% Human (short text) | REVIEW | — |
| Also Look Outward section with Joel's final P1 and d2 | 100% Human (375 words, full confidence) | REVIEW | — |

Since D9 became a note and the sentence splitter stopped breaking "Mr. Rogers" in two, the linter hard-fails three of the eight AI texts (r2, r3, music r2) and none of the five Human ones. Since the second-person hard fail became a review note (2026-09-26), it hard-fails two (r2, r3b), still none of the Human ones.

With the one-paragraph rounds added:
- It hard-fails four of the thirty-nine AI texts (r2, r3b, and both P5 attempts) and one of the thirty-six Human ones (2026-09-28: 75 texts). The Human one is Catch the Hook P1 linted whole: three coach phrases ("You might notice…", "Or you might notice…", "You can figure that out later") in 97 words, and Pangram says 100% Human. So the coach limit can block human text when the phrases are short and casual. It's still a hard fail for my own drafts (what it was set on), but a coach FAIL on text someone else wrote, or on short paragraphs, gets read before it's trusted. The two spiritual-hurt paragraphs are 100% AI and only reach REVIEW: what sank them (a therapist's sequence, stacked hedges, a reassuring close) isn't mechanical. Nor is what sank Three Adult Functions P1 r3b: a last sentence that concluded the paragraph (E74). Cutting only that sentence passed, so the pair is a clean control for T29.
- At paragraph level, coach density separated the two failing P5 attempts (2.3, 2.4) from every Human paragraph (at most 1.85).
- It misses all six context failures (the P6 + P7 pair, the whole section in rounds 11 and 13, the Borrow Love h2 body r1 and r2, and Borrow One Competency with the enjoying Nurturer), where every paragraph passes alone. In the last one a paragraph that passed alone, put in a section that passed without it, flagged itself and the Protector paragraph beside it: it restated the warmth paragraph's point, and it made the jobs march one per paragraph (E49). For the h2 body, the inventory run on the assembled section found them (E70). In round 13 its only coach flag in P7 was the sentence where Pangram's span started, which is why E62 says to check that flag first. Rounds 1, 4 and 6 only reach REVIEW. What sank them (nothing noticed, equal weight, teaching cadence, a tidy taxonomy) isn't mechanical, which is why the fresh sweep with the numbered inventory is a required step. The linter is a guard against obvious failures, not a writing guide.

That's a small set, and the thresholds were set on it, so expect misses. A CLEAR or REVIEW only means the mechanical tells weren't found; it doesn't mean the draft reads human. Add every new Pangram result to the calibration set and retune the thresholds if they start letting AI through.
