#!/usr/bin/env python3
"""Turn 112, round 7: the items whose readings inside the halves decide something, each as its text in TEXT-A.txt or
TEXT-B.txt (a heading and its paragraphs), one for every section changed since round 6 was pasted (commit dac96f36), and
one prediction per item and per half in the ledger (batch t112-substack), written before the drafts are pasted. Writes
ITEMS.json and items/<key>.txt (the ledger hashes those files). Copied from turn 107's make_items.py."""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEDGER = ROOT / 'articles/inner-child-therapy/tools/pangram-ledger.jsonl'
norm = lambda s: re.sub('[“”]', '"', re.sub('[‘’]', "'", s))
ITEMS = [
    # key, half, scope, heading or None, a line in the paragraph, what it decides, call, chance, diagnosis
    ('t112i_dontgive', 'A', 'section', 'Don’t Give the Inner Adult Away', None, 'whether P2 (GPT\'s wording, turn 111) holds in context', 'Human', 0.55,
     'P2\'s new sentence passed the owner-delivery gate; the paragraph read Human alone through the API (turn 111)'),
    ('t112i_illwill', 'A', 'section', 'Ill Will and Loving-Kindness', None, 'whether P1 after his approved cut (C3) holds in context', 'Human', 0.55,
     'P1 read Human alone after the cut (turn 111), with one Medium Human window'),
    ('t112i_lovenotyet', 'A', 'section', "If the Love Isn't Coming Yet", None, 'whether his truce sentence (Q1) holds in context', 'Human', 0.6,
     'his own sentence for "What people most often say helped"; the paragraph read Human alone (turn 111)'),
    ('t112i_borrowlove', 'A', 'section', 'Borrow Love—or Borrow the Perspective of Care', None, 'whether his version of P3 (turn 112) holds in context', 'Human', 0.55,
     'his own version of P3 ("this version passes", his check); P3 after the approved cut alone read 100% AI (turn 111)'),
    ('t112i_lovewait', 'A', 'section', "Love Doesn't Have to Wait for Trust ❤️", None, 'whether P8 after his approved cut (C5) holds in context', 'Human', 0.6,
     'P8 read Human alone after the cut (turn 111)'),
    ('t112i_remind', 'A', 'section', 'Remind Yourself', None, 'whether P5\'s son line (turn 111) holds in context', 'Human', 0.6,
     'his 2026-10-02 answer as an article sentence, through the owner-delivery gate; Human alone (turn 111)'),
    ('t112i_hook', 'A', 'section', 'Catch the Hook Before the Story Takes Over', None, 'whether P2 after his approved cut (C6) holds in context', 'Human', 0.6,
     'P2 read Human alone after the cut (turn 111)'),
    ('t112i_justlikeme', 'A', 'section', 'Just Like Me', None, 'whether his P2 sentence and his P1 cut (turn 111) hold in context', 'Human', 0.6,
     'his own sentence for P2 and his cut of the stray line in P1; both paragraphs read Human alone (turn 111)'),
    ('t112i_photos', 'A', 'section', 'Use Childhood Photographs Gently', None, 'whether P1 rewritten after round 6\'s Low 33 window holds', 'Human', 0.5,
     'round 6 read one Low window (33 words) in P1, rewritten since; two paragraphs changed since round 6'),
    ('t112i_close', 'A', 'section', 'Close the Session and Return to Life', None, 'whether the section holds after his approved cut (C7)', 'Human', 0.6,
     'the cut took out the section\'s last line; P2 read Human alone (turn 111)'),
    ('t112i_whatever', 'A', 'section', 'Start With Whatever Showed Up', None, 'whether the two paragraphs changed since round 6 hold in context', 'Human', 0.6,
     'read 0% AI through the API as a section (turn 110)'),
    ('t112i_guard', 'A', 'section', 'Hear the Guard First', None, 'whether the agreed order (turn 111) holds in context', 'Human', 0.6,
     'the agreed order read Human through the API as a section (turn 110); each new paragraph read Human alone'),
    ('t112i_belonging', 'B', 'section', 'Untangling the Belonging Bargains', None, 'whether P1 after his approved cut (C8) holds in context', 'AI', 0.4,
     'P1 reads 100% AI alone with and without the cut (turn 111); the section read Human in context in round 6 with the line in'),
    ('t112i_bad', 'B', 'section', 'Let the Child Be Bad at Things', None, 'whether P3 after his approved cut (C9) holds in context', 'Human', 0.6,
     'P3 read Human alone after the cut (turn 111)'),
    ('t112i_borrowed', 'B', 'section', 'Borrowed Adulthood in Relationship', None, 'whether his added sentence (C10) and his cut hold in context', 'Human', 0.6,
     'both paragraphs read Human alone (turn 111); his own sentence and his own cut'),
    ('t112i_hardest', 'B', 'section', 'Before You Tell the Hardest Stuff', None, 'whether his version of the agreed order (turn 111) holds in context', 'Human', 0.55,
     'the agreed order read Human through the API (turn 110); his version changes one word ("this person")'),
    ('t112i_forgive', 'B', 'section', 'How to Forgive Without Forgetting', None, 'whether the section holds after his approved cut (C11)', 'Human', 0.55,
     'one parenthesis cut; unchanged otherwise since round 6'),
    ('t112i_missing', 'B', 'section', 'Missing Someone', None, 'whether the section holds after his approved cut (C12)', 'Human', 0.55,
     'one parenthesis cut; unchanged otherwise since round 6'),
    ('t112i_ifs', 'B', 'section', 'How This Relates to IFS', None, 'whether round 6\'s three windows (45 of 598 words) come back', 'AI', 0.35,
     'round 6 read three Low or Medium windows in his lines here; one paragraph changed since'),
]
HALVES = [
    ('t112s_A', 'A', 'which of the changes since round 6 hold inside half A, and whether the half can read 100% Human', 'AI', 0.25,
     'round 6: 0.20% AI, one Low window (Use Childhood Photographs Gently P1, rewritten since); twelve sections changed since'),
    ('t112s_B', 'B', 'which of the changes since round 6 hold inside half B', 'AI', 0.25,
     'round 6: 0.39% AI, three windows in How This Relates to IFS; Untangling the Belonging Bargains P1 reads AI alone'),
]


