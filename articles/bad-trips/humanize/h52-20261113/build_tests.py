#!/usr/bin/env python3
"""build_tests.py - turn 42's carry (2026-11-13): his round-39 lessons (../../experiments/t39-answers/JOEL-TRIES-TEACH-EVID.md)
carried to Chest Pain's evidence paragraph (B123): how far the evidence goes said plainly first; each finding in the reader's
words, saying when it was given (before the heart attack, as his "when given after a stroke" says when); why the clotting
work bears on chest pain said; the links on the words that name each study, not in a list after it.

No Pangram check this turn: the link to his computer, where his Pangram history is open, failed to connect. The drafts go
through the three reads now; their checks, by themselves, come when the link is back (apply_gate.py).

  python3 build_tests.py
"""
import hashlib, pathlib
HERE = pathlib.Path(__file__).resolve().parent
HEAD = "Chest Pain and Injury"
HIS = ("DMSO is also my first remedy for many injuries and some chest pain. After I overused erythritol, I developed angina that "
       "lasted for days. I took DMSO, the pain disappeared within about a minute, and it never returned.")
CP1 = ("The heart research on DMSO is only in animals and lab dishes so far, but it leans this way. In rats given DMSO before a "
       "heart attack, about three quarters less heart muscle died, and their blood showed far less sign of heart damage. Other "
       "studies found it slowed the clotting that blocks arteries, in human platelets too.")
TESTS = {'cp-c1': CP1, 'cpsec-c1': "\n\n".join([HEAD, HIS, CP1])}

# cp-c2, after the reads of cp-c1 (reads/): which way the research leans said ("it suggests DMSO protects the heart"), and
# why the clotting work bears on chest pain ("the clotting that blocks arteries and brings on a heart attack"). The rats'
# timing stays said ("before a heart attack"), as he says when the animals got it in his evidence paragraph.
CP2 = ("The heart research on DMSO is only in animals and lab dishes so far, but it suggests DMSO protects the heart. In rats "
       "given DMSO before a heart attack, about three quarters less heart muscle died, and their blood showed far less sign of "
       "heart damage. Other studies found it slowed the clotting that blocks arteries and brings on a heart attack, in human "
       "platelets too.")
TESTS['cp-c2'] = CP2
TESTS['cpsec-c2'] = "\n\n".join([HEAD, HIS, CP2])

if __name__ == '__main__':
    for k, t in TESTS.items():
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode()).hexdigest()[:12])
