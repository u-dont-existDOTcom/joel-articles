"""The copy helper for Joel's community post (2026-10-25, after his message of 00:27 UTC: the link of the new version's
first whole-article check, which read Human Written with 0 of 72 windows AI; the handoff's next step: "When it reads
Human: ... the copy helper for his post").

docs/SUBSTACK-HELPER-DELIVERY-GATE.md: the canonical generator with the compatibility profile, init, build and verify on
the working copy (../../joel-20261024/answer65/WORKING.html: his editor HTML of 2026-10-20 with 57 to 65 and his kibbutz
image), against the recheck's helper (../../joel-20261024/recheck/COPY-TO-SUBSTACK-COMMUNITY-RECHECK.html, the same
generator on the same file, pasted into the temporary draft and rendered to the checked text exactly), then
scripts/test_substack_clipboard_interaction.py and the receipt. One more check: the helper's text is the text Pangram read.
Everything goes to articles/intentional-communities/exports/.

  python3 articles/intentional-communities/candidate/joel-20261025/helper/make_helper.py   (from the repo root)
"""
import base64, hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parents[1]
A = CAND.parent
REPO = A.parents[1]
X = A / 'exports'
GEN = REPO / 'project-sources' / 'substack_transfer_helper.py.txt'
COMPAT = REPO / 'project-sources' / 'CONFIRMED-SUBSTACK-HELPER.json'
WORK = CAND / 'joel-20261024' / 'answer65' / 'WORKING.html'
RECHECK = CAND / 'joel-20261024' / 'recheck'
BASE = RECHECK / 'COPY-TO-SUBSTACK-COMMUNITY-RECHECK.html'
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def run(*args):
    r = subprocess.run([sys.executable] + [str(a) for a in args], capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        raise SystemExit('%s failed:\n%s\n%s' % (args[0], r.stdout[-3000:], r.stderr[-3000:]))
    return r.stdout


def main():
    plan, helper = X / 'TRANSFER-PLAN-20261025.json', X / 'COPY-TO-SUBSTACK.html'
    report, inter = X / 'TRANSFER-REPORT-20261025.md', X / 'HELPER-INTERACTION-20261025.json'
    run(GEN, 'init', WORK, '--plan', plan, '--compat-profile', COMPAT)
    run(GEN, 'build', WORK, '--plan', plan, '--compat-profile', COMPAT, '--out', helper, '--report', report, '--against', BASE)
    verify = run(GEN, 'verify', WORK, '--plan', plan, '--compat-profile', COMPAT, '--helper', helper, '--against', BASE)
    run(REPO / 'scripts' / 'test_substack_clipboard_interaction.py', helper, '--out', inter)
    raw = helper.read_text(encoding='utf-8')
    man = json.loads(re.search(r'<script id="hva-transfer-manifest" type="application/json">(.*?)</script>', raw, re.S)
                     .group(1).replace('<\\/', '</'))
    segs = [base64.b64decode(s['html_b64']).decode('utf-8') for s in man['segments']]
    assert man['editor_body_boundary']['mode'] != 'fragment' and not any('contenteditable="true"' in s for s in segs), \
        'the payload carries the editor root'
    # the helper's text is the text Pangram read (the recheck's DRAFT-TEXT.txt, single spaces), and its payload the one
    # that was pasted into the draft
    sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
    import substack_check_text as C
    text = '\n'.join(re.sub(r' {2,}', ' ', x) for x in '\n'.join(C.checked_text(s) for s in segs).split('\n'))
    checked = (RECHECK / 'DRAFT-TEXT.txt').read_text(encoding='utf-8')
    assert text == checked, 'the helper\'s text is not the text Pangram read'
    same_payload = ''.join(segs) == (RECHECK / 'PAYLOAD.html').read_text(encoding='utf-8')
    it = json.loads(inter.read_text(encoding='utf-8'))
    assert it.get('status') == 'pass' and it.get('helper_sha256') == sha(helper), 'the interaction test'
    rec = {
        'format': 'substack-helper-delivery-receipt-v1',
        'protocol': 'docs/SUBSTACK-HELPER-DELIVERY-GATE.md',
        'article': 'intentional-communities',
        'why': 'Joel, 2026-10-25 00:27 UTC: the new version\'s first whole-article check (feed 954042b6) read Human Written, '
               '0 of 72 windows AI; the copy helper for his post was the next step',
        'archival_source': {'path': str(WORK.relative_to(REPO)), 'sha256': sha(WORK),
                            'from': 'his editor HTML of 2026-10-20 (candidate/joel-20261020/community-final-substack-20261020.html) '
                                    'with 57 to 63 (restructure/make_working.py), 64 (apply_64.py), 65 and his kibbutz image '
                                    '(answer65/apply_65.py)'},
        'editor_body': {'sha256': man['editor_body_sha256'], 'boundary_mode': man['editor_body_boundary']['mode']},
        'canonical_generator': {'path': str(GEN.relative_to(REPO)), 'sha256': sha(GEN)},
        'native_object_parser': {'path': 'project-sources/html_islands.py.txt', 'sha256': sha(REPO / 'project-sources' / 'html_islands.py.txt')},
        'compatibility_profile': {'path': str(COMPAT.relative_to(REPO)), 'sha256': sha(COMPAT),
                                  'manifest_sha256': man.get('compatibility_profile_sha256')},
        'helper': {'path': str(helper.relative_to(REPO)), 'sha256': sha(helper), 'manifest_format': man['format'],
                   'payload_mode': man['payload_mode'], 'segment_count': man['segment_count'],
                   'manual_native_video_steps': man['native_video_count'], 'plan': str(plan.relative_to(REPO)),
                   'build_report': str(report.relative_to(REPO))},
        'regression_baseline': {'path': str(BASE.relative_to(REPO)), 'sha256': sha(BASE),
                                'why': 'the recheck\'s helper from the same generator and file: its payload was pasted into the '
                                       'temporary draft and rendered to the checked text exactly'},
        'verify': verify.strip()[-2000:],
        'checked_text': {'equals': str((RECHECK / 'DRAFT-TEXT.txt').relative_to(REPO)), 'sha256': sha(RECHECK / 'DRAFT-TEXT.txt'),
                         'pangram': 'https://www.pangram.com/feed/954042b6-e624-4c7f-87d7-db15c547d5c8',
                         'payload_same_as_the_pasted_one': same_payload},
        'interaction_test': {'path': str(inter.relative_to(REPO)), 'status': it.get('status')},
        'destination_test': 'its payload, pasted into the temporary draft (221977934) with the lane\'s paste script, rendered '
                            'to the checked text exactly (../../joel-20261024/recheck/RECHECK-POST.json). Not tested by me: the '
                            'Copy button in Opera, and his post.',
    }
    (X / 'HELPER-RECEIPT-20261025.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: rec[k] for k in ('helper', 'checked_text')}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
