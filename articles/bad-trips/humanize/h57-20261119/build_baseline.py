#!/usr/bin/env python3
"""build_baseline.py - batch h57a: each paragraph with a window below Human High in its newest check (STATUS.md), checked
by itself exactly as the guide has it, before any change: the near miss each lesson-19b try starts from (lesson
bad-trips-2026-11-19b), or Human High by itself and done. A paragraph under 50 words goes with a neighbour or its
heading (the web app's 50-word minimum; apply_gate.py's pair and heading scopes).

Text as the lane's checks have it (h42's build_units.py): headings and labels as plain lines, links as their words, bold
and italics out, list items one per line, blocks joined by a blank line.

  python3 build_baseline.py      writes TEST-a*.txt and ITEMS-h57a.json ([[key, text, sha256], ...])
"""
import hashlib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BLOCKS = {b['id']: b for b in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}


def plain(md):
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)
    t = re.sub(r'\[([^\]]*)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', t)
    t = re.sub(r'<sub>(.*?)</sub>', r'\1', t)
    t = t.replace('**', '').replace('__', '')
    t = re.sub(r'(?<![\w*])\*(?!\s)([^*\n]+?)\*(?!\w)', r'\1', t)
    lines = []
    for l in t.split('\n'):
        l = re.sub(r'^\s*(?:[-*]|\d+\.)\s+', '', l)
        l = re.sub(r'^\s*>\s?', '', l)
        l = re.sub(r'^#+\s*', '', l)
        lines.append(l.rstrip())
    return re.sub(r'[ \t]+\n', '\n', '\n'.join(lines)).strip()


# key: (blocks, scope, what and where)
UNITS = {
    'a01-brain-protocol': (['B144'], 'paragraph', "My Brain Feels Damaged's numbered protocol (B144) as the guide has it"),
    'a02-coffee-cherry': (['B167'], 'paragraph', "Coffee Cherry's paragraph (B167) as the guide has it"),
    'a03-bmg-mdma': (['B176', 'B178'], 'pair', "Beach Morning Glory's last two paragraphs (B176, his story; B178, the MDMA line, under 50 words)"),
    'a04-shungite': (['B198'], 'paragraph', "the shungite and boiled-charcoal paragraph (B198) as the guide has it"),
    'a05-dmso-overlap': (['B201'], 'paragraph', "DMSO's overlap with aged ozonated-charcoal water (B201) as the guide has it"),
    'a06-dmso-side': (['B202', 'B203'], 'heading', "DMSO's side effects, its label and list (B202, B203), as the guide has them"),
    'a07-niacin-side': (['B213', 'B214'], 'heading', "Niacin's side effects, its label and list (B213, B214), as the guide has them"),
    'a08-niacin-forms': (['B214', 'B215'], 'pair', "Niacin's side-effect list and its B3 forms paragraph (B215, under 50 words)"),
    'a09-humic-caution': (['B217', 'B219'], 'heading', "Some Remedies Require More Caution with its first paragraph (B219) as the guide has them"),
    'a10-anchor-lead': (['B255'], 'paragraph', "Get One Human Anchor's second paragraph (B255) as the guide has it"),
    'a11-music': (['B303', 'B304'], 'heading', "the Grounding Menu's Music label and list (B303, B304) as the guide has them"),
    'a12-move-list': (['B312'], 'paragraph', "the Grounding Menu's food, walking and exercise list (B312) as the guide has it"),
    'a13-shadow-def': (['B344'], 'paragraph', "Shadow Work's opening paragraph, his definition (B344), as the guide has it"),
    'a14-redefining': (['B330c', 'B357'], 'pair', "(Re)defining \"Bad Trip\": his paragraph (B330c) and the line after it (B357, under 50 words)"),
    'a15-sorrow': (['B377', 'B378', 'B379'], 'stretch', "Dealing With Sorrow's pamphlet line, the quote and his line after it (B377 to B379, each under 50 words)"),
    'a16-shadow-thoughts': (['B410', 'B411', 'B412'], 'stretch', "Dealing With Shadow Thoughts' heading and first two paragraphs (B411 under 50 words)"),
    'a17-opposites': (['B413', 'B414'], 'pair', "Dealing With Shadow Thoughts' identity line and its opposites paragraph (B413, B414, both under 50 words)"),
    'a18-aftermath': (['B424', 'B425'], 'heading', "What Kind of Aftermath Is This? with its first paragraph (B425, his)"),
    'a19-appendix': (['B433'], 'paragraph', "the Appendix's list of further resources (B433) as the guide has it"),
    'a20-aura': (['R32-SEIZE', 'N-WARN'], 'heading', "What Else May Help's heading with his aura paragraph (N-WARN)"),
    'a21-cbd-topical': (['N-CBD-2'], 'paragraph', "his topical CBD paragraph (N-CBD-2) as the guide has it"),
    'a22-cbd-dmso': (['N-CBD-3'], 'paragraph', "the DMSO-for-seizures paragraph (N-CBD-3) as the guide has it"),
    'a23-ss-recognize': (['B131', 'B132', 'B133'], 'heading', "Recognizing serotonin toxicity: the heading, his lead-in and his list (B131 to B133)"),
    'a24-first-five': (['B236'], 'paragraph', "his first five minutes' dangers paragraph (B236) as the guide has it"),
    'a25-after-storm': (['B420'], 'paragraph', "After the Storm's first paragraph (B420) as the guide has it"),
    'a26-mh-support': (['B426-last', 'B96', 'B97'], 'heading', "Bring in mental-health support when: its heading and list (B96, B97, 38 words), after the last item of his aftermath list (B426) before it"),
}


def md_of(i):
    if i == 'B426-last':   # the last item of his aftermath list, the block before the heading
        return [l for l in BLOCKS['B426']['md'].split('\n') if l.strip()][-1]
    return BLOCKS[i]['md']


def text_of(ids):
    return '\n\n'.join(plain(md_of(i)) for i in ids)


if __name__ == '__main__':
    items = []
    for key, (ids, scope, what) in UNITS.items():
        t = text_of(ids)
        (HERE / ('TEST-%s.txt' % key)).write_text(t + '\n', encoding='utf-8')
        items.append([key, t, hashlib.sha256(t.encode('utf-8')).hexdigest()])
        print(key, len(t.split()), 'words')
    (HERE / 'ITEMS-h57a.json').write_text(json.dumps(items, ensure_ascii=False) + '\n', encoding='utf-8')
