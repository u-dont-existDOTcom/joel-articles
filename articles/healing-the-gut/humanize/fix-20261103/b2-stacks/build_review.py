#!/usr/bin/env python3
"""REVIEW.json for batch 2 (the fuels under Leaky gut, and the ready-made stacks), marked on r02: each paragraph's best
version that passed the blind meaning check and Pangram alone, and the two stretches that still read AI as stretches for
Joel to edit, in his words (his saved rule for help requests). No API calls."""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

R2 = HERE / 'r2-his-method'
MD = HERE.parent / 'r02' / 'r02.md'
md = MD.read_text(encoding='utf-8')
bl = sr.blocks(md)
RES = {}
for f in ('RESULTS.json', 'RESULTS-K.json', 'RESULTS-L.json', 'RESULTS-X.json'):
    RES.update(json.loads((R2 / f).read_text(encoding='utf-8')))
TXT = {k: (R2 / 'texts' / (k + '.txt')).read_text(encoding='utf-8') for k in RES}
BASE = json.loads((HERE.parent / 'baseline' / 'RESULTS.json').read_text(encoding='utf-8'))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/b2-stacks/r2-his-method/'


def find(start):
    i = [b['i'] for b in bl if b['text'].startswith(start)]
    assert len(i) == 1, start
    return i[0]


def conf(r):
    return ', '.join('%s %s (%sw)' % ('Human' if w['label'].startswith('Human') else 'AI', w['confidence'], w['words']) for w in r['windows'])


def tested(key):
    r = RES[key]
    return '%s, %d%% human; windows %s. [Pangram result](%s)' % (r['prediction_short'], round(100 * r['fraction_human']), conf(r), r['link'])


def reading(bkey, what):
    r = BASE[bkey]
    return 'Your post as it was, %s alone: %s, %d%% human. [Pangram result](%s)' % (what, r['prediction_short'], round(100 * r['fraction_human']), r['link'])


def reads(text, heading=False):
    out = []
    for line in [l for l in text.split('\n') if l.strip()]:
        if heading and not out:
            out.append({'text': line, 'kind': 'h2'})
        else:
            out.append({'text': line, 'kind': 'p'})
    return out


S = []
# 1. the heading and the order paragraph (L1)
h, p74 = find('Optional Ready-Made Gut Stacks'), find('I do not think there is a universal supplement stack')
l1 = TXT['b2-ST-L1'].split('\n')
S.append({'id': 'S2-1', 'type': 'voice', 'title': 'The stacks section opens in your voice', 'advice': 'approve',
          'spans': [{'block': p74, 'start': 0, 'end': len(bl[p74]['text'])}],
          'edits': [{'block': p74, 'before': bl[p74]['text'], 'after': l1[1]}], 'reads': reads(l1[1]), 'reads_label': 'As it would read',
          'what': 'The order said as what you do ("Get your digestion working mechanically first, then reset your diet and your gut motility, and only go after bugs and parasites with antimicrobial or anti-parasite protocols if you still have symptoms after that"). The phase labels I had added first read AI, so they\'re gone.',
          'why': 'It read AI in your post. Three earlier versions read AI too; this one passed the blind meaning check after one fix (the anti-parasite protocols put back).',
          'stays': 'No universal stack; the order: mechanics, then diet and motility, then antimicrobials only if symptoms persist.',
          'deciding': 'Whether it sounds like you.', 'advice_note': 'Approve, or Revise with your own wording.',
          'tested': tested('b2-ST-L1'), 'reading': reading('GH-35', 'this paragraph')})
