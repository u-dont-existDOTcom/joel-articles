"""Batch 480: candidates for the red stretches of batch 479's recheck (read after Joel's message of 2026-10-26 00:54 UTC;
../../fix-20261025/b479/recheck/RESULT-A.json, RESULT-B.json, SCORE-A.md, SCORE-B.md).

Batch 479's recheck read S2, S3a, S3b, S4, S5 and S6 Human in place. Red in it:
- S1 (part A, High, 27 words): his inner child guide's whole sentence, "That's one grown-up doing three jobs, not three more
  people moving in to help with the rent, and each job keeps the others in balance." It was Low as IC-A2's cut one.
- Working with your guards P3's last two sentences (IC-A14's words, approved by him) and the start of P4, his own exercise
  lines from his inner child guide (IC-A15): Medium, High, Medium, Low; one Human, Low window of 96 words last time.
- Your inherited parent script P1's middle two sentences, unchanged since recheck A4 (Low and Medium, marked humanized);
  Human, High and Medium, last time.
- Appendix G P1's "Borrowed is fine, as long as it's from someone steady who won't try to run your trip for you." (part B,
  Low; IC-B19, from his inner child guide); Human, Low, last time.
Nothing in the last three changed between the two checks: the windows around them did (batch 479's edits upstream).

Emulate first (E237, E235): three samples of each red paragraph (BUNDLE.json, make_bundle.py; on the laptop
emu-b480-c28a5b2a8e47 and emu-hg-cj, -ck, -cl; outputs in cj/, ck/, cl/). Only the red sentences are spliced; his own
exercise lines in P4 stay (E214: his words go back to him, and their red sat in the window with IC-A14's sentence).

  python3 articles/inner-signal/humanize/fix-20261026/b480/make_b480.py   (from the repo root)
Writes CANDIDATES.json, CANDIDATE-MASTER.md (batch 479's candidate master with these in), REVIEW-PROMPT-1.txt and
REVIEW-PROMPT-2.txt (the meaning readers', two items each), TEXTS.json and b480-items.json (the API checks).
"""
import hashlib
import json
import pathlib
import re
import sys

B = pathlib.Path(__file__).resolve().parent
ROOT = B.parents[4]
H = ROOT / 'articles/inner-signal/humanize'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
import apply_answers as AA  # noqa: E402

BASE = H / 'fix-20261025' / 'b479' / 'CANDIDATE-MASTER.md'
IC_JOBS = 'That’s one grown-up doing three jobs, not three more people moving in to help with the rent, and each job keeps the others in balance.'


def sample(run, key):
    return (B / run / (key + '.out.txt')).read_text(encoding='utf-8')


def cut(text, first, last):
    a = text.index(first)
    z = text.index(last, a) + len(last)
    assert text.count(first) == 1, first
    return text[a:z]


