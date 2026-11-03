"""FINDINGS.md and FINDINGS.json: every finding of the nonsense read (reads/ and pass2/reads/), traced to whose words it
is in and given its fate. The guide the readers read was HUMANIZED-SO-FAR.md bb5fc57d (parts/, pass2/parts/).

Whose words: his messages and answers (COMPARE-GATE.json's owner files, compare_read.is_his), his published guide of
28 September (source/published-20260928.md, which AI tools drafted before he published it), his inner child guide
(fix-20261025/ic-align/IC-GUIDE.txt), or else ours (the lanes' edits and Emulate's output). The sentence is tested
first, then the questioned phrase by itself.

  python3 articles/inner-signal/humanize/fix-20261103/nonsense/make_findings.py
"""
import glob
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

# block: (probe phrase, fate, reason). Fates: fixed (apply_nonsense.py), Q34 (his own words: his call), kept, planted.
FATES = {
    106: ('Their trust can question', 'fixed', 'trust doing the questioning and remembering; now "They can question your promises ... and take their time."'),
    138: ('a very charming guard', 'fixed', 'his published irony ("making an appearance in its usual charming way") had been flattened into a plain claim; his phrase is back'),
    436: ('one or more of trauma-specific', 'fixed', 'a missing "the"'),
    559: ('using an Implementation Intention', 'fixed', 'the missing full stop'),
    729: ('some yarn, some bubbles', 'fixed', 'bubbles don\'t unwind; his published picture is back ("some yarn unwinding, some bubbles settling, or some knots")'),
    654: ('use this app or ask around', 'fixed', '"this app" pointed at nothing (Emulate\'s sentence); cut'),
    66: ('repeated correction between', 'Q34', '"correction between" three things: likely a slip like "oily" in his published guide'),
    156: ('taking off the kid gloves', 'Q34', 'the idiom means stopping being gentle; with "so to speak" it can read as his wink'),
    227: ('playing asleep', 'Q34', 'not an idiom; reads as his play on "playing dead"'),
    276: ('the mental escape into the body', 'Q34', 'an "escape" in a paragraph about staying alert; it can mean the mind escaping into the body\'s flow'),
    566: ('when they were led to', 'Q34', '"led to" has no object'),
    192: ('consciously sculpted adult', 'kept', 'his phrase; the adult you have consciously shaped'),
    204: ('is that sudden', 'kept', 'his sentence; "that" points at the waking up, so it parses'),
    546: ('do not authorize you', 'kept', 'a cue is no warrant to decide, which is what the next sentence says'),
    715: ('lead to the same thing', 'kept', 'informal but clear'),
    731: ('gathered enough of your attention', 'kept', '"gather your attention" is the guide\'s own name for the step'),
    344: ('you meant for your little one', 'kept', 'his inner child guide\'s words'),
    379: ('alleviates the instinct', 'kept', 'his words'),
    345: ('use the Witness', 'kept', 'the guide\'s witnessing position, in his published guide and at block 555'),
    614: ('like me to know', 'kept', '"What would this felt sense like me to know?" is grammatical (would like me to know)'),
    683: ('août', 'kept', 'the text of his post-embed card (a native block), not the guide\'s prose'),
}


