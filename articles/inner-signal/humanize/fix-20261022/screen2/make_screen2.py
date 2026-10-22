"""The second screening post (2026-10-22): Appendix C's general checklist, before any meaning work, and the Appendix B
stretch read with it.

The first screening (../screen/, Joel's result link of 21:41 UTC) read neither Appendix C sample Human. Sample bg (S5) read
Human from its list of tricks to the good guide, and AI in its opening: the line on when to use the checklist, the
statement to say, and the four tests (truth and questions, love and boundaries, guidance and sleep, what is for me and the
adult self), and in its last sentence ("Therefore, no will be framed as bad ..."). Sample bh (S6) read AI nearly
throughout. In the recheck of 2026-10-21, the installed prose (batch 469g) read AI, high, as part of one 518-word window
that ran from Appendix B's list of what Joel won't use NLP for, through the NLP sequence, into Appendix C's first five
paragraphs; its last two paragraphs (slow down, the good guide) read Human, high. So this post reads four samples, in this
order, each under a heading of its own (the check doesn't read headings):

  B0  Appendix B's stretch as installed now (batch 471g in): the last items of "What I will not use NLP for", the outline's
      lead-in and the NLP sequence. Is the red window's first half Appendix B's?
  C0  Appendix C as installed now (469g), right after B0, as in the guide. Is it red without the shared window?
  C1  a new opening, then bg's middle (its tricks list, other things to notice, the child; two words put back: "a
      betrayal" for "a bad thing about you", "scared" for "terrified"), then C0's last two paragraphs, which read Human,
      high, in the recheck. The opening's diagnosis: three litanies in a row (six sources of pressure, six "I can" moves,
      four maxims of one shape) read AI in every version; here the moves are said as a person says them, with a question
      and its short answer among the tests, two tests in one sentence, and the last test as a plain warning, the shapes
      that read Human, high, in C0's last two paragraphs ("And can they take your no? A bad guide can't.").
  C2  another new opening with the same middle and end. Its diagnosis: the known names for what the opening describes
      ("the sniff test", "the voice in your head"), a test that carries its own logic ("Real guidance keeps overnight, so
      sleep on it"), and the questions of the statement asked plainly, one of them left elliptical.

C1 and C2 are the fifth and sixth tries at the opening (the published text, 469g's prose, bg and bh were the first four;
the six-try rule, docs/HUMANIZATION-GATE.md). If neither reads Human, the question goes back to Joel.

  python3 articles/inner-signal/humanize/fix-20261022/screen2/make_screen2.py   (from the repo root)
Writes CANDIDATES.json (each sample's paragraphs), PAYLOAD-S2.html (pasted into the screening draft by
../screen/paste_payload_lane.js), TEXT-S2.txt (the text the check will read), SPANS-S2.json and WORDS-S2.json.
"""
import hashlib, html, json, pathlib, re, sys

S = pathlib.Path(__file__).resolve().parent
H = S.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

BG = H / 'fix-20261018' / 'emu-bg' / 'HG32-pr1.out.txt'
BG_SHA = '15590db9eca43bec3d6c921551ceff54d95100a10b4cc4c8431df0b65c69bf72'
OPEN = '<div dir="auto" class="body markup">'
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})

C1_OPENING = [
    'Use this checklist when something is pressing on you too hard. It could be a person, an ad, an ideology or some '
    'spiritual teaching, a romantic pull, a voice inside you, anything like that. You can tell yourself something like, '
    '“Okay, I’m being influenced here. I don’t have to obey it. I don’t have to attack it either. I can slow down for a '
    'minute and ask what it’s taking for granted, and who it benefits. My body’s telling me something, but I won’t assume '
    'I know what it proves. And what would love, truth, humility and ordinary life need from me?”',
    'Then test it a little. Can it handle your questions? Something true can. Love can live with your boundaries, and real '
    'guidance will still be there after you sleep on it. If it asks you to give up your adult self, it’s not for you.',
]
C2_OPENING = [
    'Here’s my checklist for when something is leaning on you too hard: a person, an ad, an ideology, a spiritual teaching, '
    'a romantic pull, the voice in your head. Say to yourself something like, “Okay, this is influence. I don’t have to '
    'obey it, and I don’t have to fight it. I can slow way down and ask what it takes for granted and who gets something '
    'out of it. My body is saying something too, but I won’t assume I know what it proves. What would love want here? '
    'What would truth, or humility, or my ordinary life?”',
    'Then give it the sniff test. True things can stand up to questions. Love can take a boundary. Real guidance keeps '
    'overnight, so sleep on it. And whatever is really for you won’t ask you to give up your adult self.',
]
# bg's middle, with the two words the published list has put back
MIDDLE_FIXES = [('Is questioning being framed as bad (a bad thing about you)?', 'Is questioning being framed as bad (a betrayal)?'),
                ('Is your inner child being seduced, terrified, rescued?', 'Is your inner child being seduced, scared, rescued?')]


