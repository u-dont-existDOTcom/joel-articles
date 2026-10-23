"""Batch 475: recheck A3's red stretch (2026-10-23, after Joel's message of 16:55 UTC) as 4.1 edits for EDITS41.json:
EDITS-b475.json, with CANDIDATES.json (which sample each splice is from, and every fix made to it) and REVIEW-PROMPT.txt.

Recheck A3 (https://www.pangram.com/feed/43889be6-155e-4584-b232-90c4ad70e629, Mostly Human Written, 1.1% AI) read AI only
in "Come all the way back":
- windows 83 to 88 (Low, one Medium): the bring-back script's last three sentences, the count up, and the first three
  lines of the paragraph after it ("When you come out, remind yourself what day (or date) it is. Look to your left and your
  right. Look at something near, and something far.");
- window 93 (Medium): the Note's second sentence ("But if you're coming out, you should not leave yourself in an altered
  state, ...").
Batch 474's lines around them read Human. The whole stretch the red covers, script to Note, went to Emulate (E237, E235):
three samples (bo/, bp/, bq/; BUNDLE.json). bp and bq moved the guide into a hypnotist's voice ("tell the listener",
"leave them"), a known Emulate failure (docs/EMULATE-FALLBACK.md: "it changes person"), so the splices come from bo, which
kept the reader's own first person in the script and "yourself" in the Note, except the count up, where bo turned the
instruction into a script ("Now I will count up and on 5 you will be back") and bp kept it an instruction. Only the red
sentences go back; each fix to a sample's words is listed (spelling, and the meaning put back from the published guide,
master.html). No API check first: the red was Low and Medium, which the API doesn't reproduce (E226, E240), and the
count-up pair's lineage (HG18-B311) has two tries left; the in-place recheck decides.

  python3 articles/inner-signal/humanize/fix-20261023/b475/make_b475.py   (from the repo root)
  then: python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --add articles/inner-signal/humanize/fix-20261023/b475/EDITS-b475.json
"""
import json, pathlib, re

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
PLAIN = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})


def sample(s):
    return (B / s / 'HG-A-return.out.txt').read_text(encoding='utf-8')


def cut(text, first, last):
    a = text.index(first)
    b = text.index(last, a) + len(last)
    assert text.count(first) == 1
    return text[a:b]


# (the sample, its first words, its last words, the fixes as (old, new, why)); TRIAGE_FIXES, from the second reader's
# report (REVIEW.md) as triaged in TRIAGE.json, are applied after these
SPLICES = {
    'script': ('bo', 'All the instructions you have given me', 'with my adult judgement."', [
        ('in to this session', 'into this session', 'spelling'),
        ('with me in to my every day life', 'with me into my everyday life', 'spelling'),
        ('take me in to this state', 'take me into this state', 'spelling'),
        ('adult judgement."', 'adult judgment.”', 'the guide\'s spelling, and its closing quote')]),
    'count': ('bp', 'Then do a count up, e.g. On 1', 'the session is now over.', [
        ('Then do a count up, e.g. On 1', 'Then do a count up: On 1',
         'the published guide gives the five steps as the count, not as an example ("One — ... Five — ...")'),
        ('feel your weight (you can put your weight here if you like)', 'feel your weight (of your choice)',
         'the published "chosen weight": the weight you chose, not a number to put in'),
        ('hear the room around you and know where you are', 'hear the room around you and name where you are',
         'the published "Three — hear the room and name where you are"'),
        ('open your eyes whenever you like, back', 'open your eyes, back',
         'the published "Five — eyes open": the count ends with the eyes open, not whenever the reader likes')]),
    'reorient': ('bo', 'When you come out make sure you remember', 'and something further away.', []),
    'note': ('bo', 'Note: If you are going to sleep to a recording', 'for an indefinite length of time.', [
        ('just remain resting quietly, however', 'just remain resting quietly at the end of it, however',
         'the published "A sleep recording may end in sleep or quiet rest": at the end of the recording'),
        ('with lowered judgement,', 'with lowered judgment,', 'the guide\'s spelling'),
        ('a non specific reset word', 'a non-specific reset word', 'spelling')]),
}
# (old, new) from TRIAGE.json, once the second reader's report is triaged
TRIAGE_FIXES = [[x['replace'], x['with']] for x in json.loads((B / 'TRIAGE.json').read_text(encoding='utf-8'))['applied']]

