"""His new warnings of 2026-11-22 17:39 UTC (x1122a/WARNINGS-BRIEF.md; sources in x1122a/WARNINGS-SOURCES.md), as texts
of mine: a new disclaimer item for lion's mane and ashwagandha (after the Cognitive Warning, before the Agmatine Warning,
so its "anhedonia" is the article's first and is said in plain words there), and one sentence each added to agmatine's
stop line (block 16) and to 5-HTP's stop signs (block 91). The paragraphs as they would read are built from the
article's own text by script (block ids), never retyped.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD, whole=True)


def block(start):
    (b,) = [x for x in BL if x['text'].startswith(start)]
    return b


# lion's mane and ashwagandha: a new item, my text from his words (LMA0 is the version the reads saw: reads-lma.md)
LMA0 = ("Lion's Mane & Ashwagandha: I don't advise either one, and this protocol doesn't use them. People on forums and "
       "YouTube report rare cases where they were left with anhedonia (when nothing feels good anymore) and sexual "
       "problems for months after stopping. No study has looked into it yet (the trials of both mostly found mild side "
       "effects), but it's the same kind of lasting effect regulators already warn about for SSRIs and finasteride.")

# after the reads (reads-lma.md): why people take them before the don't (way 14), "after they stopped taking them" (way
# 10), the trials' clause cut (the needed read: nothing to act on; the fit read: it reassures before the warning), and the
# comparison said as what regulators warn about after SSRIs and finasteride (his point), with "these lasting effects" named
LMA = ("Lion's Mane & Ashwagandha: Lion's mane for focus and ashwagandha for stress are popular, but I don't advise either "
       "one, and this protocol doesn't use them. People on forums and YouTube report rare cases where they were left with "
       "anhedonia (when nothing feels good anymore) and sexual problems for months after they stopped taking them. These "
       "lasting effects haven't been studied yet, but they're the same kind that regulators already warn can follow SSRIs "
       "and finasteride.")

# LMA's check (checks-1123g, https://www.pangram.com/history/50622455-2e3a-482e-ac66-0ae461f68592): AI Detected, 93% AI;
# S1 AI Low ("X for A and Y for B are popular, but"), S2 and S3 AI High (the report register: "report rare cases where
# they were left with", "haven't been studied yet, but they're the same kind that regulators already warn can follow").
# His own message says it in his order and words: persistent anhedonia and sexual dysfunction, even after stopping, in
# rare cases reported on forums and YT, like SSRIs and finasteride. LMA2 follows it:
LMA2 = ("Lion's Mane & Ashwagandha: Lots of people take these for focus and stress, but I'd leave both out. In rare "
        "cases reported on forums and YouTube, people say they were left with anhedonia (when nothing feels good anymore) "
        "and sexual dysfunction that persisted even after they stopped. Nobody has studied it yet, but SSRIs and "
        "finasteride can do the same thing, and regulators already warn about that.")

# LMA2's reads (reads-lma2.md): S2 way 11 (the source before the effect), S3 ways 7 and 10 ("it", "that") and the fit
# read's misread (an SSRI user alarmed). LMA3, try 2: the effect first and the source after, as his message has it; the
# comparison kept (his point: the kind of lasting harm regulators recognize) with its referents named, and said as what
# regulators warn about, not as advice on the drugs:
LMA3 = ("Lion's Mane & Ashwagandha: Lots of people take these for focus and stress, but I'd leave both out. People say "
        "these herbs left them with anhedonia (when nothing feels good anymore) and sexual dysfunction that persisted even "
        "after they stopped, in rare cases reported on forums and YouTube. Nobody has studied these effects in the two "
        "herbs yet, but regulators already warn that SSRIs and finasteride can leave the same kind behind.")
LMA_AFTER = 'The armored brain projects its own internal threat level'   # block 13, the Cognitive Warning's rule
LMA_BEFORE = 'Agmatine Warning (The Voltage Governor):'                  # block 14

# agmatine: one sentence after "so do not "push through" numbness."
AGM_AT = 'so do not "push through" numbness.'
AGM_ADD0 = ' In rare reports, the anhedonia lasted for weeks after people stopped.'   # what the reads saw
AGM_ADD = ' In rare reports, the anhedonia lasted for weeks after people stopped taking it.'   # way 10: stopped what
AGM_BLOCK = 'Stop immediately if it causes flatness, anhedonia'

# 5-HTP: one sentence at the end of its stop signs
HTP_BLOCK = 'Side effects / stop signs: The most dangerous symptoms to watch out for'
HTP_ADD0 = (' And rarely, people report anhedonia that goes on for weeks after they stop 5-HTP, shorter than the reports for '
            'lion\'s mane and ashwagandha, but still something to keep in mind.')   # what the reads saw (reads-htp.md)
# after the reads: the comparison cut (needed and his fixes, way 7: nothing to act on; "weeks" here and "months" in the
# lion's mane item already say it) and the close cut (way 6)
HTP_ADD = ' And rarely, people report anhedonia that goes on for weeks after they stop 5-HTP.'


def agm_paragraph():
    t = block(AGM_BLOCK)['text']
    assert t.count(AGM_AT) == 1
    return t.replace(AGM_AT, AGM_AT + AGM_ADD)


def htp_paragraph():
    t = block(HTP_BLOCK)['text'].rstrip()
    return t if t.endswith(HTP_ADD.strip()) else t + HTP_ADD   # in the article since apply_x1123a.py (2026-11-23)


TEXTS = {'lma': lambda: LMA, 'lma2': lambda: LMA2, 'agm': agm_paragraph, 'htp': htp_paragraph}

if __name__ == '__main__':
    for k, f in TEXTS.items():
        t = f()
        print(k, len(t.split()), 'words')
