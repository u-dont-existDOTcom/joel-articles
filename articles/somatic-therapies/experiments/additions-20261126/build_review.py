#!/usr/bin/env python3
"""build_review.py - the marking page of 2026-11-26 for the somatic guide: the three sections ChatGPT suggested that day
(experiential therapies for people who slide away from feelings, imagery rescripting, and a branch for pain that won't
quit), as Joel asked ("i also want to make an addition to the somatic.u-dont-exist.com article with the recs from gpt
below (humanized)"), each as a card in the whole guide as it is live.

  python3 articles/somatic-therapies/experiments/additions-20261126/build_review.py

Reads, in this folder:
  WHOLE-LIVE-20261126.md      the guide as it is live on 2026-11-26 (live_markdown.py): the whole article the page shows
  ADDITIONS-<N>.json          the additions (FINAL below): heading, place (the heading they go before), paragraphs with links
  receipts/*.receipt.json     each new paragraph's and heading's making-sense receipt (fill_receipts.py)
  READINGS                    below: what Pangram read on each addition, in its section, with the links
Writes, in review/:
  ARTICLE.md                  WHOLE-LIVE-20261126.md with <!-- CUT --> lines around the long stretches that hold no card
  REVIEW.json, REVIEW.html, REVIEW-artifact.html, CARDS.md
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
import suggestion_review as sr  # noqa: E402

REL = 'articles/somatic-therapies/experiments/additions-20261126/'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
POST = 'https://somatic.u-dont-exist.com'
FINAL = 'ADDITIONS-8.json'
OUT = HERE / 'review'

# What Pangram read on each addition by itself (its section without its heading), filled from pangram-ledger.jsonl.
READINGS = json.loads((HERE / 'pangram' / 'READINGS.json').read_text(encoding='utf-8'))

# The stretches the page always shows: the context each card needs (Layer 3 for A1, which asks "As with water
# therapy"; Layer 4 for A2, which follows EMDR; Layer 5 for A3; and the closing section A3 links to).
SHOW = [('Layer 3: Compassionate Exploration of Trauma Feelings Before the Story Comes In', 'Hypnosis, the ancestral therapy'),
        ('Layer 5: Integrate, Differentiate, and Build a Life of Meaning', 'Psychedelics'),
        ('How I Judge Whether Any of This Is Helping', None)]

SOURCES = {
    'A1': [('Abbass 2021, “Intensive Short-term Dynamic Psychotherapy: Methods, Evidence, Indications and Limitations”',
            'https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and',
            'what the therapist does; the anxiety signs it watches (tense muscles, sighing, foggy thinking); most patients '
            'in its clinics overwhelm easily and get the slower, graded version'),
           ('Schanche, Hjeltnes, Berggraf and Ulvenes 2013, “Affect Phobia Therapy: Principles of graded affect exposure”',
            'https://psykologtidsskriftet.no/node/15971/pdf', 'fear of one\'s own feelings, treated like a phobia, gradually'),
           ('APA, Fosha, “Accelerated Experiential Dynamic Psychotherapy”', 'https://www.apa.org/pubs/videos/4310759',
            'not being alone with the feeling first; following the feeling in the body')],
    'A2': [('Boterhoven de Haan et al. 2020, British Journal of Psychiatry 217(5):609-615',
            'https://pubmed.ncbi.nlm.nih.gov/32892758/',
            '155 adults with PTSD from childhood trauma; imagery rescripting and EMDR both helped, neither clearly better; '
            'the therapist steps into the scene first, the patient\'s adult self later'),
           ('Your inner child guide, “Re-do Trauma Memories” (live 25 November)',
            'https://ibogaqueen.substack.com/i/189761959/re-do-trauma-memories', 'the section the card links to')],
    'A3': [('Ashar et al. 2022, JAMA Psychiatry 79(1):13-23', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8482298',
            '151 adults with chronic back pain; 66% of 50 given 4 weeks of Pain Reprocessing Therapy at 0 or 1 out of 10 '
            'afterward, against 20% of 51 given a placebo shot; gains largely kept at a year'),
           ('NIH Research Matters, 2 November 2021', 'https://www.nih.gov/news-events/nih-research-matters/retraining-brain-treat-chronic-pain',
            'the trial was in mild or moderate chronic back pain'),
           ('Yarns et al. 2024, JAMA Network Open (trial NCT03918642)', 'https://clinicaltrials.gov/study/NCT03918642',
            '126 veterans aged 60 to 95; 63% with Emotional Awareness and Expression Therapy and 17% with CBT had at least '
            '30% less pain; its parts: writing about stress, role-play, expressing anger and other feelings, being more '
            'open with others'),
           ('No trial compares the two', 'https://pubmed.ncbi.nlm.nih.gov/?term=%22pain+reprocessing+therapy%22+%22emotional+awareness+and+expression+therapy%22',
            'searched 26 November by the research lane and by me; none found')],
}

CARD = {
    'A1': dict(
        title='New section after Brainspotting: “Can’t Stay With a Feeling?”',
        where='at the end of Layer 3, after Brainspotting (an h2)',
        what=('A new section of %(n)d paragraphs (%(w)d words) at the end of Layer 3, after Brainspotting and before '
              'Layer 4: for someone who can feel their body by now but slides away from a feeling the moment it comes '
              'up in a session. It names three talk therapies built for that (Intensive Short-Term Dynamic Psychotherapy, '
              'Affect Phobia Therapy, Accelerated Experiential Dynamic Psychotherapy), says whom each fits, and ends on the '
              'question to ask before booking, the way your water therapy section does.'),
        advice=('Approve it if you want the section, but it goes in only once it reads Human, and what would get it there '
                'is something only you have. Have you seen someone slide away from a feeling like this, in your own '
                'sessions or Hâle’s, or done it yourself in therapy? A line or two of what it looked like would carry the '
                'section, and I’d build its first paragraph around it. Without one, my next try ties it to what the guide '
                'already says (Hâle’s worry that the feeling can outrun the therapist) instead of explaining the '
                'therapies in general terms; the readings show general explaining is what reads AI here.'),
        why=('ChatGPT’s first suggestion (26 November): the guide goes from body work to memory work and has nothing for '
             'the reader who can feel the body but can’t stay with a feeling in front of a therapist. You told the research '
             'lane to add only what fills a gap, and to say where it fits and who needs which; this section does that in '
             'its first paragraph and in each therapy’s sentence.'),
        deciding=('Whether the guide should name these three therapies, and here. Two things to weigh: the guide jokes '
                  'that every year brings 50 new kinds of therapies, mostly permutations of the old ones, and this adds '
                  'three names, though none is new (Abbass’s review cites Davanloo’s first ISTDP work of 1977, '
                  'Affect Phobia Therapy’s manual is from 2003, and Diana Fosha’s first book on AEDP from 2000); and it says most people who go to the first one get its slower version, which '
                  'is from Abbass’s review, not a count of my own.')),
    'A2': dict(
        title='New section after EMDR: “Imagery Rescripting”',
        where='in Layer 4, after EMDR and before hypnosis (an h2)',
        what=('A new section of %(n)d paragraphs (%(w)d words) in Layer 4, right after the EMDR paragraph that warns going '
              'straight into a trauma memory can re-traumatize: what imagery rescripting is (you picture the scene again '
              'and someone steps in to protect you, the therapist first and later your adult self), a link to “Re-do '
              'Trauma Memories” in your inner child guide, the trial that found it did about as well as EMDR, and the '
              'same care to take as with EMDR.'),
        advice=('Approve it if you want the section, but it goes in only once it reads Human. The one sentence that read '
                'Human is the one about your own Re-do Trauma Memories, so your own experience is what would carry it: '
                'have you done that exercise with someone guiding you, or guided someone through it? A line of what '
                'happened would let me build the section on it. Without one, my next try keeps the therapy\'s description '
                'to one sentence and says the rest through your section.'),
        why=('ChatGPT’s second suggestion: the guide’s memory layer has EMDR and hypnosis but not the therapy closest to '
             'your own re-doing of memories, which a trial put level with EMDR for adults traumatized as children.'),
        deciding=('Whether to add it, and whether the line tying it to your “Re-do Trauma Memories” section says it '
                  'right (“It’s a lot like the way I re-do trauma memories”): your section uses a cast of wiser future '
                  'characters, where rescripting uses the therapist and then your adult self.')),
    'A3': dict(
        title='New branch after Layer 5: “Pain That Won’t Quit?”',
        where='after Layer 5, before the optional high-intensity practices (an h1)',
        what=('A new branch of %(n)d paragraphs (%(w)d words) after Layer 5: for a reader whose pain has lasted months with '
              'no injury or disease found, two therapies (Pain Reprocessing Therapy and Emotional Awareness and '
              'Expression Therapy), each with what you do in it and its trial, limit first, then how to choose between '
              'them and a link to “How I Judge Whether Any of This Is Helping”.'),
        advice=('I’d add it as it is: it reads Human. Two things a fresh reader wanted, which I tried and Pangram then read '
                'as AI (made together with five other fixes): “false alarm” could read as “your pain isn’t real” (my fix: '
                '“the pain, though real, is a false alarm”), and “the second” and “the first” in the last paragraph could '
                'be clearer as the two names. If you want either, say so and I’ll check each by itself. The three Low '
                'windows are next on my list either way.'),
        why=('ChatGPT’s third suggestion: the guide mentions pain as something that changes how much therapy you can '
             'take, but has nothing for the reader who came to it because of pain. It is a branch (an h1 of its own), not '
             'a sixth layer.'),
        deciding=('Whether the guide should have a pain branch at all (it is the longest of the three), and whether as '
                  'its own h1 or as a section inside Layer 5. The two trials can’t be set side by side (different bars, '
                  'different people), which the section says.')),
}


def sha256(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def raw_blocks(md):
    return [b for b in re.split(r'\n\s*\n', md.strip('\n'))]


def head_text(b):
    m = re.match(r'^(#{1,6})\s+(.*)$', b.strip())
    return m.group(2).strip() if m else None


def fold(md):
    """md with <!-- CUT --> / <!-- /CUT --> lines around each long stretch outside SHOW (at least CUT_MIN_BLOCKS
    paragraphs and CUT_MIN_WORDS words, the tool's limits), cut at headings so a box holds whole sections."""
    raw = raw_blocks(md)
    heads = [head_text(b) for b in raw]
    shown = [False] * len(raw)
    for start, end in SHOW:
        a = heads.index(start)
        z = heads.index(end) if end else len(raw)
        for i in range(a, z):
            shown[i] = True
    out, run = [], []

    def flush():
        paras = [b for b in run if not head_text(b) and not b.strip().startswith('<!--')]
        words = sum(len(re.sub(r'\]\([^)]*\)', ']', b).split()) for b in paras)
        if len(paras) >= sr.CUT_MIN_BLOCKS and words >= sr.CUT_MIN_WORDS:
            out.extend(['<!-- CUT -->'] + run + ['<!-- /CUT -->'])
        else:
            out.extend(run)
        run.clear()

    for i, b in enumerate(raw):
        if shown[i]:
            flush()
            out.append(b)
        else:
            if heads[i] and heads[i] in ('The Dominant Trauma-Memory Therapies Are Missing Something',):
                flush()
            run.append(b)
    flush()
    return '\n\n'.join(out) + '\n'


def md_esc(t):
    return t.replace('*', '\\*')


def main():
    whole = (HERE / 'WHOLE-LIVE-20261126.md').read_text(encoding='utf-8')
    page_md = fold(whole)
    OUT.mkdir(exist_ok=True)
    (OUT / 'ARTICLE.md').write_text(page_md, encoding='utf-8')
    bl = sr.blocks(page_md, whole=True)
    adds = json.loads((HERE / FINAL).read_text(encoding='utf-8'))
    cards = []
    for a in adds:
        c = CARD[a['id']]
        before = next(b['i'] for b in bl if b['level'] and b['text'] == a['before_heading'])
        inserts = [{'before': before, 'kind': 'h%d' % a['level'], 'text': a['heading'], 'seq': 0}]
        inserts += [{'before': before, 'kind': 'p', 'text': p, 'seq': k + 1} for k, p in enumerate(a['paragraphs'])]
        n = len(a['paragraphs'])
        receipts = [REL + 'receipts/%s-H.receipt.json' % a['id']] + [REL + 'receipts/%s-P%d.receipt.json' % (a['id'], k)
                                                                     for k in range(1, n + 1)]
        rd = READINGS[a['id']]
        src = SOURCES[a['id']]
        cards.append({
            'id': a['id'], 'type': 'addition', 'advice': 'approve', 'approve_label': 'add it', 'title': c['title'],
            'inserts': inserts, 'card_after': before - 1,
            'what': c['what'] % {'n': n, 'w': a['words']},
            'why': c['why'],
            'stays': 'Every paragraph of the guide as it is live; nothing moves or goes.',
            'deciding': c['deciding'],
            'advice_note': ('The sources I checked: ' + '; '.join('[%s](%s) (%s)' % s for s in src) + '.'),
            'found_by': ('ChatGPT’s recommendations you sent on 26 November. I checked each claim against the sources on '
                         'this card, wrote the section in your guide’s voice, and fresh readers read it %s against the '
                         'ways you fix sentences, for what its reader needs, for fit, and for contradictions with the '
                         'guide; what they marked was changed or is named here.' % rd.get('rounds', 'five times')),
            'ask_because': ('meaning: it adds a new section with new claims about named therapies and trials to your '
                            'guide, under your byline'),
            'receipt': receipts,
            'tested': rd['tested'],
        })
        if rd.get('warning'):
            cards[-1]['warning'] = rd['warning']
        cards[-1]['advice_note'] = c['advice'] + ' ' + cards[-1]['advice_note']
    intro = [
        ('This is your somatic guide as it is live today (26 November), with the three sections ChatGPT suggested, '
         'written in the guide’s voice from its sources, which I checked, each shown where it would go. Nothing here is '
         'in the post yet.'),
        ('Together they add %d words to a guide of about %s words. Long stretches with no card fold into a box that '
         'opens.' % (sum(a['words'] for a in adds), format(round(len(re.sub(r'<!--.*?-->', '', whole, flags=re.S).split()), -2), ','))),
        ('Approve, Reject or Revise on each card is your answer; when you’re done, open “Save / send”, press “Copy my '
         'answers (JSON)” and send them back to me.'),
    ]
    review = {
        'format': sr.FORMAT,
        'review_id': 'somatic-additions-20261126',
        'title': 'Somatic Guide, 26 November: three new sections from ChatGPT’s suggestions',
        'intro': intro,
        'git_file': REL + 'review/REVIEW.html',
        'article': {'file': REL + 'review/ARTICLE.md', 'sha256': sha256(page_md)},
        'whole': {'file': REL + 'WHOLE-LIVE-20261126.md', 'sha256': sha256(whole)},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + REL + 'WHOLE-LIVE-20261126.md', 'guide_label': 'the guide as it is live on 26 November',
                  'review': BLOB + REL + 'review/CARDS.md'},
        'types': {'addition': {'label': 'New section', 'about': ('A section the guide doesn’t have yet, written from '
                                                                 'ChatGPT’s suggestions of 26 November and checked against '
                                                                 'the studies, shown where it would go.')}},
        'suggestions': cards,
    }
    (OUT / 'REVIEW.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

    md = ['# %s' % review['title'], '', intro[0], '', intro[1].split(' Long stretches')[0], '',
          'This page is the same cards for reading on GitHub; the Approve, Reject and Revise buttons are on the marking '
          'page, which shows each card inside the whole guide. [The guide as it is live](%s) · [the live post](%s)'
          % (BLOB + REL + 'WHOLE-LIVE-20261126.md', POST), '']
    for a, c in zip(adds, cards):
        md += ['## %s · %s' % (c['id'], c['title']), '', '*New section · %s*' % CARD[a['id']]['where'], '',
               '**As it would read**', '',
               '\n>\n'.join(['> %s **%s**' % ('#' * (a['level'] + 1), md_esc(a['heading']))]
                            + ['> ' + md_esc(p) for p in a['paragraphs']]), '',
               '**What it adds:** %s' % c['what'], '', '**Why:** %s' % c['why'], '',
               '**Pangram:** %s' % c['tested'], '', '**What stays:** %s' % c['stays'], '',
               '**Why I’m asking:** %s' % c['ask_because'][len('meaning: '):][:1].upper()
               + c['ask_because'][len('meaning: ') + 1:], '',
               '**You’re deciding:** %s' % c['deciding'], '', '**My advice:** %s' % c['advice_note'], '']
    (OUT / 'CARDS.md').write_text('\n'.join(md).rstrip('\n') + '\n', encoding='utf-8')

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    tool = 'tools/humanization/suggestion_review.py'
    rj = REL + 'review/REVIEW.json'
    r = subprocess.run([sys.executable, tool, 'check', rj], cwd=str(ROOT), env=env, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    if r.returncode:
        print('check did not pass: no page written')
        return 1
    r = subprocess.run([sys.executable, tool, 'page', rj, REL + 'review/REVIEW.html', '--artifact',
                        REL + 'review/REVIEW-artifact.html'], cwd=str(ROOT), env=env, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