def appendix(md, title):
    m = re.search(r'\n# %s[^\n]*\n' % re.escape(title), md)
    e = md.find('\n# ', m.end())
    return m.group(0).strip('\n# '), md[m.end():e]


def paras_of(chunk):
    """(heading?, plain text) for each block of a Markdown stretch, the way the post shows it."""
    out = []
    for b in [b.strip() for b in chunk.split('\n\n') if b.strip()]:
        head = b.startswith('#')
        t = re.sub(r'^#+\s*', '', b)
        t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
        out.append((head, ' '.join(t.split('\n'))))
    return out


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    _, b_chunk = appendix(md, 'Appendix B')
    start = b_chunk.index('I do not use NLP on people who are panicked')
    b0 = paras_of(b_chunk[start:])
    _, c_chunk = appendix(md, 'Appendix C')
    c_paras = paras_of(c_chunk.split('\n## ')[0])
    assert len(c_paras) == 7 and not any(h for h, _ in c_paras), len(c_paras)
    c0 = c_paras
    raw = BG.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == BG_SHA
    bg = [p.strip() for p in re.split(r'\n\s*\n', raw.decode('utf-8')) if p.strip()]
    middle = bg[3:6]
    assert middle[0].startswith('Before you do anything') and middle[2].startswith('Is your inner child'), middle
    for old, new in MIDDLE_FIXES:
        k = next(i for i, p in enumerate(middle) if old in p)
        middle[k] = middle[k].replace(old, new)
    end = [p for _, p in c0[5:7]]
    assert end[0].startswith('If you see several') and end[1].startswith('You can tell a good guide')
    samples = [
        ('B0', 'Appendix B, as installed', b0),
        ('C0', 'Appendix C, as installed (469g)', c0),
        ('C1', 'Appendix C, new opening 1, bg\'s middle, C0\'s end', [(False, p) for p in C1_OPENING + middle + end]),
        ('C2', 'Appendix C, new opening 2, bg\'s middle, C0\'s end', [(False, p) for p in C2_OPENING + middle + end]),
    ]
    parts, spans, words, texts, pos, cands = [], {}, [], [], 0, {}
    for label, what, paras in samples:
        bl = ['<h2>Sample %s</h2>' % label]
        for head, p in paras:
            tag = 'h3' if head else 'p'
            bl.append('<%s>%s</%s>' % (tag, html.escape(p, quote=False), tag))
        t = C.checked_text(OPEN + ''.join(bl) + '</div>')
        texts.append(t)
        spans[label] = {'what': what, 'start': pos, 'end': pos + len(t), 'words': len(t.split()),
                        'paragraphs': len(paras), 'text_sha256': hashlib.sha256(t.encode('utf-8')).hexdigest()}
        cands[label] = {'what': what, 'paragraphs': [p for _, p in paras], 'headings': [i for i, (h, _) in enumerate(paras) if h]}
        pos += len(t) + 1
        parts += bl
        for b in bl:
            words += re.sub(r'<[^>]+>', '', html.unescape(b)).translate(STRAIGHT).split()
    payload = OPEN + ''.join(parts) + '</div>'
    full = C.checked_text(payload)
    assert full == '\n'.join(texts)
    (S / 'CANDIDATES.json').write_text(json.dumps(cands, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (S / 'PAYLOAD-S2.html').write_text(payload, encoding='utf-8')
    (S / 'TEXT-S2.txt').write_text(full, encoding='utf-8')
    (S / 'SPANS-S2.json').write_text(json.dumps(spans, indent=1) + '\n', encoding='utf-8')
    w = ' '.join(words)
    (S / 'WORDS-S2.json').write_text(json.dumps({'words': len(words), 'words_sha256': hashlib.sha256(w.encode('utf-8')).hexdigest(),
                                                 'payload_sha256': hashlib.sha256(payload.encode('utf-8')).hexdigest(),
                                                 'text_sha256': hashlib.sha256(full.encode('utf-8')).hexdigest(),
                                                 'text_chars': len(full)}, indent=1) + '\n', encoding='utf-8')
    for k, v in spans.items():
        print(k, v['words'], 'words', v['start'], v['end'], v['what'])
    print('payload', len(payload), 'chars; checked text', len(full), 'chars,', len(full.split()), 'words; editor words', len(words))


if __name__ == '__main__':
    main()
