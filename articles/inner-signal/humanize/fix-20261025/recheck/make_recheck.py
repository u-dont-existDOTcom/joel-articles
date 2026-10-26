"""The whole guide's recheck after Joel's answers of 2026-10-25 (his message of 23:05 UTC: question 20, the Emulate check
page, with his answers file): the payloads for parts A and B from the working copy as it is now, built as
../../fix-20261023/recheck-a4/make_recheck.py built the last ones (part A's recheck 4, read Human Written; part B's
recheck 2), into this folder. Since those checks the guide has his review-page answers of 19:42 UTC
(../review/APPLIED.json), the strict Emulate check's fixes (../emulate-check/: fix_typos.py, fix_citations.py and the
spaces), his answers to question 20 (../emulate-check/APPLIED-20.json) and the guard sweep (../emulate-check/GUARD-SWEEP.json).

The earlier builder first ran ../../fix-20261020/apply_edits41.py --check and required "applied now: none". That check now
stops at HG35-forgive-e3, whose new words his answers have since replaced (the forgiveness paragraph is his IC-alignment
version); every other batch-41 edit is in or superseded the same way, so this builder doesn't run it.

What it writes: each payload's checked text (TEXT-A.txt, TEXT-B.txt, rebuilt by tools/humanization/substack_check_text.py,
with their SHA-256), so the rendered post can be hashed against it after the paste; and each payload's editor words with
their SHA-256 (WORDS-A.json, WORDS-B.json) for the lane's paste helper (../../fix-20261022/screen/paste_payload_lane.js).
Part A's check reads at most its first 99,999 characters; TEXT-A.txt is cut there, as the check cuts it.

  python3 articles/inner-signal/humanize/fix-20261025/recheck/make_recheck.py   (from the repo root)
"""
import base64, hashlib, json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
H = REPO / 'articles' / 'inner-signal' / 'humanize'
X = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'tools'))
import substack_merge as SM  # noqa: E402
import substack_check_text as C  # noqa: E402
import sections as S  # noqa: E402

DATE = '20261025'
GEN = REPO / 'project-sources' / 'substack_transfer_helper.py.txt'
COMPAT = REPO / 'project-sources' / 'CONFIRMED-SUBSTACK-HELPER.json'
sha = lambda b: hashlib.sha256(b).hexdigest()


def run(*args):
    r = subprocess.run([sys.executable] + [str(a) for a in args], capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        raise SystemExit('%s failed:\n%s\n%s' % (args[0], r.stdout[-2000:], r.stderr[-2000:]))
    return r.stdout


def SM_payload_text(archival):
    """The archival HTML's checked text, uncut (what part A's post holds before the check's 99,999-character cut)."""
    return archival.read_text(encoding='utf-8')


def main():
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
    # Part A's check stops at 99,999 characters. Since 2026-10-25 the main guide runs past that (its last 1,349
    # characters, the app and survey sections, were in neither part), so part B starts at the last heading whose text
    # begins at least 500 characters before A's cut: the seam is read twice, in context (the budget doc's "each starting a
    # section or two before the last one's end").
    full = C.checked_text(SM_payload_text(archival), limit=10 ** 7)
    for j in range(k, 0, -1):
        if not re.match(r'<h[1-3]\b', blocks[j]):
            continue
        nxt = next((x for x in blocks[j + 1:j + 6] if x.startswith('<p')), None)
        t = C.checked_text(src[:open_end] + nxt + src[close_start:], limit=10 ** 7) if nxt else ''
        pos = full.find(t[:50]) if t else -1
        if 0 <= pos <= 99999 - 500:
            k = j
            break
    print('part B starts at', re.sub('<[^>]+>', '', blocks[k]), 'at character', pos, 'of', len(full))
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
        html_text = payload.decode('utf-8')
        checked = C.checked_text(html_text)
        (X / ('TEXT-%s.txt' % part)).write_text(checked, encoding='utf-8')
        straight = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
        # the editor's words after the paste (its innerText, quotes made straight): inline tags join their words, any
        # other tag separates them
        words = re.sub(r'</?(?:a|em|strong|b|i|u|s|span|code|sup|sub)\b[^>]*>', '', html_text)
        words = re.sub(r'<[^>]+>', ' ', words)
        import html as _h
        words = _h.unescape(words).translate(straight).split()
        out[part] = {'archival': str(arch.relative_to(REPO)), 'archival_sha256': sha(arch.read_bytes()),
                     'helper': str(helper.relative_to(REPO)), 'helper_sha256': sha(helper.read_bytes()),
                     'payload': 'PAYLOAD-%s.html' % part, 'payload_sha256': sha(payload), 'payload_chars': len(payload),
                     'text': 'TEXT-%s.txt' % part, 'text_sha256': sha(checked.encode('utf-8')), 'text_chars': len(checked)}
        (X / ('WORDS-%s.json' % part)).write_text(json.dumps({'words': len(words), 'words_sha256': sha(' '.join(words).encode('utf-8')),
                                                               'payload_sha256': sha(payload)}, indent=1) + '\n', encoding='utf-8')
    # the text Pangram reads, for the predictions: the guide's sections from the working copy
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    secs = S.sections(md, str(H / 'source' / 'substack-editor-20260928.html'))
    texts = [S.text_of(bl) for _, bl in secs]
    heads = [h for h, _ in secs]
    kb = heads.index('# Appendices')
    (X / 'WHOLE-GUIDE-A.txt').write_text('\n\n'.join(texts), encoding='utf-8')
    (X / 'WHOLE-GUIDE-B.txt').write_text('\n\n'.join(texts[kb:]), encoding='utf-8')
    out['master_sha256'] = sha((H / 'HUMANIZED-SO-FAR.md').read_bytes())
    out['merge'] = {'verdict': merge['verdict'], 'report': 'MERGE-REPORT-%s.json' % DATE}
    (X / 'RECHECK-BUILD.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