# 'from': a list of (run, key, first words, last words) pieces, joined with a space
SPOTS = {
    'S7': {'part': 'A', 'card': 'IC-A2', 'where': 'The inner child, the guards, and the inner adult’s three jobs, P2',
           'old': IC_JOBS,
           'from': [('cl', 'HG-A-jobs2', 'It’s one person doing three jobs', 'keep the others in balance')],
           'fixes': [('keep the others in balance', 'keep the others in balance.',
                      'the sample went on "and it’s you who needs to develop ..."; his next sentence, "It’s you that needs to develop these qualities.", stays, so the spliced one ends here'),
                     ('Each job helps to keep the others in balance.', 'Each job keeps the others in balance.',
                      'the meaning read (REVIEW-1.md) found "helps to" softens his "each job keeps the others in balance"; his own verb put back')],
           'published': ('His inner child guide (The Chicken-and-Egg Problem), his own words: "' + IC_JOBS + '"\n(The published '
                         'hypnosis guide: "I organize that adult capacity into three functions: Nurturer, Protector, and '
                         'Leader/Guru. They aren’t three literal beings. They’re three ways the present-day person reparents the '
                         'inner child.")'),
           'red': 'High, 27 words: his whole sentence', 'api': True, 'lineage': 'HG-three-jobs-P2'},
    'S8': {'part': 'A', 'card': 'IC-A14', 'where': 'Working with your guards, P3',
           'old': "But before you decide where it's coming from, ask it what it's trying to stop, or what it wants. It could also be your inner child, mad that you took so long to come back, or your inherited parent script, or something from earlier today, or a bit of each.",
           'from': [('ck', 'HG-A-guards', 'Before figuring out what/where it is', 'or a combination.')],
           'fixes': [('or a combination.', 'or a bit of each.',
                      'the gate\'s linter fails a list of three in model words (E125, E186) unless it ends on a casual catch-all; '
                      'IC-A14, the card he approved, ends "or a bit of each", put back for Emulate\'s "or a combination"')],
           'published': ('IC-A14, the alignment card he approved on 2026-10-25 (19:42 UTC), whose two sentences these are: "But '
                         'before you decide where it\'s coming from, ask it what it\'s trying to stop, or what it wants. It could '
                         'also be your inner child, mad that you took so long to come back, or your inherited parent script, or '
                         'something from earlier today, or a bit of each."'),
           'red': 'Medium and High (with the start of P4): these two sentences', 'api': True, 'lineage': 'HG-guards-P3',
           'with_next': True},
    'S9': {'part': 'A', 'card': None, 'where': 'Your inherited parent script, P1',
           'old': 'This is the set of rules and ways of treating yourself that you internalized as a child, mostly based on how your parent(s) treated you, and it doesn’t always sound like a voice. This is not the same as your inner adult (Nurturer, Protector, Guide) that you build up on purpose.',
           'from': [('cj', 'HG-A-script', 'Your parent script is made up of', 'by your parent(s)).'),
                    ('ck', 'HG-A-script', 'It doesn’t always take the form of a voice', 'form of a voice'),
                    ('cj', 'HG-A-script', 'It is not the inner adult', 'that you consciously build.')],
           'fixes': [('form of a voice It is not', 'form of a voice. It is not',
                      'the end of ck\'s sentence, cut before its bracket (cj\'s next sentence says the same without "later", which ck added)'),
                     ('It is not the inner adult', 'This is not the inner adult',
                      'the gate\'s linter (R2; Joel 2026-10-17: "this" is not the same as "it"): the paragraph\'s "This is not the same as '
                      'your inner adult" became "It is not"; its "This" put back')],
           'published': ('The paragraph since recheck A4, where it read Human (these two sentences): "This is the set of rules and '
                         'ways of treating yourself that you internalized as a child, mostly based on how your parent(s) treated '
                         'you, and it doesn’t always sound like a voice. This is not the same as your inner adult (Nurturer, '
                         'Protector, Guide) that you build up on purpose."'),
           'red': 'Low (35 words) and Medium (18 words), both marked humanized: these two sentences', 'api': True,
           'lineage': 'HG-parent-script-P1'},
    'S10': {'part': 'B', 'card': 'IC-B19', 'where': 'Appendix G: Altered states, P1',
            'old': 'Borrowed is fine, as long as it’s from someone steady who won’t try to run your trip for you.',
            'from': [('cl', 'HG-B-altered', 'Borrow some from someone else', 'try to direct your trip.')],
            'fixes': [],
            'published': ('His inner child guide, where IC-B19 took it from: "Borrowed is fine, as long as it’s from someone steady '
                          'who won’t try to run your trip for you." ("Borrowed" is the Nurturer and Protector of the sentence '
                          'before, borrowed from someone else.)'),
            'red': 'Low, 21 words: this sentence', 'api': False},
}
# Two of batch 479's candidates failed the owner-delivery gate's linter as they stood (E41 coach register: one coach
# phrase in a short draft is over its limit of 2 per 100 words, and a mechanical FAIL can't be waived for model prose):
# S3a's "you can use" and S5's "You don't have to fake it!". The smallest fixes, applied here so the page, the gate and
# the next recheck all have them: S3a without "you can", and S5's last sentence as batch 479's other two samples (ci and
# cg) put it, "Don't fake it."
B479 = H / 'fix-20261025' / 'b479' / 'CANDIDATES.json'
_c479 = __import__('json').loads(B479.read_text(encoding='utf-8'))['spots']
SPOTS['S3a2'] = {'part': 'A', 'card': 'RR-4.6', 'where': 'Before you begin, P3', 'old': _c479['S3a']['new'],
                 'new': _c479['S3a']['new'].replace('opened, you can use the later', 'opened, use the later'),
                 'from': [], 'fixes': [], 'published': _c479['S3a']['published'],
                 'red': 'batch 479\'s S3a, Human in place; the linter\'s E41 coach register failed "you can use"', 'api': False,
                 'source': 'batch 479\'s S3a (sample ci) without "you can" (the gate\'s linter)'}
