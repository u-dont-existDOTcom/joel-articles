"""The hypnosis guide's marking page for batches 479 and 480 (REVIEW-480.json, REVIEW-480.html).

Joel, 2026-10-26 00:54 UTC, with batch 479's recheck results (part A
https://www.pangram.com/feed/9b9bedd2-a7d1-4141-9d85-168fbe3e81e4, part B
https://www.pangram.com/feed/84384f22-e09d-4a3b-bd39-a6617cd21cd1). The last turn's answer said each fix that reads Human in
the recheck comes to him next on a marking page, beside his own words; the stretches that read red again got Emulate's
re-run first (E235). So the page has ten cards on his working copy (HUMANIZED-SO-FAR.md, everything he approved):
- six of batch 479's, which read Human in place in that recheck (S2, S3a, S3b, S4, S5, S6; S3a and S5 with the small fixes
  the owner-delivery gate needed, ../b480/make_b480.py S3a2 and S5b);
- four of batch 480's, Emulate's versions of the four stretches that read red there (S7 for the three-jobs sentence, S8
  for IC-A14's two sentences, S9 for the parent script's two, S10 for IC-B19's "Borrowed is fine"), each read Human alone
  where it could be checked alone (480g), and now in the two temporary drafts for his next check (../b480/recheck/).
Every new sentence on the page is the gate's delivered text (../gate/<NAME>/FOR-JOEL.txt), byte for byte, and every
changed paragraph is the paragraph as the recheck has it (../b480/CANDIDATE-MASTER.md).

  python3 articles/inner-signal/humanize/fix-20261026/review/build_review_480.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import build_review as br  # noqa: E402  (its helpers, and the working copy as it is now)

sr = br.sr
br.match_style = lambda new, para: new   # the gate delivered these exact words; the post curls quote marks anyway
GIT_FILE = 'articles/inner-signal/humanize/fix-20261026/review/REVIEW-480.html'
B479 = json.loads((H / 'fix-20261025' / 'b479' / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots']
B480 = json.loads((H / 'fix-20261026' / 'b480' / 'CANDIDATES.json').read_text(encoding='utf-8'))['spots']
MASTER = sr.blocks((H / 'fix-20261026' / 'b480' / 'CANDIDATE-MASTER.md').read_text(encoding='utf-8'))
GATE = H / 'fix-20261026' / 'gate'
A = 'https://www.pangram.com/feed/9b9bedd2-a7d1-4141-9d85-168fbe3e81e4'
B = 'https://www.pangram.com/feed/84384f22-e09d-4a3b-bd39-a6617cd21cd1'
TYPES = {
    'held': {'label': 'Read Human where it stands',
             'about': 'Emulate\'s version of a stretch that read AI. In your last check of the whole guide it read Human in place.'},
    'alone': {'label': 'Read Human alone; in your next check',
              'about': 'Emulate\'s version of a stretch that read AI in your last check. It read Human checked on its own (one is too short to check alone), and it is in the two temporary drafts, so your next check shows how it reads in place.'},
}
FOUND = 'Pangram\'s check of the whole guide (your Substack drafts), then Emulate, the meaning reads and the gate\'s three reviewers'

# id: (gate NAME, the working copy's words (batch, spot), the new words (batch, spot), type, title, why, note)
CARDS = [
    ('HG-S7', 'G-S7', ('b479', 'S1'), ('b480', 'S7'), 'alone', 'One person, three jobs',
     'The line here now read AI (Low) two checks ago. In your last check (part A) your inner child guide\'s whole sentence, '
     'with the rent joke back, read AI (High): "That\'s one grown-up doing three jobs, not three more people moving in to help '
     'with the rent, and each job keeps the others in balance." Emulate\'s version, with your "keeps" put back, read Human '
     'checked alone. "Grown-up" becomes "person"; the sentences around it say it\'s you.',
     'Approve: the rent joke stays. Your next check shows how it reads in place.'),
    ('HG-S2', 'G-S2', ('b479', 'S2'), ('b479', 'S2'), 'held', 'Borrowed adulthood, the bridge',
     'This whole paragraph read AI (High) two checks ago. Emulate\'s version read Human checked alone, and Human where it '
     'stands in your last check (part A). Your two published points are back in it: the practices are familiar ones, and '
     'you don\'t claim the whole sequence is proven as one treatment.',
     'Approve: it reads Human in place and keeps your two points.'),
    ('HG-S3a', 'G-S3a', ('b479', 'S3a'), ('b480', 'S3a2'), 'held', 'Pointer to "Already open?"',
     'The end of this paragraph read AI (Low) two checks ago. Emulate\'s version read Human where it stands in your last '
     'check (part A). Since then "you can" is out (the gate\'s check counts it as coaching), so it says "use the later ... '
     'section". The section\'s own heading is in it so a reader can find it, and your "not stable" stays.',
     'Approve. Your next check reads the two-word change in place.'),
    ('HG-S3b', 'G-S3b', ('b479', 'S3b'), ('b479', 'S3b'), 'held', 'The three stop words',
     'These two sentences read AI (four Low windows) two checks ago. Emulate\'s three short sentences read Human where they '
     'stand in your last check (part A). Each of your words keeps what it does: "stop" ends the induction, "less" asks less '
     'of you, "quiet" stops the talking.',
     'Approve.'),
    ('HG-S8', 'G-S8', ('b480', 'S8'), ('b480', 'S8'), 'alone', 'Ask the guard what it wants first',
     'These two sentences (IC-A14, the inner child alignment card you approved) read Human two checks ago and AI (Medium '
     'and High) in your last check (part A), after the edits above them, and the red ran on into the guard prompt after '
     'them. Emulate\'s version read Human checked alone with the guard prompt after it. It ends on your card\'s "or a bit '
     'of each".',
     'Approve. Your next check also shows whether the guard prompt reads Human again.'),
    ('HG-S9', 'G-S9', ('b480', 'S9'), ('b480', 'S9'), 'alone', 'What the parent script is',
     'These two sentences hadn\'t changed: they read Human two checks ago and AI (Low and Medium) in your last check (part '
     'A), after the edits above them. Emulate\'s three sentences read Human checked alone. One word to know: '
     '"internalized" becomes "adopted", and the brackets still say it came from how you were treated. Checked alone, the '
     'paragraph\'s last two sentences (the critic or warden, and "fake") read AI, though they read Human in place last '
     'time; your next check shows how they read in place.',
     'Approve.'),
    ('HG-S4', 'G-S4', ('b479', 'S4'), ('b479', 'S4'), 'held', 'Big or hard-to-undo things wait',
     'These are your own two sentences from your inner child guide, and here they read AI (Low and High) two checks ago. '
     'Emulate\'s one sentence read Human checked alone, and where it stands in your last check (part B). It keeps both '
     'points: it has to make sense to you, and anything big or hard to undo waits till you\'re calm and have checked it '
     'against what you know. One change in strength: your "can wait" becomes "wait".',
     'Approve if the firmer "wait" is fine with you. Reject keeps your two sentences, which read AI here.'),
    ('HG-S5', 'G-S5', ('b479', 'S5'), ('b480', 'S5b'), 'held', 'No warmth today',
     'This line, from your inner child guide (the inner child alignment added it), read AI (High) here two checks ago. '
     'Emulate\'s version read Human where it stands in your last check (part B), ending "You don\'t have to fake it!". The '
     'gate\'s check counts "you don\'t have to" as coaching, and a reviewer turned down "Don\'t fake it." because it makes '
     'your permission a rule, so it ends on your own three words, "no faking required".',
     'Approve: Emulate\'s start, your ending. Your next check reads the new ending in place.'),
    ('HG-S6', 'G-S6', ('b479', 'S6'), ('b479', 'S6'), 'held', 'The test for a response',
     'Your published test, word for word, read AI here (High, 17 words) two checks ago. Emulate\'s question read Human '
     'checked alone, and where it stands in your last check (part B). It asks the same test: whether this way of '
     'responding helps you get clearer, steadier and less hooked.',
     'Approve if a question is fine there. Reject keeps your sentence, which read AI here.'),
    ('HG-S10', 'G-S10', ('b480', 'S10'), ('b480', 'S10'), 'alone', 'Borrowing Nurturer and Protector',
     'This sentence, from your inner child guide (the inner child alignment added it, IC-B19), read AI (Low) in your last '
     'check (part B). Emulate\'s version keeps both conditions: someone stable, and not someone who will take over your '
     'trip. It\'s one sentence, too short to check alone; your next check reads it in place.',
     'Approve.'),
]


def spot(ref):
    batch, k = ref
    return (B479 if batch == 'b479' else B480)[k]


def main():
    for sid, name, old_ref, new_ref, typ, title, why, note in CARDS:
        d = GATE / name
        delivered = (d / 'FOR-JOEL.txt').read_text(encoding='utf-8') if (d / 'FOR-JOEL.txt').exists() else None
        old_c, new_c = spot(old_ref), spot(new_ref)
        if delivered is None:
            print('SKIP', sid, '(not delivered by the gate)')
            continue
        assert delivered == new_c['new'], sid
        i = old_c['block']
        assert old_c['old'] in br.BL[i]['text'] or sr.norm_map(old_c['old'])[0] in sr.norm_map(br.BL[i]['text'])[0], sid
        s = br.add(sid, typ, title, 'approve', edits=[(i, old_c['old'], new_c['new'])], why=why, note=note, found_by=FOUND)
        after = s['edits'][0]['after']
        assert after == MASTER[i]['text'], (sid, after[:80], MASTER[i]['text'][:80])
    br.S.sort(key=lambda s: (br.first_block(s), br.order_key(s['id'])))
    br.overlaps()
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-b480-20261026',
        'title': 'Hypnosis Guide Emulate Fixes',
        'intro': [
            'This is your hypnosis guide as it is in Git now, with everything you approved. Each card is a sentence or two '
            'that read AI in one of your Pangram checks, with Emulate\'s version in its place. All of them passed the '
            'meaning reads and the gate\'s three reviewers.',
            'Six read Human where they stand in your last check (<a href="%s">part A</a>, <a href="%s">part B</a>). The '
            'other four are for the stretches that read AI in that check; each read Human checked alone, and they are in '
            'the two temporary drafts now, so your next check shows how they read in place.' % (A, B),
            'Click <b>Approve</b>, <b>Reject</b> or <b>Revise</b> on each card, and add a comment if you want. If you leave '
            'cards unmarked, tell me whether to take my advice on them as you did last time. Your answers save as you click.',
        ],
        'git_file': GIT_FILE, 'article': {'file': br.ARTICLE, 'sha256': hashlib.sha256(br.MD.encode('utf-8')).hexdigest()},
        'links': {'guide': br.BLOB + br.ARTICLE, 'review': br.BLOB + 'articles/inner-signal/humanize/fix-20261026/review/REVIEW-480.json'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': br.S,
    }
    probs = sr.check(review, br.BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-480.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, br.MD, br.BL)
    (HERE / 'REVIEW-480.html').write_text(page, encoding='utf-8')
    print(len(br.S), 'cards;', HERE / 'REVIEW-480.html', len(page), 'bytes')


if __name__ == '__main__':
    main()
