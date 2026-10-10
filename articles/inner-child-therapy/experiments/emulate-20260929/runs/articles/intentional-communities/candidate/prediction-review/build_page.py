#!/usr/bin/env python3
"""Build the prediction-miss review page (2026-10-10) from the lane's own records.

Inputs: rows4.json (every prediction row of PREDICTIONS-s2..s10 joined to its checked text; made by parse_preds.py,
join_texts.py and join2.py in this folder), the blind test's key and answers, and pairs-key.json. Every number on the
page is computed here from those files; the commentary is mine.
Usage: python3 build_page.py <rows4.json>
"""
import html, json, re, sys, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CAND = os.path.dirname(HERE)
rows = json.load(open(sys.argv[1]))
by = {r['id']: r for r in rows if r.get('body')}
E = html.escape

sc = [r for r in rows if r['res'] in ('Human', 'AI', 'Mixed', 'MostlyHuman') and r['mine'] in ('Human', 'AI', 'Mixed')]
def passed(r): return r['res'] == 'Human'
def right(r): return (r['mine'] == 'Human') == passed(r)
def stats(sel):
    n = len(sel); ok = sum(right(r) for r in sel); p = sum(passed(r) for r in sel)
    return n, ok, p, max(p, n - p)
def pct(a, b): return f"{round(100 * a / b)}%"

secs = [('Sections 2 to 10', sc)] + [(f'Section {s[1:]}', [r for r in sc if r['sec'] == s]) for s in ('s7', 's8', 's9', 's10')]
said = collections.Counter((r['mine'], passed(r), r['res']) for r in sc)
def said_n(m): return sum(v for (mm, p, res), v in said.items() if mm == m)
def said_pass(m): return sum(v for (mm, p, res), v in said.items() if mm == m and p)
mixed_ai = sum(v for (mm, p, res), v in said.items() if mm == 'Mixed' and res == 'AI')
s10c = [r for r in sc if r['sec'] == 's10' and 189 <= int(re.match(r'(\d+)', r['id']).group(1)) <= 198 and r['mine'] != 'Mixed']

# blind test
key = {k['n']: k for k in json.load(open(os.path.join(HERE, 'blind-test-holdout-key.json')))}
def load(names):
    d = {}
    for f in names:
        for e in json.load(open(os.path.join(HERE, f))): d[e['n']] = e
    return d
plain = load(['blind-test-pred-plain-A.json', 'blind-test-pred-plain-B.json'])
check = load(['blind-test-pred-check-A.json', 'blind-test-pred-check-B.json'])
def bscore(fn):
    ok = sum((fn(n) == 'Human') == (k['res'] == 'Human') for n, k in key.items()); return ok, len(key)
bt = [("My calls at the time (written before each check, with the section's history in view)", bscore(lambda n: 'Human' if key[n]['mine'] == 'Human' else 'AI')),
      ("A fresh reader (Sonnet), its own judgment", bscore(lambda n: plain[n]['pred'])),
      ("The same reader with my tells checklist", bscore(lambda n: check[n]['pred'])),
      ("Always saying AI", bscore(lambda n: 'AI'))]
check_h = sum(1 for e in check.values() if e['pred'] == 'Human')
bt_pass = sum(k['res'] == 'Human' for k in key.values())
pairs = json.load(open(os.path.join(HERE, 'pairs-key.json')))

def res_short(r):
    t = re.sub(r'\*', '', r['res_raw'])
    t = re.sub(r',\s*\d\d:\d\d(:\d\d)?', '', t)
    return t.strip()
def where(r):
    return f"section {r['sec'][1:]}, {r['id']}"
def text_html(t, flag=None):
    out = []
    for p in [p for p in t.split('\n\n') if p.strip()]:
        h = E(p.strip())
        if flag:
            for f in flag:
                fe = E(f)
                if fe in h: h = h.replace(fe, f'<span class="flag">{fe}</span>')
        out.append(f'<p>{h}</p>')
    return ''.join(out)

