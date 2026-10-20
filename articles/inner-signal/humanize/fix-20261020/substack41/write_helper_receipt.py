"""The delivery receipt for the hypnosis guide's Substack copy page of 2026-10-20 (docs/SUBSTACK-HELPER-DELIVERY-GATE.md,
"Delivery receipt"), read from the files themselves. The page is for a temporary Substack post that Joel makes to run
Substack's free whole-article Pangram check (Joel, 2026-10-20 22:01 UTC: "for very large pangram checks (not just one section,
but like whole article especially) you can just ask me to make a temporary article on substack to check it free"). It is not
the publication merge: question 1 on the questions page (is the 28 September editor HTML the latest) is still open.

Run from the repo root after substack_merge.py, the generator's init, build and verify, and
scripts/test_substack_clipboard_interaction.py:
python3 articles/inner-signal/humanize/fix-20261020/substack41/write_helper_receipt.py [B]

With B: the receipt of part B (make_part_b.py: the archival HTML from "Appendices" on, cut at a top-level block), the rest
of the guide after the first check read only its first 99,999 characters."""
import base64, collections, hashlib, json, pathlib, re, sys

PART = sys.argv[1] if len(sys.argv) > 1 else ''
SUF = '-' + PART if PART else ''

H = pathlib.Path('articles/inner-signal/humanize'); X = H / 'fix-20261020' / 'substack41'
h = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
helper_path = X / ('COPY-TO-SUBSTACK-HYPNOSIS-CHECK%s.html' % SUF)
helper = helper_path.read_text(encoding='utf-8')
man = json.loads(re.search(r'<script id="hva-transfer-manifest" type="application/json">(.*?)</script>', helper, re.S)
                 .group(1).replace('<\\/', '</'))
payload = ''.join(base64.b64decode(s['html_b64']).decode('utf-8') for s in man['segments'])
assert man['editor_body_boundary']['mode'] != 'fragment' and 'contenteditable="true"' not in payload, 'the payload carries the editor root'
merge = json.loads((X / 'MERGE-REPORT-20261020.json').read_text(encoding='utf-8'))
inter = json.loads((X / ('HELPER-INTERACTION-20261020%s.json' % SUF)).read_text(encoding='utf-8'))
assert merge['verdict'] == 'PASS' and inter['status'] == 'pass' and inter['helper_sha256'] == h(helper_path)
plan = json.loads((X / ('TRANSFER-PLAN-20261020%s.json' % SUF)).read_text(encoding='utf-8'))
types = [o.get('type') for o in plan.get('objects', [])] if PART else merge['objects']['types']
raw = H / 'source' / 'substack-editor-20260928.html'
rec = {
 'format': 'substack-helper-delivery-receipt-v1',
 'protocol': 'docs/SUBSTACK-HELPER-DELIVERY-GATE.md',
 'article': 'inner-signal (the hypnosis guide)',
 'purpose': 'a temporary Substack post for the free whole-guide Pangram 4.1 check; not the publication merge',
 'why': 'Joel, 2026-10-20 22:01 UTC: "for very large pangram checks (not just one section, but like whole article especially) you '
        'can just ask me to make a temporary article on substack to check it free" '
        '(articles/intentional-communities/candidate/joel-20261020/joel-20261020-2201-message.txt)',
 'raw_editor_html': {'path': str(raw), 'sha256': h(raw), 'from': "Joel's Substack editor paste of 2026-09-28"},
 'master': {'path': str(H / 'HUMANIZED-SO-FAR.md'), 'sha256': h(H / 'HUMANIZED-SO-FAR.md'),
            'note': 'the working copy: every installed section, the four open sections (questions 2 to 4) as published'},
 'published_bridge': {'path': str(H / 'source' / 'published-20260928.md'), 'sha256': h(H / 'source' / 'published-20260928.md')},
 'merge': {'tool': 'tools/humanization/substack_merge.py', 'report': str(X / 'MERGE-REPORT-20261020.json'), 'verdict': merge['verdict'],
           'islands_verify': merge.get('islands_verify'), 'prose_check': merge.get('prose_check'), 'links': merge.get('links'),
           'formatting_carried': dict(collections.Counter(c['how'] for c in merge.get('carried_formatting', []))),
           'line_breaks_not_carried': sum('line breaks not carried' in n for n in merge.get('notes', []))},
 'archival_source': {'path': str(X / ('ARCHIVAL-SUBSTACK-20261020%s.html' % SUF)), 'sha256': h(X / ('ARCHIVAL-SUBSTACK-20261020%s.html' % SUF)),
                     **({'derived_from': {'path': str(X / 'ARCHIVAL-SUBSTACK-20261020.html'), 'sha256': h(X / 'ARCHIVAL-SUBSTACK-20261020.html'),
                                          'how': 'make_part_b.py: the editor body from its top-level block "<h1>Appendices</h1>" to the end, raw-string slice'}}
                        if PART else {})},
 'editor_body': {'sha256': man['editor_body_sha256'], 'boundary_mode': man['editor_body_boundary']['mode']},
 'canonical_generator': {'path': 'project-sources/substack_transfer_helper.py.txt', 'sha256': h('project-sources/substack_transfer_helper.py.txt')},
 'native_object_parser': {'path': 'project-sources/html_islands.py.txt', 'sha256': h('project-sources/html_islands.py.txt')},
 'compatibility_profile': {'path': 'project-sources/CONFIRMED-SUBSTACK-HELPER.json', 'sha256': h('project-sources/CONFIRMED-SUBSTACK-HELPER.json'),
                           'manifest_sha256': man['compatibility_profile_sha256']},
 'helper': {'path': str(helper_path), 'sha256': h(helper_path), 'manifest_format': man['format'],
            'payload_mode': man['payload_mode'], 'segment_count': man['segment_count'], 'manual_native_video_steps': man['native_video_count'],
            'visible_action': 'one "Copy Article" button', 'plan': str(X / ('TRANSFER-PLAN-20261020%s.json' % SUF)),
            'build_report': str(X / ('TRANSFER-REPORT-20261020%s.json' % SUF))},
 'native_objects': {'count': len(types), 'by_type': dict(collections.Counter(types)), 'order': types},
 'canonical_verify': 'PASS: static source and conversion checks (init, build, verify); %d ordered segment(s), %d native-video manual steps'
                     % (man['segment_count'], man['native_video_count']),
 'interaction_test': {'path': str(X / ('HELPER-INTERACTION-20261020%s.json' % SUF)), 'status': inter['status'],
                      'paths': [t['path'] for t in inter['tests']], 'scope': inter['navigation']},
 'destination_status': "pending: Joel's paste into a new, temporary Substack draft (never published), for Substack's Pangram check",
}
(X / ('HELPER-RECEIPT-20261020%s.json' % SUF)).write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('receipt written; helper', rec['helper']['sha256'][:12], 'boundary', rec['editor_body']['boundary_mode'],
      'segments', man['segment_count'])
