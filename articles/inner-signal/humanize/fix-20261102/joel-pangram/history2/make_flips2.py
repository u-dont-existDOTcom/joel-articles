"""FLIPS-2.json and the table at the end of HISTORY-LEARNING-2.md: what Joel's second Pangram account taught.

Joel, 2026-11-02 21:59 UTC: "i logged into the other pangram account if you want to read that history" (the hypnosis
guide lane's history read of 18:16 UTC, ../history/, was his first account). Read in the app's browser, signed in by him:
the history list (https://web.pangram.com/api/history-list/, 2,359 checks, 2026-07-24 to 2026-11-02) and each candidate's
full record (/api/history/<uuid>/). A pair is a check that read AI (AI Generated, AI Detected or AI Assisted) followed,
within the next four checks, by a Human Written check of a text with at least 60% of its words kept (a word-level diff of
the two full texts). Of 284 such candidates, 230 kept 60% of their words, 218 of them read Human Written, and 92 changed 30
words or fewer; those 92 are 70 Human Written checks, each kept here with the AI check just before it (the edit that did
it), in rows_raw.py, whose SHA-256 (canonical JSON) matched the page's: 3dbc3bc4...

  python3 articles/inner-signal/humanize/fix-20261102/joel-pangram/history2/make_flips2.py
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from rows_raw import ROWS  # noqa: E402

L = 'https://www.pangram.com/history/'
MARK = '<!-- the table below is written by make_flips2.py -->'


def main():
    canon = json.dumps(ROWS, ensure_ascii=False, separators=(',', ':'))
    assert hashlib.sha256(canon.encode('utf-8')).hexdigest().startswith('3dbc3bc4')
    pairs = [{'n': r[0], 'ai': r[1], 'human': r[2], 'ai_checked': r[3], 'minutes_apart': r[4], 'ai_result': r[5],
              'human_result': 'Human Written', 'words': r[6], 'words_changed': r[7], 'ai_checks_of_it_before': r[8],
              'changes': r[9], 'ai_link': L + r[1], 'human_link': L + r[2]} for r in ROWS]
    out = {'about': 'Joel\'s second Pangram account (he logged into it in the app\'s browser on 2026-11-02, 21:59 UTC: "i '
                    'logged into the other pangram account if you want to read that history"): of its 2,359 checks, the 70 '
                    'Human Written checks that came within four checks after an AI one on a text with at least 60% of the '
                    'same words, where the change was 30 words or fewer; each with the AI check just before it. "changes" is '
                    'the word diff of the two full texts ([-...-] taken out, [+...+] put in), cut at 300 characters. The '
                    'links are private to that account: they open for him signed in to it and read 403 for anyone else '
                    '(E322).',
           'checks_read': 2359, 'candidates': 284, 'kept_60_percent': 230, 'human_written': 218, 'changed_30_or_fewer': 92,
           'pairs': pairs}
    (HERE / 'FLIPS-2.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    doc = HERE / 'HISTORY-LEARNING-2.md'
    head = doc.read_text(encoding='utf-8').split(MARK)[0]
    byn = {p['n']: p for p in pairs}

    def fill(m):
        n = int(m.group(2))
        assert n in byn, n
        return byn[n]['ai_link'] if m.group(1) == 'ai' else byn[n]['human_link']
    head = re.sub(r'\{(ai|hu):(\d+)\}', fill, head)
    rows = ['| # | AI check | then | words changed | what changed |', '|---|---|---|---|---|']
    for p in pairs:
        ch = p['changes'].replace('|', '\\|')
        rows.append('| %d | [%s](%s), %s | [Human Written](%s), %s min later | %d of %d | %s |' % (
            p['n'], p['ai_result'], p['ai_link'], p['ai_checked'][:10], p['human_link'], p['minutes_apart'],
            p['words_changed'], p['words'], ch))
    doc.write_text(head + MARK + '\n\n' + '\n'.join(rows) + '\n', encoding='utf-8')
    print(len(pairs), 'pairs')


if __name__ == '__main__':
    main()
