"""The screening post (2026-10-22): six Emulate samples read in one temporary Substack draft before any meaning work.

The recheck of 2026-10-21 read the induction section (HG17, Emulate sample ba with every point it lost put back) AI, most of
its windows "humanized", and Appendix C's general checklist as my prose (469g) AI as one window. Sample ba had been chosen
by meaning alone (under gate E200 no sample went through a Pangram screen), while HG18's sample, which reads Human in 4.1,
had been chosen by its screen. So the new samples (fix-20261018/make_emu_bc.py) are screened first, in one free check:
  S1, S2  HG17 from the published text (emu-bc, emu-bd)
  S3, S4  HG17 from the installed fixed section, every point kept and Joel's 11 b in (emu-be, emu-bf)
  S5, S6  Appendix C's general checklist from the installed prose (emu-bg, emu-bh)
Each sample goes in as Emulate wrote it: its paragraphs as paragraphs, and the lines that stand for the section's published
headings as headings (the check doesn't read headings, as it doesn't in the guide), picked by hand below; a heading Emulate
ran into a paragraph stays in the paragraph. Each sample is under a heading of its own ("Sample S1" ...), so the check reads
the samples one after another; SPANS.json says where each one is in the checked text, so its windows can be read alone
(a window across a boundary belongs to both).

  python3 articles/inner-signal/humanize/fix-20261022/screen/make_screen.py   (from the repo root)
Writes PAYLOAD-S.html (pasted into the draft by paste_payload_lane.js), TEXT-S.txt (the text the check will read,
tools/humanization/substack_check_text.py), SPANS.json, and WORDS-S.json (the editor's words after the paste, quotes
straightened, and their SHA-256, for the helper's check).
"""
import hashlib, html, json, pathlib, re, sys

S = pathlib.Path(__file__).resolve().parent
H = S.parents[1]
REPO = H.parents[2]
E = H / 'fix-20261018'
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

SAMPLES = [
    ('S1', 'emu-bc', 'HG17-pub2', 'HG17', {0, 3, 6, 10, 31, 37}),
    ('S2', 'emu-bd', 'HG17-pub2', 'HG17', {0, 3, 6, 10, 16, 32, 39}),
    ('S3', 'emu-be', 'HG17-fx1', 'HG17', {0, 3, 6, 10, 17, 45, 51, 56, 59, 64}),
    ('S4', 'emu-bf', 'HG17-fx1', 'HG17', {0, 3, 6, 10, 17, 44, 55, 64}),
    ('S5', 'emu-bg', 'HG32-pr1', 'HG32', {0}),
    ('S6', 'emu-bh', 'HG32-pr1', 'HG32', {0}),
]
LAPTOP_SHA = {  # sha256sum on the laptop of each output, 2026-10-22 19:0x UTC; the copies here must match
    'emu-bc': '8e9e8e52096de87ab70747d9f86c6226dcd6e991ca8eee07cfc3e27556a2a5e3',
    'emu-bd': '4660354f934ad6f54e21b596d9047e57420995a323557560957e6a767a1608e1',
    'emu-be': 'cdc07e304df28c8e6e43f81fe66e7b9ccbdbd969ffeb45ab4c8de847871e13cf',
    'emu-bf': 'ef88640d8e259d99924f8a9440437b6e5f8a1261a64b751f46bb3558210babb0',
    'emu-bg': '15590db9eca43bec3d6c921551ceff54d95100a10b4cc4c8431df0b65c69bf72',
    'emu-bh': 'acdd099fe11cbe7d8200577c82a1524e1c5cc99f1aafd26c238cf9266b3a1741',
}
OPEN = '<div dir="auto" class="body markup">'
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})


def blocks(label, folder, run, heads):
    raw = (E / folder / (run + '.out.txt')).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == LAPTOP_SHA[folder], folder
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw.decode('utf-8')) if p.strip()]
    out = ['<h2>Sample %s</h2>' % label]
    for k, p in enumerate(paras):
        tag = 'h3' if k in heads else 'p'
        out.append('<%s>%s</%s>' % (tag, html.escape(' '.join(p.split('\n')), quote=False), tag))
    return out, paras


def main():
    parts, spans, words, pos = [], {}, [], 0
    texts = []
    for label, folder, run, key, heads in SAMPLES:
        bl, paras = blocks(label, folder, run, heads)
        parts += bl
        t = C.checked_text(OPEN + ''.join(bl) + '</div>')
        texts.append(t)
        spans[label] = {'sample': folder, 'run': run, 'section': key, 'start': pos, 'end': pos + len(t),
                        'words': len(t.split()), 'headings': sorted(heads), 'paragraphs': len(paras),
                        'output_sha256': LAPTOP_SHA[folder]}
        pos += len(t) + 1
        for b in bl:
            words += re.sub(r'<[^>]+>', '', html.unescape(b)).translate(STRAIGHT).split()
    payload = OPEN + ''.join(parts) + '</div>'
    full = C.checked_text(payload)
    assert full == '\n'.join(texts), 'the samples\' texts don\'t add up to the whole'
    assert len(full) < 99999, len(full)
    (S / 'PAYLOAD-S.html').write_text(payload, encoding='utf-8')
    (S / 'TEXT-S.txt').write_text(full, encoding='utf-8')
    (S / 'SPANS.json').write_text(json.dumps(spans, indent=1) + '\n', encoding='utf-8')
    w = ' '.join(words)
    (S / 'WORDS-S.json').write_text(json.dumps({'words': len(words), 'words_sha256': hashlib.sha256(w.encode('utf-8')).hexdigest(),
                                                'payload_sha256': hashlib.sha256(payload.encode('utf-8')).hexdigest(),
                                                'text_sha256': hashlib.sha256(full.encode('utf-8')).hexdigest(),
                                                'text_chars': len(full)}, indent=1) + '\n', encoding='utf-8')
    for k, v in spans.items():
        print(k, v['sample'], v['section'], v['words'], 'words', v['start'], v['end'])
    print('payload', len(payload), 'chars; checked text', len(full), 'chars,', len(full.split()), 'words; editor words', len(words))


if __name__ == '__main__':
    main()
