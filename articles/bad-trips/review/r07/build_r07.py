"""Bad Trips Guide, Round 7 (2026-11-05): three cards from round 6's answers (ANSWERS-R06-20261105-1514.json) and this
turn's Pangram checks in his account (../../humanize/h06-checks-20261105/RESULTS.md). Y-B and Y-C are changes of mine to
what he sent, with their reasons (gate E348); FORUMS-EDIT is the one paragraph of the section that still reads AI after
four tries, his to edit (gate E265).

  python3 articles/bad-trips/review/r07/build_r07.py
Writes REVIEW-R07.json, .html, .artifact.html and .md here.
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261103/'
LANE = 'articles/bad-trips/'
GIT_FILE = LANE + 'review/r07/REVIEW-R07.html'
ARTICLE = H / 'GUIDE-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
PANEL = BLOB + LANE + 'fix-20261104/panel/%s/PANEL.md'
ASK = ('I can\'t find any more AI tells here, and I see some human tells, like %s... can you help show me the tells I\'m '
       'missing? ([The readers\' notes](%s))')
TYPES = {'help': {'label': 'Help me see what I\'m missing',
                  'about': 'A paragraph my tries couldn\'t get to read Human. Edit it the way you would, or keep it as '
                           'it is.'},
         'fix': {'label': 'A fix to your version',
                 'about': 'Something in your version that doesn\'t hold, changed in the article, with the reason. Keep '
                          'the fix, or edit the paragraph your way.'}}


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s, hits)
    return hits[0]


def whole(i):
    return [{'block': i, 'start': 0, 'end': len(sr.block_text(BL, i))}]


def main():
    ig = block_with('As for topical CBD')
    tg = sr.block_text(BL, ig)
    a = tg.index('The study authors suggested')
    b = tg.index('Generalized are the type')
    i111 = block_with('I would also use topical magnesium chloride')
    t111 = sr.block_text(BL, i111)
    c = t111.index('Purified oral CBD')
    ifo = block_with('I also read on forums')
    S = [
        {'id': 'Y-B', 'type': 'fix', 'title': '"The study authors suggested the dosing may have been too low, or ..."',
         'advice': 'edit', 'keep_label': 'keep the fix', 'spans': [{'block': ig, 'start': a, 'end': b}],
         'reading': 'your skin-gel paragraph with this sentence: [Human Written, 0%%](%saa293ceb-d603-4fe1-9007-2ddc9c6a72bb), '
                    'one window, High.' % P,
         'why': 'You wrote "or it works better for generalized rather than focal seizures". The paper doesn\'t say '
                '"generalized": it says the doses may have been too low, and that the response in adults with focal '
                'epilepsy "is not as robust as seen in patients with Dravet syndrome" ([O\'Brien et al. 2022](https://pmc.'
                'ncbi.nlm.nih.gov/articles/PMC9270696/)). So it now reads "or that CBD just doesn\'t work as well for focal '
                'seizures as it does in Dravet syndrome, where many of the seizures are generalized." Your next sentence '
                'holds and stays: drug-induced seizures are generalized ones ([a toxicology teaching note](https://cumming.'
                'ucalgary.ca/sites/default/files/teams/127/pearl-ofthe-week/Drug%%20induced%%20seizure%%20Mar%%2015%%202019.pdf): '
                '"Drug induced seizures are generalized processes"), and with MDMA they often come from low sodium swelling '
                'the brain ([Merck Manual](https://www.merckmanuals.com/professional/special-subjects/illicit-drugs-and-'
                'intoxicants/methylenedioxymethamphetamine)). The 7-OH-CBD point is out, as you said.',
         'advice_note': 'Keep the fix.',
         'found_by': 'Reading your new sentences against the trial\'s paper (gate E348), 5 November'},
        {'id': 'Y-C', 'type': 'fix', 'title': 'The focal-seizure sentence, out of the oral CBD paragraph',
         'advice': 'edit', 'keep_label': 'keep the cut', 'spans': [{'block': i111, 'start': c, 'end': len(t111)}],
         'reading': 'the paragraph without it: [Human Written, 0%%](%s5d3d05f7-30aa-4aef-b6cf-08deb2f4bd96), one window, High '
                    '(the cut sentence had been a Low window).' % P,
         'why': 'You asked "why are we talking about focal seizures, when seizures from mdma and psychedelic overdoses are '
                'generalized seizures, right?" Right, and that question also applies to the last sentence of this '
                'paragraph, "For focal seizures outside those syndromes, the evidence is mixed, but still long-term." It\'s '
                'gone, so the paragraph ends on the syndromes your reader\'s case is closest to (in Lennox-Gastaut the most '
                'common seizures are generalized tonic ones: [MedLink](https://www.medlink.com/article/generalized_onset_tonic_seizures)). The skin-gel '
                'paragraph keeps its focal point, because that says why the trial may not apply.',
         'advice_note': 'Keep the cut.',
         'found_by': 'Your question on round 6\'s CBD-TRIAL card'},
        {'id': 'FORUMS-EDIT', 'type': 'help', 'title': '"I also read on forums that some people swear smoking at the aura ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(ifo),
         'reading': 'four tries, all AI Detected: your version [62%%](%s2419edef-dd6d-4c05-9ed3-32bf737bef33) (Human Low, AI '
                    'Medium, AI Low); mine after the making-sense read [43%%](%sfd1df50a-5f61-44ee-ad14-ab61bda0542c) (the '
                    'first two sentences Human, the last two AI Low); after two readers\' notes [98%%](%sd3ff8463-b3c1-40f3-'
                    '8852-d81cedc403ed); and this one, [41%%](%sbbaa0976-fd6a-4cdb-bcb0-207e5e9d1265) (Human Low, then AI Low '
                    'on the last two sentences).' % (P, P, P, P),
         'why': 'What I fixed for sense: "it" now says smoking at the aura (after the nasal-spray paragraph it could mean the '
                'spray); the EEG woman was in a published study ([Sivakumar et al. 2017](https://pubmed.ncbi.nlm.nih.gov/'
                '27763968/)), not on a forum; and the ending said "the THC may be what makes it go either way. That\'s what '
                'happened in rats", but in the rats THC only made it worse and CBD helped, so it now says "So it may come '
                'down to how much THC is in it". The last two sentences still read AI. The readers\' notes '
                '([PANEL.md](%s)) both point at the ending as a tidy wrap-up and at the rat sentence\'s mirrored halves; '
                'rewording those without changing what they say made it worse.' % (BLOB + LANE + 'humanize/h06-checks-20261105/panel-F2/PANEL.md'),
         'advice_note': 'Edit it your way, the ending especially; it stays as it is in the guide meanwhile.',
         'found_by': 'This turn\'s checks in your account, 5 November'},
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'bad-trips-r07',
        'title': 'Bad Trips Guide, Round 7',
        'intro': [
            'Your three round-6 answers are in. Your warning-stage, cannabis-and-spray, oral CBD and skin-gel paragraphs '
            'each read Human, High, by themselves; your movement paragraph is in as you checked it. Two cards are changes of '
            'mine with their reasons; the third is the one paragraph still reading AI, for you to edit.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'GUIDE-SO-FAR.md', 'sha256': SHA},
        'links': {'guide': BLOB + LANE + 'GUIDE-SO-FAR.md', 'review': BLOB + LANE + 'review/r07/REVIEW-R07.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-R07.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-R07.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-R07.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s: every card' % review['title'], '',
          'The page\'s cards as text. Built %s from [your post with your versions in](%s). To answer, use the page; or write '
          'your version under a card\'s number in a message to me.' % (review['built'], review['links']['guide']), '']
    for s in S:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '',
               '*%s*' % sr.where(BL, s['spans'][0]['block']), '']
        md += ['**Pangram read:** %s' % s['reading'], '']
        sp = s['spans'][0]
        md += ['> %s' % BL[sp['block']]['text'][sp['start']:sp['end']], '']
        md += ['**Why:** %s' % s['why'], '', '**My ask:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-R07.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
