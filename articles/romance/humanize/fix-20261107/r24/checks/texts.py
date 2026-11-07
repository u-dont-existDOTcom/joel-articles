"""r24's check texts in the romance article (2026-11-07), each linted before its check (gate bad-trips-2026-11-07h).

r23 (../../r23/checks/RESULTS-r23.json): Jealousy 368 with 369 read Human (Medium, High, Medium; #127) and 369 alone
Human, High (#128); r23's joined 367 read AI Low (#129), so r22's 367 (Human, Medium and Low; #124) stays. The
Idealization section read Mostly Human, 4.9% AI (#130): 147 and 148 Human, the AI windows on 151's last two short
sentences, untouched live text.
- Jealousy 366 to 370, the stretch's try 2 of 2: the live 366 and 370 around r22's 367 and r23's 368 and 369.
- Idealization, the section after the fix (its two tries spent): 151's "Maybe I do talk about them too much sometimes.
  But they still matter to me." joined with but, and "pretend that isn’t on mine" made "pretend they aren’t on mine",
  since "that" would point at the wrong thing once joined."""
import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


R22 = load('r22_texts', HERE.parent.parent / 'r22' / 'checks' / 'texts.py')
R23 = load('r23_texts', HERE.parent.parent / 'r23' / 'checks' / 'texts.py')
LIVE = R22.LIVE
OLD151 = ('Maybe I do talk about them too much sometimes. But they still matter to me. If I’m supposed to listen to '
          'everything on her mind, I don’t want to have to pretend that isn’t on mine.')
NEW151 = ('Maybe I do talk about them too much sometimes, but they still matter to me. If I’m supposed to listen to '
          'everything on her mind, I don’t want to have to pretend they aren’t on mine.')
assert R23.TEXTS['r23-ideal'].count(OLD151) == 1
NEW = {367: R22.NEW[367], 368: R23.NEW[368], 369: R23.NEW[369]}
TEXTS = {
    'r24-jeal366': '\n\n'.join([LIVE[366], NEW[367], NEW[368], NEW[369], LIVE[370]]),
    'r24-ideal': R23.TEXTS['r23-ideal'].replace(OLD151, NEW151),
}
