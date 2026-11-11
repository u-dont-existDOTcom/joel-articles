"""Put SC-106e into HUMANIZED-SO-FAR.md, as he approved it in chat (2026-11-11 22:44 UTC: "yes i want the reddit links.
and your paragraph looks good other than that"), with his two Reddit links added as firsthand reports.

- Blocks 104 ("Goal: Install the "Brake Pads" ...") and 105 ("Mechanism: Potassium Channels (KCNQ).") are cut.
- Block 106 becomes SC-106e's paragraph (texts_x1111b.NEW106), with one sentence after the mood studies carrying his two
  links in the words of his description ("potassium supplementation can help people feel emotions again"; "panic
  attacks from low k"). Reddit is blocked to every tool in this session, the browser included, so the threads weren't
  read; the card's report asks him to check the sentence against them.
- Block 115 loses its second sentence (SP115G).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/apply_x1111b.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
sys.path.insert(0, str(HERE))
import texts_x1111b as T  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
POTS = 'https://www.reddit.com/r/POTS/comments/1go5xl1/did_anybody_notice_how_potassium_makes_you/'
PANIC = 'https://www.reddit.com/r/Anxietyhelp/comments/1d52hl6/low_potassium_an_issue_for_anyone/'
REDDIT = ('People describe it firsthand too: some say potassium helped them [feel emotions again](%s), and others tie '
          'their [panic attacks to low potassium](%s).' % (POTS, PANIC))
NEW106 = T.NEW106.replace(T.S2, T.S2 + ' ' + REDDIT)
assert NEW106 != T.NEW106
NEW115 = (HERE / 'SP115G.md').read_text(encoding='utf-8').strip()
CUTS = ['Goal: Install the "Brake Pads" for your nervous system.', 'Mechanism: Potassium Channels (KCNQ).']
STARTS = {'The Science: Your neurons have "brakes" called KCNQ channels': NEW106, 'The Strategy: Eat 2 large potatoes': NEW115}


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    lines = md.split('\n')
    done = []
    for c in CUTS:
        hits = [i for i, l in enumerate(lines) if l == c]
        assert len(hits) == 1, (c, hits)
        i = hits[0]
        assert lines[i + 1] == '', c
        done.append({'cut': c, 'line': i + 1})
        del lines[i:i + 2]
    for start, new in STARTS.items():
        hits = [i for i, l in enumerate(lines) if l.startswith(start)]
        assert len(hits) == 1, (start, hits)
        i = hits[0]
        done.append({'line': i + 1, 'old': lines[i], 'new': new})
        lines[i] = new
    out = '\n'.join(lines)
    rec = {'about': 'SC-106e, approved in chat 2026-11-11 22:44 UTC, with his two Reddit links as firsthand reports',
           'his_words': 'yes i want the reddit links. and your paragraph looks good other than that',
           'message': '../joel-20261111-2244-message.txt',
           'reddit_read': False,
           'why_not_read': 'Reddit is blocked to the web tools as content; the restriction covers every tool, the browser too',
           'before_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest(), 'changes': done}
    for d in done:
        print(d.get('cut') or d['new'][:90])
    print('after', rec['after_sha256'][:8])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1111B.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
