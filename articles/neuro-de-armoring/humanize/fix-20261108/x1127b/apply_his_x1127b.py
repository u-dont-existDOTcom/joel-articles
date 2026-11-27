#!/usr/bin/env python3
"""Put his versions on cards W-SW19 and W-SW23 into HUMANIZED-SO-FAR.md, as he checked them (his answers, exported
2026-11-27 22:59 UTC: ANSWERS-X1127B-20261127-2259.json; his checks read back from his history: HIS-CHECKS-X1127B.json).

- W-SW19, the one-sixteenth paragraph: his version of my step 7 (#321), with "people you're close to and who you hang
  with on most days" where mine said "people you're close to and see most days" (his comment: "who you're close to and
  see most days was hard to parse. i fixed it"). His check: Human Written, one window, High, 94 words. The link on
  "Perry, 2023", which Pangram can't see, goes back where it was.
- W-SW23, the Anti-Breakthrough and the practice paragraph: his version, "which is another dimension of micro-dosing"
  where mine said "which is what I mean by micro-dosing here" ("last line of 1st para was unclear with what it referred
  to (no context), and even with the article context it was unclear since i'm not usually talking about time when
  talking about microdosing"), and "In practice, I'd do something like 30 seconds of slow breathing, 20 times a day."
  for the post's practice paragraph ("what helped was "something like" since nobody could actually do exactly 30
  seconds 20 times"). His checks, three steps: the micro-dosing fix (High 79, Medium 14 over the practice line), "20"
  for "twenty" (the same windows: "that didn't help"), "something like" (one window, High, 95 words).

His versions don't go through apply_gate.py (they are his); each text is asserted to be the one he checked, by SHA-256.
Three of his choices go on the keep-as-is list (K9 to K11): a pass that tightens wording would undo each.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127b/apply_his_x1127b.py [--write]
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
REC = HERE / 'APPLIED-X1127B.json'
ANSWERS = HERE / 'ANSWERS-X1127B-20261127-2259.json'
CHECKS = json.loads((HERE / 'HIS-CHECKS-X1127B.json').read_text(encoding='utf-8'))['checks']
CARDS = {i['id']: i for i in json.loads(ANSWERS.read_text(encoding='utf-8'))['items']}

PERRY = 'https://issuu.com/familyjusticegroup/docs/20230629_journal_final/s/27001732'

OLD_SW19 = ('We are operating on about one-sixteenth of the relational density our biology requires ([Perry, 2023](' + PERRY +
            ')). The "Void" you feel is real. Once you have de-armored, you cannot simply return to a lonely life. You must '
            'aggressively engineer a "High-Density" social environment (A Tribe), or the brain will eventually reach for the '
            'armor again just to survive the cold.')
OLD_SW23 = ('The Anti-Breakthrough (Micro-Dosing): A brain stuck in alarm can often take in healing work for only a few seconds '
            'at a time, Perry finds. So for now we have to give up on the hour-long breakthrough that therapy aims for, since '
            'an hour spent working on the trauma itself overwhelms an armored nervous system more than it heals it. Instead, '
            'this protocol works in doses of a few seconds, which is what I mean by micro-dosing here.\n\n'
            'Your goal is Micro-Dosing Safety: 30 seconds of regulated breathing, twenty times a day. We are not running a '
            'marathon; we are doing physical therapy for a broken nervous system. Frequency beats intensity.')


def his(card, uuid):
    """His version on CARD, asserted to be the text of his check UUID (its SHA-256 as Pangram stored it)."""
    v = CARDS[card]['your_version']
    (c,) = [c for c in CHECKS if c['uuid'].startswith(uuid)]
    assert hashlib.sha256(v.encode('utf-8')).hexdigest() == c['sha256'], card
    assert c['windows'] == [c['windows'][0]] and c['windows'][0][:2] == ['Human', 'High'], card
    return v, c['link']


SW19_PLAIN, SW19_CHECK = his('W-SW19', '51ceffa5')
SW19 = SW19_PLAIN.replace('(Perry, 2023)', '([Perry, 2023](' + PERRY + '))', 1)
assert SW19.count('](') == 1
SW23, SW23_CHECK = his('W-SW23', '6bdc6163')
SW23_STEPS = [c['link'] for c in CHECKS if c['card'] == 'W-SW23']

KEEP_NEW = [
    {'id': 'K9', 'kind': 'choice', 'quote': "people you're close to and who you hang with on most days",
     'what': 'his fix of a clause that was hard to parse: with the second "who you" left out ("close to and see most '
             'days"), a reader can take "see most days" as something the people do; a pass that trims words would take '
             '"who you" out again, and "hang with" is his plain word for spending time with them',
     'joel': "who you're close to and see most days was hard to parse. i fixed it",
     'when': '2026-11-27 22:59 UTC', 'where': 'card W-SW19, his comment (fix-20261108/x1127b/ANSWERS-X1127B-20261127-2259.json)',
     'basis': 'his answer'},
    {'id': 'K10', 'kind': 'choice', 'quote': 'which is another dimension of micro-dosing',
     'what': 'his tie between doses of seconds and micro-dosing as readers know it (small doses of a substance): the '
             'protocol extends the idea to time, it does not redefine the word; "what I mean by micro-dosing here" '
             'pointed at nothing a reader had and took the word from its usual sense',
     'joel': ("last line of 1st para was unclear with what it referred to (no context), and even with the article context "
              "it was unclear since i'm not usually talking about time when talking about microdosing (nor are ppl usually "
              "talking about it that way"),
     'when': '2026-11-27 22:59 UTC', 'where': 'card W-SW23, his comment (fix-20261108/x1127b/ANSWERS-X1127B-20261127-2259.json)',
     'basis': 'his answer'},
    {'id': 'K11', 'kind': 'choice', 'quote': "I'd do something like 30 seconds of slow breathing, 20 times a day",
     'what': 'his rough figure for a daily practice: "something like" looks like a hedge to cut, and it is what makes the '
             'line honest, since nobody does exactly 30 seconds 20 times; "20" is a numeral on purpose (a model spells '
             'it out)',
     'joel': ('for the last line, you forgot not to spell out twenty i think that\'s also a repo rule, ai is always spelling '
              'numbers out ... but that didn\'t help. what helped was "something like" since nobody could actually do '
              'exactly 30 seconds 20 times, that\'s unreasonable'),
     'when': '2026-11-27 22:59 UTC', 'where': 'card W-SW23, his comment (fix-20261108/x1127b/ANSWERS-X1127B-20261127-2259.json)',
     'basis': 'his answer'},
]

OWNER_CHANGES = [
    {'by': 'card W-SW19, his version (fix-20261108/x1127b/ANSWERS-X1127B-20261127-2259.json), applied by '
           'fix-20261108/x1127b/apply_his_x1127b.py',
     'why': ('the one-sixteenth paragraph, his version of my step 7: the post\'s "relational density our biology requires" '
             'becomes "the grown-ups per child that our brains evolved with"; "You must aggressively engineer a '
             '"High-Density" social environment (A Tribe)" becomes "gather a tribe of people you\'re close to and who you '
             'hang with on most days"; "the brain will eventually reach for the armor again just to survive the cold" '
             'becomes "you\'ll eventually put the armor back on just to get through the loneliness"; Perry 2023 and its '
             'link stay. His check: ' + SW19_CHECK + ' (Human Written, one window, High, 94 words). The warning\'s meaning '
             'stays (gather a tribe, or you put the armor back on): its words "aggressively" and "High-Density" go with '
             'the post\'s sentence.'),
     'numbers_lost': [], 'numbers_new': [], 'keys_lost': {'W019': [['aggressively'], ['high-density']]}},
    {'by': 'card W-SW23, his version (fix-20261108/x1127b/ANSWERS-X1127B-20261127-2259.json), applied by '
           'fix-20261108/x1127b/apply_his_x1127b.py',
     'why': ('the Anti-Breakthrough\'s last clause becomes "which is another dimension of micro-dosing", and the post\'s '
             'practice paragraph ("Your goal is Micro-Dosing Safety: 30 seconds of regulated breathing, twenty times a day. '
             'We are not running a marathon; we are doing physical therapy for a broken nervous system. Frequency beats '
             'intensity.") becomes "In practice, I\'d do something like 30 seconds of slow breathing, 20 times a day."; the '
             '30 seconds and the 20 times a day stay (twenty now a numeral). His checks: ' + ', '.join(SW23_STEPS) +
             ' (the last Human Written, one window, High, 95 words).'),
     'numbers_lost': [], 'numbers_new': ['20times'], 'keys_lost': {}},
]


def main(write):
    text = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode('utf-8')).hexdigest()
    assert before.startswith('f8bfa190'), before
    for key, old, new in (('W-SW19', OLD_SW19, SW19), ('W-SW23', OLD_SW23, SW23)):
        assert text.count(old) == 1, key
        text = text.replace(old, new, 1)
    after = hashlib.sha256(text.encode('utf-8')).hexdigest()
    print(before[:8], '->', after[:8])
    if not write:
        # the check as the write will leave it: the keys with this change's owner_changes entries in
        tmp = pathlib.Path('/tmp/apply_his_x1127b.md')
        tmp.write_text(text, encoding='utf-8')
        keys = json.loads(KEYS.read_text(encoding='utf-8'))
        seen = {c['by'] for c in keys['owner_changes']}
        keys['owner_changes'] += [c for c in OWNER_CHANGES if c['by'] not in seen]
        tmpk = pathlib.Path('/tmp/apply_his_x1127b.keys.json')
        tmpk.write_text(json.dumps(keys, ensure_ascii=False), encoding='utf-8')
        subprocess.run([sys.executable, str(ROOT / 'tools/humanization/fidelity_keys.py'), 'check', str(tmpk), str(tmp)])
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
        {'key': 'W-SW19', 'whose': 'his version on the card, as he checked it, with the link on "Perry, 2023" put back',
         'check': 'his check: ' + SW19_CHECK + ' (Human Written, one window, High, 94 words)', 'old': OLD_SW19, 'new': SW19},
        {'key': 'W-SW23', 'whose': 'his version on the card, as he checked it (the Anti-Breakthrough and the practice '
         'paragraph)', 'check': 'his checks, three steps: ' + ', '.join(SW23_STEPS) + ' (the last Human Written, one window, '
         'High, 95 words)', 'old': OLD_SW23, 'new': SW23}],
        'answers': 'x1127b/ANSWERS-X1127B-20261127-2259.json', 'his_checks': 'x1127b/HIS-CHECKS-X1127B.json',
        'before_sha256': before, 'after_sha256': after})
    REC.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('written', after[:8])


if __name__ == '__main__':
    main('--write' in sys.argv)
