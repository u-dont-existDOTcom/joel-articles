#!/usr/bin/env python3
"""Turn 114: the items whose readings inside the two halves decide something, one for every section his turn-113 answers
changed (experiments/t113-shape/SECTIONS.json, all eleven cards approved and installed), each as its text in TEXT-A.txt or
TEXT-B.txt from its heading to the next heading that isn't one of its own case headings (so an item is the text its card
changed, with its case headings, and stops at the section's first subsection), and the two halves. One prediction per item
and per half goes in the ledger (batch t114-substack) before the drafts are pasted. Writes ITEMS.json and items/<key>.txt
(the ledger hashes those files). Adapted from turn 113's unrun make_items.py.

--chance is my chance of a 100% Human result (pangram_ledger.py): a Human call is at least 0.5, an AI call at most 0.5."""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import plain  # noqa: E402  (its ptext.plain, the text the payloads use)

LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
SEC = json.loads((HERE.parent / 't113-shape' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']
ART = (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')
ITEMS = {
    # section id: (key, call, chance, diagnosis)
    'H-guard': ('t114i_guard', 'Human', 0.6, 'read Human through the API as a section in the agreed order (turn 110, t110_sec_guard_b); now four '
                'case headings, one his own first words'),
    'H-start': ('t114i_start', 'Human', 0.55, 'Human in round 6; now six case headings (three his words), the answer paragraph split, and one '
                'sentence moved up three sentences; the long stop-rule heading is his condition'),
    'H-change': ('t114i_change', 'Human', 0.6, 'his rewrite, 0 of 425 words in AI windows in round 6; now five case headings (two his words) and '
                 'his last paragraph split'),
    'H-escape': ('t114i_escape', 'Human', 0.55, 'his text and GPT\'s paragraph, Human in round 6; now seven case headings, two splits, and two '
                 'first sentences out for their headings; seven short headings in a row could read as a template'),
    'H-fake': ('t114i_fake', 'Human', 0.6, 'Human in round 6; now three headings, each the paragraph\'s own first sentence or clause'),
    'H-therapist': ('t114i_therapist', 'Human', 0.65, 'his text, Human in round 6; now four headings, three his own words'),
    'H-hooks': ('t114i_hooks', 'Human', 0.6, 'Human in round 6; now four headings (three his words), the danger line split off, one "Also" cut'),
    'H-borrow': ('t114i_borrow', 'Human', 0.6, 'Human in round 6; now three headings, two his first words'),
    'R-helping': ('t114i_helping', 'Human', 0.65, 'Human in round 6; its 210-word paragraph split in four, every sentence kept'),
    'R-forgive': ('t114i_forgive', 'Human', 0.6, 'Human in round 6; its last paragraph split in two, every sentence kept'),
    'W-solomon': ('t114i_solomon', 'Human', 0.55, 'his version of P3 ("this version passes", his check) with five words of mine for his 109 A'),
}
HALVES = [
    ('t114s_A', 'A', 'which installed sections read Human in context in half A, and whether the case headings read as his', 'AI', 0.3,
     'round 6: 0.20% AI, one Low window, on the photos paragraph he rewrote in turn 109; since then the turn-110 cuts, Hear the Guard '
     'in the agreed order, his Borrow Love paragraph and 33 case headings in eight sections'),
    ('t114s_B', 'B', 'which installed sections read Human in context in half B, and whether the case headings read as his', 'AI', 0.35,
     'round 6: 0.39% AI, three windows in How This Relates to IFS, which he rewrote in turn 109; since then When Escape Leaves '
     'Reality Behind\'s seven case headings, two splits, and Untangling the Belonging Bargains P1, which read AI alone'),
]


def blocks(half):
    return (HERE / ('TEXT-%s.txt' % half)).read_text(encoding='utf-8').rstrip('\n').split('\n\n')


HEADS = set()
for l in re.sub(r'<!--.*?-->', '', ART, flags=re.S).split('\n'):
    m = re.match(r'^(#{1,6}) (.*)$', l)
    if m:
        HEADS.add(plain(m.group(2)).strip())


def predict(key, scope, path, call, chance, diagnosis, decides):
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', key.replace('_', '-'), '--scope', scope, '--text', str(path), '--call', call, '--chance', str(chance),
           '--tells', 'none named', '--human-tells', 'his words where the item is his', '--diagnosis', diagnosis,
           '--decides', decides, '--key', key, '--batch', 't114-substack', '--detector', 'pangram-4.1-substack']
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    return out.stdout.strip().split('\n')[-1]


def main():
    done = {json.loads(l).get('key') for l in LEDGER.read_text(encoding='utf-8').splitlines() if l.strip()}
    keys = [v[0] for v in ITEMS.values()] + [h[0] for h in HALVES]
    assert not any(k in done for k in keys), 'already predicted'
    dry = '--dry' in sys.argv
    out = {}
    (HERE / 'items').mkdir(exist_ok=True)
    for r in SEC:
        key, call, chance, diag = ITEMS[r['id']]
        head = plain(r['heading'].split(' ', 1)[1]).strip()
        own = {plain(x['md']).strip() for x in r['new'] if x['kind'] != 'p'}
        hits = []
        for half in 'AB':
            bl = blocks(half)
            for n, b in enumerate(bl):
                if b == head:
                    j = n + 1
                    while j < len(bl) and not (bl[j] in HEADS and bl[j] not in own):
                        j += 1
                    hits.append((half, '\n\n'.join(bl[n:j])))
        assert len(hits) == 1, (key, len(hits))
        half, text = hits[0]
        assert all(o in text.split('\n\n') for o in own), key
        decides = 'whether %s, as he approved it, reads Human in context' % head
        path = HERE / 'items' / (key + '.txt')
        path.write_text(text, encoding='utf-8')
        out[key] = {'half': half, 'section': head, 'scope': 'section', 'words': len(text.split()), 'decides': decides,
                    'prediction': 'dry' if dry else predict(key, 'section', path, call, chance, diag, decides)}
    for key, half, decides, call, chance, diag in HALVES:
        out[key] = {'half': half, 'scope': 'stretch', 'words': len((HERE / ('TEXT-%s.txt' % half)).read_text(encoding='utf-8').split()),
                    'decides': decides,
                    'prediction': 'dry' if dry else predict(key, 'stretch', HERE / ('TEXT-%s.txt' % half), call, chance, diag, decides)}
    if not dry:
        (HERE / 'ITEMS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for k, v in out.items():
        print('%-18s %s %-9s %5d words | %s' % (k, v['half'], v['scope'], v['words'], v['prediction'][:70]))


if __name__ == '__main__':
    main()
