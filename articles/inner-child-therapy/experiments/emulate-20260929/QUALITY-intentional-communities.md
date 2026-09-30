# Intentional communities — candidate review (2026-09-30)

**Decision: no article candidate accepted.** The 49 revised eligible inputs have A/B website captures, but option-level detector scores do not establish section quality or source fidelity. The original article remains the source of record.

## Evidence

- Pangram called all ten checked short Emulate options **Human Written, 100% Human**. When revised 0101 A and B were inserted into the first section, both were **AI Detected, 58% AI / 42% Human** (975 and 984 words scanned). The original section baseline was also 58% AI / 42% Human. Exact section inputs and highlighted spans are in `runs/pangram/` and `runs/pangram.jsonl`.
- D6 link test: the first linked input had `[*Where’s Utopia?*](https://ibogaqueen.substack.com/p/wheres-utopia-click-read-more-my)`. A moved the anchor to a truncated “Continue reading” phrase; B dropped the link and referred to a nonexistent link below. Neither preserved the linked words and emphasis. See `runs/articles/intentional-communities/D6-LINKS.md`.
- Revised 0102 B adds a memory claim (“many more that I can’t even remember the names of”) absent from the source. In 0103, A changes the remembered meeting thought into a different direct quote; B adds “mostly around electricity” and says the woman started the nut-butter factory, neither stated in the source.
- 0201 A calls the father’s 1988 film a film made “a few years ago,” altering the chronology. B says the 2023 Surgeon General advisory was “just released.” Both options flatten or move claims even though Pangram called them Human.
- The original 449-word 0501 A/B both ended mid-thought; the split second pass is retained separately. The first-person memories need Joel’s approval after source comparison.

## Gate and next work

No selected option is an approved replacement. Review each remaining eligible span against the exact source, preserve baseline-Human paragraphs byte-for-byte, restore links/media from the original Markdown, and check seams and section context only for a source-faithful assembly. The first section currently fails both the detector-context and D6 gates. No source, candidate authority, or publication was changed.
