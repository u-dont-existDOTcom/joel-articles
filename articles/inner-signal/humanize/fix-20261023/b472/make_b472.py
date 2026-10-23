"""Batch 472g (2026-10-23): the three stretches of recheck A (Joel's result of 01:10 UTC,
https://www.pangram.com/feed/47610d4b-fb69-4966-896f-317b029fc1af) that read AI, and their first API round.

Recheck A read Mostly Human Written, 1.4% AI: 10 of its 100 windows, in three stretches.
  s1  De-hypnosis, its first paragraph (HG16): the run of ten questions "By a screen? ... By repetition?" (32 words; five
      windows, Low but one Medium; light green in the recheck of 2026-10-21). The published line is one sentence ("Screens,
      advertising, politics, ... and repetition all do it."); a run of questions read AI in the Inner Child lane too (E217:
      it became one instruction with examples).
  s2  The seam between the induction section and Come all the way back: bf's last paragraph ("To turn this off, ...") in
      one window with the return's first sentence (162 words, High), then "If you've floated ..." (Medium) and "If you've
      regressed or met parts ..." (High). The return's first sentence read AI in the same place after sample ba's ending
      too (2026-10-21), and bf's last paragraph read Human, High, in the first screening post: so (E198) the window that
      comes back at the same place belongs to the return's paragraph. That paragraph says "make sure" four times, ends its
      first sentence on "when you come out of it" right after bf's "today's trance will be over when you come out of it",
      and runs four "If you've ..." conditions.
  s3  Come all the way back, its fourth paragraph: "Get up only when you feel steady." and "Make sure you're truly oriented
      and alert. Don't just assume it because you've done the count." (26 words, Low; red in the same words on 2026-10-21):
      short commands in a row, and a "don't assume" that is the published "is not proof" (E193's tell).

Each stretch is checked through the API (E218: paragraphs and sections, five or six paragraphs at most) as a pair, with
the paragraph its window needs beside it, headings left out and quotes curled as the Substack check reads them: first as
it stands (does the API see what the recheck saw?), then two candidates each. Only a candidate that reads Human goes on to
the reviews and the guide. Writes TEXTS.json (for pangram_api.py on the laptop), texts/*.txt (for the ledger),
CANDIDATES.json (the edits behind each text) and DRAFTS.md (the candidates in their paragraphs, for Joel and the reviews).

  python3 articles/inner-signal/humanize/fix-20261023/b472/make_b472.py   (from the repo root)
"""
import json, pathlib, re, sys

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
from substack_check_text import smart  # noqa: E402

RECHECK = 'https://www.pangram.com/feed/47610d4b-fb69-4966-896f-317b029fc1af'

# The induction section's last paragraph (bf's, with its fixes), and its round 3 rewording: the published points are
# all kept (to retire the cue: stop rehearsing it, take it out of recordings and active apps, go back to the familiar
# induction; say so while awake; saying it doesn't make it vanish at once; persistent responses or disorientation need
# qualified help; a kept cue is only for a later session you choose; today's trance ends with the return), the cue is
# named ("the shortcut", the heading's word, E207's move 1) and its last sentence no longer ends the way the return's
# first one does
BF_LAST_OLD = ('To turn this off, stop rehearsing it, take it out of any recordings that you have, stop having it in any apps '
               'that are active, and go back to using your regular induction that you have been using. Say that you won\'t '
               'use it anymore when you are awake, but realize that just saying that it is gone won\'t make it go away '
               'immediately. If you are finding that you are responding to it when you don\'t want to, or you are having '
               'problems with being disoriented after using it, get some help from someone who is qualified to help you. If '
               'you want to keep it in, you can, but only for the use of starting a session at a later time when you want '
               'to. For now, today\'s trance will be over when you come out of it.')
BF_LAST_NEW = ('If you want to turn the shortcut off, stop practicing it, take it out of your recordings and out of any apps '
               'you\'ve set up with it, and go back to your usual induction. Tell yourself while you\'re awake that you '
               'won\'t use it anymore, but don\'t expect that just saying it\'s gone will make it go away right away. If '
               'you keep responding to it when you don\'t want to, or you feel disoriented after using it, get help from '
               'someone who\'s qualified. You can keep it if you want, but only for starting a session later on, when you '
               'choose to. Either way, today\'s trance ends when you come back.')

