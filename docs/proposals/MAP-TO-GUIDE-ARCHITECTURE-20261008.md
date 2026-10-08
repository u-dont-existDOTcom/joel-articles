# From the map to the two guides: a brainstorm (2026-10-08)

Joel, 03:57 UTC: "the guide updates were sent to you due to map changes which GPT believed should be reflected in the guide, because the guide and map are supposed to complement each other and agree with each other, but that's also why we have the AI guide and the humanized guide, in case the map-based AI guide is just too much stuff for people to read. altho, i'm open to your brainstorm on the best architecture and how to ground the map and how to update the guide as the map is updated because i'm mainly updating the map now (based on using it on clients) rather than the guide directly. did you think none of that stuff needed saying in the guide even tho it needed to be in the map?"

## Your question first

No. Much of it does need saying, and last turn I got that wrong. I called the October 4 paragraphs "the app's rules" and parked all of them, because they weren't on the queue and some lines are written from the app's side. But that pull request's own plan made them guide text on purpose, so the guide would agree with the map. The queue made the next day listed the other October 4 additions and missed these, which looks like an oversight. They're back on the list (section 7 has what I'd carry from them).

What's still true is narrower. A few lines in them are about how the app behaves toward a client, not about what a reader does: not re-offering inner-child work after a no, the bookkeeping for a pause, "this app". Those lines don't translate into advice for a reader, so they stay out of the humanized guide.

## 1. How it works today (from innerSignalGraph's code and records)

- **The app reads the AI guide.** On every client turn, `src/orchestrator/context-builder.mjs` picks the guide passages that match the conversation (`selectGuideExcerpts(guide.text, query, …)`) and gives them to the model, next to the map's routing. That's why a map change also changes the guide: the model shouldn't read guide text that says something different from the map.
- **So the AI guide has two readers.** One is the app's model, which needs every case and caution spelled out, including notes on its own behavior ("do not keep trying to sneak it back in", "or this app the only place you can belong"). The other is a person, who needs to know what to do. The October 4 additions were written mostly for the first reader. That's why they're dense with cases and caveats, and why my drafts of them kept coming out as runs of rules and failing Pangram.
- **Two routes into the humanized guide, and they don't match.** One is the new versions of the AI guide (r1 to r4); the other is the queue. #128's October 4 additions went on the queue; #126's, the same day, didn't.
- **Grounding is uneven.**
  - Each change has an owner outcome in its plan and in the state file.
  - Some have a lesson in `THERAPY-LESSONS`, with its evidence (an owner decision, sample replies, tests). The October 4 continuity change has none.
  - The 54 owner amendments are text only. None says which client moment it came from, or whether it rests on one case or a pattern.

## 2. What each piece is for

1. **Lessons: why something changed.** One record per thing learned with a client. `THERAPY-LESSONS` already has the right shape; make it required for every map change. Each lesson records:
   - what happened (no private facts);
   - what the app did, and what would have been better (your call);
   - the principle, in a sentence or two;
   - how general it is: this one client, a pattern you've seen before, or part of your framework;
   - the evidence: your experience, research (cited), or both.
2. **The map: what the app does.** Nodes, routes, state, prompts and tests, as now. Each change points to its lesson.
3. **Teaching points: what a person should understand or do. This is the missing piece.** For each map change, the map lane writes one or two plain sentences from the person's side, or says "app only" if nothing changes for a reader. A teaching point records its map change and its lesson, and where in the guide it belongs. It also records whether the guide already says it, and whether the humanized guide needs it or can leave it to the AI guide.
4. **The AI guide: the complete guide.** It's for people who want everything, and for the app as context. It's written from the teaching points, in "you" voice, and it agrees with the map. Notes about the app's own behavior go in the app's prompts, or in a clearly marked part of the guide that the humanizer skips.
5. **The humanized guide: the article.** It carries the teaching points a reader needs, in your voice, and it can point to the AI guide for the rest. It doesn't have to grow with every client lesson.

The rule you asked for last turn is exactly the teaching-point record: what changed, and why a reader needs it.

## 3. When you update the map from a client

1. You tell the map lane what went wrong and what you want.
2. The map lane (GPT/Codex) writes the lesson, changes the map, and adds a test. Then it writes the teaching point, or marks it "app only". It updates the AI guide from the teaching point, and puts the teaching point on the queue, all in one change.
3. A check in that repository makes it hard to skip: if a change touches guide text, it must also touch the queue or mark that text app-only. That check would have caught #126.
4. I (the humanization lane) read the queue. I check each teaching point against the whole article. You OK the ones the article needs, and I draft those, one idea per paragraph, in the section where each belongs. Each teaching point's status is recorded: in the article, left to the AI guide (with the reason), or waiting.
5. You review two kinds of things: teaching points, a sentence or two each in a weekly batch, not paragraphs of rules; and drafts in place, as now.

## 4. Grounding the map

- **No map change without a lesson.** It can be short, but it names the client moment (without private facts) and the principle.
- **Mark how sure it is.** Something from one session is provisional until it shows up again, or until you say it's a principle. That keeps one client's case from becoming a rule for everyone.
- **Fix the principle, not the incident.** Before adding a rule, check whether an existing node already covers it and only needs a sentence. Most of the October 4 additions could have been a sentence or two added to an existing node.
- **Prune sometimes.** Every so often, merge amendments that overlap, and retire caveats nothing has used, so the map and the guide don't gain a caveat per client.
- **Keep the tests.** Each lesson keeps its routing test (the G-cases, as now). Sample replies stay labeled as samples, not results.

## 5. Options for the AI guide

- **A. As now, plus teaching points, and app notes kept out of guide prose or marked.** This is the smallest change, and nothing in the app's loading changes. My recommendation for now.
- **B. Split the AI guide.** The model gets an app-guidance file (cases, cautions, its own behavior); people get a guide written from the teaching points. Each is better for its reader, but it's more to maintain, and the model then needs both files. Worth it if the app-directed text keeps growing.
- **C. Generate the AI guide from the map.** It always agrees with the map, but it would read like a manual. Your voice and the humanized guide would have to carry everything.

## 6. Keeping the humanized guide in step

- **One way in: the queue of teaching points.** A guide-text change that isn't on the queue gets asked about, not guessed at.
- **Check against the whole article first** (the dedup we added this week). Fold a point into an existing paragraph before adding one.
- **A budget.** The article grows a little per batch, not per lesson. Anything that doesn't fit can live in the AI guide with a pointer.
- **Batches.** Humanize when a handful of teaching points have built up for one section, not after every map change.

## 7. Applied to the October 4 changes (#126)

What I'd carry, from the reader's side. Tick the ones you want, and I'll draft only those.

| | Teaching point | In the article already? |
|---|---|---|
| T1 | If a depth is too much, go gentler instead of pushing through with one technique after another, and instead of giving up on your little one. | Partly ("leave the deeper conversation until later", "change course sooner (stopping counts)"). New: going shallower, and not hopping between techniques. |
| T2 | If you can't stop and come back, or going inward is making it worse, come back out to the room first. Later, a gentle way back in is one protective thing in your life, or a short eyes-open hello before any imagery. | No |
| T3 | If you take a full break from your little one, note why and how far you'd got, and come back at or below that when you want to. | No (maybe more than a reader needs) |
| T4 | How pleasant a session felt doesn't tell you whether it was too much. Hard isn't harm, and staying present isn't enough by itself. | Partly (intense isn't progress: your crying story) |
| T5 | What tells you more: the next few days (sleep, getting through the day), whether you want to go back toward it, and whether it felt hard but workable or just too much. | No |
| T6 | If you can't tell yet, don't call it healing or harm. Make the next one a bit easier, one change at a time. If you're getting worse, change several things and get support. Bring the challenge back gradually. | No |
| T7 | Dreams and images show what feels important or needed now. They aren't evidence that something happened, and they shouldn't be used to build a memory. | Partly (said for memories in an altered state) |
| T8 | If being alone with it was part of the wound, reaching toward people is part of caring for your little one, and you don't have to get yourself sorted out first. | No (texting a friend is already an example elsewhere) |
| T9 | More than one place to belong. Keep the good people, add others, and not every door has to open. Let the Protector watch for a group that wants to be your only one. | No |

What I'd leave to the AI guide:
- the no to inner-child work (you cut it, and "Not wanting to do it anymore is a reason too" already covers the reader's side);
- the pause bookkeeping ("observable reactivation condition");
- "this app".

## 8. What I'd change now, if you agree

1. **The map lane writes a teaching point for each map change** (or "app only"), adds the guide-text check, and fills the queue with teaching points. This goes to innerSignalGraph as a suggested fix, and replaces my proposal from last turn, whose "not on the queue means app-only" rule was wrong. Filing it needs your OK; this session can't write to that repository on its own.
2. **In this lane:**
   - I draft from teaching points you've ticked, not from the AI guide's paragraphs.
   - The tool's check stays: a guide addition needs its map change and its reader need, which together are the teaching point.
   - The gate no longer treats an unqueued change as app-only.
3. **Next:** draft T1 to T9 (whichever you tick) where they belong, one idea per paragraph, checked against the article, and C2 after your C1 if you want it.
