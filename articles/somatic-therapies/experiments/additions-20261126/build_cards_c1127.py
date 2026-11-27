#!/usr/bin/env python3
"""build_cards_c1127.py - the teaching cards of 2026-11-27 (turn of 19:25 UTC) for the somatic additions: the texts whose
Pangram tries are spent below High, each in place, with my best tested version, what each try read (with its link), and
room for his version (Revise). Two pages, one per guide:

  - review-c1127/REVIEW-SOMATIC.*: the somatic guide as it is live (WHOLE-LIVE-20261126.md) with two cards:
      A1-TEACH: "Can't Stay With a Feeling?", its first paragraph (six tries, all AI; best 91%) and its booking paragraph
                (six tries; best Human Low); the other three paragraphs read Human High by themselves.
      A3-TEACH: "Pain That Won't Quit?", its first paragraph (seven tries; best High 88 and Medium 18 over its last
                sentence; the join of that sentence waits on the section's near-miss gate); the other four read High.
  - review-c1127/REVIEW-INNER.*: the inner child guide as it is live (IC-WHOLE-LIVE-20261127.md, from the post fetched
      through his laptop at 20:11 UTC, IC-LIVE-POST-META-20261127.json), with two cards:
      IC1: the Imagery Rescripting pointer (Human High), for his eye; IC2-TEACH: the pain-therapies pointer (six tries;
      best High 38 and Medium 20 over its second sentence).

No card asks for his experience (lesson somatic-2026-11-27a): each asks for his version of words of mine whose tries are
spent. Each card is "approve" with an approve_label (lesson neuro-2026-11-27f).

  python3 articles/somatic-therapies/experiments/additions-20261126/build_cards_c1127.py
"""
import datetime
import hashlib
import importlib
import json
import os
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import suggestion_review as sr  # noqa: E402
import build_review as BR  # noqa: E402

REL = 'articles/somatic-therapies/experiments/additions-20261126/'
OUT = HERE / 'review-c1127'
RC = OUT / 'receipts'
SR = ROOT / 'tools' / 'humanization' / 'sense_receipt.py'
PG = 'https://www.pangram.com/history/'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
SECTION = {'A1': "Can't Stay With a Feeling?", 'A3': "Pain That Won't Quit?",
           'IC1': 'Re-do Trauma Memories (inner child guide)', 'IC2': 'Physical Pain? (inner child guide)'}


def L(uuid):
    return PG + uuid


def sha256(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t).strip()


def receipt(mod, name, text, part, reader, checked, placement, same):
    """A making-sense receipt for TEXT as it would read on the card (links kept), filled from the receipts module MOD of
    the draft the text was checked in (its ANN, C, Q and read records), as that module's main() fills its own."""
    RC.mkdir(parents=True, exist_ok=True)
    txt = RC / ('%s.txt' % name)
    txt.write_text(text + '\n', encoding='utf-8')
    out = RC / ('%s.receipt.json' % name)
    subprocess.run([sys.executable, str(SR), 'make', str(txt), '--section', SECTION[part], '--reader', reader, '--out',
                    str(out)], check=True, capture_output=True)
    rec = json.loads(out.read_text(encoding='utf-8'))
    ids = []
    for x in rec['sentences']:
        sid = mod.BYS[plain(x['s'])]
        ids.append(sid)
        pay, fol, link = mod.ANN[sid]
        x['payoff'], x['follows'] = pay, fol
        if 'link' in x:
            x['link'] = link
    rec['checked'] = [mod.C[c] for c in checked]
    rec['placement'] = placement
    rec['opens']['why_reading'] = mod.ANN[ids[0]][0]
    rec['same_point'] = same
    rec['needed'] = {'reader': mod.NEEDED_READS, 'unneeded': [], 'kept': {}}
    his_marked = [{'s': mod.MARKS_HIS[i], 'difference': 'see KEEP'} for i in ids if i in mod.MARKS_HIS]
    his_marked += [{'s': s, 'difference': d} for s, d in mod.MARKS_HIS_GONE]
    rec['his_fixes'] = {'reader': mod.HIS_READS, 'marked': his_marked,
                        'kept': {mod.MARKS_HIS[i]: mod.KEEP_HIS[i] for i in ids if i in mod.MARKS_HIS}}
    rec['fit'] = {'reader': mod.FIT_READS,
                  'marked': [{'s': mod.MARKS_FIT[i], 'found': 'see kept'} for i in ids if i in mod.MARKS_FIT],
                  'kept': {mod.MARKS_FIT[i]: mod.KEEP_FIT[i] for i in ids if i in mod.MARKS_FIT}}
    rec['questions'] = mod.Q[part]
    out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    res = subprocess.run([sys.executable, str(SR), 'check', str(txt), str(out)], capture_output=True, text=True)
    if res.returncode:
        raise SystemExit('receipt %s fails: %s' % (name, (res.stdout + res.stderr).strip()))
    return REL + 'review-c1127/receipts/%s.receipt.json' % name


