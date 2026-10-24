#!/usr/bin/env python3
"""Turn 104: Joel's answers of 2026-10-23 23:21 UTC (experiments/t104-answers/JOEL-20261023-2321.md).

- 100.1 A, with his own text ("i fixed it, this passes"): The Inner Guide's naming aside moves to its own short
  paragraph after P1 (GPT's move; it read 100% Human there, check t103c_ig_opening_aside), and the last h2 becomes his:
  the heading "You Belong Everywhere and Nowhere", then P9 and P10 word for word, in his characters. His P9 and P10 are
  the texts of check t103f_ig_belonging_s06 (P9's first sentence from draft s06, P10 from draft s05); his heading is the
  fix, since the old one said P9's first sentence again.
- 100.2 A: P2's two comfort sentences become "Treats and pampering ..." (ST-CA's meaning, section 17.1.4).
Each changed paragraph gets a note above it. The script asserts every old text occurs once, so it can't run twice.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SRC = 'experiments/t104-answers/JOEL-20261023-2321.md'

ASIDE = ('By the way, this job doesn\'t have to be called the Guide. The Wise One works, or your Inner Teacher, and "Guru" '
         'does for some people.')
OLD_HEAD = '## A Belonging Deeper Than Any Group'
HIS_HEAD = '## You Belong Everywhere and Nowhere'
HIS_P9 = ('The Guide also points beyond itself, toward somewhere you belong that doesn’t ask you to give up being yourself. '
          'That might be nature, or existence itself. It might be whatever your tradition sees as ultimate. Love can come from '
          'any of these places, and you also belong there, which is a little different. Maybe you’ve felt that outside '
          'somewhere, like you didn’t need anybody’s okay to be there. The way in is time in nature and contemplative '
          'practice, like meditation.')
HIS_P10 = ('With that under you, belonging with people can get a lot less desperate. Not all at once, though. Your little one '
           'might still think, “If they stop liking me, I won’t belong anywhere,” and the Guide can remind it '
           'there’s more to belong to than them.')
OLD_COMFORT = ('Comfort does better at set times, where it can\'t get out of hand. It shouldn\'t get canceled as a punishment after '
               'a bad day, either (ST-CA, section 17.1.4).')
NEW_COMFORT = ('Treats and pampering do better at set times, where they can\'t get out of hand. They shouldn\'t get canceled as a '
               'punishment after a bad day, either (ST-CA, section 17.1.4).')


def note(what):
    return '<!-- Turn 104 (his answers of 2026-10-23 23:21 UTC, ' + SRC + '): ' + what + ' -->'


def para_index(lines, start):
    hits = [k for k, l in enumerate(lines) if l.startswith(start)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


def main():
    lines = ART.read_text(encoding='utf-8').split('\n')
    # 100.2 A
    k = para_index(lines, "Maybe you've let a small child win at Go Fish")
    assert lines[k].count(OLD_COMFORT) == 1
    lines[k] = lines[k].replace(OLD_COMFORT, NEW_COMFORT, 1)
    lines[k:k] = [note('100.2 A: "Comfort does better at set times, where it can\'t get out of hand. It shouldn\'t get canceled ..." '
                       'became "Treats and pampering do better at set times, where they can\'t get out of hand. They shouldn\'t get '
                       'canceled ...", since "comfort" could read as rationing affection (GPT, 99) and the book meant treats and '
                       'pampering (ST-CA, section 17.1.4; experiments/t84-books/CANDIDATES-stca.md, candidate 11).'), '']
    # 100.1 A: P10 first (it holds the aside), then P9, the heading, and the aside after P1
    k = para_index(lines, 'With that under you, belonging with people can get a lot less desperate.')
    assert lines[k].endswith(ASIDE), lines[k][-160:]
    lines[k] = HIS_P10
    lines[k:k] = [note('100.1 A: his P10, word for word ("i fixed it, this passes"); the naming aside that ended it is now '
                       'its own paragraph after P1 (GPT\'s move).'), '']
    k = para_index(lines, 'The Guide also points beyond itself,')
    lines[k] = HIS_P9
    lines[k:k] = [note('100.1 A: his P9, word for word; its first sentence is draft s06\'s, so it no longer says the heading\'s '
                       'words again.'), '']
    k = lines.index(OLD_HEAD)
    assert lines.count(OLD_HEAD) == 1
    lines[k] = HIS_HEAD
    lines[k + 1:k + 1] = ['', note('100.1 A: his heading, in place of "A Belonging Deeper Than Any Group" (99 A), which P9\'s '
                                   'first sentence said again (checks t103d and t103f, 27% and 25% AI on the heading and that '
                                   'sentence).')]
    k = para_index(lines, 'As the Guide, you choose what your little one learns')
    lines[k + 1:k + 1] = ['', note('100.1 A: the naming aside, moved here from the end of P10 (GPT\'s move, his "agree with '
                                   'gpt" and "100.1a"; check t103c_ig_opening_aside, 100% Human with P1).'), '', ASIDE]
    text = '\n'.join(lines)
    assert text.count(ASIDE) == 1 and text.count(HIS_HEAD) == 1
    ART.write_text(text, encoding='utf-8')
    print('applied: 100.1 A (aside, heading, P9, P10) and 100.2 A')


if __name__ == '__main__':
    main()
