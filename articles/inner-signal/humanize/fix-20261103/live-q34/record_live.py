"""LIVE-CHECK-20261103b.json: the hypnosis guide (HUMANIZED-SO-FAR.md d67ef820) in Joel's post behind
hypnosis.u-dont-exist.com, after his answers to question 34 of 2026-11-03 14:52 UTC.

His answers (`../q34/joel-20261103-1452-message.txt`, `../q34/APPLIED-Q34.json`): 34.2 his sentence ("That hand movement
grounds and aligns the distractible mind."), 34.3 the change he agreed to, 34.5 his "coordination"; 34.1 and 34.4 kept.
Question 34 a) had said the changes would then go into his post the same way as the 33a update of the same day.

What was done, in the app's browser (his Substack, signed in), the post's editor, as `../live/record_live.py` describes
(gate E332):
- The public post, read first without signing in (POST-BEFORE.json), had the same body as after the 33a update
  (`../live/POST-AFTER.json`), so he hadn't changed it since.
- substack_merge.py put the guide into the editor copy of 28 September (ARCHIVAL-20261103b.html, MERGE-REPORT.json PASS).
- `../live/make_update.py --old ../live/ARCHIVAL-20261103.html --new ARCHIVAL-20261103b.html` (UPDATE-PLAN.json: three
  changed paragraphs), pushed at 38f32975 and fetched in the tab by its SHA-256; `../live/update.js` checked all 720 of
  the editor's nodes against the blocks put in at 33a (none differed), built one transaction of three steps, and
  checked the result (720 nodes, each equal to the new blocks, the six native blocks the same nodes, the same 38 links);
  `../live/dispatch.js` applied it. The subtitle already had the day ("Last update: Nov 3, 2026, v. 7.0"), so it stayed.
  The draft saved (the draft API: 720 nodes, his three changes in, the old words gone); Update, then "Update now",
  settings untouched; the publish call answered 200.
- The public post, read without signing in from the laptop (POST-AFTER.json; it had the new body at once this time), is
  compared here with the guide's text, word for word.

  python3 articles/inner-signal/humanize/fix-20261103/live-q34/record_live.py
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
    (HERE / 'LIVE-CHECK-20261103b.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(rec['verdict'], '| guide words', len(guide), '| live words', len(live), '| differences', len(diffs),
          '| not native', len(other), '|', rec['checks'])
    for d in diffs:
        print(' ', 'native' if d['native'] else 'OTHER ', d['op'], '| guide:', d['guide'][:110], '| live:', d['live'][:110])
    return 0 if rec['verdict'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
