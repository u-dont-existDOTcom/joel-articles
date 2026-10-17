"""Section 16 draft v23 (2026-10-17): v22's one window ends at H3-P8's end in every shape of H3-P5, H3-P6 and H3-P7 (375g to
379g), so H3-P8's second sentence, the published list of four ("I've just noticed that community tends to gather wherever people
find real care, play, usefulness and room to become more honest."), changes here, in the loose shape of Emulate's calls on it
(round h's call A: "Wherever people are taking care of each other, playing, feeling useful and honest, there is community."):
- g: the four as things people get, joined by "and" ("I've just noticed that wherever people find real care and play, and get
  to be useful, and have room to become more honest, community tends to gather there.");
- j: round h's call A with the published "tends to gather" and "room to become more honest" put back ("I've just noticed that
  wherever people are taking care of each other and playing, feeling useful and having room to become more honest, community
  tends to gather.").
The base is v22 (an argument: gkk, round i's call C for H3-P6, or dmk, v21's H3-P6 with H3-P7's reaction).
Writes v23.md and v23-variants.json. Run from this folder: python3 make_v23.py P8 BASE (for example: g gkk)"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
p8 = sys.argv[1] if len(sys.argv) > 1 else 'g'
base = sys.argv[2] if len(sys.argv) > 2 else 'gkk'
subprocess.run([sys.executable, str(HERE / 'make_v22.py'), base], check=True, capture_output=True)
t = (HERE / 'v22.md').read_text(encoding='utf-8')
OLD = "I've just noticed that community tends to gather wherever people find real care, play, usefulness and room to become more honest."
P8 = {
 'g': ("I've just noticed that wherever people find real care and play, and get to be useful, and have room to become more "
       "honest, community tends to gather there."),
 'j': ("I've just noticed that wherever people are taking care of each other and playing, feeling useful and having room to "
       "become more honest, community tends to gather."),
}
assert t.count(OLD) == 1
t = t.replace(OLD, P8[p8])
(HERE / 'v23.md').write_text(t, encoding='utf-8')
(HERE / 'v23-variants.json').write_text(json.dumps({'old': OLD, 'P8': P8, 'shape': [p8, base]}, ensure_ascii=False, indent=1) + '\n',
                                        encoding='utf-8')
print('wrote v23.md in shape', p8, base)