def page(review, md, name):
    bl = sr.blocks(md, whole=True)
    probs = sr.check(review, bl)
    (OUT / ('%s.json' % name)).write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    if probs:
        for p in probs:
            print('PROBLEM', p)
        raise SystemExit(1)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    rj = REL + 'review-c1127/%s.json' % name
    r = subprocess.run([sys.executable, 'tools/humanization/suggestion_review.py', 'page', rj,
                        REL + 'review-c1127/%s.html' % name, '--artifact', REL + 'review-c1127/%s-artifact.html' % name],
                       cwd=str(ROOT), env=env, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    if r.returncode:
        raise SystemExit(r.returncode)


def cards_md(review, path, shown):
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for c in review['suggestions']:
        out += ['## %s: %s' % (c['id'], c['title']), '', '**As it would read:**', '']
        out += ['> ' + ('#' * int(i['kind'][1]) + ' ' if i['kind'] != 'p' else '') + i['text'] + '\n>'
                for i in c['inserts']]
        out[-1] = out[-1][:-2]
        out += ['', '**What it says:** %s' % c['what'], '', '**Pangram:** %s' % c['reading'], '',
                '**Every try:** %s' % c['why'], '', '**What stays:** %s' % c['stays'], '',
                '**You\'re deciding:** %s' % c['deciding'], '', '**My advice:** %s' % c['advice_note'], '']
    path.write_text('\n'.join(out) + '\n', encoding='utf-8')


def somatic():
    v23 = importlib.import_module('fill_receipts_v23')
    v21 = importlib.import_module('fill_receipts_v21')
    adds = {a['id']: a for a in json.loads((HERE / 'ADDITIONS-23.json').read_text(encoding='utf-8'))}
    a21 = {a['id']: a for a in json.loads((HERE / 'ADDITIONS-21.json').read_text(encoding='utf-8'))}
    whole = (HERE / 'WHOLE-LIVE-20261126.md').read_text(encoding='utf-8')
    md = BR.fold(whole)
    (OUT / 'ARTICLE-SOMATIC.md').write_text(md, encoding='utf-8')
    bl = sr.blocks(md, whole=True)
    A1, A3 = adds['A1'], dict(adds['A3'])
    A3['paragraphs'] = [a21['A3']['paragraphs'][0]] + list(adds['A3']['paragraphs'][1:])
    assert plain(A3['paragraphs'][0]).endswith("You also slowly go back to things you've been avoiding because of it, like going for walks.")
    assert plain(A1['paragraphs'][4]).startswith('All three keep steering you back toward your feelings,')
    rec1 = [REL + 'receipts/A1-H.receipt.json']
    place1 = ['first in the new section at the end of Layer 3: whose section it is and the first therapy',
              'second: what the first therapy watches for, and its slower version',
              'third: the second therapy, by its case', 'fourth: the third therapy, by its case',
              'last: what to ask before booking any of the three']
    for k, p in enumerate(A1['paragraphs'], 1):
        rec1.append(receipt(v23, 'A1-P%d' % k, p, 'A1', v23.A1R, ['istdp', 'apt', 'aedp'], place1[k - 1],
                            'none: read the section from its heading to the next; each paragraph says one thing once'))
    rec3 = [REL + 'receipts/A3-H.receipt.json']
    place3 = ['first in the new branch after Layer 5: whose pain it is for and the first therapy',
              'second: the first therapy\'s trial, its limit first', 'third: the second therapy, by its case',
              'fourth: the second therapy\'s trial', 'last: how to choose between the two']
    for k, p in enumerate(A3['paragraphs'], 1):
        rec3.append(receipt(v21, 'A3-P%d' % k, p, 'A3', v21.A3R, ['prt', 'real', 'eaet', 'none', 'scope'],
                            place3[k - 1], 'none: read the section from its heading to the next; each point is said once'))
    cards = []
    for a, cid in ((A1, 'A1-TEACH'), (A3, 'A3-TEACH')):
        before = next(b['i'] for b in bl if b['level'] and b['text'] == a['before_heading'])
        ins = [{'before': before, 'kind': 'h%d' % a['level'], 'text': a['heading'], 'seq': 0}]
        ins += [{'before': before, 'kind': 'p', 'text': p, 'seq': k + 1} for k, p in enumerate(a['paragraphs'])]
        cards.append((cid, ins, before))
    (i1, ins1, b1), (i3, ins3, b3) = cards
    a1 = {
        'id': i1, 'type': 'teach', 'advice': 'approve', 'approve_label': 'add it with my best tries anyway',
        'title': 'Can\'t Stay With a Feeling?: its first paragraph and its booking paragraph, six tries each, below High',
        'inserts': ins1, 'card_after': b1 - 1,
        'what': ('The new section as it stands, every paragraph checked by itself. Three read Human High: the anxiety '
                 'paragraph, Affect Phobia Therapy and AEDP. Two are my best of six tries each: the first paragraph (who '
                 'the section is for, and the therapy built for it), which reads AI, and the booking paragraph (what to '
                 'ask before booking), which reads Human, Low confidence.'),
        'why': ('The first paragraph, my six tries: [AI 100%%](%s), [AI 98%%](%s), [AI 97%%](%s), [AI 91%%, my best](%s), '
                '[AI 100%%](%s), and joined into the anxiety paragraph, [AI 100%%](%s), which pulled that paragraph (Human '
                'High by itself) to AI too. Three tell panels of fresh readers agreed every version reads as a pitch: a '
                'problem, then a named therapy.\n'
                'The booking paragraph, my six tries: [AI 100%%](%s), [Human Low, my best](%s), [AI](%s) ("hear me out" for '
                '"listen"), [Human Low again](%s) (the question in quotes, so its "you" is plainly the therapist), [22%% AI]'
                '(%s) ("slow down and listen"), [AI 100%%](%s) ("the feelings you\'d rather slip away from").\n'
                'I can\'t find more AI tells in either... can you help show me the tells I\'m missing?'
                % (L('d24b51d4-8c68-4f97-8939-ce63f875dc7d'), L('74534b8e-f7aa-4643-b630-5534b7f06bcb'),
                   L('4e4d68a4-4cff-491a-aae3-74c536c89085'), L('6e616723-4be9-418f-b508-0ae4f56f3bca'),
                   L('5aab852f-baa0-4dad-b37d-f1d067240168'), L('29ce9a61-6a1b-46e9-b1e3-3728ddb3a24a'),
                   L('cd740f96-dc28-4ef9-ac3d-dc4d062797b4'), L('7de1f32a-42f2-469c-9184-a2e9fa8ddc81'),
                   L('1c5a69f4-f539-4e30-9974-074a6c965e49'), L('ef39ee2f-d0d5-4cf2-9a26-b2b2726e57de'),
                   L('1fedeee1-2aa0-4b34-832a-1810189b1075'), L('85130339-9f9d-4032-a991-0f099d2cefff'))),
        'reading': ('My best first paragraph: [AI 91%%, two Low windows](%s). My best booking paragraph: [Human Written, 0%% '
                    'AI, one Low window](%s).' % (L('6e616723-4be9-418f-b508-0ae4f56f3bca'),
                                                   L('ef39ee2f-d0d5-4cf2-9a26-b2b2726e57de'))),
        'tested': ('Each paragraph by itself: the first [AI 91%%](%s); the anxiety paragraph [Human High](%s); Affect Phobia '
                   'Therapy, checked with the paragraph after it as it is under 50 words, [Human High over it](%s); AEDP '
                   '[Human High](%s); the booking paragraph [Human Low](%s).'
                   % (L('6e616723-4be9-418f-b508-0ae4f56f3bca'), L('63dc89df-a178-4ad6-94ea-0c9865645849'),
                      L('b4f0fea6-06e1-4076-a6a6-a0589c7d82e1'), L('da780877-d112-467b-93fc-fc02004fbc76'),
                      L('ef39ee2f-d0d5-4cf2-9a26-b2b2726e57de'))),
        'stays': ('Every paragraph of the guide as it is live. The anxiety, Affect Phobia Therapy and AEDP paragraphs as they '
                  'read here (Human High), and what the section says: whom each therapy is for, and the two questions to '
                  'ask before booking.'),
        'deciding': ('Your version of the first paragraph and of the booking paragraph (Revise), or the section with my best '
                     'tries as they read, or holding the section until both read High.'),
        'advice_note': ('Revise with your version of those two paragraphs if you can: the first says who the section is for '
                        '(someone who can feel their body by now but slips away from a feeling in a session, by explaining '
                        'it or agreeing with the therapist) and names Intensive Short-Term Dynamic Psychotherapy; the booking '
                        'paragraph asks what a therapist does if you get overwhelmed, or if they say you\'re dodging a '
                        'feeling and you don\'t think you are. If not, I\'d hold the section (Reject) rather than put in a '
                        'paragraph that reads AI.'),
        'ask_because': ('downside: the section can\'t go in while its first paragraph reads AI, and my tries for both '
                        'paragraphs are spent (six each)'),
        'found_by': ('The checks in your Pangram account, 26 and 27 November; tell panels of fresh Sonnet, Haiku and Fable '
                     'readers on the first paragraph (three) and the booking paragraph (one); fresh reads of every version '
                     'against the ways you fix sentences, for need, fit and contradictions'),
        'receipt': rec1}
    a3 = {
        'id': i3, 'type': 'teach', 'advice': 'approve', 'approve_label': 'add it with my best try anyway',
        'title': 'Pain That Won\'t Quit?: its first paragraph reads High but for its last sentence (Medium)',
        'inserts': ins3, 'card_after': b3 - 1,
        'what': ('The new branch as it stands. Its first paragraph (whose pain it is for, and the first therapy) reads Human '
                 'High over its first 88 words and Medium over its last sentence; the other four read Human High by '
                 'themselves. Two changes of meaning from the version you approved on the first page: the false alarm is '
                 'now "your brain is making real pain, signaling danger where the doctors haven\'t found any injury", and '
                 '"two therapies are worth knowing about" is now "there are two therapies I\'d look into".'),
        'why': ('The first paragraph, checked with the paragraph after it until the two were joined: [Human, Medium over the '
                'hook](%s), [Human, Medium](%s), [Human, Medium](%s), [AI 100%%](%s) (the hook joined in), [42%% AI](%s) (the '
                'hook cut), then as one paragraph with the tell panel\'s fixes, [High 88, Medium 18, my best](%s), and "the '
                'pain" for "it" in the last sentence, [High 88, Medium 19](%s).\n'
                'My next try joins the last sentence to the one before ("..., without being scared of it, and by slowly '
                'going back to things you\'ve been avoiding because of the pain, like going for walks"), which a fresh '
                'reader passed; the check rules hold it until the branch\'s own check has taken two small steps from its '
                'older near miss, so it waits for your answer here.\n'
                'I can\'t find more AI tells in that last sentence ("You also slowly go back to things you\'ve been avoiding '
                'because of it, like going for walks.")... can you help show me the tells I\'m missing?'
                % (L('06b001d4-8c68-4f97-8939-ce63f875dc7d'.replace('8c68-4f97-8939-ce63f875dc7d', '8d15-4c82-9343-9c99800cf2eb')),
                   L('c805f2d9-ab93-44cc-9b8a-019adcb7517a'), L('0615933a-a6eb-4722-8e6b-8222bfea1f27'),
                   L('dea167f3-c362-46f5-9c67-732ae95c05cd'), L('96db84be-5b7f-48c7-a362-390f75757f59'),
                   L('382a6e6b-372e-4f94-a8ec-a454d44492c0'), L('710b14c4-7fae-4337-9e91-ad39b3168cc1'))),
        'reading': ('My best first paragraph: [Human Written, 0%% AI, High over 88 words, Medium over the last 18](%s).'
                    % L('382a6e6b-372e-4f94-a8ec-a454d44492c0')),
        'tested': ('Each paragraph by itself: the first [High 88, Medium 18](%s); the first therapy\'s trial [Human High](%s); '
                   'the second therapy [Human High](%s); its trial [Human High](%s); how to choose [Human High](%s).'
                   % (L('382a6e6b-372e-4f94-a8ec-a454d44492c0'), L('1f690117-8ab6-47c9-beaf-2e9eaa4ea8c3'),
                      L('625ebf0c-6a40-42f5-8429-a9f8feffdbbc'), L('76768c4b-1a89-46e8-b37d-befaf314177b'),
                      L('0320a0bc-3f6d-4eb1-80c2-5d8b7639c6e9'))),
        'stays': ('Every paragraph of the guide as it is live; the branch\'s other four paragraphs as they read here (Human '
                  'High), with both trials\' numbers and their limits.'),
        'deciding': ('Your version of the first paragraph\'s last sentence (Revise), or the branch with my best try as it '
                     'reads (one Medium sentence), or holding it until it reads High; and whether the two changes of meaning '
                     'above say it right.'),
        'advice_note': ('Revise with your version of the last sentence if you can (it says you also slowly go back to things '
                        'the pain made you avoid, like walks); the rest can stay as it is. If not, Approve and I\'ll check '
                        'my join as the branch\'s next try before it goes in.'),
        'ask_because': ('downside: one sentence of the branch reads Medium, and the first paragraph\'s tries are spent '
                        '(seven, the last one no better than the one before)'),
        'found_by': ('The checks in your Pangram account, 26 and 27 November; a tell panel of fresh Sonnet, Haiku and Fable '
                     'readers on the first paragraph; fresh reads of every version against the ways you fix sentences, for '
                     'need, fit and contradictions'),
        'receipt': rec3}
    review = {
        'format': sr.FORMAT,
        'review_id': 'somatic-additions-cards-20261127',
        'title': 'Somatic Guide, 27 November: two new sections for you to teach me',
        'intro': [('Your somatic guide as it is live (26 November), with the two new sections whose last paragraphs my '
                   'tries couldn\'t get to Human High, each where it would go. Nothing here is in the post yet; the '
                   'Imagery Rescripting section (your version) reads Human High and waits for these.'),
                  ('Two cards. Revise opens the section for your version of the paragraphs the card names. Every claim is '
                   'the same as on the first page; the two changes of meaning are named on the cards.')],
        'git_file': REL + 'review-c1127/REVIEW-SOMATIC.html',
        'article': {'file': REL + 'review-c1127/ARTICLE-SOMATIC.md', 'sha256': sha256(md)},
        'whole': {'file': REL + 'WHOLE-LIVE-20261126.md', 'sha256': sha256(whole)},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://somatic.u-dont-exist.com', 'guide_label': 'your live post',
                  'review': BLOB + REL + 'review-c1127/CARDS-SOMATIC.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A new section whose Pangram tries are spent below High for one or two paragraphs: '
                                     'my best tested version, what each try read, and room for yours.'}},
        'suggestions': [a1, a3]}
    page(review, md, 'REVIEW-SOMATIC')
    cards_md(review, OUT / 'CARDS-SOMATIC.md', md)