# 2. the categories paragraph: his help
p75, o1, o2, o3 = find('That said, some people want'), find('Microbiome support:'), find('Prebiotic / butyrate support:'), find('Barrier repair:')
tries = [('b2-ST-J2', 'my first, in your Phase 1 method'), ('b2-ST-K2', 'my second, after three fresh readers'), ('b2-ST-L2', 'my third, its opening as a question to you')]
links = '; '.join('%s: [%s](%s)' % (w, RES[k]['prediction_short'] + ' %d%%' % round(100 * RES[k]['fraction_human']), RES[k]['link']) for k, w in tries)
S.append({'id': 'S2-2', 'type': 'help', 'title': 'The three things to look for: four versions read AI', 'advice': 'edit',
          'spans': [{'block': p75, 'start': 0, 'end': len(bl[p75]['text'])}], 'card_after': o3,
          'why': 'I can\'t find any more AI tells here, and I see some human tells, like these: "But maybe you\'d rather start with something ready-made", "and so on" at the end of the list, no labels. Can you help show me the tells I\'m missing? ' + links + '. A fourth, by Codex, failed the meaning check (it added "can be a hassle"). Three fresh readers flagged the three parallel "something ..." items and the list itself ([panel](' + GH + 'panel/b2-ST-K2/PANEL.md)).',
          'advice_note': 'Rewrite it with Edit, the way you did Phase 1. It has to keep: a ready-made start instead of buying every ingredient separately; a general "repair and rebuild" stack; the three things (a well-tolerated probiotic or probiotic system; prebiotic or butyrate support, especially butyrate; and barrier repair with glutamine, zinc carnosine, colostrum, mucosal-support herbs or similar).\n\nMy best try:\n' + TXT['b2-ST-L2'],
          'reading': reading('GH-36-39', 'this paragraph and its list')})
# 3. the kits (X3, Codex's, which passed)
p79 = find('The best general commercial stack')
x3 = TXT['b2-ST-X3']
S.append({'id': 'S2-3', 'type': 'voice', 'title': 'The kits, with your answer about them', 'advice': 'approve',
          'spans': [{'block': p79, 'start': 0, 'end': len(bl[p79]['text'])}],
          'edits': [{'block': p79, 'before': bl[p79]['text'], 'after': x3}], 'reads': reads(x3), 'reads_label': 'As it would read',
          'what': 'Your r01 answer first, fitted as one sentence ("Gemini suggested these kits to me, but so far they\'re the best ones I\'ve seen, tho I haven\'t used them myself, so check the reviews"). The three kits in a different order (GI Revive first, Microbiome Labs last as "the best general stack of these"). Written by Codex after two of my versions read Mixed on the GI Revive sentence.',
          'why': 'It read AI in your post; it passed the blind meaning check.',
          'stays': 'The three kits, what each is for, that GI Revive is only the repair part; your answer that Gemini suggested them, they\'re the best you\'ve seen so far, you haven\'t used them, check the reviews.',
          'deciding': 'Whether the new order and the wording are yours.', 'advice_note': 'Approve, or Revise.',
          'tested': tested('b2-ST-X3'), 'reading': reading('GH-40', 'this paragraph')})
# 4. the cleanse stacks (K4)
p80 = find('I would not recommend general')
k4 = TXT['b2-ST-K4']
S.append({'id': 'S2-4', 'type': 'voice', 'title': 'The cleanse stacks, with your berberine note', 'advice': 'approve',
          'spans': [{'block': p80, 'start': 0, 'end': len(bl[p80]['text'])}],
          'edits': [{'block': p80, 'before': bl[p80]['text'], 'after': k4}], 'reads': reads(k4), 'reads_label': 'As it would read',
          'what': '"I wouldn\'t start everyone off on" for "as a universal starting point"; the herbs after their category; "Those are for later (Phase 3)", a pointer of mine; your berberine note as it was.',
          'why': 'It read AI in your post; it passed the blind meaning check. Its first window reads Human at Low, so it\'s not done: if you see what reads AI in "I wouldn\'t start everyone off ...", that\'s the spot.',
          'stays': 'Not a universal starting point; the herbs; later, when there\'s more reason to suspect overgrowth, parasites, H. pylori or something specific; your H. pylori exception.',
          'deciding': 'Whether it sounds like you, and the "(Phase 3)" pointer.', 'advice_note': 'Approve, or Revise.',
          'tested': tested('b2-ST-K4'), 'reading': reading('GH-41', 'this paragraph')})
