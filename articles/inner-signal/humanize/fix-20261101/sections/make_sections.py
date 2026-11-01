"""The guide's sections, each to be checked in Pangram by itself (gate E307; Joel, 2026-11-01 18:57 UTC, on N-238 and
N-587: a whole-guide check hides a section that reads Mixed alone).

A section is a heading and its paragraphs, down to the next heading of level 1 or 2 (a level-3 or level-4 heading stays
inside its section, as in the Milton Model's ten patterns). A section under MIN words is joined to the next one in the
same top-level part (or to the one before, at the end of a part), since a short text gives Pangram too little to read
alone. The text is what a reader sees: each block's plain text (headings as lines, links as their words), one blank line
between blocks.

  python3 articles/inner-signal/humanize/fix-20261101/sections/make_sections.py
Writes SECTIONS.json (each section: key, name, blocks, words, sha256, text) and sNNN-items.json ([key, text, sha256]) for
the web app's helper (tools/humanization/pangram_page_helpers.js).
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
MIN = 120
BATCH = 's1101'


def words(bs):
    return sum(len(b['text'].split()) for b in bs)


def main():
    md = GUIDE.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    parts, cur = [], None
    for b in bl:
        if b['level'] == 1 or cur is None:
            cur = []
            parts.append(cur)
        cur.append(b)
    units = []
    for part in parts:
        secs, s = [], []
        for b in part:
            if b['level'] in (1, 2) and s and any(not x['level'] for x in s):
                secs.append(s)
                s = []
            s.append(b)
        secs.append(s)
        out = []
        for s in secs:
            if out and words(out[-1]) < MIN:
                out[-1] = out[-1] + s
            else:
                out.append(s)
        if len(out) > 1 and words(out[-1]) < MIN:
            last = out.pop()
            out[-1] = out[-1] + last
        units += out
    # a part too short alone joins the next part
    final = []
    for u in units:
        if final and words(final[-1]) < MIN:
            final[-1] = final[-1] + u
        else:
            final.append(u)
    if len(final) > 1 and words(final[-1]) < MIN:
        last = final.pop()
        final[-1] = final[-1] + last
    secs = []
    for k, u in enumerate(final, 1):
        text = '\n\n'.join(b['text'] for b in u)
        heads = [b['text'] for b in u if b['level'] in (1, 2)]
        secs.append({'key': '%s-%02d' % (BATCH, k), 'name': ' / '.join(heads) or '(opening)',
                     'blocks': [b['i'] for b in u], 'words': len(text.split()),
                     'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(), 'text': text})
    assert [i for s in secs for i in s['blocks']] == list(range(len(bl)))
    guide_sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    (HERE / 'SECTIONS.json').write_text(json.dumps({'guide_sha256': guide_sha, 'min_words': MIN, 'sections': secs},
                                                   ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / ('%s-items.json' % BATCH)).write_text(json.dumps([[s['key'], s['text'], s['sha256']] for s in secs],
                                                            ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(secs), 'sections,', sum(s['words'] for s in secs), 'words; guide', guide_sha[:8])
    for s in secs:
        print(s['key'], s['words'], s['name'][:90])


if __name__ == '__main__':
    main()
