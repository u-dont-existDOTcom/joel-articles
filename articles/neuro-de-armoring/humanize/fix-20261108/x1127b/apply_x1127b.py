#!/usr/bin/env python3
"""Put this turn's paragraph that read Human High in every window by itself into HUMANIZED-SO-FAR.md (apply_gate.py):
the underpinnings paragraph (P-SW21), step 3 from his card version: HDAC inhibition said with the ketones that do it.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127b/apply_x1127b.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import apply_gate  # noqa: E402
import texts_x1127b as T  # noqa: E402

REC = HERE / 'APPLIED-X1127B.json'


def sw17(write):
    """The "Underpinning" Principle, PAIR-SW17-18 step 2 (the title off Perry, the label marked off, the curtains line
    joined), checked with the paragraph before it (#328, one window, High)."""
    new = T.STEP['sw17-s2']
    apply_gate.require(T.H / 'pangram-ledger.jsonl', [T.plain(new)])
    text = T.ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode()).hexdigest()
    assert text.count(T.OLD['sw17']) == 1
    text = text.replace(T.OLD['sw17'], new)
    after = hashlib.sha256(text.encode()).hexdigest()
    print('sw17', before[:8], '->', after[:8])
    if write:
        T.ARTICLE.write_text(text, encoding='utf-8')
        rec = json.loads(REC.read_text(encoding='utf-8'))
        rec['runs'].append({'applied': [{
            'key': 'sw17', 'whose': 'mine: the post\'s "Underpinning" Principle with "Dr." off Perry, a colon after the '
            'label, and the curtains line joined to the sentence before ("and you can\'t hang curtains in a collapsing '
            'house")', 'check': 'my check, this turn: https://www.pangram.com/history/29eb7cd5-f1bd-4ce8-80e4-6a8e33e42277 '
            '(Human Written, one window, High, 139 words, with the paragraph before it; PAIR-SW16-17 #328); with the '
            'Gibson paragraph after it the Principle read High too, the Gibson paragraph\'s opening question Medium '
            '(https://www.pangram.com/history/7316e9b0-455f-4fb4-9bdc-0ec0b33fad13, #327)',
            'old': T.OLD['sw17'], 'new': new}], 'before_sha256': before, 'after_sha256': after})
        REC.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('written', after[:8])


def main(write):
    new = T.STEP['sw21-s3']
    apply_gate.require(T.H / 'pangram-ledger.jsonl', [T.plain(new)])
    text = T.ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode()).hexdigest()
    assert text.count(T.SW21_263) == 1
    text = text.replace(T.SW21_263, new)
    after = hashlib.sha256(text.encode()).hexdigest()
    print('sw21', before[:8], '->', after[:8])
    if write:
        T.ARTICLE.write_text(text, encoding='utf-8')
        rec = {'about': 'the humanizing pass of "Psychology is the Software; Biology is the Hardware.", the turn of his '
                        'message of 2026-11-27 20:08 UTC', 'runs': [{'applied': [{
                            'key': 'sw21', 'whose': 'mine: his card version of 2026-11-03 (the underpinnings paragraph) '
                            'with three small steps: "so we can dig ... and pour ..., and eventually ..." for "to allow us to '
                            'dig ..., and pour ..., so we can eventually ...", "works like" for "serves as", "the psychology '
                            'upstairs" for "the psychological software upstairs", and HDAC inhibition said with the ketones '
                            '("Ketones (BHB, which block HDACs)")',
                            'check': 'my check, this turn: https://www.pangram.com/history/8a7cf54b-2112-41e5-94ab-b14087a373f1 '
                                     '(Human Written, one window, High, 57 words; P-SW21 step 3, #325)',
                            'old': T.SW21_263, 'new': new}], 'before_sha256': before, 'after_sha256': after}]}
        REC.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        print('written', after[:8])


if __name__ == '__main__':
    if '--sw17' in sys.argv:
        sw17('--write' in sys.argv)
    else:
        main('--write' in sys.argv)
