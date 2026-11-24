"""The texts x1124a checks by themselves, as the article has them now (links as their words, the way Pangram reads the
post): L61, his Weeks 3-7 line with 61a's words in (he checked his version: Human Written, one window, High,
https://www.pangram.com/history/dd9b04f2-605a-4d05-a1fc-256ad186a83e), and N58, his answer 58 fitted after the Weeks 1-2
daily list."""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

ARTICLE = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'


def block(start):
    (b,) = [b for b in cr.sr.blocks(ARTICLE.read_text(encoding='utf-8')) if b['text'].startswith(start)]
    return b['text']


def L61():
    return block('So you can tell what each new thing does')


def N58():
    return block("For the zinc, I'd use zinc carnosine")


TEXTS = {'l61': L61, 'n58': N58}
