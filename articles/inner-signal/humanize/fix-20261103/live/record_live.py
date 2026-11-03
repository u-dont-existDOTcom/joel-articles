"""LIVE-CHECK-20261103.json: the hypnosis guide (HUMANIZED-SO-FAR.md 010b9fc3) in Joel's post behind
hypnosis.u-dont-exist.com, after his "33a" of 2026-11-03 13:46 UTC.

Question 33 a) was: "with the Pattern 10 card's answer in, I put the guide into your post the way I did on 2 November (in
its editor, one change, no pasting), change "Last update" in the subtitle to today, and read the public post back word for
word." His message (`../c1103b/joel-20261103-1346-message.txt`) also gave his Pattern 10 version (E-523) and "old" for
"oily"; both went in first, then the six slips the nonsense read found in our words (`../nonsense/`).

What was done, in the app's browser (his Substack, signed in), the post's editor:
- The public post, read without signing in before anything changed (POST-BEFORE.json), was exactly the post of
  2 November (its body's SHA-256 f014f7b8, the same as after that day's date change), so he hadn't changed it since.
- substack_merge.py put the guide into the editor copy of 28 September (ARCHIVAL-20261103.html, MERGE-REPORT.json PASS:
  30,354 words equal to the guide's text blocks, 43 links, 8 native objects byte for byte).
- make_update.py compared that with 2 November's archival HTML block by block (UPDATE-PLAN.json, pushed at bb25cc0d and
  fetched in the tab from raw.githubusercontent.com, checked by its SHA-256). update.js checked every one of the editor's
  729 nodes against 2 November's blocks (none differed, so no draft change of his was there to lose), parsed the 76
  changed ranges with the editor's own schema into one transaction of 76 steps, and checked the result: 720 nodes, each
  equal to today's blocks, the six native blocks the same nodes as before, the same 38 links in order. dispatch.js
  applied it. The subtitle's "Last update: Nov 2, 2026, v. 7.0" became "Last update: Nov 3, 2026, v. 7.0" (the date
  only: question 33 asked about the date, not the version). The draft saved (its body, 720 nodes, and its subtitle
  checked in the editor's own draft API); Update, then "Update now", settings untouched.
- The public API first answered with the old post for a few minutes (two copies on the laptop, POST-AFTER-cached*.json,
  the same as POST-BEFORE but for its time stamp); then the new one. That one, read without signing in from the laptop
  (POST-AFTER.json), is compared here with the guide's text, word for word.

  python3 articles/inner-signal/humanize/fix-20261103/live/record_live.py
"""
import difflib
import hashlib
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

URL = 'https://ibogaqueen.substack.com/p/guide-to-self-hypnosis-and-app-including'
SUBTITLE = "You won't find a hypnosis guide like this anywhere. Last update: Nov 3, 2026, v. 7.0"
TITLE = 'Inner Signal Guide to Self-Hypnosis (& APP), including Reparenting, Conscious-Subconscious Spiritual Communion'
# What differed on 2 November too (LIVE-CHECK-20261102.json): the native blocks' own text, which the guide's Markdown
# names ("image 1", the video's and the post embeds' cards) and the post shows differently, and one word the editor's
# markup splits ("suggestion" and its "s" in two runs).
NATIVE = re.compile(r'^(image \d+( |$)|Double click to interact with video$|Psychedelics Trip-Sitting Medical Triage)')


def words(t):
    return re.findall(r"[\w’'-]+", t)


def body_words(body):
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', body, flags=re.S)
    return words(html.unescape(re.sub(r'<[^>]+>', ' ', t)))


def main():
    before = json.loads((HERE / 'POST-BEFORE.json').read_text(encoding='utf-8'))
    after = json.loads((HERE / 'POST-AFTER.json').read_text(encoding='utf-8'))
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    guide = words(' '.join(b['text'] for b in sr.blocks(md)))
    live = body_words(after['body_html'])
    diffs, other = [], []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=guide, b=live, autojunk=False).get_opcodes():
        if op == 'equal':
            continue
        d = {'op': op, 'guide': ' '.join(guide[i1:i2])[:300], 'live': ' '.join(live[j1:j2])[:300]}
        d['native'] = bool(NATIVE.match(d['guide'])) and not d['live'] or (d['guide'], d['live']) == ('suggestions', 'suggestion s')
        diffs.append(d)
        if not d['native']:
            other.append(d)
    rec = {'about': __doc__.split('\n\n')[0].replace('\n', ' '), 'url': URL, 'post_id': after.get('id'),
           'title': after.get('title'), 'subtitle': after.get('subtitle'), 'audience': after.get('audience'),
           'post_date': after.get('post_date'),
           'before': {'body_html_sha256': hashlib.sha256(before['body_html'].encode('utf-8')).hexdigest(),
                      'subtitle': before.get('subtitle'), 'words': len(body_words(before['body_html']))},
           'after': {'body_html_sha256': hashlib.sha256(after['body_html'].encode('utf-8')).hexdigest(),
                     'words': len(live)},
           'guide': {'file': 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md',
                     'sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(), 'words': len(guide)},
           'checks': {'title unchanged': after.get('title') == TITLE == before.get('title'),
                      'subtitle': after.get('subtitle') == SUBTITLE,
                      'audience unchanged': after.get('audience') == before.get('audience') == 'everyone',
                      'post date unchanged': after.get('post_date') == before.get('post_date'),
                      'words: only the native blocks differ': not other},
           'differences': diffs}
    rec['verdict'] = 'PASS' if all(rec['checks'].values()) else 'FAIL'
    (HERE / 'LIVE-CHECK-20261103.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(rec['verdict'], '| guide words', len(guide), '| live words', len(live), '| differences', len(diffs),
          '| not native', len(other), '|', rec['checks'])
    for d in diffs:
        print(' ', 'native' if d['native'] else 'OTHER ', d['op'], '| guide:', d['guide'][:110], '| live:', d['live'][:110])
    return 0 if rec['verdict'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
