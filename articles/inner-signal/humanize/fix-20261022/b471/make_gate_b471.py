"""Batch 471g's gate records (2026-10-22), then the batch through the gate (as make_gate_b470.py).

The texts are ./drafts.json (make_b471.py): each changed paragraph as Pangram reads it. Each record cites its reviews: the
march read of the installed paragraph and the edit (round 1 in r1/march/, round 2 in r2/march/), the item review
(r1/REVIEW.md), the stance check (r1/STANCE.md) and the re-read of round 2's fixes in place (r2/VERIFY-r2.md). Both
paragraphs were installed from Emulate's text with my meaning fixes, so each record is an edit of an Emulate text
("was_kind": "emulate"), linted like for like (lint_was against the candidate) and compared rule by rule
(lint-compare.json).

The three-roles step's reading in the recheck of 2026-10-21 isn't found by make_b470.reading_of (its "Leader" became
"Guide" in batch 470g): it is in part B's window 16, AI-Generated, High, the 518 words that run from Appendix B's last
list into Appendix C's prose (fix-20261020/substack41r/WINDOWS-41r2-b.txt), so it is given here.

No text goes to pangram.com from here (gate E200): the paragraphs are read in the next whole-guide recheck through
Substack.

  python3 articles/inner-signal/humanize/fix-20261022/b471/make_gate_b471.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
B = pathlib.Path(__file__).resolve().parent
OUT = B / 'batch'
HSF = REPO / 'articles' / 'inner-signal' / 'humanize' / 'HUMANIZED-SO-FAR.md'
sys.path.insert(0, str(REPO / 'articles' / 'inner-signal' / 'humanize' / 'tools'))
import sections as S  # noqa: E402


READING = {'b471-three-roles': {'part': 'B', 'shade': 'red', 'windows': [16],
                                'link': 'https://www.pangram.com/feed/558d14f6-625d-46aa-8495-adf9141cb3a4'}}


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def march_reads(folder):
    """{text key: {'was': [labels per paragraph], 'new': [...]}} from a round's march-labels.txt and march-map.json."""
    lf = folder / 'march-labels.txt'
    if not lf.exists():
        return {}
    labels = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', lf.read_text(encoding='utf-8'), re.M))
    out = {}
    for m in json.loads((folder / 'march-map.json').read_text(encoding='utf-8')):
        seq = ' '.join(labels[str(m['start'] + j + 1)] for j in range(m['n']))
        out.setdefault(m['key'], {}).setdefault(m['ver'], []).append(seq)
    return out


def lint(text, article=None):
    """tells_lint.py's verdict on TEXT, in context when ARTICLE is given. For lint_was the installed version of a text is
    linted against the candidate, so the sentences the batch changes count as "mine" in both versions, as the gate's own
    in-context run counts them in the edit: like for like. Linted alone or against the working copy, the installed
    version has no words of mine, and a rename inside an installed sentence ("You can also work with your Guide.") then
    reads as a new coach phrase (E41's 2 per 100 of my words) that the installed sentence had too."""
    f = OUT / 'texts' / '_lint.txt'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), str(f)]
                       + (['--installed', str(article)] if article else []), capture_output=True, text=True, cwd=REPO)
    return next((l.split(':', 1)[1].strip() for l in r.stdout.split('\n') if l.startswith('verdict:')), None)


def rules(text):
    """The linter's rule headers on TEXT (its "-- B4/E15 ..." lines), as make_b470_r4.py compared them."""
    f = OUT / 'texts' / '_rules.txt'
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), str(f)], capture_output=True,
                       text=True, cwd=REPO)
    return sorted(set(re.findall(r'^-- ([A-Z]\w*(?:/[A-Z]\w*)*)', r.stdout, re.M)))


def main():
    OUT.mkdir(exist_ok=True)
    drafts = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    edits = {e['key']: e for e in meta['edits']}
    mr = march_reads(B / 'r1' / 'march')
    for k, v in march_reads(B / 'r2' / 'march').items():   # round 2's read of a paragraph replaces round 1's
        mr[k] = v
    (B / 'march.json').write_text(json.dumps(mr, indent=1) + '\n', encoding='utf-8')
    blocks = HSF.read_text(encoding='utf-8').split('\n\n')
    cand = (B / 'CANDIDATE.md').read_text(encoding='utf-8').split('\n\n')
    changed_blocks = sorted({t['block'] for t in meta['texts'].values()})
    rec, keys = {}, []
    for k, t in meta['texts'].items():
        if t.get('heading'):
            continue
        keys.append(k)
        r41 = t.get('reading_41') or READING.get(k) or {}
        was = ('%s in the whole guide (4.1, window%s %s of part %s, %s)'
               % ({'dark': 'Human, high', 'light': 'Human, medium or low', 'red': 'AI'}[r41['shade']],
                  's' if len(r41['windows']) > 1 else '', ', '.join(map(str, r41['windows'])), r41['part'], r41['link'])
               if r41 else 'not found in the recheck\'s text')
        # the installed version of the text Pangram reads (a short paragraph is read with its neighbor, so a label line's
        # text holds the paragraph after it): every changed paragraph in it put back as installed
        old_para = drafts[k]
        for j in changed_blocks:
            old_para = old_para.replace(S.plain(cand[j]), S.plain(blocks[j]))
        cold = [rel(B / 'r1' / 'REVIEW.md'), rel(B / 'r2' / 'VERIFY-r2.md')]
        rec[k] = {'kind': 'edit', 'was': was, 'was_kind': 'emulate', 'lint_was': lint(old_para, B / 'CANDIDATE.md'), 'march_was': mr.get(k, {}).get('was', []), 'march': mr.get(k, {}).get('new', []),
                  'cold_read': cold, 'grounding_note': rel(B / 'r1' / 'REVIEW.md'), 'stance_note': rel(B / 'r1' / 'STANCE.md'),
                  'cold': None, 'grounding': None, 'stance': None, 'missing': [], 'words': t['words'],
                  'march_reads': rel(B / 'march.json'), 'edits': t['edits']}
    comp = {}
    for k in keys:
        i = meta['texts'][k]['block']
        ro, rn = rules(blocks[i]), rules(cand[i])
        comp[k] = {'installed': ro, 'edit': rn, 'new_rules': [x for x in rn if x not in ro]}
    (B / 'lint-compare.json').write_text(json.dumps(comp, indent=1) + '\n', encoding='utf-8')
    over = B / 'gate-answers.json'
    if over.exists():
        for k, v in json.loads(over.read_text(encoding='utf-8')).items():
            if k in rec:
                rec[k].update(v)
    (OUT / 'drafts.json').write_text(json.dumps({k: drafts[k] for k in keys}, ensure_ascii=False, indent=1) + '\n',
                                     encoding='utf-8')
    (OUT / 'GATE.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(OUT / 'drafts.json'),
                        str(OUT / 'GATE.json'), str(OUT / 'b471.js'), '--name', 'B471log', '--lint-article', str(HSF)] + keys,
                       capture_output=True, text=True, cwd=REPO)
    print(r.stdout[-4000:], r.stderr[-2000:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
