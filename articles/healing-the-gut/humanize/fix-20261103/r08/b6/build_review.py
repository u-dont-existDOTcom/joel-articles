#!/usr/bin/env python3
"""REVIEW.json for batch 6: the stacks section, fixed before any article check, marked on r07 (the article before these
changes) so each card shows its change in place. Joel, 2026-11-04 14:41 UTC: "no the whole article doesn't decide, we need
to first fix any windows we can see before we check the article" (gate E354). In its own API check the section read AI (5%
human, 12 of 13 windows AI). A newcomer read (../stacks/links/) and the tell panel (../stacks/panel/) found what to fix;
every changed paragraph passed the blind meaning check (../stacks/MEANING-VERDICTS*.json). Two of mine now read Human
(High) by themselves; the kits, the start-low paragraph and the glutamine caution still read AI or Low and ask his help;
his three-category paragraph gets my suggestion, his to take or leave. No API calls."""
import hashlib, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
R08 = HERE.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = R08.parent / 'r07' / 'r07.md'
bl = sr.blocks(MD.read_text(encoding='utf-8'))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-r07-20261104/articles/healing-the-gut/humanize/fix-20261103/'
draft = (R08 / 'stacks' / 'DRAFT-SECTION.md').read_text(encoding='utf-8')
paras = [b.strip() for b in draft.split('\n\n') if b.strip() and not b.startswith('#') and not re.match(r'\d\. ', b)]
P1, HIS, KITS, P80, P81A, P81B = paras
CAU = (R08 / 'stacks' / 'CAUTION-DRAFT.txt').read_text(encoding='utf-8').strip()
WEB = {}
for f in ('RESULTS-paras-webapp.json', 'RESULTS-paras-2-webapp.json'):
    WEB.update(json.loads((R08 / 'checks' / f).read_text(encoding='utf-8')))
SEC = json.loads((R08.parent / 'r07' / 'checks' / 'RESULTS.json').read_text(encoding='utf-8'))['r07-stacks-section']


def web(k, what=''):
    h, ai, words, wins, _, uuid, _flag = WEB[k]
    short = {'Human Written': 'Human', 'AI Generated': 'AI', 'AI Detected': 'AI Detected'}.get(h, h)
    conf = '; '.join(w.strip().replace('AI-Generated', 'AI').replace(', ', ' ', 1).rsplit(', ', 1)[0] for w in wins.split(';'))
    return '%s[%s](https://www.pangram.com/history%s) (%d words: %s)' % (what, short, uuid, words, conf)


def sec(what='The whole section by itself, before: '):
    c = ', '.join('%s %s' % ('Human' if w['label'].startswith('Human') else 'AI', w['confidence']) for w in SEC['windows'])
    return '%s[AI, %d%% human](%s) (%s)' % (what, round(100 * SEC['fraction_human']), SEC['link'], c)


def find(start):
    i = [b['i'] for b in bl if b['text'].startswith(start)]
    assert len(i) == 1, start
    return i[0]


def card(sid, typ, title, block, after, what, why, stays, deciding, tested, reading, advice='approve', note='Approve, or Revise.'):
    before = bl[block]['text']
    return {'id': sid, 'type': typ, 'title': title, 'advice': advice,
            'spans': [{'block': block, 'start': 0, 'end': len(before)}],
            'edits': [{'block': block, 'before': before, 'after': after}], 'reads': [{'text': after, 'kind': 'p'}],
            'reads_label': 'As it would read', 'what': what, 'why': why, 'stays': stays, 'deciding': deciding,
            'advice_note': note, 'tested': tested, 'reading': reading}


ASK = ("I can't find any more AI tells here, and I see some human tells, like these: %s. Can you help show me the tells I'm "
       "missing?")
p1, his, items, kits = find("I don't think there's one supplement stack"), find('That said, some people want'), None, find('Gemini suggested these kits')
p80, p81, cau = find("You'll also find"), find('Start with low doses, especially'), find('CAUTION: cancer cells')
HIS_SUG = ('That said, some people want a ready-made stack rather than buying every ingredient for it separately. So, if I '
           'were to recommend a general "repair and rebuild" stack, I\'d want three things in it: a probiotic you tolerate '
           'well, to put good bacteria back; a prebiotic to feed them, which they turn into butyrate, the short-chain fatty '
           'acid your colon cells run on (see Leaky gut, above), or else butyrate itself; and something to help repair the gut '
           'lining, like glutamine, zinc carnosine, colostrum, or herbs that coat it, such as slippery elm and marshmallow root.')
