"""The community article with Joel's answers of 2026-10-23 22:29 UTC put in (joel-20261023-2229-message.txt beside the
folder above): his final Substack editor HTML of 2026-10-20 (../../joel-20261020/community-final-substack-20261020.html,
the newest he has given) with

- 60 a: the nine typos of the review (spelling and punctuation only);
- 57 a: his own words from his Q07 answer as the sentence after "I’ll go more in detail on this in “The Medicine Part”
  section below." ("true, altho just because it's optional participating in the ceremonies doesn't mean they don't have
  to work with the other parts"), capitalized, with the article's apostrophes and a period;
- 58 a: "The Math of Absorption, and Who This Isn’t For" split: "The Math of Absorption" where it was, and "Who This Isn’t
  For" (same level) before "But before you submit your application to the community, submit it to yourself.";
- 59 a, with his note ("most of the second half of that part could be compressed down into a sentence sinec all this is
  already stated later. could just mention that"): the freeloader passage's second paragraph is Emulate's compression
  (sample emu-ic-c, BUNDLE-IC.json) of my one-sentence draft, with a pointer to the manual, and his last line kept;
  "It requires developing healthier forms of relationships." (his 59 a) goes with the rest;
- 61 b and 62: the essay first (The New Age May Dawn Suddenly, Communes Are Hot Again, Why Communities Keep Dying,
  Practicing Community Can Start Now, The Best Model I've Seen: Zapatistas, What Community Looks Like From Sénégal, A
  Hope For Humanity), then a "How-To Manual" heading with the sections he named under it, one level down and in their
  order (the four parts, medicine, technosphere, jealousy, children, money and land, founderism, movement, leaving),
  then the appendix. Each section carries its divider. Practicing Community points to the manual in a new paragraph
  after its first (Emulate's sample emu-ic-c of my draft), and "pl/ork", now first met there, gets his own gloss
  ("play + work", from "Pl/ork means play + work.").

Every other word is his. The record of each change is RECORD.json beside this file.

  python3 articles/intentional-communities/candidate/joel-20261023/restructure/make_working.py   (from the repo root)
"""
import html, json, pathlib, re
from html.parser import HTMLParser

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parents[1] / 'joel-20261020' / 'community-final-substack-20261020.html'
VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr', 'area', 'base', 'col', 'embed', 'param', 'track'}

TYPOS = [  # (wrong, right) as they are in the HTML, the review's list in order
    ('civilization We lived', 'civilization. We lived'),
    ('Most of the my', 'Most of my'),
    ('whoi end up', 'who end up'),
    ('indispensibility', 'indispensability'),
    ('(”snails”)', '(“snails”)'),
    ('like I’d gone thru', 'like if I’d gone thru'),
    ('wants their to be alone', 'wants to be alone'),
    ('do we we see', 'do we see'),
    ('inbox  to a zillion', 'inbox to a zillion'),
    ('sometimes.  If you depend', 'sometimes. If you depend'),
]
MED_AFTER = 'I’ll go more in detail on this in “The Medicine Part” section below.'
HIS_Q07 = 'Just because it’s optional participating in the ceremonies doesn’t mean they don’t have to work with the other parts.'
OLD_FREE = ('Communal ownership entails folks taking on visible and named stewardship duties. It requires knowing what to do if '
            'someone is leeching off the group and how to deal with it. It requires developing healthier forms of '
            'relationships. ')
NEW_FREE = ('Any attempt at communal ownership needs to take this into account by having folks take on visible and named '
            'stewardship duties, and by having a plan to deal with leeches. The How-To Manual after this essay deals with these '
            'issues. ')
FREE_MINE = [('by assigning stewardship duties by name', 'by having folks take on visible and named stewardship duties',
              'the reader (REVIEW.md, item 1): "assigning" brings in someone who hands out the jobs, like the boss the last line '
              'says is gone, and "visible" was lost; back in his own words ("folks taking on visible and named stewardship '
              'duties")'),
             ('The manual at the bottom of the post deals with these issues.', 'The How-To Manual after this essay deals with '
              'these issues.', 'the manual comes after the essay, and the appendix is at the bottom; and the reader (item 1): '
              'this is the manual\'s first mention, so it gets its heading\'s name')]
