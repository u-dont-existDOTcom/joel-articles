#!/usr/bin/env python3
"""Check and deliver each gated draft (tools/humanization/owner_delivery_gate.py) once its three reviews are in, and write
GATE-OUTCOMES.json (each draft's reviewers' verdicts and whether the gate admitted it) and GATE.md (the same for Joel's
sessions). A draft a reviewer failed is not delivered, and its card doesn't go on his page. The same steps as
../../fix-20261025/emulate-check/gate/run_gate.py: deliver writes FOR-JOEL.txt and its proof once; a later run checks the
same files again.

  python3 articles/inner-signal/humanize/fix-20261026/gate/run_gate.py
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
sys.path.insert(0, str(HERE))
import make_gate_files as mg  # noqa: E402
ROLES = ('preservation', 'cold_read_1', 'cold_read_2')


def gate_md(inputs, res):
    out = ['# The owner-delivery gate for batches 479 and 480', '',
           'Made by `run_gate.py` (this folder); the numbers come from the review files. Main\'s owner-delivery gate '
           '(`docs/HUMANIZATION-OWNER-DELIVERY-GATE.md`): model-written words in Joel\'s byline, shown to him as a proposed '
           'revision, pass `tools/humanization/owner_delivery_gate.py deliver` first: the linter, the writer\'s tell ledger, '
           'and three reviewers, each a fresh agent with only its brief and the files (preservation, cold reader 1, cold '
           'reader 2). Here the words are Emulate\'s (with the splices\' small fixes, each named in `the_change`); the card '
           'for each delivered draft is on his marking page (`../review/REVIEW-480.json`).', '',
           '## Gated: %d drafts, %d delivered' % (len(inputs), sum(1 for n in inputs if res[n]['admitted'])), '',
           '| NAME | spot | the new words | preservation | cold reader 1 | cold reader 2 | delivered |',
           '| --- | --- | --- | --- | --- | --- | --- |']
    for n in inputs:
        d = pathlib.Path(inputs[n]['folder'])
        draft = (d / 'DRAFT.txt').read_text(encoding='utf-8').replace('|', '\\|')
        v = res[n]['reviews']
        batch, spot, _ = mg.DRAFTS[n]
        out.append('| %s | %s %s | %s | %s | %s | %s | %s |' % (n, batch, spot, draft, v['preservation'], v['cold_read_1'],
                                                            v['cold_read_2'], 'yes (`%s/FOR-JOEL.txt`)' % n if res[n]['admitted'] else 'no'))
    fails = [(n, r, '; '.join(json.loads((pathlib.Path(inputs[n]['folder']) / ('REVIEW-%s.json' % r)).read_text(encoding='utf-8'))['unresolved']))
             for n in inputs for r in ROLES if res[n]['reviews'][r] == 'FAIL']
    if fails:
        out += ['', 'What the reviewers failed:', '']
        out += ['- %s, %s: %s' % (n, r, why) for n, r, why in fails]
    out += ['', '## What changed during the gate', '',
            '- **G-S5.** Its first draft ended "Don\'t fake it." (batch 479\'s third sample, after "You don\'t have to fake '
            'it!" failed the linter\'s coach register). The preservation reviewer failed it: his line is a release ("no '
            'faking required") and the draft made it a rule (`superseded/G-S5-dont-fake-it/REVIEW-preservation.json`; the '
            'two cold readers had passed it). The new draft ends on his own three words, "no faking required", and went '
            'through all three roles again (`BRIEF-<role>-e.md`). Cold reader 1 of group b, which had read the first draft, '
            'also reviewed the new one when its files changed under it; group e\'s fresh cold reader 1 wrote after it, so the '
            'file on record is that fresh reader\'s (`G-S5/REVIEW-cold_read_1.json`, context id '
            '`b480-gate-cold_read_1-subagent-e`).',
            '- **G-S8 and G-S9** failed the linter before any review (E125, a list of three without a casual catch-all; R2, '
            'the paragraph\'s "This" made "It"), so each got the smallest fix first: IC-A14\'s own "or a bit of each" for '
            'Emulate\'s "or a combination", and "This" put back (`../b480/make_b480.py`). **G-S7** got his "keeps" back for '
            'Emulate\'s "helps to keep" on the meaning read (`../b480/REVIEW-1.md`).',
            '- **The writer\'s lint reasons.** Several reviewers noted that the D9 and B7 reasons in G-S2 to G-S6\'s manifests '
            'were written once for the batch and cite asides from other drafts ("if I can put it that way", "Don\'t fake '
            'it."); each reviewer judged those findings on the draft itself. G-S5\'s new draft and G-S7 to G-S10 have reasons '
            'written for each draft (`fill_ledgers.py` LINT_BY).', '',
            '## The reviewers', '']
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
    inputs = {n: inputs[n] for n in mg.DRAFTS if n in inputs}
    res = {}
    for n, x in inputs.items():
        d = pathlib.Path(x['folder'])
        files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
                 '--manifest', str(d / 'ADMISSION.json')]
        verdicts = {}
        for role in ROLES:
            p = d / ('REVIEW-%s.json' % role)
            verdicts[role] = json.loads(p.read_text(encoding='utf-8')).get('verdict') if p.exists() else 'missing'
        done = (d / 'FOR-JOEL.txt').exists() and (d / 'FOR-JOEL.proof.json').exists()
        extra = [] if done else ['--out', str(d / 'FOR-JOEL.txt'), '--proof', str(d / 'FOR-JOEL.proof.json')]
        out = subprocess.run([sys.executable, str(GATE), 'check' if done else 'deliver'] + files + extra,
                             capture_output=True, text=True)
        same = (d / 'FOR-JOEL.txt').exists() and (d / 'FOR-JOEL.txt').read_bytes() == (d / 'DRAFT.txt').read_bytes()
        res[n] = {'reviews': verdicts, 'admitted': out.returncode == 0 and same,
                  'delivered_at_utc': json.loads((d / 'FOR-JOEL.proof.json').read_text(encoding='utf-8'))['verified_at_utc']
                  if (d / 'FOR-JOEL.proof.json').exists() else None,
                  'gate': (out.stdout.strip() or out.stderr.strip())[-1500:].replace(str(ROOT) + '/', '')}
        print('%-6s %s %s' % (n, 'ADMITTED' if res[n]['admitted'] else 'BLOCKED', verdicts))
    (HERE / 'GATE-OUTCOMES.json').write_text(json.dumps(res, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    gate_md(inputs, res)


if __name__ == '__main__':
    main()
