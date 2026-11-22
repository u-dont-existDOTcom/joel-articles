#!/usr/bin/env python3
"""predict.py - this folder's predictions (pangram_ledger.py predict), written before each batch's checks.

  python3 predict.py KEY...      (from anywhere) predict the named tests
"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
L = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
DET = 'Pangram web app (his account, Pangram Professional)'
U = {u['key']: u for u in json.loads((HERE.parent / 'h42-20261111/pass/UNITS.json').read_text(encoding='utf-8'))}
H42 = json.loads((HERE.parent / 'h42-20261111/pass/RESULTS-h42a.json').read_text(encoding='utf-8'))
FIVE = ("his five fixes (SKILL.md, Writing for Pangram) on the window that read below High, nothing else in the unit "
        "changed: the point first, the plain word, what belongs together joined, a long list taken apart")
P = {
 'h42-08': dict(call='Human', chance=0.75, batch='h43a',
   tells=["but it's still experimental"],
   human=['So it might help alongside rescue medicine', "I wouldn't wait on it while a seizure keeps going"],
   first="payoff: the sentence opens on what the mixed evidence means for the reader ('So it might help alongside rescue "
         "medicine'); join: the caution joined to it ('but ... and I wouldn't wait on it'); plain: 'a plausible "
         "experimental adjunct remedy rather than something to wait on while a seizure continues' to 'might help alongside "
         "rescue medicine, but it's still experimental, and I wouldn't wait on it while a seizure keeps going'"),
 'h42-17': dict(call='Human', chance=0.65, batch='h43a',
   tells=["though a longer trip can be useful and healthy when it's planned"],
   human=['Eating a couple of coffee cherries helps my nausea.', "I wouldn't reach for coffee cherries first"],
   first="payoff: the instruction first ('I wouldn't reach for coffee cherries first if somebody is already becoming "
         "manic'), his view of a longer trip after it; join: still one sentence, turned on 'though'; plain: 'That can be "
         "useful and healthy when planned' to 'a longer trip can be useful and healthy when it's planned', the referent named"),
 'h42-30': dict(call='Human', chance=0.6, batch='h43a',
   tells=['The same goes after a stimulant or an unknown mixture, or with any medical concern.'],
   human=["Going outside can help too, if it's somewhere quiet with nothing high to fall from",
          "and hold off too if you feel faint or badly confused"],
   first="payoff: going outside opens on what it does ('can help too'), its limits after; join: the exercise limit's seven "
         "conditions said as two pairs and a sentence for the rest; plain: 'Go outside only away from roads, heights, crowds, "
         "and water' to 'somewhere quiet with nothing high to fall from, away from roads and water', 'with overheating, chest "
         "pain, faintness, severe confusion' to 'if you're overheating or have chest pain ... if you feel faint or badly confused'"),
 'h42-20': dict(call='Human', chance=0.55, batch='h43b',
   tells=['With seizures it can go either way:'],
   human=['in animal studies it calmed one kind and, at some doses, made another kind worse'],
   first="payoff: the item opens on what it means for someone with seizures ('With seizures it can go either way'); join: "
         "its two sentences made one, the second cut as a repeat of Active Seizure's DMSO paragraph (gate E378); plain: "
         "'both anticonvulsant and proconvulsant effects depending on dose and seizure model' to 'in animal studies it "
         "calmed one kind and, at some doses, made another kind worse'"),
 'h42-22': dict(call='Human', chance=0.55, batch='h43b',
   tells=["there's something organizing about it too"],
   human=["I just know that again and again it's felt like a powerful natural remedy"],
   first="payoff: what it feels like first ('It feels grounding and cooling'); join: 'I don't understand the mechanism.' "
         "and 'I only know that ...' made one sentence, as he joins; plain: 'a grounding, cooling, organizing effect "
         "different from DMSO, aged ozonated-charcoal water, zeolite, or beach morning glory' to 'grounding and cooling, "
         "and there's something organizing about it too that I don't get from DMSO or my other remedies', 'excessive "
         "psychedelic intensity' to 'a trip that's too intense'"),
 'h42-25': dict(call='Human', chance=0.5, batch='h43b',
   tells=['the fear or grief, an old memory, a sudden certainty...'],
   human=['somebody still needs to sit with whatever the altered mind has opened up'],
   first="payoff: the sentence turns on who is needed ('somebody still needs to sit with'), not on a list; join: still one "
         "sentence; plain: the five-noun list ('fear, grief, memory, certainty, and whatever else') taken apart into what "
         "the trip opened up, ending on a trailing '...' (his list fix, the fifth)"),
 'h42-08-fix2': dict(call='Human', chance=0.6, batch='h43b', base='h42-08',
   tells=["although that's experimental"],
   human=["I'd still consider DMSO alongside it"],
   first="payoff: the point first ('While a seizure continues, the rescue medicine comes first'), said as what to do; join: "
         "his act and its hedge in the same sentence; plain: 'a plausible experimental adjunct remedy rather than something "
         "to wait on' to 'I'd still consider DMSO alongside it, although that's experimental'",
   after="fix1 ('So it might help ..., but it's still experimental, and I wouldn't wait on it ...') read AI Low (a0b91061); "
         "this says the last sentence in the shape of his Human High line in the part before ('I'd also try sniffing "
         "humic/fulvic acid powder, although that's just a hunch ...'): one first-person act and one candid hedge, after "
         "the point said as what to do"),
 'h42-20-p': dict(call='Human', chance=0.6, batch='h43b', base='h42-20', scope='paragraph',
   lineage="bad-trips DMSO's contraindications (Mental Stabilizers 3 of 6), the seizure item fixed (h43)",
   tells=['With seizures it can go either way:'],
   human=['even though rubbing DMSO--especially with magnesium chloride--on the head can alleviate tension headaches'],
   first=None),
 'h42-22-p': dict(call='Human', chance=0.55, batch='h43b', base='h42-22', scope='paragraph',
   lineage="bad-trips Ocean water's touch and its effect (Mental Stabilizers 5 of 6), fixed (h43)",
   tells=["there's something organizing about it too"],
   human=["Touching the outside of a bottle doesn't do it."],
   first=None),
 'h42-25-p': dict(call='AI', chance=0.45, batch='h43b', base='h42-25', scope='paragraph',
   lineage='bad-trips Niacin\'s B3 forms and the bridge to tripsitting, fixed (h43)',
   tells=['the fear or grief, an old memory, a sudden certainty...'],
   human=['Niacinamide sometimes relaxes people and sometimes creates hyperfocus, depending on their state.'],
   first=None),
 'h42-20-fix1': dict(call='Human', chance=0.65, batch='h43c', base='h42-20',
   tells=['With seizures it can go either way:'],
   human=["although I haven't found anecdotes of this causing a real problem"],
   first=None,
   narrowed="bad-trips DMSO's contraindications (Mental Stabilizers 3 of 6), the seizure item fixed (h43): Human High 61 "
            "(https://www.pangram.com/history/4d3214e7-ee0f-4940-9654-442fe51a0520)"),
 'h42-22-fix1': dict(call='Human', chance=0.6, batch='h43c', base='h42-22',
   tells=["there's something organizing about it too"],
   human=['I noticed it in Kenya and Florida.'],
   first=None,
   narrowed="bad-trips Ocean water's touch and its effect (Mental Stabilizers 5 of 6), fixed (h43): Human High 93 "
            "(https://www.pangram.com/history/c6065c63-c667-44f8-bfcf-deca95b61e4d)"),
 'h42-25-p2': dict(call='AI', chance=0.4, batch='h43c', base='h42-25', scope='paragraph', key='h42-25-p-fix2',
   lineage='bad-trips Niacin\'s B3 forms and the bridge to tripsitting, fixed (h43)',
   big="only the bridge sentence changed (the forms paragraph is the same); in a 37-word sentence the five-item list that fix1 kept, taken apart, is most of its words, and that list was the tell: fix1 still read AI High (fd6713de)",
   tells=['whatever the trip stirred up still needs somebody to sit with it'],
   human=['Niacinamide sometimes relaxes people and sometimes creates hyperfocus, depending on their state.'],
   first="payoff: unchanged, who is needed; join: still one sentence; plain: the list dropped, since it only previewed what "
         "the sections after it say in full (lesson 06a), and 'whatever else the altered mind has opened' said as "
         "'whatever the trip stirred up'"),
 'anchor-a1': dict(call='AI', chance=0.35, batch='h43c', base=None, scope='pair', key='anchor-a1',
   lineage='bad-trips Get One Human Anchor, its first two paragraphs after round 33 (h43)',
   tells=['So have one calm person be the anchor and take the lead.'],
   human=['So can a crowd of people telling them what it all means, or panicking right along with them.'],
   first="payoff: the two ways a trip gets worse said as what makes it worse, then the instruction; join: the crowd's four "
         "acts made two; the hand-off's conditions one sentence, the firm one last ('and do it right away if there's any "
         "risk of violence or self-harm'); plain: 'start advising, arguing, spiritualizing, or panicking' to 'telling them "
         "what it all means, or panicking right along with them'"),
 'harm-b1': dict(call='AI', chance=0.3, batch='h43c', base=None, scope='paragraph', key='harm-b1',
   lineage="bad-trips Risk of Harm, its first paragraph after round 33 (h43)",
   tells=['Dangerous physical symptoms count, and so does'],
   human=['like when they keep heading for roads and high places, or water for that matter'],
   first="payoff: the instruction first ('Get urgent help the moment'), each reason after it; join: the nine conditions in "
         "five sentences, two at most a sentence; plain: 'command voices or fixed terrifying beliefs driving action' to "
         "'Voices telling them what to do ... a fixed, terrifying belief they've started acting on', 'exceeds what the sitter "
         "can safely contain' to 'more than you can safely handle'"),
 'h42-08-fix3': dict(call='Human', chance=0.6, batch='h43d', base='h42-08', key='h42-08-fix3',
   tells=["although that's experimental"],
   human=["I'd treat DMSO as a plausible adjunct remedy"],
   first="payoff: the point first ('While a seizure continues, the rescue medicine comes first'); join: his act and its "
         "hedge in the same sentence; plain: 'rather than something to wait on while a seizure continues' said as what to "
         "do, his 'adjunct remedy' kept (KEEP-AS-IS K12)",
   after="fix2 read Human Medium (83f4caef) but dropped his 'adjunct remedy' (KEEP-AS-IS K12: 'the one thing that flipped "
         "it was adding remedy to adjunct'); this keeps those words in fix2's order"),
 'h42-41-p': dict(call='Human', chance=0.55, batch='h43d', base='h42-41', scope='paragraph', key='h42-41-p-fix1',
   lineage='bad-trips Dealing With Shadow Thoughts, its during-a-trip lines with the paragraph before, fixed (h43)',
   tells=['Confessing it to everyone in the room can wait, and so can turning it into some permanent diagnosis...'],
   human=["maybe don't take every shadow thought as the truth about you"],
   first="payoff: when it applies first ('While you're still tripping'); join: the four don'ts in two sentences, as he "
         "says a don't (J69: a hedged don't, plain verbs, a trailing '...'); plain: 'identify with' to 'take ... as the "
         "truth about you', 'convert it into a permanent diagnosis' to 'turning it into some permanent diagnosis', the "
         "'Notice:' script said as what to notice"),
 'harm-b3': dict(call='AI', chance=0.35, batch='h43d', base=None, scope='paragraph', key='harm-b3',
   lineage="bad-trips Risk of Harm, its first paragraph after round 33 (h43)",
   tells=['It\'s time as well when voices are telling them what to do'],
   human=['If you find yourself wondering whether this is more than you can safely handle, it probably is, so call.'],
   panel='articles/bad-trips/humanize/h43-20261111/panel-harm-b2/PANEL.md',
   big="b1 took the nine conditions apart into five sentences and read AI 100% (4c6f1bf6); the panel on the next wording "
       "(panel-harm-b2/PANEL.md) flagged every sentence and the whole shape, an even run of if-X-call triggers with a "
       "thesis opener and a summary closer, so the small fixes inside that shape are spent: this drops the opener and the "
       "closer and says each reason in a different shape",
   first="payoff: the first reason says to act without waiting to be sure; join: the voices, the belief and violence in "
         "one sentence; plain: 'dangerous physical symptoms' named as 'dangerous signs, like trouble breathing or "
         "overheating', the closer said as the sitter's own doubt"),
}


def predict(key):
    p = P[key]
    base = p['base'] if 'base' in p else key
    u = U[base] if base else {'title': p['lineage']}
    r = H42[base] if base else None
    fname = p.get('file') or (key[:-5] if key.endswith('-fix1') else key)
    text = 'articles/bad-trips/humanize/h43-20261111/TEST-%s.txt' % fname
    a = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', L,
         '--lineage', p.get('lineage') or 'bad-trips %s as it stands (h42)' % u['title'], '--scope', p.get('scope', 'section'), '--text', text,
         '--key', p.get('key') or (key if '-fix' in key else key + '-fix1'), '--batch', p['batch'], '--call', p['call'], '--chance', str(p['chance']), '--detector', DET,
         '--receipt', 'articles/bad-trips/humanize/h43-20261111/TEST-%s.receipt.json' % fname,
         '--humanized', FIVE, '--first-fix', p['first'] or P[base if base in P else key.rsplit('-fix', 1)[0]]['first'],
         '--diagnosis', ('h42a read the unit %s (%s; https://www.pangram.com/history%s); this fixes only the window below High '
                        'that is mine to fix' % (r[0], r[3], r[5])) if r else 'h42a read its section AI Generated, 100%; earlier '
                        'wordings were tried in turns before round 33; this is my best try of the text after round 33, his five fixes first',
         '--decides', 'whether this fix goes into the guide']
    if p.get('panel'):
        a += ['--panel', p['panel']]
    if p.get('big'):
        a += ['--big-change', p['big']]
    if p.get('narrowed'):
        a += ['--narrowed', p['narrowed']]
    if p.get('after'):
        a += ['--after-fix', p['after']]
    for t in p['tells']:
        a += ['--tells', t]
    for t in p['human']:
        a += ['--human-tells', t]
    r = subprocess.run(a, cwd=REPO, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(key, '|', out.splitlines()[-1] if out else r.returncode)
    if r.returncode:
        print(out)


if __name__ == '__main__':
    for k in sys.argv[1:] or list(P):
        predict(k)
