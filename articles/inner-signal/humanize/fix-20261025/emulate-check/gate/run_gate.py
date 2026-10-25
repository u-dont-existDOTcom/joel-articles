#!/usr/bin/env python3
"""Check and deliver each gated sentence (tools/humanization/owner_delivery_gate.py) once its three reviews are in, and
write GATE-OUTCOMES.json (each candidate's reviewers' verdicts and whether the gate admitted it) and GATE.md (the same for
Joel's sessions: what was gated, what was withdrawn and why, and the cards that stay outside the gate). A candidate a
reviewer failed is not delivered; the card shows his own words instead.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/gate/run_gate.py
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
sys.path.insert(0, str(HERE))
import make_gate_files as mg  # noqa: E402
ROLES = ('preservation', 'cold_read_1', 'cold_read_2')
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(ROOT))


def gate_md(inputs, res):
    cards = {}
    for page, (rpath, _gdir) in mg.PAGES.items():
        for c in json.loads(rpath.read_text(encoding='utf-8'))['suggestions']:
            cards[c['id']] = (page, c)
    gated = {mg.DRAFTS[n][1] for n in inputs}
    withdrawn = {mg.DRAFTS[n][1] for n in mg.WITHDRAWN}
    out = ['# The owner-delivery gate for the two Emulate check pages', '',
           'Made by `run_gate.py` (this folder); the numbers come from the review files. Main\'s owner-delivery gate '
           '(`docs/HUMANIZATION-OWNER-DELIVERY-GATE.md`, 2026-10-25 17:44 UTC): model-written words in Joel\'s byline, '
           'shown to him as a proposed revision, pass `tools/humanization/owner_delivery_gate.py deliver` first: the '
           'linter, the writer\'s tell ledger, and three reviewers, each a fresh agent with only its brief and the files '
           '(preservation, cold reader 1, cold reader 2). His own words are exempt. The pages: the hypnosis guide\'s '
           '(`../REVIEW-EMULATE.json`) and the community article\'s '
           '(`articles/intentional-communities/candidate/joel-20261025/emulate-check/REVIEW-EMULATE.json`).', '',
           '## Gated: %d drafts, %d delivered' % (len(inputs), sum(1 for n in inputs if res[n]['admitted'])), '',
           '| NAME | card | the new words | preservation | cold reader 1 | cold reader 2 | delivered |',
           '| --- | --- | --- | --- | --- | --- | --- |']
    for n in inputs:
        d = pathlib.Path(inputs[n]['folder'])
        draft = (d / 'DRAFT.txt').read_text(encoding='utf-8').replace('|', '\\|')
        v = res[n]['reviews']
        out.append('| %s | %s | %s | %s | %s | %s | %s |' % (n, mg.DRAFTS[n][1], draft, v['preservation'], v['cold_read_1'],
                                                         v['cold_read_2'], 'yes (`%s/FOR-JOEL.txt`)' % n if res[n]['admitted'] else 'no'))
    fails = [(n, r, '; '.join(json.loads((pathlib.Path(inputs[n]['folder']) / ('REVIEW-%s.json' % r)).read_text(encoding='utf-8'))['unresolved']))
             for n in inputs for r in ROLES if res[n]['reviews'][r] == 'FAIL']
    if fails:
        out += ['', 'What the reviewers failed (each card then shows his own words, or a new draft goes through again):', '']
        out += ['- %s, %s: %s' % (n, r, why) for n, r, why in fails]
    out += ['', '## Withdrawn after round 1: the card shows his own words', '', '| NAME | card | why |', '| --- | --- | --- |']
    out += ['| %s | %s | %s |' % (n, mg.DRAFTS[n][1], why) for n, why in mg.WITHDRAWN.items()]
    out += ['', '## Outside the gate: his own words, a word or mark of his, or quote marks off', '', '| card | page | title | what it does |',
            '| --- | --- | --- | --- |']
    for cid, (page, c) in cards.items():
        if cid in gated or (cid in withdrawn and cid not in gated):
            continue
        out.append('| %s | %s | %s | %s |' % (cid, page, c['title'].replace('|', '\\|'), c.get('advice_note', '').replace('|', '\\|')))
    only_his = sorted(withdrawn - gated)
    out += ['', 'Cards whose only drafts were withdrawn, so they now carry his own words: %s.' % ', '.join(only_his)]
    out += ['', '## Rounds', '',
            '- Round 1 (`GATE-INPUTS-ROUND1.json`, sixteen drafts, `BRIEF-<role>.md`): the preservation reviewer and cold reader 2 '
            'wrote all sixteen reviews. Cold reader 1 read all sixteen drafts before writing anything, hit its output limit '
            'twice while thinking, and was stopped at 21:58 UTC after 46 minutes with no review written. Six drafts were '
            'withdrawn on round 1\'s fails (above).',
            '- Round 2 (`make_round2_briefs.py`, `BRIEF-r2-*.md`, `GATE-INPUTS.json`): the ten drafts left, in four groups, one '
            'fresh cold reader 1 each, one NAME at a time with its file written before the next. C-E3a\'s context changed '
            'after round 1 (its card\'s other question became his own words), so it got all three roles again; its round-1 '
            'files are in `C-E3a/superseded/`.', '', '## The reviewers', '']
    seen = {}
    for n in inputs:
        for r in ROLES:
            p = pathlib.Path(inputs[n]['folder']) / ('REVIEW-%s.json' % r)
            if p.exists():
                rv = json.loads(p.read_text(encoding='utf-8'))['reviewer']
                seen.setdefault((r, rv['context_id']), []).append(n)
    out += ['- %s, `%s`: %s' % (r, cid, ', '.join(ns)) for (r, cid), ns in sorted(seen.items())]
    (HERE / 'GATE.md').write_text('\n'.join(out) + '\n', encoding='utf-8')


def main():
    inputs = json.loads((HERE / 'GATE-INPUTS.json').read_text(encoding='utf-8'))
    res = {}
    for n, x in inputs.items():
        d = pathlib.Path(x['folder'])
        files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
                 '--manifest', str(d / 'ADMISSION.json')]
        verdicts = {}
        for role in ('preservation', 'cold_read_1', 'cold_read_2'):
            p = d / ('REVIEW-%s.json' % role)
            verdicts[role] = json.loads(p.read_text(encoding='utf-8')).get('verdict') if p.exists() else 'missing'
        # deliver writes FOR-JOEL.txt and its proof once (it refuses to replace them, and the proof carries its time);
        # on a later run, check validates the same files again and FOR-JOEL.txt must still be the draft's bytes
        done = (d / 'FOR-JOEL.txt').exists() and (d / 'FOR-JOEL.proof.json').exists()
        extra = [] if done else ['--out', str(d / 'FOR-JOEL.txt'), '--proof', str(d / 'FOR-JOEL.proof.json')]
        out = subprocess.run([sys.executable, str(GATE), 'check' if done else 'deliver'] + files + extra,
                             capture_output=True, text=True)
        same = (d / 'FOR-JOEL.txt').exists() and (d / 'FOR-JOEL.txt').read_bytes() == (d / 'DRAFT.txt').read_bytes()
        res[n] = {'reviews': verdicts, 'admitted': out.returncode == 0 and same,
                  'delivered_at_utc': json.loads((d / 'FOR-JOEL.proof.json').read_text(encoding='utf-8'))['verified_at_utc']
                  if (d / 'FOR-JOEL.proof.json').exists() else None,
                  'gate': (out.stdout.strip() or out.stderr.strip())[-1500:].replace(str(ROOT) + '/', '')}
        print('%-8s %s %s' % (n, 'ADMITTED' if out.returncode == 0 else 'BLOCKED', verdicts))
    (HERE / 'GATE-OUTCOMES.json').write_text(json.dumps(res, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    gate_md(inputs, res)


if __name__ == '__main__':
    main()
