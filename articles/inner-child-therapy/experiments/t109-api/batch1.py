#!/usr/bin/env python3
"""Turn 109, API batch 1: the first checks of what turn 109 installed (experiments/t109-installs/apply_t109.py), each
paragraph of 50 words or more alone and then its section, the predictions written to the ledger first.

  105.1  his own end of How This Relates to IFS (his friend Pink's account), alone and in the section
  105.2  his own start of Use Childhood Photographs Gently: P1 (30 words, so only in the section) and P2, alone and in it
  104 A  Hear the Guard First in its new shape: the four paragraphs of 50 words or more whose sentences moved (P1, P3, P4
         and P5; P6 and P7 are as they were), alone, and the section"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0]]
import make_texts as M  # noqa: E402

ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
BATCH = 't109-api-1'
texts, names, preds = {}, {}, {}


def add(name, text, desc, lineage, scope, chance, diagnosis, tells='none named', human='his words'):
    texts[name], names[name] = text, desc
    preds[name] = (lineage, scope, chance, diagnosis, tells, human)


add('t109_ifs_p8', M.para('And the parts just keep coming'), 'How This Relates to IFS, its last paragraph, his own text of 105.1, alone',
    't109-ifs-pink', 'paragraph', 0.6,
    'his own text, first check; the list of parts with its ellipsis was one of the panel\'s tells in my version, but here it leads into his friend\'s actual case, which is what the panel said was missing',
    tells='the list of parts with an ellipsis; "thus"', human='his friend Pink and her own account; his verdict in his words')
add('t109_sec_ifs', M.h2('How This Relates to IFS'), 'How This Relates to IFS, the whole section, with his text at the end',
    't106-sec-ifs', 'section', 0.5,
    'the old last paragraph read AI inside half B in rounds 5 and 6, the section alone read Human in turn 106; with his text in its place, no AI window')
add('t109_photos_p2', M.para('While you look, notice any new feelings'), 'Use Childhood Photographs Gently P2, his two new first sentences of 105.2 and the rest as it was, alone',
    't109-photos-p2', 'paragraph', 0.6,
    'his two sentences replace my redundant start; the rest of the paragraph is his turn-81 text that read Human before',
    human='his "feather touch" from Pema Chödrön; his "family/friends"; his "You hated that coat"')
add('t109_sec_photos', M.h2('Use Childhood Photographs Gently'), 'Use Childhood Photographs Gently, the whole section, with his new first paragraph and P2 start',
    't106-sec-photos', 'section', 0.55,
    'the section read Human through the API in turn 106; round 6 flagged only the old opener (Low, in half A), which is his sentence now')
add('t109_guard_p1', M.para('Whichever protective part showed up'), 'Hear the Guard First P1 (the plain path), alone',
    't109-guard-plain', 'paragraph', 0.6,
    'four of his sentences (the question, "Tell me what you remember", the Nurturer line and "Peek-a-boo!") after my two plain-path sentences; first check in this order',
    tells='the instruction-led first two sentences', human='his question and his "Peek-a-boo!"')
add('t109_guard_p3', M.para('That part might say this will just be one more performance'), 'Hear the Guard First P3 (one more performance), alone',
    't109-guard-performance', 'paragraph', 0.6,
    'his performance sentences with my sting and fooled-before lines; every sentence was in the section before, in another order',
    human='his "Even if you didn\'t win an Emmy last year"')
add('t109_guard_p4', M.para('That part doesn'), 'Hear the Guard First P4 (it doesn\'t have to move out), alone',
    't109-guard-moveout', 'paragraph', 0.55,
    'the roommate-free half of the old P3 and P4 joined; the ST-CA citation and the blinds image are his choices',
    tells='"It doesn\'t have to be all or nothing, either."', human='the blinds image; the citation')
add('t109_guard_p5', M.para('If it\'s been calling all this stupid'), 'Hear the Guard First P5 (scared of getting its hopes up), alone',
    't109-guard-hopes', 'paragraph', 0.5,
    'four short sentences that were the end of the old P4; first check alone',
    tells='"I wouldn\'t want to get mine up either." could read as a stake added for effect', human='the quoted line to the part')
# Hear the Guard First's section check waits: the point-of-view read flagged "I'd still keep it the same." in its P2, and my pick there changes the section, so it is checked once he has decided (project-sources/PRODUCTION-HUMANIZATION-PREFLIGHT.md: resolve the flag before spending credits).
# add('t109_sec_guard', M.h2('Hear the Guard First'), 'Hear the Guard First, the whole section in its new shape',
#     't109-sec-guard', 'section', 0.5,
#     'every sentence was in the section that read Human inside round 6\'s half B; only the order and the breaks changed, so it should read Human, though the order is new to the detector')

(HERE / 'TEXTS-1.json').write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, x in texts.items():
    (HERE / 'texts' / (n + '.txt')).write_text(x, encoding='utf-8')
allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8')) if (HERE / 'NAMES.json').exists() else {}
allnames.update(names)
(HERE / 'NAMES.json').write_text(json.dumps(allnames, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
if '--dry' in sys.argv or '--dry' in sys.orig_argv:
    for n, x in texts.items():
        print('%-18s %4d words | %s' % (n, len(x.split()), x[:90].replace('\n', ' / ')))
    sys.exit(0)
for n, (lin, scope, chance, diag, tells, human) in preds.items():
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER), '--lineage', lin, '--scope', scope,
           '--text', str(HERE / 'texts' / (n + '.txt')), '--call', 'Human', '--chance', str(chance), '--tells', tells,
           '--human-tells', human, '--diagnosis', diag, '--decides', 'whether the turn-109 install stays as it is', '--key', n,
           '--batch', BATCH]
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    print(out.stdout.strip().split('\n')[-1])
