"""r29 (2026-11-08, his message of 17:20 UTC): his T3 answers. "Slow & steady" 180 to 184 as he wrote them (two
paragraphs, read [one Human High window](https://www.pangram.com/history/e05bf34d-fbdd-454a-a6c3-c7abde583a56) by
themselves, the whole section), and his yes to having 369 point back to the college friend that Labels tells
("agree with your plan"), checked in the jealousy section as r29-jeal."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
SLOW = [
    'Going slowly can show you how somebody’s moods wibble and wobble over time, how they treat you and other people, but '
    'it can’t tell you how good the sex will be or how either of you will act afterward. You can know somebody for 20 '
    'years and then discover on the first night that the polarity isn’t there. Touch or smell can feel wrong, or your '
    'desire levels or kinks don’t match up.',
    'Some of those things might get better if both partners are committed to helping each other through it, but '
    'sometimes bad sexual fit still feels like, “Let’s just be friends!” Saying, “The sex isn’t working for me,” might '
    'sound like, “I only love you if the sex is good.” But that vague love word again needs clarifying. Universal love is '
    'the basis of any good relationship of any kind. It doesn’t make someone special the way romance does. Romantic love '
    'generally needs good sex too, or else we’re basically just friends who care deeply about each other.',
]
OLD369 = ('like my one poly college friend who boasted about having 4 girlfriends, but admitted to me that he felt deeply '
          'unhappy.')
NEW369 = 'like the college friend with four girlfriends I mentioned earlier.'
jeal = (FIX / 'r27' / 'checks' / 'CHECK-r27-jeal-b.txt').read_text(encoding='utf-8').strip()
assert jeal.count(OLD369) == 1
TEXTS = {'r29-jeal': jeal.replace(OLD369, NEW369), 'r29-slow-his': '\n\n'.join(SLOW)}