# ---- the examples (ids, what I see now, why I got it wrong); texts and results come from the records ----
H2AI = [
  ('187g-P3b1P4c', None, None,
   'I see the need to spread healing practices, train people and seed new projects. It\'s also important to keep any one comfortable enclave from forgetting that it isn\'t the whole movement.',
   '"I see the need to" and "It\'s also important to" are stock lines a model uses to announce a point, with a list of three and "keep … from forgetting that it isn\'t". The first paragraph (P3b1) had passed alone, though it carries "the boring problem" and the "nicer logo" quip.',
   'I went by where it came from. Emulate is the humanizer, so I treated its output as human, but its output has stock lines of its own.'),
  ('188g-P6g', None, None, None,
   'Three stock connectives in one paragraph ("One thing to notice about", "Related to this", "and not just in theory"), "quietly turn into", and an eight-item list after "that means".',
   'Same as above: it came from Emulate, so I said Human.'),
  ('168g-P13k4', None, None, None,
   'Questions the paragraph answers itself ("…? Yes.", "So what do they show? That …"), "sure. But", and nouns doing the work with no one acting ("major necessities and public functions can be taken out of ordinary market purchase and governed collectively").',
   'I counted "Now,", "sure" and "Yes." as speech. This paragraph went through eight versions (166g to 169g); I said Human every time and every one read 100% AI. The project\'s own rule already says rhetorical questions and informal markers aren\'t humanization switches. I treated them as switches.'),
  ('147g-pub-P1P2P3', None, None, None,
   'Two polished quips ("a nice combination when you\'re trying to visit a revolution", "apparently the empire had questions") and four questions in an even row.',
   'I went by "it\'s your own story". I even wrote down that the quip read polished, and still said Human. Your published draft was AI-assisted, and the true story didn\'t outweigh the quips.'),
  ('185g-P3a', None, None, None,
   'The three you flagged this morning: "the boring problem", the stock quip "with a nicer logo", and "I don\'t want … / I\'d like …" opening the stance.',
   'I let one spoken-sounding word ("I\'d like" for the published "I want") outweigh three tells.'),
  ('196g-P8v', ['When you have to deal with a collision of two principles, don\'t only store the rule. Store the hard case too: what happened, the principles that actually conflicted, your first judgments, and your final decision and rationale.'], None, None,
   'Pangram flagged its first two sentences. The only change from the version that passed (195g-P8t) was the opening: "When you create a rule to deal with" became "When you have to deal with". The correction pair ("don\'t only store the rule. Store the hard case too") is in the passing versions too, so it isn\'t what decided this.',
   'I assumed a paragraph that passed would keep passing after a small meaning fix.'),
  ('191g-P34n1', None, None, None,
   'Identical to P34m, which passed, except "I\'d like them to connect, help each other and move people …" lost "connect,". P34m already carried "the boring problem", the "nicer logo" quip, "but also to stay distinct enough that …" and a four-item list after a colon.',
   'A paragraph that passes while carrying that many tells sits right on the line, and any edit can tip it. I treated its pass as safe.'),
]
AI2H = [
  ('185g-P1a', 'Loose, spoken phrasing ("everybody goes out and buys new land right away") and a concrete sequence of steps.',
   'I predicted from my record (my first rewrites in section 9 had mostly read AI), not from the words.'),
  ('186g-P7b1', 'The list items are uneven and concrete ("a vehicle or a tool on loan", "a visit that\'s mainly for training or relationship building"), and the sentences around the list change shape.',
   'I called it AI for one feature, a list after a colon.'),
  ('193g-P6k', 'Loose wording around it: "Friends who may just want to stay friends", "the freedom to move is just decorative", "for it to work". The P6 that opened the same way and read AI (185g-P6a) had "Often the answer is a thin interface that says who\'s responsible … without making every internal system match."',
   'I called it AI for "quietly" and "similarly practical". One word doesn\'t decide Pangram. You were still right to cut "quietly": readers notice it.'),
  ('147g-pub-P4', 'Concrete first-person events: basketball with Zapatista youth, translating for your friends "because my Spanish was better".',
   'I called it AI for one formal phrase at the end ("to make the communities less easy to attack in silence").'),
  ('192g-D1top12', 'Section 10\'s top with both headings, P1a and P2b2.',
   'I blamed the stacked headings for a window that turned out to be in P34m.'),
]
PAIRS = [  # (passed wording, failed wording, result, where)
  ('tools or a little money; tools or a small stash', 'tools or a small reserve', 'AI 100%', 'section 8, P25 (131g, 135g / 133g, 134g)'),
  ('quietly lord it over the younger ones; quietly boss the younger ones around', 'quietly dominate the younger ones', 'AI 100%; Mixed 63%', 'section 8, P13 (129g, 134g / 133g)'),
  ('Keep everyone safe first, right away, then make sure', 'Keep whoever\'s at risk safe first; Safety comes first, right away. Then make sure', 'AI 100%', 'section 8, P19 (127g, 134g / 133g, 134g, 137g)'),
  ('a … confused kid may tell it wrong; may tell it badly; may get mixed up telling it', 'may not tell the story perfectly', 'AI 100%', 'section 8, P18 (129g, 130g, 133g / 129g)'),
  ('Adults can go on about their intentions', 'Adults can talk about their intentions', 'Mixed 40%', 'section 8, P3 (129g)'),
  ('but the kids might have something to say', 'but the kids who lived it / who lived through it / who grew up in it might have something', 'AI 100%', 'section 8, P3 (129g, 130g)'),
  ('it\'s an outsider\'s view of the Ye\'kuana … idealizing them', 'it\'s one outsider\'s interpretation of the Ye\'kuana … idealizing what she saw', 'Mixed 41%', 'section 8, P8 (95g / 97g)'),
  ('no one exhausted parent is expected … can recreate some of this', 'a single exhausted parent isn\'t expected … can imitate some of this', 'AI-assisted 100%', 'section 8, P8 (95g / 97g)'),
  ('Kids also need a good set of transferable skills … good relationships', 'Kids also need transferable skills … relationships', 'Mixed 66%', 'section 8, P25 (130g / 129g)'),
  ('one plausible next step outside the community (school, work, family, another community)', 'one plausible next step (school, work, family, or another community)', 'AI 100%; Mixed 66%', 'section 8, P25 (130g, 131g / 129g)'),
  ('and others will start their own', 'and that others will start; and others may start', 'Mixed 39%', 'section 8, P26 (131g, 135g / 134g, 135g)'),
  ('the closest thing to a whole example that I found', 'the closest whole example I found', 'AI 100%', 'section 9, P7 (168g, 169g)'),
  ('can come out of ordinary market purchase and be governed collectively', 'can be taken out of / pulled out of ordinary market purchase and governed collectively', 'AI 100%', 'section 9, P13 (167g, 170g, 176g)'),
  ('One thing the Zapatistas have been clear about … The useful thing isn\'t their diagram, though. It\'s how they learn', 'One thing the Zapatistas themselves have been clear about … The useful thing isn\'t their diagram. It\'s how they learn', 'AI 100%', 'section 9, P12 (151g / 157g)'),
  ('When you create a rule to deal with a collision; When you create or apply a rule to deal with', 'When you have to deal with a collision; Whenever you use a rule to settle a collision', 'Mixed 45%; AI 100%', 'section 10, P8 (195g, 197g / 196g, 197g)'),
  ('I\'d like them to connect, help each other and move people', 'I\'d like them to help each other and move people', 'AI 100%', 'section 10, P34 (188g / 191g)'),
  ('if it becomes a business', 'if it becomes a visitor business', 'AI 100%', 'section 9, P15 (150g, 151g / 151g)'),
]

