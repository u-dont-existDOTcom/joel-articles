"""Batch 472g's two edits that go in (2026-10-23): EDITS-472g.json for fix-20261020/apply_edits41.py --add, and GATE.json,
the record of what each passed.

  s1b  De-hypnosis P1: the run of ten "By X?" questions becomes the bracketed list of Joel's Appendix C opening
       ("(a screen, a specific ad, ..., repetition, etc.)"). Human on its pair through the API, the sentence's window High
       where the questions had read Medium; c, which joined "It's all around you." on to clear the linter's B3, read worse
       (Mostly Human Written, 9.6% AI), so b goes in with the short sentence as installed (E211).
  s3c  Come all the way back P4: the short commands joined, with the count's caveat as a gloss in brackets and the installed
       "truly". Human on its pair, the whole pair in one High window.

The seam between the induction section and the return (s2) read AI, High, in six versions and goes to Joel (question 14);
nothing of it goes in. s1 and s3 read Human on their pairs as they stood too, so the pair shows only that these are not
worse; the next whole-guide recheck reads them in place.

  python3 articles/inner-signal/humanize/fix-20261023/b472/install_b472.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
REPO = H.parents[2]
PAGE = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/inner-signal/humanize/'
        'fix-20261023/b472/API-CHECKS.md')
RECHECK = 'https://www.pangram.com/feed/47610d4b-fb69-4966-896f-317b029fc1af'
GO = {
    'b472_s1b': ('recheck A (%s, part 7): the run of questions read AI, Low and one Medium, in five short windows (light '
                 'green on 2026-10-21). A run of questions read AI in the Inner Child lane (E217); the list goes in '
                 'brackets after the noun it lists, ending "etc.", as in Joel\'s Appendix C opening, which read Human, high, '
                 'in his check.' % RECHECK),
    'b472_s3c': ('recheck A (%s, part 9): "Get up only when you feel steady." and "Make sure you\'re truly oriented and '
                 'alert. Don\'t just assume it because you\'ve done the count." read AI, Low, as on 2026-10-21: short commands '
                 'in a row, and the published "is not proof" (E193\'s tell). They are joined, and the caveat is a gloss in '
                 'brackets in plain words.' % RECHECK),
}


def main():
    cands = json.loads((B / 'CANDIDATES.json').read_text(encoding='utf-8'))
    lint = json.loads((B / 'lint-compare.json').read_text(encoding='utf-8'))
    results = {}
    for f in sorted(B.glob('API-RESULTS-*.jsonl')):
        for l in f.read_text(encoding='utf-8').splitlines():
            if l.strip():
                r = json.loads(l)
                results[r['name']] = r
    edits, gate = [], {}
    for name, why in GO.items():
        c = cands[name]
        e = c['edit']
        r = results[name]
        assert r['headline'] == 'Human Written', (name, r['headline'])
        edits.append({'key': e['key'], 'section': e['section'], 'old': e['old'], 'new': e['new'], 'batch': '472g',
                      'diagnosis': why, 'block': c['block'], 'paragraph_check': PAGE + '#' + name,
                      'paragraph_result': '%s (Pangram %s, the API, %s; on its pair: %s)' % (r['headline'], r['version'],
                                                                                          r['utc'], c['what']),
                      'section_check': None, 'section_result': None, 'reviews': 'fix-20261023/b472/'})
        lk = name if name in lint else name[:-1] + 'b'
        gate[name] = {'sense': 'OK (REVIEW.md, item 3)', 'meaning': 'KEPT (REVIEW.md, item 1)',
                      'published': 'OK (REVIEW.md, item 2)',
                      'lint_new_rules': lint[lk]['new_rules'] if name.endswith('b') else [],
                      'lint_note': ('B3 on "It\'s all around you.", the installed sentence, now after a long one: the try '
                                    'that cleared it (b472_s1c) read worse, so it stays (E211)') if name == 'b472_s1b' else
                                   'none brought: c has the installed "truly" for b\'s "actually" (O25)',
                      'api': PAGE + '#' + name, 'ledger': 'pangram-ledger.jsonl, key %s' % name}
    (B / 'EDITS-472g.json').write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(H / 'fix-20261020' / 'apply_edits41.py'), '--add', str(B / 'EDITS-472g.json')],
                       capture_output=True, text=True, cwd=REPO)
    print(r.stdout[-400:], r.stderr[-800:])
    assert r.returncode == 0


if __name__ == '__main__':
    main()
