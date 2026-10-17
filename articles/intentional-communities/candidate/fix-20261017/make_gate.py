"""The reviews for the changes of 2026-10-17 13:11 UTC (Joel's answers to questions 39 to 42 and his corrections; the PsyPost
study in section 12). Joel's own words need no march and no meaning review (pangram_gate.py: an owner text is his own words);
my new paragraph in section 12 needs all of them, and each changed section needs its repeats check (E172) with the drafts in
place. Writes into this folder:
- article-with-drafts.md: HUMANIZED-SO-FAR.md with section 4 v11.4, section 12 v14, section 15 v13 and section 16 v28 in place;
- march-r1/: the march of the new section 12 paragraph and of the two "often" probes for Joel's question 40;
- SENSE-PROMPT-s12.txt (cold read of section 12 with the new paragraph), STANCE-PROMPT-s12.txt (stance check against the
  published essay and Joel's later positions), SOURCE-PROMPT-s12.txt (the paragraph's claims against the study's write-up);
- REPEATS-PROMPT-sN.txt for sections 4, 12, 15 and 16.
Run from the repo root: python3 articles/intentional-communities/candidate/fix-20261017/make_gate.py"""
import json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
py = sys.executable
RV = str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py')
ST = str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py')
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
SECTIONS = {
    's4': ('# The Four Parts That Have to Pl/ork Together', HERE / 's4-v11.4.md'),
    's12': ('# The Math of Absorption, and Who This Isn’t For', HERE / 's12-v14.md'),
    's15': ('# What This Looks Like From Sénégal', C / 's15' / 'v13.md'),
    's16': ('# Practice Comes Before Property', C / 's16' / 'v28.md'),
}
for key, (h, path) in SECTIONS.items():
    a = art.index(h)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- Section|# )', art[a + 3:])
    b = a + 3 + m.start()
    art = art[:a] + path.read_text(encoding='utf-8').strip() + '\n' + art[b:]
(HERE / 'article-with-drafts.md').write_text(art, encoding='utf-8')

# the march: the new paragraph, and the probes of question 40 ("so 'often' is an ai tell?")
S12 = (HERE / 's12-v14.md').read_text(encoding='utf-8')
NEWP = next(b.strip() for b in re.split(r'\n\s*\n', S12) if b.strip().startswith('A [new study]'))
V12 = (C / 's15' / 'v12.md').read_text(encoding='utf-8')
C_NOW = next(b.strip() for b in re.split(r'\n\s*\n', V12) if b.strip().startswith('In the villages and families'))
assert 'so much is taken care of by' in C_NOW
PROBE_C_OFTEN = C_NOW.replace('so much is taken care of by', 'so much is often taken care of by')
G = json.loads((C / 's15' / 'v8-variants.json').read_text(encoding='utf-8'))['H1-P4']['g']
PROBE_G_NO_OFTEN = G.replace('things often go through', 'things go through')
assert PROBE_C_OFTEN != C_NOW and PROBE_G_NO_OFTEN != G
probes = {'q40-c-plus-often': PROBE_C_OFTEN, 'q40-g-minus-often': PROBE_G_NO_OFTEN, 'q40-g-was': G, 'q40-c-now': C_NOW}
(HERE / 'probes-q40.json').write_text(json.dumps(probes, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
paras = [['s12-P2b', NEWP], ['q40-c-plus-often', PROBE_C_OFTEN], ['q40-g-minus-often', PROBE_G_NO_OFTEN]]
(HERE / 'march-r1').mkdir(exist_ok=True)
(HERE / 'march-r1' / 'paras.json').write_text(json.dumps(paras, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

subprocess.run([py, RV, '--article', str(HERE / 'article-with-drafts.md'), 'sense-section', str(HERE / 'SENSE-PROMPT-s12.txt'),
                '--section', SECTIONS['s12'][0], '--report', str(HERE / 'SENSE-s12.md')], check=True)
subprocess.run([py, ST, '--essay', str(C.parent / 'original.md'), '--rewrite', str(HERE / 's12-v14.md'),
                '--out', str(HERE / 'STANCE-PROMPT-s12.txt'), '--scope',
                'section 12 ("The Math of Absorption, and Who This Isn’t For"), with one new paragraph after its second',
                '--topic', 'building intentional communities', '--report', str(HERE / 'STANCE-s12.md'),
                '--images', str(C / 'images.json'), '--positions', str(C / 's15' / 'positions.txt')], check=True)
for key, (h, _) in SECTIONS.items():
    subprocess.run([py, RV, '--article', str(HERE / 'article-with-drafts.md'), 'repeats', str(HERE / ('REPEATS-PROMPT-%s.txt' % key)),
                    '--focus', '"%s"' % h[2:], '--only', '--report', str(HERE / ('REPEATS-%s.md' % key))], check=True)
URL = re.search(r'\]\((https://www\.psypost\.org/[^)]+)\)', NEWP).group(1)
(HERE / 'SOURCE-PROMPT-s12.txt').write_text(
    'You are checking one paragraph of a blog article against the study it cites. Do not read any other file.\n\n'
    'THE PARAGRAPH (Markdown; the link is on "new study"):\n\n' + NEWP + '\n\n'
    'It comes right after this sentence in the article: "Emotional intelligence doesn\'t pay the bills. Instead we optimize to fit '
    'the career market with all the little energy we\'ve got." "Kind of a \'no, duh\' study" is the author\'s own comment on it.\n\n'
    'Open the link (' + URL + ') with your web-fetch tool and read the write-up of the study. Then report, in plain sentences:\n'
    '1. Each claim the paragraph makes about the study: SUPPORTED (quote the write-up\'s words that support it, under 15 words), '
    'OVERSTATED (what the write-up says instead), or NOT IN THE WRITE-UP.\n'
    '2. Whether "found the same goes for how we see the world", right after the career-market sentence, misreads the study.\n'
    '3. Whether anything the study found that a reader would need to read the paragraph fairly is missing (only if its absence '
    'makes the paragraph wrong, not merely shorter).\n'
    'End with one line: VERDICT: OK, or VERDICT: FIX followed by the smallest change in the paragraph\'s own casual voice.\n'
    'Write the report to ' + str(HERE / 'SOURCE-s12.md') + ' and reply "done".\n', encoding='utf-8')
print('wrote the prompts in', HERE)
print('new paragraph words:', len(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', NEWP).split()))