# Round 4 (after c and d: one window, High, both times): every version so far kept the two instruction lists as lists.
# E194 and E223: change what the paragraphs do, in his register, not their words: the reader's own decision and what to
# expect, his casual words ("kicking in", "spacey"), images for the reversals ("like a balloon", "little again", "in the
# driver's seat"), the published points all kept
BF_LAST_JOEL = ('If you ever want to get rid of the shortcut, quit practicing it, take it out of your recordings and whatever '
                'apps you set it up in, and go back to your usual induction. Decide that while you\'re wide awake, and say '
                'it to yourself. Don\'t be surprised if it still works on you for a while, though. Saying it\'s gone '
                'doesn\'t erase it overnight. If it keeps kicking in when you don\'t want it to, or it leaves you spacey '
                'and disoriented after you use it, get help from someone qualified. And if you\'d rather keep it, that\'s '
                'fine, as long as you only use it to start a session you\'ve chosen for later. Either way, today\'s trance '
                'ends when you come back.')
P1_OLD = ('Make sure to reverse anything you\'ve done to alter your state when you come out of it. If you\'ve floated, make '
          'sure you regain your weight (of your choice, of course). If you\'ve shrunk, grow to your normal size again. If '
          'you\'ve regressed or met parts, make sure you come back to feeling complete in the here and now and acknowledge '
          'that your body belongs to you and is under control of the adult mind. If you\'ve gone somewhere, make sure you '
          'go back the same way. Etcetera. Make sure that the only things you bring out with you are the ones you want to.')
P1_JOEL = ('On the way out, undo whatever you did to get in. If you floated up like a balloon, come back down and feel your '
           'weight again (whatever weight you choose, of course). If you shrank, grow back to your normal size. If you were '
           'little again for a while, or spent time with your parts, come back to being all of you, here and now, in a body '
           'that\'s yours, with your adult self in the driver\'s seat. If you went somewhere, come back the way you came. '
           'Etcetera. The only things you bring back out are the ones you actually want.')

# Round 5 (after e: AI alone and in the pair; the return paragraph's closer read AI, High, in a 13-word window of its
# own): both paragraphs ended on tidy closers in every version ("today's trance ends ...", "The only things you bring
# back out are ..."), a shape the gate lists among what read red. f takes them out: the induction paragraph ends on its
# referral, made specific ("like a therapist who knows hypnosis"), and leaves "today's altered state ends with the return"
# to the return's script two paragraphs on, which says it ("All instructions ... to keep me in this state are now
# finished ... neither of them keeps me in this state"); the return paragraph puts "keep only what you chose" in its first
# sentence and ends on "Etcetera."
BF_LAST_F = ('If you ever want to retire the shortcut, stop practicing it, take it out of your recordings and any apps that '
             'play it, and go back to your usual induction. Decide that while you\'re wide awake, and tell yourself so. '
             'Don\'t be surprised if it still works on you for a while, though, since saying it\'s gone doesn\'t erase it '
             'overnight. You can also keep it, but only to start a session you\'ve chosen ahead of time. If it keeps '
             'pulling you in when you don\'t want it to, or you come out of it disoriented, find someone qualified to help '
             'you with it, like a therapist who knows hypnosis.')
P1_F = ('On the way out, undo whatever you did to get in, and only bring back the things you actually want. If you floated '
        'up like a balloon, come back down and feel your weight again (whatever weight you choose, of course). If you '
        'shrank, grow back to your normal size. If you were little again for a while, or spent time with your parts, come '
        'back to being all of you, here and now, in a body that\'s yours, with your adult self in the driver\'s seat. If '
        'you went somewhere, come back the way you came. Etcetera.')

