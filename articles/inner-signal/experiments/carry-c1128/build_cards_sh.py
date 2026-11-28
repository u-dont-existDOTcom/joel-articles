#!/usr/bin/env python3
"""build_cards_sh.py - the marking page for carrying the somatic additions into the Self-Hypnosis guide (turn of
2026-11-28 09:44 UTC; his ask, 09:44 UTC: "yes i want to carry changes into self hypnhosis guide also once we're done").
The guide as it is live (LIVE-HYPNOSIS-20261128.md, fetched through his laptop), long stretches with no card folded into
boxes, and three cards, each a new paragraph where it would go:
  SH1 (Imagery Rescripting, the somatic guide's A2 and the inner child guide's IC1) at the end of "Do These With a Clinician";
  SH2 (the two pain therapies, A3 and IC2) at the end of "What It's For, and Not For";
  SH3 (the therapies for explaining feelings away, A1) at the end of "Too Analytical?".
Each is "approve" with an approve_label (lesson neuro-2026-11-27f); none asks for his experience (somatic-2026-11-27a).

  python3 articles/inner-signal/experiments/carry-c1128/build_cards_sh.py DRAFT_N RESULTS.json
"""
import datetime
import hashlib
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
sys.path.insert(0, str(ROOT / 'articles/somatic-therapies/experiments/additions-20261126'))
import suggestion_review as sr  # noqa: E402
import build_review as BR  # noqa: E402

REL = 'articles/inner-signal/experiments/carry-c1128/'
OUT = HERE / 'review'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
SHOW = [("What It's For, and Not For", 'Forget Left Brain/Right Brain'),
        ('Do These With a Clinician', 'Find a Hypnotist Who Fits'),
        ('Dissociating or Unreal?', 'Too Blissful or Diffuse?')]