# 5. start low and the clinician list (J5)
p81 = find('Start low, especially with prebiotics')
j5 = TXT['b2-ST-J5']
S.append({'id': 'S2-5', 'type': 'voice', 'title': 'Start low, and who should see a clinician', 'advice': 'approve',
          'spans': [{'block': p81, 'start': 0, 'end': len(bl[p81]['text'])}],
          'edits': [{'block': p81, 'before': bl[p81]['text'], 'after': j5}], 'reads': reads(j5), 'reads_label': 'As it would read',
          'what': '"Start with low doses, especially of ..."; the clinician list as one plain "if you have ..., don\'t stack supplements on your own, work with a qualified clinician instead".',
          'why': 'It read AI in your post; it passed the blind meaning check.', 'stays': 'Every supplement to start low with, and every condition on the list.',
          'deciding': 'Whether it sounds like you.', 'advice_note': 'Approve, or Revise.',
          'tested': tested('b2-ST-J5'), 'reading': reading('GH-42', 'this paragraph')})
# 6. the fuels: his help
f0 = find('Mitochondrial & Cellular Energy Starvation')
f_end = find('TCA Cycle Intermediates')
ftries = [('b2-LGF-J', 'mine in your Phase 1 method'), ('b2-LGF-X', "Codex's, after three fresh readers")]
flinks = '; '.join('%s: [AI %d%%](%s)' % (w, round(100 * RES[k]['fraction_human']), RES[k]['link']) for k, w in ftries)
S.append({'id': 'S2-6', 'type': 'help', 'title': 'The mitochondrial fuels: five versions read AI', 'advice': 'edit',
          'spans': [{'block': f0, 'start': 0, 'end': len(bl[f0]['text'])}], 'card_after': f_end,
          'why': 'I can\'t find any more AI tells here, and I see some human tells, like these: "watch Dr. Rhonda vid", "your home-brewed SIBO yogurt", "clean sour stuff", "CAUTION:" the way you write it under diverticulosis. Can you help show me the tells I\'m missing? Five versions read 0% human: two writers\' and a shorter one earlier today, then ' + flinks + '. The three readers flag the same thing in each: name a substance, give its mechanism, give a confident benefit, again ([panel](' + GH + 'panel/b2-LGF-J/PANEL.md)). It\'s the neuro article\'s pattern too (gate E336: the science and the doses read Human only in your wording).',
          'advice_note': 'Rewrite one part of it with Edit (the glutamine item, say), the way you did Phase 1, and I\'ll do the rest the way yours is built. It has to keep every dose (5g a day baseline for hard training; 10-30g during acute immune exposure, high stress or active IBD), the cancer caution with the portal vein, the link, and each fuel\'s job.\n\nMy try in your method:\n' + TXT['b2-LGF-J'],
          'reading': reading('GH-12', 'the whole Leaky gut item, where your part read Human, High and this stretch AI')})

review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b2-stacks-20261103',
    'title': 'Gut Stacks and Fuels',
    'intro': ['Batch 2, on the article as it now stands (r02: your Phase 1 and Phase 5, your approved phases, the nicknames gone, the standard swap). Four paragraphs of the stacks section now read Human alone, each checked blind for meaning; each card has its Pangram link and every window\'s confidence.',
              'Two stretches still read AI after my versions, three fresh readers and a rewrite by Codex: the stacks section\'s three things to look for, and the mitochondrial fuels under Leaky gut. Those are stretches for you to edit.'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/b2-stacks/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r02/r02.md', 'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-03',
    'links': {'guide': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/r02/r02.md',
              'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/b2-stacks/REVIEW-CARDS.md'},
    'types': {'voice': {'label': 'In your voice', 'about': 'Rewritten and checked'},
              'help': {'label': 'Your help', 'about': 'Faithful rewrites still read AI'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s['advice'] == 'edit':
        out += [s['why'], '', s['advice_note'].replace('\n', '\n\n'), '', s['reading'], '']
        continue
    out += ['**As it would read:**', ''] + ['> ' + p['text'] for p in s['reads']] + ['']
    out += ['**Pangram on this version:** ' + s['tested'], '', '**Before:** ' + s['reading'], '', '**What changed:** ' + s['what'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
