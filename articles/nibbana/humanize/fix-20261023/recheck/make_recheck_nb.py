"""Nibbāna's whole-article recheck (2026-10-23): one payload of the working copy (HUMANIZED-SO-FAR.html, Joel's editor HTML
of 2026-10-22 with batch n1's fixes) for a temporary Substack draft, so Pangram's check of the draft reads the article with
the fixes in place while his post stays as it is.

The lane's transfer helper (project-sources/substack_transfer_helper.py.txt) splits the article into four segments at its
three native uploaded videos, which a paste can't carry, and turns each embedded Substack note into its link, which
Substack's editor turns back into the note on paste. The check reads text, and the videos have none, so the four
segments go into one payload: its text is the post's checked text except for the two notes (and an image's caption
line), which come back when the editor rebuilds the notes from their links. TEXT.txt is the payload's text as the check
reads it; EXPECTED.txt is the working copy's, which the rendered draft should match once the notes are rebuilt.

  python3 articles/nibbana/humanize/fix-20261023/recheck/make_recheck_nb.py   (from the repo root)
"""
import base64, hashlib, json, pathlib, re, subprocess, sys, html as _h

R = pathlib.Path(__file__).resolve().parent
H = R.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

GEN = REPO / 'project-sources' / 'substack_transfer_helper.py.txt'
COMPAT = REPO / 'project-sources' / 'CONFIRMED-SUBSTACK-HELPER.json'
sha = lambda b: hashlib.sha256(b).hexdigest()


def run(*args):
    r = subprocess.run([sys.executable] + [str(a) for a in args], capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        raise SystemExit('%s failed:\n%s\n%s' % (args[0], r.stdout[-2000:], r.stderr[-2000:]))
    return r.stdout


def main():
    work = H / 'HUMANIZED-SO-FAR.html'
    plan, helper = R / 'TRANSFER-PLAN.json', R / 'COPY-TO-SUBSTACK-NIBBANA-RECHECK.html'
    run(GEN, 'init', work, '--plan', plan, '--compat-profile', COMPAT)
    run(GEN, 'build', work, '--plan', plan, '--compat-profile', COMPAT, '--out', helper, '--report', R / 'TRANSFER-REPORT.json')
    run(GEN, 'verify', work, '--plan', plan, '--compat-profile', COMPAT, '--helper', helper)
    raw = helper.read_text(encoding='utf-8')
    man = json.loads(re.search(r'<script id="hva-transfer-manifest" type="application/json">(.*?)</script>', raw, re.S)
                     .group(1).replace('<\\/', '</'))
    segs = [base64.b64decode(s['html_b64']).decode('utf-8') for s in man['segments']]
    payload = ''.join(segs)
    (R / 'PAYLOAD.html').write_text(payload, encoding='utf-8')
    text = '\n'.join(C.checked_text(s) for s in segs)
    (R / 'TEXT.txt').write_text(text, encoding='utf-8')
    expected = C.checked_text(work.read_text(encoding='utf-8'))
    (R / 'EXPECTED.txt').write_text(expected, encoding='utf-8')
    # What the draft will show (2026-10-23, E233): Substack's editor makes a run of spaces single on paste, and splits an
    # image gallery into single images with its caption as a paragraph of its own, which the post's check never reads. So
    # DRAFT-TEXT.txt is EXPECTED.txt with single spaces, and each gallery caption is printed, to be deleted in the draft
    # before the rendered check.
    draft_text = '\n'.join(re.sub(r' {2,}', ' ', x) for x in expected.split('\n'))
    (R / 'DRAFT-TEXT.txt').write_text(draft_text, encoding='utf-8')
    for cap in re.findall(r'class="image-gallery-embed".*?<figcaption[^>]*>(.*?)</figcaption>', payload, re.S):
        print('a gallery caption the editor will turn into a paragraph (delete it in the draft):', _h.unescape(cap))
    straight = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
    words = re.sub(r'</?(?:a|em|strong|b|i|u|s|span|code|sup|sub)\b[^>]*>', '', payload)
    words = _h.unescape(re.sub(r'<[^>]+>', ' ', words)).translate(straight).split()
    out = {'segments': len(segs), 'payload_sha256': sha(payload.encode('utf-8')), 'payload_chars': len(payload),
           'text_sha256': sha(text.encode('utf-8')), 'text_chars': len(text),
           'expected_sha256': sha(expected.encode('utf-8')), 'expected_chars': len(expected),
           'draft_text_sha256': sha(draft_text.encode('utf-8')), 'draft_text_chars': len(draft_text),
           'words': len(words), 'words_sha256': sha(' '.join(words).encode('utf-8')),
           'working_copy_sha256': sha(work.read_bytes())}
    (R / 'RECHECK-BUILD.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
