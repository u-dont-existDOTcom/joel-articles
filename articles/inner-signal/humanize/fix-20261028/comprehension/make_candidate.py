"""The hypnosis guide with Joel's six answers of 2026-10-28 in, then with the comprehension fixes in.

--answers-only: BASE-ANSWERS.md and CHANGES-ANSWERS.json. His answers file of 15:19 UTC (../ANSWERS-20261028-1519.json,
from the editor page of 2026-10-27): HG-S11 and HG-S12 approved, ED-A1, ED-A3, ED-A5 and HG-S15 revised. A revised card's
version replaces its whole paragraph, word for word, except one obvious typo ("All of these can are separate factors" ->
"All of these are separate factors"). Links and italics stay on their words (html_text_edit.set_text, as in the 25
October answers).

Without it: CANDIDATE.md and CHANGES.json, BASE-ANSWERS.md with every fix of fix/KEPT.json in (the writers' fixes as I
kept or changed them, review_fixes.py), each an exact replacement of words inside its paragraph. A fix whose new words
run over several lines gives a list back its line breaks: a lead-in line, then "- " items.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/make_candidate.py [--answers-only]
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text, split_block  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
EDITOR = H / 'fix-20261027' / 'review' / 'EDITOR-27.json'
ANSWERS = H / 'fix-20261028' / 'ANSWERS-20261028-1519.json'
TYPOS = {'HG-S15': [('All of these can are separate factors', 'All of these are separate factors')]}


def answers():
    """BASE-ANSWERS.md: the guide of 2026-10-27 with his six answers in, and CHANGES-ANSWERS.json."""
    # the guide as the editor page showed it (commit 0a44911d), whatever HUMANIZED-SO-FAR.md holds now
    md = subprocess.run(['git', 'show', '0a44911d:articles/inner-signal/humanize/HUMANIZED-SO-FAR.md'], cwd=ROOT,
                        capture_output=True, text=True, check=True).stdout
    editor = json.loads(EDITOR.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == editor['article']['sha256'], 'the guide changed since the editor page'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl), (len(raw), len(bl))
    text = {b['i']: b['text'] for b in bl}
    changes, lost = [], []
    S = {s['id']: s for s in editor['suggestions']}
    for x in answers['items']:
        if x['status'] not in ('approved', 'revise'):
            continue
        s = S[x['id']]
        if x['status'] == 'approved':
            (e,) = s['edits']
            i, after = e['block'], e['after']
            assert text[i] == e['before'], x['id']
            how = 'approved (his answer of 2026-10-28 15:19 UTC)'
        else:
            i = (s['edits'][0]['block'] if s['edits'] else s['spans'][0]['block'])
            after = x['your_version'].strip()
            for a, b in TYPOS.get(x['id'], []):
                assert a in after
                after = after.replace(a, b)
            how = 'his version (revised, 2026-10-28 15:19 UTC)' + (', one typo fixed' if x['id'] in TYPOS else '')
        raw[i] = set_block_text(raw[i], after, lost)
        changes.append({'id': x['id'], 'block': i, 'where': sr.where(bl, i), 'how': how, 'before': text[i],
                        'after': after, 'findings': []})
        text[i] = after
    out = '\n\n'.join(raw) + '\n'
    (HERE / 'BASE-ANSWERS.md').write_text(out, encoding='utf-8')
    write_record('CHANGES-ANSWERS.json', sha, md, out, changes, lost)


def fixes():
    """CANDIDATE.md: BASE-ANSWERS.md with every fix of fix/KEPT.json in, and CHANGES.json."""
    md = (HERE / 'BASE-ANSWERS.md').read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl), (len(raw), len(bl))
    text = {b['i']: b['text'] for b in bl}
    new_raw, changes, lost = {}, [], []
    kept = json.loads((HERE / 'fix' / 'KEPT.json').read_text(encoding='utf-8'))
    for fx in kept['fixes']:
        i = fx['block']
        before = text[i]
        assert before.count(fx['replace']) == 1, (fx['id'], fx['replace'][:80], before[:200])
        after = before.replace(fx['replace'], fx['with'])
        if '\n' in after:
            # a list whose line breaks were lost, given back as a lead-in line and "- " items
            assert i not in new_raw, '%s: a list fix must be its paragraph\'s only fix' % fx['id']
            outs = []
            for ln in (x.strip() for x in after.split('\n')):
                if not ln:
                    continue
                outs.append('- ' + ln[2:].strip() if ln.startswith('- ') else ln)
            new_raw[i] = outs
        else:
            new_raw[i] = [set_block_text(new_raw[i][0] if i in new_raw else raw[i], after, lost)]
        changes.append({'id': fx['id'], 'block': i, 'where': sr.where(bl, i), 'how': fx['how'],
                        'replace': fx['replace'], 'with': fx['with'], 'before': before, 'after': after,
                        'findings': fx['findings'], 'note': fx.get('note', '')})
        text[i] = after
    out = []
    for j, r in enumerate(raw):
        out += new_raw.get(j, [r])
    cand = '\n\n'.join(out) + '\n'
    (HERE / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    write_record('CHANGES.json', sha, md, cand, changes, lost)


def write_record(name, sha, md, out, changes, lost):
    rec = {'from': {'sha256': sha, 'blocks': len(sr.blocks(md))},
           'to': {'sha256': hashlib.sha256(out.encode('utf-8')).hexdigest(), 'blocks': len(sr.blocks(out))},
           'links_lost': lost, 'changes': changes}
    (HERE / name).write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(name, len(changes), 'changes;', rec['from']['blocks'], '->', rec['to']['blocks'], 'blocks; links lost:', lost)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--answers-only', action='store_true')
    args = ap.parse_args()
    answers() if args.answers_only else fixes()


if __name__ == '__main__':
    main()
