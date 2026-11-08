"""His versions of blocks 37 and 38 (answers of 2026-11-08 00:49 UTC, ANSWERS-X1107C-20261108-0049.json).

Block 37 is the text of his own last Pangram check, read back from his history (it is not in the card's box):
https://www.pangram.com/history/b1bd7488-ed0c-42f7-be0c-3bd6fd46bcc8 (Human Written, one window Human at High, 167 words).
His comment: "fixed the science and made it clearer, now it passes but your last part is human medium conf: [02f568ff]
... clarified more and now all high conf: [b1bd7488]".

Block 38 is the text in his card: "did you even read what you had there? it was making no sense. i removed most of it and
just put the basic facts."

What I fix in his words without a card (lesson bad-trips-2026-11-07e: his typos are fixed, the fixed version checked,
and it goes in): "which s" to "which is"; the two Markdown links he typed with a space before the address and an
unclosed bracket; the citation links his plain-text paste dropped (Wilson 2015, Boyle 2013, Wang 2025), put back to the
sources they had; Conrad's year, 2009 to 2008 (Rev Neurosci 2008;19(6):395-411; the 2009 date is when PubMed Central
posted the manuscript); the trailing space. Two claims in his words that his sources don't support go to him on a card.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/apply_his_x1107c.py [--write]
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ANS = HERE / 'ANSWERS-X1107C-20261108-0049.json'

HIS37_CHECKED = (
    'The Mechanism: When glutamate floods into the neuron, it jams open the NMDA "doors" (receptors), which allows '
    'calcium to flood in. Calcium at such high levels caused by stress can swell and injure the neurons. Possibly as a '
    'protective mechanism, those neurons have been observed (in rats) to pull back their complex interactions with other '
    'neurons for up to two weeks after a stressful event ([Bonifacino, et al, 2023] '
    '(https://www.nature.com/articles/s41398-023-02366-w). It\'s theorized that chronic stress on neurons also makes them '
    'more vulnerable to other toxic insults ([Conrad, 2009] (https://pmc.ncbi.nlm.nih.gov/articles/PMC2746750/)), which s '
    'kind of common sense. What does all that feel like? Although popular neuroscience doesn\'t communicate this well, '
    'neurotransmitters affect different brain regions differently. Under chronic stress, glutamate rises in the part of '
    'the amygdala that flags threats (Wilson, 2015), producing anxiety, rage, all that good stuff. Block the NMDA '
    'receptors there, and anxious behaviour drops in animals (Boyle, 2013).')
HIS37_SHA = None  # filled from the text above, checked against his history below

HIS37 = (
    'The Mechanism: When glutamate floods into the neuron, it jams open the NMDA "doors" (receptors), which allows '
    'calcium to flood in. Calcium at such high levels caused by stress can swell and injure the neurons. Possibly as a '
    'protective mechanism, those neurons have been observed (in rats) to pull back their complex interactions with other '
    'neurons for up to two weeks after a stressful event '
    '([Bonifacino, et al, 2023](https://www.nature.com/articles/s41398-023-02366-w)). It\'s theorized that chronic '
    'stress on neurons also makes them more vulnerable to other toxic insults '
    '([Conrad, 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2746750/)), which is kind of common sense. What does all '
    'that feel like? Although popular neuroscience doesn\'t communicate this well, neurotransmitters affect different '
    'brain regions differently. Under chronic stress, glutamate rises in the part of the amygdala that flags threats '
    '([Wilson, 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4721288)), producing anxiety, rage, all that good stuff. '
    'Block the NMDA receptors there, and anxious behaviour drops in animals '
    '([Boyle, 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3670432)).')

HIS38 = (
    'The Secondary Signal Dial (GluD Receptors): While NMDA receptor opening is the main spark that starts up neuronal '
    'excitation, another calcium door was recently discovered in the GluD receptors. What opens them is D-serine (one '
    'of the tools below) and GABA, the neurotransmitter that usually quiets down communication, not glutamate '
    '([Wang, et al, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12520249/)).')


def plain(t):
    return re.sub(r'\*([^*]+)\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t))


def main(write=False):
    ans = json.loads(ANS.read_text(encoding='utf-8'))
    md = ARTICLE.read_text(encoding='utf-8')
    assert ans['article']['sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), 'article changed since his page'
    t38 = [i for i in ans['items'] if i['id'] == 'T-38'][0]['your_version'].strip()
    assert plain(HIS38).replace(' (Wang, et al, 2025)', ' (Wang, et al, 2025)') == t38, 'block 38 differs from his card'
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    (i37,) = [k for k, b in enumerate(raw) if b.startswith('The Mechanism:')]
    (i38,) = [k for k, b in enumerate(raw) if b.startswith('The Signal Dial')]
    before = {'37': raw[i37], '38': raw[i38]}
    raw[i37], raw[i38] = HIS37, HIS38
    print('block 37: his checked version, with the typo, links and Conrad year fixed')
    print('block 38: his card version, with the Wang link put back')
    if write:
        ARTICLE.write_text('\n\n'.join(raw) + '\n', encoding='utf-8')
        (HERE / 'APPLIED-HIS-X1107C.json').write_text(json.dumps({
            'answers': ANS.name, 'answered_utc': ans['exported_at'],
            'block37': {'from': 'his Pangram check b1bd7488 (Human Written, Human High 167)',
                        'his_checked_text_sha256': hashlib.sha256(HIS37_CHECKED.encode('utf-8')).hexdigest(),
                        'fixed': ['"which s" to "which is"', 'two Markdown links repaired', 'Wilson and Boyle links put back',
                                  'Conrad 2009 to 2008 (publication year)'],
                        'before': plain(before['37']), 'after': plain(HIS37)},
            'block38': {'from': 'his card T-38', 'fixed': ['the Wang link put back', 'trailing space'],
                        'before': plain(before['38']), 'after': plain(HIS38)},
            'article_sha256_after': hashlib.sha256(ARTICLE.read_bytes()).hexdigest()},
            ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('written')
    return 0


if __name__ == '__main__':
    sys.exit(main('--write' in sys.argv))
