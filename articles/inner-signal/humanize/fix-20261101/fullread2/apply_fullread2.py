"""Put in what my second full read of the guide found (READER-1..18.md, FIXES-1..18.json), the two-hand merge Joel
asked for (S-636), and the contradiction fixes (E310); record every finding's fate.

Joel, 2026-11-01 18:57 UTC (joel-20261101-1857-message.txt and his answers ANSWERS-20261101-1850.json): read the whole
guide again for the places Emulate "made ... sound like a madman screaming" (R-508), the compressed and vague places
("the AI guide was also too vague"), lists missing "the relationships between things that explain them" (N-580), his
tells ('"one" is super ai', R-381), clearly needed commas (C-3), "inner child not child" (N-145); "go thru the guide to
make sure stuff isn't contradicting other stuff"; and for the two-hand practice, "rather than just being less clear about
the practice can we cut or merge some of the 4 dups?" (S-636). Lessons E306 to E310.

- A fix in FIXES-n.json is (old words, new words) in our words (Emulate's, the writers', mine); the few that touch his
  own sentences are obvious typos or punctuation, or a label he didn't write (listed in TOUCHES_HIS, each with why).
  A finding marked "card" is his own words and goes to him (CARDS); a finding with no fix is recorded with its reason.
- MERGE: the two-hand induction section is cut; its one new thing (his paragraph: divine Love above, the inner child
  below, the adult present, the massage) goes into The two-hand practice, with a line saying it also works as an
  induction (the Sober induction already offers it as an anchor). The troubleshooting line and Appendix D's inner child
  love say what to do with the hands again (Appendix D in his words of 30 October, R-630), naming the practice.
- CONTRA: contradictions the read across all parts found (CONTRADICTIONS.md) that are fixed in our words.

  python3 articles/inner-signal/humanize/fix-20261101/fullread2/apply_fullread2.py [--check]

Writes HUMANIZED-SO-FAR.md, APPLIED-FULLREAD2.json (each changed paragraph before and after, with its findings) and
DISPOSITIONS.json (every finding's fate, for compare_read.py record).
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
BEFORE_SHA = 'd4f3b12e'  # the guide with his answers of 1 November (commit b20792c6), the text the read read

# fixes that touch his own sentences, each with why it is allowed (hisfuzzy check: his versions and his 25 October list)
TOUCHES_HIS = {
    'F6.11': 'two obvious slips in his N-238 version, fixed as typos: a missing "with" and "its" for the plural methods',
    'F7.6': 'the closing quotation mark of his sentence (straight after a curly opening one)',
    'F11.17': 'the "DO NOT:" label and Emulate\'s "Utilize" in front of his 25 October change ("guard parts"), which '
              'stays; the label changes with the whole list\'s',
    'F13.5': 'the punctuation after his "dialog rhythm" (a colon and "ie." become a comma and "for example:")',
    'F13.19': 'quotation marks around the five questions (straight, like the others in his paragraph) and a comma after "Instead" in his version of 30 October '
              '(R-561); his words as they are',
}

# the two-hand merge (S-636): (what it does, old raw text, new raw text); applied before the fixes
MERGE = [
    ('cut the two-hand induction section; its blocks are the practice again, except his paragraph, which moves',
     '\n\n## The two-hand induction\n\nStart with the two-hand practice: one hand on your heart for your Nurturer, the '
     'other on your solar plexus for your vulnerable child.\n\nBreathe gently.\n\nImagine a divine Love from above, with '
     'the inner child below, in the solar plexus area. The inner adult is present. You can also use the hand on the '
     'solar plexus to massage that area. Say:\n\n“Sending my love down to my Child. If something comes back up, I let '
     'it, and send my love on down again. If nothing comes back, I just keep sending mine, and listening.”\n\n',
     '\n\n'),
    ('his paragraph from the two-hand induction, into The two-hand practice after the hands (without its "Say:", '
     'since the script it led into was the practice\'s loop again)',
     'on your solar plexus, where your child can be.\n\nBegin to send love',
     'on your solar plexus, where your child can be.\n\nImagine a divine Love from above, with the inner child below, '
     'in the solar plexus area. The inner adult is present. You can also use the hand on the solar plexus to massage '
     'that area.\n\nBegin to send love'),
    ('the practice also works as an induction (the Sober induction offers it as an anchor)',
     'This is a conversation with your child from your heart.\n\n## The Nurturer',
     'This is a conversation with your child from your heart.\n\nBreathe gently the whole time. The practice also works as '
     'an induction: it’s one of the anchors you can choose in the Sober induction below.\n\n## The Nurturer'),
    ('troubleshooting says what to do with the hands, naming the practice',
     'Do the two-hand practice and say,',
     'Put one hand on your heart and the other on your solar plexus, as in the two-hand practice, and say,'),
    ('Appendix D says what to do with the hands, in his words of 30 October (R-630), naming the practice',
     'Do the two-hand practice from Working with your inner child, and say to yourself in a loving way,',
     'Put your hand over your heart and your other hand on your solar plexus (the two-hand practice in Working with your '
     'inner child), and say to yourself in a loving way,'),
]
MERGED_AWAY = {'F7.7': 'its paragraph (Start with the two-hand practice ...) was cut with the two-hand induction (S-636)',
               'F7.8': 'its paragraph (the two-hand induction\'s script) was cut with the two-hand induction (S-636)'}

# contradictions fixed in our words (CONTRADICTIONS.md): (id, old, new)
CONTRA = [
    ('K2', 'and that can ironically lead instead to more foolish indifference.',
     'and that can ironically lead instead to more foolish indifference. So when I say to invoke your Higher Self, I mean '
     'stepping into that wider view while you keep your own judgment.'),
]

# findings left as they are, each with why (no fix in FIXES-n.json)
LEFT = {'F14.3': ['his', 'his own sentence (his version of 30 October, b483): "some kind of proof" stays as he wrote it']}

# his own words: to him as cards (CARDS-FULLREAD2.json builds the page)
CARDS = ['F1.6', 'F7.5', 'F18.1']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha.startswith(BEFORE_SHA), 'the guide changed since the read: %s' % sha[:8]
    before_blocks = sr.blocks(md)
    log = []
    for what, old, new in MERGE:
        assert md.count(old) == 1, (what, md.count(old))
        md = md.replace(old, new)
        log.append({'merge': what})
    fixes = []
    for n in range(1, 19):
        fx = json.loads((HERE / ('FIXES-%d.json' % n)).read_text(encoding='utf-8'))
        for fid, f in fx.items():
            fixes.append((fid, f))
    fates = {}
    lost = []
    for fid, f in fixes:
        if f == 'card':
            assert fid in CARDS, fid
            fates[fid] = ['his', 'his own words: on his cards page (CARDS-FULLREAD2.json)']
            continue
        if fid in MERGED_AWAY:
            fates[fid] = ['done', MERGED_AWAY[fid]]
            continue
        old, new = f
        k = md.count(old)
        if k == 1:
            md = md.replace(old, new)
        else:
            assert k == 0, (fid, k)
            # the words are plain text inside a paragraph with markup (a link): change the paragraph's text and keep
            # its links (set_block_text)
            raw = re.split(r'\n\s*\n', md.rstrip('\n'))
            bl = sr.blocks(md)
            hit = [i for i, b in enumerate(bl) if b['text'].count(old) == 1]
            assert len(hit) == 1, (fid, len(hit), old[:60])
            i = hit[0]
            raw[i] = set_block_text(raw[i], bl[i]['text'].replace(old, new), lost)
            md = '\n\n'.join(raw) + '\n'
        fates[fid] = ['fixed', TOUCHES_HIS.get(fid, 'in our words')]
    for cid, old, new in CONTRA:
        assert md.count(old) == 1, cid
        md = md.replace(old, new)
        log.append({'contradiction': cid})
    for fid, v in LEFT.items():
        fates[fid] = v
    # every finding of the read has a fate
    import compare_read as cr
    recs = []
    for n in range(1, 19):
        recs += cr.parse_reader((HERE / ('READER-%d.md' % n)).read_text(encoding='utf-8'), n)[0]
    ids = [r['id'] for r in recs]
    missing = [i for i in ids if i not in fates]
    assert not missing, missing
    after_blocks = sr.blocks(md)
    bt = [b['text'] for b in before_blocks]
    at = [b['text'] for b in after_blocks]
    import difflib
    changed = []
    sm = difflib.SequenceMatcher(None, bt, at, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        changed.append({'op': op, 'before': bt[i1:i2], 'after': at[j1:j2], 'after_blocks': list(range(j1, j2)),
                        'before_blocks': list(range(i1, i2))})
    rec = {'before_sha256': sha, 'after_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'findings': len(ids), 'fates': dict(collections_count(fates)), 'links_dropped': lost,
           'merge_and_contradictions': log, 'touches_his': TOUCHES_HIS, 'changed': changed}
    print(json.dumps({k: rec[k] for k in ('before_sha256', 'after_sha256', 'findings', 'fates', 'links_dropped')},
                     indent=1), len(changed), 'changes (runs of paragraphs)')
    if not a.check:
        GUIDE.write_text(md, encoding='utf-8')
        (HERE / 'APPLIED-FULLREAD2.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n',
                                                    encoding='utf-8')
        (HERE / 'DISPOSITIONS.json').write_text(json.dumps(fates, ensure_ascii=False, indent=1) + '\n',
                                               encoding='utf-8')


def collections_count(fates):
    from collections import Counter
    return Counter(v[0] for v in fates.values())


if __name__ == '__main__':
    main()
