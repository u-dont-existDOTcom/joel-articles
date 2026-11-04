#!/usr/bin/env python3
"""REVIEW.json for batch 1 (the protocol section): the whole article as of r01 with each phase's best tested
rewrite marked on it, Phase 1 as a stretch for Joel, and the nickname question. No API calls."""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = HERE.parent / 'r01' / 'r01.md'
md = MD.read_text(encoding='utf-8')
bl = sr.blocks(md)
W = {t: json.loads((HERE / ('writer_%s.json' % t)).read_text(encoding='utf-8')) for t in 'ABC'}
R = {}
for t in 'ABC':
    R.update(json.loads((HERE / ('RESULTS-%s.json' % t)).read_text(encoding='utf-8')))
BASE = json.loads((HERE.parent / 'baseline' / 'RESULTS.json').read_text(encoding='utf-8'))


def conf(r):
    return ', '.join('%s %s (%dw)' % ('Human' if w['label'].startswith('Human') else 'AI', w['confidence'], w['words'] or 0)
                     for w in r['windows'])


def tested(key):
    r = R[key]
    return '%s, %d%% human; windows %s. [Pangram result](%s)' % (r['prediction_short'], round(100 * r['fraction_human']), conf(r), r['link'])


def reading(bkey, what):
    r = BASE[bkey]
    return 'Your post as it was, %s alone: %s, %d%% human. [Pangram result](%s)' % (what, r['prediction_short'], round(100 * r['fraction_human']), r['link'])


# the blocks of each unit in r01.md
heads = [b['i'] for b in bl if b['kind'] == 'h4' and b['text'].startswith('Phase ')]
end = [b['i'] for b in bl if b['kind'] == 'h2' and b['text'].startswith('Optional Ready-Made')][0]
units = {}
for n, h in enumerate(heads):
    k = 'P' + re.search(r'Phase (\d)', bl[h]['text']).group(1)
    units[k] = list(range(h, heads[n + 1] if n + 1 < len(heads) else end))
pi = [b['i'] for b in bl if b['text'].startswith('This protocol is designed to be executed in phases')][0]
units['PI'] = [pi]


def paras(text):
    """The rewrite's paragraphs for "reads": heading, then each paragraph or list item as the reader sees it."""
    out = []
    for block in text.split('\n\n'):
        for line in block.split('\n'):
            t = line.strip()
            if not t:
                continue
            kind = 'p'
            m = re.match(r'^(#+)\s*(.*)$', t)
            if m:
                kind, t = 'h%d' % len(m.group(1)), m.group(2)
            t = re.sub(r'^(?:[-*]|\d+\.)\s+', '', t)
            t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
            t = re.sub(r'(\*\*|__)(.+?)\1', r'\2', t)
            t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\1', t)
            out.append({'text': t, 'kind': kind})
    return out


def unit_change(k, writer):
    blocks = units[k]
    new = paras(W[writer][k]['text'])
    body = [p['text'] for p in new if p['kind'] == 'p']
    edits = []
    if bl[blocks[0]]['kind'] == 'h4':
        h = [p['text'] for p in new if p['kind'] == 'h4'][0]
        if h != bl[blocks[0]]['text']:
            edits.append({'block': blocks[0], 'before': bl[blocks[0]]['text'], 'after': h})
        rest = blocks[1:]
    else:
        rest = blocks
    edits.append({'block': rest[0], 'before': bl[rest[0]]['text'], 'after': ' '.join(body)})
    for i in rest[1:]:
        edits.append({'block': i, 'before': bl[i]['text'], 'after': ''})
    return edits, new


S = []
PICK = [('PI', 'A', 'The protocol\'s opening line', None, None),
        ('P2', 'C', 'Phase 2 in your voice', 'GH-21-23', 'Phase 2'),
        ('P3', 'B', 'Phase 3 in your voice', 'GH-24-26', 'Phase 3 (your H2O2 lines included)'),
        ('P4', 'B', 'Phase 4 in your voice', 'GH-29-31', 'the old Phase 5, which held Investigation'),
        ('P5', 'A', 'Phase 5 in your voice', 'GH-32-34', 'the old Phase 6, Restoration'),
        ('P6', 'B', 'Phase 6 in your voice', 'GH-29-31', 'the old Phase 5, which held Nathan and Hopper')]