GLOSS = ('The most important pl/ork doesn’t need land anyway.', 'The most important pl/ork (play + work) doesn’t need land anyway.')
POINTER = ('The How-To Manual which follows this essay covers the whole model: inner, relational, and medicine pl/ork, the '
           'container that holds them, tech, jealousy, kids, money, land, founder power, how the communities spread, leaving, '
           'etc.')
POINTER_MINE = [('container,', 'the container that holds them,', 'the reader (REVIEW.md, item 2): "container" is first met here; '
                 'his own picture is that the first three parts are the inside of the container')]
# 63 a: alt text, by the image's file name on Substack (images that already had a description keep it, except a file name or
# a copied Reddit title)
ALT = {
    '5bc9c45d': 'Infographic, “Building Healing Community – ‘Escuelitas’ to Save the World”. Its panels: why now (loneliness), '
                'the two deaths of community (secular and spiritual), the escuelita mission (come in, live in, learn to hold, '
                'go out and start the next one), what’s missing (inner work and healthy structure), and six core design '
                'principles.',
    'ebd8f0ea': 'A painted banner reading “Suddenly it’s gonna dawn on you: The New Age”, with a sun rising over hills, on the '
                'wall above a couch in a cozy living room.',
    'ae1e4fd0': 'Google Trends chart of worldwide search interest from 2004 to now: highest in 2004, sinking to a low, flat line '
                'through the 2010s, then shooting back up in 2025.',
    '0b760a8e': 'Infographic, “Building Healing Community – How It Could Work: a lived village, a training ground, and a path '
                'toward deeper common life”. Its panels: my journey, daily life in a healing community, why children need '
                'community, the couple problem, a path toward less money, shared inner purpose, practices that keep community '
                'alive, and the invitation.',
    '7daf9ea4': 'Diagram, “The Math of Absorption”: a community can absorb only as much need as its members have free resource '
                'to meet. With 8 people and 2 in crisis (1 in 4), everything goes to triage; with 80 people and 5 in crisis '
                '(1 in 16), they’re carried and barely felt. Small communities need new members most and can absorb them least.',
    '745198f3': 'A mural across the front of a Zapatista schoolhouse: a row of men, women and children, some with bandanas or ski '
                'masks over their faces, standing among corn plants under an orange sky, with “Digna Rabia” painted at the top.',
    'ee14d04d': 'A big open-sided hall with a metal roof and strings of colored paper lanterns, packed with seated students.',
    '7db4e048': 'The African Renaissance Monument in Dakar: a giant bronze statue of a man holding a child up high, with a woman at '
                'his side, overlooking the city and the ocean.',
    'd33aef69': 'Screenshot of a text chat with a friend about living in Dakar, buying farmland in the south, and how almost '
                'nobody in Sénégal took the Covid vaccine.',
    '98df3b3c': 'A pink wall in Dakar with hand-painted words down one side, “Tolérance! Ouvert! Union! Bonheur! Amour!”, their '
                'first letters spelling TOUBA, next to a swirling drawing.',
    '8957e830': 'Diagram of a house. The roof is Community. Three pillars hold it up: inner pl/ork (reparenting, somatic '
                'regulation, contemplative practice), relational pl/ork (peer counseling, jealousy processing, honesty '
                'practices, conflict handling) and medicine pl/ork (peer-guided, no shamans, gated behind the other work). They '
                'stand on the container: membership, land, money, governance, children and exit. If one of the four gets '
                'skipped, it will need to be dealt with eventually, at high stress.',
    '66730244': 'Meme: a world map with a cat’s outline traced around the continents, captioned “World is just a cat playing '
                'with Australia”.',
    '0844bbea': 'A traveler in a cloak stands in a carved stone doorway, with a glowing world of giant mushrooms and sacred '
                'geometry behind them, looking out over a village at sunset where people share a meal and walk the paths.',
    '1807a9c3': 'An Amish horse and buggy on a country road, between cars and a pickup truck.',
    'ddd2a051': 'A wedding with a coffin in front of the altar: the bride and groom look startled, a guest in sunglasses throws '
                'rose petals, and a sign reads “Till Death Do Us Party”.',
}
ESSAY = ['The New Age May Dawn Suddenly', 'Communes Are Hot Again 🔥', 'Why Communities Keep Dying in the Same Two Ways',
         'Practicing Community Can Start Now', 'The Best Model I’ve Seen: Zapatistas',
         'What Community Looks Like From Sénégal', 'A Hope For Humanity']