# stretch: (the paragraph the edit is in, its first words), the paragraph its pair takes (offset), candidates: an
# (old, new) edit inside that paragraph, or a list of edits in either paragraph of the pair (a letter in the list takes
# that candidate's edit)
STRETCHES = {
    's1': {
        'section': 'HG16', 'para': 'One of the best side-effects of learning self-hypnosis is influence literacy', 'pair': +1,
        'what': 'De-hypnosis P1 with P2 after it; the recheck\'s part 7, at its end',
        'cands': {
            'a': ('By a screen? By a specific ad? By a politician? By religious fear? By erotic imprinting? By charismatic '
                  'authority? By pressure to belong? By shame? By a sense of urgency? By repetition?',
                  'It could be a screen or a specific ad, a politician, religious fear, erotic imprinting, charismatic '
                  'authority, the pressure to belong, shame, a sense of urgency, or just hearing the same thing over and over.'),
            'b': ('day-to-day life. By a screen? By a specific ad? By a politician? By religious fear? By erotic imprinting? By '
                  'charismatic authority? By pressure to belong? By shame? By a sense of urgency? By repetition?',
                  'day-to-day life (a screen, a specific ad, a politician, religious fear, erotic imprinting, charismatic '
                  'authority, pressure to belong, shame, a sense of urgency, repetition, etc.).'),
            # c: b with the next sentence joined on, since b's change left "It's all around you." as a short knock-down
            # after a long sentence (the linter's B3, a rule the edit brought: lint-compare.json)
            'c': ('day-to-day life. By a screen? By a specific ad? By a politician? By religious fear? By erotic imprinting? By '
                  'charismatic authority? By pressure to belong? By shame? By a sense of urgency? By repetition? It\u2019s all '
                  'around you.',
                  'day-to-day life (a screen, a specific ad, a politician, religious fear, erotic imprinting, charismatic '
                  'authority, pressure to belong, shame, a sense of urgency, repetition, etc.), and it\u2019s all around you.'),
        }},
    's2': {
        'section': 'HG18', 'pair_section': 'HG17', 'para': 'Make sure to reverse anything you\'ve done to alter your state', 'pair': -1,
        'what': 'the induction section\'s last paragraph (bf\'s, as installed) with Come all the way back P1; part 9',
        'cands': {
            'a': ('Make sure to reverse anything you\'ve done to alter your state when you come out of it.',
                  'As you come back, undo anything you did to change your state on the way in.'),
            'b': ('Make sure to reverse anything you\'ve done to alter your state when you come out of it. If you\'ve floated, '
                  'make sure you regain your weight (of your choice, of course). If you\'ve shrunk, grow to your normal size '
                  'again. If you\'ve regressed or met parts, make sure you come back to feeling complete in the here and now '
                  'and acknowledge that your body belongs to you and is under control of the adult mind. If you\'ve gone '
                  'somewhere, make sure you go back the same way. Etcetera. Make sure that the only things you bring out with '
                  'you are the ones you want to.',
                  'As you come back, undo anything you did to change your state on the way in. So if you floated, come back '
                  'down and regain your weight (of your choice, of course). If you shrank, grow back to your normal size. If '
                  'you went younger or met parts, come back to feeling all of you here and now, in a body that\'s yours, with '
                  'your adult mind in charge of it. If you went off somewhere, come back the same way you went. Etcetera. '
                  'Only bring out with you the things you actually want to bring.'),
            # round 3 (after b: still one 241-word window, High, from the induction's last paragraph on): that paragraph,
            # unchanged in a and b, is reworded too, inside the pair; c keeps P1 as installed, d takes b's P1
            'c': [(BF_LAST_OLD, BF_LAST_NEW)],
            'd': [(BF_LAST_OLD, BF_LAST_NEW), 'b'],
            'e': [(BF_LAST_OLD, BF_LAST_JOEL), (P1_OLD, P1_JOEL)],
            'f': [(BF_LAST_OLD, BF_LAST_F), (P1_OLD, P1_F)],
        }},
    's3': {
        'section': 'HG18', 'para': 'When you come out, remind yourself what day (or date) it is.', 'pair': -1,
        'what': 'Come all the way back P4 with P3 (the count) before it; part 9',
        'cands': {
            'a': ('Move around a bit before getting up. Get up only when you feel steady. Make sure you\'re truly oriented and '
                  'alert. Don\'t just assume it because you\'ve done the count.',
                  'Move around a bit before getting up, and only get up once you feel steady. Then check that you\'re really '
                  'oriented and alert, because doing the count doesn\'t always bring you all the way back.'),
            'b': ('Move around a bit before getting up. Get up only when you feel steady. Make sure you\'re truly oriented and '
                  'alert. Don\'t just assume it because you\'ve done the count.',
                  'Move around a bit, and don\'t get up until you feel steady. Make sure you\'re actually oriented and alert '
                  '(the count is supposed to bring you back, but it doesn\'t always do the whole job).'),
            # c: b with the installed "truly" back for "actually", a word the linter flags (O25) that b had brought
            'c': ('Move around a bit before getting up. Get up only when you feel steady. Make sure you\'re truly oriented and '
                  'alert. Don\'t just assume it because you\'ve done the count.',
                  'Move around a bit, and don\'t get up until you feel steady. Make sure you\'re truly oriented and alert '
                  '(the count is supposed to bring you back, but it doesn\'t always do the whole job).'),
        }},
}


