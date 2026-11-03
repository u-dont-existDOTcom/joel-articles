"""FINDINGS.md: my full read's 122 findings as a page Joel can read (he can't read JSON: gates E280 to E282), each with
where it is, the words, his published words, what was wrong, and what became of it.

  python3 articles/inner-signal/humanize/fix-20261030/fullread/make_findings_md.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
KIND = {'garbled': 'garbled', 'lost': 'a point lost', 'unclear': 'unclear', 'vaguer': 'vaguer than yours'}
FATE = {'fixed': 'Fixed', 'his': 'Yours', 'not': 'Not a problem', 'kept': 'Kept', 'done': 'Done'}
TO_YOU = [(r'\bHe approved\b', 'You approved'), (r'\bhe approved\b', 'you approved'), (r'\bHis\b', 'Your'),
          (r'\bhis\b', 'your'), (r'\bhe asked\b', 'you asked'), (r'\bhe named\b', 'you named'),
          (r'\bhe replaced\b', 'you replaced'), (r'\bhim\b', 'you')]


def to_you(t):
    for a, b in TO_YOU:
        t = re.sub(a, b, t)
    return t


def main():
    F = json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']
    D = json.loads((HERE / 'DISPOSITIONS.json').read_text(encoding='utf-8'))
    counts = {}
    for f in F:
        counts[D[f['id']][0]] = counts.get(D[f['id']][0], 0) + 1
    out = ['# My read of the whole guide beside your published version (2026-10-30)', '',
           'I read all 21 parts of the guide myself, each sentence beside your published one, after your answers of 14:35 '
           'UTC. These are the %d places where the guide read worse than yours: %d fixed in our words, %d yours (the '
           'suggestions are on your next cards page), %d not a problem once checked. Each fixed paragraph, before and '
           'after, beside yours: [VERIFY-PAIRS.md](VERIFY-PAIRS.md).' % (len(F), counts.get('fixed', 0),
                                                                        counts.get('his', 0), counts.get('not', 0)), '']
    part = None
    for f in F:
        if f['part'] != part:
            part = f['part']
            out += ['## Part %d' % part, '']
        fate, why = D[f['id']][0], D[f['id']][1]
        out.append('**%s** (%s, %s%s). %s' % (f['id'], '; '.join(f.get('where') or []), KIND.get(f['kind'], f['kind']),
                                              ', serious' if f['severity'] >= 2 else '', f['why']))
        out.append('')
        out.append('> Guide: %s' % f['now'])
        if f.get('published') and f['published'].strip().lower() != 'none':
            out.append('>')
            out.append('> Yours: %s' % f['published'])
        out.append('')
        out.append('%s.%s' % (FATE.get(fate, fate), '' if fate == 'fixed' else ' ' + to_you(why)))
        out.append('')
    (HERE / 'FINDINGS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(len(F), 'findings')


if __name__ == '__main__':
    main()
