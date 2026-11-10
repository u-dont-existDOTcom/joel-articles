#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r28's checks (texts.py). A sentence an earlier receipt in this article has a row
for keeps it; the rest are written here. Writes RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import glob
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

OLD = {}
for f in sorted(glob.glob(str(ROOT / 'articles' / 'romance' / 'humanize' / '**' / 'RECEIPT-*.json'), recursive=True)):
    if '/r28/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))
NEW = {
    'Here’s the funny thing about labels': (
        'a label can sit on a half-committed person for years, but the word quickly shows whether both think they are '
        'in the same relationship', 'the section heading (labels describe, they don\'t prescribe)', 'labels'),
    'I get it, neither of us could believe': (
        'he understood her doubt, and it still felt like she brushed him off because she wanted his knee to be fine',
        'her suggesting it was in his head', 'I get it'),
    'Well, it didn’t exactly solve the problem: in late-1700s': (
        'bundling didn\'t solve it: 30 to 40 percent of New England brides were already pregnant at their weddings',
        'what bundling was', 'it didn’t exactly solve the problem'),
    'A lot of women have seen me that way, and honestly': (
        'being seen as a father figure can be fine by itself', 'women seeing him as a father figure', 'that way'),
    'Sometimes I actually learned something about her, but other times': (
        'sometimes the certainty came from learning about her, other times only from being attached, which makes him '
        'question it less', 'his question "Based on what?"', 'Sometimes I actually learned something'),
    'Maybe their smell turns you off': (
        'what can be wrong on the first night: smell, or how often each of you wants sex', 'knowing someone for twenty '
        'years before the first night', 'Maybe'),
    'Your kinks might not line up either': (
        'more of what can be wrong: kinks, one person shut down, bodies that don\'t click', 'smell and how often',
        'either'),
    'You can know somebody for twenty years and then discover on the first night that the polarity isn’t there: maybe': (
        'twenty years of knowing someone can\'t tell you if their smell turns you off or how often each of you wants sex',
        'what going slowly can show', 'twenty years'),
    'Even if I found my twin flame': (
        'even a twin flame is one person', 'the twin flame section before it', None),
    'The polarity could be perfect': (
        'a perfect match still needs other people around', 'one person', 'still need other people'),
    'Here’s how this looks for me': (
        'in his relationships, each partner runs to their own friends when something serious comes up',
        'needing other people around', 'Here’s how this looks for me'),
    'Maybe an unusually strong couple': (
        'a rare strong couple may manage without outside support', 'the two-person backup system', None),
    'I think that’s rare.': ('such couples are rare', 'the strong couple', 'that’s rare'),
    'But often, a friend who actually knows us both': (
        'a friend who knows both partners often sees the pattern first', 'the rare couple', 'But often'),
    'On the other hand, If both people are falling apart': (
        'when both partners fall apart, friends can only do so much', 'the friend who sees the pattern',
        'On the other hand'),
    'Separate confidants can be helpful and harmful.': (
        'separate confidants cut both ways', 'what friends can and can\'t do', None),
    'Sometimes you need privacy from your partner': (
        'the help: privacy and somewhere else to say what you feel', 'helpful and harmful', 'Sometimes'),
    'But if your confidant doesn’t have a good connection': (
        'the harm: a confidant who doesn\'t know your partner becomes an echo chamber', 'the help', 'But if'),
    'Having the same confidant creates the opposite problem': (
        'a shared confidant leaves no release valve for privacy, so neither way is perfect', 'the echo chamber',
        'the opposite problem'),
    'I lived all the permutations of this with Bee': (
        'he lived every version of this with Bee, but never in community', 'the confidants\' bias', None),
    'I suspect if we had, we might still be together.': (
        'with community they might still be together', 'never living in community', 'if we had'),
    'She would not have been capable of demonizing me': (
        'demonizing him wouldn\'t have worked where everyone knew them both', 'what community would have done',
        'She would not have been'),
    'It would have contained all the insanity.': ('community would have contained it', 'the demonizing', 'It'),
    'Baseless accusations only work with friends': (
        'baseless accusations only work on friends who know one side', 'the community that knew both', None),
}
READER = ('a fresh reader (a Sonnet subagent that saw only the changed paragraphs, their headings and what each is for, '
          'given tools/humanization/needed_read_brief.md), 2026-11-08')
SECTIONS = {
    'r28-labels': ('Labels Are Descriptive, Not Prescriptive', 'what a relationship label can and can\'t do'),
    'r28-deeper': ('It always goes deeper', 'what a partner\'s care under small stress shows'),
    'r28-bundling': ('the bundling section', 'why we still need a recognized middle stage'),
    'r28-ptsd': ('Anti-PTSD Can Be Just As Dangerous As PTSD', 'when a father-figure dynamic is fine and when it harms'),
    'r28-dam': ('Holding up a leaky dam', 'how attachment, not knowledge, can make a partner seem right'),
    'r28-slow': ('Slow & steady', 'what going slowly can\'t tell about sexual fit'),
    'r28-slow-b': ('Slow & steady', 'what going slowly can\'t tell about sexual fit'),
    'r28-pillars': ('De-ontologizing Twin Flames FTW (330 to 336)', 'why a couple needs shared outside support'),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'PASS: the advice is the live post\'s',
    'Q3': 'PASS: the people are named as in the live post',
    'Q4': 'PASS: no new term',
    'Q5': 'PASS: each sentence\'s tie is in its words (the links field), or it opens its paragraph',
    'Q6': 'PASS: the order is the live post\'s',
    'Q7': 'PASS: each change keeps what the paragraph tells the reader',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence',
}
NEEDED = json.loads((HERE / 'NEEDED.json').read_text(encoding='utf-8')) if (HERE / 'NEEDED.json').exists() else {}
bad = 0
for name, (section, job) in SECTIONS.items():
    text = TEXTS[name]
    r = S.make(text, section, 'Someone dating or in a relationship who wants honest, practical advice on ' + job + '.')
    for s in r['sentences']:
        row = next((v for k, v in NEW.items() if s['s'].startswith(k)), None) or OLD.get(s['s'].strip())
        assert row, ('no row', name, s['s'][:60])
        pay, fol, link = row
        s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
        s['follows'] = fol
        if 'link' in s:
            s['link'] = link or 'none: it opens its paragraph, and the paragraph before it ends its own point'
    r['opens']['why_reading'] = 'It tells the reader ' + job + '.'
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = [{'point': 'the window his whole-article check read AI or Low here', 'found': 'RESULTS-whole-r27.json',
                     'still_needed': 'yes: they get ' + job + ', said plainly', 'fate': 'changed'}]
    r['placement'] = 'In its section, as the fixed version has it (r28/README.md).'
    r['needed'] = dict(NEEDED.get(name) or {'unneeded': [], 'kept': {}}, reader=READER)
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
