#!/usr/bin/env python3
"""Turn 105: IDEAS.md, the reader's edit (edit/) and the hedge read (caveats/) on one page for Joel and GPT (question 102.4).

Joel, 2026-10-24 18:40 UTC: "go thru all the other sections and figure try to make those read better as well, then we can see
what gpt thinks of your ideas on that". Each read's own page comes from tools/humanization/clarity_read.py (its ITEMS.json,
with my checks); this puts the two together, numbered E1... and H1... so one reply can name any item.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402

INTRO = '''# Ideas for the other sections (turn 105, question 102.4)

Joel, 2026-10-24 18:40 UTC: "go thru all the other sections and figure try to make those read better as well, then we can see what gpt thinks of your ideas on that. my goal is i want something that reads engagingly like i assume Lucia's book does (does it?)".

How Lucia Capacchione's *Recovery of Your Inner Child* reads beside this article is in [ENGAGING.md](ENGAGING.md), next to this page. Her own story comes first, the reader is doing an exercise within a page or two, and her sentences are plain and sure of themselves: one in twenty-five has a hedge like may, might or sometimes, against one in five here.

Two kinds of fresh reader went through the whole article in parts, each told nothing about earlier drafts:

- **The reader's edit (E1 to E{ne}):** where a reader has more to work through at once than they need, and the smallest structural change that fixes it: a heading, a move, or the cut of a repeat or of a last line that adds nothing. No rewording. Eleven readers, a part of the article each (`edit/`).
- **The hedge read (H1 to H{nh}):** lines a reader doesn't need where they are: a hedge, a reassurance, a takeback, a caution said again. Six readers, a part each (`caveats/`).

The reader's edit asked five questions of each section, and its "question 1" to "question 5" are these: (1) how many decisions does one passage ask of the reader at once; (2) does a second subject start inside the section without a heading of its own; (3) does each warning change what the reader does there, or only explain why the instruction has qualifications; (4) is a paragraph performing, with a joke, a metaphor or a last line that only makes it sound casual; (5) what would an attentive reader still need here. Joel's choices on the first sections that had this edit: he put in all four headings proposed, one of them over a single paragraph ("Why the Tangle Is Heavy"), and declined the one label, since the paragraph's first line already said what it was for. He kept two passages of his own (a study's three sentences that make a warning land, and a stock phrase that starts the article's dream thread), and he cut a parenthetical of his that used a term two sections before it was explained.

I checked each item against the whole article and Joel's earlier answers (each reader's brief lists the ones that bear on it), and each says whose words it touches. Words of his change only if he says so. Two sections already had this edit (The Inner Guide; Borrow One Competency at a Time), so nothing is proposed there.

Nothing here is in the article yet, and nothing is checked in Pangram. Whatever goes in gets its checks first: a changed paragraph alone, then its section.

To answer: "102.4: your picks" takes every pick below; or name the ones you'd change, like "E3 B, H7 A".
'''


def numbered(page, prefix):
    """The page's own "### n." headings as "### E n." (or H), and its title one level down."""
    page = re.sub(r'^### (\d+)\. ', lambda m: '### %s%s. ' % (prefix, m.group(1)), page, flags=re.M)
    return re.sub(r'^# ', '## ', page, count=1, flags=re.M)


def main():
    edit, ne = C.page(HERE / 'edit', title="The reader's edit: what a reader has to work through")
    items = json.loads((HERE / 'caveats' / 'ITEMS.json').read_text(encoding='utf-8'))
    live = [x for x in items if x.get('status', 'keep') == 'keep']
    his = sum(1 for x in live if 'yours' in (x.get('whose') or ''))
    mine = sum(1 for x in live if 'mine' in (x.get('whose') or ''))
    cut = sum(1 for x in live if (x.get('my_pick') or '').upper() == 'A')
    hedge_intro = ('Most of what the hedge readers flagged is your own wording: %d of the %d lines, against %d of mine (the '
                   'rest I couldn\'t place). My picks keep most of yours, since they\'re your voice and a lot of them are in '
                   'text you checked yourself, and cut %d in all. So if you want the article closer to her plain, sure '
                   'sentences, the B items below are where that would come from.' % (his, len(live), mine, cut))
    hedge, nh = C.page(HERE / 'caveats', title="The hedge read: what a reader doesn't need where it is", intro=hedge_intro)
    hedge = hedge.replace('## Looked at and kept', '## Taken up elsewhere (102.1, 102.2 or the reader\'s edit)')
    out = INTRO.replace('{ne}', str(ne)).replace('{nh}', str(nh)) + '\n' + numbered(edit, 'E') + '\n' + numbered(hedge, 'H')
    (HERE / 'IDEAS.md').write_text(out.rstrip() + '\n', encoding='utf-8')
    print('IDEAS.md:', ne, 'edit items,', nh, 'hedge items')


if __name__ == '__main__':
    main()
