#!/usr/bin/env python3
"""Turn 113, gate round 3: GATE-INPUTS-R3.json, what each reviewer needs beside the folder's files (the change in words, the
three hashes their report must carry, the linter's findings with the writer's reasons, and the rows the writer marked PRESENT
but kept), and the reviewer briefs, in small batches (round 1's long batches ran reviewers out of output room).

  python3 make_inputs_r3.py"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
from make_gate_files_r3 import R3  # noqa: E402

inputs = {}
for name in R3:
    d = HERE / name
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    assert m['status'] == 'READY_FOR_CHECK', name
    inputs[name] = {
        'the_change': (d / 'CHANGE.txt').read_text(encoding='utf-8').strip(),
        'candidate_sha256': m['candidate_sha256'], 'context_sha256': m['context_sha256'], 'source_sha256': m['source_sha256'],
        'lint_findings': [{'label': f['label'], 'examples': f['examples'], 'writer_reason': f.get('reason', '')} for f in m['lint']['findings']],
        'writer_marked_present': [{'id': r['id'], 'evidence': r['evidence'], 'reason': r.get('reason', '')}
                                  for r in m['tell_ledger'] if r['status'] == 'PRESENT'],
    }
(HERE / 'GATE-INPUTS-R3.json').write_text(json.dumps(inputs, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

names = list(R3)
BATCHES = {  # role: {batch: names}
    'preservation': {'r3a': names[:10], 'r3b': names[10:]},
    'cold_read_1': {'r3a': names[:10], 'r3b': names[10:]},
    'cold_read_2': {'r3a': names[0:3], 'r3b': names[3:6], 'r3c': names[6:9], 'r3d': names[9:12], 'r3e': names[12:15], 'r3f': names[15:]},
}
template = (HERE / 'BRIEF-cold_read_2-r2a.md').read_text(encoding='utf-8')
ROLE_TEXT = {}
for role, f in (('preservation', 'BRIEF-preservation-r2.md'), ('cold_read_1', 'BRIEF-cold_read_1-r2.md'), ('cold_read_2', 'BRIEF-cold_read_2-r2a.md')):
    t = (HERE / f).read_text(encoding='utf-8')
    ROLE_TEXT[role] = t[t.index('## Your role'):t.index('## For each NAME')]
LABEL = {'preservation': 'preservation reviewer', 'cold_read_1': 'cold read 1 reviewer', 'cold_read_2': 'cold read 2 reviewer'}
CID = {'preservation': 'preservation', 'cold_read_1': 'cold-read-1', 'cold_read_2': 'cold-read-2'}
ROUND_NOTE_OLD = template[template.index('This is the second round:'):template.index('Work efficiently:')]
ROUND_NOTE = ('This is the third and last round: after a cold read of each whole section, every case heading became a small '
              '(####) heading, some headings were reworded or added, and some paragraphs split, so each folder holds its section '
              'as it reads now. Some NAMEs are headings whose words did not change but whose section did; judge them where they '
              'are now. ')
written = []
for role, batches in BATCHES.items():
    for b, ns in batches.items():
        t = template.replace('GATE-INPUTS-R2.json', 'GATE-INPUTS-R3.json')
        t = t.replace(t[t.index('## Your role'):t.index('## For each NAME')], ROLE_TEXT[role])
        t = t.replace('Your NAMEs: start-thoughts-r2, start-anxiety-r2, start-stop, hooks-change-r2.', 'Your NAMEs: %s.' % ', '.join(ns))
        t = t.replace('REVIEW-cold_read_2.json', 'REVIEW-%s.json' % role).replace('"role": "cold_read_2"', '"role": "%s"' % role)
        t = t.replace('Claude Sonnet, fresh subagent (cold read 2 reviewer, r2a)', 'Claude Sonnet, fresh subagent (%s, %s)' % (LABEL[role], b))
        t = t.replace('t113-gate-cold-read-2-r2a-subagent', 't113-gate-%s-%s-subagent' % (CID[role], b))
        t = t.replace('turn 113, 2026-10-25', 'turn 113, 2026-10-26')
        t = t.replace(ROUND_NOTE_OLD, ROUND_NOTE)
        t = t.replace('), except NAME solomon, which is one of Joel\'s sentences with a few words changed at his request.', ').')
        t = t.replace(' (for a heading, the paragraphs it stands over, as they are now; for solomon, Joel\'s sentence and the study it links)',
                      ' (the paragraphs the heading stands over, as they are now)')
        t = t.replace(' For the one sentence (NAME solomon): does it keep every word and voice marker of Joel\'s sentence except the change '
                      '`the_change` describes, and is the change true to the study it links? Anything lost, added or changed beyond that is a FAIL.', '')
        assert 'solomon' not in t, (role, b)
        assert 'r2' not in t.replace('GATE-INPUTS-R3', ''), (role, b)
        out = HERE / ('BRIEF-%s-%s.md' % (role, b))
        out.write_text(t, encoding='utf-8')
        written.append((out.name, ns))
for n, ns in written:
    print(n, len(ns), ns)
