"""Install the induction section from sample bf (2026-10-22), after its reviews and the gate.

The section is already installed (rf-zg's fixed sample ba), so tools/install_fixed.py's install, which looks for the
published blocks, can't place it. Instead the section's span in the working copy, from its h1 to the next h1, is replaced by
SECTION.md (install_fixed.py's section_md of HG17.bf-fixed.json, as make_hg17_bf_fixed.py wrote it), which is how
CANDIDATE.md was built; the working copy must still be the one CANDIDATE.md was built from, apart from that span. Then the
4.1 edits must all be in (fix-20261020/apply_edits41.py --check), and fix-20261018/installed.json's HG17 record says what
went in.

  python3 articles/inner-signal/humanize/fix-20261022/hg17-bf/install_bf.py   (from the repo root)
"""
import datetime, json, pathlib, subprocess, sys

V = pathlib.Path(__file__).resolve().parent
H = V.parents[1]
REPO = H.parents[2]
H1 = '# Induction: gathering attention without disappearing\n'


def span(md):
    a = md.index(H1)
    return a, md.index('\n# ', a + 5)


def main():
    hsf = H / 'HUMANIZED-SO-FAR.md'
    md = hsf.read_text(encoding='utf-8')
    cand = (V / 'CANDIDATE.md').read_text(encoding='utf-8')
    sec = (V / 'SECTION.md').read_text(encoding='utf-8').rstrip('\n')
    a, b = span(md)
    ca, cb = span(cand)
    assert md[:a] == cand[:ca] and md[b:] == cand[cb:], 'the working copy changed outside the section since CANDIDATE.md'
    assert cand[ca:cb] == sec, 'CANDIDATE.md does not hold SECTION.md'
    if md == cand:
        print('installed already')
    else:
        hsf.write_text(cand, encoding='utf-8')
        print('installed: HG17 is sample bf with its fixes (%d words, was %d)' % (len(sec.split()), len(md[a:b].split())))
    r = subprocess.run([sys.executable, str(H / 'fix-20261020' / 'apply_edits41.py'), '--check'], capture_output=True,
                       text=True, cwd=REPO)
    assert r.returncode == 0 and 'applied now: none' in r.stdout, r.stdout[-1500:] + r.stderr[-1500:]
    inst = H / 'fix-20261018' / 'installed.json'
    rec = json.loads(inst.read_text(encoding='utf-8'))
    old = rec.get('HG17', {})
    rec['HG17'] = {
        'stage': 'fixed (sample bf, pending its 4.1 reading in the guide)',
        'whole': 'sample bf read Human in every window of the first screening post (fix-20261022/screen/SCREEN-RESULT.json, '
                 'S4; Joel\'s result link of 21:41 UTC, https://www.pangram.com/feed/e836ef9c-c964-4012-a5af-994ef88658eb); '
                 'the fixed section is read in the next whole-guide recheck through Substack (gate E200)',
        'meaning': 'fix-20261022/hg17-bf/VERIFY-part1.md to part3.md (bf: kept 169, changed 52, lost 30, added claims 10); '
                   'the fixes drafted per part against FIX-BRIEF.md (FIXDRAFT-partN.json), applied in make_hg17_bf_fixed.py '
                   '(FIXES.json); the reviews: FIX-CHECK.md (the fixes in place and an audit of the let stands), '
                   'SENSE-HG17.md, STANCE-HG17.md, march/, and the rounds after them',
        'fixed': 'fix-20261022/hg17-bf/HG17.bf-fixed.json',
        'installed': '%s, fix-20261022/hg17-bf/install_bf.py (the section\'s span replaced by SECTION.md); before it, '
                     'rf-zg/HG17.fixed.json (sample ba), which read AI in the recheck of 2026-10-21'
                     % datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'replaced': old,
    }
    inst.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('installed.json: HG17 updated; 4.1 edits all in')


if __name__ == '__main__':
    main()
