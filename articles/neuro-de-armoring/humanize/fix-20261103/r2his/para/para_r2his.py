"""Warnings in the register of his X-15, one paragraph at a time (after both tries of the warnings stretch read 100% AI).

Try 1 of stretch V1 kept the post's phrases inside his sentence build; try 2 re-said each phrase in a chatty voice ("Don't
think of these as", "I'd be extra conservative"). Both read 100% AI in one High window. His X-15 did neither: it is a
supplement label's terse register ("Do not use concurrently with", "Not recommended for use in", "Use with extreme
caution in those with"), with a reason in brackets in a few words. So these are three of the post's warnings in that
register, each checked by itself, the way his X-15 was (paragraph scope): whether the register reads Human in my hand, by
itself, before a stretch is tried again.

PARAS below: block index -> the paragraph's new text. The fidelity check runs on the article with all three in.
  python3 articles/neuro-de-armoring/humanize/fix-20261103/r2his/para/para_r2his.py
Writes CANDIDATE.md, TEXTS.json and PREDICTIONS.json here, and the predictions into the ledger first (batch r1103e).
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
ARTICLE_SHA = '6db92b7aff987195049b8af1f99883ec4a3f2e05e62af6a978679871c7957944'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218, E325: at most six paragraphs and 1,200 words)'
BATCH = 'r1103e'
PARAS = {
    16: 'Stop use immediately if it causes flatness, anhedonia, emotional blunting, new depression, agitation, insomnia, '
        'dizziness, palpitations, nausea, loose stools, diarrhea, or increased craving. Do not attempt to “push through” '
        'numbness (if agmatine makes the world more gray, it is the wrong tool for that phase).',
    17: 'Uridine & 5-HTP Warning for Psychedelic Users: Not to be used as “trip enhancers” (these are repair-oriented '
        'levers that can change brain sensitivity quickly). 5-HTP is a direct serotonin precursor, and therefore '
        'serotonergic: do not combine with SSRIs, SNRIs, MAOIs, linezolid, lithium, tramadol, methadone, fentanyl, DXM, '
        'MDMA, St. John’s wort, SAM-e, L-tryptophan, or other serotonin-raising stacks without clinician review. Use extra '
        'conservatively around ayahuasca and/or harmalas (MAO-A inhibition can amplify serotonin load), and iboga and/or '
        'ibogaine (ibogaine and noribogaine interact with serotonin transport biology, and already carry serious cardiac '
        'and neurological risk).',
    85: 'Side effects / stop signs: Most common is the “choline headache” or spaced-out brain fog (if UMP accelerates '
        'membrane synthesis while choline availability is low, the system can feel under-supplied). Other stop signs '
        'include insomnia, jitteriness, racing thoughts, irritability, emotional flatness, nausea, stomach cramps, or loose '
        'stools. Stop if it makes you wired, numb, or weirdly irritable, and do not push through.',
}
PRED = {
    16: (0.35, 'his terse label register ("Stop use immediately if", "Do not attempt to"), the reason in brackets; the '
               'symptom list is the post\'s, long'),
    17: (0.3, 'his register ("Not to be used as", "do not combine with", "Use extra conservatively around", "and/or"), '
              'reasons in brackets, but a long sentence of drug names and two technical reasons'),
    85: (0.35, 'his register ("Most common is", the mechanism in brackets, "Stop if"), the post\'s list of stop signs'),
}


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == ARTICLE_SHA, 'the article changed'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    for i, t in PARAS.items():
        assert raw[i] == sr.blocks(md)[i]['text'], i   # no marks in these paragraphs
        raw[i] = t
    cand = '\n\n'.join(raw) + '\n'
    (HERE / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'fidelity_keys.py'), 'check',
                         str(H / 'FIDELITY-KEYS.json'), str(HERE / 'CANDIDATE.md')], capture_output=True, text=True)
    print(fk.stdout.strip()[-2000:])
    if fk.returncode:
        sys.exit(1)
    texts, rows = {}, []
    (HERE / 'texts').mkdir(exist_ok=True)
    done = {json.loads(l).get('key') for l in LEDGER.read_text(encoding='utf-8').splitlines()
            if json.loads(l).get('batch') == BATCH}
    for i, t in PARAS.items():
        key = 'p%03d' % i
        texts[key] = t
        sha = hashlib.sha256(t.encode('utf-8')).hexdigest()
        chance, why = PRED[i]
        lineage = 'ND1103-P%03d' % i
        rows.append({'key': key, 'name': 'B%03d by itself, in his X-15 register' % i, 'lineage': lineage,
                     'scope': 'paragraph', 'words': len(t.split()), 'call': 'AI' if chance < 0.5 else 'Human',
                     'chance': chance, 'why': why, 'sha256': sha})
        f = HERE / 'texts' / (key + '.txt')
        f.write_text(t, encoding='utf-8')
        if key in done:
            continue
        subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                        '--lineage', lineage, '--scope', 'paragraph', '--text', str(f), '--call', rows[-1]['call'],
                        '--chance', str(chance), '--key', key, '--batch', BATCH, '--detector', DETECTOR, '--tells', why,
                        '--diagnosis', 'both tries of the warnings stretch read 100% AI (the post\'s phrases in his build; '
                        'then re-said chattily); his X-15 is a supplement label\'s terse register, so this is that register',
                        '--decides', 'whether his X-15 register reads Human in my hand for a paragraph by itself, before a '
                        'stretch is tried again or the warnings go to him'], check=True)
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
