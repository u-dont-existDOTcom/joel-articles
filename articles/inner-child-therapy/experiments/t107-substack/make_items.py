#!/usr/bin/env python3
"""Turn 107, round 6: the items whose readings inside the halves decide something, each as its text in TEXT-A.txt or
TEXT-B.txt (a heading and its paragraphs, or one paragraph), found by a line it contains, and one prediction per item and
per half in the ledger (batch t107-substack), written before the drafts are pasted. Writes ITEMS.json and
items/<key>.txt (the ledger hashes those files). Copied from turn 98's make_items.py."""
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
    ('t107i_journey', 'A', 'section', 'My Journey', None, 'whether his My Journey (turn 107) holds inside the half', 'Human', 0.75,
     'his rewrite, all dark green in his check; three answers of his that I had put in as he typed them are his article sentences now'),
    ('t107i_hero', 'A', 'section', 'Not Every Hero Wears A Cape', None, 'whether his first three paragraphs (turn 107) hold inside the half', 'Human', 0.75,
     'his rewrite, all dark green in his check; the three read 2.65% AI through the API before it, with no AI window'),
    ('t107i_intentional', 'A', 'section', 'Make It Intentional', None, 'whether the new heading\'s section holds in context', 'Human', 0.7,
     'Human through the API under its new heading (turn 106)'),
    ('t107i_monologue', 'A', 'section', 'You Don’t Need an Inner Monologue', None, 'whether his rewrite holds where round 5 read Low 19 (P2)', 'Human', 0.75,
     'his rewrite, Human through the API with and without the paragraph break (turn 106)'),
    ('t107i_checking2', 'A', 'paragraph', None, 'Going back can still matter, even when nothing new turns up.', 'whether round 5\'s Low 29 here was the check varying', 'Human', 0.55,
     'unchanged since round 5, which read Low 29 here the first time; nothing around it has changed'),
    ('t107i_narrate3', 'A', 'paragraph', None, "Do keep an ear on who's narrating, though.", 'whether round 5\'s Low 33 here (mine) was the check varying', 'Human', 0.5,
     'unchanged since round 5 (Low 33, the first time); mine, with a parenthesis that comments on itself'),
    ('t107i_change', 'A', 'section', 'When to Change the Strategy', None, 'whether his rewrite holds where round 5 read four windows (P3, P4)', 'Human', 0.75,
     'his rewrite, 100% high-confidence Human in his check (turn 106); the typo fix is one word'),
    ('t107i_guide5', 'B', 'paragraph', None, "Once a need does show, after all that hiding, it's okay to want a lot of closeness.", 'whether my turn-100 rewrite of The Inner Guide P5 holds inside the half', 'Human', 0.6,
     'rewritten after round 5 (Low 42 in rounds 4 and 5); Human alone and with its neighbors through the web app (turn 100)'),
    ('t107i_ended', 'B', 'section', 'When One Life Has Ended and the Next Hasn’t Begun', None, 'whether my turn-100 rewrite of its P1 holds inside the half', 'Human', 0.6,
     'P1 rewritten after round 5 (Low 14 and Low 61); Human alone and in its h1 (turn 100)'),
    ('t107i_ifs', 'B', 'section', 'How This Relates to IFS', None, 'whether its rewritten P7 and the E34 break hold inside the half', 'Human', 0.6,
     'P7 rewritten after round 5 (Low 9, Low 30); the section Human through the API with E34\'s break (turn 106)'),
    ('t107i_related1', 'B', 'paragraph', None, 'This framework developed through the teachers and collaborators credited below', 'whether round 5\'s Low 14 on its first line was the check varying', 'Human', 0.55,
     'unchanged since round 5 (Low 14 on the first line, rounds 4 and 5)'),
    ('t107i_timing', 'B', 'section', 'Timing Is Individual', None, 'whether the second writer\'s P2 holds inside the half', 'Human', 0.6,
     'Codex\'s P2, Human alone and in its section through the API (turn 106), after my drafts read AI alone'),
    ('t107i_crisis', 'B', 'section', 'If You Want to Kill Yourself', None, 'whether his crisis stretch holds inside the half', 'Human', 0.7,
     'his crisis stretch, fully Human in his check (turn 106)'),
    ('t107i_social', 'B', 'section', 'First Social Connections, Done Right', None, 'whether his rewrite holds inside the half', 'Human', 0.75,
     'his rewrite, fully green in his check (turn 106)'),
    ('t107i_speak', 'B', 'section', 'Speak Toward What You Are Building', None, 'whether his rewrite holds above the new heading', 'Human', 0.7,
     'his rewrite, all green in his check; its last paragraph is now under Ask What Kind of Company They Want'),
    ('t107i_company', 'B', 'section', 'Ask What Kind of Company They Want', None, 'whether the one-paragraph section holds under its new heading', 'Human', 0.65,
     'his paragraph, Human through the API under the new heading (turn 106)'),
    ('t107i_belong', 'B', 'section', 'You Belong Everywhere and Nowhere', None, 'whether its 0.0137% through the API was the check varying', 'Human', 0.6,
     'his section with his H31 cut, 0.0137% AI with no AI window through the API (turn 106)'),
]
HALVES = [
    ('t107s_A', 'A', 'which of the rewrites since round 5 hold inside half A, and whether the half can read 100% Human', 'AI', 0.25,
     'round 5: 1.2% AI, 8 Low or Medium windows, 6 of them in text he has rewritten since (You Don\'t Need an Inner Monologue P2, When to Change the Strategy P3 and P4); two Low ones in unchanged text of mine (When Healing Turns Into Checking P2, And So That\'s the Way It Happened! P3)'),
    ('t107s_B', 'B', 'which of the rewrites since round 5 hold inside half B', 'AI', 0.25,
     'round 5: 1.4% AI, 6 Low windows, 5 in text rewritten since (The Inner Guide P5, When One Life Has Ended P1, How This Relates to IFS P7); one in his line in Related Clinical Work P1, unchanged'),
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
           '--decides', decides, '--key', key, '--batch', 't107-substack', '--detector', 'pangram-4.1-substack']
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
