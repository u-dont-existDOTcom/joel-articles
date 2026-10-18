"""The delivery receipt for the community article's Substack copy helper (docs/SUBSTACK-HELPER-DELIVERY-GATE.md, "Delivery
receipt"): every identity, hash and check result the gate asks for, read from the files themselves. Run from the repo root after
substack_merge.py, the generator's init, build and verify, and scripts/test_substack_clipboard_interaction.py:
python3 articles/intentional-communities/candidate/fix-20261018/write_helper_receipt.py"""
import base64, collections, hashlib, json, pathlib, re

A = pathlib.Path('articles/intentional-communities'); X = A / 'exports'
h = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
helper = (X / 'COPY-TO-SUBSTACK.html').read_text(encoding='utf-8')
man = json.loads(re.search(r'<script id="hva-transfer-manifest" type="application/json">(.*?)</script>', helper, re.S).group(1).replace('<\\/', '</'))
payload = ''.join(base64.b64decode(s['html_b64']).decode('utf-8') for s in man['segments'])
assert man['editor_body_boundary']['mode'] != 'fragment' and 'contenteditable="true"' not in payload, 'the payload carries the editor root'
merge = json.loads((X / 'MERGE-REPORT-20261018.json').read_text(encoding='utf-8'))
inter = json.loads((X / 'HELPER-INTERACTION-20261018.json').read_text(encoding='utf-8'))
assert merge['verdict'] == 'PASS' and inter['status'] == 'pass' and inter['helper_sha256'] == h(X / 'COPY-TO-SUBSTACK.html')
types = merge['objects']['types']
raw = A / 'candidate/joel-20261018/substack-editor-20261018-0129.html'
rec = {
 'format': 'substack-helper-delivery-receipt-v1',
 'protocol': 'docs/SUBSTACK-HELPER-DELIVERY-GATE.md',
 'article': 'intentional-communities',
 'why': 'Joel, 2026-10-18 01:29 UTC: "merge the final article into the substack html. i\'m pasting the latest one i have. use the '
        'validated clipboard helper to give me a copy button" (candidate/joel-20261018/joel-20261018-0129-message.txt)',
 'raw_editor_html': {'path': str(raw), 'sha256': h(raw), 'from': "Joel's paste of 2026-10-18 01:29 UTC"},
 'master': {'path': str(A / 'master.md'), 'sha256': h(A / 'master.md')},
 'published_bridge': {'path': str(A / 'original.md'), 'sha256': h(A / 'original.md')},
 'merge': {'tool': 'tools/humanization/substack_merge.py', 'report': str(X / 'MERGE-REPORT-20261018.json'), 'verdict': merge['verdict'],
           'islands_verify': merge.get('islands_verify'), 'prose_check': merge.get('prose_check'), 'links': merge.get('links'),
           'formatting_carried': dict(collections.Counter(c['how'] for c in merge.get('carried_formatting', [])))},
 'archival_source': {'path': str(X / 'ARCHIVAL-SUBSTACK-20261018.html'), 'sha256': h(X / 'ARCHIVAL-SUBSTACK-20261018.html')},
 'editor_body': {'sha256': man['editor_body_sha256'], 'boundary_mode': man['editor_body_boundary']['mode']},
 'canonical_generator': {'path': 'project-sources/substack_transfer_helper.py.txt', 'sha256': h('project-sources/substack_transfer_helper.py.txt')},
 'native_object_parser': {'path': 'project-sources/html_islands.py.txt', 'sha256': h('project-sources/html_islands.py.txt'),
                          'note': '2026-10-18 repair: the current editor root (data-testid="editor", class "tiptap ProseMirror") is the editor body (test in tests/test_html_islands_current_substack_shapes.py)'},
 'compatibility_profile': {'path': 'project-sources/CONFIRMED-SUBSTACK-HELPER.json', 'sha256': h('project-sources/CONFIRMED-SUBSTACK-HELPER.json'),
                           'manifest_sha256': man['compatibility_profile_sha256']},
 'helper': {'path': str(X / 'COPY-TO-SUBSTACK.html'), 'sha256': h(X / 'COPY-TO-SUBSTACK.html'), 'manifest_format': man['format'],
            'payload_mode': man['payload_mode'], 'segment_count': man['segment_count'], 'manual_native_video_steps': man['native_video_count'],
            'visible_action': 'one "Copy Article" button', 'plan': str(X / 'TRANSFER-PLAN-20261018.json'),
            'build_report': str(X / 'TRANSFER-REPORT-20261018.json')},
 'native_objects': {'count': len(types), 'by_type': dict(collections.Counter(types)), 'order': types},
 'canonical_verify': 'PASS: static source and conversion checks (init, build, verify); 1 ordered segment, 0 native-video manual steps',
 'interaction_test': {'path': str(X / 'HELPER-INTERACTION-20261018.json'), 'status': inter['status'],
                      'paths': [t['path'] for t in inter['tests']], 'scope': inter['navigation']},
 'destination_status': "pending: Joel's paste into a Substack draft in Opera (the images, the three post embeds, the two YouTube "
                       "videos, Share and Subscribe to be checked there)",
 'manual_steps_for_joel': ['Upload the PsyPost screenshot (candidate/images/psypost-relational-mobility.png) in section 12, "The Math of '
                           'Absorption, and Who This Isn\'t For", after the paragraph that starts "This doesn\'t surprise me, since we\'re '
                           'taught to put on a show of competence", with the caption It\'s kind of a "no, duh" study. (the link on "study": '
                           'https://www.psypost.org/social-freedom-shapes-whose-version-of-reality-you-adopt-new-research-suggests/), and the '
                           'image linked to the same page.'],
}
(X / 'HELPER-RECEIPT-20261018.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('receipt written; helper', rec['helper']['sha256'][:12], 'boundary', rec['editor_body']['boundary_mode'])
