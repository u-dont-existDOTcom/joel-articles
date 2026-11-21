"""Writes the section of RESULTS.md about his answer of 2026-11-21 13:04 UTC: why two serotonin headings sat in a row,
what changed, the picks read after it, and the fate of every heading the check or a reader flagged."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
M = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
SC = {r['reader']: r for r in json.load(open(os.path.join(HERE, 'SCORES.json'), encoding='utf-8'))['rows']}
NOW = json.load(open(os.path.join(HERE, 'NOW.json'), encoding='utf-8'))
ORDER = [e['id'] for e in NOW]
NAMES = ['PICK', 'PICK2', 'PICK3', 'PICK4', 'PICK5', 'PICK6']
LABEL = {'PICK': 'My pick (on the page he answered)', 'PICK2': 'Second', 'PICK3': 'Third', 'PICK4': 'Fourth',
         'PICK5': 'Fifth', 'PICK6': 'Sixth'}
P = {n: {e['id']: e for e in json.load(open(os.path.join(HERE, 'PROPOSAL-%s.json' % n), encoding='utf-8'))} for n in NAMES}
F6 = json.load(open(os.path.join(HERE, 'FATES-PICK6.json'), encoding='utf-8'))
F5 = json.load(open(os.path.join(HERE, 'FATES-PICK5.json'), encoding='utf-8'))


def two(n, k):
    return ', '.join(str(SC['%s-%d' % (n, i)][k]) for i in (1, 2))


out = ['## The two serotonin headings in a row (his answer, 2026-11-21 13:04 UTC)', '',
       'His message: "done. learn lessons. why would you put 2 serotonin syndrome headings in a row / continue".', '',
       '**Why it happened.** Fable named each heading to read on its own, so it turned his "Suspected Serotonin Syndrome '
       '(SS)" into "Serotonin Syndrome (SS)?" and his "Recognizing serotonin toxicity", the heading right under it, into '
       '"Is It Serotonin Toxicity?": the same question twice. My pick took both from Fable. Nothing compared a heading '
       'with the one it sits under or the one before it; the readers were only asked where they would look, and their '
       'scores came out fine, because a reader who opens either heading lands in the right place. When readers '
       'mentioned the pair in their replies, I didn\'t act on it.', '',
       '**What changed** (lessons bad-trips-2026-11-21a to c, [the lesson file](%sdocs/lessons/2026-11-21-1304-bad-trips.md)):' % M,
       '',
       '- [The headings brief](%stools/humanization/headings_brief.md) has rule 11: no two headings in a row say or ask '
       'the same thing; a parent names the topic and its children name their parts.' % M,
       '- [toc_check.py](%stools/humanization/toc_check.py) lists every heading that shares a word with the one it sits '
       'under or the one before it, and every heading a reader marked hard, and fails until each one is changed or kept '
       'with the reason it stays.' % M,
       '- Readers now end with a "HARD:" line for each of the three hardest headings and for each pair that says the '
       'same thing, and a changed heading is read again by fresh readers before it goes to him.',
       '- His round 47 picks never reached me: the page had no database when he answered, so they were kept only in '
       'the browser he used. The page now sends them when it opens there, and it saves the headings themselves, not '
       'only which column he clicked, so they still read right if the columns change.', '',
       '**The picks read after his answer.** Each one was read by two fresh readers; the serotonin pair went in the '
       'second.', '',
       '| Contents | What changed from the one before | First pick right (of 32) | Guesses | Right by the 2nd pick |',
       '|---|---|---|---|---|']
prev = None
for n in NAMES:
    if prev is None:
        what = 'as on the page'
    else:
        what = '; '.join('"%s" → "%s"' % (P[prev][i]['heading'], P[n][i]['heading'])
                         for i in ORDER if P[prev][i]['heading'] != P[n][i]['heading'])
    out.append('| %s | %s | %s | %s | %s |' % (LABEL[n], what.replace('|', '/'), two(n, 'first_right'),
                                                 two(n, 'guesses'), two(n, 'right_by_second')))
    prev = n
out += ['', 'The serotonin part in the sixth: "Serotonin Syndrome (SS)?", then "How to Recognize It" and "What to Do '
        'Right Away" under it.', '',
        '**Every heading the check or a reader flagged in the sixth pick, and its fate:**', '',
        '| Heading | Why it was flagged | Fate |', '|---|---|---|']
WHY = {'repeat': 'shares a word with the heading above it or before it', 'hard': 'a reader marked it hard'}
for k, f in F6.items():
    kind, i = k.split(':', 1)
    if i not in P['PICK6']:
        continue
    out.append('| %s | %s | %s |' % (P['PICK6'][i]['heading'].replace('|', '/'), WHY[kind], f.replace('|', '/')))
out += ['', 'In the fifth pick both readers couldn\'t tell what "Beyond Rescue Medicine" covered: %s.' %
        F5['hard:R32-SEIZE'].split(': ', 1)[1], '',
        '**Next, when his picks arrive** ([read_answers.py](read_answers.py)): his headings are worked out again from '
        'his picks with the columns he saw and compared with what the page saved; his contents gets the same check '
        '(the serotonin pair is fixed whichever way he picked it, from the headings read above) and two fresh readers; '
        'then the headings go into the guide with their evidence tag lines.', '']
print('\n'.join(out))
