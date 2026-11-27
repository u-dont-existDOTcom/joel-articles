"""The humanizing pass in "Psychology is the Software; Biology is the Hardware." while his cards wait: the
Anti-Breakthrough (lineage P-SW22), from its near miss of last turn (#267: Human, High 25 words, Medium 2 words over "Perry
finds.", High 36, Medium 22 over its last sentence; https://www.pangram.com/history/36898004-2c24-40f5-9e53-f005d95b8a1d),
one change a check (the near-miss rule). The receipts use x1126b's builder (its sw22), the reads x1126b/v1.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127a/sw_x1127a.py [KEY ...]   (receipts)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
sys.path.insert(0, str(FIX / 'x1126b'))
import build_receipts_x1126b as RB  # noqa: E402

T = RB.T
RB.B.HERE = HERE / 'receipts'
SW22 = T.NEW['sw22']
# Step 1: the window of two words, "Perry finds.", is the split Pangram makes at "Dr."; the title off, as his 71 took it
# off Epley ("71 ok", 2026-11-26), and the section introduced "Dr. Bruce Perry" two paragraphs before.
STEP = {'sw22-s1': SW22.replace('seconds at a time, Dr. Perry finds.', 'seconds at a time, Perry finds.')}
assert STEP['sw22-s1'] != SW22


# Step 1 read Human Written, 0.0% AI: High over the first two sentences (62 words, the split gone), Medium over the last
# (https://www.pangram.com/history/97d19f12-4aa9-4349-ae0f-ac29b81f1e72). Step 2, its last sentence: "and those small
# doses are what I mean by micro-dosing here" says "doses" again, and a reader who met "Micro-Dosing" as the drug doses
# (v1/fit/sw22) can take "those small doses" as drug doses too; "which is what I mean by micro-dosing here" points at
# the doses of seconds just named, and the sentence is spoken, not a definition.
STEP['sw22-s2'] = STEP['sw22-s1'].replace('a few seconds, and those small doses are what I mean by micro-dosing here.',
                                          'a few seconds, which is what I mean by micro-dosing here.')
assert STEP['sw22-s2'] != STEP['sw22-s1']

if __name__ == '__main__':
    keys = sys.argv[1:] or list(STEP)
    bad = []
    for k in keys:
        bad += RB.sw22('SW22-' + k.split('-')[1].upper(), T.plain(STEP[k]), False)
    print('\n'.join(bad))
    print('receipts:', 'FAIL' if bad else 'PASS')
