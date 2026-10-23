#!/usr/bin/env python3
"""Turn 103, second round.
(a) Diagnostics: the four paragraphs that read AI or Mixed alone after their cut (97.8, 97.12, 98.2, 98.7), as they were
    before the cut, alone: Human means the cut caused it, AI means the paragraph read AI alone anyway.
(b) Sections or five-paragraph stretches (E231) for every cut whose paragraph passed alone or is under 50 words, for his
    96.1 paragraph (it passed his own check), and for The Inner Guide's first two new h2s. Held back until their paragraph
    is fixed: Not Every Hero Wears A Cape (98.2), When to Change the Strategy (98.7), When Escape Leaves Reality Behind
    (97.7 and 97.8) and The Inner Guide's A Belonging Deeper Than Any Group (97.12 and 98.9).
Writes TEXTS-2.json."""
import json
import pathlib

from make_texts import line, seq, AFTER

HERE = pathlib.Path(__file__).resolve().parent


def at(start, kind=None):
    hits = [i for i, (k, b) in enumerate(seq) if b.startswith(start) and (kind is None or k == kind)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


def section(head):
    """The heading and its body up to the next heading at its level or above (sub-headings included)."""
    i = at(head, 'h')
    lvl = len(head) - len(head.lstrip('#'))
    j = i + 1
    while j < len(seq) and not (seq[j][0] == 'h' and len(seq[j][1]) - len(seq[j][1].lstrip('#')) <= lvl):
        j += 1
    return seq[i:j]


def section_until_sub(head):
    """The heading and its own paragraphs, up to its first sub-heading."""
    i = at(head, 'h')
    j = i + 1
    while j < len(seq) and seq[j][0] != 'h':
        j += 1
    return seq[i:j]


def stretch(start, before=2, after=2):
    i = at(start, 'p')
    a, b = i, i
    for _ in range(before):
        if a - 1 >= 0 and seq[a - 1][0] == 'p':
            a -= 1
    for _ in range(after):
        if b + 1 < len(seq) and seq[b + 1][0] == 'p':
            b += 1
    return seq[a:b + 1]


DIAG = {'t103b_97_8_old': '97.8', 't103b_97_12_old': '97.12', 't103b_98_2_old': '98.2', 't103b_98_7_old': '98.7'}
TEXTS = {n: [('p', AFTER[i]['before'])] for n, i in DIAG.items()}
TEXTS.update({
    't103b_body_h2': section('## Your Body Might Need Some Love First'),
    't103b_monologue_h2': section('## You Don’t Need an Inner Monologue'),
    't103b_blame_h3': section('### Instead of Blame'),
    't103b_hook_h2': section('## Catch the Hook Before the Story Takes Over'),
    't103b_journal_h2': section('## Journal With Each Hand'),
    't103b_justlike_h2': section('## Just Like Me'),
    't103b_sowhat_h2': section('## “And So That’s the Way It Happened!”'),
    't103b_whatever_stretch': stretch('Or if you do get an answer'),
    't103b_altered_intro_stretch': stretch('Remember those guards'),
    't103b_requires_stretch': stretch('If a voice or urge is directing', before=4, after=0),
    't103b_kill_stretch': stretch("But if you're still thinking of staking", before=2, after=2),
    't103b_untangle_stretch': stretch('What I found, once I started'),
    't103b_fourpairs_stretch': stretch('Differentiation is slow, and it goes on your whole life.', before=3, after=1),
    't103b_ig_spoiling_h2': section('## Between Spoiling and Clamping Down'),
    't103b_ig_perfect_h2': section('## A Healthy Mind Is Not a Perfect Mind'),
    't103b_happiness_h1': section('# How Much Happiness Do You Know Is Possible?'),
    't103b_firstsocial_h2': section_until_sub('## First Social Connections, Done Right'),
    't103b_speak_h2': section('## Speak Toward What You Are Building'),
    't103b_ended_h1': section('# When One Life Has Ended and the Next Hasn’t Begun'),
})
NAMES = {
    't103b_97_8_old': '97.8\'s paragraph (When Escape Leaves Reality Behind) as it was before the cut, alone (a diagnostic)',
    't103b_97_12_old': '97.12\'s paragraph (The Inner Guide P10) as it was before the cut, alone (a diagnostic)',
    't103b_98_2_old': '98.2\'s paragraph, your Not Every Hero Wears A Cape P5, as it was before the cut, alone (a diagnostic)',
    't103b_98_7_old': '98.7\'s paragraph (When to Change the Strategy P5) as it was before the cut, alone (a diagnostic)',
    't103b_body_h2': 'Your Body Might Need Some Love First, with 97.1',
    't103b_monologue_h2': 'You Don\'t Need an Inner Monologue, with 98.1',
    't103b_blame_h3': 'Instead of Blame, with 98.3 and 98.4',
    't103b_hook_h2': 'Catch the Hook Before the Story Takes Over, with 97.2 and 97.3',
    't103b_journal_h2': 'Journal With Each Hand, with 98.5',
    't103b_justlike_h2': 'Just Like Me, with 97.4',
    't103b_sowhat_h2': '"And So That\'s the Way It Happened!", with 98.6',
    't103b_whatever_stretch': 'Start With Whatever Showed Up, five paragraphs around 97.5',
    't103b_altered_intro_stretch': 'Altered States Can Deepen the Therapy, five paragraphs around 97.6',
    't103b_requires_stretch': 'Altered States Can Require Reparenting, the five paragraphs ending with 97.9',
    't103b_kill_stretch': 'If You Want to Kill Yourself, five paragraphs with 97.10 and 97.11',
    't103b_untangle_stretch': 'Untangling the Belonging Bargains, five paragraphs around 98.8',
    't103b_fourpairs_stretch': 'Four Pairs That Commonly Hook the Child, five paragraphs with your 96.1 paragraph',
    't103b_ig_spoiling_h2': 'The Inner Guide\'s new h2 Between Spoiling and Clamping Down (99 A)',
    't103b_ig_perfect_h2': 'The Inner Guide\'s new h2 A Healthy Mind Is Not a Perfect Mind (99 A)',
    't103b_happiness_h1': 'How Much Happiness Do You Know Is Possible?, the h1 with its two h2s, with 97.13 (Somatic Heart Opening)',
    't103b_firstsocial_h2': 'First Social Connections, Done Right, its own three paragraphs, with 97.14',
    't103b_speak_h2': 'Speak Toward What You Are Building, with 98.10',
    't103b_ended_h1': 'When One Life Has Ended and the Next Hasn\'t Begun, with 98.11 and 97.15',
}

if __name__ == '__main__':
    out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
    (HERE / 'TEXTS-2.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    names = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))
    names.update(NAMES)
    (HERE / 'NAMES.json').write_text(json.dumps(names, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for n, t in out.items():
        (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
        print('%-28s %4d words, %d blocks | %s' % (n, len(t.split()), len(TEXTS[n]), t[:60].replace('\n', ' / ')))
