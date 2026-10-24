"""CHANGED.json for the community article's first whole-article recheck (2026-10-24, after Joel's message of 23:40 UTC):
every paragraph of the draft that isn't in his post as published (his editor HTML of 2026-10-20), with my chance that it
reads red, and every new seam between two unchanged paragraphs (the move into essay and manual; paragraphs his cuts
removed). part_forecast.py adds each changed paragraph's neighbours itself.

The chances: Emulate's two passages from 59 and 62 (the freeloader sentence, the pointer to the manual), never checked in
Pangram, 0.15 each; his own 57 sentence 0.05; a paragraph his 64 or 65 cuts changed 0.03 (a cut changes where a window
falls: the Inner Child lane's E248, one cut in 26 made a paragraph read AI); a typo fix 0.01; the "(play + work)" gloss
0.02; a new seam 0.02. His post's sections read 100% Human one by one before it went up; this is their first check as
one article, in the new order.

  python3 articles/intentional-communities/candidate/joel-20261024/recheck/make_changed_ic.py   (after make_recheck_ic.py)
"""
import json, pathlib, re, sys

R = pathlib.Path(__file__).resolve().parent
CAND = R.parents[1]
REPO = R.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402
sys.path.insert(0, str(CAND / 'joel-20261023' / 'restructure'))
import make_working as MW  # noqa: E402  (the 57 to 63 changes, with their texts)

SRC = CAND / 'joel-20261020' / 'community-final-substack-20261020.html'
one = lambda s: re.sub(r' {2,}', ' ', s)


def main():
    draft = (R / 'DRAFT-TEXT.txt').read_text(encoding='utf-8')
    lines = draft.split('\n')
    src = [one(x) for x in C.checked_text(SRC.read_text(encoding='utf-8'), limit=10 ** 9).split('\n')]
    srcset = set(src)
    prev_in_src = {src[i]: (src[i - 1] if i else None) for i in range(len(src))}
    typo_fixed = {}
    for wrong, right in MW.TYPOS:
        for s in src:
            if wrong.replace('  ', ' ') in s:
                typo_fixed[s.replace(wrong.replace('  ', ' '), right)] = s
    emulate = [C.smart(MW.NEW_FREE.strip())[:60], C.smart(MW.POINTER)[:60]]
    out, kinds = [], {}
    for i, line in enumerate(lines):
        if not line.strip() or draft.count(line) != 1:
            continue
        if line in srcset:
            p = prev_in_src.get(line)
            if i and lines[i - 1] in srcset and p != lines[i - 1]:
                out.append({'name': 'seam %d: a new neighbour above it' % i, 'text': line, 'chance_red': 0.02,
                            'why': 'unchanged, but the paragraph before it is new to it (the move into essay and manual, or '
                                   'paragraphs cut between them)'})
                kinds['seam'] = kinds.get('seam', 0) + 1
            continue
        if any(e[:50] in line for e in emulate):
            k, ch, why = 'emulate', 0.15, "Emulate's wording of my draft (59 or 62), with the reader's fixes; never checked in Pangram"
        elif C.smart(MW.HIS_Q07)[:50] in line:
            k, ch, why = 'his 57', 0.05, 'his own words from his Q07 answer, after the medicine sentence'
        elif 'pl/ork (play + work)' in line:
            k, ch, why = 'gloss', 0.02, 'his own gloss of pl/ork, put where the word is now first met'
        elif line in typo_fixed:
            k, ch, why = 'typo', 0.01, 'a typo fixed (60 a)'
        else:
            k, ch, why = 'cut', 0.03, 'a paragraph his 64 or 65 cuts changed'
        kinds[k] = kinds.get(k, 0) + 1
        out.append({'name': '%s %d' % (k, i), 'text': line, 'chance_red': ch, 'why': why})
    (R / 'CHANGED.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (R / 'LAST-NONE.json').write_text('{"text": "", "windows": [], "why": "no whole-article check of this article yet"}\n',
                                      encoding='utf-8')
    print('%d parts in CHANGED.json: %s' % (len(out), kinds))


if __name__ == '__main__':
    main()
