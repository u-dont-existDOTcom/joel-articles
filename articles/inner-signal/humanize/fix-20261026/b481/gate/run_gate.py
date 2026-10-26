#!/usr/bin/env python3
"""Check and deliver each of batch 481's gated drafts (tools/humanization/owner_delivery_gate.py) once its three reviews are
in, and write GATE-OUTCOMES.json and GATE.md, the same steps as ../../gate/run_gate.py: deliver writes FOR-JOEL.txt and its
proof once; a later run checks the same files again. A draft a reviewer failed is not delivered, and its card doesn't go
on his page.

  python3 articles/inner-signal/humanize/fix-20261026/b481/gate/run_gate.py
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
NOTES = [   # what changed during the gate
    '**G-S14, G-S31 and G-S32 failed preservation in the first round** (G-S14 also cold reader 2; the files are in '
    '`superseded/`). G-S14: Emulate\'s FTC sentence said "their" dark patterns, "used to" and "trick and manipulate", where his '
    'line says designs that "trick or manipulate"; his words are back. G-S31: "this part knows it" lost his "remembers" (which '
    'his next line picks up) and "Try" lost his "works well here"; the new draft is Emulate\'s start ending on his "and that '
    'part remembers", and his next sentence stays. G-S32: Emulate dropped his "genuinely"; it is back. Each new draft went '
    'through all three roles again with fresh reviewers (groups i and j), with G-S15 and G-S30, whose sections changed with '
    'them (each context holds the other draft): `superseded/G-S15-first-context`, `superseded/G-S30-first-context`.',
    '**G-S36 failed preservation** in the first round: Emulate\'s "What boundaries do I need to set as a result?" dropped his '
    'published "still" and added a cause. That question stays as the working copy has it, and the new draft, only "What’s '
    'theirs and what’s mine?", went through all three roles again (group l): `superseded/G-S36-first-draft`.',
    '**Reviewers still at work when their folders moved.** Group h\'s three reviewers checked their files at the end, found '
    'the G-S33 and G-S34 reviews gone (the folders had moved to `superseded/` for the fixes) and wrote five of them again into '
    'the new folders, some with the new context\'s hashes. Those files are kept in `superseded/` as '
    '`*-rewritten-after-move.json`, the two agents still running were stopped, and the files on record are group k\'s, each checked by its context id. A folder moves only '
    'once every reviewer of it has finished.',
    '**G-S34 failed all three roles** in the first round on one mark: my fix of Emulate\'s "Lets" typo used a straight '
    'apostrophe where the section\'s other words have curly ones. The new draft has "Let’s", and it and G-S33 (whose section '
    'it is in) went through all three roles again (group k): `superseded/G-S34-first-draft`, `superseded/G-S33-first-context`.',
    '**The writer\'s T28 line.** Its stock text said each draft is not the end of its section; a reviewer of group f found it '
    'wrong for G-S27 and G-S29. `fill_ledgers.py` now says where a draft is in its section\'s last paragraph (G-S11, G-S12, '
    'G-S22, G-S27, G-S29); the line is the writer\'s claim, not part of the reviewed files. A reviewer of group d found '
    'the same for T14 and T15, whose stock lines (from the gate where each draft put his words back) said each draft "puts '
    'back" his point; they now say what these drafts are, Emulate\'s own wording, with his words back where the_change '
    'says. The reviewers judged the rows on the drafts, not on those lines. G-S32\'s D9 note still quoted its first draft '
    '(without "genuinely"); a second-round reviewer caught it, and the draft was delivered again with the note fixed (the '
    'first delivery\'s files: `superseded/G-S32-delivered-with-stale-reason`).',
    '**Where reviewers and the writer differ on a row.** All three of G-S33\'s second-round reviewers found T19 (an announcing '
    'set-up) present and justified: "Here is a little script you could use:" leads into the script, as the line it replaces '
    'did. The writer\'s ledger says absent; the delivered manifest is left as it was, and the reviewers\' judgment is the one '
    'on record. G-S25\'s cold reader 1 found T02 (a run of commands) present and justified the same way, and G-S32\'s '
    'second-round preservation reviewer T26 ("Ethical Double Bind Question" just before the paragraph\'s "Ethical Double Bind '
    'Questions might be:"; the section\'s defined term).',
    '**What the reviewers had in their context.** Each was a fresh Sonnet subagent with its brief and the files it names, '
    'but the harness also loads the repository\'s standing instructions (CLAUDE.md, AGENTS.md) for every agent, so the '
    '"only this brief and its files" in each review file\'s reviewer.origin (copied from the brief) is not literally true. '
    'Several reviewers said so; two took clock readings for those instructions\' timestamp rule. Their judgments rest on the '
    'brief\'s files and the tell inventory.',
]


def gate_md(inputs, res):
    out = ['# The owner-delivery gate for batch 481', '',
           'Made by `run_gate.py` (this folder); the numbers come from the review files. Main\'s owner-delivery gate '
           '(`docs/HUMANIZATION-OWNER-DELIVERY-GATE.md`): model-written words in Joel\'s byline, shown to him as a proposed '
           'revision, pass `tools/humanization/owner_delivery_gate.py deliver` first: the linter, the writer\'s tell ledger, '
           'and three reviewers, each a fresh agent with only its brief and the files (preservation, cold reader 1, cold '
           'reader 2). Here the words are Emulate\'s (with the splices\' small fixes, each named in `the_change`), for the '
           'windows that read Human at less than High confidence in batch 480\'s recheck; the card for each delivered draft '
           'is on his marking page (`../../review/REVIEW-481.json`).', '',
           '## Gated: %d drafts, %d delivered' % (len(inputs), sum(1 for n in inputs if res[n]['admitted'])), '',
           '| NAME | spot | his words? | the new words | preservation | cold reader 1 | cold reader 2 | delivered |',
           '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for n in inputs:
        d = pathlib.Path(inputs[n]['folder'])
        draft = (d / 'DRAFT.txt').read_text(encoding='utf-8').replace('|', '\\|')
        v = res[n]['reviews']
        spot, _ = mg.DRAFTS[n]
        out.append('| %s | %s | %s | %s | %s | %s | %s | %s |' % (
            n, spot, 'his' if inputs[n].get('his') else '', draft, v['preservation'], v['cold_read_1'], v['cold_read_2'],
            'yes (`%s/FOR-JOEL.txt`)' % n if res[n]['admitted'] else 'no'))
    fails = [(n, r, '; '.join(json.loads((pathlib.Path(inputs[n]['folder']) / ('REVIEW-%s.json' % r)).read_text(encoding='utf-8'))['unresolved']))
             for n in inputs for r in ROLES if res[n]['reviews'][r] == 'FAIL']
    if fails:
        out += ['', 'What the reviewers failed:', '']
        out += ['- %s, %s: %s' % (n, r, why) for n, r, why in fails]
    if NOTES:
        out += ['', '## What changed during the gate', ''] + ['- ' + x for x in NOTES]
    out += ['', '## The reviewers', '']
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
