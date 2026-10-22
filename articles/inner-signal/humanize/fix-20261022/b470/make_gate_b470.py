"""Batch 470g's gate records (2026-10-22), then the batch through the gate.

The texts are ./drafts.json (make_b470.py): each changed paragraph as Pangram reads it. Each record cites its reviews: the
march read of the installed paragraph and the edit (round 1, r1/march/, for every paragraph; round 2, r2/march/, for the
four that round 2 changed), the item review (REVIEW.md in r1/, its round 2 in r2/VERIFY-r2.md), which reads each changed
paragraph against the answers it carries out, its meaning, the figures' names and its sense between the paragraphs around
it, the cold read of the h1 that holds most of the changes (r1/SENSE-HG14.md), the stance check (r1/STANCE.md), and the
re-reads of each round's fixes in place (r2/VERIFY-r2.md for round 1's findings, r3/VERIFY-r3.md for the stance check's). A
reviewer's finding that is answered rather than fixed is answered in gate-answers.json, which fills or overrides these
records.

Every section the batch changes was installed from Emulate's text with my meaning fixes (fix-20261018/installed.json:
samples, refixes and triaged refixes), so each record is an edit of an Emulate text ("was_kind": "emulate"): a linter FAIL
holds it only when the installed paragraph wasn't FAIL too, and the rules behind each FAIL are compared before and after
(lint-compare.json, the same rules each time, so the batch's words brought none).

No text goes to pangram.com from here (gate E200: the changed paragraphs are read in the real article, in the next
whole-guide recheck through Substack); GATE.json records that each edit cleared the reviews before it went into the working
copy, and the gate's verdict on each (b470.js is written by pangram_gate.py but not run).

  python3 articles/inner-signal/humanize/fix-20261022/b470/make_gate_b470.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
B = pathlib.Path(__file__).resolve().parent
OUT = B / 'batch'
HSF = REPO / 'articles' / 'inner-signal' / 'humanize' / 'HUMANIZED-SO-FAR.md'
sys.path.insert(0, str(REPO / 'articles' / 'inner-signal' / 'humanize' / 'tools'))
import sections as S  # noqa: E402


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
    for rnd in ('r2', 'r3', 'r4'):   # a later round's read of a paragraph replaces the earlier one
        for k, v in march_reads(B / rnd / 'march').items():
            mr[k] = v
    # A label line ("The Guide:", "Working with childhood protector parts:") has no sentence of its own; Pangram reads it
    # with the paragraph after it (drafts.json), so its march is that paragraph's: B132 (an edit of this batch) for the
    # first, the unchanged B138 for the second (read in r3/march-label-neighbors/).
    mr['b470-guide-label'] = mr['b470-guide-work']
    mr.update(march_reads(B / 'r3' / 'march-label-neighbors'))
    (B / 'march.json').write_text(json.dumps(mr, indent=1) + '\n', encoding='utf-8')
    blocks = HSF.read_text(encoding='utf-8').split('\n\n')
    cand = (B / 'CANDIDATE.md').read_text(encoding='utf-8').split('\n\n')
    changed_blocks = sorted({t['block'] for t in meta['texts'].values()})
    rec, keys = {}, []
    for k, t in meta['texts'].items():
        if t.get('heading'):
            continue
        keys.append(k)
        r41 = t.get('reading_41') or {}
        was = ('%s in the whole guide (4.1, window%s %s of part %s, %s)'
               % ({'dark': 'Human, high', 'light': 'Human, medium or low', 'red': 'AI'}[r41['shade']],
                  's' if len(r41['windows']) > 1 else '', ', '.join(map(str, r41['windows'])), r41['part'], r41['link'])
               if r41 else 'not found in the recheck\'s text')
        # the installed version of the text Pangram reads (a short paragraph is read with its neighbor, so a label line's
        # text holds the paragraph after it): every changed paragraph in it put back as installed
        old_para = drafts[k]
        for j in changed_blocks:
            old_para = old_para.replace(S.plain(cand[j]), S.plain(blocks[j]))
        cold = ([rel(B / 'r1' / 'REVIEW.md'), rel(B / 'r2' / 'VERIFY-r2.md'), rel(B / 'r3' / 'VERIFY-r3.md'),
                 rel(B / 'r4' / 'VERIFY-r4.md')]
                + ([rel(B / 'r1' / 'SENSE-HG14.md')] if t['section'] == 'HG14' else []))
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
                        str(OUT / 'GATE.json'), str(OUT / 'b470.js'), '--name', 'B470log', '--lint-article', str(HSF)] + keys,
                       capture_output=True, text=True, cwd=REPO)
    print(r.stdout[-4000:], r.stderr[-2000:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
