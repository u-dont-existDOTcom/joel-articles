"""The hypnosis guide's comprehension audit (2026-10-28): every part of the working copy beside the same part of Joel's
published guide, for fresh readers to find each place the working copy is harder to understand than what he published.

Joel, 2026-10-28 15:20 UTC: "the guide itself is now too incomprehensible, we went wrong somewhere", and on a card: "is
there more weird stuff in here that makes no sense like this? didn't you already do a comprehension check? ... is this
whole guide messed up now?". The clarity read of 2026-10-25 had readers flag what stood out in the guide alone, and it
missed "As associated with the Silva Mind Control method:"; its first run flagged the agreement list and the rerun dropped
it. This read is exhaustive and comparative instead: each reader gets a part of the guide as it is now (NOW) and the same
part as he published it (PUBLISHED), and goes through NOW sentence by sentence.

The parts follow the headings both versions share (127 of the published guide's 131 h1 and h2 headings are in the working
copy), about 2,500 words of NOW each.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/make_chunks.py   -> CHUNK-k.txt, BRIEF-k.txt, CHUNKS.json
"""
import difflib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

PUB = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
# the guide as it was when he wrote (2026-10-28 15:20 UTC), the version every reader read: commit 0a44911d, sha256
# c38ca36f..., before his six answers of that afternoon went in
AUDITED = subprocess.run(['git', 'show', '0a44911d:articles/inner-signal/humanize/HUMANIZED-SO-FAR.md'],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
NOW = sr.blocks(AUDITED)
TARGET = 2500

BRIEF = '''You are checking part of a long self-hypnosis guide by Joel, a Substack writer, for comprehension. You get the same
part in two versions:
- PUBLISHED: the guide as Joel published it (written with AI help, but clear);
- NOW: a rewrite made so that an AI detector reads it as human-written, which was meant to keep every point and stay
  clear.

Your job: find EVERY place where NOW is harder for a reader to understand than PUBLISHED, or doesn't make sense on its
own. Go through NOW paragraph by paragraph and sentence by sentence; don't skim. Content may have moved between sections
or been added; judge NOW as a reader would read it, and use PUBLISHED as the reference for what it should say.

Flag a sentence (or a few together) when it is one of these:
- garbled: ungrammatical, a fragment standing as a sentence, a word that doesn't fit, a sentence that doesn't parse, a
  list with no verb that doesn't say what it's for (for example "Apples, pears, plums. Can fruit be bought?" where the
  published text said "Apples are one thing. Pears are another." and the point was that they differ);
- unclear: a reader would have to reread it, or guess what it means or what "it", "this" or "that" refers to;
- lost: NOW drops or changes a point, a step, a condition or a contrast that PUBLISHED made, so the passage no longer says
  it (for example "one thing ... another" becoming a plain list loses the point that the things differ);
- vaguer: NOW says the same thing less exactly, in a way a reader would notice (a concrete step becomes general, a
  strong rule becomes a hint, or the reverse).

Don't flag: a plainer, more casual or more personal wording that is just as clear; a heading change; a change of order; a
typo that doesn't hide the meaning; new material in NOW that is clear. Don't rewrite anything.

Write your findings with a single Write call to `__OUT__`, in exactly this form, one block per finding, in NOW's order:

## F__K__.1
NOW: <the exact sentence(s) from NOW, copied character for character>
PUBLISHED: <the matching sentence(s) from PUBLISHED, copied exactly, or "none">
KIND: garbled | unclear | lost | vaguer
SEVERITY: 3 (a reader won't get it, or it now says something else) | 2 (most readers would stumble) | 1 (a small snag)
WHY: <one sentence>

(number them F__K__.1, F__K__.2, ...). After the last block add a line "TOTAL: n". Read only the file below, don't run
commands, don't use the web. Reply with only the TOTAL line.

The part to check is in `__CHUNK__`.
'''


def sections(bl):
    """[(heading text or None, level, [block indices])], split at h1 and h2 headings."""
    out, cur = [], [None, 0, []]
    for b in bl:
        if b['level'] and b['level'] <= 2:
            out.append(tuple(cur))
            cur = [b['text'], b['level'], [b['i']]]
        else:
            cur[2].append(b['i'])
    out.append(tuple(cur))
    return [s for s in out if s[2]]


def text_of(bl, idx):
    lines = []
    for i in idx:
        b = bl[i]
        if b['level']:
            lines.append('#' * b['level'] + ' ' + b['text'])
        elif b['text'].strip():
            lines.append(b['text'])
    return '\n\n'.join(lines)


def words(bl, idx):
    return sum(len(bl[i]['text'].split()) for i in idx if not bl[i]['level'])


def main():
    sp, sn = sections(PUB), sections(NOW)
    sm = difflib.SequenceMatcher(a=[s[0] for s in sp], b=[s[0] for s in sn], autojunk=False)
    # each NOW section's published counterpart: the same heading, or (for a heading the published guide lacks) the
    # published section of the last shared heading before it
    match = {}
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            match[blk.b + k] = blk.a + k
    chunks, cur, last_pub = [], {'now': [], 'pub': set()}, 0
    for j, s in enumerate(sn):
        if j in match:
            last_pub = match[j]
            cur['pub'].add(match[j])
        else:
            cur['pub'].add(last_pub)
        cur['now'].append(j)
        if sum(words(NOW, sn[x][2]) for x in cur['now']) >= TARGET:
            chunks.append(cur)
            cur = {'now': [], 'pub': set()}
    if cur['now']:
        chunks.append(cur)
    meta = []
    for k, c in enumerate(chunks, 1):
        now_idx = [i for j in c['now'] for i in sn[j][2]]
        pub_idx = [i for j in sorted(c['pub']) for i in sp[j][2]]
        body = ('=== PUBLISHED (as Joel published it) ===\n\n' + text_of(PUB, pub_idx) +
                '\n\n=== NOW (the rewrite to check) ===\n\n' + text_of(NOW, now_idx) + '\n')
        (HERE / ('CHUNK-%d.txt' % k)).write_text(body, encoding='utf-8')
        out = HERE / ('READER-%d.md' % k)
        (HERE / ('BRIEF-%d.txt' % k)).write_text(BRIEF.replace('__OUT__', str(out)).replace('__K__', str(k))
                                                .replace('__CHUNK__', str(HERE / ('CHUNK-%d.txt' % k))), encoding='utf-8')
        meta.append({'chunk': k, 'now_words': words(NOW, now_idx), 'pub_words': words(PUB, pub_idx),
                     'first': sn[c['now'][0]][0], 'last': sn[c['now'][-1]][0], 'now_blocks': [now_idx[0], now_idx[-1]]})
    (HERE / 'CHUNKS.json').write_text(json.dumps(meta, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for m in meta:
        print(m['chunk'], m['now_words'], m['pub_words'], '|', m['first'], '->', m['last'])


if __name__ == '__main__':
    main()
