"""My meaning reviews of the three sections from the redo runs (435g Human): the introduction (HG02+03), the closing
(HG27: its third paragraph is emu-a's, with rev-a's fixes again) and the anxiety appendix (HG33). Each fix is the
smallest change that gives back the published point, keeping Emulate's words around it; each (old, new) is checked
against the stretch's exact text."""
import json
def build(key, fixes, links=None):
    d = json.load(open('rev-e/%s.units.json' % key, encoding='utf-8'))
    body = {u['blocks'][0]: '\n\n'.join(u['paras']) for u in d['units'] if u['kind'] == 'emulate'}
    rv = []
    for b in body:
        fs = [f for f in fixes if f[0] == b]
        for f in fs:
            assert body[b].count(f[3]) == 1, (key, b, f[3])
        r = {'block': b, 'verdict': 'FIX' if fs else 'OK'}
        if fs:
            r['problems'] = [{'type': t, 'what': w, 'replace': o, 'with': n} for _, t, w, o, n in fs]
        if links and b in links:
            r['links'] = links[b]
        rv.append(r)
    assert not [f for f in fixes if f[0] not in body]
    json.dump(rv, open('rev-e/%s.review.json' % key, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(key, len(fixes), 'fixes in', sum(r['verdict'] == 'FIX' for r in rv), 'of', len(rv), 'stretches')

build('HG02+03', [
 (4, 'INVENTED', "'exquisitely designed and arranged' (a designed brain)", 'an exquisitely designed and arranged brain and mind', 'a brain and mind'),
 (5, 'LOST', 'and call that adulthood', 'and so on and so forth.', 'and so on and so forth, and to call that adulthood.'),
 (5, 'SHIFT', "'it is no wonder' makes the programs a result of the training; the published: meanwhile the deeper mind kept running its own programs, each with what it wants",
  'It is no wonder that you have many different "programs" running in your mind, including child mind, guard, body mind, intuitive mind, fantasy mind, etc.',
  'Meanwhile, your deeper mind kept running its own "programs": the child mind wanting safety, the guard expecting danger, the body mind remembering what you explained away, the intuitive mind speaking before words, the fantasy mind trying to become guidance, etc.'),
 (6, 'INVENTED', "'I learned hypnosis from a lot of people'; the published: a lot of hypnosis teaching treats the subconscious like a machine, and that never did much for him",
  'I learned hypnosis from a lot of people who tried to act as if the subconscious mind worked like a machine, and all they had to do was feed in a command and the machine would do what they put in.',
  'A lot of hypnosis teaching acts as if the subconscious mind worked like a machine, and all you had to do was feed in a command and the machine would do what you put in. That never did much for me.'),
 (6, 'SHIFT', 'listening (not talking) until the scared kid, the guard, the body, the intuition and the part trying to run Tuesday can all be heard without one seizing the microphone',
  'For me, a much more useful model was to learn to talk to different parts of myself until they all could listen together.',
  'For me, a much more useful model was to sit down and listen to the different parts of myself (the scared kid, the guard, the body, the intuition, the part trying to run Tuesday) until they all could be heard without one of them seizing the microphone.'),
 (7, 'UNCLEAR', "'the audience of'; self-hypnosis gathers attention", 'to bring the audience of the conscious mind', 'that gathers your attention and brings the conscious mind'),
 (7, 'LOST', 'one honest inner meeting', 'to be able to listen and talk together.', 'to be able to listen and talk together honestly.'),
 (9, 'LOST', 'proven in ordinary life', 'between all parts of the mind.', 'between all parts of the mind, proven in ordinary life.'),
 (11, 'SHIFT', "'heal inner child trauma'; 'we must be skilled enough' is new; the order (begin with Higher Self when the system needs coherence, parts only when that helps); why reparenting",
  'I work with the premise that the subconscious is an ecology, and we must be skilled enough to communicate with its many parts, to separate ourselves into those parts if necessary to better understand them, to heal inner child trauma by reparenting those parts, to coalesce that ecology into a Higher Self or universal heart when need be, and more.',
  'I work with the premise that the subconscious is a living ecology of parts, memories, impulses, images, protections and wisdom. When the system needs coherence, I begin by coalescing that ecology into a Higher Self or universal heart, and I separate into those parts only when that helps. I bring in inner-child reparenting because a wounded young part won’t be repaired by a clever suggestion.'),
 (11, 'LOST', 'why prompt engineering', 'I also pull in elements from prompt engineering, and teach', 'I also pull in elements from prompt engineering, because the shape of a question changes the kind of answer we can hear, and teach'),
], links={11: [{'published': 'inner-child reparenting', 'new': 'inner-child reparenting'}]})

build('HG27', [
 (1, 'INVENTED', "a person called Sarah; 'all on your side' for: none of them is the enemy, most have been trying to help without being introduced",
  'Hi, I’m Sarah. I believe that your subconscious mind, your body, your analytical mind, and the part of you that feels like it needs to protect you are all on your side.',
  'I believe that your subconscious mind, your body, your sharp analytical mind, and the protector that has been braced for years aren’t your enemies. Most of them have been trying to help without ever being properly introduced.'),
 (2, 'SHIFT', 'how deeply you can get hypnotized; an adult you can trust (you, not others)',
  'Whether or not you can “get hypnotized” isn’t as important to me as whether or not you can become a trustworthy adult.',
  'How deeply you can “get hypnotized” isn’t as important to me as whether or not you can become an adult you can trust.'),
 (3, 'INVENTED', "the kid became 'her'; listen until the kid is willing to come closer", 'Then listen to her when she wants to come closer.', 'Then listen until the kid is willing to come closer.'),
 (3, 'INVENTED', "'her' again; enough small promises", 'keep some of your promises to her, too,', 'keep enough small promises to the kid,'),
 (3, 'SHIFT', "think clearly, not 'thinking about yourself'", 'work on thinking about yourself', 'work on thinking clearly'),
])

build('HG33', [
 (1, 'SHIFT', 'anxiety is often a Protector (not always)', 'Remember that the anxiety is coming from', 'Remember that the anxiety is often coming from'),
 (4, 'SHIFT', "the script: 'Little one, you are not alone ... The adult is listening' (not 'You are a little one', 'Let the adult take this')",
  '“You are a little one. You are not alone. You don’t have to fix this. I’m here now. Let the adult take this.”',
  '“Little one, you are not alone. You don’t have to fix this. I’m here now. The adult is listening.”'),
 (4, 'LOST', 'a frightened child', 'like you are talking to a little child that you love.', 'like you are talking to a frightened little child that you love.'),
 (8, 'LOST', "don't force breath holds", 'However, it should not be forced,', 'However, don’t force breath holds,'),
 (11, 'LOST', 'tap gently', 'tap on your body', 'tap gently on your body'),
 (11, 'INVENTED', "'if you're not responding to first-line therapies'; the evidence should be treated cautiously beside first-line therapies",
  'While it should be handled with a bit of caution, it’s something to keep in mind if you’re not responding to first-line therapies.',
  'Still, the evidence should be handled with a bit of caution next to first-line therapies.'),
 (12, 'SHIFT', 'a script line (its quotation marks); kind to the part of me that is afraid',
  'Even though I have this anxiety, I am willing to be kind to myself.',
  '“Even though I have this anxiety, I am willing to be kind to the part of me that is afraid.”'),
 (14, 'UNCLEAR', "'for to know', 'session to how'",
  'Would\xa0it be helpful for\xa0to know\xa0more or even experience a free intro session\xa0to how I work as a Somatic Guide?',
  'Would it be helpful for you to know more or even experience a free intro session on how I work as a Somatic Guide?'),
 (14, 'LOST', 'we track gently', 'in SE we learn to track.', 'in SE we learn to track gently.'),
 (14, 'SHIFT', 'can attention move slowly between them', '"Where can we move, at a snail\'s pace, from one to the other?"', '"Can attention move, at a snail\'s pace, from one to the other?"'),
 (17, 'WRONG', 'the published line is the question itself', 'Do all of these with the felt sense of the whole:', '“What is the felt sense of this whole anxiety?”'),
 (18, 'LOST', "don't answer from the head immediately; give the body time", 'Give it time to get one vague sense of the whole. Then, ask:',
  'Don’t answer from your head right away. Give your body time to get one vague sense of the whole thing. Then, ask:'),
 (19, 'SHIFT', "the felt sense; 'etc.' is new", '“What would this like me to know?” etc.', '“What would this felt sense like me to know?”'),
 (20, 'UNCLEAR', "'both' has nothing to point to: words and bodily attention", 'It’s good to use both to correct each other.', 'It’s good to use both, the words and the body, to correct each other.'),
 (22, 'INVENTED', "'as the first resort'", 'Consider massage, either self or given by someone else, as the first resort.', 'Consider massage, either self or given by someone else.'),
 (22, 'INVENTED', "'one foot with the other'", 'Maybe massage the top of one foot with the other, or the scalp,', 'Maybe massage a foot, or the scalp,'),
 (22, 'LOST', 'a massage gun used carefully', 'massage gun, etc.', 'massage gun used carefully, etc.'),
 (23, 'INVENTED', "'others mentioned'; and LOST: use what actually helps, not a tiny wellness trade show",
  'Others mentioned warmth, darkness, favorite music, massage, weighted blanket, breathwork, favorite object, and favorite personal technology.',
  'Others settle with warmth, darkness, favorite music, massage, weighted blanket, breathwork, favorite object, or personal relaxation technology. Use the support that actually helps, rather than building a tiny wellness trade show around the anxiety.'),
 (24, 'SHIFT', 'one relaxation support (not an important tool)', 'as an important tool in the protocol of relaxing.', 'as one relaxation support.'),
 (24, 'LOST', "both are optional, and they don't prove that any inner signal is true", 'and may be of some benefit, although not at all essential.',
  'and both are optional, not at all essential. Neither one proves that any inner signal is true.'),
 (24, 'LOST', 'listen gently', 'to a state of stabilization where one can begin', 'to a state of stabilization, listen gently, and begin'),
 (24, 'SHIFT', 'one grounded action', 'Once reality tested, take appropriate actions to restore oneself to a grounded state.', 'Once reality tested, come back to one grounded action.'),
 (26, 'INVENTED', "'What is my butt doing?'; and LOST 'first'", 'What are my feet doing? What is my butt doing?', 'What are my feet doing?'),
 (26, 'LOST', 'first, body', 'Where is my body?', 'First, where is my body?'),
 (27, 'INVENTED', "'here to protect you'", 'know that I am here and that I am here to protect you.', 'know that I am here.'),
 (28, 'SHIFT', "if no action is needed (not 'nothing my body can do'); gently", 'And if there is nothing my body can do right now, help my body stand down.',
  'And if no action is needed, help my body stand down gently.'),
 (29, 'LOST', 'the signal (not you); I will listen, test and act', 'I won’t abandon you, but I won’t worship you either.',
  'I won’t abandon the signal, but I won’t worship it either. I’ll listen, test, and act.'),
], links={11: [{'published': '2025 systematic review', 'new': '2025 systematic review'}], 14: [{'published': 'Somatic Guide', 'new': 'Somatic Guide'}],
          24: [{'published': 'ZHoly3O', 'new': 'ZHoly3O'}, {'published': 'Blushield', 'new': 'Blushield'}]})
