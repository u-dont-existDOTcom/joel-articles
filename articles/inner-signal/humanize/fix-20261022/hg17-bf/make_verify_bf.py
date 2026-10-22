"""The meaning check of the induction section's screened sample (2026-10-22): Emulate's sample bf (fix-20261018/emu-bf,
HG17-fx1.out.txt, made from the installed fixed section with Joel's 11 b) read Human in every window of the screening post
(fix-20261022/screen/SCREEN-RESULT.json, S4), so it is the one the meaning work starts from.

The check is the one the fixed section had (fix-20261018/rf-zg/HG17.fixed.verify.partN.prompt.txt): every point of the
published section against the rewrite, in three parts split at the same headings in both texts so that each report stays
under the reader's output limit. The published parts are taken from those prompts word for word; the sample is split
where its own versions of the same headings start ("Variations Open already", "Fractionation").

  python3 articles/inner-signal/humanize/fix-20261022/hg17-bf/make_verify_bf.py   (from the repo root)
Writes VERIFY-partN-PROMPT.txt (Sonnet, -> VERIFY-partN.md) and SAMPLE-partN.txt.
"""
import hashlib, pathlib, re

V = pathlib.Path(__file__).resolve().parent
H = V.parents[1]
ZG = H / 'fix-20261018' / 'rf-zg'
OUT = H / 'fix-20261018' / 'emu-bf' / 'HG17-fx1.out.txt'
SHA = 'ef88640d8e259d99924f8a9440437b6e5f8a1261a64b751f46bb3558210babb0'
STARTS = (None, 'Variations Open already', 'Fractionation (at some point')


def main():
    raw = OUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw.decode('utf-8')) if p.strip()]
    cut = [0] + [next(i for i, p in enumerate(paras) if p.startswith(s)) for s in STARTS[1:]] + [len(paras)]
    for n in (1, 2, 3):
        old = (ZG / ('HG17.fixed.verify.part%d.prompt.txt' % n)).read_text(encoding='utf-8')
        head, rest = old.split('THE PUBLISHED SECTION:\n\n', 1)
        published = rest.split('\n\nTHE REWRITE:', 1)[0]
        head = head.replace(str(ZG / ('HG17.fixed.verify.part%d.out.md' % n)), str(V / ('VERIFY-part%d.md' % n)))
        head = head.replace('The rewrite was made by a paraphrasing tool that writes in a plainer, more personal voice, and '
                            'then edited; its looser wording is fine.',
                            'The rewrite was made by a paraphrasing tool that writes in a plainer, more personal voice; its '
                            'looser wording is fine.')
        assert str(V / ('VERIFY-part%d.md' % n)) in head
        sample = '\n\n'.join(paras[cut[n - 1]:cut[n]])
        (V / ('SAMPLE-part%d.txt' % n)).write_text(sample + '\n', encoding='utf-8')
        (V / ('VERIFY-part%d-PROMPT.txt' % n)).write_text(head + 'THE PUBLISHED SECTION:\n\n' + published +
                                                          '\n\nTHE REWRITE:\n\n' + sample + '\n', encoding='utf-8')
        print('part %d: published %d words, sample %d words (paragraphs %d-%d)'
              % (n, len(published.split()), len(sample.split()), cut[n - 1], cut[n] - 1))


if __name__ == '__main__':
    main()
