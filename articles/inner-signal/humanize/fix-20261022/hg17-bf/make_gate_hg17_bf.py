"""HG17's gate record (2026-10-22): the induction section from sample bf (make_hg17_bf_fixed.py) through the gate before it
goes into the working copy (as fix-20261018/rf-zg/make_gate_hg17.py did for sample ba).

The text is the section as Pangram reads it in the guide (CANDIDATE.md, the section's blocks as sections.text_of gives
them). Its record is an edit of an Emulate text ("was_kind": "emulate"): sample bf with my meaning fixes. Unlike ba, bf was
read in Pangram before any meaning work: Human in every window of the first screening post. The record cites its reviews:
the march read of every paragraph the fixes or the headings changed, bf's version and the fixed one (march/ for round 1,
rN/march/ for each later round), the fix check with its audit of the let stands (FIX-CHECK.md), the cold read
(SENSE-HG17.md), the stance check (STANCE-HG17.md) and the meaning check it started from (VERIFY-part1.md to part3.md). A
finding answered rather than fixed is answered in gate-answers.json, which fills or overrides the record.

No text goes to pangram.com from here (gate E200): the fixed section is read in the next whole-guide recheck.

  python3 articles/inner-signal/humanize/fix-20261022/hg17-bf/make_gate_hg17_bf.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

V = pathlib.Path(__file__).resolve().parent
H = V.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import reviewer as R   # noqa: E402
import sections as S   # noqa: E402

OUT = V / 'batch'
KEY = 'HG17-bf'
TITLE = '# Induction: gathering attention without disappearing'
BF = H / 'fix-20261018' / 'emu-bf' / 'HG17-fx1.out.txt'


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def lint(text):
    f = OUT / 'texts' / '_lint.txt'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), str(f)], capture_output=True,
                       text=True, cwd=REPO)
    return next((l.split(':', 1)[1].strip() for l in r.stdout.split('\n') if l.startswith('verdict:')), None)


def march_reads():
    """march/march.json: {'was': [labels of each of bf's changed paragraphs], 'new': [... of the fixed ones]}, each
    paragraph in CHANGED-PARAS.json, its labels from the last round that read that version."""
    got = {}
    rounds = sorted((p.name for p in V.glob('r[0-9]*') if p.is_dir()), key=lambda n: int(n[1:]))
    for folder in [V / 'march'] + [V / r / 'march' for r in rounds]:
        lab = folder / 'march-labels.txt'
        if not lab.exists():
            continue
        labels = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', lab.read_text(encoding='utf-8'), re.M))
        for m in json.loads((folder / 'march-map.json').read_text(encoding='utf-8')):
            got[(m['para'], m['ver'])] = [labels[str(m['start'] + j + 1)] for j in range(m['n'])]
    out = {'was': [], 'new': []}
    for c in json.loads((V / 'CHANGED-PARAS.json').read_text(encoding='utf-8')):
        for ver in ('was', 'new'):
            q = c.get(ver)
            if q and len(R.march_paragraphs(q)):
                k = (c['para'], ver)
                if k not in got:
                    raise SystemExit('no march read of %r: run the round that reads it' % (k,))
                out[ver] += got[k]
    (V / 'march' / 'march.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8')
    return out


def main():
    OUT.mkdir(exist_ok=True)
    cand = (V / 'CANDIDATE.md').read_text(encoding='utf-8')
    secs = {h: bl for h, bl in S.sections(cand, str(H / 'source' / 'substack-editor-20260928.html'))}
    text = S.text_of(secs[TITLE])
    mr = march_reads()
    was_b = sum('B' in m.split() for m in mr['was'])
    new_b = sum('B' in m.split() for m in mr['new'])
    bf = '\n\n'.join(p.strip() for p in re.split(r'\n\s*\n', BF.read_text(encoding='utf-8')) if p.strip())
    rec = {KEY: {'kind': 'edit', 'was_kind': 'emulate',
                 'was': 'emu-bf, Emulate\'s run of the installed fixed section with Joel\'s 11 b (fix-20261018/emu-bf): Human '
                        'in all 46 of its windows in the first screening post (23 of them medium or low), '
                        'https://www.pangram.com/feed/e836ef9c-c964-4012-a5af-994ef88658eb (fix-20261022/screen/SCREEN-RESULT.json, '
                        'S4); under gate E200 the fixed section is read in the next whole-guide recheck through Substack',
                 'lint_was': lint(bf), 'march_was': mr['was'], 'march': mr['new'],
                 'march_breaks': 'bf %d of %d changed paragraphs with a break, fixed %d of %d' % (
                     was_b, len(mr['was']), new_b, len(mr['new'])),
                 'cold_read': rel(V / 'SENSE-HG17.md'), 'grounding_note': rel(V / 'FIX-CHECK.md'),
                 'stance_note': rel(V / 'STANCE-HG17.md'), 'cold': None, 'grounding': None, 'stance': None,
                 'missing': [], 'words': len(text.split()), 'march_reads': rel(V / 'march' / 'march.json'),
                 'lint_compare': rel(V / 'lint-compare.json')}}
    over = V / 'gate-answers.json'
    if over.exists():
        for k, v in json.loads(over.read_text(encoding='utf-8')).items():
            rec[k].update(v)
    (OUT / 'drafts.json').write_text(json.dumps({KEY: text}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (OUT / 'GATE.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(rec[KEY]['march_breaks'], '| lint_was', rec[KEY]['lint_was'])
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(OUT / 'drafts.json'),
                        str(OUT / 'GATE.json'), str(OUT / 'hg17bf.js'), '--name', 'HG17bflog', '--lint-article',
                        str(H / 'HUMANIZED-SO-FAR.md'), KEY], capture_output=True, text=True, cwd=REPO)
    print(r.stdout[-3000:], r.stderr[-2000:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