MANUAL = ['The Four Parts That Have to Pl/ork Together', 'The Medicine Part - Yes, I’m Naming It',
          'Which Connections to the Technosphere Do You Keep?', 'Jealousy Can Capture Monogamy or Free Love',
          'The Grown Children Get the Final Review', 'Money, Land, and Shared Resources', 'Founderism: The Four Questions',
          'From One Community to a Movement', 'Leaving, Removal, and Dissolution']
APPENDIX = ['Appendix: Watch These, Then Read These']
MANUAL_HEADING = 'How-To Manual'


class _Blocks(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text, self.depth, self.cur, self.out = text, 0, None, []
        self.starts = [0] + [m.end() for m in re.finditer('\n', text)]

    def _off(self):
        line, col = self.getpos()
        return self.starts[line - 1] + col

    def handle_starttag(self, tag, attrs):
        if self.depth == 1:
            o = self._off()
            if tag in VOID:
                self.out.append((tag, o, self.text.index('>', o) + 1))
            else:
                self.cur = [tag, o]
        if tag not in VOID:
            self.depth += 1

    def handle_startendtag(self, tag, attrs):
        if self.depth == 1:
            o = self._off()
            self.out.append((tag, o, self.text.index('>', o) + 1))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        self.depth -= 1
        if self.depth == 1 and self.cur is not None:
            o = self._off()
            self.out.append((self.cur[0], self.cur[1], self.text.index('>', o) + 1))
            self.cur = None


def blocks(work):
    """The top-level blocks of WORK, the editor's body without its own div."""
    wrapped = '<div>' + work + '</div>'
    p = _Blocks(wrapped)
    p.feed(wrapped)
    return [(t, a - 5, b - 5, html.unescape(re.sub(r'<[^>]+>', '', wrapped[a:b])).strip()) for t, a, b in p.out]


def one(work, s, what):
    assert work.count(s) == 1, (what, work.count(s))


def alt_text(work):
    """Put ALT into each image's alt attribute and into the alt of Substack's data-attrs (what the editor reads on paste)."""
    done = {}
    for key, alt in ALT.items():
        tags = [m for m in re.finditer(r'<img\b[^>]*>', work) if key in re.search(r'\bsrc="([^"]*)"', m.group(0)).group(1)]
        assert len(tags) == 1, (key, len(tags))
        tag = tags[0].group(0)
        raw = re.search(r'\bdata-attrs="([^"]*)"', tag).group(1)
        attrs = json.loads(html.unescape(raw))
        dump = lambda d: html.escape(json.dumps(d, ensure_ascii=False, separators=(',', ':')), quote=True)
        assert dump(attrs) == raw, (key, 'data-attrs would not round-trip')
        was = attrs.get('alt') or re.search(r'\balt="([^"]*)"', tag).group(1)
        attrs['alt'] = alt
        new_tag = tag.replace(raw, dump(attrs))
        assert len(re.findall(r'\balt="[^"]*"', new_tag)) == 1, key
        new_tag = re.sub(r'\balt="[^"]*"', lambda m: 'alt="%s"' % html.escape(alt, quote=True), new_tag)
        work = work[:tags[0].start()] + new_tag + work[tags[0].end():]
        done[key] = {'alt': alt, 'was': html.unescape(was)}
    return work, done


def alt_page(work, alts):
    """ALT-TEXT.md: the images in article order, each with the heading it is under, its caption, and its alt text."""
    replaced = sum(1 for a in alts.values() if a['was'])
    out = ['# Alt text for the community article\'s images (your 63 a)', '',
           'Each description is already in the new version\'s HTML (each image\'s alt text), so it comes along when you paste '
           'it. %d images had none; %d had one I replaced (a file name, a copied Reddit title, and a photo caption copied '
           'with the mural), and the old one is shown under the new. The images with a description of yours keep it. To '
           'change one, say which number and what, or change it in the image\'s settings in Substack.'
           % (len(alts) - replaced, replaced), '']
    heads = [(a, x) for t, a, _b, x in blocks(work) if re.fullmatch(r'h[1-6]', t)]
    n = 0
    for m in re.finditer(r'<img\b[^>]*>', work):
        key = next((k for k in alts if k in m.group(0)), None)
        if key is None:
            continue
        n += 1
        head = [h for p, h in heads if p < m.start()]
        fig_end = work.find('</figure>', m.end())
        cap = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', work[m.end():fig_end], re.S)
        where = ('Under "%s"' % head[-1]) if head else ('At the top, before "%s"' % heads[0][1])
        out.append('%d. %s%s:' % (n, where, (', captioned "%s"' % html.unescape(
            re.sub(r'<[^>]+>', '', cap.group(1))).strip()) if cap else ''))
        out.append('   > %s' % alts[key]['alt'])
        if alts[key]['was']:
            out.append('   - The old one: %s' % alts[key]['was'])
        out.append('')
    return '\n'.join(out)


def main():
    raw = SRC.read_text(encoding='utf-8')
    m = re.match(r'(<div[^>]*>)(.*)(</div>)\s*$', raw, re.S)
    open_div, body, close_div = m.group(1), m.group(2), m.group(3)
    rec = []
    for a, b in TYPOS:
        one(body, a, 'typo ' + a)
        body = body.replace(a, b)
        rec.append({'answer': '60 a', 'kind': 'typo', 'old': a, 'new': b})
    one(body, MED_AFTER, '57')
    body = body.replace(MED_AFTER, MED_AFTER + ' ' + html.escape(HIS_Q07, quote=False))
    rec.append({'answer': '57 a', 'kind': 'his words', 'after': MED_AFTER, 'new': HIS_Q07,
                'source': 'his Q07 answer in gpt-reader-edit-answers-20261023.json: "true, altho just because it\'s optional '
                          'participating in the ceremonies doesn\'t mean they don\'t have to work with the other parts"'})
    old_h = '<h2>The Math of Absorption, and Who This Isn’t For</h2>'
    one(body, old_h, '58 heading')
    body = body.replace(old_h, '<h2>The Math of Absorption</h2>')
    first = '<p>But before you submit your application to the community, submit it to yourself.'
    one(body, first, '58 paragraph')
    body = body.replace(first, '<h2>Who This Isn’t For</h2>' + first)
    rec.append({'answer': '58 a', 'kind': 'heading split', 'old': 'The Math of Absorption, and Who This Isn’t For',
                'new': ['The Math of Absorption', 'Who This Isn’t For (before "But before you submit your application ...")']})
    one(body, OLD_FREE, '59')
    body = body.replace(OLD_FREE, html.escape(NEW_FREE, quote=False))
    rec.append({'answer': '59 a and his note', 'kind': 'compressed', 'old': OLD_FREE.strip(), 'new': NEW_FREE.strip(),
                'source': 'Emulate sample emu-ic-c (IC-free) of my draft', 'mine': FREE_MINE,
                'kept': 'his last line: "No, taking away the idea of a boss does not make everyone less passive, selfish, '
                        'thieving, nor suddenly unlearning learned helplessness."',
                'review': 'REVIEW.md item 1 (CHANGED): "visible" and who takes the duties on, fixed in his words; the manual '
                          'unnamed at its first mention, fixed; "developing healthier forms of relationships" dropped, which '
                          'is his 59 a'})
    one(body, GLOSS[0], 'gloss')
    body = body.replace(GLOSS[0], GLOSS[1])
    rec.append({'answer': '62 (references the moves break)', 'kind': 'gloss', 'old': GLOSS[0], 'new': GLOSS[1],
                'why': '"pl/ork" is now first met in Practicing Community; his own definition is "Pl/ork means play + work."'})
    # the pointer, after Practicing Community's first paragraph
    bl = blocks(body)
    k = next(i for i, x in enumerate(bl) if x[0] == 'h1' and x[3] == 'Practicing Community Can Start Now')
    assert bl[k + 1][0] == 'p' and bl[k + 1][3].startswith('I realize that for most people')
    at = bl[k + 1][2]
    body = body[:at] + '<p>' + html.escape(POINTER, quote=False) + '</p>' + body[at:]
    rec.append({'answer': '61 b and 62', 'kind': 'pointer', 'new': POINTER,
                'after': 'I realize that for most people reading this ... The most important pl/ork (play + work) doesn’t need '
                         'land anyway.', 'source': 'Emulate sample emu-ic-c (IC-point) of my draft', 'mine': POINTER_MINE,
                'review': 'REVIEW.md item 2 (CHANGED): "container" unexplained, fixed; "the whole model" kept, since saying '
                          'there is a whole model below is the pointer\'s job (his 61 b: "so that people know i\'m not just '
                          'giving them some basic \'go hand out with friends\' advice"), and the essay has named models before '
                          'it; "medicine" kept as the manual\'s own word for its part'})
    # the order: units start at each h1, with the divider (and an image between it and the h1) that comes before it
    bl = blocks(body)
    h1 = [i for i, x in enumerate(bl) if x[0] == 'h1']
    starts = []
    for i in h1:
        s = i
        if s >= 1 and bl[s - 1][0] == 'hr':
            s -= 1
        elif s >= 2 and bl[s - 1][0].startswith('div') and bl[s - 2][0] == 'hr':
            s -= 2
        starts.append(s)
    starts[0] = 0
    units = {}
    for n, (i, s) in enumerate(zip(h1, starts)):
        e = starts[n + 1] if n + 1 < len(starts) else len(bl)
        units[bl[i][3]] = body[bl[s][1]:bl[e - 1][2]]
    assert set(units) == set(ESSAY + MANUAL + APPENDIX), sorted(set(units) ^ set(ESSAY + MANUAL + APPENDIX))

    def demote(u):
        return re.sub(r'<(/?)h([1-5])\b', lambda m: '<%sh%d' % (m.group(1), int(m.group(2)) + 1), u)

    hr = '<hr contenteditable="false">'
    new = ''.join(units[t] for t in ESSAY)
    new += hr + '<h1>' + html.escape(MANUAL_HEADING, quote=False) + '</h1>'
    first = demote(units[MANUAL[0]])
    assert re.match(r'<hr\b[^>]*>', first), 'the first manual section starts with its divider'
    new += re.sub(r'^<hr\b[^>]*>', '', first)  # the manual's heading has the divider; none between it and its first section
    new += ''.join(demote(units[t]) for t in MANUAL[1:])
    new += ''.join(units[t] for t in APPENDIX)
    words = lambda h: sorted(html.unescape(re.sub(r'<[^>]+>', ' ', h)).split())
    assert words(new) == sorted(words(body) + MANUAL_HEADING.split()), 'the moves add only the manual heading'
    rec.append({'answer': '62', 'kind': 'order', 'essay': ESSAY, 'manual_heading': MANUAL_HEADING,
                'manual': MANUAL, 'manual_levels': 'one level down (h1 to h2, h2 to h3, h3 to h4)', 'appendix': APPENDIX})
    new, alts = alt_text(new)
    rec.append({'answer': '63 a', 'kind': 'alt text', 'images': alts,
                'note': 'in each image\'s alt attribute and Substack\'s data-attrs "alt", so it comes along with a paste; '
                        'Pangram never reads it (substack_check_text reads no attributes); ALT-TEXT.md lists them'})
    (HERE / 'ALT-TEXT.md').write_text(alt_page(new, alts), encoding='utf-8')
    out = open_div + new + close_div
    (HERE / 'WORKING.html').write_text(out, encoding='utf-8')
    try:
        from markdownify import markdownify
        text = re.sub(r'\n{3,}', '\n\n', markdownify(out, heading_style='ATX', bullets='-', strip=['span'])).strip()
        (HERE / 'READING-COPY.md').write_text(
            '> A reading copy of the new version (WORKING.html beside this file, which is what gets pasted into Substack), '
            'made by make_working.py: your answers of 2026-10-23 22:29 UTC are in (RECORD.json lists each change).\n\n'
            + text + '\n', encoding='utf-8')
    except ImportError:
        print('no markdownify here: READING-COPY.md not rebuilt')
    (HERE / 'RECORD.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('WORKING.html: %d characters, %d changes' % (len(out), len(rec)))


if __name__ == '__main__':
    main()
