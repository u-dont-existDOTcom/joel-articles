"""The mechanical net under the nonsense read: every token in the hypnosis guide that isn't a dictionary word, isn't in
his published guide of 28 September or his inner child guide, and isn't a name or a term the guide uses on purpose.
A model reads meaning ("oily" for "old" is a real word, which only a reader catches, BRIEF.md); this lists the non-words
(typos, letters dropped or added, words run together) for the lead session to read in place.

  python3 articles/inner-signal/humanize/fix-20261103/nonsense/nonwords.py
Writes NONWORDS.json and prints them with their block numbers.
"""
import collections
import json
import pathlib
import re
import sys

from spellchecker import SpellChecker

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

WORD = re.compile(r"[A-Za-z][A-Za-z'’]*[A-Za-z]|[A-Za-z]")


def words(text):
    return [w.replace('’', "'") for w in WORD.findall(text)]


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    his = (H / 'source' / 'published-20260928.md').read_text(encoding='utf-8') + '\n' + \
        (H / 'fix-20261025' / 'ic-align' / 'IC-GUIDE.txt').read_text(encoding='utf-8')
    known = {w.lower() for w in words(his)}
    sp = SpellChecker()
    hits = collections.defaultdict(list)
    for b in bl:
        for w in words(b['text']):
            lw = w.lower().strip("'")
            if len(lw) < 3 or lw in known:
                continue
            base = re.sub(r"'(s|t|re|ve|ll|d|m)$", '', lw)
            if sp.known([lw]) or sp.known([base]):
                continue
            if w[0].isupper() and not w.isupper() and b['text'].find(w) > 0:
                continue   # a name in mid-sentence
            hits[lw].append(b['i'])
    out = [{'word': w, 'blocks': sorted(set(v)), 'where': [sr.where(bl, i) for i in sorted(set(v))][:3],
            'suggest': sorted(sp.candidates(w) or [])[:5]} for w, v in sorted(hits.items())]
    (HERE / 'NONWORDS.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for x in out:
        print(x['word'], x['blocks'][:6], x['suggest'])
    print(len(out), 'non-words')


if __name__ == '__main__':
    main()
