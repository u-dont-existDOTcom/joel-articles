"""pangram_round.py - build one screen round for a new paragraph: each candidate alone, beside the paragraph
before it, and at the end of its section, in one batch (E181).

Usage (from the repo root):
  python3 tools/humanization/pangram_round.py --article ARTICLE --heading "HEADING" --round t64a \
      --out-prefix articles/X/tools/pangram-runs/2026-10-17-turn64-a --predictions articles/X/tools/PREDICTIONS.md \
      --date "2026-10-17 (turn 64)" --label P11 --note "what the round tries" \
      --section-march "P1 S S B | P2 ..." DRAFT.txt:"S S B S" [DRAFT.txt:"MARCH" ...]

Joel, 2026-10-17 01:15 UTC: "idk why that had to take 38 mins tho, at this rate we will never be done. the point of
this was that you would learn to do this better and quicker but it seems like it's getting slower". Turn 63 split its
checks over five rounds (alone first, then the seams and the h1 for the ones that passed) and wrote each round's files
by hand. This builds them in one command: for every candidate, the paragraph alone, the pair with the paragraph before
it (the section's last block), and the section with the candidate added at its end (section text as everywhere: HTML
comments removed, from the heading to the end of the article, blocks joined by a blank line). It writes
OUT-drafts.json and OUT-gate.json (kind "screen", the march given, the lint left to pangram_gate.py --lint-article),
adds a "(pending)" row per check to PREDICTIONS.md, and runs pangram_gate.py, which refuses the batch if any record
fails the gate.

With --spec FILE.json, paragraphs for several sections go in one batch (2026-10-17, turn 65: Joel asked for twelve
hours of work done as fast as I can; one batch is one wait in the browser instead of three). Each record carries the
article it goes into ("lint_article"), and the gate lints it against that one.
  {"round": "t65q", "out_prefix": "...-turn65-q", "predictions": ".../PREDICTIONS.md", "date": "2026-10-17 (turn 65)",
   "groups": [{"article": "A.md", "heading": "H", "section_march": "P1 S B", "outer": [["H1", "P1 S B | P2 S B"]],
               "label": "H P2", "note": "...", "cands": [["DRAFT.txt", "S B S"]]}, ...]}
A group with "checks": "alone" gets only the paragraph-alone checks (its section isn't settled yet), and one with
"checks": "section" only the checks in context (its paragraphs were checked alone before).
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def section_text(md, heading):
    """The section as a reader sees it: comments out, from HEADING to the end, blocks joined by one blank line."""
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    start = md.index('# ' + heading)
    while start > 0 and md[start - 1] == '#':
        start -= 1
    return '\n\n'.join(b.strip() for b in re.split(r'\n\s*\n', md[start:]) if b.strip())


def build(article, heading, rnd, cands, section_march, note, more=(), alone_only=False):
    """Drafts and gate records for every candidate: alone, after the section's last block, and in the section.
    MORE: (heading, march) pairs for the larger sections around it (an h1 around an h2), each checked too.
    ALONE_ONLY: only the paragraph alone, for a paragraph whose section isn't settled yet (turn 65: a later
    paragraph's section check, built on my guess for the one before it, is wasted when the guess reads AI)."""
    md = pathlib.Path(article).read_text(encoding='utf-8')
    sec = section_text(md, heading)
    before = sec.split('\n\n')[-1]
    n = len([b for b in sec.split('\n\n') if not b.startswith('#')])
    outer = [(h, m, section_text(md, h)) for h, m in more]
    drafts, gate = {}, {}
    for path, march in cands:
        text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        tag = re.sub(r'[^a-z0-9]', '', pathlib.Path(path).stem.lower())
        if alone_only != 'section':  # 'section': the paragraph alone was checked before (Pangram won't take the same text twice)
            drafts[f'{rnd}_{tag}'] = text
            gate[f'{rnd}_{tag}'] = {'kind': 'screen', 'march': [march], 'lint': 'REVIEW',
                                    'note': f'{note}; {pathlib.Path(path).stem}. March: my own reading.'}
        if alone_only is True:
            continue
        # Under a fresh heading, or after the section's only paragraph, the pair is the section itself (give or take
        # the heading line), checked below; turn 65 checked both and paid for each twice.
        if not before.startswith('#') and n > 1:
            drafts[f'{rnd}_pair{tag}'] = before + '\n\n' + text
            gate[f'{rnd}_pair{tag}'] = {'kind': 'screen', 'march': [f'P{n} (installed) | P{n + 1} {march}'], 'lint': 'REVIEW',
                                        'note': f'{rnd}: P{n}+P{n + 1}, the paragraph before and {pathlib.Path(path).stem}.'}
        drafts[f'{rnd}_sec{tag}'] = sec + '\n\n' + text
        gate[f'{rnd}_sec{tag}'] = {'kind': 'screen', 'march': [f'{section_march} | P{n + 1} {march}'], 'lint': 'REVIEW',
                                   'note': f'{rnd}: {heading} with P{n + 1} = {pathlib.Path(path).stem}.'}
        for i, (h, m, osec) in enumerate(outer, 2):
            drafts[f'{rnd}_sec{i}{tag}'] = osec + '\n\n' + text
            gate[f'{rnd}_sec{i}{tag}'] = {'kind': 'screen', 'march': [f'{m} | {march}'], 'lint': 'REVIEW',
                                          'note': f'{rnd}: {h} with {pathlib.Path(path).stem} at its end.'}
    order = [k for k in drafts if '_pair' not in k and '_sec' not in k]
    order += [k for k in drafts if '_pair' in k] + [k for k in drafts if '_sec' in k and not re.match(r'.*_sec\d', k)]
    order += [k for k in drafts if re.match(r'.*_sec\d', k)]
    return {k: drafts[k] for k in order}, {k: gate[k] for k in order}, n + 1


