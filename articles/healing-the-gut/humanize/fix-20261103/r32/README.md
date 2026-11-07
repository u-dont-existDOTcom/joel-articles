# r32: Pooyan's news, and the version for his post's update (2026-11-07)

When I asked whether to update his post, Joel answered with one change first: "Oh, one change. Pooyan is actually all
better from his gut issues now that nobody could fix. Apparently he didn't need the insane treatments he was doing on
himself. What worked was some Bombax ceiba flower i sent him. It's sold on amazon cheap. AskRigor is what told me about
this when doing ethnobotanical research. My other friend, Acacea, is also benefitting from this flower".

r32 is r31 with that news as a fourth sub-item of "Years of accumulated shit in your guts", after the A1-dairy relapse
it updates and before the CAUTION (`build_r32.py`):

> Update: Pooyan is actually all better now from his gut issues that nobody could fix. Apparently he didn't need the
> insane treatments he was doing on himself. What worked was some Bombax ceiba flower, from the red silk-cotton tree,
> that I sent him. It's sold on Amazon, cheap. AskRigor, my research tool, is what told me about it when I was doing
> ethnobotanical research. My other friend, Acacea, is also benefitting from this flower.

His facts and phrases, two of his sentences word for word. Mine: "now" moved so "now that" can't read as "since";
"AskRigor, my research tool," because this is now where a reader first meets the name; and the gloss "from the red
silk-cotton tree" ([Flora of Qatar](https://www.floraofqatar.com/bombax_ceiba.htm): "Kapok, red cotton tree, red
silk-cotton"). The item with all four sub-items read [Human Written, one High window](https://www.pangram.com/history/99c2dd24-0dcf-4898-8321-28ccf6380474)
(#210).

## The update, ready for his OK

- `live-update/make_r32_html.py` → `live-update/r32.html`: r31.html (`../r31/live-update/`) with the new sub-item, its
  label bold like the CAUTION after it, quote marks curled; all 75 lines his extension reads are in it, exactly and in
  order (`live-update/EXPECTED-TEXT-r32.txt`).
- `../live/UPDATE-PLAN-4.json`, rebuilt from r32.html (`make_plan.py r32.html r12.html UPDATE-PLAN-4.json`): 95 blocks
  before and after, the same six native blocks. It replaces the plan built from r31.html.

It goes in as `../r31/README.md` says, with r32.html and this plan, once he says yes; no email. Afterwards the live
post's text is compared with `live-update/EXPECTED-TEXT-r32.txt` character by character (E362 (gut)), and his extension
can read the live post itself as the last check.
