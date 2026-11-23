"""candidates.py - every unlinked mention of a section's subject outside that section (turn 61, Joel 2026-11-23: "make
sure that sections are linked to when mentioned or when they should be referenced"). Code finds the mentions; each is
judged by reading it (CANDIDATES.md), since whether a mention should send the reader to the section is a question of
meaning.

  python3 candidates.py > CANDIDATES.md
"""
import json, pathlib, re

ART = pathlib.Path(__file__).resolve().parents[3]
blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
SUBJ = {
    'call-medics-for': [r'call(?:ing)? (?:the )?medics', r'signs? (?:above|below)'],
    'who-to-contact': [r'poison control', r'TripSit', r'Fireside', r'warm ?line', r'crisis line'],
    'medical-and-brain-rescue': [r'remedies below', r'remedies above'],
    'my-brain-feels-damaged': [r'brain (?:feels )?damage'],
    'active-seizure': [r'\bseizures?\b', r'convuls'],
    'mdma-magnesium-alarm': [r'jaw tension', r'jaw tenses', r'magnesium chloride'],
    'chest-pain-and-injury': [r'chest pain'],
    'swallowed-too-much': [r'swallowed too much', r'oral (?:toxic )?ingestion'],
    'serotonin-syndrome-ss': [r'serotonin syndrome'],
    'activated-charcoal': [r'activated charcoal', r'\bcharcoal\b'],
    'humic-acid-for-the-brain': [r'humic'],
    'dmso': [r'\bDMSO\b'],
    'syrian-rue-oil-gentler': [r'Syrian rue oil', r'rue oil'],
    'beach-morning-glory': [r'beach morning glory', r'Ipomoea'],
    'niacin-flushes-trips-out': [r'\bniacin\b'],
    'metta-sniffer-chill-love': [r'Metta NMT sniffer', r'\bsniffer\b'],
    'creatine-for-brain-and-bliss': [r'\bcreatine\b'],
    'mango-leaf-tea-chill-bliss': [r'mango leaf'],
    'lime-or-eos-for-calm': [r'essential oils?', r'\blime\b'],
    'ocean-water-calms': [r'ocean water', r'sea ?water'],
    'shungite-holy-water': [r'shungite', r'holy water'],
    'coffee-cherry-brain-too': [r'coffee cherry'],
    'zeocharge-and-ferment': [r'ZeoCharge', r'zeolite'],
    'grounding-menu': [r'grounding menu', r'\bgrounding\b'],
    'get-one-human-anchor': [r'human anchor'],
    'ask-before-you-touch': [r'ask before you touch'],
    'shadow-thoughts': [r'shadow thoughts?'],
    'lingering-symptoms': [r'lingering'],
    'get-mental-health-help-if': [r'mental[- ]health help'],
    'need-to-stop-the-trip': [r'stop (?:the|a) trip', r'end(?:ing)? (?:the|a) trip'],
    'too-intense-stabilizers': [r'stabiliz'],
}
heads = json.loads((ART / 'SECTION-LINKS.json').read_text(encoding='utf-8'))['headings']
level = {h['anchor']: h['level'] for h in heads}
anchor_of = {h['text']: h['anchor'] for h in heads}

# the heading path of every block
path, where = [], []
for x in blocks:
    if x['kind'] in ('h1', 'h2', 'h3'):
        lv = int(x['kind'][1])
        txt = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', re.sub(r'^#+\s*', '', x['md'])).replace('**', '').strip()
        path = [p for p in path if p[0] < lv] + [(lv, anchor_of.get(txt, txt))]
    where.append([p[1] for p in path])

out = []
for i, x in enumerate(blocks):
    if x['kind'] in ('h1', 'h2', 'h3', 'image', 'youtube', 'hr'):
        continue
    plain_links = [(m.start(), m.end(), m.group(2)) for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', x['md'])]
    for anc, pats in SUBJ.items():
        if anc in where[i]:
            continue
        for pat in pats:
            for m in re.finditer(pat, x['md'], re.I):
                inl = [h for a, b, h in plain_links if a <= m.start() < b]
                if any(anc in h for h in inl):
                    continue
                s = x['md']
                out.append('- **%s** in %s (%s), "%s": ...%s...%s' % (
                    anc, ' > '.join(where[i][-2:]), x['id'], m.group(0),
                    s[max(0, m.start() - 110):m.start()].replace('\n', ' '),
                    (' (inside a link to %s)' % inl[0][:60]) if inl else ''))
                break
print('# Unlinked mentions of a section\'s subject outside that section\n')
print('%d mentions. Each gets a fate in LINKS.md.\n' % len(out))
print('\n'.join(out))
