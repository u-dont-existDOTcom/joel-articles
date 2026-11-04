"""The 5-HTP "Who this is for" (block 88), second try, into the article: it read Human Written, 0.0% AI, by itself in
Pangram's web app (batch x1104k, https://www.pangram.com/history/8d2d4cf1-13da-4c6c-83ae-eddb774ef930), its windows Medium,
High, Medium and Low (the Low one its last two sentences). The one-sentence fix of that Low window (batch x1104l) read
worse, AI Detected, 13.8% AI, with every window moved (E350), so this version goes in and the Low window goes to Joel.

The comparative read beside his post (E284, E294) is mine, sentence by sentence: "5-HTP is not for every depressed person
either" is his post's "not for every depressed person"; "It could help, though, with a low-serotonin-looking pattern" is
his "This is for the low-serotonin-looking pattern" said with the hedge he chose for uridine in the same place (his
"Who this is for", block 81: "It could be helpful, though, for folks that show ..."), who it's for kept; "it's hard to fall
asleep and your mood is low, without much warmth to it" and "At night you get anxious and keep going over the same
things" are his "poor sleep initiation, low mood, low warmth, night anxiety, repetitive rumination"; "It makes more sense
if there's also a genetic or clinical reason to suspect a bottleneck in serotonin synthesis" is the last item of his
list, now said as what makes the pattern likelier; Scott's TPH2 bottleneck and what 5-HTP helped are his; the four
exclusions are his, in his order, and "you shouldn't be casually experimenting with it" is his "this is not a casual
experiment". No finding.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/next2/apply_b088.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-B088.json and read/READ-RECORD.json.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import fidelity_keys as fk  # noqa: E402
import suggestion_review as sr  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = 'c73f5b5d'
TESTED = 'https://www.pangram.com/history/8d2d4cf1-13da-4c6c-83ae-eddb774ef930'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha.startswith(BEFORE), 'the article changed'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    new = (HERE / 'blocks' / '088.md').read_text(encoding='utf-8').strip()
    tested = json.loads((HERE.parent / 'checks' / 'x1104k' / 'TEXTS.json').read_text(encoding='utf-8'))['b088']
    assert re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', new) == tested, 'not the text that was checked'
    (i,) = [k for k, b in enumerate(raw) if b.startswith('Who this is for: This is for the low-serotonin-looking pattern')]
    old = raw[i]
    raw[i] = new
    out = '\n\n'.join(raw) + '\n'
    r = fk.check(json.loads((H / 'FIDELITY-KEYS.json').read_text(encoding='utf-8')), out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'about': 'block 88, the 5-HTP "Who this is for", second try: Human Written, 0.0% AI by itself in the web app',
           'before_sha256': sha, 'after_sha256': after, 'block': i, 'before': old, 'after': new, 'tested': TESTED,
           'windows': ['Human, Medium, 13', 'Human, High, 27', 'Human, Medium, 12', 'Human, Low, 61'],
           'low_window_fix': 'https://www.pangram.com/history/4079bcd3-65eb-43f8-97bb-ec8436fc5f19 (AI Detected, 13.8% AI: '
                             'not taken; the Low window goes to Joel, E350)',
           'fidelity_pass': r['pass']}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    assert r['pass'], r
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    (HERE / 'APPLIED-B088.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(sr.blocks(out)[i]['text'])], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: block 88 (the 5-HTP "Who this is for", second try) read beside his '
                      'post\'s by the lead session (E284, E294)' % after[:8])


if __name__ == '__main__':
    main()