def fold_show(md, show):
    """MD with CUT lines around each long stretch outside SHOW ([start heading, end heading], both shown), as
    build_review.fold does for the somatic guide."""
    raw = BR.raw_blocks(md)
    heads = [BR.head_text(b) for b in raw]
    shown = [False] * len(raw)
    for start, end in show:
        a = heads.index(start)
        z = heads.index(end, a) + 1
        for k in range(a, z):
            shown[k] = True
    out, run = [], []

    def flush():
        paras = [b for b in run if not BR.head_text(b) and not b.strip().startswith('<!--')]
        words = sum(len(re.sub(r'\]\([^)]*\)', ']', b).split()) for b in paras)
        if len(paras) >= sr.CUT_MIN_BLOCKS and words >= sr.CUT_MIN_WORDS:
            out.extend(['<!-- CUT -->'] + run + ['<!-- /CUT -->'])
        else:
            out.extend(run)
        run.clear()

    for k, b in enumerate(raw):
        if shown[k]:
            flush()
            out.append(b)
        else:
            run.append(b)
    flush()
    return '\n\n'.join(out) + '\n'


def inner():
    v19 = importlib.import_module('fill_receipts_v19')
    ic = json.loads((HERE / 'INNER-CHILD-ADDS-9.json').read_text(encoding='utf-8'))
    whole = (HERE / 'IC-WHOLE-LIVE-20261127.md').read_text(encoding='utf-8')
    md = fold_show(whole, [('Re-do Trauma Memories', 'Discipline Done Right?'), ('Physical Pain?', 'Compassionate Exit?')])
    (OUT / 'ARTICLE-INNER.md').write_text(md, encoding='utf-8')
    bl = sr.blocks(md, whole=True)
    j_i = next(b['i'] for b in bl if b['level'] and b['text'] == 'Discipline Done Right?') - 1
    h_i = next(b['i'] for b in bl if b['level'] and b['text'] == 'Compassionate Exit?') - 1
    assert 'it might take years to imagine that correction' in ' '.join(b['text'] for b in bl[j_i - 2:j_i + 1]), bl[j_i]['text'][:80]
    assert 'be the end of the investigation' in bl[h_i]['text'], bl[h_i]['text'][:80]
    r1 = receipt(v19, 'IC1', ic['IC1']['add'], 'IC1', v19.ICR1, ['imrs'],
                 'a paragraph of its own at the end of Re-do Trauma Memories, after his J. paragraph and its picture',
                 'none: read the section from its heading to the next; no other paragraph names a clinical therapy')
    r2 = receipt(v19, 'IC2', ic['IC2']['add'], 'IC2', v19.ICR2, ['real', 'prt', 'eaet'],
                 'a paragraph of its own at the end of Physical Pain?, after his advice not to stop the investigation',
                 'none: read the section from its heading to the next; no other paragraph names these therapies')
    c1 = {
        'id': 'IC1', 'type': 'addition', 'advice': 'approve', 'approve_label': 'add it',
        'title': 'Re-do Trauma Memories: a pointer to Imagery Rescripting',
        'inserts': [{'before': j_i + 1, 'kind': 'p', 'text': ic['IC1']['add'], 'seq': 0}], 'card_after': j_i,
        'what': ('A paragraph of its own at the end of the section, after your J. example: for a memory too big to redo on '
                 'your own, Imagery Rescripting, linked to its new section in your somatic guide, and what the therapist '
                 'does in it. Its aside "which I only found out about after I wrote this section" is your line from the '
                 'Imagery Rescripting section you wrote for the somatic guide.'),
        'why': ('It reads [Human Written, 0%% AI, one High window](%s) by itself, after three tries with a Medium second '
                'sentence ([1](%s), [2](%s), [3](%s)); your aside carried it.'
                % (L('cfb9154d-4b26-4e87-ad84-b4112676c8f0'), L('9af27523-3ac6-452d-aa8f-b08441054702'),
                   L('e2f5b150-fe52-40ff-8109-61804c63bd87'), L('6f326772-9c3d-478f-99fc-d5949125b7ce'))),
        'reading': '[Human Written, 0%% AI, one High window](%s).' % L('cfb9154d-4b26-4e87-ad84-b4112676c8f0'),
        'tested': 'By itself: [Human High, 56 words](%s).' % L('cfb9154d-4b26-4e87-ad84-b4112676c8f0'),
        'stays': 'Every paragraph of the section, your J. example included.',
        'deciding': 'Whether the section points to the somatic guide\'s Imagery Rescripting here, with your aside in it.',
        'advice_note': 'I\'d add it: it reads Human High, and it goes in with the somatic guide\'s new sections.',
        'ask_because': 'meaning: it adds a paragraph with your own line in it to your inner child guide',
        'whose': ('his own: the aside "which I only found out about after I wrote this section", from his version of the '
                  'somatic guide\'s Imagery Rescripting section (his answers of 27 November); the rest of the paragraph is mine'),
        'found_by': 'Fresh reads against the ways you fix sentences, for need, fit and contradictions; the checks in your Pangram account',
        'receipt': [r1]}
    c2 = {
        'id': 'IC2-TEACH', 'type': 'teach', 'advice': 'approve', 'approve_label': 'add my best try anyway',
        'title': 'Physical Pain?: a pointer to the two pain therapies, six tries, its second sentence Medium',
        'inserts': [{'before': h_i + 1, 'kind': 'p', 'text': ic['IC2']['add'], 'seq': 0}], 'card_after': h_i,
        'what': ('A paragraph of its own at the end of the section, after your advice not to stop the investigation: what '
                 'to try meanwhile, the two pain therapies in your somatic guide (linked), and why they\'re worth it. Its '
                 'first sentence reads Human High; the second ("They both treat the pain as real, and they\'ve helped '
                 'people with long-lasting back, muscle and joint pain."), Medium.'),
        'why': ('My tries, after two earlier forms that read [AI](%s) and [52%% AI](%s): [AI](%s), [High 38, Medium 20, my '
                'best](%s), then each a change to the second sentence: "in their trials most people ... got better" [High 38, '
                'Low 23](%s); "see the pain as real" [High 38, Low 20](%s); "between them" [37%% AI](%s); and, after a tell '
                'panel that agreed the reassurance reads as a stock phrase, your word "imaginary" ("Neither one sees the pain '
                'as imaginary") [AI 90%%](%s), which pulled the first sentence down too.\n'
                'I can\'t find more AI tells in the second sentence. The one human tell I can name is in the first: "I go '
                'into in my somatic guide", where a model smooths the doubled preposition ("that I cover in my somatic '
                'guide")... can you help show me the tells I\'m missing?'
                % (L('c4b90cd8-2adc-4d39-973b-ae905bb7cd91'), L('acb8fc15-87b0-4e5f-a784-1d12c54bf18f'),
                   L('e267be27-30ce-4593-9f9a-dae0e261e553'), L('0f422892-5de8-43b0-8cb2-bfe4b5045d27'),
                   L('24c2a0ba-a6c0-47f0-91a9-92d7055797a6'), L('17eec1c6-00cc-485f-ac1c-ebf21725e259'),
                   L('af0a6004-2934-4510-89ce-1d546552b28e'), L('866e6d04-dc99-464b-b787-d537cb8d8926'))),
        'reading': '[Human Written, 0%% AI, High over 38 words, Medium over the last 20](%s).' % L('0f422892-5de8-43b0-8cb2-bfe4b5045d27'),
        'tested': 'By itself: [High 38, Medium 20](%s).' % L('0f422892-5de8-43b0-8cb2-bfe4b5045d27'),
        'stays': 'Every paragraph of the section, your advice to keep investigating included; the first sentence as it reads (High).',
        'deciding': 'Your version of the second sentence (Revise), or my best as it reads (one Medium sentence), or holding it until it reads High.',
        'advice_note': ('Revise with your version of the second sentence if you can: it says why the two are worth trying '
                        '(neither treats the pain as imaginary, and they\'ve helped people with pain like this). If not, '
                        'Approve and it goes in with its Medium sentence, or Reject and it waits.'),
        'ask_because': 'downside: one sentence reads Medium, and my tries are spent (six)',
        'found_by': ('The checks in your Pangram account, 26 and 27 November; a tell panel of fresh Sonnet, Haiku and Fable '
                     'readers; fresh reads of every version against the ways you fix sentences, for need, fit and contradictions'),
        'receipt': [r2]}
    review = {
        'format': sr.FORMAT,
        'review_id': 'inner-child-pointers-cards-20261127',
        'title': 'Inner Child Guide, 27 November: two pointers to the somatic guide\'s new sections',
        'intro': [('Your inner child guide as it is live today (27 November), with the two pointers to the somatic '
                   'guide\'s new sections, each where it would go: the end of Re-do Trauma Memories and the end of Physical '
                   'Pain?. Long stretches with no card fold into a box that opens. Nothing here is in the post yet.'),
                  ('Two cards: Imagery Rescripting (Human High) for your eye, and the pain therapies, whose second sentence '
                   'my tries couldn\'t get above Medium, for your version.')],
        'git_file': REL + 'review-c1127/REVIEW-INNER.html',
        'article': {'file': REL + 'review-c1127/ARTICLE-INNER.md', 'sha256': sha256(md)},
        'whole': {'file': REL + 'IC-WHOLE-LIVE-20261127.md', 'sha256': sha256(whole)},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/i/189761959/re-do-trauma-memories', 'guide_label': 'your live post',
                  'review': BLOB + REL + 'review-c1127/CARDS-INNER.md'},
        'types': {'addition': {'label': 'New paragraph', 'about': 'A paragraph the guide doesn\'t have yet, shown where it would go.'},
                  'teach': {'label': 'For you to teach me',
                            'about': 'A paragraph whose Pangram tries are spent below High: my best tested version, what '
                                     'each try read, and room for yours.'}},
        'suggestions': [c1, c2]}
    page(review, md, 'REVIEW-INNER')
    cards_md(review, OUT / 'CARDS-INNER.md', md)


def main():
    OUT.mkdir(exist_ok=True)
    somatic()
    inner()
    print('ok')
    return 0


if __name__ == '__main__':
    sys.exit(main())
