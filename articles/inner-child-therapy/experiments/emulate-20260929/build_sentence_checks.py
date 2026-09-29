#!/usr/bin/env python3
"""Builds the sentence checks (put-backs, controls, fixes) for GPT to paste into Pangram.
Written by Claude, 2026-09-29. Run from the experiment folder:
    python3 build_sentence_checks.py
Every splice is exact: spans are cut from the saved files by start/end markers, and the
script fails if a marker is missing or ambiguous. Nothing here is article prose."""
import json, hashlib, os, re, sys
EXP = os.getcwd()
OUTDIR = 'runs/sentence-checks'
os.makedirs(OUTDIR, exist_ok=True)
def rd(p): return open(os.path.join(EXP, p), encoding='utf-8').read().strip()
def seg(text, start, end):
    i = text.find(start)
    assert i >= 0 and text.find(start, i + 1) < 0, ('start marker', start)
    j = text.find(end, i)
    assert j >= 0, ('end marker', end)
    return text[i:j + len(end)]
def once(text, old, new):
    assert text.count(old) == 1, ('not exactly once', old[:60])
    return text.replace(old, new)
A = 'inputs/learning/A_joelfixes/'; B = 'inputs/learning/B_protector/'; E = 'runs/emulate/'
checks = []
def add(cid, kind, question, text, src, note, span_from=None, span_to=None):
    assert len(text.split()) >= 50, (cid, len(text.split()))
    path = f'{OUTDIR}/{cid}.txt'
    open(os.path.join(EXP, path), 'w', encoding='utf-8').write(text + '\n')
    checks.append(dict(check_id=cid, variant='splice' if kind == 'putback' else ('edit' if kind == 'fix' else 'control'),
        kind=kind, question=question, text_file=path, words=len(text.split()),
        sha256=hashlib.sha256((text + '\n').encode()).hexdigest(), sources=src, note=note,
        replaced=span_from, inserted=span_to))

# ---------- 1. PUT-BACKS: one of Claude's draft sentences back into a passing Emulate output ----------
Q1 = 'Does this sentence of Claude’s bring the AI verdict back inside otherwise Human text?'
def putbacks(pair, out_file, draft_file, units):
    out, dr = rd(out_file), rd(draft_file)
    for n, (e_start, e_end, s_start, s_end, label) in enumerate(units, 1):
        e_span = seg(out, e_start, e_end); s_span = seg(dr, s_start, s_end)
        add(f'putback-{pair}-{n:02d}', 'putback', Q1, once(out, e_span, s_span),
            [out_file, draft_file], label, e_span, s_span)

putbacks('A08', E+'gpt_A08_api_r1.txt', A+'A08_before.txt', [
 ('Do whatever', 'safety related).', 'Handle whatever', 'needs doing.', 'opening instruction'),
 ('At the start of the next round', 'since you were last here?', 'Then, before another round', 'you processed this.', 'ask what changed'),
 ('Has something come up that allows', 'unsure of your last answer?', 'Did you finally feel', 'certain enough?', 'three questions in a row'),
 ('Grief does often', 'something new.', 'Grief can come back', 'a new request.', 'closing principle (two sentences)'),
])
putbacks('A10', E+'gpt_A10_api_r1.txt', A+'A10_before.txt', [
 ('NB I’ve developed', 'is my own):', 'I developed this practical map', 'is my own:', 'intro'),
 ('child on her own', 'external safety', 'The child alone:', 'safety to begin.', 'list item 1'),
 ('child with borrowed adult', 'symbolic figure', 'The child with a borrowed adult:', 'symbolic figure.', 'list item 2'),
 ('adult as apprentice', 'looking after the child', 'The adult apprentice:', 'at least one part yourself.', 'list item 3'),
 ('adult in her own right', 'protection and direction', 'The inner adult:', 'familiar enough to summon.', 'list item 4'),
 ('adult in relation to child', 'managing life', 'The adult and child in relationship:', 'the whole life alone.', 'list item 5'),
 ('The child doesn’t need to stop', 'becoming an adult…’', 'You don’t have to stop being the child.', 'the adult who stays.”', 'closing (three sentences)'),
])
putbacks('A12', E+'gpt_A12_api_r1.txt', A+'A12_before.txt', [
 ("Sometimes you'll notice you're hooked", 'doing the hooking.', 'You might notice the hook', 'doing the hooking.', 'opening sentence'),
 ("Sometimes you won't notice it", 'for example.', 'Or you might notice it embarrassingly late.', 'observing yourself.', 'the jaw/stomach sentence Joel changed, as Claude wrote it'),
 ("It's okay to forget", 'which part it is.', 'Maybe forget the parts detective work', 'figure that out later.', 'forget the detective work (two sentences)'),
 ('Just be aware, as Pema', 'She calls this shenpa .', 'Pema Chödrön calls', '"shenpa."', 'shenpa sentence'),
])
# A12 extra: the same slot with Joel's version of the sentence he changed
out, joel = rd(E+'gpt_A12_api_r1.txt'), rd(A+'A12_joel_after_REFERENCE_ONLY.txt')
e_span = seg(out, "Sometimes you won't notice it", 'for example.'); j_span = seg(joel, 'Or you might notice it embarrassingly late.', 'observing yourself.')
add('putback-A12-02j', 'putback', 'Same slot as putback-A12-02, with Joel’s one-clause change: does his change matter inside Human text?',
    once(out, e_span, j_span), [E+'gpt_A12_api_r1.txt', A+'A12_joel_after_REFERENCE_ONLY.txt'], 'Joel’s fixed version of the jaw/stomach sentence', e_span, j_span)