# S5's second fix (2026-10-26, the gate's preservation review of "Don't fake it.", G-S5/REVIEW-preservation.json): his line
# is a release ("no faking required"), and "Don't fake it." made it a rule. His own three words end Emulate's sentence
# instead, as his inner child guide ends the line ("... notice what you find, no faking required."); the linter reads it
# REVIEW (no coach phrase, no short landing).
SPOTS['S5b'] = {'part': 'B', 'card': 'IC-B14', 'where': 'Inner child love, P1', 'old': _c479['S5']['new'],
                'new': _c479['S5']['new'].replace(' see what you feel. You don’t have to fake it!', ' see what you feel, no faking required.'),
                'from': [], 'fixes': [], 'published': _c479['S5']['published'],
                'red': 'batch 479\'s S5, Human in place; the linter\'s E41 coach register failed "You don\'t have to fake it!", and the '
                       'preservation review failed "Don\'t fake it." (a rule where his line is a release)',
                'api': False, 'source': 'batch 479\'s S5 (sample ch) with his own last words from his inner child guide, "no faking required"'}
assert SPOTS['S3a2']['new'] != SPOTS['S3a2']['old'] and SPOTS['S5b']['new'] != SPOTS['S5b']['old']

NAMES = {
    'S7': 'the guide\'s section on the inner adult: what the grown-up you build up does, in three jobs',
    'S8': 'what to do when, instead of your inner child, you meet numbness, cynicism, urges and the like in an inner meeting',
    'S9': 'the inherited parent script, the internalized rules that are not the inner adult',
    'S10': 'an appendix on altered states: learn the inner child work sober first, with enough inner adult present',
}


