#!/usr/bin/env python3
"""build_cards_c1127b.py - the teaching card of 2026-11-27 (turn of 22:26 UTC) for the last new section of the somatic
additions, "Can't Stay With a Feeling?" (A1), whose section checks are spent with two windows below High.

His answers of 22:19 UTC gave his versions of A1's first and booking paragraphs; with them in, the section read 24% AI, and
his lessons of this turn, applied to my AEDP paragraph one check at a time, took it to Human Written, 0% AI, with two Medium
windows (draft 29): one over his "The ISTDP therapist catches you ...", one over the AEDP paragraph's last two sentences with
his "All three keep steering you back ...". My one guess at those two (the short forms in brackets where each therapy is
named, draft 30) read worse. The card shows draft 29 in place, in the guide as it is live since 22:45 UTC
(apply-c1127/LIVE-SOMATIC-20261127.md), with every check and room for his version (Revise). "approve" with an approve_label
(lesson neuro-2026-11-27f); it asks for no experience of his (lesson somatic-2026-11-27a).

  python3 articles/somatic-therapies/experiments/additions-20261126/build_cards_c1127b.py
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
OUT = HERE / 'review-c1127b'
RC = OUT / 'receipts'
SR = ROOT / 'tools' / 'humanization' / 'sense_receipt.py'
PG = 'https://www.pangram.com/history/'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
SECTION = "Can't Stay With a Feeling?"


def L(uuid):
    return PG + uuid


def sha256(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t).strip()


def receipt(mod, name, text, reader, checked, placement, same, his=None):
    """A making-sense receipt for TEXT as it would read on the card (links kept), filled from draft 29's receipts module
    MOD (its ANN, C, Q and read records), as build_cards_c1127.receipt fills the first page's; HIS (his paragraph) maps
    each of his sentences to the sentence that carries it (lesson bad-trips-2026-11-27k)."""
    RC.mkdir(parents=True, exist_ok=True)
    txt = RC / ('%s.txt' % name)
    txt.write_text(text + '\n', encoding='utf-8')
    out = RC / ('%s.receipt.json' % name)
    subprocess.run([sys.executable, str(SR), 'make', str(txt), '--section', SECTION, '--reader', reader, '--out',
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
    rec['needed'] = {'reader': mod.NEEDED_READS.replace('READ-26.md to READ-29.md', 'READ-26.md to READ-30.md'),
                     'unneeded': [], 'kept': {}}
    his_marked = [{'s': mod.MARKS_HIS[i], 'difference': 'see KEEP'} for i in ids if i in mod.MARKS_HIS]
    rec['his_fixes'] = {'reader': mod.HIS_READS.replace('READ-26.md to READ-29.md', 'READ-26.md to READ-30.md'),
                        'marked': his_marked, 'kept': {mod.MARKS_HIS[i]: mod.KEEP_HIS[i] for i in ids if i in mod.MARKS_HIS}}
    rec['fit'] = {'reader': mod.FIT_READS.replace('READ-26.md to READ-29.md', 'READ-26.md to READ-30.md'),
                  'marked': [{'s': mod.MARKS_FIT[i], 'found': 'see kept'} for i in ids if i in mod.MARKS_FIT],
                  'kept': {mod.MARKS_FIT[i]: mod.KEEP_FIT[i] for i in ids if i in mod.MARKS_FIT}}
    rec['questions'] = mod.Q['A1']
    # his paragraphs as he sent them (plain text, from his Pangram history): each sentence of his is the claim, carried
    # by the same sentence here with its link put back
    rec['his_answer'] = [{'said': plain(x['s']), 'in': x['s']} for x in rec['sentences']] if his else []
    out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    res = subprocess.run([sys.executable, str(SR), 'check', str(txt), str(out)], capture_output=True, text=True)
    if res.returncode:
        raise SystemExit('receipt %s fails: %s' % (name, (res.stdout + res.stderr).strip()))
    return REL + 'review-c1127b/receipts/%s.receipt.json' % name


def page(review, md, name):
    bl = sr.blocks(md, whole=True)
    probs = sr.check(review, bl)
    (OUT / ('%s.json' % name)).write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    if probs:
        for p in probs:
            print('PROBLEM', p)
        raise SystemExit(1)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    rj = REL + 'review-c1127b/%s.json' % name
    r = subprocess.run([sys.executable, 'tools/humanization/suggestion_review.py', 'page', rj,
                        REL + 'review-c1127b/%s.html' % name, '--artifact', REL + 'review-c1127b/%s-artifact.html' % name],
                       cwd=str(ROOT), env=env, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    if r.returncode:
        raise SystemExit(r.returncode)


def cards_md(review, path):
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


def main():
    OUT.mkdir(exist_ok=True)
    v29 = importlib.import_module('fill_receipts_v29')
    A1 = {a['id']: a for a in json.loads((HERE / 'ADDITIONS-29.json').read_text(encoding='utf-8'))}['A1']
    whole = (HERE / 'apply-c1127' / 'LIVE-SOMATIC-20261127.md').read_text(encoding='utf-8')
    md = BR.fold(whole)
    (OUT / 'ARTICLE-SOMATIC.md').write_text(md, encoding='utf-8')
    bl = sr.blocks(md, whole=True)
    assert [plain(p) for p in A1['paragraphs']] == [v29.PARAS['A1-P%d' % k] for k in range(1, 6)]
    his = {1: True, 5: True}
    place = ['first in the new section at the end of Layer 3: whose section it is and the first therapy (his, as he sent it)',
             'second: what the first therapy watches for, and its slower version',
             'third: the second therapy, by its case', 'fourth: the third therapy, by its case',
             'last: what to ask before booking any of the three (his, as he sent it)']
    recs = [REL + 'receipts/A1-H.receipt.json']
    for k, p in enumerate(A1['paragraphs'], 1):
        recs.append(receipt(v29, 'A1-P%d' % k, p, v29.A1R, ['istdp', 'apt', 'aedp'], place[k - 1],
                            'none: read the section from its heading to the next; each paragraph says one thing once',
                            his.get(k)))
    before = next(b['i'] for b in bl if b['level'] and b['text'] == A1['before_heading'])
    ins = [{'before': before, 'kind': 'h%d' % A1['level'], 'text': A1['heading'], 'seq': 0}]
    ins += [{'before': before, 'kind': 'p', 'text': p, 'seq': k + 1} for k, p in enumerate(A1['paragraphs'])]
    card = {
        'id': 'A1-TEACH-2', 'type': 'teach', 'advice': 'approve', 'approve_label': 'add it as it reads',
        'title': 'Can\'t Stay With a Feeling?: with your two paragraphs in, Human 0% AI, two windows Medium',
        'inserts': ins, 'card_after': before - 1,
        'what': ('The section as it would go in: your first and booking paragraphs word for word as you sent them, and my '
                 'three between them. The AEDP paragraph changed after your answers, by your lessons of this turn, one '
                 'check at a time: "The AEDP therapist" for "The therapist" (whose therapist, as in your first paragraph); '
                 'the "and" between the therapist\'s two acts taken out, so they are two sentences; what the therapist '
                 'does ("stays with you through whatever comes up") in place of what they work at ("works to keep you from '
                 'feeling alone with whatever comes up"), a small change of meaning, from their aim to their act; and '
                 '"kindness", the paragraph\'s own word for what you can\'t let in, for "care". Every other claim is the '
                 'same as on the first page.'),
        'why': ('With your two paragraphs in and mine as on the first page, the section read [24%% AI](%s). Then your lessons '
                'on my AEDP paragraph, one check after each fix: whose therapist and the "and" taken out, [17%% AI](%s); '
                'what the therapist does in place of their aim, [Human Written, one Low window](%s); "kindness" for "care", '
                '[Human Written, two Low windows](%s); the repeat cut ("so you\'re not alone with it" after "stays with '
                'you"), [Human Written, 0%% AI, no window below Medium, my best](%s).\n'
                'Then my one guess at the two Medium windows: each started on a short form the text hadn\'t given ("The '
                'ISTDP therapist", "The AEDP therapist"), so I gave each in brackets where its therapy is named, the way '
                'you did with (PRT) and (EAET). A fresh reader said a reader needs them, but the section read worse: '
                '[Human Written, three Medium windows and one Low](%s), so they\'re not in the version above.\n'
                'The Medium window over your "The ISTDP therapist catches you ..." holds in every check since your '
                'paragraph went in, though your paragraph read High by itself; I can\'t find more AI tells in it or in my '
                'AEDP paragraph\'s end... can you help show me the tells I\'m missing?'
                % (L('79b83fb1-6ec3-4eb8-9a64-0e2e66992e8e'), L('6abb3f4b-54ab-41e5-8b4f-4e9c660a244b'),
                   L('bd7b5cbd-12b7-4a4b-99f3-693d4c9e2eba'), L('17413390-d21e-4635-a786-e9044baa03ed'),
                   L('089bbeb6-7fe6-4961-b18f-7d54fd474d5b'), L('c8b1288c-3c7f-4921-a4f2-af8b472edc62'))),
        'reading': ('[Human Written, 0%% AI: High 47, Medium 19, High 143, Medium 49, High 55](%s): the first Medium window is '
                    'your "The ISTDP therapist catches you each time they notice you slipping, and asks what you\'re feeling '
                    'right then."; the second is the AEDP paragraph\'s last two sentences with your "All three keep '
                    'steering you back toward your feelings, which can get to be too intense sometimes."'
                    % L('089bbeb6-7fe6-4961-b18f-7d54fd474d5b')),
        'tested': ('The section as above: [Human Written, 0%% AI, two Medium windows](%s). Each paragraph by itself: your '
                   'first [Human High](%s); the anxiety paragraph [Human High](%s); Affect Phobia Therapy, checked with the '
                   'AEDP paragraph as it was on the first page, [Human High](%s); that AEDP paragraph [Human High](%s), the '
                   'version here only in the section; your booking paragraph [Human High](%s).'
                   % (L('089bbeb6-7fe6-4961-b18f-7d54fd474d5b'), L('94d585ca-53e5-434a-84f9-8546e789bcc0'),
                      L('63dc89df-a178-4ad6-94ea-0c9865645849'), L('b4f0fea6-06e1-4076-a6a6-a0589c7d82e1'),
                      L('da780877-d112-467b-93fc-fc02004fbc76'), L('598494c2-0559-4fb2-8ce8-2794d1373d9c'))),
        'stays': ('Every paragraph of the guide as it is live (Imagery Rescripting and Pain That Won\'t Quit? went in at 22:45 '
                  'UTC, with your versions); your two paragraphs word for word; what the section says: whom each therapy is '
                  'for, and the questions to ask before booking.'),
        'deciding': ('Whether the section goes in as it reads (Human, 0% AI, two Medium windows), or with your version of the '
                     'sentences under the Medium windows (Revise), or waits.'),
        'advice_note': ('Revise if you see the fix: the windows are over your "The ISTDP therapist catches you each time they '
                        'notice you slipping, and asks what you\'re feeling right then." and over the AEDP paragraph\'s "The '
                        'AEDP therapist stays with you through whatever comes up. When some of their kindness does get in, '
                        'they ask what that\'s like and where you feel it in your body." with your "All three keep steering '
                        'you back ...". If not, Approve and it goes in as it reads: Human, 0% AI, nothing below Medium.'),
        'ask_because': ('downside: two windows read Medium, one over your own sentence, and my section checks are spent '
                        '(seven, the last one worse than the one before)'),
        'found_by': ('The checks in your Pangram account, 27 November; fresh Fable readers of each draft against the ways you '
                     'fix sentences, for need, fit and contradictions (READ-26 to READ-30, none marked)'),
        'receipt': recs}
    review = {
        'format': sr.FORMAT,
        'review_id': 'somatic-a1-card-20261127b',
        'title': 'Somatic Guide, 27 November (late): the last new section, for you to teach me',
        'intro': [('Your somatic guide as it is live now (Imagery Rescripting and Pain That Won\'t Quit? went in at 22:45 UTC, '
                   'with your versions), with the one new section still out, Can\'t Stay With a Feeling?, where it would go, '
                   'at the end of Layer 3. Nothing on this page is in the post yet.'),
                  ('One card. Approve puts the section in as it reads; Revise opens it for your version of the sentences '
                   'the card names.')],
        'git_file': REL + 'review-c1127b/REVIEW-A1.html',
        'article': {'file': REL + 'review-c1127b/ARTICLE-SOMATIC.md', 'sha256': sha256(md)},
        'whole': {'file': REL + 'apply-c1127/LIVE-SOMATIC-20261127.md', 'sha256': sha256(whole)},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/somatic-modalities-strategic-sequencing',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'review-c1127b/CARDS-A1.md'},
        'types': {'teach': {'label': 'For you to teach me',
                            'about': 'A new section whose Pangram tries are spent below High: my best tested version, what '
                                     'each try read, and room for yours.'}},
        'suggestions': [card]}
    page(review, md, 'REVIEW-A1')
    cards_md(review, OUT / 'CARDS-A1.md')
    print('ok')
    return 0


if __name__ == '__main__':
    sys.exit(main())
