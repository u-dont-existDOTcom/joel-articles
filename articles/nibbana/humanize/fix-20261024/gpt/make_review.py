"""REVIEW.md: my read of every change in Joel's GPT edit of 2026-10-24 against the eighth recheck's text (2026-10-24).

  python3 articles/nibbana/humanize/fix-20261024/gpt/make_review.py   (after diff_gpt.py)
"""
import difflib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
CUTS = {47: 2, 66: 3, 70: 4, 74: 6, 77: 7, 92: 11, 107: 12, 128: 13, 137: 14, 147: 15, 159: 16, 252: 20, 269: 23}
NOTES = {
    62: 'The Vinaya sentence in three sentences instead of one with dashes; the same facts.',
    63: '"made life without a hidden observer imaginable enough to practice toward" in plainer words; "framed as sitting inside" is "described as being inside"; the same point.',
    68: 'MN 121\'s sentence reordered; "tellingly" is now "is telling"; the same point.',
    70: 'Besides your cut: "did so with some cultivation of" is "cultivated some", and "although not always before" is "though they didn\'t all do that before"; the same claim.',
    77: 'Besides your cut: "Literal translations are narrower and actually clearer, explaining" is "The literal translations say less, but they\'re actually clearer about", and the last sentence is split; the same claims.',
    129: '"soteriology" is "teaching on liberation": a plainer word.',
    134: 'Two edits: GPT\'s first pass reworded the second half ("Besides that ease and joy from recollection, I find that unification can also loosen physically"), and a style edit added "describes a different route to ease and joy"; that framing is GPT\'s, and it fits the next sentence.',
    147: 'Besides your cut: the constructed-functioning sentences in fewer words, and "saṃsāric" defined the same way.',
    155: 'Emulate\'s sentence from batch n6 in GPT\'s plainer words ("That\'s different from the usual viññāṇaṃ ..."); the duality is still there ("when one thing perceives another").',
    159: 'Besides your cut: dashes are parentheses, and one semicolon is a new sentence.',
    161: '"My own plain-language addition:" is "I\'d add this in plain language:".',
    166: 'One sentence split in two.',
    172: 'The neutrality-versus-bliss sentence reordered ("You might expect neutrality ..., but what seems to be left is supreme bliss."); the same claim.',
    178: '"a body in it that is made of matter that changes in time from moment to moment" is "a body made of matter that changes from moment to moment": "in it" and "in time" go, and the sense stays.',
    184: '"comes at ultimate reality from a more unified lens than me" is "takes a more unified view of ultimate reality than I do".',
    186: 'One sentence split in two.',
    196: '"Regarding the self," is gone from the start; the sentence says the same.',
    201: 'Sentences split; "although" is "though" (your N6 18, kept).',
    214: '"For this article, the first stage is the one that matters." is "I\'m focusing on the first stage here."',
    215: 'Reworded throughout, and the parenthesis that listed the realization again is gone (the sentence before lists it); your N6 19 is kept, as its own sentence.',
    222: '"durable" is "lasting".',
    226: 'The question from batch n6 in GPT\'s words ("as a coherent picture rather than just a set of concepts"); the same question.',
    233: '"SN 22.95 shows us how form is empty" is "In SN 22.95, form is empty", with a semicolon.',
}
STYLE = {59: 1, 67: 2, 113: 3, 134: 4, 147: 5, 207: 6, 225: 7, 230: 8, 232: 9, 259: 10}
STYLE_NOTES = {
    59: 'The same three things, as verbs ("Being less selfish, grasping less, and getting better at loving").',
    67: '"he" is "the Buddha": the sentence before talks about John, so it\'s clearer.',
    113: '"help the development of" is "help develop".',
    207: 'The four protections in a different order of words; the same four. GPT noted its own voice reviewer preferred yours here.',
    225: 'The AN 11.12 clause in fewer words; the same point.',
    230: '"rebirth is seen as" is "Buddhists see rebirth as", and "lighting another" is "light another" (a grammar fix). The sentence after it has a slip that was already there; see question N7.',
    232: 'Two sentences joined ("Reasoning can make you doubt the dream, but the event made that doubt impossible to reverse.").',
    259: 'Your N6 22, kept, as two sentences ("I\'d put most of the emphasis on ...").',
}


def wdiff(a, b):
    a, b = a.split(), b.split()
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != 'equal':
            out.append('~~%s~~ **%s**' % (' '.join(a[i1:i2]), ' '.join(b[j1:j2])) if i2 > i1 and j2 > j1 else
                       ('~~%s~~' % ' '.join(a[i1:i2]) if i2 > i1 else '**%s**' % ' '.join(b[j1:j2])))
    return ' · '.join(out)


def main():
    d = json.loads((HERE / 'DIFF.json').read_text(encoding='utf-8'))
    final = {c['line']: c for c in d['Nibbana_Updated_Draft.txt']['changed'] if c['line'] != 76}
    out = ['# Your GPT edit of the Nibbāna article, change by change', '',
           'Your message of 2026-10-24 19:52 UTC: "i had GPT apply all the nibbana cuts for you to save your credits, and it '
           'also fixed some other ai tells it saw, i checked the output and it\'s 100%% human on pangram. so save the result". '
           'Saved: it is the working copy now (batch n8), with every link, picture and heading as they were. GPT worked '
           'from the eighth recheck\'s draft, which had read 100%% Human itself. %d paragraphs changed: your 13 cuts (N6), '
           'GPT\'s own edits in %d paragraphs (%d of them where your cuts were), and its ten style edits. No heading, caption or picture changed. Your 10 '
           'keeps are all there; three are reworded (your 18, 19 and 22). I read every change against your text: each keeps '
           'your meaning. One slip was already there before GPT: question N7.' % (
               len(final), len(NOTES), len([n for n in NOTES if n in CUTS])), '',
           'Each change: ~~what went~~ **what came in**.', '']
    for n in sorted(final):
        c = final[n]
        what = []
        if n in CUTS:
            what.append('your N6 %d cut' % CUTS[n])
        if n in NOTES:
            what.append('GPT\'s edit')
        if n in STYLE:
            what.append('style edit %d' % STYLE[n])
        out += ['### %s' % ' and '.join(what), '', wdiff(c['ours'], c['gpt']), '']
        note = ' '.join(x for x in (NOTES.get(n), STYLE_NOTES.get(n)) if x)
        if note:
            out += ['My read: ' + note, '']
    (HERE / 'REVIEW.md').write_text('\n'.join(out), encoding='utf-8')
    print('REVIEW.md: %d paragraphs' % len(final))


if __name__ == '__main__':
    main()
