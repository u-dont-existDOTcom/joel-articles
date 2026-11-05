"""The ATP section's first paragraph (his post's block 95), first try, into the article: it read Human Written, 0.0% AI,
one window, High, by itself in Pangram's web app (batch x1104u,
https://www.pangram.com/history/53b000ed-a200-44af-8eb7-051b992576a1).

The comparative read beside his post (E284, E294) is mine, sentence by sentence. "If your cortisol is normal or low, low ATP
signaling in the brain might be what's behind your anxiety or depression" says the section's heading ("Fixing ATP Signaling if
Cortisol Isn't High") as the reader's case, the point first (E357, E360); "Recent neuroscience (Tian-Ming Gao, et al, 2025) has
shown in male mice that anxiety and depression are a result of reduced hippocampal ATP signaling" is his sentence; "So I'd trial
20mg of PQQ in the morning to boost ATP, with ketones" is his "To address both issues, you can trial a morning dose of 20mg of
PQQand ketones", the typo fixed, the dose his own advice like his Y-88, and what each does said from his Part 1 ("We use PQQ to
boost ATP, and Ketones, which bypass the broken glucose pathways"): "which your neurons can still burn for energy when they're
struggling to burn sugar". Two findings, both changes of mine, to him on Cards (5):
- his "Calabrese, et al (2024) have shown in one study that's part of much broader research that ketones and reduced
  carbohydrate intake are highly effective for anxiety, depression, and other mental illnesses" said as what the paper shows
  (E348): it is a case series of three adults on a ketogenic diet, all in full remission of depression and anxiety within 7
  to 12 weeks (Frontiers in Nutrition 2024, PMC11182043); "highly effective for ... other mental illnesses" is more than three
  people can show. His "part of much broader research" stays.
- the order: the ketone study now comes after the step it supports.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/next6/apply_b095.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-B095.json and read/READ-RECORD.json.
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
BEFORE = 'bef55334'
TESTED = 'https://www.pangram.com/history/53b000ed-a200-44af-8eb7-051b992576a1'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha.startswith(BEFORE), 'the article changed'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    new = (HERE / 'blocks' / '095.md').read_text(encoding='utf-8').strip()
    tested = json.loads((HERE.parent / 'checks' / 'x1104u' / 'TEXTS.json').read_text(encoding='utf-8'))['b095']
    tested = tested if isinstance(tested, str) else tested['text']
    assert re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', new) == tested, 'not the text that was checked'
    (i,) = [k for k, b in enumerate(raw) if b.startswith('[Recent neuroscience](')]
    old = raw[i]
    raw[i] = new
    out = '\n\n'.join(raw) + '\n'
    r = fk.check(json.loads((H / 'FIDELITY-KEYS.json').read_text(encoding='utf-8')), out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'about': 'his post\'s block 95, the ATP section\'s first paragraph, first try: Human Written, 0.0% AI by itself in '
                    'the web app, one window, High',
           'before_sha256': sha, 'after_sha256': after, 'block': i, 'before': old, 'after': new, 'tested': TESTED,
           'windows': ['Human, High, 114'], 'tries': [],
           'changes': ['the Calabrese case series said as what it shows (E348; card on Cards (5))',
                       'the ketone study after the step it supports; the point first (E357, E360)'],
           'fidelity_pass': r['pass']}
    print(json.dumps(rec, ensure_ascii=False, indent=1))
    assert r['pass'], r
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    (HERE / 'APPLIED-B095.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(sr.blocks(out)[i]['text'])], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: his post\'s block 95 (the ATP section\'s first paragraph, first try) read '
                      'beside his post\'s by the lead session (E284, E294)' % after[:8])


if __name__ == '__main__':
    main()
