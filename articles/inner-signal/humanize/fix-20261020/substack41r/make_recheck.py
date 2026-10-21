"""The whole guide's 4.1 recheck through a temporary Substack post (2026-10-21): the copy payloads for parts A and B.

The first check (../substack41/, 2026-10-20) read the guide in two parts because Substack's Pangram check reads at most the
first 99,999 characters of a post: part A is the whole guide (the check stops inside Appendix B), part B starts at
"Appendices". This builds the same two parts from the working copy as it is now (HUMANIZED-SO-FAR.md with the 4.1 edits,
../apply_edits41.py), the same way: tools/humanization/substack_merge.py into Joel's editor HTML of 28 September, part B
cut at the "Appendices" h1 by raw-string slicing, then the canonical generator (project-sources/substack_transfer_helper.py.txt
init, build, verify) and the clipboard test (scripts/test_substack_clipboard_interaction.py) on each copy page.

Since Joel's message of 23:54 UTC ("you can automate this method yourself"), I paste the copy page's payload into a new
Substack draft myself, in the desktop app's browser: PAYLOAD-A.html and PAYLOAD-B.html are the HTML each copy page puts on
the clipboard (its manifest's segments, decoded), and paste_payload.js pastes one into the editor as a paste event
carrying that HTML, after checking its SHA-256. Never Publish.

  python3 articles/inner-signal/humanize/fix-20261020/substack41r/make_recheck.py   (from the repo root)
"""
import base64, hashlib, json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
H = REPO / 'articles' / 'inner-signal' / 'humanize'
X = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'tools'))
import substack_merge as SM  # noqa: E402
import sections as S  # noqa: E402

DATE = '20261021'
GEN = REPO / 'project-sources' / 'substack_transfer_helper.py.txt'
COMPAT = REPO / 'project-sources' / 'CONFIRMED-SUBSTACK-HELPER.json'
sha = lambda b: hashlib.sha256(b).hexdigest()


def run(*args):
    r = subprocess.run([sys.executable] + [str(a) for a in args], capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        raise SystemExit('%s failed:\n%s\n%s' % (args[0], r.stdout[-2000:], r.stderr[-2000:]))
    return r.stdout


def main():
    applied = run(H / 'fix-20261020' / 'apply_edits41.py', '--check')
    assert 'applied now: none' in applied, applied
    archival = X / ('ARCHIVAL-SUBSTACK-%s.html' % DATE)
    run(REPO / 'tools' / 'humanization' / 'substack_merge.py', '--editor', H / 'source' / 'substack-editor-20260928.html',
        '--master', H / 'HUMANIZED-SO-FAR.md', '--published', H / 'source' / 'published-20260928.md', '--out', archival,
        '--report', X / ('MERGE-REPORT-%s.json' % DATE))
    merge = json.loads((X / ('MERGE-REPORT-%s.json' % DATE)).read_text(encoding='utf-8'))
    assert merge['verdict'] == 'PASS', merge.get('failures')
    src = archival.read_text(encoding='utf-8')
    open_end, close_start = src.index('>') + 1, src.rindex('</div>')
    blocks = SM.top_blocks(src[open_end:close_start])
    assert ''.join(blocks) == src[open_end:close_start]
    k = blocks.index('<h1>Appendices</h1>')
    archival_b = X / ('ARCHIVAL-SUBSTACK-%s-B.html' % DATE)
    archival_b.write_text(src[:open_end] + ''.join(blocks[k:]) + src[close_start:], encoding='utf-8')
    out = {}
    for part, arch in (('A', archival), ('B', archival_b)):
        suf = '' if part == 'A' else '-B'
        plan = X / ('TRANSFER-PLAN-%s%s.json' % (DATE, suf))
        helper = X / ('COPY-TO-SUBSTACK-HYPNOSIS-RECHECK%s.html' % suf)
        run(GEN, 'init', arch, '--plan', plan, '--compat-profile', COMPAT)
        run(GEN, 'build', arch, '--plan', plan, '--compat-profile', COMPAT, '--out', helper,
            '--report', X / ('TRANSFER-REPORT-%s%s.json' % (DATE, suf)))
        run(GEN, 'verify', arch, '--plan', plan, '--compat-profile', COMPAT, '--helper', helper)
        inter = X / ('HELPER-INTERACTION-%s%s.json' % (DATE, suf))
        run(REPO / 'scripts' / 'test_substack_clipboard_interaction.py', helper, '--out', inter)
        assert json.loads(inter.read_text(encoding='utf-8'))['status'] == 'pass'
        raw = helper.read_text(encoding='utf-8')
        man = json.loads(re.search(r'<script id="hva-transfer-manifest" type="application/json">(.*?)</script>', raw, re.S)
                         .group(1).replace('<\\/', '</'))
        assert len(man['segments']) == 1, 'more than one segment: a manual native step would be needed'
        payload = base64.b64decode(man['segments'][0]['html_b64'])
        (X / ('PAYLOAD-%s.html' % part)).write_bytes(payload)
        out[part] = {'archival': str(arch.relative_to(REPO)), 'archival_sha256': sha(arch.read_bytes()),
                     'helper': str(helper.relative_to(REPO)), 'helper_sha256': sha(helper.read_bytes()),
                     'payload': 'PAYLOAD-%s.html' % part, 'payload_sha256': sha(payload), 'payload_chars': len(payload)}
    # the text Pangram reads, for the predictions: the guide's sections from the working copy
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    secs = S.sections(md, str(H / 'source' / 'substack-editor-20260928.html'))
    texts = [S.text_of(bl) for _, bl in secs]
    heads = [h for h, _ in secs]
    kb = heads.index('# Appendices')
    (X / 'WHOLE-GUIDE-41r-A.txt').write_text('\n\n'.join(texts), encoding='utf-8')
    (X / 'WHOLE-GUIDE-41r-B.txt').write_text('\n\n'.join(texts[kb:]), encoding='utf-8')
    out['master_sha256'] = sha((H / 'HUMANIZED-SO-FAR.md').read_bytes())
    out['merge'] = {'verdict': merge['verdict'], 'report': 'MERGE-REPORT-%s.json' % DATE}
    (X / 'RECHECK-BUILD.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
