"""Batch n7 (Nibbāna): Emulate's round 5 for recheck 7's red, spliced sentence by sentence (2026-10-23, Joel's message of
23:28 UTC gave recheck 7's link).

The red (../recheck7/SCORE.md; feed 31fd6bda, Human Written, 0.39% AI, 2 of 114 windows AI): windows 67 (Low) and 68
(Medium), the first two sentences of his published paragraph "Part of the problem is that the Buddha, or those who recorded
him, left the pieces in different drawers. Ud 1.10 points to ... like Jenga." (light green, Low, in recheck 6; the first
sentence read AI, Low, on 2026-10-20). All four of batch n6's splices read Human.

Emulate ran on the whole paragraph (E235, E244), three samples (cd, ce, cf; BUNDLE5.json). Only the two red sentences go
back, from sample cf, which keeps their meaning best (with the reader's two fixes, the second in sample ce's words): cd adds that the Buddha "knew where all these pieces fit together" and
turns Jenga into "two jenga towers"; ce folds the paragraph's Advaita sentence into the reeds and loses "the gateway". Every
change I made to Emulate's words is in "mine" with its reason. The rest of the paragraph stays his.

  python3 articles/nibbana/humanize/fix-20261023/n7/emulate_n7.py --prompt   writes REVIEW-PROMPT.txt for a fresh reader
  (install_n1.py calls apply() after batch n6)
"""
import argparse, json, pathlib, sys

N7 = pathlib.Path(__file__).resolve().parent
ROOT = N7.parents[4]
sys.path.insert(0, str(N7.parent / 'n6'))
import emulate_n6 as E6  # noqa: E402  (the paragraph and inline-markup helpers)


def sample(run, key):
    return (N7 / run / (key + '.out.txt')).read_text(encoding='utf-8').strip()


SPLICES = {
    'n7-drawers': dict(
        first='Part of the problem is that the Buddha', run='cf', key='NB-drawers',
        old='Part of the problem is that the Buddha, or those who recorded him, left the pieces in different drawers. Ud 1.10 '
            'points to direct sensations as the gateway; SN 12.44 gives the contact chain building “the world”; SN 12.67 has '
            'consciousness and mind-and-body leaning together like two bundles of reeds – pull either away and the other '
            'falls, like Jenga.',
        take=('Yes, I think part of the problem', 'in SN 12.67.'),
        mine=[('Yes, I think part of the problem', 'Part of the problem',
               '"Yes," answers nothing (the paragraph before ends on a statement, DN 16); and the reader (REVIEW.md): '
               '"I think" made his flat claim less certain'),
              ('he talks about the importance of direct sensations in Ud 1.10',
               'he talks about direct sensations as the gateway in Ud 1.10',
               'his point is that Ud 1.10 makes direct sensations the gateway; "the importance of" lost it'),
              ('consciousness and mind/body', 'consciousness and mind-and-body', 'the article\'s own term (E246)'),
              ('lean against each other (Jenga!)', 'lean against each other (remove one and the other falls down, Jenga!)',
               'the reader (REVIEW.md): "pull either away and the other falls", the sutta\'s point, was lost; back in '
               'sample ce\'s own words')],
        windows='67 (Low) and 68 (Medium) in recheck 7; window 69 of recheck 6 (Human, Low); the first sentence AI, Low, '
                'on 2026-10-20'),
}


def new_text(s):
    out = sample(s['run'], s['key'])
    a, b = s['take']
    i = out.index(a)
    out = out[i:out.index(b, i) + len(b)]
    for x, y, _why in s['mine']:
        assert out.count(x) == 1, (x, out)
        out = out.replace(x, y)
    return out


def apply(work):
    recs = []
    for key, s in SPLICES.items():
        a, b = E6.para_bounds(work, s['first'])
        p = E6._Inline(work[a:b])
        old = s['old']
        if p.text.count(old) != 1:  # the editor's straight apostrophes
            old = old.replace('’', "'")
        new = new_text(s)
        dropped = p.replace(old, new)
        work = work[:a] + p.html() + work[b:]
        recs.append({'key': key, 'old': s['old'], 'new': new, 'windows': s['windows'],
                     'source': 'Emulate sample %s (%s)' % (s['run'], s['key']),
                     'mine': [{'replace': x, 'with': y, 'why': w} for x, y, w in s['mine']],
                     'markup_dropped': dropped, 'check': None, 'try': None,
                     'result': 'read in place in the next recheck (recheck 8)',
                     'review': 'fix-20261023/n7/REVIEW.md', 'triage': 'fix-20261023/n7/TRIAGE.json'})
    (N7 / 'EDITS-n7.json').write_text(json.dumps(recs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return work, recs


def prompt(text_before):
    lines = [l for l in text_before.split('\n') if l.strip()]
    done = text_before
    for s in SPLICES.values():
        done = done.replace(s['old'], new_text(s))
    dlines = [l for l in done.split('\n') if l.strip()]
    items = []
    for n, (key, s) in enumerate(SPLICES.items(), 1):
        _b, para, _a = E6.context(lines, s['old'])
        before, now_para, after = E6.context(dlines, new_text(s))
        items.append('## Item %d (a paragraph on why the suttas never give one clear account of nibbāna)\n\nBEFORE:\n%s\n\n'
                     'PARAGRAPH WITH WAS:\n%s\n\nWAS:\n%s\n\nNOW:\n%s\n\nPARAGRAPH WITH NOW:\n%s\n\nAFTER:\n%s\n'
                     % (n, before, para, s['old'], new_text(s), now_para, after))
    return E6.PROMPT.format(n=len(SPLICES), report=(N7 / 'REVIEW.md').resolve(), items='\n'.join(items)).replace(
        'You check 1 rewritten passages', 'You check 1 rewritten passage')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--prompt', action='store_true')
    a = ap.parse_args(argv)
    if a.prompt:
        text = (N7.parent / 'recheck7' / 'DRAFT-TEXT.txt').read_text(encoding='utf-8')
        (N7 / 'REVIEW-PROMPT.txt').write_text(prompt(text), encoding='utf-8')
        print('REVIEW-PROMPT.txt written')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
