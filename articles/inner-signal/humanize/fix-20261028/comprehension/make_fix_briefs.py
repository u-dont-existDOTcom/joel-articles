"""Fixes for the comprehension audit's findings (2026-10-28): one brief per part for a fresh writer, who makes each
flagged paragraph at least as clear as Joel's published version and gives back exact replacements.

Only findings I confirmed (CHECKED.json, verdict "real") go to the writers, and none in his own words: those are his to
rewrite on the marking page. Each brief has, for every paragraph with findings, the paragraph as it is now, the published
blocks the findings point at, the findings, and the paragraphs around it, so a fix fits where it stands.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/make_fix_briefs.py [PART ...]  -> fix/FIX-k.txt, fix/BRIEF-FIX-k.txt
"""
import collections
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

# the guide with his six answers of 2026-10-28 in (make_candidate.py --answers-only), so a fix is made on his new text
NOW = sr.blocks((HERE / 'BASE-ANSWERS.md').read_text(encoding='utf-8'))
PUB = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
OUT = HERE / 'fix'

BRIEF = '''You are fixing comprehension problems in part of a long self-hypnosis guide by Joel, a Substack writer. The guide
was rewritten so that an AI detector (Pangram) reads it as human-written, and in places the rewrite became garbled,
unclear, vaguer, or lost a point that Joel's published version made. Readers have found those places. Your job is to fix
each one so the paragraph is at least as clear as Joel's published version and says everything it said, while changing
as little as possible, because every changed word can make the detector read the paragraph as AI again.

The file `__FILE__` has, for each paragraph to fix:
- "P<n> NOW": the paragraph as it is in the guide now (the text you change);
- "PUBLISHED": the blocks of Joel's published guide the findings point at (what it should say, clearly);
- the findings: each with the words concerned, its kind (garbled, unclear, lost, vaguer; MINOR for a small snag),
  what the reader said, and what my check of it found (follow my check where the two differ);
- "BEFORE" and "AFTER": the paragraphs around it, for context only (don't change them).

How to fix:
1. Fix every finding listed for the paragraph. Change only the sentence(s) a finding names, plus a word or two around
   them if a sentence needs it to read well. Leave every other sentence exactly as it is, character for character.
2. The fixed sentence must be clear on a first read to someone who never saw the published version, and must say what
   the published version says there: every point, step, condition, contrast and strength of claim ("may" stays "may",
   "one thing ... another" keeps the point that they differ).
3. Prefer Joel's published wording when it fits the paragraph as it now stands: copy his sentence (or the part of it
   that's needed) exactly. When it doesn't fit (the paragraph now says things in another order, or his sentence would
   repeat something already said), write the fix in the paragraph's own voice: its contractions, plain everyday words,
   sentence lengths. Say plainly what he meant; don't polish, don't add an image or a flourish of your own.
4. Don't add anything the published version doesn't say: no new claims, examples, cautions or safety lines, no
   reassurance that isn't there. Don't fix things nobody flagged. Keep his casual grammar where it isn't a problem.
   Joel's terms stay as the guide now uses them: the inner adult's three jobs are the Nurturer, the Protector and the
   Guide (not "the Leader"), a protective part from childhood is a guard, and the inner child may be "your little one".
   Don't change a sentence just to use the published guide's older term.
5. A finding marked MINOR is a small snag: fix it only if a few words do it (up to about six changed); otherwise put
   it in "not_fixed" with the reason "minor".
6. A paragraph whose items run together without punctuation (a list whose line breaks were lost) is fixed by giving the
   items back as a list: in "with", put each item on its own line starting with "- ", and any lead-in sentence on its
   own line before them; keep the items' words.
7. Avoid these words unless the published text has them: boring, quietly, ordinary, truly, deeply, crucial, vital,
   navigate, journey, delve, "it's worth noting", "that's where X matters". Don't start a sentence with "And" or "But"
   more than the paragraph already does.
8. If a finding is wrong (the NOW text is as clear as the published one and keeps its point), don't fix it; say so.

Write your answer with a single Write call to `__OUT__`, as JSON in exactly this shape (no other text in the file):

{"part": __K__,
 "fixes": [{"p": <the paragraph's number n from "P<n> NOW">, "findings": ["F3.2", "F3.3"],
            "replace": "<exact words from that paragraph as it is NOW, copied character for character, occurring once in it>",
            "with": "<the fixed words>",
            "how": "published" or "rewrite",
            "note": "<a few words: what the fix restores or clears up>"}],
 "not_fixed": [{"finding": "F3.4", "why": "<why it needs no fix>"}]}

Several fixes may share a paragraph; their "replace" strings must not overlap. Keep each "replace" as short as the fix
allows (a sentence or two, not the whole paragraph). Every finding listed goes into exactly one fix's "findings" or into
"not_fixed". Read only the file named above, don't run commands, don't use the web. Reply with only the number of fixes.
'''


