#!/usr/bin/env python3
"""Build Joel's questions page for the rules audit of 2026-11-27 from the verified clusters.

  python3 build_questions.py            writes ../QUESTIONS.md and ../SPEC.json (for tools/humanization/decision_page.py)

Each cluster's card is the second Fable read's text (verify/V1.md to V5.md: the rule as it reads, his words, the check,
the fix and any question only he can decide), with the lead's own corrections in LEAD (where the lead's double check
found a verifier wrong), and the hand-written items in EXTRA (the two corrections he asked for, the lead's own
addition, and the old and retired rules).
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
AUDIT = HERE.parent
REPO_URL = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/rules-audit/2026-11-27/'

GROUPS = [
    ('done', 'The two you corrected, and my addition',
     'Already changed this turn, for your check. Approve keeps the change; Revise says how; Reject undoes it.'),
    ('feature', 'A feature of your fix made into the method',
     'The smooth mistake: something that merely happened to be true of one fix of yours became the rule.'),
    ('count', 'A count or a word match standing in for judgment',
     'A word count, a word list, a percentage or a string test where you asked for a reading of meaning.'),
    ('conflict', 'Rules that contradict each other or your later word',
     'A lane obeying one of these breaks another, or undoes something you said since.'),
    ('steps', 'Steps, checks and questions nobody asked for',
     'Machinery I added that slows the work or sends you questions; your own words in these stay.'),
    ('stretch', 'Your words stretched past what you said',
     'A remark about one case taken as a rule for every case, or a quote carried past its meaning.'),
    ('old', 'Old and retired rules still reading as active',
     'Text you have overruled or retired that a lane could still follow.'),
]
GROUP_OF = {
    'C01': 'feature', 'C03': 'feature', 'C13': 'feature', 'C14': 'feature', 'C21': 'feature', 'C28': 'feature',
    'C10': 'count', 'C11': 'count', 'C22': 'count', 'C23': 'count', 'C25': 'count',
    'C04': 'conflict', 'C05': 'conflict', 'C07': 'conflict', 'C08': 'conflict', 'C12': 'conflict', 'C15': 'conflict',
    'C24': 'conflict',
    'C02': 'steps', 'C16': 'steps', 'C17': 'steps', 'C18': 'steps', 'C20': 'steps', 'C26': 'steps', 'C27': 'steps',
    'C30': 'steps',
    'C06': 'stretch', 'C09': 'stretch', 'C19': 'stretch', 'C29': 'stretch', 'C31': 'stretch',
}

# The lead's corrections of the second read (2026-11-27): where it was wrong about his words.
LEAD = {
    'C30': {
        'fix': 'The worker deletes the temporary Substack drafts it made once their results are recorded, and says so '
               '(your 2026-10-21 "yes delete the drafts once definitely done with them"). The preview link goes to you '
               'with whatever you need to use it. The mailbox check stays every turn: that one is your own word '
               '(2026-10-31: "can we make sure you always check what is addressed to you in each turn?"), and so do '
               'lane pull requests merging themselves, tools included (2026-11-14: "that should happen automatically").',
        'question': '',
        'note': 'The second read called the every-turn mailbox check unasked and asked whether tool changes may merge '
                'without you; both are your words already, so neither is a question.',
    },
}

EXTRA = [
    {'id': 'S1', 'group': 'done', 'title': 'The smooth lesson: the accurate word, not the same word',
     'rule': 'Way 30 of the read against your fixes: "find the word against the main point, and say what the thing '
             'does with a word the passage already has, as he did." Way 10, from a romance fix: "he named each with '
             'words the passage already had, and added nothing."',
     'fix': 'Way 30 now: for each word that says what something does, write what it actually does here (lowers the '
            'intensity, ends it, starts it); mark the word if it says less than that, or if its everyday sense could '
            'take a reader somewhere else ("improve the trip" reads as "boost it"); use the word that says exactly what '
            'the thing does, whether or not the passage already has it. Way 10 now: you named exactly what each "it" '
            'stood for, and added nothing else.',
     'said': '"it\'s not about using the same word. it\'s about using a word that\'s accurate. didn\'t i explain that? '
             '"change" doesn\'t mean much. "improves" is not what smoothes means, it\'s more vague." (2026-11-27 22:48 '
             'UTC); earlier, on the card: "smooth the trip makes more sense, and is more accurate also".',
     'checks': ['The Fable checker found both copies of this rule blind, for your reason ("a word the passage already has '
                'merely happened to be true of his fix; he said more accurate"), before the full audit ran.',
                'Way 10 had the same reading in a romance fix ("it" became "honesty", "won\'t look" became "won\'t look '
                'at the truth"); I changed it the same way. That one is my reading of your romance fix.'],
     'question': 'In those romance fixes, was the point naming exactly what "it" stood for (as I now have it)?',
     'where': 'tools/humanization/his_fixes_brief.md (ways 10 and 30); lessons bad-trips-2026-11-27j and l; '
              'romance-2026-11-23h'},
    {'id': 'S2', 'group': 'done', 'title': 'Your answer\'s words: what is relevant, not every word',
     'rule': '"every word of four letters or more he said for it either in that sentence or named with where it went", '
             'and the receipt tool refused a text until each such word was accounted for.',
     'fix': 'Something relevant you said (a condition, a scope, a reason) stays with your point, or has a reason to '
            'go, or I ask you when I\'m not sure it\'s relevant. Not every word: you often say things beside the '
            'point, so I read what you mean first. The clearest sign something is relevant: what I wrote doesn\'t make '
            'sense or say what you meant without it (here, "works through the skin almost as well as eating" without '
            '"sensitive skin"). The tool no longer counts your words; it only checks that a recorded drop has a reason.',
     'said': '"it\'s not that every word of my answer has to reach the sentence that says my point, but clearly if '
             'i\'m saying something which is relevant and then you\'re removing that, you\'d need to have a reason for '
             'removing it. if you\'re unsure, you\'d ask." (2026-11-27 22:48 UTC)',
     'checks': ['The checker flagged this one blind too: "a word-length count stands in for a judgment of meaning".'],
     'question': '',
     'where': 'tools/humanization/sense_receipt.py (his_answer); docs/FIXING-AN-ARTICLE.md section 5; lessons '
              'bad-trips-2026-11-27k and m'},
    {'id': 'S3', 'group': 'done', 'title': 'A check of every new lesson against your words (my addition)',
     'rule': 'Nothing checked a new lesson against what you said before it went to every lane.',
     'fix': 'Before a lesson file goes to main, a fresh Fable reader reads it with the brief that found the smooth '
            'rule; a flag about your meaning comes to you, the rest are fixed or the lesson says why they stand. About '
            'a minute per lesson file, not a gate on article work. A lesson\'s method is the reason you gave; what your '
            'fix merely happened to do is the method only where your words or the case show it is why the fix works.',
     'said': '"i often assume you\'re understanding the lessons" (2026-11-27 22:48 UTC)',
     'checks': ['This turn\'s three new lessons had it first: five flags, all taken (one lesson contradicted itself, '
                'my test for "relevant" was narrower than yours, and two places that are my reading are now marked).'],
     'question': '',
     'where': 'docs/lessons/README.md; tools/humanization/rules_check_brief.md; lesson bad-trips-2026-11-27n'},
    {'id': 'OLD-GATE', 'group': 'old', 'title': 'The old gate (September to early November): mark it historical',
     'rule': 'docs/HUMANIZATION-GATE.md opens "Status: ACTIVE" and still says: every reviewer flag is fixed; every '
             'paragraph gets a break (a question, an exclamation); first drafts use jokes and asides because they read '
             'Human; an emoji placement goes to you for a yes or no; a two-call Pangram budget; a stretch is acted on '
             'only once it reads AI twice (E324); a cut you agreed to still waits on a forecast (E343); "quietly" is '
             'both a fail and a caution; "Lists themselves are fine" beside your "avoid that unless it\'s really needed".',
     'fix': 'Mark its sections historical in the file, each pointing to where its topic lives now, and settle the '
            'contradictions by your latest words: a window that reads AI, Low or Medium once is fixed (no second '
            'reading); a cut you agreed to is made; "quietly" goes unless it says how something sounds; a list is '
            'avoided unless it\'s really needed; reviewer flags are leads, sense and Pangram are the gates.',
     'said': '"if a section reads ai or human low, we don\'t need to check it again to verify that, we need to fix it"; '
             '"remove "quietly" that\'s an ai tell"; "it made no difference taking those exclamation phrases out for '
             'pangram"; "my approach requires not even thinking about pangram at first".',
     'checks': ['Clusters C32 to C34 and five stale items: 41 flags in all; the second read confirmed each.'],
     'question': '',
     'where': 'docs/HUMANIZATION-GATE.md; docs/INDEX.md calls it "the working humanization gate"'},
    {'id': 'EMULATE', 'group': 'old', 'title': 'Emulate: retired, but parts still read as active',
     'rule': 'docs/EMULATE-FALLBACK.md says both "RETIRED for new humanization, 2026-11-03" and "ACTIVE for every '
             'article", "they go to Emulate first"; its shape rules still go into every writer\'s brief, and one rule '
             'prefers Emulate\'s wording over your published words.',
     'fix': 'Everything but the strict checks of Emulate text already in your articles is marked retired; its shape '
            'rules leave the briefs; your published words are never replaced by Emulate\'s.',
     'said': '"emulate doens\'t even pass pangram 4.1 very well anymore so that\'s pointless and emulate has done so '
             'much damage to my guides"; "make those emulate checks more strict pls for future also".',
     'checks': ['17 flags; the second read confirmed it.'],
     'question': '',
     'where': 'docs/EMULATE-FALLBACK.md; docs/INDEX.md'},
    {'id': 'LEFTOVERS', 'group': 'old', 'title': 'Three leftovers that contradict newer text',
     'rule': 'Lesson gut-2026-11-06f\'s bold line still gives the instruction you corrected two hours later; '
             'docs/CLARITY-READ.md still writes you "the list, numbered in the article\'s order"; docs/INDEX.md names a '
             'ChatGPT/Codex "task-time lesson contract" for a Somatic lane, with no words of yours.',
     'fix': 'The headline says the correction; the numbered list goes (the marking page replaced it); the contract is '
            'marked historical.',
     'said': '"way too dificult, you\'re giving me half suggestion that are out of context" (the marking page, '
             '2026-10-25).',
     'checks': ['Four flags; confirmed, except one SKILL.md leftover the second read couldn\'t find (left alone).'],
     'question': '',
     'where': 'docs/lessons/2026-11-06-2126-gut.md; docs/CLARITY-READ.md; docs/INDEX.md'},
]


def parse_verify():
    out = {}
    for f in sorted((AUDIT / 'verify').glob('V*.md')):
        cur = None
        for line in f.read_text(encoding='utf-8').split('\n'):
            m = re.match(r'^## (C\d\d) (.*?): (confirmed|partly|not sus)\s*$', line)
            if m:
                cur = out.setdefault(m.group(1), {'title': m.group(2).strip(), 'verdict': m.group(3), 'rule': '',
                                                  'said': '', 'checks': [], 'fix': '', 'question': ''})
                continue
            if line.startswith('## '):
                cur = None
                continue
            if cur is None or not line.startswith('- '):
                continue
            k, _, v = line[2:].partition(': ')
            k = k.strip().lower()
            if k == 'rule':
                cur['rule'] = v
            elif k == 'he said':
                cur['said'] = v
            elif k == 'check':
                cur['checks'].append(v)
            elif k == 'fix':
                cur['fix'] = v
            elif k.startswith('question'):
                cur['question'] = v
    return out


VERBS = ('say says said asks asked wants gives finds keeps names writes uses sends approves cuts fixes calls dislikes '
         'prefers likes means meant thinks knows sees reads checks picks rejects answers allows allowed corrected '
         'removed added called gave named wrote typed kept rejected cut fixed asked chose changed').split()


def to_you(s):
    """The second read wrote about Joel ("he said"); the card speaks to him. Only text outside quotation marks changes."""
    parts = re.split(r'("[^"]*")', s)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            out.append(p)
            continue
        p = re.sub(r"\bJoel's\b", 'your', p)
        p = re.sub(r'\bJoel\b', 'you', p)
        p = re.sub(r'\bhimself\b', 'yourself', p)
        p = re.sub(r"\bhe's\b", "you're", p)
        p = re.sub(r"\bHe's\b", "You're", p)
        p = re.sub(r'\bHe\b', 'You', p)
        p = re.sub(r'\bhe\b', 'you', p)
        p = re.sub(r'\bHis\b', 'Your', p)
        p = re.sub(r'\bhis\b', 'your', p)
        p = re.sub(r'\bhim\b', 'you', p)
        p = re.sub(r'\byou (is)\b', 'you are', p)
        p = re.sub(r'\b([Yy]ou) has\b', r'\1 have', p)
        p = re.sub(r'\b([Yy]ou) supplies\b', r'\1 supply', p)
        p = re.sub(r'\byou (was)\b', 'you were', p)
        p = re.sub(r'\byou (does)\b', 'you do', p)
        for v in VERBS:
            if v.endswith('s') and not v.endswith('ss'):
                p = re.sub(r'\b(you|You) %s\b' % v, r'\1 %s' % (v[:-2] if v.endswith('es') and v[:-2].endswith(('sh', 'ch', 'x')) else v[:-1]), p)
        p = re.sub(r'\s*\((?:pref|prefs|preferences\.md)[ :]?(?:line )?\d+(?:, \d+)*\)', ' (your saved preferences)', p)
        p = re.sub(r'\bprefs? (?:line )?\d+\b', 'your saved preferences', p)
        out.append(p)
    return ''.join(out)


def plain(s):
    """Paths and line numbers stay, but the card reads in plain words: '(file:12)' marks become '(file, line 12)'."""
    return to_you(re.sub(r'\(([\w./-]+\.(?:md|py|json)):(\d+(?:-\d+)?)\)', r'(\1, line \2)', s))


def main():
    clusters = {c['id']: c for c in json.loads((AUDIT / 'CLUSTERS.json').read_text(encoding='utf-8'))['clusters']}
    ver = parse_verify()
    items = []
    for cid in sorted(GROUP_OF, key=lambda x: ([g[0] for g in GROUPS].index(GROUP_OF[x]), x)):
        v, c = ver[cid], clusters[cid]
        lead = LEAD.get(cid, {})
        files = []
        for r in c['rules']:
            for f in re.split(r',\s*', r.get('file', '')):
                f = f.strip()
                if f and f not in files:
                    files.append(f)
        items.append({'id': cid, 'group': GROUP_OF[cid], 'title': c['title'], 'verdict': v['verdict'],
                      'rule': plain(v['rule']), 'fix': plain(lead.get('fix', v['fix'])), 'said': plain(v['said']),
                      'checks': [plain(x) for x in v['checks']] + ([lead['note']] if lead.get('note') else []),
                      'question': plain(lead['question'] if 'question' in lead else v['question']),
                      'where': '; '.join(files), 'flags': len(c['flags'])})
    items = EXTRA[:3] + items + EXTRA[3:]
    # Markdown, which GitHub renders
    md = ['# Rules audit of 2026-11-27: the rules that look sus',
          '',
          'You asked me to go over all the rules with Fable double-checking, after the wrong smooth lesson. What ran: '
          'every rule in the repository (2,087 units: AGENTS.md, SKILL.md, the briefs and docs, all 110 lesson files, '
          'the old gate, the 223 tells, and your saved preferences) went to Fable checkers in 35 batches. Before the '
          'full run, the checker had to find the smooth rule blind, told nothing about it: it flagged both copies '
          'for your reason, and the every-word rule too. 404 flags came back; a Fable consolidator merged them into '
          '34 clusters and 8 stale items; five Fable verifiers checked each against the rule\'s own text and your words '
          'in context, and rewrote the fixes that would have undone something you said later; I checked their checks '
          '(one correction of mine, on C30).',
          '',
          'Each card: the rule as it reads now, what I\'d change it to, what you said, why it looks off, and a question '
          'where only you can decide. **Approve** = I change the rule as proposed, in every file it lives in. '
          '**Revise** = tell me how in the note. **Reject** = it stays as it is. The interactive page has the same '
          'cards with buttons; this file is the record.',
          '',
          'The record of the run: [flags](flags/), [clusters](CLUSTERS.md), [the second read](verify/), [the '
          'checker\'s brief](CHECKER-BRIEF.md).',
          '']
    for gid, gtitle, gintro in GROUPS:
        md += ['## ' + gtitle, '', gintro, '']
        for it in [i for i in items if i['group'] == gid]:
            md += ['### %s. %s' % (it['id'], it['title']), '']
            md += ['- **The rule now:** ' + it['rule'],
                   '- **What I\'d change it to:** ' + it['fix'],
                   '- **What you said:** ' + it['said']]
            for ch in it['checks']:
                md.append('- **Why it looks off:** ' + ch)
            if it.get('question'):
                md.append('- **Question for you:** ' + it['question'])
            md.append('- **Where it lives:** ' + it['where'] + (
                ' (%d flags%s)' % (it['flags'], ', ' + it['verdict'] if it.get('verdict') else '')
                if it.get('flags') else ''))
            md.append('')
    text = '\n'.join(md).rstrip('\n') + '\n'
    (AUDIT / 'QUESTIONS.md').write_text(text, encoding='utf-8')
    sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
    spec = {'review_id': 'rules-audit-20261127', 'title': 'Rules audit, 27 Nov: the rules that look sus',
            'source_sha256': sha, 'source_name': 'docs/rules-audit/2026-11-27/QUESTIONS.md',
            'repo_file': REPO_URL + 'QUESTIONS.md',
            'intro': [md[2], md[4]],
            'groups': [{'id': g, 'title': t, 'intro': i,
                        'approve': 'change the rule as proposed, in every file it lives in',
                        'reject': 'the rule stays as it is'} for g, t, i in GROUPS],
            'items': []}
    for it in items:
        fields = [{'label': 'What you said', 'text': it['said']}]
        fields.append({'label': 'Why it looks off', 'list': it['checks']} if len(it['checks']) > 1
                      else {'label': 'Why it looks off', 'text': it['checks'][0]})
        if it.get('question'):
            fields.append({'label': 'Question for you', 'text': it['question']})
        fields.append({'label': 'Where it lives', 'text': it['where']})
        entry = {'id': it['id'], 'group': it['group'], 'title': it['title'],
                 'section': '%s%s' % (it.get('verdict', 'done' if it['group'] == 'done' else 'confirmed'),
                                      (', %d flags' % it['flags']) if it.get('flags') else ''),
                 'whose': 'a rule I wrote',
                 'blocks': [{'label': 'The rule now', 'paras': [[[it['rule'], '']]]},
                            {'label': 'What I\'d change it to', 'paras': [[[it['fix'], 'ins']]]}],
                 'fields': fields,
                 'links': [{'text': 'This card in the record (GitHub)', 'url': REPO_URL + 'QUESTIONS.md'}]}
        if it['group'] == 'done':
            entry['approve'] = 'keep the change I made'
            entry['reject'] = 'undo it'
        spec['items'].append(entry)
    (AUDIT / 'SPEC.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(items), 'items;', len(text), 'chars of Markdown; sha', sha[:12])


if __name__ == '__main__':
    main()