def sha256(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def fold_show(md, show):
    """MD with CUT lines around each long stretch outside SHOW ([start heading, end heading], both shown)."""
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


def page(review, md, name):
    bl = sr.blocks(md, whole=True)
    probs = sr.check(review, bl)
    (OUT / ('%s.json' % name)).write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    if probs:
        for p in probs:
            print('PROBLEM', p)
        raise SystemExit(1)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    r = subprocess.run([sys.executable, 'tools/humanization/suggestion_review.py', 'page', REL + 'review/%s.json' % name,
                        REL + 'review/%s.html' % name, '--artifact', REL + 'review/%s-artifact.html' % name],
                       cwd=str(ROOT), env=env, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    if r.returncode:
        raise SystemExit(r.returncode)


def cards_md(review, path):
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for c in review['suggestions']:
        out += ['## %s: %s' % (c['id'], c['title']), '', '**Where:** after "%s"' % c['after_quote'], '',
                '**As it would read:**', '']
        out += ['> ' + i['text'] for i in c['inserts']]
        out += ['', '**What it says:** %s' % c['what'], '', '**Pangram:** %s' % c['reading'], '',
                '**Every try:** %s' % c['why'], '', '**What stays:** %s' % c['stays'], '',
                '**You\'re deciding:** %s' % c['deciding'], '', '**My advice:** %s' % c['advice_note'], '']
    path.write_text('\n'.join(out) + '\n', encoding='utf-8')


CARD = {
    'SH1': dict(
        title='Do These With a Clinician: a pointer to Imagery Rescripting',
        what=('A paragraph of its own at the end of the section, after "high-risk trauma work needs a bigger container than '
              'that": one such container, Imagery Rescripting, linked to its section in your somatic guide; how it is '
              'like the way you re-do trauma memories in your inner child guide (linked), and how it differs, the therapist '
              'in the scene as the ideal adult until you can be that adult yourself. It carries the somatic guide\'s '
              '"Imagery Rescripting" and the inner child guide\'s pointer to it (both live since 27 November).'),
        stays='Every paragraph of the section, its warnings about regression and memory included.',
        deciding='Whether this section points to Imagery Rescripting, worded this way.',
        ask_because=('meaning: it adds a paragraph to the Self-Hypnosis guide; and a fresh reader saw a tension: your inner '
                     'child guide has you re-do memories on your own, and this section sends trauma-focused regression to a '
                     'clinician (the pointer keeps the clinician side and names your way only as what the therapy is like)')),
    'SH2': dict(
        title="What It's For, and Not For: a pointer to the two pain therapies",
        what=('A paragraph of its own at the end of the section, after "Don\'t use self-hypnosis to: ... push symptoms down '
              'instead of getting medical attention ...": when the symptom is pain that has lasted months with no injury '
              'or disease found, keep using self-hypnosis for it and look for one of the two talk therapies in your somatic '
              'guide (linked), with your own sentence from the inner child guide on how they help. It carries "Pain That '
              'Won\'t Quit?" and the inner child guide\'s pointer to it.'),
        stays='Every paragraph of the section, and "Hypnosis Evidence" (that its evidence is strongest for pain).',
        deciding='Whether this section points to the two pain therapies, worded this way.',
        ask_because='meaning: it adds a paragraph to the Self-Hypnosis guide, with a sentence of yours from the inner child guide',
        whose=('his own: the last sentence, from his version of IC2 in the inner child guide (card IC2-TEACH, answers of '
               '2026-11-27 22:26 UTC); the rest of the paragraph is mine')),
    'SH3': dict(
        title='Too Analytical?: a pointer to Can\'t Stay With a Feeling?',
        what=('A paragraph of its own at the end of the section: analyzing a feeling instead of feeling it can follow you '
              'into therapy sessions, as explaining a feeling as soon as it comes up; if it keeps happening, ask whether '
              'your therapist is trained in Intensive Short-Term Dynamic Psychotherapy, or look for someone who is; what '
              'that therapist does, in your words from the somatic guide; and the section that has it and two other '
              'therapies (linked). It carries "Can\'t Stay With a Feeling?", live since this morning.'),
        stays='Every paragraph of the section and of "Dissociating or Unreal?" two headings up.',
        deciding='Whether this section points to the somatic guide\'s therapies for staying with feelings, worded this way.',
        ask_because='meaning: it adds a paragraph to the Self-Hypnosis guide'),
}


def main():
    n, res_path = sys.argv[1], sys.argv[2]
    OUT.mkdir(exist_ok=True)
    drafts = json.loads((HERE / ('DRAFTS-%s.json' % n)).read_text(encoding='utf-8'))
    results = json.loads(pathlib.Path(res_path).read_text(encoding='utf-8'))
    whole = (HERE / 'LIVE-HYPNOSIS-20261128.md').read_text(encoding='utf-8')
    md = fold_show(whole, SHOW)
    (OUT / 'ARTICLE-HYPNOSIS.md').write_text(md, encoding='utf-8')
    bl = sr.blocks(md, whole=True)
    cards = []
    for d in drafts:
        if d['id'] not in results:   # not checked yet, or below High: no card
            continue
        r = results[d['id']]
        before = next(b['i'] for b in bl if b['level'] and b['text'] == BR.head_text(d['next_block']))
        assert d['after'] in bl[before - 1]['text'], (d['id'], bl[before - 1]['text'][:80])
        c = CARD[d['id']]
        card = {'id': d['id'], 'type': 'addition', 'advice': 'approve', 'approve_label': 'add it',
                'title': c['title'], 'inserts': [{'before': before, 'kind': 'p', 'text': d['text'], 'seq': 0}],
                'card_after': before - 1, 'what': c['what'],
                'why': ('Four fresh readers read it against the ways you fix sentences, for need, fit and contradictions, '
                        'and every mark was acted on before the check ([the reads](%s)). %s' % (
                            BLOB + REL + 'reads/READ-4.md', r['why'])),
                'reading': r['reading'], 'tested': r['tested'], 'stays': c['stays'], 'deciding': c['deciding'],
                'advice_note': r['advice'], 'ask_because': c['ask_because'],
                'found_by': ('Fresh Fable reads against your fixes, for need, fit and contradictions; the check in your '
                             'Pangram account, 28 November'),
                'receipt': [REL + 'receipts/v%s/%s-linked.receipt.json' % (n, d['id'])],
                'after_quote': d['after']}
        if c.get('whose'):
            card['whose'] = c['whose']
        cards.append(card)
    review = {
        'format': sr.FORMAT, 'review_id': 'hypnosis-carry-cards-20261128',
        'title': 'Self-Hypnosis Guide, 28 November: the somatic and inner child additions, carried',
        'intro': [('Your Self-Hypnosis guide as it is live (25 November), with what is ready of the paragraphs that carry '
                   'what went into your somatic and inner child guides on 27 and 28 November, each where it would go. Long '
                   'stretches with no card fold into a box that opens. Nothing here is in the post yet.'),
                  ('One card now: the pointer to Imagery Rescripting, Human High. The other two, the pain therapies and '
                   'the therapies for explaining feelings away, wait for Pangram: the account\'s monthly credits ran out '
                   'this morning, with the pain pointer reading AI and the other not yet checked.')],
        'git_file': REL + 'review/REVIEW-HYPNOSIS.html',
        'article': {'file': REL + 'review/ARTICLE-HYPNOSIS.md', 'sha256': sha256(md)},
        'whole': {'file': REL + 'LIVE-HYPNOSIS-20261128.md', 'sha256': sha256(whole)},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': 'https://ibogaqueen.substack.com/p/guide-to-self-hypnosis-and-app-including',
                  'guide_label': 'your live post', 'review': BLOB + REL + 'review/CARDS-HYPNOSIS.md'},
        'types': {'addition': {'label': 'New paragraph', 'about': 'A paragraph the guide doesn\'t have yet, shown where it '
                                                                  'would go.'}},
        'suggestions': cards}
    page(review, md, 'REVIEW-HYPNOSIS')
    cards_md(review, OUT / 'CARDS-HYPNOSIS.md')
    print('ok')
    return 0


if __name__ == '__main__':
    sys.exit(main())
