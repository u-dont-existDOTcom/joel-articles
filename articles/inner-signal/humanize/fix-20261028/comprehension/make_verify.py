"""Fresh readers for the fixed paragraphs (2026-10-28): each fixed paragraph beside his published one, before it goes on
his page.

A writer's fix is checked by someone who didn't write it and didn't see the finding's discussion: the reader gets, for
each changed paragraph, his PUBLISHED blocks, the paragraph BEFORE the fix and AFTER it, and says whether AFTER reads at
least as clearly as PUBLISHED and says what it says; any new problem (garbled, unclear, lost, vaguer) in AFTER is written
down the way the audit's readers wrote theirs.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/make_verify.py   -> verify/PAIRS-k.txt, verify/BRIEF-k.txt
"""
import collections
import difflib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

OUT = HERE / 'verify'
PUB = sr.blocks((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
BASE = sr.blocks((HERE / 'BASE-ANSWERS.md').read_text(encoding='utf-8'))
PER = 12  # paragraphs per reader

BRIEF = '''You are checking fixes made to a long self-hypnosis guide by Joel, a Substack writer. The guide was rewritten so
that an AI detector reads it as human-written, and in places the rewrite became hard to understand. Each paragraph below
has been fixed. You get, for each one:
- PUBLISHED: Joel's own published version of that passage (clear, the reference for what it should say);
- BEFORE: the paragraph as it was in the rewrite;
- AFTER: the paragraph with the fix (only some words changed).

For each paragraph, read AFTER as a reader who never saw the other versions would, then compare. Answer:
- CLEAR: is AFTER clear on a first read? (yes / no)
- SAYS: does AFTER say what PUBLISHED says in the part that changed: every point, step, condition and contrast, with the
  same strength? (yes / no). Ignore points PUBLISHED makes that AFTER never touched, and points AFTER adds that are clear.
- BETTER: is AFTER easier to understand than BEFORE? (yes / same / worse)
- If any answer is no or worse, say exactly which words and why, in one sentence.

Don't flag: casual or personal wording that is clear; his terms (the Nurturer, the Protector and the Guide are the inner
adult's three jobs; a protective part from childhood is a guard); a point PUBLISHED makes that the fix didn't touch.

Write your answer with a single Write call to `__OUT__`, one block per paragraph, in this form:

## P<n>
CLEAR: yes|no
SAYS: yes|no
BETTER: yes|same|worse
PROBLEM: <one sentence, or "none">

Then a last line "DONE: <number of paragraphs>". Read only the file `__PAIRS__`; don't run commands or use the web. Reply
with only the DONE line.
'''


def main():
    ch = json.loads((HERE / 'CHANGES.json').read_text(encoding='utf-8'))
    F = {r['id']: r for r in json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']}
    by_block = collections.defaultdict(list)
    for c in ch['changes']:
        by_block[c['block']].append(c)
    # the two cards he approved today put Emulate's words in (HG-S11, HG-S12): they get the same read (gate E288)
    ans = json.loads((HERE / 'CHANGES-ANSWERS.json').read_text(encoding='utf-8'))
    approved = {}
    for c in ans['changes']:
        if c['how'].startswith('approved'):
            pubs = sorted(range(len(PUB)), key=lambda j: -difflib.SequenceMatcher(
                a=c['after'].lower(), b=PUB[j]['text'].lower(), autojunk=False).ratio())[:1]
            approved[c['block']] = {'before': c['before'], 'after': c['after'], 'pub': pubs, 'id': c['id']}
    blocks = sorted(set(by_block) | set(approved))
    OUT.mkdir(exist_ok=True)
    # readers already given paragraphs keep them; a paragraph whose AFTER text changed since (a fix redone) or that is
    # new goes to a new reader, numbered after the others
    old_meta = json.loads((OUT / 'VERIFY-PARTS.json').read_text(encoding='utf-8')) if (OUT / 'VERIFY-PARTS.json').exists() else []
    done = {}
    for m in old_meta:
        for i, t in zip(m['paragraphs'], m.get('after', [None] * len(m['paragraphs']))):
            done[i] = t
    def after_of(i):
        return approved[i]['after'] if i in approved else by_block[i][-1]['after']
    blocks = [i for i in blocks if done.get(i) != after_of(i)]
    meta = list(old_meta)
    start = max([m['reader'] for m in old_meta] or [0])
    for k in range(0, len(blocks), PER):
        group = blocks[k:k + PER]
        n = start + k // PER + 1
        lines = []
        for i in group:
            if i in approved:
                a = approved[i]
                pub, before, after = a['pub'], a['before'], a['after']
            else:
                cs = by_block[i]
                pub = sorted({j for c in cs for f in c['findings'] for j in F[f]['pub_blocks']})
                before, after = BASE[i]['text'], cs[-1]['after']
            lines += ['=' * 70, 'P%d (%s)' % (i, sr.where(BASE, i)), '',
                      'PUBLISHED:', '\n\n'.join(PUB[j]['text'] for j in pub) or '(none)', '',
                      'BEFORE:', before, '', 'AFTER:', after, '']
        f = OUT / ('PAIRS-%d.txt' % n)
        f.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        (OUT / ('BRIEF-%d.txt' % n)).write_text(BRIEF.replace('__OUT__', str(OUT / ('VERIFY-%d.md' % n)))
                                                .replace('__PAIRS__', str(f)), encoding='utf-8')
        meta.append({'reader': n, 'paragraphs': group, 'after': [after_of(i) for i in group]})
    (OUT / 'VERIFY-PARTS.json').write_text(json.dumps(meta, indent=1) + '\n', encoding='utf-8')
    print(len(blocks), 'new paragraphs for', len(meta) - len(old_meta), 'new readers;', len(meta), 'readers in all')


if __name__ == '__main__':
    main()
