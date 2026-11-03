"""An experiment, not a draft: the 5-HTP warning (block 17) with its warning phrases re-said too, checked by itself.

Its first try in his X-15 register (../, batch r1103e) read 100% AI, like both tries of the warnings stretch. One
difference from his X-15 is left: he re-said the warning phrases themselves ("without having a physician competent to
consider the likelihoods of problematic interactions" for "without clinician review"), which fidelity_keys.py lets only
his own words do (FIDELITY-KEYS.json, "owner_wording"), so every one of my tries kept the post's phrases ("without
clinician review", "be especially conservative", "repair-oriented"). This try re-says them, every compound kept. It can't
go into the article as it is: its warning words differ from the post's, so it would go to him as a card first.

  python3 articles/neuro-de-armoring/humanize/fix-20261103/r2his/para/try2/try2_p017.py
Writes TEXTS.json and PREDICTIONS.json here, and the prediction into the ledger first (batch r1103f).
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[3]
ROOT = H.parents[2]
LEDGER = H / 'pangram-ledger.jsonl'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218, E325: at most six paragraphs and 1,200 words)'
BATCH = 'r1103f'
KEY, LINEAGE = 'p017', 'ND1103-P017'
TEXT = ('Uridine & 5-HTP Warning for Psychedelic Users: Neither one is a “trip enhancer.” They’re repair tools, and either '
        'one can shift how sensitive your brain is fast. 5-HTP turns directly into serotonin, so stacking it with SSRIs, '
        'SNRIs, MAOIs, linezolid, lithium, tramadol, methadone, fentanyl, DXM, MDMA, St. John’s wort, SAM-e, L-tryptophan, '
        'or anything else that pushes serotonin up is off the table unless your prescriber has gone over the combination. '
        'Ayahuasca and harmalas are a bigger problem still, since their MAO-A inhibition can pile more serotonin on top, and '
        'so are iboga and ibogaine, where ibogaine and noribogaine act on serotonin transport and already come with serious '
        'heart and neurological risk.')
CHANCE = 0.3
WHY = ('the warning phrases re-said ("off the table unless your prescriber has gone over the combination", "a bigger '
       'problem still", "pile more serotonin on top"), but in my idioms, not his, and the drug list is as long as before')


def main():
    sha = hashlib.sha256(TEXT.encode('utf-8')).hexdigest()
    (HERE / 'TEXTS.json').write_text(json.dumps({KEY: TEXT}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'p017.txt').write_text(TEXT, encoding='utf-8')
    row = {'key': KEY, 'name': 'B017 by itself, its warning phrases re-said too (an experiment)', 'lineage': LINEAGE,
           'scope': 'paragraph', 'words': len(TEXT.split()), 'call': 'AI', 'chance': CHANCE, 'why': WHY, 'sha256': sha}
    (HERE / 'PREDICTIONS.json').write_text(json.dumps([row], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if any(json.loads(l).get('batch') == BATCH and json.loads(l).get('key') == KEY
           for l in LEDGER.read_text(encoding='utf-8').splitlines()):
        return
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                    '--lineage', LINEAGE, '--scope', 'paragraph', '--text', str(HERE / 'p017.txt'), '--call', 'AI',
                    '--chance', str(CHANCE), '--key', KEY, '--batch', BATCH, '--detector', DETECTOR, '--tells', WHY,
                    '--diagnosis', 'try 1 in his X-15 register kept the post\'s warning phrases, which the fidelity check holds for '
                    'my words but not his; his X-15 re-said them; this try re-says them too',
                    '--decides', 'whether the locked warning phrases are what keeps my warnings reading AI, so that re-saying them '
                    '(each shown to him first) is worth proposing'], check=True)


if __name__ == '__main__':
    main()
