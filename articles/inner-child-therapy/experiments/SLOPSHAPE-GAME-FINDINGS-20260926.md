# SlopShape "Spot the slop" game — findings for this article (2026-09-26)

Joel asked for Sonnet to play the free game at https://sitefire.ai/spot-the-slop, which is built on SlopShape (Madler, [arXiv:2609.15369v2](https://arxiv.org/html/2609.15369v2)). A Sonnet subagent played 15 rounds in the built-in browser and got all 15 right. It took about 24 minutes. This is my summary of its notes, in my words; the raw notes quoted the posts and aren't kept here.

**Advisory only.** The game's pairs are B2B blog posts of 600–2,500 words, single-pass AI against pre-ChatGPT human posts. Pangram at paragraph level is a different test.

## How the game scores

- Each round shows two post openings, one human and one written by one of five models (GPT-5.4, Claude Sonnet 4.6, Gemini 3 Flash, DeepSeek V3.2, Kimi K2.5).
- Every passage gets a value for each of the ten signals, marked as the value AI posts usually take or the one humans usually take.
- Across the 15 pairs, human passages scored 1–3 of 10 AI signals and AI passages 5–10.
- The same model's posts ranged from 5 to 10, so a model isn't a fixed fingerprint.

## The signals, with the game's own figures (identical each time they came up)

| signal | AI-typical value | AI posts | human posts |
|---|---|---|---|
| Closing move | restates the thesis or reframes it | 77% | 12% |
| Payoff | promised in the title | 89% | 26% |
| Legacy vs. modern | the argument is built as old vs. new | 76% | 26% |
| Thesis | stated before the first section | 93% | 51% |
| Stakes | the opening escalates them before making its point | 88% | 52% |
| Voice | an editorial explainer talking about a category | 71% | 40% |
| Problem placement | named in the title or the opening sentence, before any setup | 53% | 24% |

- The game gave no figures for summary stage, path to participate, or length.
- Several signals take more than two values:
  - Voice: the human-typical values are institutional brand, curator or compiler, and named individual expert.
  - Closing move: the human-typical values are a call to action, a pointer to related content, or just stopping.
  - Payoff: it can sit in the opening paragraph instead of the title, or never be promised at all.
  - Problem placement: it can surface after some setup, or stay implied.

## What the human posts did

- **They were grounded in one real case**: a company's own product, one team's migration, a named person. The AI posts talked about a category ("engineering teams", "resellers").
- **The voice signal is about being grounded, not about formality.** A chatty, joke-filled post still counts as an editorial explainer if it never anchors to a specific person or case.
- **Openings start low and endings move on.** Human posts open plainly and end by stopping or pointing elsewhere. AI posts open high and loop back to the thesis.
- **Micro-patterns the AI posts shared**, outside the ten signals:
  - "isn't X, it's Y";
  - runs of rhetorical questions (one opening had six in a row);
  - parallel triads, and rules set up only to be knocked down;
  - stacked hyperbole.

## What transfers here, and what doesn't

- **Joel's own case is the human voice.** Where the source speaks as Joel ("my practical version", "I don't want to flatten them", "a feeling I cannot honestly access"), keep his first person. I can't invent his experience, so elsewhere ground a point in a familiar instance (E62, E64).
- **Question runs.** Borrow Love BL-U7 is a run of four questions from the source. Carry the content without the run.
- **Section endings** should stop or point onward rather than restate. This was only part of the story on Borrow (see E62), so it's a question to ask, not a rule.
- **Openings that diagnose in the first sentence** are a shape question for whole-section checks.
- **Don't imitate the human "noise".** The game credits typos, stray spaces and filler to humans, but `SKILL.md` forbids adding errors or fake specificity to look human.
