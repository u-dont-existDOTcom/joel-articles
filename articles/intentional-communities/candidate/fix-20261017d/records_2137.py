"""The lane's records after Joel's message of 2026-10-17 21:37 UTC: the STATUS.md entry (newest on top) and the current state's
checkpoint, remaining work and next action. Reads the batch results, so it says what actually went in. Idempotent.
Run from candidate/: python3 fix-20261017d/records_2137.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
R = {}
for b in ('b421', 'b422', 'b423', 'b424'):
    f = HERE / b / ('%s-results.json' % b)
    if f.exists():
        R.update(json.loads(f.read_text(encoding='utf-8')))
human = lambda k: k in R and R[k][0].startswith('Human') and R[k][3].startswith('Human') and '; AI' not in R[k][3]
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v18 = (C / 's15' / 'v18.md')
S15V = 'v18' if v18.exists() and v18.read_text(encoding='utf-8').strip() in art else 'v17'
PRED = ['421g 14 of 15', '422g 11 of 15', '423g 9 of 11', '424g 2 of 3']   # fill_preds.py's scores
s15_line = ('section 15 v18 ("So which is it? Well, in a way, it\'s both." out, since his new P1 answers it; march r4, cold read '
            'SENSE-s15d.md; 424g 100%% Human, %s)' % link('S15v18') if S15V == 'v18' else
            'section 15 v18 ("So which is it? Well, in a way, it\'s both." out, his new P1 answers it; march r4, cold read '
            'SENSE-s15d.md OK) not in: 424g read the cut paragraph AI with his law paragraph before it (0.95, %s), Human with the '
            'one after (%s), the section 100%% Human (%s); a paragraph that passes only beside a strong neighbor is borderline (his '
            'rule of 2026-10-16), so v17 stays' % (link('S15v18-p3+prev'), link('S15v18-p3+next'), link('S15v18')))
ENTRY = (
    '**Joel\'s message of 2026-10-17 21:37 UTC (his answers to 45 to 51): sections 8 v31, 13 v37b (accepted), 15 %s and 16 v30 in the '
    'article, each 100%% Human; section 2 waits on its first paragraph (question 52), and the master on section 2 (45 a).** '
    '421g (`fix-20261017d/make_2137.py`, `make_batch421.py`, `install_2137.py`): section 8 v31 (49: "punishing departure" back, '
    'Rumspringa without a fixed length; points 1 and 4 as he wrote them; %s), section 15 v15 (47.4, his rewrite; %s), section 16 '
    'v30 (47.1, his cut; %s; the practice paragraph passes with the one before it, and the one after passes with its own next, '
    '389g). Section 2 v3.4 (his P2, the anomie paragraph, the screenshot) read AI whole, three windows (%s), though each new '
    'paragraph read Human; section 12 v16 waits with it. 422g (`make_tighten.py`, march rounds r1 to r3, `TONE-tighten.md`, '
    '`SENSE-s13.md`, `SENSE-s15.md`, `make_batch422.py`, `install_422.py`): the tightening and question-answer pass where the march '
    'let it through, section 13 v36 (four paragraphs) and section 15 v16 (one tag); section 16 v31 ("can" for "CAN") read AI, a '
    'window 300 words on (%s), and stays out; section 2 one change at a time: his P2 only, Mostly Human with the first paragraph '
    '(installed text) an AI window (%s); with the anomie paragraph, AI (%s). His Pangram test of the two held exclamation cuts '
    '("it made no difference taking those exclamation phrases out for pangram") showed the march was wrong about cuts: '
    '`pangram_gate.py` now sends an edit that only takes words out ("cut_of", checked in code) to Pangram whatever the march says '
    '(test added). 423g (`make_batch423.py`, `install_423.py`): the six held cuts; section 13 v37b with three ("Honestly?", "Why '
    'wouldn\'t they be?", "Yeah, it\'s tough. It\'s also true."; %s); with the opening\'s two as well the section read AI windows '
    '(%s, %s), so "It may sound cheesy" and "Until then, what\'s it worth?" stay; section 15 v17 ("Can you believe it?" out; %s). '
    'Then %s. The lessons (`docs/HUMANIZATION-GATE.md`, "What Joel\'s answers of 2026-10-17 21:37 UTC showed"): cuts and the march, '
    '"a break in the thought" for "a turn", a window that flips away from the change, a published word checked in its new sentence '
    '("either"), a joke that restates a limit, a reviewer\'s reason checked first, his own words first; the cold-read prompt names '
    'the last two kinds (test added). Questions page version 14: 52 section 2\'s first paragraph, 53 the Geneva aside (the UN\'s '
    'Mandela Rules), 54 section 8, a report from a kid who lies a lot (my own concern); 50 answered: his point is in section 11 '
    'already. Ledger: the two entries his answers superseded updated, ten new (`check_owner_edits.py`: 87 pass, 3 waiting).\n'
    'Predictions: %s.\n'
    'Delegations (model, piece, check, outcome): Sonnet, march reads (rounds r1 to r4), checked against the gate\'s rule: nine '
    'changes held, then six of them run as cuts; Sonnet, cold reads of sections 13 and 15 (three), checked against the text; Opus, '
    'the tone check of the tightening (three WEIRD: two fixed with its wording, one kept by his decision); Sonnet, the side-by-side '
    'pages of sections 8, 13, 15 and 16, checked by me (each page\'s links, its changed rows against the installs).\n\n'
    % (S15V, link('S8v31'), link('S15v15'), link('S16v30'), link('S2v34'), link('S16v31'), link('S2v34a'), link('S2v34b'),
       link('S13v37b'), link('S13v37'), link('S13v37a'), link('S15v17'), s15_line, ', '.join(PRED)))
st = C / 'STATUS.md'
t = st.read_text(encoding='utf-8')
if not t.startswith('**Joel\'s message of 2026-10-17 21:37 UTC'):
    st.write_text(ENTRY + t, encoding='utf-8')

cs = C.parent / 'CURRENT-STATE.md'
t = cs.read_text(encoding='utf-8')
a, b = t.index('## Current checkpoint'), t.index('## Evidence / artifacts')
NEW = ('## Current checkpoint\n\n'
       'Sections 13 (v37b) and 14 (v9) are accepted; the rest of `candidate/HUMANIZED-SO-FAR.md` is candidates, each section 100%% '
       'Human as a whole in Pangram\'s web app. After Joel\'s message of 2026-10-17 21:37 UTC (his answers to 45 to 51; records in '
       '`candidate/fix-20261017d/`): sections 8 v31, 13 v37b, 15 %s and 16 v30 went in (batches 421g to %s). Section 2 waits: with '
       'his new P2, Pangram reads its first paragraph AI (question 52), and the anomie paragraph and his screenshot (46 a) wait with '
       'it. His 45 a ("Accept it all ... once 46 to 51 are settled") is ready to run when section 2 is settled: '
       '`candidate/fix-20261017d/make_master.py` (master.md, the article without its version notes) and `promote.py` (the registry, '
       'the owner locks, the editorial status), with a receipt `PROMOTION-RECEIPT-20261017.md` still to write. Open questions 52 to '
       '54 on the lane\'s questions page. The lane\'s notes are `STATUS.md` (newest entry on top) and `candidate/STATUS.md`.\n\n'
       '## Remaining\n\n'
       '- Joel\'s answers to questions 52 to 54; then section 2 (his P2 with 53\'s aside, the anomie paragraph and the screenshot), '
       'each checked alone and in the section, and the promotion (45 a).\n'
       '- Claim-level citation review (`CITATIONS.json`, pending) when Joel asks for it.\n\n'
       '## Blockers / unresolved\n\n'
       '- Open items for Joel are on the lane\'s questions page (`candidate/OWNER-QUESTIONS.md`). The article\'s image 7 link is still '
       'the old one until the new address is known.\n'
       '- Pangram checks run in the desktop app\'s browser pane, signed in to Joel\'s account; the API key is out of credits.\n\n'
       % (S15V, '424g' if 'S15v18' in R else '423g'))
t = t[:a] + NEW + t[b:]
t = re.sub(r'wait for Joel\'s answers to questions 45 to 51, then do what each answer says there\.',
           'wait for Joel\'s answers to questions 52 to 54, then do what each answer says there.', t)
cs.write_text(t, encoding='utf-8')
print('STATUS and CURRENT-STATE written; section 15', S15V, '; predictions', PRED)
