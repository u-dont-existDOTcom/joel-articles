"""CUTS.md: every decision of the overcompletion read (DECISIONS.json), for Joel to read on GitHub: what was cut, from where,
whose words it was, and what already said it; what was asked (question 32) and what was kept, with the reason. Block
numbers are the guide's before the cuts (090588f7). It replaces the first CUTS.md apply_cuts.py wrote, which had no
whose-words marks.

  python3 articles/inner-signal/humanize/fix-20261103/overcompletion/make_cuts_md.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent


def main():
    d = json.loads((HERE / 'DECISIONS.json').read_text(encoding='utf-8'))
    a = json.loads((HERE / 'APPLIED-CUTS.json').read_text(encoding='utf-8'))
    dec = d['decisions']
    his_pub = [x for x in dec if x['decision'] == 'cut' and 'published' in x['whose']]
    ours = [x for x in dec if x['decision'] == 'cut' and 'published' not in x['whose']]
    ask = [x for x in dec if x['decision'] == 'ask']
    keep = [x for x in dec if x['decision'] == 'keep']
    L = ['# The overcompletion read of 3 November: what was cut, asked and kept', '',
         'Joel, on card E-61 (2026-11-03 00:39 UTC): "cut all this. you didn\'t notice the massive overcompletion here? prob '
         'this whole guide is full of it then." Fresh readers read the guide in parts for anything explained a second time '
         '(BRIEF.md here), without knowing whose words were whose; the lead session read each find in place and decided '
         '(DECISIONS.json, make_decisions.py). The guide went from %s to %s: %d cuts, about %d words, %d paragraphs gone '
         'whole. Block numbers are the guide\'s before the cuts.' % (a['before_sha256'][:8], a['after_sha256'][:8],
                                                                    len(a['cuts_applied']), a['words_cut'],
                                                                    a['blocks'][0] - a['blocks'][1]), '']

    def item(x):
        out = ['- **[%d] %s**: ~~%s~~' % (x['block'], x['where'], x['cut'].strip())]
        if x.get('join') and x['decision'] == 'cut':
            out.append('  - now reads: %s' % x['join'])
        out.append('  - why: %s' % x['why'])
        return out

    L += ['## Cut, in our words (%d)' % len(ours), '']
    for x in ours:
        L += item(x)
    L += ['', '## Cut, lines of his published version that only said it again (%d)' % len(his_pub), '',
          'His card W-685 (2 November): "let\'s see what other redundancy remains in this article and cut that also". '
          'Each is back with one word from him.', '']
    for x in his_pub:
        L += item(x)
    L += ['', '## Asked, his own words (%d): question 32' % len(ask), '']
    for x in ask:
        L += ['- **[%d] %s**: %s' % (x['block'], x['where'], x['cut'].strip()), '  - why: %s' % x['why']]
    L += ['', '## Kept (%d)' % len(keep), '']
    for x in keep:
        L += ['- **[%d] %s** (%s): %s' % (x['block'], x['where'], x['whose'], x['cut'].strip()), '  - why kept: %s' % x['why']]
    (HERE / 'CUTS.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(len(ours), len(his_pub), len(ask), len(keep))


if __name__ == '__main__':
    main()
