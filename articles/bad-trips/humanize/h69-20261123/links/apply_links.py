"""apply_links.py - the section links from the read of every mention (LINKS.md beside this file), from the repo root:

  python3 articles/bad-trips/humanize/h69-20261123/links/apply_links.py

Joel, 2026-11-23 19:13 UTC: "make sure that sections are linked to when mentioned or when they should be referenced".
Each link goes on words already in the guide; no word changes, so no Pangram check changes (the checks read the text
without its links). Each one is recorded in SECTION-LINKS.json, which section_links.py check reads. The two serotonin links go to How to
Check for SS, whose anchor has only plain characters (Serotonin Syndrome (SS)?'s is not yet seen on a rendered page),
and which is what both mentions need: the signs to look for.
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[5]
ART = REPO / 'articles' / 'bad-trips'
MD = ART / 'GUIDE-SO-FAR.md'
BL = ART / 'GUIDE-SO-FAR-blocks.json'
CAT = ART / 'SECTION-LINKS.json'
U = 'https://ibogaqueen.substack.com/i/170920118/'
A = {'AS': 'active-seizure', 'MBFD': 'my-brain-feels-damaged', 'CP': 'chest-pain-and-injury',
     'SS': 'how-to-check-for-ss', 'MBR': 'medical-and-brain-rescue', 'CMF': 'call-medics-for',
     'TIS': 'too-intense-stabilizers', 'DMSO': 'dmso', 'METTA': 'metta-sniffer-chill-love', 'BMG': 'beach-morning-glory',
     'MAG': 'mdma-magnesium-alarm', 'HUMIC': 'humic-acid-for-the-brain', 'AC': 'activated-charcoal',
     'ZEO': 'zeocharge-and-ferment', 'SHUNG': 'shungite-holy-water', 'WHO': 'who-to-contact',
     'WGOH': 'when-to-get-outside-help', 'NIACIN': 'niacin-flushes-trips-out', 'RUE': 'syrian-rue-oil-gentler'}

# (block, the words before, the words to link, the words after, target): before + words + after must occur once
LINKS = [
    ('B94', '- A ', 'seizure', ' after taking too much', 'AS'),
    ('B94', 'when the person cannot complete ', 'a basic neurological check', ' or is rapidly worsening', 'MBFD'),
    ('B94', 'radiating, or exertional ', 'chest pain', '--or chest pain with', 'CP'),
    ('B94', '- ', 'Concerning symptoms', ' after an MAOI', 'SS'),
    ('B95', '', 'The remedies below', ' can begin while help is being arranged.', 'MBR'),
    ('B100', "I'd ", 'calm and stabilize the trip', ' right where they are', 'TIS'),
    ('B100', 'none of the signs on the ', 'Call medics list', ' above show up', 'CMF'),
    ('R38-BRAIN-LIST', 'Watch for a ', 'seizure', ', and for vomiting', 'AS'),
    ('R38-BRAIN-LIST', 'really bad headache or ', 'chest pain', '', 'CP'),
    ('R37-CHEST-LIST', 'stroke signs from the ', 'brain checks', ' above show up', 'MBFD'),
    ('B144', '1. **', 'DMSO', ' immediately.', 'DMSO'),
    ('B144', '**Smell the ', 'Metta NMT sniffer', '**', 'METTA'),
    ('B144', 'use ', '*Ipomoea pes-caprae*', ' to stop the trip', 'BMG'),
    ('B144', 'magnesium chloride and ', 'the broader electrolyte branch', ' instead.', 'MAG'),
    ('N-WARN', "I'd also try sniffing ", 'humic/fulvic acid powder', '', 'HUMIC'),
    ('B111', 'consider topical ', 'DMSO', ' with a known-genuine CBD', 'DMSO'),
    ('B119', 'A ', 'seizure', ' or collapse can result', 'AS'),
    ('B122', '', 'DMSO', ' is also my first remedy', 'DMSO'),
    ('B126', 'are they suffering from ', 'slow and shallow breathing', ' (respiratory depression', 'CMF'),
    ('B126', 'Do you see symptoms of ', 'serotonin toxicity', ', like seizure', 'SS'),
    ('B127', '', 'Activated charcoal', ' may help after some recent oral ingestions', 'AC'),
    ('B154', 'which then requires ', 'activated charcoal', ' to reduce gut histamine', 'AC'),
    ('B161', 'I prefer ', 'zeolite', '.', 'ZEO'),
    ('B165', 'When ', 'ozonated zeolite and ferment', " don't help", 'ZEO'),
    ('R30-OILS2', "If you don't have the ", 'Metta NMT sniffer', ', just use', 'METTA'),
    ('B201', 'It overlaps with ', 'aged ozonated-charcoal water', ', but the two', 'SHUNG'),
    ('B178', 'MDMA remains ', 'a separate branch', ' centered on magnesium', 'MAG'),
    ('B211', 'compared with ', 'beach morning glory', '.', 'BMG'),
    ('B278', 'identify the local emergency number and ', 'crisis line', ' before you ever need them', 'WHO'),
    ('B333', '', 'The triage above', ' is meant to make trips useful.', 'WGOH'),
    ('B426', "I'd also try ", 'DMSO', ', niacin, and other', 'DMSO'),
    ('B426', "I'd also try [DMSO](%sdmso), " % U, 'niacin', ', and other', 'NIACIN'),
    ('B426', 'antipsychotics mentioned in this guide, like DMSO, ', 'syrian rue OIL', ', and niacin', 'RUE'),
    ('B426', 'my trusty relaxing herbs first, like ', 'beach morning glory', ', Syrian rue oil or the', 'BMG'),
    ('B426', ', Syrian rue oil or the ', 'Metta NMT sniffer', ', and natural antipsychotics', 'METTA'),
]


def section_of(blocks):
    sec, out = None, {}
    for x in blocks:
        if x['kind'] in ('h1', 'h2', 'h3'):
            import re
            sec = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', x['md'].lstrip('#').strip()).replace('**', '')
        out[x['id']] = sec
    return out


def main():
    blocks = json.loads(BL.read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    sec = section_of(blocks)
    cat = json.loads(CAT.read_text(encoding='utf-8'))
    done = 0
    for bid, before, words, after, t in LINKS:
        href = U + A[t]
        md = by[bid]['md']
        new = '%s[%s](%s)%s' % (before, words, href, after)
        if '[%s](%s)' % (words, href) in md:  # already linked (a re-run)
            continue
        old = before + words + after
        assert md.count(old) == 1, (bid, old, md.count(old))
        by[bid]['md'] = md.replace(old, new)
        done += 1
        link = {'in': sec[bid], 'text': words.strip('*'), 'href': href}
        if link not in cat['links']:
            cat['links'].append(link)
    MD.write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    BL.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for x in blocks:  # the links already in the guide from earlier rounds, in the catalog too
        import re
        for m in re.finditer(r'\[([^\]]+)\]\((%s[^)]+)\)' % re.escape(U), x['md']):
            link = {'in': sec[x['id']], 'text': m.group(1).strip('*'), 'href': m.group(2)}
            if link not in cat['links']:
                cat['links'].append(link)
    CAT.write_text(json.dumps(cat, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('linked %d; the catalog has %d section links' % (done, len(cat['links'])))


if __name__ == '__main__':
    main()