S = [
 card('F6-1', 'point', 'The stacks section opens with what a stack is for', p1, P1,
      'Your opener stays, with "(a set of supplements you take together)" in brackets the way you define terms; then "no '
      'stack can do the phases above for you", the phases pointed back to instead of recapped, and where a stack fits: the '
      'rebuilding in Phase 5, once you\'re clear of infection.',
      'In its own check the whole section read AI, this paragraph included, though it had read Human (High) by itself. A '
      'newcomer read asked, in this order: what a stack is and whether it replaces the phases; the order of what; where a '
      'stack goes; and why the next paragraph feeds the bacteria when Phase 2 starves them. Phase 5 answers the last one. My '
      'first try answered them as an explainer, a definition sentence and the phases recapped with their numbers, and read '
      'AI; this one points back, as you said to (E349).',
      'Your opener, and the point that bugs come last.', 'Whether the Phase 5 point is right: it\'s mine, from Phase 5\'s own words.',
      web('r08b-p1', 'By itself: ') + '. ' + web('r08-p1', 'My first try: '), sec()),
 {'id': 'F6-2', 'type': 'voice', 'title': 'Your three categories: my suggestion, your call', 'advice': 'edit',
  'spans': [{'block': his, 'start': 0, 'end': len(bl[his]['text'])}],
  'reads': [{'text': HIS_SUG, 'kind': 'p'}],
  'why': 'With the kits after it, this read AI: the lead-in and first item AI High, the other two items AI Low (' +
         web('r08-kits-with-categories').split(' (')[0] + '). All three panel readers agree on three tells here: the '
         'announced "three categories:" with First/Then/Other, "or similar compounds", and "butyrate ... especially the main '
         'one, butyrate" ([panel](' + GH + 'r08/stacks/panel/PANEL.md)). A newcomer asked what a "probiotic system" is, why '
         'butyrate sits under feeding the probiotics (it feeds your colon cells, not the bacteria), and which herbs '
         '"mucosal-support herbs" means ([reader](' + GH + 'r08/stacks/links/READER.md)). My suggestion answers those with '
         'your Leaky gut item\'s own point, that the bacteria make butyrate from what they ferment, and names two herbs that '
         'are in GI Revive. Not checked: this paragraph has one try left, so I\'d save it for your wording.',
  'advice_note': 'Keep yours, take mine, or write your own with Edit. Yours as it is now:\n' + bl[his]['text'],
  'reading': web('r08-kits-with-categories', 'Yours with the kits: ')},
 card('F6-3', 'help', 'The kits: which category each covers', kits, KITS,
      '"three kits" for "these kits", the best general one first, and what each kit has in it, from the makers\' pages '
      '([Total Gut Restoration](https://fullscript.com/catalog/products/total-gut-restoration-kit-1): a probiotic, a prebiotic '
      'and a mucosal product; [Ruscio\'s kit](https://store.drruscio.com/products/leaky-gut-support-kit): a probiotic, a '
      'lining formula and L-glutamine, no prebiotic; [GI Revive](https://www.priceplow.com/designs-for-health/gi-revive): '
      'lining nutrients and herbs, no probiotic or prebiotic).',
      'A newcomer asked: complete in what way, what "the rest of a gut protocol" is, and why the best one comes last. Mapping '
      'each kit to your three categories answers all three. With your categories before it, the first two sentences read '
      'Human (High, then Low) and the Ruscio and GI Revive sentences read AI High; it has one try left. ' + ASK % (
          '"Gemini suggested three kits to me, but so far they\'re the best ones I\'ve seen, tho I haven\'t used them myself, '
          'so check the reviews", "so you\'d still need a probiotic and a prebiotic with it"'),
      'Your Gemini sentence, and every kit.', 'What reads AI in the Ruscio and GI Revive sentences.',
      web('r08-kits-with-categories', 'With your categories: '), sec(), advice='edit',
      note='Rewrite it from "Dr. Ruscio\'s" with Edit, or tell me what to change. It has to keep: Total Gut Restoration has '
           'all three; Ruscio\'s has a probiotic and two lining products but no prebiotic, so it\'s more for leaky gut; GI '
           'Revive is only the lining part.'),
 card('F6-4', 'point', 'The cleanse stacks, following your Phase 3', p80, P80,
      'They\'re like Phase 3\'s herbal antibiotics, so only for when diet didn\'t clear your symptoms, and even then you\'d '
      'mostly skip them for H2O2; H. pylori explained from your Parasites item; berberine taken on its own.',
      'A newcomer asked whether these stacks are fine once you reach Phase 3, since Phase 3 says to "AVOID most herbal '
      'antibiotics". My earlier wording sent them to Phase 3 as if Phase 3 recommends them. This follows your own Phase 3: '
      '"H2O2 actually works better than the herbal antibiotics", and berberine is the one that works for H. pylori.',
      '"They kill bugs", the herbs, and your berberine advice.', 'Whether "take it on its own, not in a cleanse stack" says what you mean.',
      web('r08-p80', 'By itself: '), sec()),
 card('F6-5', 'help', 'Start low, and when to see a doctor', p81, P81A + '\n\n' + P81B,
      'Start low with its reason (the gas is what the bacteria make from the prebiotic), then the conditions split by what '
      'they call for, every one kept, with reasons for two: probiotics are live bacteria that can be risky with a weak '
      'immune system ([NCCIH](https://content.govdelivery.com/accounts/USNIHNCCIH/bulletins/378abdf)); pregnant women '
      'should avoid goldenseal, whose berberine can cause or worsen jaundice in newborns '
      '([NCCAM](https://webarchive.library.unt.edu/web/20121017011343/http://nccam.nih.gov/health/goldenseal)).',
      'Three versions read AI: r07\'s in the section (one AI High window), and my two today by themselves (AI High). All '
      'three panel readers named the red-flag list with its stock "see a clinician" ending, and the linter flags it as '
      'safety language (your rule of 2026-10-23). I kept every condition, because they\'re safety points I shouldn\'t drop '
      'to pass. ' + ASK % ('"(berberine isn\'t safe then)", "The prebiotic part especially can give you gas at first"') +
      ' Or, if some of the list can go, which?',
      'Every condition, and working it out with a doctor instead of putting a stack together yourself.',
      'What reads AI, or which conditions you\'d cut.',
      web('r08c-p81', 'By itself: ') + '. ' + web('r08-p81', 'My first try today: '), sec(), advice='edit',
      note='Rewrite it with Edit, or tell me which conditions can go. It has to keep: start low and build up; see a doctor '
           'first for bleeding, fast weight loss, bad pain, a fever or dehydration; work out what to take with your doctor '
           'if you\'re pregnant, your immune system is weak, or you have an IBD flare, cancer or another serious illness.'),
 card('F6-6', 'point', 'Glutamine\'s caution: why the liver', cau, CAU,
      'The last sentence says why the portal vein matters: the gut\'s blood goes straight to the liver, so a big dose reaches '
      'it before anywhere else.',
      'Checked with the dosing paragraph before it, the liver sentence was the one Low window ([Human, Low](' +
      'https://www.pangram.com/history/ba5e7a60-4ff8-4b53-af00-beb38c1c6607)); a newcomer would ask why going there first '
      'matters. By itself my version read Human, but the whole paragraph as one Low window, so it isn\'t clearly better yet: '
      'checked by itself it lost the dosing paragraph it leans on (E349).',
      'Every word but the end of the last sentence.', 'Whether the reason is right and worth the words.',
      web('r08-caution', 'By itself: '), None),
]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b6-stacks-20261104',
    'title': 'Gut Stacks, Before the Article Check',
    'intro': ['Your point of 14:41 UTC, put in: the stacks section\'s windows get fixed before the whole article is checked '
              'again. By itself the section read AI (5% human, 12 of its 13 windows AI), your paragraphs\' windows included. '
              'A newcomer read and three fresh readers found what to fix; every change passed the blind meaning check.',
              'Two of mine now read Human (High) by themselves (F6-1, F6-4). The kits, the start-low paragraph and the caution '
              'still read AI or Low, so those ask your help, and your three-category paragraph has my suggestion. The section '
              'goes to a check of its own once these are settled, and the article after that.',
              'Two rules came from your messages: the browser I drive isn\'t your Brave unless you say it is (E353), and an '
              'article check now waits until the windows we can see are fixed (E354, enforced in the ledger).'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r08/b6/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r07/r07.md', 'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-04',
    'links': {'guide': GH + 'r08/r08.md', 'review': GH + 'r08/b6/REVIEW-CARDS.md'},
    'types': {'point': {'label': 'A changed point', 'about': 'Checked, with the reason'},
              'voice': {'label': 'Your words', 'about': 'My suggestion, your call'},
              'help': {'label': 'Your help', 'about': 'Faithful rewrites still read AI'}},
    'suggestions': S,
}
for s in S:
    if s['advice'] == 'edit':
        mine = s['reads'][0]['text']
        s['advice_note'] = s['advice_note'] + '\n\n' + ('My suggestion:\n' if s['type'] == 'voice' else 'My version, now in r08:\n') + mine
        for k in ('edits', 'reads', 'reads_label'):
            s.pop(k, None)
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s.get('reads'):
        out += ['**%s:**' % s['reads_label'], '', '> ' + s['reads'][0]['text'].replace('\n\n', '\n>\n> '), '']
    if s.get('tested'):
        out += ['**Pangram:** ' + s['tested'], '']
    if s.get('what'):
        out += ['**What changed:** ' + s['what'], '']
    out += ['**Why:** ' + s['why'], '', '**What I\'d like:** ' + s['advice_note'].replace('\n', '\n\n'), '']
    if s.get('reading'):
        out += [s['reading'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