for k, wr, title, bkey, what in PICK:
    edits, new = unit_change(k, wr)
    key = 'b1-%s-%s' % (k, wr)
    s = {'id': 'H-' + k, 'type': 'voice', 'title': title, 'advice': 'approve',
         'spans': [{'block': units[k][0], 'start': 0, 'end': len(bl[units[k][0]]['text'])}],
         'edits': edits, 'reads': new, 'reads_label': 'As it would read', 'card_after': units[k][-1],
         'what': W[wr][k]['notes'],
         'why': 'The phase read AI in your post. This version keeps every step, test, compound, dose, warning and source, and your "My notes" line word for word; a blind reader checked it step by step against the original (PASS).',
         'stays': 'Everything the phase tells the reader to do, in the same order, with the same sources.',
         'deciding': 'Whether it sounds like you.',
         'advice_note': 'Approve, or Revise with your own wording.',
         'tested': tested(key)}
    if bkey:
        s['reading'] = reading(bkey, what)
    S.append(s)

# Phase 1: three faithful tries all read AI; his help, in the words he asked for
links = ', '.join('[%s](%s)' % (t, R['b1-P1-%s' % t]['link']) for t in 'ABC')
S.append({
    'id': 'H-P1', 'type': 'help', 'title': 'Phase 1: three faithful rewrites all read AI', 'advice': 'edit',
    'spans': [{'block': units['P1'][0], 'start': 0, 'end': len(bl[units['P1'][0]]['text'])}],
    'card_after': units['P1'][-1],
    'why': 'I can\'t find any more AI tells here, and I see some human tells, like these: the reader\'s questions run together ("Are your pupils dilated all the time? No gag reflex?"), "Then bile.", plain verbs, and no engine/fuel/fire metaphor. Can you help show me the tells I\'m missing? Three different faithful versions each read about 10% human: ' + links + '. The third, mine, is below; every step and source is in it.',
    'advice_note': 'Rewrite it yourself with Edit, or tell me what still reads AI to you. It\'s the only phase where no version passed; your "My notes" line reads Human in all three, and everything above it reads AI, at High confidence on the "Then according to Hale you\'re stuck in fight/flight" and "Do your stools float" stretches. My guess is the symptom, then state, then fix pattern, twice, but I\'ve already rewritten around that once. If you have your own take on Hale\'s checks (you say in Low stomach acid he\'s "a bit controversial on some points"), a sentence of it here might be what it needs; I won\'t add one for you.\n\nMy try:\n' + '\n'.join(p['text'] for p in paras(W['C']['P1']['text'])),
    'reading': reading('GH-18-20', 'Phase 1'),
})

S.append({
    'id': 'Q-NICK', 'type': 'question', 'title': 'Drop the nicknames from the phase headings?', 'advice': 'ask',
    'spans': [{'block': units['P2'][0], 'start': 0, 'end': len(bl[units['P2'][0]]['text'])}],
    'question': 'The headings carry Gemini\'s nicknames: (The Mechanic & Electrician), (The Architect & Scientist), (The Restorer), (The Detective), (The Gardener), (The Hazmat Team). The rewrites that passed mostly dropped them, so as it stands some headings have one and some don\'t. Drop them all, or keep them all? (My pick: drop them. They\'re Gemini\'s persona labels, not yours. If you say drop, I\'ll recheck Phase 5 without its nickname, since it was tested with it.)',
    'why': 'The headings have to be consistent either way.',
    'stays': 'Each heading as tested until you answer.',
    'advice_note': 'Drop them all.',
})

review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b1-protocol-20261103',
    'title': 'Gut Protocol Voice',
    'intro': [
        'The protocol section in your voice, phase by phase. Two writers worked from your fixes catalogue, every version passed a blind step-by-step meaning check, and each phase shown here passed Pangram alone (the link is on its card, with each window\'s confidence). Where a window reads Human below High, the card says so; those are the next thing I\'d work on.',
        'Phase 1 is the exception: three faithful versions all read AI, so it\'s on the page as a stretch for you, with my best try in the card.',
    ],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/b1-protocol/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r01/r01.md', 'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-03',
    'links': {'guide': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/r01/r01.md',
              'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/b1-protocol/REVIEW-CARDS.md'},
    'types': {'voice': {'label': 'In your voice', 'about': 'A phase rewritten and checked'},
              'help': {'label': 'Your help', 'about': 'Faithful rewrites still read AI'},
              'question': {'label': 'Question', 'about': 'Needs your answer'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')

out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s['advice'] == 'ask':
        out += ['**Question:** ' + s['question'], '']
        continue
    if s['advice'] == 'edit':
        out += [s['why'], '', s['advice_note'].replace('\n', '\n\n'), '', s.get('reading', ''), '']
        continue
    out += ['**As it would read:**', ''] + ['> ' + p['text'] + '\n>' for p in s['reads']] + ['']
    out += ['**Pangram on this version:** ' + s['tested'], '']
    if s.get('reading'):
        out += ['**Before:** ' + s['reading'], '']
    out += ['**What changed:** ' + s['what'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
