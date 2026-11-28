#!/usr/bin/env python3
"""build_cards_c1128.py - two cards for the somatic guide (turn of 2026-11-28 09:44 UTC): the two slips the word-for-sense
read before A1 went in found in text that went live on 27 November (sense-c1128/). Both are his versions of my drafts, so
the fixes are mine to make and test (gate E373); Pangram couldn't check them (the account's monthly credits ran out at
10:09 UTC), so whether they go in untested is a downside for him to weigh. The guide as it is live
(apply-c1128/LIVE-SOMATIC-20261128.md), long stretches folded.

  python3 articles/somatic-therapies/experiments/additions-20261126/build_cards_c1128.py
"""
import datetime
import hashlib
import json
import os
import pathlib
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
OUT = HERE / 'review-c1128'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
NOCREDIT = ('Pangram couldn\'t check it: the account\'s monthly credits ran out at 10:09 UTC this morning ("You have used all '
            'your AI detection credits for this month. Your monthly credits will refill in 22 days.").')
READS = ('The word-for-sense read before A1 went in found it (one fresh reader of the five new texts, three planted errors, '
         'all three found: [its findings](%s)); a second fresh reader marked nothing in the fix ([the read](%s)).'
         % (BLOB + REL + 'sense-c1128/out/FINDINGS-RAW.json', BLOB + REL + 'sense-c1128/READ-SR.md'))


def sha256(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    whole = (HERE / 'apply-c1128' / 'LIVE-SOMATIC-20261128.md').read_text(encoding='utf-8')
    md = BR.fold(whole)
    (OUT / 'ARTICLE-SOMATIC.md').write_text(md, encoding='utf-8')
    bl = sr.blocks(md, whole=True)
    cards = []
    for key, old, title, span_words, what, advice, label in (
            ('SR-A2', "Instead of EMDR's mechanical approach. The Imagery Rescripting therapist",
             'Imagery Rescripting: a sentence fragment, joined with a comma', "approach. The",
             ('"Instead of EMDR\'s mechanical approach." stands as a sentence of its own. A comma joins it to the sentence '
              'it introduces: "Instead of EMDR\'s mechanical approach, the Imagery Rescripting therapist is there with you as '
              'you explain the scene ...". The live fragment could also belong to the sentence before it; both readings say '
              'the same thing, and the fix takes the forward one.'),
             ('I\'d fix it now: a comma for the full stop joins two halves of one thought, and nothing else in the paragraph '
              'changes. If you\'d rather it waits for a check, Reject and it waits.'), 'fix it now, unchecked'),
            ('SR-A3', "I'd start with the second, and otherwise with the first.",
             'Pain That Won\'t Quit?: "the second" and "the first" named', 'the second, and otherwise with the first',
             ('"I\'d start with the second, and otherwise with the first" comes right after "I haven\'t found a trial '
              'comparing EAET with PRT", so a reader can take "the second" as PRT, the opposite of what the section means '
              '(EAET is the one for pain tied to stress or the people in your life). The fix names them, with the short '
              'forms your version gives each where it is named: "I\'d start with EAET, and otherwise with PRT."'),
             ('I\'d fix it now: as it reads, a reader can come away with the advice reversed. If you\'d rather it waits for '
              'a check, Reject and it waits.'), 'fix it now, unchecked')):
        i = next(b['i'] for b in bl if old in b['text'])
        before = bl[i]['text']
        fixed = (HERE / 'sense-c1128' / 'fixes' / ('%s.md' % key)).read_text(encoding='utf-8').strip()
        start = before.index(span_words)
        cards.append({
            'id': key, 'type': 'sense', 'advice': 'approve', 'approve_label': label, 'title': title,
            'spans': [{'block': i, 'start': start, 'end': start + len(span_words)}],
            'edits': [{'block': i, 'before': before, 'after': fixed}],
            'what': what, 'why': READS + ' ' + NOCREDIT,
            'stays': 'Every other word of the paragraph and of the section.',
            'deciding': 'Whether the fix goes in now, before Pangram can check it, or waits for a check.',
            'advice_note': advice,
            'ask_because': ('downside: it changes a live paragraph of the section that read Human High, without a Pangram '
                            'check (the credits are out until they refill)'),
            'found_by': 'The word-for-sense read of 28 November and a fresh reader of the fix',
            'receipt': [REL + 'sense-c1128/fixes/%s-linked.receipt.json' % key]})
    review = {
        'format': sr.FORMAT, 'review_id': 'somatic-sense-cards-20261128',
        'title': 'Somatic Guide, 28 November: two slips in the new sections',
        'intro': [('Your somatic guide as it is live this morning (Can\'t Stay With a Feeling? went in at 09:49 UTC), with '
                   'two small fixes in the sections that went live yesterday, each where it applies. Long stretches with no '
                   'card fold into a box that opens. Nothing here is in the post yet.'),
                  ('Two cards. Pangram can\'t check them until the account\'s credits refill, so each asks whether the fix '
                   'goes in now or waits.')],
        'git_file': REL + 'review-c1128/REVIEW-SENSE.html',
        'article': {'file': REL + 'review-c1128/ARTICLE-SOMATIC.md', 'sha256': sha256(md)},
        'whole': {'file': REL + 'apply-c1128/LIVE-SOMATIC-20261128.md', 'sha256': sha256(whole)},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/somatic-modalities-strategic-sequencing',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'review-c1128/CARDS-SENSE.md'},
        'types': {'sense': {'label': 'Reads wrong', 'about': 'Words that a reader can misread or trip on, with the smallest '
                                                             'fix.'}},
        'suggestions': cards}
    probs = sr.check(review, bl)
    (OUT / 'REVIEW-SENSE.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    if probs:
        for p in probs:
            print('PROBLEM', p)
        return 1
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    r = subprocess.run([sys.executable, 'tools/humanization/suggestion_review.py', 'page', REL + 'review-c1128/REVIEW-SENSE.json',
                        REL + 'review-c1128/REVIEW-SENSE.html', '--artifact', REL + 'review-c1128/REVIEW-SENSE-artifact.html'],
                       cwd=str(ROOT), env=env, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for c in cards:
        out += ['## %s: %s' % (c['id'], c['title']), '', '**As it reads now:**', '', '> ' + c['edits'][0]['before'], '',
                '**As it would read:**', '', '> ' + c['edits'][0]['after'], '', '**What changes:** %s' % c['what'], '',
                '**Why:** %s' % c['why'], '', '**You\'re deciding:** %s' % c['deciding'], '',
                '**My advice:** %s' % c['advice_note'], '']
    (OUT / 'CARDS-SENSE.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok')
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