putbacks('A14', E+'gpt_A14_api_r1.txt', A+'A14_before.txt', [
 ('Later on, when you’re feeling good', 'felt like a violation.', 'Later, ask the fun question:', 'what actually happened?', 'the sentence Joel deleted'),
 ('Maybe they did do something', 'something in you.', 'Somebody may really have crossed', 'something old in you.', 'boundary sentence'),
 ('But you don’t have to figure it out now', 'actually evil or not.', 'You felt your stomach tighten up', 'in your happy place.', 'closing (two sentences)'),
])
putbacks('A18', E+'gpt_A18_api_r1.txt', A+'A18_before.txt', [
 ('Even if you do n', 'a sentence to say to him.', 'You might barely have', 'Try it and see.', 'opening (two sentences)'),
 ('If you do, use those words', 'in your imagination.', 'If words are there', 'imaginary-conversation zone.', 'use the words'),
 ('But if this feels like homework', 'song lyrics, etc.)', 'And if that starts feeling like homework', 'suddenly feels relevant.', 'homework + list of signals (two sentences)'),
 ('Or you may not get any response', 'loving thing to say to him.', 'Sometimes nothing', 'what would be kind.', 'closing of paragraph 1'),
 ('It may or may not be possible', 'understand the feeling.', 'The order gets murky too.', 'which happened first.', 'order gets murky (two sentences)'),
 ('But that does n', 'understand your feelings.', "I don't think you need", 'help you understand it.', 'closing of paragraph 2'),
])
putbacks('B07', E+'gpt_B07_api_r1.txt', B+'B07_out_b.txt', [
 ('We have explained', 'nothing’s come of them.', 'Your little one has heard kind words', 'more of the same.', 'opening'),
 ('So what he believes', 'in our life.', 'What your little one ends up trusting', 'wearing down your safety.', 'what the little one trusts'),
])  # the third unit would leave 48 words, under Pangram's 50-word minimum
putbacks('B14', E+'gpt_B14_api_r1.txt', B+'B14_pick_a.txt', [
 ('Work on only one', 'to carry it out.', 'Pick one protective act', 'whatever help it needs.', 'instruction'),
 ('Perhaps you need to budget', 'your old bedroom.', 'If the act is staying in a motel', 'what a night costs.', 'motel example'),
 ('Or you might need to rehearse', 'one or two times.', 'The hard part is telling your mother', 'before you call her.', 'rehearse (closing)'),
])
putbacks('B01', E+'claude_test_B01_m34_opt1.txt', B+'B01_m34.txt', [
 ('Don’t worry if you can’t find', 'do this exercise for your Protector.', "If you can't feel any warmth", 'the Protector can go first.', 'opening'),
 ('They probably can think', 'putting their phone down at midnight.', 'Care might start as', 'putting your phone down at midnight.', 'list of small acts'),
 ('Consider rehearsing', 'in difficult moments.', "If there's a hard moment", "what you'll say ahead of time.", '“it can help to” coaching'),
 ('Were you afraid?', 'getting in the way?', 'It could have been fear', 'practical getting in the way.', 'list of reasons (vs five questions)'),
 ('If you did do what you planned', 'if you feel better.', 'And if you did it', "doesn't prove it helped either.", '“doesn’t mean it failed, but…” contrast'),
 ('Keep in mind that doing something', 'things that actually help.', 'Keep what actually makes', 'what gets a check mark.', 'closing “not just a check mark” contrast'),
])