def main():
    canaries = json.loads((HERE / 'CANARIES.json').read_text(encoding='utf-8'))
    canaries = canaries if isinstance(canaries, list) else canaries['canaries']
    planted = {c['block']: c for c in canaries}
    gate = json.loads((H / 'COMPARE-GATE.json').read_text(encoding='utf-8'))
    mine = cr.owner_paragraphs(gate['owner'], str(ROOT))
    pub = cr.loose((H / 'source' / 'published-20260928.md').read_text(encoding='utf-8'))
    ic = cr.loose((H / 'fix-20261025' / 'ic-align' / 'IC-GUIDE.txt').read_text(encoding='utf-8'))
    parts = {}
    for f in sorted(glob.glob(str(HERE / 'parts' / '*.md'))) + sorted(glob.glob(str(HERE / 'pass2' / 'parts' / '*.md'))):
        for line in pathlib.Path(f).read_text(encoding='utf-8').splitlines():
            if line.startswith('[') and '] ' in line:
                i = int(line[1:line.index(']')])
                parts.setdefault(i, line[line.index(']') + 2:].lstrip('# '))
    rows = {}
    for f in sorted(glob.glob(str(HERE / 'reads' / 'READ-*.json'))) + sorted(glob.glob(str(HERE / 'pass2' / 'reads' / 'READ-*.json'))):
        name = ('pass 2 ' if '/pass2/' in f else 'pass 1 ') + pathlib.Path(f).stem[5:]
        for x in json.loads(pathlib.Path(f).read_text(encoding='utf-8'))['findings']:
            b = x['block']
            c = planted.get(b)
            if c and (c.get('planted') or c.get('new') or '').split()[-1].strip('.') in x['text']:
                key = ('planted', b)
            else:
                key = ('real', b)
            r = rows.setdefault(key, {'block': b, 'readers': [], 'text': x['text'], 'what': x['what'], 'fix': x['fix']})
            r['readers'].append(name)
    out = []
    for (kind, b), r in sorted(rows.items(), key=lambda kv: (kv[0][0] != 'real', kv[0][1])):
        if kind == 'planted':
            r.update(fate='planted', why='one of the nine planted errors (CANARIES.json)', whose='planted')
        else:
            probe, fate, why = FATES[b]
            t = parts.get(b, '')
            sent = next((s for s in cr.sentences(t) if probe in s), t)
            L, P = cr.loose(sent), cr.loose(probe)
            whose = ('his message or answers' if cr.is_his(L, mine) else
                     'his published guide of 28 September' if L in pub else
                     'his inner child guide' if L in ic else
                     'his phrase (messages or answers)' if any(P in m for m in mine) else
                     'his phrase (published guide)' if P in pub else
                     'his phrase (inner child guide)' if P in ic else 'ours (our edits or Emulate)')
            if b == 683:
                whose = 'his post-embed card (native block)'
            r.update(fate=fate, why=why, whose=whose, sentence=sent)
        out.append(r)
    (HERE / 'FINDINGS.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    real = [r for r in out if r['fate'] != 'planted']
    lines = ['# The nonsense read: every finding, whose words, and what became of it', '',
             'Two passes over HUMANIZED-SO-FAR.md bb5fc57d (after his E-523 and "old"): nine fresh readers on nine parts',
             '(`BRIEF.md`, `reads/`), then three on three parts with nine planted errors of the "oily" kind and a required',
             'list of every block read (`pass2/BRIEF.md`, `pass2/reads/`, `CANARIES.json`). Pass 2 found all nine planted',
             'errors. Under them, a mechanical net: `nonwords.py` (NONWORDS.json: 25 non-words, every one a name, a term or',
             'his coinage). Made by `make_findings.py`.', '',
             '%d real findings: %d fixed (`apply_nonsense.py`), %d in his own words for him (question 34), %d kept.' % (
                 len(real), sum(r['fate'] == 'fixed' for r in real), sum(r['fate'] == 'Q34' for r in real),
                 sum(r['fate'] == 'kept' for r in real)), '',
             '| Block | Readers | Whose words | Fate | The sentence | Why |', '|---|---|---|---|---|---|']
    for r in out:
        s = (r.get('sentence') or r['text']).replace('|', '\\|')
        lines.append('| %d | %s | %s | %s | %s | %s |' % (r['block'], ', '.join(r['readers']), r['whose'], r['fate'],
                                                         s[:220], r['why'].replace('|', '\\|')))
    (HERE / 'FINDINGS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    for r in out:
        print(r['block'], r['fate'], '|', r['whose'], '|', ', '.join(r['readers']))


if __name__ == '__main__':
    main()