# what each splice replaces in the working copy (straight quotes, as HUMANIZED-SO-FAR.md has them)
OLD = {
    'script': ('All instructions you have given me to carry me deeper in this session or to keep me in this state are now '
               'finished. The only instruction I will take with me into my everyday life, or the only cue I will use to take '
               'me into this state in the future, is the one I consciously choose to, and neither of them keeps me in this '
               'state. When I come out of this session, I will be me, in my body, with my adult judgment."'),
    'count': None,  # the whole count-up line
    'reorient': ('When you come out, remind yourself what day (or date) it is. Look to your left and your right. Look at '
                 'something near, and something far.'),
    'note': None,  # the whole Note line
}
LINE_FIRST = {'count': 'Then count up, using these five steps:', 'note': "Note: If you're going to sleep to a recording"}
KEYS = {'script': 'HG18-b475-script', 'count': 'HG18-b475-count', 'reorient': 'HG18-b475-reorient', 'note': 'HG18-b475-note'}
FROM = {'script': 'the script\'s last three sentences from sample bo (bp and bq moved it out of the reader\'s first person)',
        'count': 'the count up from sample bp (bo turned the instruction into a script: "Now I will count up and on 5 you will be back")',
        'reorient': 'the paragraph\'s first three lines, as one sentence, from sample bo',
        'note': 'the Note from sample bo ("yourself" kept; bp and bq wrote "leave them" and "the listener")'}


def line(md, first):
    a = md.index(first)
    assert md.count(first) == 1, first
    return md[a:md.index('\n', a)]


