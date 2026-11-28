#!/usr/bin/env python3
"""open_questions.py - the rule tree's open questions as cards for Joel (2026-11-28, turn 76).

  python3 open_questions.py    writes ../OPEN-QUESTIONS.md and ../OPEN-SPEC.json (for tools/humanization/decision_page.py)

Each card is one rule of rules/TREE.md whose Status is an open question his answers on the audit left open: the rule as
it stands, his words, what the editor does until he answers (Approve keeps it), and the other way (Reject takes it).
The rule's text and his words come from rules/tree.json, so the cards say what the tree says.
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
AUDIT = HERE.parent
REPO = AUDIT.parents[2]
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
VIEW = 'https://claude.ai/artifact/RPYerG1RZ1iNwECeaBTSZk'

# (rule id, the question in plain words, Approve: what happens until he answers, Reject: the other way)
QUESTIONS = [
    ('R-model-text-is-mine',
     'When I fix wording you humanized yourself (in an article a model drafted), does the fix go in and get reported, or '
     'go on a card you can revise? Card C12 said a card; card C18 said a tested change goes in without one, and you '
     'approved both.',
     'It goes in, tested, and is reported with its before and after; a card only where the fix could change something '
     'you decided.',
     'Each fix to wording you humanized goes on a card you can revise.'),
    ('R-every-window-high',
     'When a paragraph of mine still reads Medium after its whole budget of tries, does it go into the article marked as '
     'open work, or stay out until it reads High?',
     'It stays out until it reads High, as your words of 2026-11-12 ask ("i guess you need to stop passing over anything '
     'that\'s not human high"), and is reported as open work with its link.',
     'It goes in, marked as open work with its link, and stays on the list of what is left.'),
    ('R-check-rewrite-once',
     'The old gates from August and September (the preservation ledger, the architecture ledger, the delivery gate, three '
     'fixed writing rounds, the reader-question audit offers): do you still want any of them?',
     'None of them; one compare with your text per pass, sized to the change.',
     'Keep some of them: say which in the note.'),
    ('R-x-does-not-y',
     'Your rule "let\'s make sure "X does not Y" is changed in general": does it mean every plain negative statement, or '
     'the abstract kind, like ""I saw it" does not create a duty to act"?',
     'The abstract kind is reworked by default; a plain negative ("it does not dissolve in water") is judged case by '
     'case.',
     'Every plain negative statement too.'),
    ('R-kitchen-and-weekdays',
     'An added day of the week reads as an AI sign to you. Should a weekday be cut everywhere, or only where I added '
     'it?',
     'One I added goes; a real day in one of your own stories stays.',
     'A weekday is cut everywhere, yours included (I would ask before changing your own story).'),
    ('R-dashes-and-quotes',
     'Should your two hyphens "--" always have no spaces around them, as you typed "handling--we see"?',
     'No spaces, as you type it.',
     'Spaces are fine (say how in the note).'),
    ('R-his-warnings-stay',
     'May a warning give an amount, or say what to take instead?',
     'Amounts you wrote stay; I add none.',
     'A warning may give an amount or an alternative where its source supports it, on a card for you first.'),
    ('R-close-read',
     'Before an article goes into your post, every word is read for sense. Do you also want that read tested each time '
     'with planted errors (wrong words slipped in to see whether the read finds them)?',
     'Yes: the close read on every article, and the planted-error test as it is now.',
     'Only the close read; drop the planted-error test.'),
    ('R-contents-order',
     'When an article\'s contents change, do you want fresh readers tested on it ("where would you look first?") every '
     'time, or only when you ask?',
     'Only when you ask.',
     'Every time the contents change.'),
    ('R-studies-where-expected',
     'You suggested asking, at the start of any article, how much research evidence should go into it, and said I '
     'could brainstorm it. '
     'My proposal: one plain question at the start, with three answers: none (your experience and reasoning carry it); a '
     'little, only where a reader would expect a source; or full citations for every claim of fact. The answer decides '
     'whether I look up studies at all, and where.',
     'Ask that one question, with those three answers, at the start of every article.',
     'Something else: say what in the note.'),
    ('R-fixes-searchable',
     'You asked how to make your fixes searchable, maybe as a graph. My proposal: an index of every before-and-after of '
     'yours, one line each, saying what the passage lacked (from the 32 ways your fixes differ from my drafts) and what '
     'you did; before I rewrite a passage, a reader picks from it the fixes closest to that passage by meaning, and I read '
     'those in full. A graph only if the index isn\'t enough.',
     'Build the index that way.',
     'Something else: say what in the note.'),
    ('R-mimic-pangram',
     'You were curious how we could mimic the way Pangram analyzes text statistically. My proposal: our record of Pangram '
     'checks holds hundreds of texts with how each read; train a small stand-in on it, test it on checks it hasn\'t seen, '
     'and if it predicts Pangram well, use it to choose what to fix before spending a check. Never in place of Pangram.',
     'Try that, and report how well it predicts.',
     'Something else: say what in the note.'),
]


def main():
    tree = json.loads((REPO / 'rules' / 'tree.json').read_text(encoding='utf-8'))
    rules = {r['id']: (b, g, r) for b in tree['branches'] for g in b['groups'] for r in g['rules']}
    md = ['# The rule tree: questions still open for you', '',
          'Made 2026-11-28 (turn 76), after your answers on the rules audit. Each rule of [the rule tree](%s) that your '
          'answers left open is here once: the rule as it stands, your words, what I do until you answer (Approve keeps '
          'it), and the other way (Reject takes it). Revise, with a note, for anything else.' % VIEW, '']
    items = []
    for rid, q, yes, no in QUESTIONS:
        b, g, r = rules[rid]
        f = r['fields']
        rule = re.sub(r'\s*\((R-[a-z0-9-]+(?:; R-[a-z0-9-]+)*)\)', '', f['Rule'])
        md += ['## %s' % r['title'], '', '- **Question:** ' + q, '- **The rule now:** ' + rule,
               '- **Your words:** ' + f.get('Why', '(none recorded)'), '- **Until you answer (Approve):** ' + yes,
               '- **The other way (Reject):** ' + no,
               '- **In the tree:** [%s › %s](%s#%s)' % (b['num'] + ' ' + b['title'], g['num'] + ' ' + g['title'], VIEW,
                                                     rid), '']
        items.append({'id': rid, 'group': 'open', 'title': r['title'], 'section': '%s %s, %s %s' % (
                          b['num'], b['title'], g['num'], g['title']), 'whose': '',
                      'blocks': [{'label': 'The rule now', 'paras': [[[rule, '']]]},
                                 {'label': 'Until you answer', 'paras': [[[yes, 'ins']]]}],
                      'fields': [{'label': 'Question', 'text': q}, {'label': 'Your words', 'text': f.get('Why', '')},
                                 {'label': 'The other way', 'text': no}],
                      'links': [{'text': 'This rule in the tree', 'url': '%s#%s' % (VIEW, rid)},
                                {'text': 'These questions on GitHub', 'url': GH + 'docs/rules-audit/2026-11-27/OPEN-QUESTIONS.md'}],
                      'approve': 'keep what I do until you answer: ' + yes[0].lower() + yes[1:],
                      'reject': 'the other way: ' + no[0].lower() + no[1:]})
    text = '\n'.join(md).rstrip('\n') + '\n'
    (AUDIT / 'OPEN-QUESTIONS.md').write_text(text, encoding='utf-8')
    sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
    spec = {'review_id': 'rule-tree-open-20261128', 'title': 'The rule tree: 12 questions still open',
            'source_sha256': sha, 'source_name': 'docs/rules-audit/2026-11-27/OPEN-QUESTIONS.md',
            'repo_file': GH + 'docs/rules-audit/2026-11-27/OPEN-QUESTIONS.md',
            'intro': [md[2]],
            'groups': [{'id': 'open', 'title': 'Questions your answers left open',
                        'intro': 'Approve keeps what I do now; Reject takes the other way; Revise with a note for '
                                 'anything else.',
                        'approve': 'keep what I do until you answer', 'reject': 'the other way'}],
            'items': items}
    (AUDIT / 'OPEN-SPEC.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(items), 'cards; sha', sha[:12])


if __name__ == '__main__':
    main()
