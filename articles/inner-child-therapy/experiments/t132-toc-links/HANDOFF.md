# Turn 132 handoff (paused 2026-11-20 ~17:25 UTC, usage limit)

Request: see ../t132-answers/JOEL-20261120-1639.md.

## Done (live on Substack, post 189761959, updated 17:06:32Z, no email sent)
- 153 headings set exactly as his picks (HIS-PICKS-RESOLVED.json; his new h4 "Compassionate Exit?" kept; S122 kept his post edit "Opening Up Carefully"; S106 his "Life’s a trip also").
- 4 text edits: S132 "of their approach" -> "of a therapist’s approach" (intro no longer followed the short heading); S046 Healther->Healthier; S081 and S094 section names updated to the new headings.
- 22 section-mention links added (1 -> 23 section links; all anchors checked on the rendered page). List: publish/PLAN.json. Link form: https://ibogaqueen.substack.com/i/189761959/<slug>; slug rule in publish/lib132.js (verified on 151 anchors).
- Intro-sentence check over all 102 changed headings (HEADING-CHANGES.json): only S132 needed a fix. "Confused After Trips?" (S103) intro he rewrote himself; it reads fine.

## Safety flag (his content, NOT edited; raise with him once)
S013 crisis paragraph ("Maybe you’re reading this about to act...") sends readers in pain to "Compassionate Exit?" as "an alternative plan". That section frames fasting as a way to give up on an unbearable life and claims fasting cured end-stage PML in 10 days. Suggest: drop the pointer from the crisis paragraph; say plainly the section is not a crisis plan; fasting needs medical supervision; the cure story is one anecdote.

## Order test (his question: which model gets closest to his order)
Score: order/score_order.py vs his 20 re-parentings. Results so far: no model, alone or with rules v1, came closer to his order than leaving the 4 Nov order unchanged (tau 0.923). Models catch local moves (N126 -> Physical Pain, N132 -> Differentiation) but none made his big moves (Shame/Forgiveness -> Nurturer, altered-state -> Altered States, spiritual -> Inner Guide, Vow -> Practicing).
Rules v2 (order-test/input/RULES-ORGANIZE-2.md) outputs ready but NOT yet scored: SONNET-rules2-1, FABLE-rules2-1. OPUS-rules-1/2 (v1) also unscored. GPT outputs from laptop: GPT-gpt-*-OUTLINE.json.

## Heading test
Exact-match baselines vs his 146 picks: Opus t130 132, Fable t131 121, Opus B2 119, GPT C 91, his 17 Nov 43. New runs with RULES-HEADINGS.md: SONNET-1, FABLE-1, GPT-1 in heading-test/out, NOT yet scored (heading-test/validate.py; then blind Sonnet judge same/close/different).
Patterns in his picks: Title Case, short and clear; questions for "is this me?" sections; positive framing; "you"; no meaning changes or misleading words; second heading for two-part sections; his exact old words are not a priority.

## Next steps
1. Score rules-v2 order runs + heading runs; pick the best model+rules; save universal rules into docs/ (organizing prompt, heading rules, "section mentions are always linked", intro-sentence rule) and update docs/FIXING-AN-ARTICLE.md §3. Add tools/humanization/section_links.py from publish/lib132.js slug rule.
2. Options page: own-words box sized to each level's sidebar room (toc_sidebar.py ROOM h1 217, h2 205, h3 193, h4 181 px, Inter 15px) for 3 and 4 columns.
3. REVIEW.json: 35 flagged passages (11 high) -> marking page for him; not applied.
4. Questions for him: S029 lower case, S035 kept "Shame Says “Unlovable”", S139 "If They Can’t Hear You" - why.
5. Lane bookkeeping: lane_state.py 132, lessons file docs/lessons/2026-11-20-1639-inner-child.md, OWNER-QUESTIONS.md, merge via lane_push.py.
6. After this article: fix links + ToC on hypnosis.u-dont-exist.com, then nibbana.u-dont-exist.com.
