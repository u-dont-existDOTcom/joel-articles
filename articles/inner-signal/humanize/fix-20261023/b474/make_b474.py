"""Batch 474: recheck A's three red stretches (2026-10-23, after Joel's message of 14:14 UTC) as 4.1 edits for EDITS41.json:
EDITS-b474.json.

Recheck A (https://www.pangram.com/feed/3f9225c6-4ec8-452e-bdff-d44040b1acc0, Mostly Human Written, 1.4% AI) read AI on:
- windows 83 to 86 (Low and Medium): the driving caution's second sentence into the shortcut paragraph, though batch 473's
  shortcut paragraph had read Human, High, alone and as a pair (E240);
- window 93 (Low): the return's check, "Move around a bit, and don't get up until you feel steady. Make sure you're truly
  oriented and alert (the count ...)";
- windows 102 and 103 (Low and Medium, marked humanized): Nothing happens' two lines and It feels fake's first question,
  Emulate's text of 460g, Human, Medium, in the check before.
Each stretch went to Emulate (E237; its own text re-run, E235): three samples (bl/, bm/, bn/; BUNDLE.json), and only the red
sentences were spliced back (CANDIDATES.json says from which sample and why). All three read Human, 0% AI, through the API
(API-CHECKS.md), which for Low and Medium red says only that they are no worse (E226, E240); the next recheck of part A
decides. The second reader's report is REVIEW.md; its triage, TRIAGE_FIXES below.

  python3 articles/inner-signal/humanize/fix-20261023/b474/make_b474.py   (from the repo root)
  then: python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --add articles/inner-signal/humanize/fix-20261023/b474/EDITS-b474.json
"""
import json, pathlib

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
PLAIN = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})
# (replace, with) pairs from TRIAGE.json, applied to the new texts (the second reader's, triaged; REVIEW.md)
TRIAGE_FIXES = [["And that’s use it while you’re driving", "And that’s use it, practice it or test it while you’re driving"], ["Take mental note of anything that has come up for you", "Take mental note of only what actually came up for you"], ["Show yourself one sensation, one word,", "Show yourself one body sensation, one word,"]]


def line(md, first):
    a = md.index(first)
    assert md.count(first) == 1, first
    return md[a:md.index('\n', a)]


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    C = json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))
    links = {r['name']: r['dashboard_link'] for f in sorted(B.glob('API-RESULTS-*.jsonl'))
             for r in map(json.loads, f.read_text(encoding='utf-8').splitlines()) if r}
    def fix(s):
        for a, b in TRIAGE_FIXES:
            if a in s:
                s = s.replace(a, b)
        return s
    src ='Emulate (E237, E235), three samples of each stretch (b474/bl, bm, bn); '
    seam_new = [fix(x).translate(PLAIN) for x in C['b474_seam2']['new']]
    s3c_new = fix(C['b474_s3c']['new'][0]).translate(PLAIN)
    tr_new = [fix(x).translate(PLAIN) for x in C['b474_trouble']['new']]
    edits = []
    for key, first, new, check, frm in (
            ('HG17-b474-drive', 'Never do this when you are driving', seam_new[0], 'b474_seam2', 'the driving caution from sample bn'),
            ('HG17-b474-retire', 'If you want to turn this one off,', seam_new[1], 'b474_seam2', 'the shortcut paragraph from sample bl'),
            ('HG18-b474-s3c', 'When you come out, remind yourself what day', s3c_new, 'b474_s3c_pair', C['b474_s3c']['from']),
            ('HG24-b474-small', 'Could you try starting a bit smaller?', tr_new[0], 'b474_trouble', 'the first line from sample bm'),
            ('HG24-b474-show', 'Showing yourself just one sensation in your body', tr_new[1], 'b474_trouble', 'the second line from sample bn')):
        edits.append({'key': key, 'section': key.split('-')[0], 'source': src + frm, 'batch': '474', 'old': line(md, first),
                      'new': new, 'paragraph_check': links[check],
                      'paragraph_result': 'Human Written, 0% AI, through the API (no worse; the in-place recheck decides)',
                      'section_check': None, 'section_result': 'read in place in the next recheck of part A',
                      'review': 'fix-20261023/b474/REVIEW.md'})
    q3_old = "Do you know what exactly feels fake - the words, an image, what you are expecting, the role etc?"
    assert md.count(q3_old) == 1
    q3_new = tr_new[2][:tr_new[2].index(' It doesn')]
    edits.append({'key': 'HG24-b474-fake', 'section': 'HG24', 'source': src + 'the question from sample bm', 'batch': '474',
                  'old': q3_old, 'new': q3_new, 'paragraph_check': links['b474_trouble'],
                  'paragraph_result': 'Human Written, 0% AI, through the API (no worse; the in-place recheck decides)',
                  'section_check': None, 'section_result': 'read in place in the next recheck of part A',
                  'review': 'fix-20261023/b474/REVIEW.md'})
    (B / 'EDITS-b474.json').write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('EDITS-b474.json: %d edits' % len(edits))


if __name__ == '__main__':
    main()
