"""The community article's first whole-article recheck since his post went up (2026-10-24, after Joel's message of 23:40
UTC, which answered 65, the last open question): one payload of the new version (../answer65/WORKING.html: his editor
HTML of 2026-10-20 with 57 to 63, the move into essay and How-To Manual, his 64 and 65 cuts, and his kibbutz image) for a
temporary Substack draft, so Pangram's check of the draft reads the whole article while his post stays as it is.

Built the way Nibbāna's rechecks are (articles/nibbana/humanize/fix-20261023/recheck8/make_recheck_nb.py): the lane's
transfer helper (project-sources/substack_transfer_helper.py.txt) splits the article at its native uploaded videos, which
a paste can't carry; PAYLOAD.html is its parts joined. TEXT.txt is the payload's text as the check reads it, EXPECTED.txt
the working copy's, and DRAFT-TEXT.txt what the draft will show (single spaces; E233), which the rendered draft should
match once any gallery caption printed below is deleted.

  python3 articles/intentional-communities/candidate/joel-20261024/recheck/make_recheck_ic.py   (from the repo root)
"""
import base64, hashlib, json, pathlib, re, subprocess, sys, html as _h

R = pathlib.Path(__file__).resolve().parent
REPO = R.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

WORK = R.parent / 'answer65' / 'WORKING.html'
GEN = REPO / 'project-sources' / 'substack_transfer_helper.py.txt'
COMPAT = REPO / 'project-sources' / 'CONFIRMED-SUBSTACK-HELPER.json'
sha = lambda b: hashlib.sha256(b).hexdigest()


def run(*args):
    r = subprocess.run([sys.executable] + [str(a) for a in args], capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        raise SystemExit('%s failed:\n%s\n%s' % (args[0], r.stdout[-2000:], r.stderr[-2000:]))
    return r.stdout


def main():
    plan, helper = R / 'TRANSFER-PLAN.json', R / 'COPY-TO-SUBSTACK-COMMUNITY-RECHECK.html'
    run(GEN, 'init', WORK, '--plan', plan, '--compat-profile', COMPAT)
    run(GEN, 'build', WORK, '--plan', plan, '--compat-profile', COMPAT, '--out', helper, '--report', R / 'TRANSFER-REPORT.md')
    verify = run(GEN, 'verify', WORK, '--plan', plan, '--compat-profile', COMPAT, '--helper', helper)
    raw = helper.read_text(encoding='utf-8')
    man = json.loads(re.search(r'<script id="hva-transfer-manifest" type="application/json">(.*?)</script>', raw, re.S)
                     .group(1).replace('<\\/', '</'))
    assert man['editor_body_boundary']['mode'] != 'fragment'
    segs = [base64.b64decode(s['html_b64']).decode('utf-8') for s in man['segments']]
    payload = ''.join(segs)
    assert 'contenteditable="true"' not in payload
    (R / 'PAYLOAD.html').write_text(payload, encoding='utf-8')
    text = '\n'.join(C.checked_text(s) for s in segs)
    (R / 'TEXT.txt').write_text(text, encoding='utf-8')
    expected = C.checked_text(WORK.read_text(encoding='utf-8'))
    (R / 'EXPECTED.txt').write_text(expected, encoding='utf-8')
    draft_text = '\n'.join(re.sub(r' {2,}', ' ', x) for x in expected.split('\n'))
    (R / 'DRAFT-TEXT.txt').write_text(draft_text, encoding='utf-8')
    captions = [_h.unescape(re.sub(r'<[^>]+>', '', c)).strip()
                for c in re.findall(r'class="image-gallery-embed".*?<figcaption[^>]*>(.*?)</figcaption>', payload, re.S)]
    for cap in captions:
        print('a gallery caption the editor will turn into a paragraph (delete it in the draft):', cap)
    straight = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
    words = re.sub(r'</?(?:a|em|strong|b|i|u|s|span|code|sup|sub)\b[^>]*>', '', payload)
    words = _h.unescape(re.sub(r'<[^>]+>', ' ', words)).translate(straight).split()
    out = {'segments': len(segs), 'native_videos': man.get('native_video_count'), 'verify': verify.strip()[-400:],
           'payload_sha256': sha(payload.encode('utf-8')), 'payload_chars': len(payload),
           'text_sha256': sha(text.encode('utf-8')), 'text_chars': len(text),
           'expected_sha256': sha(expected.encode('utf-8')), 'expected_chars': len(expected),
           'draft_text_sha256': sha(draft_text.encode('utf-8')), 'draft_text_chars': len(draft_text),
           'words': len(words), 'words_sha256': sha(' '.join(words).encode('utf-8')),
           'gallery_captions': captions, 'working_copy_sha256': sha(WORK.read_bytes())}
    assert len(draft_text) <= 99999, 'longer than the check reads: split it in two parts'
    (R / 'RECHECK-BUILD.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
