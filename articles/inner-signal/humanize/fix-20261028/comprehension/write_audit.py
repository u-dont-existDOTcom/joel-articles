"""AUDIT.md: the comparative read's findings and my check of each (FINDINGS.json, CHECKED.json).

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/write_audit.py
"""
import collections
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import collect as c  # noqa: E402

REPO = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = REPO + 'articles/inner-signal/humanize/'
D = json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))
F = {r['id']: r for r in D['findings']}
V = json.loads((HERE / 'CHECKED.json').read_text(encoding='utf-8'))['verdicts']
CHUNKS = json.loads((HERE / 'CHUNKS.json').read_text(encoding='utf-8'))
LABEL = {'real': 'a real problem', 'done': 'a real problem (settled by his own version)', 'minor': 'a small snag',
         'his': 'in his own words (his call)', 'not': 'not a problem'}


def q(text):
    return '\n'.join('> ' + line if line.strip() else '>' for line in text.strip().splitlines())


def pct(a, b):
    return '%d%%' % round(100 * a / b) if b else '-'


def origin(f):
    o = F[f]['origin'] or {}
    d = o.get('date')
    if not d:
        return 'not traced'
    if o.get('subject') == 'as published':
        return 'as he published it'
    return '18 Oct (the overnight Emulate run)' if d == '2026-10-18' else \
        '20-23 Oct (installs of the induction section, the NLP appendix and his answers)' if d <= '2026-10-23' else \
        '25 Oct (the answers of his first marking page)'


def block(f):
    return (F[f]['now_blocks'] or [None])[0]


def main():
    paras = [b for b in c.NOW if not b['level']]
    real = [f for f, v in V.items() if v[0] in ('real', 'done')]
    minor = [f for f, v in V.items() if v[0] == 'minor']
    his = [f for f, v in V.items() if v[0] == 'his']
    nots = [f for f, v in V.items() if v[0] == 'not']
    rb = {block(f) for f in real} - {None}
    mb = {block(f) for f in minor} - {None} - rb
    sev = collections.Counter(V[f][1] for f in real)
    kinds = collections.Counter(F[f]['kind'] for f in real)
    seen = [f for f in real if F[f]['seen_25oct']]
    stood = [f for f in real if F[f]['let_stand_18oct']]
    out = ['# The hypnosis guide\'s comprehension audit (2026-10-28)', '',
           'Joel, 2026-10-28 15:20 UTC: "i started on it, but the guide itself is now too incomprehensible, we went wrong '
           'somewhere" ([his message](%sfix-20261028/joel-20261028-1520-message.txt)).' % LANE, '',
           'Fresh readers each had one part of the guide twice, as it was when he wrote (commit 0a44911d) and as he '
           'published it ([published](%ssource/published-20260928.md)), and went through the part sentence by sentence '
           'for every place it reads worse than his: **garbled** (doesn\'t parse, a word that doesn\'t fit), **unclear** '
           '(a reader has to reread or guess), **lost** (a point, step, condition or contrast he made is gone) or '
           '**vaguer**. Then I checked every finding against the whole guide and his own decisions: his terms (the Guide, '
           'guard), the cautions and repeats he cut on 25 October, the lines his newer inner child guide put in. Eleven '
           'parts of about 2,500 words; six were read again in halves when their first readers ran out of room '
           '([how the parts were made](%sfix-20261028/comprehension/make_chunks.py), '
           '[the halves](%sfix-20261028/comprehension/make_halves.py)).' % (LANE, LANE, LANE), '',
           '## The numbers', '',
           '- **%d findings** from the readers (%d at their severity 3, %d at 2, %d at 1).'
           % (len(V), *[collections.Counter(F[f]['severity'] for f in V)[s] for s in (3, 2, 1)]),
           '- **%d real problems** by my check, in **%d of the guide\'s %d paragraphs (%s)**: %d where a reader won\'t get '
           'it or it now says something else, %d where most readers would stumble. By kind: %s.'
           % (len(real), len(rb), len(paras), pct(len(rb), len(paras)), sev[3], sev[2],
              ', '.join('%s %d' % kv for kv in kinds.most_common())),
           '- **%d small snags** (a vaguer word, a lost nuance, an unclear "it") in %d more paragraphs (%s).'
           % (len(minor), len(mb), pct(len(mb), len(paras))),
           '- **%d in his own words**: his call, on the fix page as passages to keep or edit.' % len(his),
           '- **%d not problems** (%s of the findings): as clear as his, his own terms or decisions, or explained '
           'elsewhere in the guide.' % (len(nots), pct(len(nots), len(V))),
           '- **When the real problems came in** (the first version of the guide in Git with their words): ' +
           '; '.join('%s, %d' % kv for kv in collections.Counter(origin(f) for f in real).most_common()) + '.',
           '- **Seen before and left:** %d of the %d real problems had been flagged by the strict Emulate check\'s '
           'readers on 25 October, rated "small" and left; %d had been named by the 18 October second readers and let '
           'stand as wording or tone.' % (len(seen), len(real), len(stood)), '',
           '## By part', '', '| Part | From | To | Real | Snags | His | Not |', '|---|---|---|---|---|---|---|']
    for ch in CHUNKS:
        k = ch['chunk']
        cs = collections.Counter(V[f][0] for f in V if F[f]['chunk'] == k)
        out.append('| %d | %s | %s | %d | %d | %d | %d |' % (k, ch['first'] or '(start)', ch['last'],
                                                         cs['real'] + cs['done'], cs['minor'], cs['his'], cs['not']))
    for title, ids in (('The real problems', real), ('In his own words', his), ('The small snags', minor),
                       ('Not problems', nots)):
        out += ['', '## %s (%d)' % (title, len(ids)), '']
        for f in sorted(ids, key=lambda x: (block(x) if block(x) is not None else 10 ** 6, x)):
            r, v = F[f], V[f]
            out += ['**%s** · %s · %s · %s' % (f, r['kind'], '; '.join(r['where']) or '(place not found)', LABEL[v[0]]),
                    '', 'Now:', '', q(r['now']), '']
            if r['published'] and r['published'].lower() != 'none':
                out += ['Published:', '', q(r['published']), '']
            out += ['Reader: ' + r['why'], '', 'My check: ' + v[-1][:1].upper() + v[-1][1:], '']
            extra = [origin(f)]
            if r['seen_25oct']:
                extra.append('flagged on 25 Oct (%s, rated %s)' % (r['seen_25oct'][0]['id'], r['seen_25oct'][0]['severity']))
            out += ['_came in: %s_' % '; '.join(extra), '']
    (HERE / 'AUDIT.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('AUDIT.md: %d findings; real %d in %d paragraphs; snags %d in %d more; his %d; not %d'
          % (len(V), len(real), len(rb), len(minor), len(mb), len(his), len(nots)))


if __name__ == '__main__':
    main()
