#!/usr/bin/env python3
"""style_profile.py - an article's style profile, STYLE.json: its register, the kinds of break a paragraph may take, whether the
entries of a list need one, and the range of exclamations the article has (2026-10-17).

Joel, 2026-10-17 13:11 UTC. On the community article's reading list, where every run of entries had been given a break
("Why this one?", "Want it straight from the Zapatistas?"): "a is fine for this article. In a more formal article it might not
be. we need rules that are more flexible depending on the style of the article needed". And on section 16, where the breaks
had become exclamations: "damn you have three sentences ending in exclamation marks in a row that's pretty nuts, you should
check the article style before you do something so far out of range." The march (docs/HUMANIZATION-GATE.md) asks every
paragraph for a break, and its examples start with "the writer reacts or exclaims"; nothing said which breaks suit which
article, or how many exclamations an article has. This file says both, per article, and the checks read it:
- tells_lint.py --style STYLE.json: S1 fails a stretch with more exclamations than the article ever has, S2 flags a draft
  whose rate of them is more than twice the article's;
- reviewer.py march --style STYLE.json: for a formal article, a reaction or an exclamation doesn't count as a break;
- the writer's brief (and Emulate's output, which doesn't keep a voice: Joel, same message, "emulate isn't so great at keeping
  the style/voice so keep that in mind") takes its breaks from "breaks.kinds".

  python3 tools/humanization/style_profile.py REFERENCE.md --register conversational|formal --out STYLE.json
      [--lists per-run|skip] [--note TEXT] [--article ID]
  python3 tools/humanization/style_profile.py --show STYLE.json

REFERENCE.md is the article as it stands (the installed humanized text, with the author's own sections in it); its range is
measured, not set by hand. Re-run it when a section goes in, since each section changes the range a little.
"""
import argparse
import datetime
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import tells_lint  # noqa: E402

KINDS = {
    'conversational': [
        'a reaction, inside the exclamation range below (most reactions end with a period)',
        'an aside that loosens what was just said',
        'a question to the reader',
        'a joke',
        'a story or a memory',
        'a pause, waiting, or a permission',
        "the writer's own doubt or opinion, only where the published text holds it (tells_lint A2)",
    ],
    'formal': [
        'a concrete case: a named community, a number, a place or a date from the source',
        'a short plain sentence that steps back from the sequence',
        "the author's own observation from experience, where the source has it",
        'a question, only where the source asks it',
    ],
}
NEVER = ["an opinion or feeling the published text doesn't hold (tells_lint A2)",
         'more exclamations in a row than the article has (tells_lint S1)']
MARCH_B = {
    'formal': ('- B, a break: the sentence stops that forward march, even for a moment, in the way a careful essay does: a '
               'concrete case (a named place, a number, a date, an example); a short plain sentence that steps back from the '
               "sequence; the author's own observation from experience; a question the text really asks. A reaction or an "
               'exclamation is not a break in this article.'),
}


def build(reference, register, lists, note, article):
    paras = tells_lint.paragraphs(tells_lint.clean(pathlib.Path(reference).read_text(encoding='utf-8')))
    most, share = tells_lint.bang_range(paras)
    return {
        'article': article,
        'register': register,
        'note': note,
        'breaks': {'required': True, 'kinds': KINDS[register], 'never': NEVER,
                   'lists': lists,
                   'lists_note': ('one break per run of entries, the stretch Pangram reads' if lists == 'per-run' else
                                  'list entries skip the break rule; Pangram still has to pass them')},
        'exclamations': {'window': tells_lint.BANG_WINDOW, 'max_in_window': max(1, most) if register == 'conversational' else most,
                         'share': round(share, 3), 'measured_from': str(reference),
                         'measured': datetime.date.today().isoformat()},
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('reference', nargs='?')
    ap.add_argument('--register', choices=sorted(KINDS))
    ap.add_argument('--lists', choices=('per-run', 'skip'))
    ap.add_argument('--note', default='')
    ap.add_argument('--article', default='')
    ap.add_argument('--out')
    ap.add_argument('--show')
    a = ap.parse_args(argv)
    if a.show:
        st = json.loads(pathlib.Path(a.show).read_text(encoding='utf-8'))
        print('%s article (%s). Breaks: %s. Never: %s. Lists: %s. Exclamations: at most %d in any %d sentences in a row, about '
              '%.0f%% of sentences.' % (st['register'], st.get('article', ''), '; '.join(st['breaks']['kinds']),
                                         '; '.join(st['breaks']['never']), st['breaks']['lists_note'],
                                         st['exclamations']['max_in_window'], st['exclamations']['window'],
                                         100 * st['exclamations']['share']))
        return 0
    if not (a.reference and a.register and a.out):
        ap.error('REFERENCE, --register and --out are needed (or --show STYLE.json)')
    lists = a.lists or ('per-run' if a.register == 'conversational' else 'skip')
    st = build(a.reference, a.register, lists, a.note, a.article)
    pathlib.Path(a.out).write_text(json.dumps(st, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('wrote', a.out, st['exclamations'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