def build():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    cands, edits = {}, []
    for k, (s, first, last, fixes) in SPLICES.items():
        new = cut(sample(s), first, last)
        done = []
        for a, b, why in fixes:
            assert new.count(a) == 1, (k, a)
            new = new.replace(a, b)
            done.append({'replace': a, 'with': b, 'why': why})
        reviewed = new  # the text the second reader saw (REVIEW-PROMPT.txt); the triage's fixes come after
        for a, b in TRIAGE_FIXES:
            if a in new:
                new = new.replace(a, b)
                done.append({'replace': a, 'with': b, 'why': 'the second reader (REVIEW.md, TRIAGE.json)'})
        old = OLD[k] if OLD[k] else line(md, LINE_FIRST[k])
        assert md.count(old) == 1, (k, old[:60])
        cands[k] = {'sample': s, 'from': FROM[k], 'old': old, 'new': new, 'reviewed': reviewed, 'fixes': done}
        edits.append({'key': KEYS[k], 'section': 'HG18', 'source': 'Emulate (E237, E235), three samples of the stretch '
                      '(b475/bo, bp, bq); ' + FROM[k], 'batch': '475', 'old': old, 'new': new.translate(PLAIN),
                      'paragraph_check': None,
                      'paragraph_result': 'no API check: the red was Low and Medium (E226, E240); read in place in recheck A4',
                      'section_check': None, 'section_result': 'read in place in recheck A4',
                      'review': 'fix-20261023/b475/REVIEW.md', 'fixes': done})
    (B / 'CANDIDATES.json').write_text(json.dumps(cands, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'EDITS-b475.json').write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return md, cands


PUBLISHED = {
    'script': ('“I bring back only what is useful now.\nThe rest can remain safely held until there is more capacity.\nI '
               'return to the room, the body, the day, and one honest action.\nAll instructions to deepen or remain in this '
               'session are finished. I keep only the ordinary-life intention or future-practice cue I consciously chose; '
               'neither keeps today’s altered state running.\nI am myself, in my body, with adult judgment fully available.”'),
    'count': ('One — feel the body’s contact and chosen weight.\nTwo — let the breath return to its ordinary rhythm.\nThree — '
              'hear the room and name where you are.\nFour — move fingers, toes, shoulders, and eyes.\nFive — eyes open, '
              'present, ordinary, clear. The session has ended.'),
    'reorient': ('Name the day or date. Look left, right, near, and far. Move before standing, and stand only when steady. '
                 'Check that you are actually oriented and alert; repeating the count is not proof of a complete return. '
                 'Note only what actually appeared, and any action it calls for. Then do something normal.'),
    'note': ('Sleep is separate. A sleep recording may end in sleep or quiet rest. A waking recording shouldn’t end by '
             'preserving a role, reduced judgment, impaired movement, blankness, an undefined reset word, or an invitation to '
             'remain altered indefinitely.'),
}


def prompt(md, cands):
    # the section with all four splices in, so each item's BEFORE and AFTER are its neighbours as they will read
    for k in ('script', 'count', 'reorient', 'note'):
        md = md.replace(cands[k]['old'], cands[k]['reviewed'].translate(PLAIN))
    sec = md[md.index('# Come all the way back'):md.index('# The actual inner meeting')]
    paras = [p for p in sec.split('\n') if p.strip()]
    items = []
    names = {'script': 'the end of the generic bring-back script, which the reader says to themselves',
             'count': 'the count up out of trance, right after the script',
             'reorient': 'the first sentence of the paragraph after the count up',
             'note': 'the Note at the end of the section, about sleep recordings'}
    for n, k in enumerate(('script', 'count', 'reorient', 'note'), 1):
        c = cands[k]
        new = c['reviewed'].translate(PLAIN)
        k_para = next(i for i, p in enumerate(paras) if new in p)
        now_para = paras[k_para]
        before = paras[k_para - 1] if k_para > 0 else '(the heading "Come all the way back")'
        after = paras[k_para + 1] if k_para + 1 < len(paras) else '# The actual inner meeting'
        items.append('## Item %d (%s)\n\nBEFORE:\n%s\n\nPUBLISHED:\n%s\n\nNOW:\n%s\n\nAFTER:\n%s\n' % (
            n, names[k], before, PUBLISHED[k], now_para, after))
    head = (
        "You check 4 rewritten passages of Joel's long self-hypnosis guide (how to learn self-hypnosis safely, with inner "
        "child and parts work, and many safety cautions). All four are in its section \"Come all the way back\", the return "
        "from trance: a script the reader says to themselves, a count up, how to check you are fully back, and a note on "
        "sleep recordings. The guide is self-guided: the reader leads themselves, reading it or using a recording they "
        "made, so \"you\" is the reader and \"I\" in the script is the reader too. Each NOW is a detector-passing rewrite "
        "(only part of each NOW paragraph changed; the rest read human already); PUBLISHED is the guide as he published it, "
        "the meaning to keep. Safety cautions and steps matter most.\n\n"
        "For each item, say in a few words each:\n"
        "1. MEANING: does NOW keep every point, step, caution and claim of PUBLISHED, with the same strength (nothing made "
        "more or less certain or more optional, no instruction turned into a suggestion, no safety caution weakened, no "
        "step lost, nobody else brought in to do what the reader does)? KEPT, or what CHANGED or was LOST, and anything "
        "ADDED that a reader would take as a claim.\n"
        "2. SENSE: would a reader understand NOW in its place, between BEFORE and AFTER? OK, or the words that stop them "
        "and why.\n"
        "End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning and sense only, not style or "
        "grammar (the casual grammar, the run-on sentences and comma splices are on purpose), and suggest the smallest "
        "possible rewrite only for a problem you report.\n\n"
        "Write your report with a single Write call to `%s`, one \"## Item N\" part per item, then reply with only the "
        "verdicts, one line per item. Don't read any other file, don't run commands, and don't use the web.\n\n" % (B / 'REVIEW.md'))
    (B / 'REVIEW-PROMPT.txt').write_text(head + '\n'.join(items), encoding='utf-8')


if __name__ == '__main__':
    md, cands = build()
    prompt(md, cands)
    print('EDITS-b475.json: %d edits; REVIEW-PROMPT.txt written' % len(cands))
