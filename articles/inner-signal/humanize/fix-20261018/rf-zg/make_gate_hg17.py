"""HG17's gate record (2026-10-21): the fixed induction section (make_hg17_fixed.py) through the gate before it goes
into the working copy.

The text is the section as Pangram reads it in the guide (CANDIDATE.md from make_hg17_reviews.py, the section's blocks
as sections.text_of gives them). Its record is an edit of an Emulate text ("was_kind": "emulate"): sample ba of the fast
path with my meaning fixes. The record cites its reviews: the march read of every paragraph a fix changed, ba's version
and the fixed one (march/march-labels.txt, decoded by march/march-map.json into march/march.json), the cold read
(SENSE-HG17.md), the meaning check (HG17.fixed.verify.out.md) and the stance check (STANCE-HG17.md). A reviewer's finding
that is answered rather than fixed is answered in gate-answers.json, which fills or overrides the record.

No text goes to pangram.com from here (gate E200: many paragraphs are read in the real article through free Substack
posts): sample ba was never read in Pangram, and the fixed section is read in the next whole-guide recheck. GATE.json
records that it cleared the meaning reviews before it went into the working copy, and the gate's verdict
(batch/hg17.js is written by pangram_gate.py but not run).

  python3 articles/inner-signal/humanize/fix-20261018/rf-zg/make_gate_hg17.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
import assemble as A   # noqa: E402
import sections as S   # noqa: E402

OUT = HERE / 'batch'
KEY = 'HG17-fixed'
TITLE = '# Induction: gathering attention without disappearing'


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def lint(text, article=None):
    f = OUT / 'texts' / '_lint.txt'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), str(f)]
                       + (['--installed', str(article)] if article else []), capture_output=True, text=True, cwd=REPO)
    return next((l.split(':', 1)[1].strip() for l in r.stdout.split('\n') if l.startswith('verdict:')), None)


def march_reads():
    """march/march.json: {'was': [labels of each of ba's changed paragraphs], 'new': [... of the fixed ones]}."""
    labels = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (HERE / 'march' / 'march-labels.txt').read_text(encoding='utf-8'),
                             re.M))
    out = {'was': [], 'new': []}
    for m in json.loads((HERE / 'march' / 'march-map.json').read_text(encoding='utf-8')):
        for j in range(m['n']):
            out[m['ver']].append(labels[str(m['start'] + j + 1)])
    (HERE / 'march' / 'march.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8')
    return out


def ba_text():
    """Sample ba's section as it came composed (rf-zg/HG17.ba.json: the published headings and ba's paragraphs)."""
    d = json.loads((HERE / 'HG17.ba.json').read_text(encoding='utf-8'))
    kbk = A.kb()[d['key']]
    out = []
    for u in d['units']:
        out += u['paras'] if u['kind'] == 'emulate' else [S.plain(kbk[b][0]) for b in u['blocks']]
    return '\n\n'.join(out)


def main():
    OUT.mkdir(exist_ok=True)
    cand = (HERE / 'CANDIDATE.md').read_text(encoding='utf-8')
    secs = {h: bl for h, bl in S.sections(cand, str(H / 'source' / 'substack-editor-20260928.html'))}
    text = S.text_of(secs[TITLE])
    mr = march_reads()
    was_b = sum('B' in m.split() for m in mr['was'])
    new_b = sum('B' in m.split() for m in mr['new'])
    rec = {KEY: {'kind': 'edit', 'was_kind': 'emulate',
                 'was': 'emu-ba, sample ba of the fast path (three Emulate samples of the whole section from the published '
                        'text, 2026-10-21): not read in Pangram; under gate E200 the fixed section is read in the next '
                        'whole-guide recheck through Substack. The published section read AI in the first 4.1 check',
                 'lint_was': lint(ba_text()), 'march_was': mr['was'], 'march': mr['new'],
                 'march_breaks': 'ba %d of %d changed paragraphs with a break, fixed %d of %d' % (
                     was_b, len(mr['was']), new_b, len(mr['new'])),
                 'cold_read': rel(HERE / 'SENSE-HG17.md'), 'grounding_note': rel(HERE / 'HG17.fixed.verify.out.md'),
                 'stance_note': rel(HERE / 'STANCE-HG17.md'), 'cold': None, 'grounding': None, 'stance': None,
                 'missing': [], 'words': len(text.split()), 'march_reads': rel(HERE / 'march' / 'march.json')}}
    over = HERE / 'gate-answers.json'
    if over.exists():
        for k, v in json.loads(over.read_text(encoding='utf-8')).items():
            rec[k].update(v)
    (OUT / 'drafts.json').write_text(json.dumps({KEY: text}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (OUT / 'GATE.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(rec[KEY]['march_breaks'], '| lint_was', rec[KEY]['lint_was'])
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(OUT / 'drafts.json'),
                        str(OUT / 'GATE.json'), str(OUT / 'hg17.js'), '--name', 'HG17log', '--lint-article',
                        str(H / 'HUMANIZED-SO-FAR.md'), KEY], capture_output=True, text=True, cwd=REPO)
    print(r.stdout[-3000:], r.stderr[-2000:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
