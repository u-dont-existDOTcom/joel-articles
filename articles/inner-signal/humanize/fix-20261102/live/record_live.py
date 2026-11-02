"""LIVE-CHECK-20261102.json: the finished hypnosis guide in Joel's post behind hypnosis.u-dont-exist.com.

Joel, 2026-11-02 18:16 UTC: "so are we done now can you update the hypnosis article? hypnosis.u-dont-exist.com" (the
address redirects to https://ibogaqueen.substack.com/p/guide-to-self-hypnosis-and-app-including, post 202810155).

What was done, in the app's browser (his Substack, signed in), the post's editor:
- The live post's words were first compared with the editor copy of 28 September (source/substack-editor-20260928.html):
  the same text blocks but for two embed cards' own text, so he hadn't changed the prose since; but one image (the one
  at the top, fdb94728) was gone from the live post.
- substack_merge.py put the guide (HUMANIZED-SO-FAR.md a789009c) into that editor copy (ARCHIVAL-20261102.html,
  MERGE-REPORT.json: 31,417 words equal to the guide's, 43 links, 8 native objects byte for byte).
- A first try pasted it through the editor's paste (view.pasteHTML, with view.dispatch held), meant to read the parse
  without applying it; Substack's own paste handler applied it anyway, asynchronously, at the top of the draft, so the
  draft held the guide twice for about two minutes (saved 18:29:35 UTC, never published).
- Then one transaction replaced the whole document: the archival HTML parsed with the editor's own schema, the top
  image he had removed left out, and the post's own six native blocks (Subscribe, Share, the YouTube video, the two
  post embeds, the image) carried over as they were in the editor. Its text blocks were checked equal to the archival
  HTML's, the guide appeared once, and the draft saved (18:31:20 UTC). Update, then "Update now", settings untouched.
- The public post, read through Substack's API from the laptop without signing in (POST-AFTER.json), is compared here
  with the guide's text, word for word.

  python3 articles/inner-signal/humanize/fix-20261102/live/record_live.py POST-BEFORE.json POST-AFTER.json
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


def words(t):
    return re.findall(r"[\w’'-]+", t)


def body_words(body):
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', body, flags=re.S)
    return words(html.unescape(re.sub(r'<[^>]+>', ' ', t)))


def main():
    before = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
    after = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding='utf-8'))
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    guide = words(' '.join(b['text'] for b in sr.blocks(md)))
    live = body_words(after['body_html'])
    diffs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=guide, b=live, autojunk=False).get_opcodes():
        if op != 'equal':
            diffs.append({'op': op, 'guide': ' '.join(guide[i1:i2])[:300], 'live': ' '.join(live[j1:j2])[:300]})
    rec = {'about': __doc__.split('\n\n')[2].replace('\n', ' '), 'url': URL, 'post_id': after.get('id'),
           'title': after.get('title'), 'subtitle': after.get('subtitle'), 'audience': after.get('audience'),
           'post_date': after.get('post_date'),
           'before': {'body_html_sha256': hashlib.sha256(before['body_html'].encode('utf-8')).hexdigest(),
                      'words': len(body_words(before['body_html']))},
           'after': {'body_html_sha256': hashlib.sha256(after['body_html'].encode('utf-8')).hexdigest(),
                     'words': len(live)},
           'editor_doc_sha256': {'with the guide twice (never published)': 'a8941fc43ae8df842976806eb71e959c84467aa09ebb81825d5fe3e9cb89c1b9',
                                 'published': '3b8ec9f3046a70b629b1da8eca9fbbb946e44411198148feb2431f66f1f11735'},
           'guide': {'file': 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md',
                     'sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(), 'words': len(guide)},
           'differences': diffs}
    (HERE / 'LIVE-CHECK-20261102.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('guide words', len(guide), '| live words', len(live), '| differences', len(diffs))
    for d in diffs[:20]:
        print(d['op'], '| guide:', d['guide'][:110], '| live:', d['live'][:110])


if __name__ == '__main__':
    main()
