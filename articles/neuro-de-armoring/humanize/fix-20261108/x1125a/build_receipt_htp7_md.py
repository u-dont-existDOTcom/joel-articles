"""The 5-HTP warning's version 7 (the closest try, 67.2% AI) as it would go into the article, with its link in Markdown:
the receipt the cards page needs for the text it shows (suggestion_review.py matches a card's new text to its receipt
word for word). Same parts and reads as v7/HTP4.receipt.json, which is for the words as Pangram read them.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/build_receipt_htp7_md.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_receipts_x1125a as R  # noqa: E402

T, B = R.T, R.B
OUT = HERE / 'v7'
B.HERE = OUT
T.V4 = dict(T.V4, htp=T.V7['htp'])
R.REGISTER_ONLY = True
R.htp()
R.REGISTER_ONLY = False
print('\n'.join(R._build('HTP7-MD', T.V7['htp'], ['htp'], {})) or 'receipt: PASS')
