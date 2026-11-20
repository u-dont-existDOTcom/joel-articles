#!/usr/bin/env python3
"""build.py - turn 50's texts for Pangram (batch h58a and after), made the way h57's build_baseline.py makes them.

- His two points of 2026-11-20 00:01 UTC on turn 49's fixes, each a try from that paragraph's last Human High check:
  "Sensitivity varies." back in DMSO's nausea line, with what to do about it ("we can explain they should try less at
  first because of that"); niacin's liver line tied to sustained-release niacin and to regular niacin spread through the
  day, not to niacin in general ("the niacin risk is for extended release ... unless you take it thru the day to make it
  ER").
- The paragraph he left to fix in Dealing With Shadow Thoughts ("you can try to fix p5": B415, "During a trip, don't
  identify ..."), checked by itself as it stands first (lesson 19b).

Each try is a list of (block, old words, new words) on the guide's Markdown, so the text checked and the text that goes in
are the same.

  python3 build.py h58a      writes TEST-KEY.txt, MD-KEY.md and ITEMS-h58a.json ([[key, text, sha256], ...])
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / 'h57-20261119'))
import build_baseline as BB  # noqa: E402

BLOCKS = {b['id']: b for b in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}

# key: (blocks, scope, what and where), as BB.UNITS
UNITS = dict(BB.UNITS)
UNITS.update({
    'a01-trip-shadow': (['B415'], 'paragraph',
                        "Dealing With Shadow Thoughts' during-a-trip paragraph (B415, after his rewrite of the section) by itself"),
})

BATCHES = {'h58a': ['a01-trip-shadow', 'b01-dmso-side', 'b02-niacin-side']}

# key: (unit it starts from, [(block, old, new), ...], what changed and why)
TRIES = {
    'b01-dmso-side': ('a06-dmso-side', [
        ('B203', 'dilute it in water, juice, or milk and sip gradually.',
                 'dilute it in water, juice, or milk and sip gradually. Sensitivity varies, so try a small amount at first.')],
        'his line back, as he asked ("don\'t cut \'sensitivity varies\'"), with what the reader does about it in his words '
        '("we can explain they should try less at first because of that"), "less" said as "a small amount" (the read '
        'against his fixes: less than what?); from b06 (21a95b3c, Human High 179)'),
    'b02-niacin-side': ('a07-niacin-side', [
        ('B214', 'Higher or repeated doses can create a real risk of liver damage,',
                 '[Sustained-release niacin](https://pubmed.ncbi.nlm.nih.gov/8309029/), or repeated doses through the day, '
                 'can create a real risk of liver damage,')],
        'the liver risk said where it is, as he said it ("the niacin risk is for extended release ... unless you take it '
        'thru the day"): sustained-release niacin (McKenney et al. 1994, JAMA: hepatotoxic effects in 12 of 23 on '
        'sustained-release, none of 23 on immediate-release at the same doses, up to 3 g a day), or his "repeated doses" '
        'said as through the day; "Higher" out, since regular niacin taken at once is not where the risk is. From b07 '
        '(7ef96156, Human High 57)'),
}


# batch h58b: from DMSO's near miss (b06, Human High 179, the guide's text; b01 read his line and the rats line Human
# Medium, 9 and 8 words: fb34d3fb), a word or two each; and the first tries at B415, which read AI High in one window
# over the whole paragraph (a01, ee4961ce), so no near miss to start from: his four don'ts unpacked the way his round-43
# rewrite of the section before it unpacked "I also notice them after excessive focus" into reasons and examples
B415_OLD = ("During a trip, don't identify with every shadow thought, suppress it, confess it to everybody, or convert it into "
            "a permanent diagnosis. Notice: ")
TRIES.update({
    'c01-dmso-side': ('a06-dmso-side', [
        ('B203', 'dilute it in water, juice, or milk and sip gradually.',
                 'dilute it in water, juice, or milk and sip gradually. Sensitivity to DMSO varies, so start with less '
                 'than you planned.'),
        ('B203', 'In rats, higher doses made sleep less deep', 'In rats, higher doses of DMSO made sleep less deep')],
        'his line with what to do (b01), and in the two Medium windows of b01 a word or two a reader could take two ways: '
        'sensitivity to what ("to DMSO"), and less than what, his "try less" said against what they planned ("start with '
        'less than you planned"; the reads: "a small amount" gave no measure); higher doses of what ("of DMSO")'),
    'c02-dmso-side': ('a06-dmso-side', [
        ('B203', 'dilute it in water, juice, or milk and sip gradually.',
                 'dilute it in water, juice, or milk and sip gradually, starting with less than you planned, since '
                 'sensitivity varies.'),
        ('B203', 'In rats, higher doses made sleep less deep', 'In rats, higher doses of DMSO made sleep less deep')],
        'his line joined to the sentence it belongs to, the act first and his reason after it (his round-43 joins), so it '
        'isn\'t a short line on its own; higher doses of what ("of DMSO")'),
    'd01-trip-shadow': ('a01-trip-shadow', [
        ('B415', B415_OLD,
         "During a trip, try not to take every dark thought that comes up as the truth about you, since it's often just "
         "the flip side of whatever you've been focusing on. Pushing the thought away tends to make it come back stronger, "
         "so let it be there. You can tell the person sitting with you, but maybe hold off on confessing it to everybody "
         "else, or deciding it means something is permanently wrong with you. Just notice what's there: ")],
        'the four don\'ts unpacked, each with its reason from his rewrite of the section before it (the opposite shows '
        'up where you focus; "ignoring problems only makes them worse"), the last two as a hedged don\'t (his fifth '
        'fix); "identify with" said as taking it as the truth about you, "suppress" as pushing the thought away, '
        '"convert it into a permanent diagnosis" as deciding something is permanently wrong with you; after the three '
        'reads: "shadow thought" said as a dark thought that comes up, "the other half of a pair" as the flip side of '
        'what you\'ve been focusing on, the sitter told apart from "everybody else", the "it"s named. The script and his '
        'room-first line (OWNER-EDITS q5-room-first) as they are'),
    'd02-trip-shadow': ('a01-trip-shadow', [
        ('B415', B415_OLD + '**"A thought is here. A feeling is here. It is intense, but it is not the whole of me."** Then return to '
                 'room, body, human, time, and love.',
         "During a trip, try not to take every dark thought that comes up as the truth about you. It's often just the flip "
         "side of whatever you've been focusing on, and pushing it away tends to make it come back stronger. You can tell "
         "the person sitting with you, but maybe hold off on confessing it to everybody else, since a trip is about the "
         "worst time to decide something is permanently wrong with you. Just notice what's there, maybe saying to yourself, **\"OK, "
         "there's a thought, and there's a feeling, and it's intense, but it's not all of me.\"** Then come back to the room "
         "you're in, your body, the person with you, what time it is, and love.")],
        'd01 read AI High over the whole paragraph, the script and his room-first line included (1eac3d57: "A feeling is '
        'here." AI Medium on its own, the script\'s last line and the room line AI High): the script\'s three lines, '
        'built the same way, said as one breath a person says to themselves, and the room line\'s five category words as '
        'the five things to come back to, room still before body (his Q-5 decision); d01\'s unpacking of the don\'ts with '
        'the reasons said as what happens, and the diagnosis as deciding something is permanently wrong with you, the '
        'slack in its reason'),
})
BATCHES['h58b'] = ['c01-dmso-side', 'd01-trip-shadow']
BATCHES['h58c'] = ['d02-trip-shadow']

# batch h58d: B415's third try, after the tell panel on d02 (panel-d02/PANEL.md: S2 to S5 agreed, and both readers on the
# whole: an even sequence of sentences of one length, no specific detail or rough edge)
B415_ALL = B415_OLD + ('**"A thought is here. A feeling is here. It is intense, but it is not the whole of me."** Then return to '
                       'room, body, human, time, and love.')
TRIES['d03-trip-shadow'] = ('a01-trip-shadow', [
    ('B415', B415_ALL,
     "During a trip, a dark thought can show up that feels like the plain truth about you, like suddenly hating someone you "
     "love, or being sure you're a fraud. It's usually not the truth, just the opposite of whatever you were trying so "
     "hard to feel, coming into focus. Don't shove the thought down, because it'll just come back louder. Tell the person "
     "sitting with you if you "
     "want to, but don't go texting your whole family about it at 3 a.m., and don't decide you've got some lifelong "
     "disorder either. Just notice the thought and the feeling that came with it. They're intense, sure, but they aren't "
     "all of you. Then come back to the room you're in, your body, the person with you, what time it is, and, when you can, "
     "to love.")],
    'the panel\'s agreed tells on d02 fixed, and its point on the whole: what a shadow thought is, shown (hating someone you '
    'love, being sure you\'re a fraud); the reason said as his section says it ("dark stuff coming into focus"); the '
    'confession said as something from the reader\'s own night (texting your whole family at 3 a.m.), the diagnosis as a '
    'lifelong disorder; the script said as what to notice, in sentences of different lengths; love after the four '
    'concrete things, room still before body (his Q-5 decision)')
BATCHES['h58d'] = ['d03-trip-shadow']

# batch h58e: his own paragraphs that read below High by themselves in h57a, a word or two each from that check (lesson
# 19b), to go to him on round 44's card since the words are his
TRIES.update({
    'e01-aftermath': ('a18-aftermath', [
        ('B425', 'When symptoms linger, people', 'When symptoms linger after a trip, people'),
        ('B425', 'psychological and/or physiological patterns', 'psychological or physical patterns')],
        'the two Medium windows of a18 (522cc1a4): symptoms of what ("after a trip"); "and/or physiological" said as "or '
        'physical", the plain word'),
    'e02-ss-recognize': ('a23-ss-recognize', [
        ('B132', 'We can use the same Hunter criteria that clinicians use to diagnose serotonin syndrome.',
                 'We can use the Hunter criteria, the same checklist clinicians use to diagnose serotonin syndrome.')],
        'the Medium window of a23 (67e584da), the heading with his first sentence: "Hunter criteria" explained where it is '
        'first used ("the same checklist clinicians use"), his second way'),
    'e03-first-five': ('a24-first-five', [
        ('B236', 'If they want to go confront somebody, that can wait.',
                 'If they want to go confront somebody, that can wait until tomorrow.')],
        'the Medium window of a24 (189231bd), his confront line: wait how long ("until tomorrow", the guide\'s "No big '
        'actions until morning")'),
    'e04-redefining': ('a14-redefining', [
        ('B330c', 'Samsara offers no shortage', 'Samsara, the cycle of ordinary existence, offers no shortage'),
        ('B330c', 'to reduce present-moment trauma so we can address what was already there.',
                  'to reduce the trauma the trip itself is causing, so we can address what was already there.'),
        ('B357', 'makes the blockage visible:', 'shows us what\'s blocking it:')],
        'the AI and Low windows of a14 (3b646eb8): "Samsara" explained where it is first used; "present-moment trauma" said '
        'as the trauma the trip itself is causing (the fit read: "the trauma happening now" read fast called the reader\'s rough trip trauma); in my line after his paragraph, "the blockage" (which?) said as what\'s blocking it'),
})
BATCHES['h58e'] = ['e01-aftermath', 'e02-ss-recognize', 'e03-first-five', 'e04-redefining']


def md_of(i):
    return BB.md_of(i) if hasattr(BB, 'md_of') and not i.startswith(('B', 'N-', 'R', 'H')) else BLOCKS[i]['md']


def unit_text(ids, md=None):
    md = md or {}
    return '\n\n'.join(BB.plain(md.get(i, BLOCKS[i]['md'])) for i in ids).strip() + '\n'


def edited(base, edits):
    ids = UNITS[base][0]
    md = {i: BLOCKS[i]['md'] for i in ids}
    for b, old, new in edits:
        assert md[b].count(old) == 1, (b, old)
        md[b] = md[b].replace(old, new)
    return ids, md


def write(key, text, md=None):
    (HERE / ('TEST-%s.txt' % key)).write_text(text, encoding='utf-8')
    if md is not None:
        (HERE / ('MD-%s.md' % key)).write_text('\n\n'.join(md.values()) + '\n', encoding='utf-8')
    t = text.strip()
    return [key, t, hashlib.sha256(t.encode('utf-8')).hexdigest()]



def main(batch):
    items = []
    for key in BATCHES[batch]:
        if key in TRIES:
            base, edits, _ = TRIES[key]
            ids, md = edited(base, edits)
            items.append(write(key, unit_text(ids, md), md))
        else:
            items.append(write(key, unit_text(UNITS[key][0])))
        print(key, len(items[-1][1].split()), 'words', items[-1][2][:12])
    (HERE / ('ITEMS-%s.json' % batch)).write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1])
