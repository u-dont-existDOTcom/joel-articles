# r33: AskRigor linked, the version that goes into his post (2026-11-07)

Joel, 12:10 UTC: "link askrigor to askrigor.com and then post the article pls thanks". r33 is r32 with two links to
https://askrigor.com (`build_r33.py`): the name in Pooyan's item, where a reader first meets AskRigor, and the domain
written out in the plant foods item ("re-check it with askrigor.com"). No words change, so nothing new to check: the
text is r32's, whose new item read Human Written, High (#210), and the rest is draft E's (#208) with the oxytocin gloss
(#209).

- `live-update/make_r33_html.py` → `live-update/r33.html`: r32.html with the two links, made as the post's other links
  are; all 75 lines his extension reads unchanged (`live-update/EXPECTED-TEXT-r33.txt`).
- `../live/UPDATE-PLAN-4.json`, rebuilt from r33.html: 95 blocks before and after, the same six native blocks.

It goes in as the second update did (`../live/README.md`, `../live/LIVE-CHECK-20261104b.json`): `update2.js` in the
post's editor with the plan and r33.html from a pushed commit, `dispatch.js`, then Continue and "Update now" with "Send
via email" unchecked. Then the live post's text is compared with `live-update/EXPECTED-TEXT-r33.txt` character by
character (E362 (gut)).
