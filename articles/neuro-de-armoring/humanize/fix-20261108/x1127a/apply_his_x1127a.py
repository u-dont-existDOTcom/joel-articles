#!/usr/bin/env python3
"""Put his versions on cards W-LMA-73A and W-COG-SEC into HUMANIZED-SO-FAR.md, as he checked them (his answers, exported
2026-11-27 19:16 UTC: ANSWERS-X1127A-20261127-1916.json; his checks read back from his history: HIS-CHECKS-X1127A.json,
each Human Written, one window, High).

- W-LMA-73A: his herbs warning, with "we know about this phenomenon already from SSRIs and finasteride users" where my
  try said "it's the same kind of thing SSRIs and finasteride can do" (his comment: "the issue was lack of clarity").
- W-COG-SEC: his Cognitive Warning and the paragraph after it, as he checked them in four steps; the two links Pangram
  can't see go back where they were ([*Mindwise*] and ["Metabolic Red Line"]).

His versions don't go through apply_gate.py (they are his); each text is asserted to be the one he checked, by SHA-256.
Two of his words go on the keep-as-is list: "Post-ashwa" (his clipped name: "post-ashwa is a human tell bc ai doesn't
tend to reduce the full name") and "nonsensical" ("one word to clarify fixes it all").

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127a/apply_his_x1127a.py [--write]
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = HERE.parents[4]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
KEEP = H / 'KEEP-AS-IS.json'
KEYS = H / 'FIDELITY-KEYS.json'
REC = HERE / 'APPLIED-X1127A.json'
ANSWERS = HERE / 'ANSWERS-X1127A-20261127-1916.json'
CHECKS = json.loads((HERE / 'HIS-CHECKS-X1127A.json').read_text(encoding='utf-8'))['checks']
CARDS = {i['id']: i for i in json.loads(ANSWERS.read_text(encoding='utf-8'))['items']}

MINDWISE = 'https://www.amazon.com/Mindwise-Misunderstand-Others-Think-Believe/dp/030774356X'
RED_LINE = 'https://ibogaqueen.substack.com/i/181671197/a-the-metabolic-red-line'

OLD_LMA = ("I'm not advising lion's mane or ashwagandha, even though they're popular herbs for focus and stress, because "
           "some people report anhedonia (no desire) and sexual dysfunction long after they stop taking them. Post-ashwa "
           "and post-lion's mane syndrome are rare, but it's the same kind of thing SSRIs and finasteride can do, so it's "
           "something to keep in mind.")
OLD_COG = ('As you de-armor, you will feel naked and exposed. You will assume everyone can see your anxiety, which they '
           'mostly can\'t. Nicholas Epley, [*Mindwise*](' + MINDWISE + '), calls this the "Illusion of Transparency."\n\n'
           'Your armored brain also projects the threat it feels onto neutral faces, so you will think people are judging '
           'you when they\'re mostly just thinking about themselves. So during this protocol, do not trust your social '
           'intuition: assume you are misreading every room, at least until your heart rate is back down to your usual '
           'resting rate, and under 90 BPM, since a racing heart means your reasoning brain is offline (see the '
           '["Metabolic Red Line"](' + RED_LINE + ') below).')


def his(card, link_id):
    """His version on CARD, asserted to be the text of his check LINK_ID (its SHA-256 as Pangram stored it)."""
    v = CARDS[card]['your_version']
    (c,) = [c for c in CHECKS if link_id in c['link']]
    assert hashlib.sha256(v.encode('utf-8')).hexdigest() == c['sha256'], card
    assert c['windows'] == [c['windows'][0]] and c['windows'][0][:2] == ['Human', 'High'], card
    return v, c['link']


LMA, LMA_CHECK = his('W-LMA-73A', 'ea117cc8')
COG_PLAIN, COG_CHECK = his('W-COG-SEC', 'c642954e')
COG = (COG_PLAIN.replace('Nicholas Epley, Mindwise, calls', 'Nicholas Epley, [*Mindwise*](' + MINDWISE + '), calls', 1)
       .replace('(see the "Metabolic Red Line" below)', '(see the ["Metabolic Red Line"](' + RED_LINE + ') below)', 1))
assert COG.count('](') == 2

KEEP_NEW = [
    {'id': 'K7', 'kind': 'coinage', 'quote': 'Post-ashwa',
     'what': 'his clipped name for post-ashwagandha syndrome; it looks like something to spell out, and it is one of the '
             'things that makes the herbs warning read human: a model writes the full name',
     'joel': "post-ashwa is a human tell bc ai doesn't tend to reduce the full name",
     'when': '2026-11-27 19:16 UTC', 'where': 'card W-LMA-73A, his comment (fix-20261108/x1127a/ANSWERS-X1127A-20261127-1916.json)',
     'basis': 'his answer'},
    {'id': 'K8', 'kind': 'choice', 'quote': 'you project the nonsensical threat you feel onto others',
     'what': 'his one clarifying word: the threat a de-armoring reader projects isn\'t real, so others aren\'t the danger; '
             'a pass that trims adjectives would cut "nonsensical", and the person (not the brain) does the projecting',
     'joel': 'and now one word to clarify fixes it all',
     'when': '2026-11-27 19:16 UTC', 'where': 'card W-COG-SEC, his comment (fix-20261108/x1127a/ANSWERS-X1127A-20261127-1916.json)',
     'basis': 'his answer'},
]

OWNER_CHANGES = [
    {'by': 'card W-LMA-73A, his version (fix-20261108/x1127a/ANSWERS-X1127A-20261127-1916.json), applied by '
           'fix-20261108/x1127a/apply_his_x1127a.py',
     'why': 'his herbs warning with 73a: "(no desire)" becomes "(no joy or desire)"; "it\'s the same kind of thing SSRIs '
            'and finasteride can do, so it\'s something to keep in mind" becomes "we know about this phenomenon already '
            'from SSRIs and finasteride users, so if you\'re already on either herb, I\'d quit it as soon as you notice any '
            'of that". His check: ' + LMA_CHECK + ' (Human Written, one window, High, 79 words).',
     'numbers_lost': [], 'numbers_new': [], 'keys_lost': {}},
    {'by': 'card W-COG-SEC, his version (fix-20261108/x1127a/ANSWERS-X1127A-20261127-1916.json), applied by '
           'fix-20261108/x1127a/apply_his_x1127a.py',
     'why': 'his Cognitive Warning and the paragraph after it: the first two sentences joined; "Your armored brain also '
            'projects the threat it feels onto neutral faces, so you will think people are judging you when ..." becomes '
            '"On top of that, you\'ll tend to think people are judging you, when really they\'re mostly just thinking about '
            'themselves. That\'s because when your brain is armored up, you project the nonsensical threat you feel onto '
            'others."; the heart-rate test, the 90 BPM and both links stay. His check: ' + COG_CHECK + ' (Human Written, '
            'one window, High, 123 words).',
     'numbers_lost': [], 'numbers_new': [], 'keys_lost': {}},
]


def main(write):
    text = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode('utf-8')).hexdigest()
    for key, old, new in (('W-LMA-73A', OLD_LMA, LMA), ('W-COG-SEC', OLD_COG, COG)):
        assert text.count(old) == 1, key
        text = text.replace(old, new, 1)
    after = hashlib.sha256(text.encode('utf-8')).hexdigest()
    print(before[:8], '->', after[:8])
    if not write:
        tmp = pathlib.Path('/tmp/apply_his_x1127a.md')
        tmp.write_text(text, encoding='utf-8')
        subprocess.run([sys.executable, str(ROOT / 'tools/humanization/fidelity_keys.py'), 'check', str(KEYS), str(tmp)])
        return
    ARTICLE.write_text(text, encoding='utf-8')
    keep = json.loads(KEEP.read_text(encoding='utf-8'))
    have = {k['id'] for k in keep['keep']}
    keep['keep'] += [k for k in KEEP_NEW if k['id'] not in have]
    KEEP.write_text(json.dumps(keep, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    keys = json.loads(KEYS.read_text(encoding='utf-8'))
    seen = {c['by'] for c in keys['owner_changes']}
    keys['owner_changes'] += [c for c in OWNER_CHANGES if c['by'] not in seen]
    KEYS.write_text(json.dumps(keys, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    rec = json.loads(REC.read_text(encoding='utf-8'))
    rec['runs'].append({'applied': [
        {'key': 'W-LMA-73A', 'whose': 'his version on the card, as he checked it', 'check': 'his check: ' + LMA_CHECK +
         ' (Human Written, one window, High, 79 words)', 'old': OLD_LMA, 'new': LMA},
        {'key': 'W-COG-SEC', 'whose': 'his version on the card, as he checked it, with the two links Pangram can\'t see put '
         'back', 'check': 'his checks, four steps: ' + ', '.join(c['link'] for c in CHECKS if c['card'] == 'W-COG-SEC') +
         ' (the last Human Written, one window, High, 123 words)', 'old': OLD_COG, 'new': COG}],
        'answers': 'x1127a/ANSWERS-X1127A-20261127-1916.json', 'his_checks': 'x1127a/HIS-CHECKS-X1127A.json',
        'before_sha256': before, 'after_sha256': after})
    REC.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('written', after[:8])


if __name__ == '__main__':
    main('--write' in sys.argv)
