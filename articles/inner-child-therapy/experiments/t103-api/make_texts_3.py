#!/usr/bin/env python3
"""Turn 103, third round.
- 97.8's paragraph read AI after the cut and Human before it (#171): the cut took its one first-person line, so draft s01
  puts the two instructions in his first person ("I'd get", "I wouldn't", "I'd ask"), points unchanged.
- 98.7's paragraph read AI before the cut too (#174), so it's rewritten (draft s02): the march after the relapse (the usual
  guess, my double denial, the reframe, the in-there/out-here instruction, the payoff) cut down, every point kept.
- 97.12: P10 read AI after the cut and Human before it (#172). GPT's idea, for question 100: the naming aside moves to right
  after P1, so P10 ends on belonging. Both halves checked: P10 without the aside, alone, and the h1's opening with the
  aside as its own short paragraph after P1.
- Four sections read Mixed (Low windows) after their cuts: each as it was before the cuts (the article at the last commit,
  before this turn's install), to see whether the cut caused it. Each is its section's second and last API try.
Writes TEXTS-3.json."""
import json
import pathlib
import re
import subprocess

from make_texts import line, seq, ROOT
from make_texts_2 import at, section, section_until_sub, stretch
import make_texts_2 as m2

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent / 't103-tries' / 'drafts'
from paragraphs_alone import reader_blocks  # noqa: E402
old_md = subprocess.run(['git', 'show', 'HEAD:articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'], cwd=ROOT,
                        capture_output=True, text=True, check=True).stdout
old_seq = reader_blocks(re.sub(r'<!--.*?-->', '', old_md, flags=re.S))


def old(fn, *args, **kw):
    """Run one of make_texts_2's section helpers on the article as it was before this turn's install."""
    saved = m2.seq
    m2.seq = old_seq
    try:
        return fn(*args, **kw)
    finally:
        m2.seq = saved


def draft(name):
    return [('p', (D / name).read_text(encoding='utf-8').strip())]


i_h1 = at('# The Inner Guide', 'h')
TEXTS = {
    't103c_97_8_s01': draft('s01-97_8.txt'),
    't103c_98_7_s02': draft('s02-98_7.txt'),
    't103c_97_12_p10': draft('s03-97_12-p10.txt'),
    't103c_ig_opening_aside': [seq[i_h1], seq[i_h1 + 1]] + draft('s04-naming-aside.txt'),
    't103c_monologue_old': old(section, '## You Don’t Need an Inner Monologue'),
    't103c_kill_old': old(stretch, "But if you're still thinking of staking", before=2, after=2),
    't103c_firstsocial_old': old(section_until_sub, '## First Social Connections, Done Right'),
    't103c_speak_old': old(section, '## Speak Toward What You Are Building'),
}
NAMES = {
    't103c_97_8_s01': '97.8\'s paragraph rewritten in your first person, with the cut kept (draft s01), alone',
    't103c_98_7_s02': '98.7\'s paragraph rewritten, with the cut kept (draft s02), alone',
    't103c_97_12_p10': 'The Inner Guide P10 without the naming aside (GPT\'s move, question 100), alone',
    't103c_ig_opening_aside': 'The Inner Guide\'s opening with the naming aside after P1 (GPT\'s move, question 100)',
    't103c_monologue_old': 'You Don\'t Need an Inner Monologue as it was before 98.1\'s cut (a diagnostic)',
    't103c_kill_old': 'If You Want to Kill Yourself, the same five paragraphs before 97.10 and 97.11 (a diagnostic)',
    't103c_firstsocial_old': 'First Social Connections, Done Right before 97.14\'s cut (a diagnostic)',
    't103c_speak_old': 'Speak Toward What You Are Building before 98.10\'s cut (a diagnostic)',
}

if __name__ == '__main__':
    out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
    (HERE / 'TEXTS-3.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    names = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
    names.update(NAMES)
    (HERE / 'NAMES.json').write_text(json.dumps(names, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for n, t in out.items():
        (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
        print('%-26s %4d words, %d blocks | %s' % (n, len(t.split()), len(TEXTS[n]), t[:60].replace('\n', ' / ')))