css = open(os.path.join(CAND, 'community-section10-side-by-side.html')).read().split('<style>')[1].split('</style>')[0]
css += """
.tbl{width:100%;border-collapse:collapse;font:14px/1.45 system-ui,sans-serif;margin:8px 0 4px}
.tbl th,.tbl td{border-top:1px solid var(--line);padding:6px 10px 6px 0;vertical-align:top;text-align:left}
.tbl th{font-weight:600;color:var(--mute)} .num{text-align:right;white-space:nowrap}
.exh{font:600 13px/1.4 system-ui,sans-serif;color:var(--mute)}
.ex{margin:16px 0} .ex .card p{margin:.4em 0} .k{font:600 13px/1.3 system-ui,sans-serif;color:var(--mute);margin-top:10px}
.say{font:15px/1.5 system-ui,sans-serif;margin:.3em 0}
.pass{background:rgba(70,170,90,.16);border-radius:3px;padding:0 2px} .fail{background:var(--flag);border-radius:3px;padding:0 2px}
@media (max-width:760px){.tbl{font-size:13px}.tbl th.num{white-space:normal}.tbl td,.tbl th{padding-right:6px}}
.tbl td{overflow-wrap:anywhere}
"""
P = []
a = P.append
a('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
  '<title>Prediction misses</title><style>' + css + '</style></head><body><main>')
