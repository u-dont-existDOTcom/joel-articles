#!/usr/bin/env python3
"""predict.py - turn 67's predictions for the kidney paragraph (B120), written before the checks, through the API with his
key on his laptop. Two methods, each in its own lineage: a1, small fixes from his post's text by the ways of his round-55
fixes (the as-is text read AI High 100 in one window, df3704bf); w1, a second writer's (Haiku) rewrite from the tell panel
on that text (panel-b120/PANEL.md, two readers: Sonnet and Haiku; the Codex reader could not run this turn), vetted by me
for his words and with nothing added.

  python3 predict.py a1-b120 w1-b120
"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
REL = 'articles/bad-trips/humanize/h75-20261124/'
DET = 'Pangram API (pangram-4), his key, run on his laptop (tools/humanization/pangram_api.py)'
BATCH = 'h75b'
HUM = ('turn 66\'s three fresh reads of this paragraph inside the section (../h74-20261124/reads/*-a1-sec.txt) and this turn\'s '
       'tell panel on his post\'s text (panel-b120/PANEL.md): the agreed tells S2 to S5 each get a fix, the caution reads once, '
       'each "it" points at one thing')
P = {
    'a1': dict(lineage='bad-trips MDMA: Magnesium Alarm, the kidneys (B120) as it stands, by itself (h75)', call='AI', chance=0.3,
               tells=['That makes kidney impairment a strong reason not to take MDMA', 'People with impaired kidneys do need to be more cautious'],
               human=["I just wouldn't tell somebody with serious kidney impairment", "they still shouldn't sit there with worsening jaw tension"],
               first=('payoff: his bold lead first, then why the MDMA is the bigger danger to those kidneys; join: "since MDMA can cause", '
                      '"That makes", "although once they\'ve taken it", "I just wouldn\'t"; plain: "they still shouldn\'t sit there with worsening jaw tension"'),
               diag=('try 1, his post\'s paragraph as it stands, read AI High 100 in one window (df3704bf), and the tell panel on it '
                     '(panel-b120/PANEL.md, Sonnet and Haiku) agreed on four sentences: the stock pivot standing alone (S2), the tidy '
                     'four-item list (S3), the dash correction "--not a reason to" (S4) and the mirrored pair "I would not tell ...; I '
                     'would tell them" with its generic "treat the situation as higher-risk" (S5). This try fixes each with one of the '
                     'ways of his round-55 fixes and changes a third of the words: S2 runs on into what the MDMA can cause ("since"), '
                     'the list gets two shapes with the kidney injury first, the dash aside is its own clause after "although" with '
                     'one "it", and the pair is one sentence with its reason ("since that\'s a higher-risk situation")')),
    'w1': dict(lineage='bad-trips MDMA: Magnesium Alarm, the kidneys by a second writer from the tell panel (h75)', call='AI', chance=0.15,
               tells=['Kidney impairment is a strong reason to skip MDMA altogether.', 'But the MDMA should worry them far more.'],
               human=['the kidneys are no reason to sit there with it', 'Treat the situation as higher-risk and get help sooner.'],
               first=('payoff: who it is for, then the bigger danger; join: "But the MDMA", "It can cause", "Once someone has taken it"; '
                      'plain: "the kidneys are no reason to sit there with it"'),
               diag=('my three tries of turns 65 and 66 read Mixed, AI and AI (258a5b17, 230891b4, e2566e53) and his post\'s text reads '
                     'AI High 100 (df3704bf); the panel says the whole is built as caution, pivot, list, contrast, disclaimer. This is '
                     'another writer\'s rewrite from the panel\'s notes and his own lines (rewrite-b120/REWRITE-PROMPT.txt, Haiku), a '
                     'different method from mine: short plain statements, the advice as instructions, no mirrored pair and no dash. I '
                     'restored his bold lead, "more cautious" and the link, took out the writer\'s gloss of rhabdomyolysis (not his) '
                     'and "no excuse" (stronger than his "not a reason")')),
}


def run(key):
    k = key.split('-')[0]
    p = P[k]
    a = ['python3', 'tools/humanization/pangram_ledger.py', 'predict', L, '--lineage', p['lineage'], '--scope', 'paragraph',
         '--text', REL + 'TEST-%s.txt' % key, '--key', key, '--batch', BATCH, '--call', p['call'], '--chance', str(p['chance']),
         '--detector', DET, '--decides', ('whether %s reads Human High in every window by itself; if it does it goes in, and if not '
                                          'the paragraph goes to him as a teaching card with the panel and every try') % key,
         '--receipt', REL + 'TEST-%s.receipt.json' % key, '--humanized', HUM, '--first-fix', p['first'],
         '--diagnosis', p['diag'], '--panel', REL + 'panel-b120/PANEL.md']
    for t in p['tells']:
        a += ['--tells', t]
    for t in p['human']:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=str(REPO), capture_output=True, text=True)
    print(key, '|', (r.stdout + r.stderr).strip()[-900:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(max(run(k) for k in sys.argv[1:]))