def para(i):
    b = NOW[i]
    return ('#' * b['level'] + ' ' + b['text']) if b['level'] else b['text']


def main():
    D = json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))
    C = json.loads((HERE / 'CHECKED.json').read_text(encoding='utf-8'))
    V = C['verdicts']
    F = [r for r in D['findings'] if V.get(r['id'], ['not'])[0] in ('real', 'minor') and r['now_blocks']]
    for r in F:
        r['minor'] = V[r['id']][0] == 'minor'
        r['my_note'] = V[r['id']][-1]
    OUT.mkdir(exist_ok=True)
    by_part = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in F:
        by_part[r['chunk']][r['now_blocks'][0]].append(r)
    meta = []
    only = [int(a) for a in sys.argv[1:]]   # parts to write (all if none given); briefs already answered stay as sent
    for k in sorted(by_part):
        if only and k not in only:
            continue
        lines = []
        for i in sorted(by_part[k]):
            rs = by_part[k][i]
            pub = sorted({j for r in rs for j in r['pub_blocks']})
            before = [j for j in range(i - 2, i) if j >= 0]
            after = [j for j in range(i + 1, i + 3) if j < len(NOW)]
            lines += ['=' * 70, 'P%d NOW (%s):' % (i, sr.where(NOW, i)), para(i), '',
                      'PUBLISHED:', '\n\n'.join(PUB[j]['text'] for j in pub) or '(none given)', '', 'FINDINGS:']
            for r in rs:
                lines += ['- %s (%s%s): "%s"' % (r['id'], r['kind'], ', MINOR' if r['minor'] else '', r['now'].strip()),
                          '  published: "%s"' % r['published'].strip(), '  reader: %s' % r['why'].strip(),
                          '  checked: %s' % r['my_note'].strip()]
            lines += ['', 'BEFORE (context only):'] + [para(j) for j in before]
            lines += ['', 'AFTER (context only):'] + [para(j) for j in after] + ['']
        f = OUT / ('FIX-%d.txt' % k)
        f.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        (OUT / ('BRIEF-FIX-%d.txt' % k)).write_text(
            BRIEF.replace('__FILE__', str(f)).replace('__OUT__', str(OUT / ('FIXES-%d.json' % k)))
            .replace('__K__', str(k)), encoding='utf-8')
        meta.append({'part': k, 'paragraphs': len(by_part[k]), 'findings': sum(len(v) for v in by_part[k].values())})
    old = json.loads((OUT / 'FIX-PARTS.json').read_text(encoding='utf-8')) if (OUT / 'FIX-PARTS.json').exists() else []
    meta = sorted([m for m in old if m['part'] not in {x['part'] for x in meta}] + meta, key=lambda m: m['part'])
    (OUT / 'FIX-PARTS.json').write_text(json.dumps(meta, indent=1) + '\n', encoding='utf-8')
    for m in meta:
        print(m)


if __name__ == '__main__':
    main()
