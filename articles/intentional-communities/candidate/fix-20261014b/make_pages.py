"""The side-by-side pages after Joel's answers of 2026-10-14 21:19 UTC: sections 4, 9, 10 and 11.

New map versions from the last ones (fix-20261014/make_pages.py's): the same rows and source starts, the starts
that changed fixed, last turn's notes and proposal rows dropped (questions 22 to 26 are answered), today's notes on
the rows that changed, and the one new proposal (section 10). Highlights are against main at b8a061ec, the version
Joel last saw (this morning's pages, merged at the start of this turn).

Run from the candidate folder: python3 fix-20261014b/make_pages.py
"""
import json, pathlib, subprocess, sys

CAND = pathlib.Path(__file__).resolve().parent.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import render_in_context as R  # noqa: E402

SINCE = 'b8a061ec'
CUR = R.paragraphs((CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
DROP = (' · changed today', ' · changed this turn', ' · changed for your answer', ' (PROPOSAL)', ', a proposal')
FIRST = ('Your published section is on the left. On the right is the version now in the article so far. '
         'Highlighted words are new since the version you saw this morning, and struck words are ones that went.')
NOT_YET = 'Not checked in Pangram yet: I\'ll check it once you pick.'
B283 = json.loads((CAND / 'fix-20261014b' / 'gui' / 'b283-results.json').read_text(encoding='utf-8'))
B284 = json.loads((CAND / 'fix-20261014b' / 'gui' / 'b284-results.json').read_text(encoding='utf-8'))


def para(start):
    return R.plain(R.find(CUR, start, start))[0]


def swap(start, old, new):
    text = para(start)
    assert text.count(old) == 1, (start, old)
    return text.replace(old, new)


def got(r, key, what='alone'):
    x = r[key]
    return 'Pangram: Human %s (%d words, %s UTC, %s).' % (what, x['words'], x['utc'][11:19], 'batch ' + ('283g' if r is B283 else '284g'))


def build(name, old, meta, intro, fixes=None, changed=None, proposals=None):
    fixes, changed, proposals = fixes or {}, changed or {}, proposals or []
    m = json.loads((CAND / 'in-context' / old).read_text(encoding='utf-8'))
    out = {'title': m['title'], 'meta': meta, 'intro': intro, 'blocks': []}
    used = set()
    for blk in m['blocks']:
        rows = []
        for r in blk['rows']:
            if 'text' in r:          # last turn's proposals: answered
                continue
            r2 = {k: v for k, v in r.items() if k not in ('notes', 'note', 'flag', 'repeats')}
            lab = r2.get('label', '')
            for d in DROP:
                lab = lab.replace(d, '')
            r2['label'] = lab
            if 'article' in r2:
                r2['article'] = next((new for old_, new in fixes.items() if r2['article'].startswith(old_)), r2['article'])
                for k, (suffix, notes) in changed.items():
                    if r2['article'].startswith(k):
                        r2['label'] = (lab + ' · ' + suffix) if lab else suffix
                        r2['notes'] = notes
                        used.add(k)
            rows.append(r2)
            for p in proposals:
                if 'article' in r2 and r2['article'].startswith(p['after']):
                    rows.append({'label': p['label'], 'text': p['text'], 'proposal_of': r2['article'],
                                 'source': r2.get('source', []), 'notes': p['notes']})
                    used.add('P:' + p['label'])
        out['blocks'].append({'headings': blk.get('headings', []), 'rows': rows})
    missing = [k for k in changed if k not in used] + [p['label'] for p in proposals if 'P:' + p['label'] not in used]
    assert not missing, (name, missing)
    path = CAND / 'in-context' / name
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return path


PAGES = []

PAGES.append((build('ic04-v7.json', 'ic04-v6.json',
    'Community article · section 4 · v11.2, 2026-10-14 21:19 · your final section, in the article so far as a candidate',
    [FIRST,
     'What changed: your answers 24 ("p10 agree": "If one of the four gets skipped") and 26 ("sect 4: yes": without "and don\'t freeze into doctrine").',
     'Pangram\'s web app: each changed paragraph reads Human with its neighbor (both are under 50 words; 283g), and the whole section 100%% Human (%d words, %s UTC, batch 284g).' % (B284['S4v112']['words'], B284['S4v112']['utc'][11:19]),
     'Your fixed reparenting paragraph with "And inner pl/ork is built on ..." didn\'t come through: in your message, "here\'s the fixed reparenting + 3 sentence para:" goes straight on to 25, and the attachment holds section 11 only. Could you paste it again? (27 on the questions page.)',
     'One more for you: the diagram in this section (image 7) still says "authority stays with the practitioner" under the roof, from the published principle. Your text now says "our practices weave the community into the quilt", and membership depends on the community\'s processes (your F13 answer). The stance check flagged the clash. It\'s your image, so only you can change it; my pick is to change that line to match your text (question 29).'],
    fixes={'If one of them gets skipped': 'If one of the four gets skipped'},
    changed={
        'Nothing suppressed, everything processed.': ('changed today', [
            'Your 26: "and don\'t freeze into doctrine" is out; two paragraphs later "When agreements get frozen, religious communities tend to call the frozen version doctrine." carries it.',
            got(B283, 'J4-P1pair', 'with your next paragraph')]),
        'If one of the four gets skipped': ('changed today', [
            'Your 24: "the four" for "them".',
            got(B283, 'J4-P10pair', 'with the paragraph before')])}),
    'community-section4-side-by-side.html'))

PAGES.append((build('ic09-v5.json', 'ic09-v4.json',
    'Community article · section 9 · v16, 2026-10-14 21:19 · in the article so far as a candidate',
    [FIRST,
     'What changed: your 26 ("sect 9: yes"): "The useful thing is how they learn:" for "The useful thing isn\'t their diagram. It\'s how they learn:".',
     'Pangram\'s web app: the paragraph reads Human alone, and the section 100%% Human (%d words, %s UTC, batch 284g).' % (B284['S9v16']['words'], B284['S9v16']['utc'][11:19])],
    changed={
        "And that's not me saying that": ('changed today', ['Your 26.', got(B283, 'J9-P14')])}),
    'community-section9-side-by-side.html'))

S10 = 'Whenever you create or apply a rule'
PAGES.append((build('ic10-v4.json', 'ic10-v3.json',
    'Community article · section 10 · v3, 2026-10-14 21:19 · in the article so far as a candidate',
    [FIRST,
     'What changed: your last paragraph of 21:19 ("this version is clearer and passes"), as you wrote it.',
     'Pangram\'s web app: it reads Human alone (283g), and the section 100%% Human (%d words, %s UTC, batch 284g).' % (B284['S10v3']['words'], B284['S10v3']['utc'][11:19]),
     'One flag, from both cold reads of the section: the paragraph reads as a new topic. Nothing ties it to the federation paragraphs before it, and they couldn\'t tell whose rules these are. My proposal is one word, under it.'],
    fixes={'When you create or apply a rule': S10},
    changed={
        S10: ('yours, changed today', [
            'Your 25, as you wrote it.', got(B283, 'J10-P5')])},
    proposals=[
        {'after': S10, 'label': 'PROPOSAL · question 28 (my pick)',
         'text': swap(S10, 'Whenever you create or apply a rule,', 'Whenever you create or apply a federation rule,'),
         'notes': ['Both cold reads: "nothing ties it to the heading about federated communities or to P6\'s exchanges and obligations"; "whose rules?". "A federation rule" ties it to the section and to the limits just before it. If you meant any rule, in a community too, the other fix is to say so: "Whenever a community or a federation creates or applies a rule".', NOT_YET]}]),
    'community-section10-side-by-side.html'))

PAGES.append((build('ic11-v6.json', 'ic11-v5.json',
    'Community article · section 11 · v15, 2026-10-14 21:19 · your text, in the article so far as a candidate',
    [FIRST,
     'What changed: your text of the first subsection as you pasted it (your 22 and 23: P2\'s definition, your P3 and P4, my P6 lead-in, P8\'s "the people who review the founder"; and single spaces in J3), and R15 without its "living balance" sentence (your 26).',
     'Pangram\'s web app: every changed paragraph reads Human alone (P2 with P3, since it\'s under 50 words; 283g), and the whole section 100%% Human (%d words, %s UTC, batch 284g).' % (B284['S11v15']['words'], B284['S11v15']['utc'][11:19]),
     'You asked me to say if you overlooked anything. A cold read of the section found nothing to stop a reader (the second read broke off), the stance check found nothing in your paragraphs that conflicts with the rest of the article, and the repeats check found nothing inside the section that doesn\'t add a step. Of what P4 lost, "Can people disagree, leave, and later tell a different story about it?" is still in P10\'s signs, and "A group can keep its members because people love it, or because leaving costs too much." is in your "without being trapped". The one thing said nowhere else now is "Is the community still materially viable?". My opinion: fine without it, since it\'s about the method, not the founder.'],
    fixes={'I know this personally': "I've seen founderism",
           'Here are the four questions about the founder': 'The questions so far have been about the method'},
    changed={
        'That person ends up': ('yours, changed today', [
            'Your 22: "founderism isn\'t my term, it\'s in the commune literature". Your definition is about timing: power that "fails to get distributed as the conditions ripen".',
            got(B283, 'J11-P2P3', 'with P3')]),
        "I've seen founderism": ('yours, changed today', [got(B283, 'J11-P3')]),
        'A few things help keep that in check': ('yours, changed today', [
            'Your 23: "there was too much stuff in that p4". Five questions now, and your own judgment to close it.',
            got(B283, 'J11-P4')]),
        'The questions so far have been about the method': ('changed today', ['Your 23: "P6: ok good use yours".']),
        'Then follow the practical power.': ('changed today', ['Your 23: "P8 agree".']),
        "It's a bit like the process of getting married": ('changed today', ['Two double spaces are single, as in your paste.']),
        'Peer counseling can become peer surveillance': ('changed today', [
            'Your 26: "There are pros and cons to each extreme, and again, a living balance must be struck." is out.',
            got(B283, 'J11-R15')])}),
    'community-section11-side-by-side.html'))

if __name__ == '__main__':
    for mp, out in PAGES:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                            str(CAND / out), '--article', str(CAND / 'HUMANIZED-SO-FAR.md'),
                            '--source', str(CAND.parent / 'original.md'), '--since', SINCE],
                           capture_output=True, text=True)
        print(mp.name, '->', out, 'exit', r.returncode)
        print('  ' + '\n  '.join(l for l in (r.stdout + r.stderr).strip().split('\n') if 'label number was dropped' not in l))
