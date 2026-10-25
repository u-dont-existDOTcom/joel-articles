#!/usr/bin/env python3
"""Round 2 of the reviewers' briefs (REVIEW-BRIEF.md with each role's text from round 1's BRIEF-<role>.md).

Round 1's cold reader 1 read all sixteen drafts before writing anything and stopped, after 46 minutes, with no review
written (it hit its output limit twice while thinking). Round 2 splits the ten drafts still gated (GATE-INPUTS.json) into
small groups, one fresh agent each, and asks for one NAME at a time, its file written before the next is opened. C-E3a's
context changed after round 1 (the card's other question is now his own words), so it gets all three roles again.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/gate/make_round2_briefs.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
GROUPS = {   # brief: (role, NAMEs)
    'cold_read_1-a': ('cold_read_1', ['G-EM2', 'G-EM5', 'G-EM9']),
    'cold_read_1-b': ('cold_read_1', ['G-EM14', 'G-EM15', 'G-EMS2']),
    'cold_read_1-c': ('cold_read_1', ['C-E2', 'C-E3a']),
    'cold_read_1-d': ('cold_read_1', ['C-E4', 'C-T1']),
    'preservation-e': ('preservation', ['C-E3a']),
    'cold_read_2-f': ('cold_read_2', ['C-E3a']),
}
NAMES = {'cold_read_1': 'Claude Sonnet, fresh subagent (cold reader 1)', 'cold_read_2': 'Claude Sonnet, fresh subagent (cold reader 2)',
         'preservation': 'Claude Sonnet, fresh subagent (preservation reviewer)'}


def role_text(role):
    b = (HERE / ('BRIEF-%s.md' % role)).read_text(encoding='utf-8')
    return b.split('## Your role\n\n', 1)[1].split('\n\n## For each NAME', 1)[0]


def main():
    tpl = (HERE / 'REVIEW-BRIEF.md').read_text(encoding='utf-8')
    inputs = json.loads((HERE / 'GATE-INPUTS.json').read_text(encoding='utf-8'))
    for key, (role, names) in GROUPS.items():
        assert all(n in inputs for n in names), names
        n = WORDS[len(names)]
        guide = [x for x in names if x.startswith('G-')]
        comm = [x for x in names if x.startswith('C-')]
        line = 'The NAMEs: ' + '; '.join(p for p in [', '.join(guide) + ' (the guide)' if guide else '',
                                                    ', '.join(comm) + ' (the community essay)' if comm else ''] if p) + '.'
        b = tpl.replace('ROLE_TEXT', role_text(role)).replace('ROLE_NAME', role).replace('REVIEWER_NAME', NAMES[role])
        b = b.replace('CONTEXT_ID', 'emulate-gate-%s-subagent-r2%s' % (role, key[-1]))
        b = b.replace('ORIGIN', 'Claude Agent tool subagent, model sonnet, a fresh context with only this brief and its files, launched '
                      '2026-10-25 by session_01Mxpoi6tFT3FgKmBvtGjRtS (the writer\'s session), round 2')
        b = re.sub(r'^The NAMEs: .*$', line, b, count=1, flags=re.M)
        b = b.replace('sixteen proposed sentence changes', '%s proposed sentence change%s' % (n, 's' if len(names) > 1 else ''))
        b = b.replace('When all sixteen files are written', ('When both files are written' if len(names) == 2 else 'When all %s files are written' % n) if len(names) > 1 else 'When the file is written')
        if not (guide and comm):
            b = b.replace('sentence change%s in two articles' % ('s' if len(names) > 1 else ''),
                          'sentence change%s in one article' % ('s' if len(names) > 1 else ''))
        b = b.replace('## For each NAME\n', '## For each NAME\n\nDo one NAME at a time: read its three files, judge it, and write its review file before you open the next NAME\'s files.\n', 1)
        assert 'sixteen' not in b and 'ROLE_' not in b and 'CONTEXT_ID' not in b, key
        (HERE / ('BRIEF-r2-%s.md' % key)).write_text(b, encoding='utf-8')
        print(key, names)


if __name__ == '__main__':
    main()