def rows_for(drafts, label, heading, more, pn, date, prediction):
    """A "(pending)" PREDICTIONS.md row for each check of one group."""
    rows = []
    for k, text in drafts.items():
        stem = k.split('_', 1)[1]
        words = len(text.split())
        if stem.startswith('pair'):
            what = f'P{pn - 1}+P{pn}, with {stem[4:]} ({words} words)'
        elif re.match(r'sec\d', stem):
            h = more[int(stem[3]) - 2][0]
            what = f'{h} with {stem[4:]} at its end ({words} words)'
        elif stem.startswith('sec'):
            what = f'{heading} with P{pn} = {stem[3:]} ({words} words)'
        else:
            what = f'{label}, {stem} alone ({words} words)'
        rows.append(f'| {date} | {what} [{k}], a screen | {prediction} | (pending) | |')
    return rows


def run(groups, rnd, out_prefix, predictions, date):
    """Build every group's checks into one batch, run pangram_gate.py on it (each record linted against its own
    group's article) and, if the gate writes the batch, add the prediction rows. GROUPS: dicts with article, heading,
    section_march, cands [[DRAFT, MARCH]], and optionally outer [[HEADING, MARCH]], label, note, prediction."""
    drafts, gate, rows = {}, {}, []
    for g in groups:
        more = [tuple(o) for o in g.get('outer', [])]
        d, gt, pn = build(g['article'], g['heading'], rnd, [tuple(c) for c in g['cands']], g['section_march'],
                          g.get('note') or rnd, more, alone_only={'alone': True, 'section': 'section'}.get(g.get('checks'), False))
        clash = set(d) & set(drafts)
        if clash:
            sys.exit('two groups give the same check: %s (name the drafts apart)' % ', '.join(sorted(clash)))
        for k in gt:
            gt[k]['lint_article'] = str(g['article'])
        drafts.update(d)
        gate.update(gt)
        rows += rows_for(d, g.get('label', 'the new paragraph'), g['heading'], more, pn, date,
                         g.get('prediction', 'Human, low (my call)'))
    out = pathlib.Path(out_prefix)
    out.with_name(out.name + '-drafts.json').write_text(json.dumps(drafts, indent=1, ensure_ascii=False), encoding='utf-8')
    out.with_name(out.name + '-gate.json').write_text(json.dumps(gate, indent=1, ensure_ascii=False), encoding='utf-8')
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_gate.py'), str(out.with_name(out.name + '-drafts.json')),
           str(out.with_name(out.name + '-gate.json')), str(out.with_name(out.name + '.js')), '--name', rnd,
           '--lint-article', str(groups[0]['article'])] + list(drafts)
    rc = subprocess.run(cmd).returncode
    if rc == 0:  # the prediction rows go in only for a batch the gate wrote
        p = pathlib.Path(predictions)
        p.write_text(p.read_text(encoding='utf-8').rstrip('\n') + '\n' + '\n'.join(rows) + '\n', encoding='utf-8')
    return rc


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--spec', help='a JSON file: {"round", "out_prefix", "predictions", "date", "groups": [...]}, '
                    'for paragraphs of several sections in one batch (each group as the options below)')
    for a in ('--article', '--heading', '--round', '--out-prefix', '--predictions', '--date', '--section-march'):
        ap.add_argument(a)
    ap.add_argument('--label', default='the new paragraph')
    ap.add_argument('--note', default='')
    ap.add_argument('--prediction', default='Human, low (my call)')
    ap.add_argument('--outer', action='append', default=[], metavar='HEADING::MARCH',
                    help='a larger section around --heading to check too, with its march (e.g. the h1 around an h2)')
    ap.add_argument('cands', nargs='*', help='DRAFT.txt:MARCH')
    a = ap.parse_args(argv)
    if a.spec:
        s = json.loads(pathlib.Path(a.spec).read_text(encoding='utf-8'))
        return run(s['groups'], s['round'], s['out_prefix'], s['predictions'], s['date'])
    need = [o for o in ('article', 'heading', 'round', 'out_prefix', 'predictions', 'date', 'section_march') if not getattr(a, o)]
    if need or not a.cands:
        ap.error('without --spec, these are needed: ' + ', '.join(['--' + o.replace('_', '-') for o in need] + ([] if a.cands else ['DRAFT.txt:MARCH'])))
    group = {'article': a.article, 'heading': a.heading, 'section_march': a.section_march, 'label': a.label,
             'note': a.note or a.round, 'prediction': a.prediction, 'outer': [o.split('::', 1) for o in a.outer],
             'cands': [c.rsplit(':', 1) for c in a.cands]}
    return run([group], a.round, a.out_prefix, a.predictions, a.date)


if __name__ == '__main__':
    sys.exit(main())