a('<h1>What I got wrong predicting Pangram</h1><p class="meta">Community article · sections 2 to 10 · review of my predictions, 2026-10-10</p>')
a('<p class="intro">You asked for the examples I got wrong: what tells I noticed, and why I said Human when it was AI and the other way around. '
  'Below: the numbers, the misses in both directions with the text, pairs of near-identical texts where one passed and one didn\'t, '
  'a blind test of the tells I could name, and what I\'m changing.</p>')

# numbers
a('<h2>The numbers</h2>')
a('<p class="intro">"Right" means pass or no pass: a Human call is right when the text came back 100% Human, and an AI or Mixed call is right when it didn\'t. '
  'For comparison, the last column is how often saying "AI" every time would have been right.</p>')
a('<table class="tbl"><tr><th></th><th class="num">checks</th><th class="num">my call right</th><th class="num">passed</th><th class="num">always "AI" right</th></tr>')
for name, sel in secs:
    n, ok, p, maj = stats(sel)
    ai_only = n - p
    a(f'<tr><td>{E(name)}</td><td class="num">{n:,}</td><td class="num">{pct(ok, n)}</td><td class="num">{pct(p, n)}</td><td class="num">{pct(ai_only, n)}</td></tr>')
a('</table>')
hn, hp = said_n('Human'), said_pass('Human'); an, ap = said_n('AI'), said_pass('AI'); mn, mp = said_n('Mixed'), said_pass('Mixed')
ok10 = sum(right(r) for r in s10c)
a(f'<ul class="notes"><li>When I said Human, {hp} of {hn:,} passed ({pct(hp, hn)}). When I said AI, {ap} of {an} passed ({pct(ap, an)}). '
  f'When I hedged with "Mixed" ({mn} times), {mp} passed and {mixed_ai} read 100% AI.</li>'
  f'<li>Batches 189g to 198g, the ones I reported this morning: {len(s10c)} calls of Human or AI, {ok10} right. (This morning I wrote 25 of 62, counting the "Mixed" calls.)</li>'
  '<li>The 25 out of 25 from before was a different thing: the reviewer catching AI in your published paragraphs on 9-28. Those read 100% AI, and fully AI text is easy to spot. '
  'My rewrites sit near the line, where one word can decide it, and that\'s where my calls go wrong.</li></ul>')

def example(r, flag=None, excerpt=None, now='', why=''):
    s = [f'<div class="ex"><div class="card"><div class="exh">{E(where(r))} · I said {E(r["mine_raw"])} · Pangram: {E(res_short(r))}</div>']
    s.append(text_html(r['body'], flag))
    s.append(f'<div class="k">What I wrote then</div><p class="say">{E(r["why"] or "(no reason written)")}</p>')
    s.append(f'<div class="k">What I see now</div><p class="say">{E(now)}</p>')
    s.append(f'<div class="k">Why I got it wrong</div><p class="say">{E(why)}</p></div></div>')
    return ''.join(s)

a('<h2>I said Human, it came back AI</h2>')
for i, flag, _x, _y, now, why in H2AI:
    a(example(by[i], flag, None, now, why))
a('<h2>I said AI, it came back Human</h2>')
for i, now, why in AI2H:
    a(example(by[i], None, None, now, why))

a('<h2>One small change apart</h2>')
a(f'<p class="intro">In sections 7 to 10 there are {len(pairs)} pairs of near-identical texts where one passed and the other didn\'t, most of them differing by one to five words. '
  'These show what Pangram reacts to better than anything I could list. Some of them:</p>')
