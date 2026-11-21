#!/usr/bin/env python3
"""predict.py - turn 58's predictions (pangram_ledger.py predict) for the remedy headings he picked in round 47 with their
evidence tags and first paragraphs, and the Grounding Menu's renamed pointer, written before the checks.

  python3 predict.py [KEY...]
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h66-20261121/'
DET = "Pangram web app (his account), in the desktop app's browser pane"
BATCH = 'h66a'
UNCH = ('his round-47 heading for this remedy, the evidence tag his round-46 answer gave it on its own line under it (as the '
        'round-47 page showed it to him), and the section\'s first paragraph as the guide has it: no words of mine')
DECIDES = ('whether the evidence tag goes in under the heading he picked: Human High in every window, read the way the reader '
           'meets them (heading, tag, first paragraph); if not, the window says what the tag or heading does to the '
           'paragraph, and the tag waits')
P = {
    't1-coffee-1': ('Coffee Cherry', 'Human', 0.6, ['Tried by Me and Friends'], ['(Coffee Cherry for Brain also)']),
    't2-sniffer-1': ('Metta NMT Sniffer', 'Human', 0.6, ['Tried by Me and Friends'], ['Chill Love']),
    't3-humic-1': ('Humic Acid', 'Human', 0.55, ['Humic Acid for the Brain'], ['Tried by Me and Friends']),
    't4-creatine-mango-1': ('Creatine and Mango Leaf Tea', 'Human', 0.6, ['Creatine for Brain & Bliss'],
                            ['people keep thinking I mean snorting when I say smell']),
    't5-rue-1': ('Syrian Rue Oil', 'Human', 0.55, ['Syrian Rue Oil: Gentler'], ['Tried by Me and Friends']),
    't6-ocean-1': ('Ocean Water', 'Human', 0.55, ['Ocean Water Calms'], ['Tried by Me and Friends']),
    't7-shungite-1': ('Shungite and Holy Water', 'Human', 0.55, ['Tried by Me and Friends'],
                      ['I honestly can\'t say how different these are from ocean water']),
}
MENU = ('t8-menu-smell-1', 'Human', 0.5, ['Exhale longer than you inhale for ten breaths.'],
        ['Scratch & sniff a lime peel'])


def run(key):
    if key == MENU[0]:
        _, call, chance, tells, human = MENU
        lineage = 'bad-trips Grounding Menu Body, Smell and Breath (B297 to B302), the Smell line naming the stabilizers by its round-47 heading'
        flag = ('the Grounding Menu\'s Body, Smell and Breath parts as the guide has them, the Smell line naming the '
                'stabilizers section by the heading he picked in round 47 ("Too Intense? Stabilizers") instead of its old one')
        decides = 'whether the renamed pointer leaves the Grounding Menu at Human High; if not, which window it touched'
        scope = 'stretch'
    else:
        name, call, chance, tells, human = P[key]
        lineage = 'bad-trips remedy heading with its evidence tag and first paragraph: %s (round 47)' % name
        flag, decides, scope = UNCH, DECIDES, 'heading'
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', lineage, '--scope', scope,
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', call, '--chance', str(chance),
         '--detector', DET, '--decides', decides, '--unchanged', flag]
    for t in tells:
        a += ['--tells', t]
    for t in human:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out[:900] if r.returncode else out.splitlines()[-1][:200])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max([run(k) for k in (sys.argv[1:] or list(P) + [MENU[0]])] or [0]))