def build():
    md = BASE.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    by = {sr.where(bl, b['i']): b['i'] for b in bl}
    new_text, cands = {}, {}
    for k, s in SPOTS.items():
        i = by[s['where']]
        t = new_text.get(i, bl[i]['text'])
        flat = lambda x: x.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'}))
        old = s['old']
        if t.count(old) != 1:   # the working copy mixes straight and curly quotes; match either
            k0 = flat(t).find(flat(old))
            assert k0 >= 0 and flat(t).count(flat(old)) == 1, (k, old[:50])
            old = t[k0:k0 + len(old)]
        pieces = [cut(sample(run, key), first, last) for run, key, first, last in s['from']]
        raw_new = ' '.join(pieces) if pieces else s['new']
        new = raw_new
        done = []
        for a, b, why in s['fixes']:
            assert new.count(a) == 1, (k, a)
            new = new.replace(a, b)
            done.append({'replace': a, 'with': b, 'why': why})
        new_text[i] = t.replace(old, new)
        cands[k] = {'part': s['part'], 'card': s['card'], 'where': s['where'], 'block': i, 'red': s['red'],
                    'samples': ['%s/%s' % (r, kk) for r, kk, _, _ in s['from']], 'source': s.get('source'), 'old': old, 'sample_words': raw_new,
                    'new': new, 'fixes': done, 'published': s['published'], 'api': s['api'], 'lineage': s.get('lineage'),
                    'left': s.get('left', []), 'note': s.get('note')}
    out, lost = list(raw), []
    for i, t in new_text.items():
        out[i] = AA.set_block_text(raw[i], t, lost)
    assert not lost, lost
    master = '\n\n'.join(out) + ('\n' if md.endswith('\n') else '')
    bl2 = sr.blocks(master)
    for k, c in cands.items():
        c['paragraph_after'] = bl2[c['block']]['text']
        assert c['new'] in c['paragraph_after'], k
        prev, nxt = c['block'] - 1, c['block'] + 1
        c['paragraph_before'] = bl2[prev]['text'] if bl2[prev]['level'] == 0 else '(the heading "%s")' % bl2[prev]['text']
        c['paragraph_next'] = bl2[nxt]['text'] if bl2[nxt]['level'] == 0 else '(the heading "%s")' % bl2[nxt]['text']
    (B / 'CANDIDATE-MASTER.md').write_text(master, encoding='utf-8')
    rec = {'base': str(BASE.relative_to(ROOT)), 'base_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'candidate_master_sha256': hashlib.sha256(master.encode('utf-8')).hexdigest(), 'spots': cands}
    (B / 'CANDIDATES.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return cands


def prompt(cands, keys, path, out_name):
    items = []
    for n, k in enumerate(keys, 1):
        c = cands[k]
        items.append('## Item %d (%s)\n\nBEFORE:\n%s\n\nPUBLISHED:\n%s\n\nNOW:\n%s\n\nCHANGED WORDS IN NOW:\n%s\n\nAFTER:\n%s\n' % (
            n, NAMES[k], c['paragraph_before'], c['published'], c['paragraph_after'], c['new'], c['paragraph_next']))
    head = (
        "You check %d rewritten passages of Joel's long self-hypnosis guide (how to learn self-hypnosis safely, with inner "
        "child and parts work, and many safety cautions). The guide is self-guided: the reader leads themselves, so \"you\" "
        "is the reader. In each NOW paragraph only the CHANGED WORDS are new (a detector-passing rewrite); the rest of NOW "
        "read human already and stays. PUBLISHED is the meaning to keep: the words the change replaces, which the author "
        "wrote or approved, with where they come from. Safety cautions and steps matter most.\n\n"
        "For each item, say in a few words each:\n"
        "1. MEANING: do the CHANGED WORDS keep every point, step, caution and claim of PUBLISHED that they replace, with the "
        "same strength (nothing made more or less certain or more optional, no instruction turned into a suggestion, no "
        "safety caution weakened, no step lost)? KEPT, or what CHANGED or was LOST, and anything ADDED that a reader would "
        "take as a claim.\n"
        "2. SENSE: would a reader understand NOW in its place, between BEFORE and AFTER? OK, or the words that stop them "
        "and why.\n"
        "End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning and sense only, not style or "
        "grammar (the casual grammar, run-on sentences and comma splices are on purpose), and suggest the smallest "
        "possible rewrite only for a problem you report.\n\n"
        "Write your report with a single Write call to `%s`, one \"## Item N\" part per item, then reply with only the "
        "verdicts, one line per item. Don't read any other file, don't run commands, and don't use the web.\n\n" % (
            len(keys), B / out_name))
    path.write_text(head + '\n'.join(items), encoding='utf-8')


def api_texts(cands):
    texts = {}
    for k, c in cands.items():
        if not c['api']:
            continue
        t, name = c['paragraph_after'], 'b480-%s-p' % k
        if SPOTS[k].get('with_next'):
            t, name = t + '\n\n' + c['paragraph_next'], 'b480-%s-p+next' % k
        texts[name] = t
    (B / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    items = [[n, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for n, t in texts.items()]
    (B / 'b480-items.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return texts


if __name__ == '__main__':
    cands = build()
    for keys, name, report in ((['S7', 'S8'], 'REVIEW-PROMPT-1.txt', 'REVIEW-1.md'),
                               (['S9', 'S10'], 'REVIEW-PROMPT-2.txt', 'REVIEW-2.md')):
        if not (B / name).exists():
            prompt(cands, keys, B / name, report)
    texts = api_texts(cands)
    for k, c in cands.items():
        print(k, '|', c['new'])
    print('API texts:', {n: len(t.split()) for n, t in texts.items()})