a('<table class="tbl"><tr><th>passed</th><th>didn\'t pass</th><th>result</th><th>where</th></tr>')
for p_, f_, res, wh in PAIRS:
    a(f'<tr><td><span class="pass">{E(p_)}</span></td><td><span class="fail">{E(f_)}</span></td><td>{E(res)}</td><td>{E(wh)}</td></tr>')
a('</table>')
a('<ul class="notes"><li>In most of these, the version that failed is the tighter, more exact, more formal or more hedged one ("a small reserve", "dominate", "whoever\'s at risk", "may not tell the story perfectly", "one outsider\'s interpretation"). '
  'The version that passed is looser and plainer ("a little money", "lord it over", "everyone", "tell it wrong", "an outsider\'s view").</li>'
  '<li>Several of the failing versions were my own meaning fixes, which made a sentence more exact ("whoever\'s at risk", "the kids who lived it", "alone", "visitor business" put back from the published text).</li>'
  '<li>The tells I could name sit on both sides. "Don\'t only store the rule. Store the hard case too" is in the P8s that passed and in the ones that didn\'t, and so is "isn\'t what it\'s for. It\'s for" in P15. '
  'The last two rows don\'t fit any rule I can see: near the line, a word anywhere can tip it.</li>'
  f'<li>The full list of {len(pairs)} pairs is in <code>prediction-review/pairs-with-diffs.md</code>.</li></ul>')

a('<h2>A blind test of the tells</h2>')
a(f'<p class="intro">To check whether the tells I learned from sections 9 and 10 predict Pangram, I gave {len(key)} texts from sections 7 and 8 to a fresh reader, without the results '
  f'({bt_pass} of them had passed). It read them once on its own judgment and once with my checklist of tells (<code>prediction-review/blind-test-CHECKLIST-v1.md</code>).</p>')
a('<table class="tbl"><tr><th></th><th class="num">right</th></tr>')
for name, (ok, n) in bt:
    a(f'<tr><td>{E(name)}</td><td class="num">{ok} of {n} ({pct(ok, n)})</td></tr>')
a('</table>')
a(f'<ul class="notes"><li>With the checklist the reader said Human only {check_h} times: nearly every text had two or more of the tells, so the checklist said AI. Tells like lists, quips and correction pairs are everywhere in this prose, in passing and failing texts alike.</li>'
  '<li>So the tells you flag still matter for readers, and I keep cutting them. But they don\'t predict Pangram well. The word-level looseness in the pairs above is the better guide.</li>'
  '<li>I meant to have a second blind reader judge which version of each pair is looser, to test that pattern without me seeing the answers. The account hit its usage limit at 15:20 UTC, so that check didn\'t run.</li></ul>')

a('<h2>What changes</h2><ul class="notes">'
  '<li>I predict from the words, never from where a text came from (Emulate, my own fix, your published draft) or from my record.</li>'
  '<li>Loose and plain reads human; tight, exact, formal or hedged reads AI. When a meaning fix adds precision ("whoever\'s at risk", "alone", "who lived it"), I look for the plain way to say the same thing before the check.</li>'
  '<li>Speech markers don\'t cancel AI shapes. A question the text answers itself, "sure. But", and Emulate\'s stock lines ("I see the need to", "It\'s also important to", "One thing to notice about") count against a text.</li>'
  '<li>One feature in loose, concrete prose (a list, "quietly", a heading) doesn\'t make me say AI. Your tells still get cut for readers.</li>'
  '<li>A paragraph that passes while carrying several tells is fragile. After any edit to it I expect AI until it\'s checked.</li>'
  '<li>Some of this can\'t be predicted: near the line, one word flips it. I\'ll keep scoring every call, and section 11 is the first test of this way of predicting. Its score goes next to "always AI" when the section is done.</li></ul>')
a('<p class="meta">Built by <code>prediction-review/build_page.py</code> from the predictions records of sections 2 to 10 (<code>prediction-review/all-calls.csv</code> has every scored call).</p>')
a('</main></body></html>')
open(os.path.join(CAND, 'community-prediction-misses.html'), 'w').write(''.join(P))
print('ok', len(''.join(P)))
for name, (ok, n) in bt: print(name, ok, n)