def plain(md):
    md = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md)
    return md.replace('**', '').replace('*', '').strip()


def checked(paras):
    """The paragraphs as the Substack check reads them: plain text, quotes curled, one line each."""
    return '\n'.join(smart(plain(p)) for p in paras)


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    blocks = md.split('\n\n')
    texts, cands, drafts = {}, {}, ['# Batch 472g: the candidates in their paragraphs', '',
                                    'Recheck A (%s) read AI in three stretches; each candidate is one edit inside its '
                                    'paragraph, shown with the paragraph its pair check takes.' % RECHECK, '']
    for sid, s in STRETCHES.items():
        i = next(k for k, b in enumerate(blocks) if b.startswith(s['para']))
        j = i + s['pair']
        while blocks[j].startswith('#'):   # headings are left out of the check, so the pair is the next paragraph past them
            j += s['pair']
        lineage = '%s-B%d' % (s['section'], i)
        order = (j, i) if j < i else (i, j)
        base = checked([blocks[k] for k in order])
        texts['b472_%s_base' % sid] = base
        cands['b472_%s_base' % sid] = {'stretch': sid, 'lineage': lineage, 'block': i, 'pair_block': j, 'what': s['what'],
                                       'edit': None}
        drafts += ['## %s: %s' % (sid, s['what']), '', '**As it stands** (`b472_%s_base`):' % sid, '',
                   '> ' + blocks[i], '']
        for c, spec in s['cands'].items():
            edits = []
            for e in (spec if isinstance(spec, list) else [spec]):
                edits += [s['cands'][e]] if isinstance(e, str) else [e]
            now = {k: blocks[k] for k in order}
            keys = []
            for n, (old, new) in enumerate(edits):
                k = next(k for k in order if now[k].count(old) == 1)
                now[k] = now[k].replace(old, new)
                keys.append({'key': 'b472-%s%s' % (sid, c) + ('-%d' % (n + 1) if len(edits) > 1 else ''),
                             'section': s['section'] if k == i else s.get('pair_section', s['section']), 'block': k,
                             'old': old, 'new': new})
            name = 'b472_%s%s' % (sid, c)
            texts[name] = checked([now[k] for k in order])
            changed = sorted({e['block'] for e in keys})
            # the lineage is the paragraph a candidate changes; one that changes only the pair's other paragraph is its own
            lin = lineage if i in changed else '%s-B%d' % (s.get('pair_section', s['section']), changed[0])
            cands[name] = {'stretch': sid, 'lineage': lin, 'block': i, 'pair_block': j, 'what': s['what'],
                           'edit': keys[0] if len(keys) == 1 else None, 'edits': keys,
                           'paragraph_now': now[i], 'pair_now': now[j]}
            drafts += ['**Candidate %s** (`%s`):' % (c, name), ''] + ['> ' + now[k] + '\n' for k in order if k in changed]
    # round 4: e's induction paragraph alone (E190: a stuck pair is checked a part at a time)
    k = cands['b472_s2e']['pair_block']
    texts['b472_s2e_alone'] = checked([cands['b472_s2e']['pair_now']])
    cands['b472_s2e_alone'] = dict(cands['b472_s2e'], lineage='HG17-B%d' % k, alone=True,
                                   what='the induction section\'s last paragraph alone, as candidate e has it; part 9')
    k = cands['b472_s2f']['pair_block']
    texts['b472_s2f_alone'] = checked([cands['b472_s2f']['pair_now']])
    cands['b472_s2f_alone'] = dict(cands['b472_s2f'], lineage='HG17-B%d' % k, alone=True,
                                   what='the induction section\'s last paragraph alone, as candidate f has it; part 9')
    (B / 'texts').mkdir(exist_ok=True)
    for name, t in texts.items():
        (B / 'texts' / (name + '.txt')).write_text(t, encoding='utf-8')
    (B / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'CANDIDATES.json').write_text(json.dumps(cands, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (B / 'DRAFTS.md').write_text('\n'.join(drafts) + '\n', encoding='utf-8')
    for name, t in texts.items():
        print('%-14s %-9s %3d words | %s' % (name, cands[name]['lineage'], len(t.split()), t[:70].replace('\n', ' / ')))


if __name__ == '__main__':
    main()