def blocks(half):
    return (HERE / ('TEXT-%s.txt' % half)).read_text(encoding='utf-8').rstrip('\n').split('\n\n')


# The article's headings, as plain text, so a section stops at the next heading of any level.
_md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
HEADS = {re.sub(r'^#+\s*', '', l).strip(): True for l in _md.split('\n') if re.match(r'^#{1,5} ', l)}


def predict(key, scope, path, call, chance, diagnosis, decides):
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', key.replace('_', '-'), '--scope', scope, '--text', str(path), '--call', call, '--chance', str(chance),
           '--tells', 'none named', '--human-tells', 'his words where the item is his', '--diagnosis', diagnosis,
           '--decides', decides, '--key', key, '--batch', 't112-substack', '--detector', 'pangram-4.1-substack']
    out = subprocess.run(cmd, capture_output=True, text=True)
    if out.returncode:
        sys.exit(out.stdout + out.stderr)
    return out.stdout.strip().split('\n')[-1]


def main():
    done = {json.loads(l).get('key') for l in LEDGER.read_text(encoding='utf-8').splitlines() if l.strip()}
    assert not any(k in done for k, *_ in ITEMS + HALVES), 'already predicted'
    out = {}
    (HERE / 'items').mkdir(exist_ok=True)
    for key, half, scope, head, line, decides, call, chance, diag in ITEMS:
        bl = blocks(half)
        if head:
            i = [n for n, b in enumerate(bl) if b == head]
            assert len(i) == 1, (key, i)
            i = i[0]
            j = i + 1
            while j < len(bl) and not HEADS.get(bl[j]):
                j += 1
            text = '\n\n'.join(bl[i:j])
        else:
            hit = [b for b in bl if norm(line) in norm(b)]
            assert len(hit) == 1, (key, len(hit))
            text = hit[0]
        path = HERE / 'items' / (key + '.txt')
        path.write_text(text, encoding='utf-8')
        out[key] = {'half': half, 'scope': scope, 'words': len(text.split()), 'first': text[:80], 'decides': decides,
                    'prediction': predict(key, scope, path, call, chance, diag, decides)}
    for key, half, decides, call, chance, diag in HALVES:
        out[key] = {'half': half, 'scope': 'stretch', 'words': len((HERE / ('TEXT-%s.txt' % half)).read_text(encoding='utf-8').split()),
                    'decides': decides, 'prediction': predict(key, 'stretch', HERE / ('TEXT-%s.txt' % half), call, chance, diag, decides)}
    (HERE / 'ITEMS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for k, v in out.items():
        print('%-18s %s %-9s %5d words | %s' % (k, v['half'], v['scope'], v['words'], v['prediction'][:70]))


if __name__ == '__main__':
    main()
