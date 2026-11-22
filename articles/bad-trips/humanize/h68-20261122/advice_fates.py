"""The fate of every sentence the four advice readers flagged (turn 60), and the table for RESULTS.md.

Fates: artifact (the reader saw one part, the thing is elsewhere in the guide), decided (his decision in an earlier
round), stance (his own remedy or experience, said as his), answered (his round-49 answers), verified (checked against
its source today), asked (a round-50 card), left (with why).
  python3 advice_fates.py      writes advice/FATES.json and advice/FATES.md
"""
import json, pathlib, collections
H = pathlib.Path(__file__).resolve().parent
rows = json.loads((H / 'advice' / 'TABLE.json').read_text(encoding='utf-8'))
F = {}
def put(part, ss, fate, why):
    for s in ss:
        F[(part, s)] = (fate, why)
OH, BS, MC, SS = 'outside-help', 'brain-seizure', 'mdma-chest-swallowed', 'serotonin'
put(OH, [4], 'left', 'the signs anyone can see come first; the term follows them')
put(OH, [5], 'decided', 'round 38 (r38b-call-seizure): he cut "first seizure" from his seizure call list and kept "over 5 minutes"; this line says the same')
put(OH, [6], 'left', 'the usual wording; each is something a helper sees')
put(OH, [7], 'left', 'clonus is explained in Serotonin Syndrome below; "(not just regular sweating)" is his')
put(OH, [8], 'asked', 'ADVICE-CALL a: moved here from his paragraph in round 35; what he meant by severe')
put(OH, [9, 10, 11, 13], 'left', 'his line from the start; "sudden", "one-sided", "rapidly worsening" carry it, and the chest line matches the AHA signs')
put(OH, [14], 'left', 'the signs of serotonin syndrome follow in their own section')
put(OH, [15], 'artifact', 'the remedies follow it in the guide')
put(OH, [20], 'asked', 'ADVICE-CALL b: acting delusional, or acting on a delusion')
put(OH, [24, 26], 'left', 'the guide is read beforehand too; that is the line\'s point')
put(OH, [30], 'verified', 'Fireside\'s page: any day 11 a.m. to 11 p.m., Pacific time, which the guide says (the reader\'s copy was cut at "p.m.")')
put(OH, [32, 35, 44], 'left', 'describes the service; nothing wrong in it')
put(OH, [40], 'verified', 'Crisis Text Line: US text, web chat and WhatsApp; partners in Canada, the UK and Ireland')
put(OH, [42], 'verified', 'ICEERS: up to five free online sessions')
put(OH, [43], 'verified', 'a free online group on the last Sunday of each month (an older listing)')
put(BS, [2, 14, 39, 48], 'artifact', 'what the reader missed is elsewhere in the guide (the call list above, MDMA\'s section, the link and its bracket)')
put(BS, [3, 5], 'stance', 'his from the start: the ER may be a poor place for a stable trip; benzodiazepines don\'t reliably help psychosis')
put(BS, [11, 12, 13, 26, 27, 29, 31, 32, 33, 37, 38, 40, 45], 'stance', 'his remedies (DMSO, humic acid, the sniffer, Ipomoea) and his experience, said as his; animal and lab evidence is said to be that')
put(BS, [19, 21, 23, 24, 25], 'decided', 'round 38 (r38-teach-brain): his brain checks and when to call')
put(BS, [50], 'left', 'his from the start')
put(BS, [59, 60, 63], 'decided', 'round 39 (r39c-call-list-his): his seizure call list, whole')
put(BS, [71, 73, 75, 76, 78, 79, 80, 81, 82, 88, 89, 90, 91, 92], 'stance', 'his seizure remedies (aura smells, humic acid, CBD, THC, DMSO) with the studies and the Congress testimony linked')
put(MC, [3, 5, 6, 7, 8, 9, 12, 14, 15, 22, 23, 24, 25, 26], 'stance', 'his MDMA experience and his kidney paragraph, said as his; his answer d of round 49 keeps magnesium')
put(MC, [16, 17, 19, 20, 21], 'decided', 'round 42 (r42-med-mdma): his salty drink and the signs')
put(MC, [28, 29, 30, 34, 35, 38, 39, 40, 41, 42], 'decided', 'round 3 (the AHA\'s "call 911", which gave "if unsure" its place) and round 37 (his chest-pain version)')
put(MC, [32, 33], 'decided', 'round 40 (r40-chest-evid): his evidence paragraph, Human High')
put(MC, [45], 'asked', 'ADVICE-ORAL b: naloxone, which the guide never names')
put(MC, [46, 47, 48, 49], 'decided', 'round 35 (r35-teach-oral): his paragraph; vomiting soon after swallowing can bring some back up, "up to a point" is his')
put(MC, [50], 'asked', 'ADVICE-ORAL a: ibogaine slows the heart; slow breathing isn\'t in the sources')
put(MC, [51, 53, 54, 55, 56], 'stance', 'his charcoal and poison-control paragraphs from the start; his step 3 of round 49 (call poison control when the mix is unknown) fits them; "Clinical review." is a link')
put(SS, [6, 8, 9, 10, 11, 12, 13], 'decided', 'rounds 36 and 44 (r36-teach-ss, r44-ss-lead-his): his recognition part; a helper can see most patterns without a test')
put(SS, [18, 48, 50, 51, 53], 'answered', 'his round-49 steps and answers (c, d), his words')
put(SS, [22], 'asked', 'SS-ASKED-2 b: the dose')
put(SS, [39], 'asked', 'SS-ASKED-2 e: flexing the feet is how doctors set off clonus')
put(SS, [41], 'asked', 'SS-DRINK: step 6')
put(SS, [45], 'asked', 'SS-ASKED-2 a: "the seizure" before any seizure')
put(SS, [49], 'asked', 'SS-ASKED-2 d: almost none, yet could harm')
out, missing = [], []
for r in rows:
    k = (r['part'], r['S'])
    if k not in F:
        missing.append(k); continue
    fate, why = F[k]
    out.append(dict(r, fate=fate, why=why))
assert not missing, missing
(H / 'advice' / 'FATES.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
c = collections.Counter(o['fate'] for o in out)
md = ['| part | sentence | what the reader said | fate | why |', '|---|---|---|---|---|']
for o in out:
    said = '; '.join('%s: %s' % (q, v.split(',')[0][:90]) for q, v in o['flags'].items() if q in ('RIGHT', 'MISREAD')) or '; '.join(q for q in o['flags'])
    md.append('| %s | S%d "%s" | %s | %s | %s |' % (o['part'], o['S'], o['sentence'][:90].replace('|', '/'), said.replace('|', '/'), o['fate'], o['why'].replace('|', '/')))
(H / 'advice' / 'FATES.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(len(out), dict(c))
