"""Batch n1102: the neuro de-armoring article as it stands in his post, checked through the API with public links before
anything is changed, in ten sections and as one whole text, with my predictions written first (E307: each section by itself,
and the whole). Started at Joel's message of 2026-11-02 18:16 UTC: "then we can start on the next one we had queued".

The sections follow the article's headings, joined where a heading's text is too short to read by itself (under about 150
words): the introduction with the disclaimers, Part 1 in two, Part 2 in four, Parts 3 and 4 each whole, Part 5 with the
Aftermath. The text is the post's text: images and the video's placeholder are left out, as they are when the post is read.

My read before the run (the lead session read the whole article): the introduction, the Scott passages and the D-serine
paragraph sound like him; most of the rest is set out in a template ("The Problem:", "The Mechanism:", "The Fix:", "The
Rule:", "The Takeaway:") with paired lines that read AI ("that is a flood, not a fix", "Frequency beats intensity.", "It is
not a symptom of sickness; it is the symptom of coming back to life."), so I expect AI in every section and in the whole.

  python3 articles/neuro-de-armoring/humanize/fix-20261102/baseline/make_baseline.py [--ledger]
Writes TEXTS.json and PREDICTIONS.json here; with --ledger, adds the predictions to the lane's ledger.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'
SKIP = {'Double click to interact with video'}
# (key, first heading, name, chance of a fully Human result, why)
SECTIONS = [
    ('n1102-01', 'Introduction', 'the introduction and the disclaimers', 0.15,
     'his introduction, then the warnings set out as "The Rule:", "Cognitive Warning:" with capitalized terms and paired '
     'lines ("calibrated to Threat, not Truth")'),
    ('n1102-02', 'Psychology is the Software; Biology is the Hardware.', 'Psychology is the Software', 0.05,
     'paired lines throughout ("that is a flood, not a fix", "We are not running a marathon; we are doing physical '
     'therapy", "Frequency beats intensity.")'),
    ('n1102-03', 'Part 1: THE SCIENCE (Why We Do This)', 'Part 1, A and B', 0.08,
     'the Problem/Mechanism/Fix template and "The Takeaway:"; the D-serine paragraph sounds more like him'),
    ('n1102-04', 'C. The “Hardened” Circuit: Dynorphin & DeltaFosB', 'Part 1, C to E', 0.08,
     '"you are not crazy", "You cannot \'wait\' for this to pass", "This turns the lights back on immediately."'),
    ('n1102-05', 'Part 2: Reducing Anxiety & Depression', 'Part 2: phosphatidylserine, and agmatine vs PS vs PC', 0.15,
     'Scott and "Be honest about the evidence, though" sound like him; "The catch, again:", "Counterintuitive but real:" '
     'and the rule of thumb read set out'),
    ('n1102-06', 'Dopamine Receptor Burnout / DAWS Pattern: Uridine Monophosphate', 'Part 2: uridine (UMP)', 0.10,
     'careful hedged evidence prose ("That is a specific phenotype, not a generic claim", "That does not prove ... It does '
     'suggest")'),
    ('n1102-07', 'Serotonin Bottleneck Pattern: 5-HTP + Low-Dose P5P', 'Part 2: 5-HTP, and ATP signaling', 0.10,
     'the same hedged prose ("More is not better.", "not as strong as people online imply"), then the ketone decision'),
    ('n1102-08', 'Part 3: THE SHIELD (Flu-Proofing & Voltage Control)', 'Part 3: the Shield', 0.20,
     'labels and lists of doses and foods ("The Mandate:", "The King of Potassium"); lists of numbers read either way'),
    ('n1102-09', 'Part 4: THE JAMMER (Acute Symptom Management)', 'Part 4: the Jammer', 0.20,
     '"Anatomy overrides intellect." and the scenario template; the D-serine paragraph ("ssuggested", "Again, all '
     'd-serine is doing") sounds like him'),
    ('n1102-10', 'Part 5: THE TIMELINE (The 8-Week Path)', 'Part 5: the timeline, and the Aftermath', 0.10,
     'the timeline\'s lists, then the Aftermath\'s paired close ("It is not a symptom of sickness; it is the symptom of '
     'coming back to life. Welcome it.")'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = [b for b in sr.blocks(md) if not (b['kind'] == 'image' or b['text'].startswith('image ') and len(b['text'].split()) <= 2)
          and b['text'] not in SKIP]
    starts = []
    for key, head, *_ in SECTIONS:
        [k] = [j for j, b in enumerate(bl) if b['level'] and b['text'] == head]
        starts.append(k)
    starts[0] = 0
    texts, rows = {}, []
    for n, (key, head, name, chance, why) in enumerate(SECTIONS):
        end = starts[n + 1] if n + 1 < len(starts) else len(bl)
        texts[key] = '\n\n'.join(b['text'] for b in bl[starts[n]:end])
    texts['n1102-whole'] = '\n\n'.join(b['text'] for b in bl)
    assert len(texts['n1102-whole']) < 99999
    for key, head, name, chance, why in SECTIONS + [('n1102-whole', None, 'the whole article', 0.02,
                                                       'every section above, read together')]:
        t = texts[key]
        rows.append({'key': key, 'name': name, 'lineage': 'ND1102-' + key.split('-')[1], 'scope': 'article' if key.endswith('whole') else 'section',
                     'chars': len(t), 'words': len(t.split()), 'call': 'Human' if chance >= 0.5 else 'AI', 'chance': chance,
                     'why': why, 'sha256': hashlib.sha256(t.encode('utf-8')).hexdigest()})
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for r in rows:
        print(r['key'], r['words'], r['call'], r['chance'], r['name'])
    if not a.ledger:
        return
    td = HERE / 'texts'
    td.mkdir(exist_ok=True)
    for r in rows:
        f = td / (r['key'] + '.txt')
        f.write_text(texts[r['key']], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', r['scope'], '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', r['key'], '--batch', 'n1102', '--detector', DETECTOR,
               '--tells', r['why'], '--diagnosis', 'the article as it stands in his post, before any change',
               '--decides', 'which sections need work first, and what the whole reads now (the baseline)']
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (r['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
