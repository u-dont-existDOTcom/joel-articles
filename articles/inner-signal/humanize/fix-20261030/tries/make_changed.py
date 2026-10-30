"""CHANGED-A.json and CHANGED-B.json for the next recheck (part_forecast.py make), written before the paste.

The last check is the recheck of 30 October (../recheck/read/RESULT-A.json and RESULT-B.json, of
../recheck/CANDIDATE-MASTER.md). What changed since is TRIES.json, eleven paragraphs. My chance that each reads red, by
one stated rule:
- a take-back (the sentence my full read restored comes out, and the paragraph goes back to words that read High on 29
  October): 0.15;
- a new try in our words where the last check read AI: 0.4 (his shape rules, E303, are new to my tries; batch 483's
  writers with the earlier rules got 2 of 11 of the hardest stretches Human); where it read Human Low: 0.2;
- a suggestion for his words: 0.35, as last time.
And the words nobody changed that read AI last time (the double binds, the weekend line, his embedded-invitations
paragraph, the smaller-scale line): 0.4 each, below last time's 0.6, because each read High or Medium on 29 October with
the same words and the restored sentences next to them are what come out or change now (E302). part_forecast.py adds the
neighbours and the windows that read Human at Low last time.

  python3 articles/inner-signal/humanize/fix-20261030/tries/make_changed.py
"""
import json
import pathlib

X = pathlib.Path(__file__).resolve().parent
LAST = X.parent / 'recheck' / 'read'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})


def find(text, s):
    ft, fs = text.translate(FLAT), s.translate(FLAT).strip()
    for probe in (fs, fs[:120]):
        if probe and ft.count(probe) == 1:
            k = ft.find(probe)
            return k, k + len(fs if probe is fs else probe)
    return None


def chance(t):
    if t['kind'] == 'take back':
        return 0.15
    if t['kind'] == 'suggestion':
        return 0.35
    return 0.4 if t['read'].startswith('AI') else 0.2


def main():
    tries = json.loads((X / 'TRIES.json').read_text(encoding='utf-8'))['tries']
    for part in ('A', 'B'):
        text = (X / ('TEXT-%s.txt' % part)).read_text(encoding='utf-8')
        result = json.loads((LAST / ('RESULT-%s.json' % part)).read_text(encoding='utf-8'))
        out, taken = [], []
        for t in tries:
            loc = find(text, t['after'])
            if not loc:
                continue
            out.append({'name': '%s (%s)' % (t['id'], t['kind']), 'text': text[loc[0]:loc[1]], 'chance_red': chance(t),
                        'chance_high': 0.3 if t['kind'] == 'take back' else 0.2,
                        'why': '%s; read %s last time' % (t['whose'], t['read']), 'kind': 'changed'})
            taken.append(loc)
        for w in result['windows']:
            if not str(w['label']).startswith('AI'):
                continue
            seg = result['text'][w['start_index']:w['end_index']].strip()
            loc = find(text, seg)
            if not loc or any(a < loc[1] and b > loc[0] for a, b in taken):
                continue
            taken.append(loc)
            out.append({'name': 'kept red: ' + seg[:44].rstrip() + '...', 'text': text[loc[0]:loc[1]], 'chance_red': 0.4,
                        'chance_high': 0.1, 'why': 'unchanged; read %s (%s) last time, High or Medium on 29 October' % (
                            w['label'], w.get('confidence')), 'kind': 'changed'})
        (X / ('CHANGED-%s.json' % part)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(part, len(out), 'parts', round(sum(c['chance_red'] for c in out), 2), 'expected red among them')


if __name__ == '__main__':
    main()
