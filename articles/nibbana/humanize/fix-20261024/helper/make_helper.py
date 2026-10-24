"""The copy helper for Joel's Nibbāna post (2026-10-24, after his message of 19:52 UTC: his GPT edit saved as batch n8, and
the eighth recheck read 100% Human; the earlier next step: "When Nibbāna reads Human: the clipboard helper for his post,
with N5 for him to decide there").

docs/SUBSTACK-HELPER-DELIVERY-GATE.md: the canonical generator (project-sources/substack_transfer_helper.py.txt) with the
compatibility profile, run through init, build and verify on the working copy (HUMANIZED-SO-FAR.html: his editor HTML of
2026-10-22, the native-object authority, with every batch's text in it), against the eighth recheck's helper, which was
pasted into the temporary draft and rendered to its expected text (the destination test), then
scripts/test_substack_clipboard_interaction.py and the receipt. Everything goes to articles/nibbana/exports/.

  python3 articles/nibbana/humanize/fix-20261024/helper/make_helper.py   (from the repo root)
"""
import base64, hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
A = H.parent
REPO = A.parents[1]
X = A / 'exports'
GEN = REPO / 'project-sources' / 'substack_transfer_helper.py.txt'
COMPAT = REPO / 'project-sources' / 'CONFIRMED-SUBSTACK-HELPER.json'
BASE = H / 'fix-20261023' / 'recheck8' / 'COPY-TO-SUBSTACK-NIBBANA-RECHECK.html'
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})


def run(*args):
    r = subprocess.run([sys.executable] + [str(a) for a in args], capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        raise SystemExit('%s failed:\n%s\n%s' % (args[0], r.stdout[-3000:], r.stderr[-3000:]))
    return r.stdout


def main():
    X.mkdir(exist_ok=True)
    work = H / 'HUMANIZED-SO-FAR.html'
    plan, helper = X / 'TRANSFER-PLAN-20261024.json', X / 'COPY-TO-SUBSTACK.html'
    report, inter = X / 'TRANSFER-REPORT-20261024.md', X / 'HELPER-INTERACTION-20261024.json'  # the generator's report is Markdown
    run(GEN, 'init', work, '--plan', plan, '--compat-profile', COMPAT)
    run(GEN, 'build', work, '--plan', plan, '--compat-profile', COMPAT, '--out', helper, '--report', report, '--against', BASE)
    verify = run(GEN, 'verify', work, '--plan', plan, '--compat-profile', COMPAT, '--helper', helper, '--against', BASE)
    run(REPO / 'scripts' / 'test_substack_clipboard_interaction.py', helper, '--out', inter)
    raw = helper.read_text(encoding='utf-8')
    man = json.loads(re.search(r'<script id="hva-transfer-manifest" type="application/json">(.*?)</script>', raw, re.S)
                     .group(1).replace('<\\/', '</'))
    payload = ''.join(base64.b64decode(s['html_b64']).decode('utf-8') for s in man['segments'])
    assert man['editor_body_boundary']['mode'] != 'fragment' and 'contenteditable="true"' not in payload, \
        'the payload carries the editor root'
    # the helper carries his GPT edit: each of batch n8's paragraphs is in the parts' text in its new form, none in its old
    sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
    import substack_check_text as C
    flat = lambda t: ' '.join(t.translate(STRAIGHT).split())
    text = flat(' '.join(C.checked_text(base64.b64decode(s['html_b64']).decode('utf-8')) for s in man['segments']))
    n8 = json.loads((H / 'fix-20261024' / 'n8' / 'EDITS-n8.json').read_text(encoding='utf-8'))
    found = sum(flat(e['new']) in text for e in n8)
    stale = [e['old'][:60] for e in n8 if flat(e['old']) in text]
    assert found == len(n8) and not stale, ('the GPT edit is not all in the helper', found, len(n8), stale)
    it = json.loads(inter.read_text(encoding='utf-8'))
    assert it.get('status') == 'pass' and it.get('helper_sha256') == sha(helper), 'the interaction test'
    rec = {
        'format': 'substack-helper-delivery-receipt-v1',
        'protocol': 'docs/SUBSTACK-HELPER-DELIVERY-GATE.md',
        'article': 'nibbana',
        'why': 'Joel, 2026-10-24 19:52 UTC: his GPT edit saved (batch n8, "so save the result"); the eighth recheck read '
               '100% Human (feed 355a29d0); N5 he decides at this helper ("i\'ll look at it later when youu give me the '
               'clipboard helper", 2026-10-23 22:29 UTC)',
        'archival_source': {'path': str(work.relative_to(REPO)), 'sha256': sha(work),
                            'from': "his editor HTML of 2026-10-22 (humanize/source/substack-editor-20261022.html) with "
                                    "every batch's text, n1 to n8 (fix-20261023/n1/install_n1.py)"},
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
                                'why': 'the eighth recheck\'s helper from the same generator: its four parts were pasted into the '
                                       'temporary draft, rendered to the expected text, and read 100% Human'},
        'verify': verify.strip()[-2000:],
        'gpt_edit_in_helper': {'paragraphs': len(n8), 'new_text_found': found, 'old_text_found': len(stale),
                               'from': 'fix-20261024/n8/EDITS-n8.json'},
        'interaction_test': {'path': str(inter.relative_to(REPO)), 'status': it.get('status')},
        'destination_test': 'pending, in his post. What has been tested: the four parts of the eighth recheck\'s helper (the same '
                            'generator on the same editor HTML) were pasted into the temporary draft with the lane\'s paste '
                            'script, and the preview read back to the expected text (fix-20261023/recheck8/RECHECK-POST.json). '
                            'Not tested by me: the Copy buttons in Opera, and the three video steps, which he does by hand.',
    }
    (X / 'HELPER-RECEIPT-20261024.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({k: rec[k] for k in ('helper', 'verify')}, ensure_ascii=False, indent=1)[:2500])


if __name__ == '__main__':
    main()
