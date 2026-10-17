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


def build(article, heading, rnd, cands, section_march, note):
    """Drafts and gate records for every candidate: alone, after the section's last block, and in the section."""
    sec = section_text(pathlib.Path(article).read_text(encoding='utf-8'), heading)
    before = sec.split('\n\n')[-1]
    n = len([b for b in sec.split('\n\n') if not b.startswith('#')])
    drafts, gate = {}, {}
    for path, march in cands:
        text = pathlib.Path(path).read_text(encoding='utf-8').strip()
        tag = re.sub(r'[^a-z0-9]', '', pathlib.Path(path).stem.lower())
        drafts[f'{rnd}_{tag}'] = text
        gate[f'{rnd}_{tag}'] = {'kind': 'screen', 'march': [march], 'lint': 'REVIEW',
                                'note': f'{note}; {pathlib.Path(path).stem}. March: my own reading.'}
        drafts[f'{rnd}_pair{tag}'] = before + '\n\n' + text
        gate[f'{rnd}_pair{tag}'] = {'kind': 'screen', 'march': [f'P{n} (installed) | P{n + 1} {march}'], 'lint': 'REVIEW',
                                    'note': f'{rnd}: P{n}+P{n + 1}, the paragraph before and {pathlib.Path(path).stem}.'}
        drafts[f'{rnd}_sec{tag}'] = sec + '\n\n' + text
        gate[f'{rnd}_sec{tag}'] = {'kind': 'screen', 'march': [f'{section_march} | P{n + 1} {march}'], 'lint': 'REVIEW',
                                   'note': f'{rnd}: {heading} with P{n + 1} = {pathlib.Path(path).stem}.'}
    order = [k for k in drafts if '_pair' not in k and '_sec' not in k]
    order += [k for k in drafts if '_pair' in k] + [k for k in drafts if '_sec' in k]
    return {k: drafts[k] for k in order}, {k: gate[k] for k in order}, n + 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for a in ('--article', '--heading', '--round', '--out-prefix', '--predictions', '--date', '--section-march'):
        ap.add_argument(a, required=True)
    ap.add_argument('--label', default='the new paragraph')
    ap.add_argument('--note', default='')
    ap.add_argument('--prediction', default='Human, low (my call)')
    ap.add_argument('cands', nargs='+', help='DRAFT.txt:MARCH')
    a = ap.parse_args(argv)
    cands = [c.rsplit(':', 1) for c in a.cands]
    drafts, gate, pn = build(a.article, a.heading, a.round, cands, a.section_march, a.note or a.round)
    out = pathlib.Path(a.out_prefix)
    out.with_name(out.name + '-drafts.json').write_text(json.dumps(drafts, indent=1, ensure_ascii=False), encoding='utf-8')
    out.with_name(out.name + '-gate.json').write_text(json.dumps(gate, indent=1, ensure_ascii=False), encoding='utf-8')
    rows = []
    for k, text in drafts.items():
        stem = k.split('_', 1)[1]
        words = len(text.split())
        if stem.startswith('pair'):
            what = f'P{pn - 1}+P{pn}, with {stem[4:]} ({words} words)'
        elif stem.startswith('sec'):
            what = f'{a.heading} with P{pn} = {stem[3:]} ({words} words)'
        else:
            what = f'{a.label}, {stem} alone ({words} words)'
        rows.append(f'| {a.date} | {what} [{k}], a screen | {a.prediction} | (pending) | |')
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_gate.py'), str(out.with_name(out.name + '-drafts.json')),
           str(out.with_name(out.name + '-gate.json')), str(out.with_name(out.name + '.js')), '--name', a.round,
           '--lint-article', a.article] + list(drafts)
    rc = subprocess.run(cmd).returncode
    if rc == 0:  # the prediction rows go in only for a batch the gate wrote
        p = pathlib.Path(a.predictions)
        p.write_text(p.read_text(encoding='utf-8').rstrip('\n') + '\n' + '\n'.join(rows) + '\n', encoding='utf-8')
    return rc


if __name__ == '__main__':
    sys.exit(main())