# ---------- 2. CONTROLS for Joel's one-sentence flips ----------
Q2 = 'Does it matter which sentence changes, or is the draft just on the edge so that any change flips it?'
d21 = rd(A+'A21_before.txt')
s1 = seg(d21, 'Your little one wants to play', 'play + work.'); s3 = seg(d21, 'So an afternoon', 'what went wrong.')
add('control-A21-draft', 'control', Q2, d21, [A+'A21_before.txt'], 'Claude’s draft as it was (historically 100% AI)')
add('control-A21-cut-last', 'control', Q2, once(d21, ' ' + s3, ''), [A+'A21_before.txt'], 'Joel’s cut: the “So…” closing removed (historically Human)')
add('control-A21-cut-first', 'control', Q2, once(d21, s1 + ' ', ''), [A+'A21_before.txt'], 'Control: the first sentence removed instead, the “So…” closing kept')
d12, j12 = rd(A+'A12_before.txt'), rd(A+'A12_joel_after_REFERENCE_ONLY.txt')
add('control-A12-draft', 'control', Q2, d12, [A+'A12_before.txt'], 'Claude’s draft as it was (historically AI, medium)')
add('control-A12-joel', 'control', Q2, j12, [A+'A12_joel_after_REFERENCE_ONLY.txt'], 'Joel’s one-clause change (historically Human, medium)')
add('control-A12-tiny-1', 'control', Q2, once(d12, 'detective work for a minute.', 'detective work for now.'), [A+'A12_before.txt'],
    'Control: a tiny change in a different sentence (“for a minute” to “for now”)', 'detective work for a minute.', 'detective work for now.')
add('control-A12-tiny-2', 'control', Q2, once(d12, 'before you have any clue what part', 'before you have any idea what part'), [A+'A12_before.txt'],
    'Control: a one-word change in a different sentence (“clue” to “idea”)', 'any clue', 'any idea')

# ---------- 3. FIXES to passing Emulate outputs ----------
Q3 = 'Can Emulate’s output be corrected without going back to AI?'
def fix(cid, out_file, edits, note, sub):
    t = rd(out_file)
    for old, new in edits: t = once(t, old, new) if not old.startswith('ALL:') else t.replace(old[4:], new)
    add(cid, 'fix', Q3 + ' (' + sub + ')', t, [out_file], note, [e[0] for e in edits], [e[1] for e in edits])
fix('fix-A18-noise', E+'gpt_A18_api_r1.txt', [('do n\'t have', "don't have"), ("does n't matter-you", "doesn't matter—you"), ('skip it-he', 'skip it—he')], 'spacing and hyphen noise only', 'noise')
fix('fix-B19-noise', E+'gpt_B19_api_r1.txt', [('ALL:`` ', '“'), ("ALL:''", '”'), ("does n't", "doesn't")], 'old-style quote marks and “does n’t” only', 'noise')
fix('fix-B17-noise', E+'gpt_B17_api_r1.txt', [('`` ', '“'), ("''", '”')], 'old-style quote marks only', 'noise')
fix('fix-A12-noise', E+'gpt_A12_api_r1.txt', [('Chödron has explained ,', 'Chödrön has explained,'), ('shenpa .', 'shenpa.')], 'space before comma and period, and the name’s spelling', 'noise')
fix('fix-A05-typo', E+'gpt_A05_api_r1.txt', [('afterwords', 'afterward')], 'one typo', 'noise')
fix('fix-A06-spelling', E+'gpt_A06_api_r1.txt', [('behaviour', 'behavior')], 'one British spelling', 'noise')
fix('fix-A11-spelling', E+'gpt_A11_api_r1.txt', [('no-one', 'no one')], 'one British spelling', 'noise')
fix('fix-A21-invented', E+'gpt_A21_api_r1.txt', [('I always tell my kids that the hard part in therapy is pl/ork', 'That’s why I call the deeper therapy pl/ork')], 'invented “my kids” removed, pl/ork put back to the draft’s meaning (Claude’s words)', 'content')
fix('fix-B01web-midnight', E+'gpt_charge_B01_web_optA.txt', [('at 12 pm each night', 'at midnight')], '“12 pm” (noon) corrected to “midnight”', 'content')
fix('fix-B12-invented', E+'gpt_B12_api_r1.txt', [('for your toddler to sleep', 'for your little one to sleep'), (' (even if it’s McDonald’s a couple times a week)', '')], 'invented “toddler” and “McDonald’s” removed', 'content')
fix('fix-A15-meaning', E+'gpt_A15_api_r1.txt', [('and tell them that they’ve hooked you', 'and tell yourself you’re hooked')], '“tell them they’ve hooked you” corrected to tell yourself', 'content')
fix('fix-A19-pronoun', E+'gpt_A19_api_r1.txt', [('that he did really well even though he hid', 'that they did really well even though they hid')], 'the little one’s invented “he” made “they”', 'content')
fix('fix-B02-reversed', E+'claude_test_B02_after_a_opt1.txt', [('but most of the time you can just tick them off', 'and the rest only earn a tick')], 'reversed point put right (Claude’s words)', 'content')

json.dump(checks, open(os.path.join(EXP, 'runs/sentence-check-queue.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
w = sum(c['words'] for c in checks)
print(len(checks), 'checks,', w, 'words, about', sum(-(-c['words'] // 100) for c in checks), 'credits')
for k in ('putback', 'control', 'fix'): print(k, sum(c['kind'] == k for c in checks))
print('digest', hashlib.sha256(''.join(c['sha256'] for c in checks).encode()).hexdigest()[:16])
