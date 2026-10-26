#!/usr/bin/env python3
"""NOT RUN in turn 113: Joel said the drafts can wait for the big edits ("no point checking the drafts at this point, we are
about to make major edits"), so the check runs on what he approves after GPT's review. Before running it, rebuild its
inputs from the version he approves and write new predictions for that version; numbers written here are from an earlier round.

Turn 113: the items whose readings inside the two halves decide something, one for every section the turn-113 review
sheet changes (experiments/t113-shape/SECTIONS.json), each as its text in TEXT-A.txt or TEXT-B.txt from its heading to
the next heading of the same or a higher level (so a section's new case headings are inside its item), and one prediction
per item and per half in the ledger (batch t113-substack), written before the drafts are pasted. Writes ITEMS.json and
items/<key>.txt (the ledger hashes those files). Copied from turn 112's make_items.py."""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
SEC = json.loads((HERE.parent / 't113-shape' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']
PROPOSAL = (HERE.parent / 't113-shape' / 'PROPOSAL-ARTICLE.md').read_text(encoding='utf-8')
ITEMS = {
    # section id: (key, call, chance, diagnosis)
    'H-guard': ('t113i_guard', 'Human', 0.55, 'the agreed order read Human through the API as a section (turn 110); now four case headings and one lead drop'),
    'H-start': ('t113i_start', 'Human', 0.55, 'read 0% AI through the API as a section (turn 110); now five case headings and two lead drops'),
    'H-change': ('t113i_change', 'Human', 0.6, 'his rewrite, 100% Human in his check (turn 106); now five headings, his first-sentence question as one of them, one split'),
    'H-escape': ('t113i_escape', 'Human', 0.55, 'his text, Human in round 6; now six headings, two first sentences become headings, one split'),
    'H-fake': ('t113i_fake', 'Human', 0.55, 'Human in round 6; now three headings from the paragraphs\' own words and two lead drops'),
    'H-therapist': ('t113i_therapist', 'Human', 0.6, 'his text, Human in round 6; now four headings and two lead drops'),
    'H-hooks': ('t113i_hooks', 'Human', 0.55, 'Human in round 6; now three headings and one lead drop'),
    'H-borrow': ('t113i_borrow', 'Human', 0.55, 'Human in round 6; now three headings, two from the paragraphs\' first words'),
    'R-helping': ('t113i_helping', 'Human', 0.6, 'a 210-word paragraph split in four, every sentence kept'),
    'R-forgive': ('t113i_forgive', 'Human', 0.6, 'its last paragraph split in two, every sentence kept; one parenthesis cut in turn 111'),
    'W-solomon': ('t113i_solomon', 'Human', 0.5, 'his version of P3 ("this version passes", his check) with five words of mine for 109 A'),
}
HALVES = [
    ('t113s_A', 'A', 'which proposed sections read Human in context in half A, before Joel decides', 'AI', 0.25,
     'round 6: 0.20% AI, one Low window; nine proposed sections in this half, with 26 new headings'),
    ('t113s_B', 'B', 'which proposed sections read Human in context in half B, before Joel decides', 'AI', 0.3,
     'round 6: 0.39% AI, three windows in How This Relates to IFS; Untangling the Belonging Bargains P1 reads AI alone'),
]


def blocks(half):
    return (HERE / ('TEXT-%s.txt' % half)).read_text(encoding='utf-8').rstrip('\n').split('\n\n')


_md = re.sub(r'<!--.*?-->', '', PROPOSAL, flags=re.S)
LEVEL = {}
for l in _md.split('\n'):
    m = re.match(r'^(#{1,6}) (.*)$', l)
    if m:
        LEVEL.setdefault(m.group(2).strip(), len(m.group(1)))


def predict(key, scope, path, call, chance, diagnosis, decides):
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', key.replace('_', '-'), '--scope', scope, '--text', str(path), '--call', call, '--chance', str(chance),
           '--tells', 'none named', '--human-tells', 'his words where the item is his', '--diagnosis', diagnosis,
           '--decides', decides, '--key', key, '--batch', 't113-substack', '--detector', 'pangram-4.1-substack']
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    return out.stdout.strip().split('\n')[-1]


def main():
    done = {json.loads(l).get('key') for l in LEDGER.read_text(encoding='utf-8').splitlines() if l.strip()}
    keys = [v[0] for v in ITEMS.values()] + [h[0] for h in HALVES]
    assert not any(k in done for k in keys), 'already predicted'
    out = {}
    (HERE / 'items').mkdir(exist_ok=True)
    for r in SEC:
        key, call, chance, diag = ITEMS[r['id']]
        head = r['heading'].split(' ', 1)[1].strip()
        lvl = LEVEL[head]
        hits = []
        for half in 'AB':
            bl = blocks(half)
            for n, b in enumerate(bl):
                if b == head:
                    j = n + 1
                    while j < len(bl) and not (bl[j] in LEVEL and LEVEL[bl[j]] <= lvl):
                        j += 1
                    hits.append((half, '\n\n'.join(bl[n:j])))
        assert len(hits) == 1, (key, len(hits))
        half, text = hits[0]
        decides = 'whether the proposals in %s read Human in context, before Joel decides' % head
        path = HERE / 'items' / (key + '.txt')
        path.write_text(text, encoding='utf-8')
        out[key] = {'half': half, 'section': head, 'scope': 'section', 'words': len(text.split()), 'decides': decides,
                    'prediction': predict(key, 'section', path, call, chance, diag, decides)}
    for key, half, decides, call, chance, diag in HALVES:
        out[key] = {'half': half, 'scope': 'stretch', 'words': len((HERE / ('TEXT-%s.txt' % half)).read_text(encoding='utf-8').split()),
                    'decides': decides, 'prediction': predict(key, 'stretch', HERE / ('TEXT-%s.txt' % half), call, chance, diag, decides)}
    (HERE / 'ITEMS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for k, v in out.items():
        print('%-18s %s %-9s %5d words | %s' % (k, v['half'], v['scope'], v['words'], v['prediction'][:70]))


if __name__ == '__main__':
    main()
