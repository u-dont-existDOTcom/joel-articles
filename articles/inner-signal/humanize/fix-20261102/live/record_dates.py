"""DATES-20261102.json: the "Last update" dates in Joel's two posts, after his answer of 2026-11-02 19:11 UTC.

His words (`../joel-20261102-1911-message.txt`): "29a yes you can always update that date when updating a post of course".
Question 29 a) was the hypnosis guide's subtitle, "Last update: Sept 16, 2026, v. 6.1" to "Last update: Nov 2, 2026,
v. 7.0". "you can always update that date when updating a post" is a standing rule (gate E323), so the community post,
updated today twice (his six card edits and his fix of question 67), had its title's "Updated: Nov 1 2026" made "Updated:
Nov 2 2026" too.

How, in the app's browser (his Substack, signed in), each post's editor: the subtitle or title box set with its own value
setter and an input event, the draft saved by the editor, the saved draft's body compared with the published body, then
Update and "Update now". The hypnosis draft's body stayed equal to the published one. The community draft's body gained one
attribute, "cover_image_crop": null, in three post embeds: the editor's current default for that node, nothing a reader
sees; the published HTML differs from the copy read after question 67 (`inbox/ic-live-20261102b/post.json` on the laptop)
only there, so its words are unchanged. Both posts were then read through Substack's public API from the laptop without
signing in (POST-DATES-HYPNOSIS.json, POST-DATES-COMMUNITY.json), and this script checks them.

  python3 articles/inner-signal/humanize/fix-20261102/live/record_dates.py
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
HYP_NEW = "You won't find a hypnosis guide like this anywhere. Last update: Nov 2, 2026, v. 7.0"
HYP_OLD = "You won't find a hypnosis guide like this anywhere. Last update: Sept 16, 2026, v. 6.1"
COM_NEW = 'Building Healing Community "Escuelitas" to Save The World 🫶🏿🌍🫶🏿 Updated: Nov 2 2026'
COM_OLD = 'Building Healing Community "Escuelitas" to Save The World 🫶🏿🌍🫶🏿 Updated: Nov 1 2026'
COM_BEFORE_SHA = 'c804501598df41646370af9dde760dac6718d448009fe84a0cc0b8d4688a09c1'   # LIVE-CHECK-Q67.json's post


def sha(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def main():
    hyp = json.loads((HERE / 'POST-DATES-HYPNOSIS.json').read_text(encoding='utf-8'))
    com = json.loads((HERE / 'POST-DATES-COMMUNITY.json').read_text(encoding='utf-8'))
    after = json.loads((HERE / 'POST-AFTER.json').read_text(encoding='utf-8'))
    assert hyp['subtitle'] == HYP_NEW and after['subtitle'] == HYP_OLD
    assert sha(hyp['body_html']) == sha(after['body_html']), 'the hypnosis post body changed'
    assert com['title'] == COM_NEW
    body = com['body_html']
    assert body.count('&quot;cover_image_crop&quot;:null,') == 3
    assert sha(body.replace('&quot;cover_image_crop&quot;:null,', '')) == COM_BEFORE_SHA, 'more than the embeds changed'
    rec = {'about': __doc__.split('\n\n')[1].replace('\n', ' '),
           'hypnosis': {'url': 'https://ibogaqueen.substack.com/p/guide-to-self-hypnosis-and-app-including', 'post_id': hyp['id'],
                        'subtitle': {'before': HYP_OLD, 'after': HYP_NEW},
                        'body_html_sha256': sha(hyp['body_html']), 'body': 'unchanged (as in POST-AFTER.json)'},
           'community': {'url': 'https://ibogaqueen.substack.com/p/building-healing-community-escuelitas', 'post_id': com['id'],
                         'title': {'before': COM_OLD, 'after': COM_NEW},
                         'body_html_sha256': {'before': COM_BEFORE_SHA, 'after': sha(body)},
                         'body': ('the words unchanged; three post embeds\' data gained "cover_image_crop": null, the editor\'s '
                                  'default, and without it the HTML is the copy read after question 67, byte for byte')}}
    (HERE / 'DATES-20261102.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('hypnosis subtitle and community title live; bodies as recorded')


if __name__ == '__main__':
    main()
