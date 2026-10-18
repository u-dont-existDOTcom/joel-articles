"""Joel's message of 2026-10-17 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt), the parts that are his words or his
decisions on single lines:
- 47.4: his rewrite of section 15's "All is not well in paradise" P1 and P2, as he wrote it with three obvious typos fixed ("No,
  not quite The warmth" gets its period, "favort" is "favor"), and the published law link kept on "March 2026" (his text drops it;
  the published article and every version since carry it).
- 47.5: his section 2 P2 ("Genevia" is "Geneva"); 46 a: the anomie paragraph of question 46 after it, with his screenshot and
  caption moved there from section 12 (section 12 v16 loses them).
- 47.1: section 16's "One disagreement is enough!" out ("it undermines ... "at least one""). 47.2 and 47.3 change nothing
  ("Really, go!" stays; the version that passed, "make a difference", stays).
- 49: section 8's "If it can't, it can still avoid punishing departure." (the published sentence, shortened, after the transition
  help it follows in the published), and the Rumspringa sentence without its fixed length ("a 2-year period" becomes "a period";
  "age 16" becomes "from about age 16"). Points 1 and 4 stay as he wrote them.
Writes fix-20261017d/s2-v34.md, s8-v31.md, s12-v16.md, s15/v15.md, s16/v30.md and fix-20261017d/article-with-drafts.md.
Run from candidate/: python3 fix-20261017d/make_2137.py"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
H2 = '# Communes Are Hot Again 🔥'
H8 = '# The Grown Children Get the Final Review'
H12 = '# The Math of Absorption, and Who This Isn’t For'
H15 = '# What This Looks Like From Sénégal'
H16 = '# Practice Comes Before Property'


def block(md, h1):
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return md[a:a + 3 + m.start()].strip() + '\n'


def swap(text, old, new, n=1):
    assert text.count(old) == n, (old[:70], text.count(old))
    return text.replace(old, new)


# section 2: his P2, then the anomie paragraph, then the screenshot and his caption (from section 12)
S2_OLD_P2 = ('Whether you want to call that loneliness an official “epidemic” or not, it’s obvious that a lot of people can’t tolerate '
             'modern life in isolation anymore. They may disagree about politics, food, God, sex, or whether shoes are oppressive, but '
             'they agree that something about the current arrangement is starvin’ them.')
S2_NEW_P2 = ('Whether you want to call that loneliness an official “epidemic” or not, it’s obvious that a lot of people can’t tolerate '
             'modern life in isolation anymore (it\'s literally classified as torture by the UN\'s Geneva Convention). They may disagree '
             'about politics, food, God, sex, or whether shoes are oppressive, but they agree that something about the current '
             'arrangement is starving them.')
ANOMIE = ('What\'s starving them is anomie. We evolved to live in small groups where everybody knows everybody. In a large society the '
          'shared norms and close ties that held those groups together fall apart, and that\'s how large societies end up run by '
          'psychopaths. (Yes, I\'m always going on about this.)')
s12 = block(ART, H12)
img = re.search(r'<!-- IMAGE https://raw\.githubusercontent\.com/[^\n]*psypost-relational-mobility\.png[^\n]*-->\n\[caption\][^\n]*\n', s12).group(0)
note = re.search(r'<!-- The screenshot is Joel\'s, sent 2026-10-17 13:11[^\n]*-->\n', s12).group(0)
s2 = block(ART, H2)
s2 = swap(s2, S2_OLD_P2, S2_NEW_P2 + '\n\n' + ANOMIE + '\n\n' + img.rstrip('\n') + '\n'
          '<!-- The screenshot is Joel\'s, sent 2026-10-17 13:11 (candidate/images/psypost-relational-mobility.png), with his aside to '
          'me as its caption and the link to the write-up (his 44c of 17:16); moved here from section 12 with the anomie paragraph (his '
          '46 a of 21:37). The Substack image goes in when he uploads it, linked to the write-up. -->')
(HERE / 's2-v34.md').write_text(s2, encoding='utf-8')
# section 12: the screenshot, its caption and its note out (they're in section 2 now)
s12n = swap(s12, img + note, '')
(HERE / 's12-v16.md').write_text(s12n, encoding='utf-8')
# section 15: his P1 and P2
S15_OLD = ('But does this mean I think Sénégal is some magical place that\'s kept its communal paradise? No, not that either! The warmth '
           'has hard limits here, and LGBTQ+ people can pay a brutal price for crossing them.\n\n'
           'Sénégal passed a law in March 2026 ([Law No. 2026-08](https://www.humandignitytrust.org/resources/law-no-2026-08-of-march-27-'
           '2026-amending-article-319-of-law-no-65-60-of-july-21-1965/)) that increased the penalty for consensual same-sex intimacy to 5 to '
           '10 years in prison, and it also made public advocacy for homosexuality a crime. Homosexuals were already facing arrests, family '
           'rejection, harassment, assault and mob violence, but some say they\'re actually protected once they\'re arrested, because then at '
           'least the mob can\'t get at them. I\'m not going to praise communal belonging and ignore the people who have to hide who they are '
           'to survive it, or leave.')
S15_NEW = ('But does this mean I think Sénégal is some magical place that\'s kept its communal paradise? No, not quite. The warmth has hard '
           'limits here. One noteworthy example is the plight of LGBTQ+ people here, who cross them automatically.\n\n'
           'Sénégal passed a law in March 2026 ([Law No. 2026-08](https://www.humandignitytrust.org/resources/law-no-2026-08-of-march-27-'
           '2026-amending-article-319-of-law-no-65-60-of-july-21-1965/)) that increased the penalty for "consensual same-sex intimacy" to 5 '
           'to 10 years in prison, and it also made public advocacy for homosexuality a crime. Homosexuals were already facing arrests, '
           'family rejection, harassment, assault and mob violence, so ironically, some say they\'re actually safer once they\'re arrested, '
           'because then at least the mob can\'t get at them. And also ironically, LGBTQ+ people are using this prejudice in their favor to '
           'get refugee status and live in rich countries. Anyway, I\'m not going to praise communal belonging and ignore the people who have '
           'to hide who they are to survive it, or leave.')
v14 = (C / 's15' / 'v14.md').read_text(encoding='utf-8')
assert v14.strip() in ART
(C / 's15' / 'v15.md').write_text(swap(v14, S15_OLD, S15_NEW), encoding='utf-8')
# section 16: his cut
v29 = (C / 's16' / 'v29.md').read_text(encoding='utf-8')
assert v29.strip() in ART
(C / 's16' / 'v30.md').write_text(swap(v29, 'keep your commitments. One disagreement is enough! You can talk',
                                        'keep your commitments. You can talk'), encoding='utf-8')
# section 8: punishing departure back, Rumspringa's length out
s8 = block(ART, H8)
s8 = swap(s8, 'Amish young people, age 16, go through a 2-year period of freedom from parental control called *Rumspringa*.',
          'Amish young people, from about age 16, go through a period of freedom from parental control called *Rumspringa*.')
s8 = swap(s8, 'It would be great if the community could also provide resources to smooth the transition, like temporary housing, help '
              'with travel, etc.',
          'It would be great if the community could also provide resources to smooth the transition, like temporary housing, help '
          'with travel, etc. If it can\'t, it can still avoid punishing departure.')
(HERE / 's8-v31.md').write_text(s8, encoding='utf-8')
# the article with all five in place
new = ART
for h1, text in ((H2, s2), (H8, s8), (H12, s12n), (H15, (C / 's15' / 'v15.md').read_text(encoding='utf-8')),
                 (H16, (C / 's16' / 'v30.md').read_text(encoding='utf-8'))):
    a = new.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', new[a + 3:])
    new = new[:a] + text.strip() + '\n' + new[a + 3 + m.start():]
(HERE / 'article-with-drafts.md').write_text(new, encoding='utf-8')
print('written: s2-v34, s8-v31, s12-v16, s15/v15, s16/v30, article-with-drafts')
