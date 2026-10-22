#!/usr/bin/env python3
"""Turn 93: take out the AI tells round 2 found in my own paragraphs (Joel's answer to question 83, 2026-10-22 19:01 UTC:
"i like you to try yourself IF you know what looks like AI tells, then i can help you if you can't find the AI tells").

Each item names its round-2 windows, the tells (docs/HUMANIZATION-GATE.md, "What Pangram 4.1 flagged") and the change.
The fixes only cut or say plainly; nothing is added. Run from articles/inner-child-therapy:
  python3 experiments/t93-tells/apply_t93.py
It writes the article, a turn-93 note before each changed paragraph, and each new paragraph to experiments/t93-tells/drafts/.
It ran once. After the first lint, five items were reworded (a01, a05, a09 and a11 had FAILed; a14's doctor line was
unclear), so FIXES.json and drafts/ hold the final wording, not ITEMS below.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent / 'HUMANIZED-ARTICLE-SO-FAR.md'
HEAD = ('Turn 93 (Joel\'s answer to question 83, 2026-10-22 19:01 UTC: I find the AI tells myself and take them out, adding '
        'nothing; experiments/t93-tells/TELLS-ROUND2.md, item %s): round 2 (check t90s_%s, %s) read AI here: %s. The tells: %s. '
        '%s Lint %s. Not yet checked in Pangram.')

ITEMS = [
 dict(id='a01', half='A', where="Don't Give the Inner Adult Away P7", tries='third try',
      windows="High 27, Medium 7 and High 18, its last three sentences",
      tells="a general point told as a little scenario (\"and suddenly someone's an exception\"), a reassuring turn (\"I wouldn't argue with the feeling.\") and a two-part advice closer",
      change="\"all its\" and \"and suddenly\" are out, the reassuring sentence is cut, and the advice is one clause.",
      old='''A group can do it too, with all its praise and special attention, and suddenly someone's an exception to rules you'd use with anybody else. I wouldn't argue with the feeling. I'd give it a few days before deciding anything big, and check the facts in the meantime.''',
      new='''A group can do it too, with praise and special attention, until someone's an exception to rules you'd use with anybody else. I'd take a few days to check the facts before deciding anything big.'''),
 dict(id='a02', half='A', where="Don't Give the Inner Adult Away P8", tries='third try',
      windows="Medium 50, all of it",
      tells="a topic sentence built like P7's \"A group can do it too\", a sentence explaining the example, and a short knock-down (\"Laugh if it's funny.\")",
      change="The joke is now the first sentence's example; the explanation and the knock-down are cut.",
      old='''Humor can sneak things past you too. "Ha, I'll just borrow your card, kidding... unless?" is a joke and a request at the same time. Laugh if it's funny. But if saying yes would cost you money, I'd answer it like they'd asked you straight out.''',
      new='''A joke can carry a request, like "Ha, I'll just borrow your card, kidding... unless?" If saying yes would cost you money, I'd answer it like they'd asked you straight out.'''),
 dict(id='a03', half='A', where="Before You Try to Go Deep P2", tries='first try',
      windows="Low 51 and High 40, from \"If you can't\" on",
      tells="a then-and-now reframe closing on a balanced contrast (\"instead of giving up on them\") and a reassuring closer (\"Even just ... counts.\")",
      change="The contrast is cut, and the eyes-open hello is the gentler thing.",
      old='''Now there's a grown-up around who can say, "Okay, that's enough for today," and try something gentler instead of giving up on them. Even just saying hi to them with your eyes open, before any imagery, counts.''',
      new='''Now there's a grown-up around who can say, "Okay, that's enough for today," and try something gentler, like saying hi to them with your eyes open.'''),
 dict(id='a04', half='A', where="Before You Try to Go Deep P3", tries='first try',
      windows="Medium 25, High 32, Medium 9, High 21 and Medium 9, all of it",
      tells="two follow-ups that reassure or explain (\"A couple of lines on your phone is plenty.\", \"After a while away, it gets hard to remember.\"), a \"So\" summary and an either-or closer",
      change="The two follow-ups are cut, and the last two sentences are one.",
      old='''If you do need one, I'd jot down why, and how far you'd gotten before it got to be too much. A couple of lines on your phone is plenty. After a while away, it gets hard to remember. So once that reason has changed and you want to come back, the note tells you where it was still okay. I'd start there, or somewhere a bit gentler.''',
      new='''If you do need one, I'd jot down why, and how far you'd gotten before it got to be too much. Once that reason has changed and you want to come back, start where the note says it was still okay, or a bit gentler.'''),
 dict(id='a05', half='A', where="Before You Try to Go Deep P4", tries='first try',
      windows="Low 74, all of it",
      tells="a question answered with a short knock-down (\"I really don't think so.\"), an aphorism that restates the first sentence (\"waiting just means more of being alone\") and a \"So\" closer",
      change="The answer is said plainly and the aphorism is cut.",
      old='''Do you have to get yourself sorted out first, so you'll be better company? I really don't think so. If the hurt was being alone, waiting just means more of being alone. So I'd call somebody or show up somewhere, mess and all.''',
      new='''You don't have to get yourself sorted out first to be better company. I'd call somebody or show up somewhere, mess and all.'''),
 dict(id='a06', half='A', where="Your Body Might Need Some Love First P4", tries='first try',
      windows="Low 115, from its second sentence into his P5",
      tells="a quip (\"or stuff you'd rather never have met\")",
      change="It's cut; the rest of the window is his P5.",
      old='''This kind of work can bring up grief and fear, and sometimes hard dreams, or stuff you'd rather never have met.''',
      new='''This kind of work can bring up grief and fear, and sometimes hard dreams.'''),
 dict(id='a07', half='A', where="Borrow One Competency at a Time P9", tries='first try',
      windows="Low 12, Low 15, Medium 19 and High 30, all of it",
      tells="wry quips (\"Which, fair enough, you did take a while.\", \"two six-year-olds arguing\") and a wry closer (the eye-roll)",
      change="All three are cut; his 😜 and the hearing-it-out line (2026-10-14) stay.",
      old='''More like "Oh, so NOW you care?" Which, fair enough, you did take a while. Your first instinct might be "But I'm trying!", and then it's just two six-year-olds arguing. Some days, just hearing it out like a decent adult is the only thing you'll manage to borrow, and your little one might still roll their eyes at you. 🙄''',
      new='''More like "Oh, so NOW you care?" Your first instinct might be "But I'm trying!" Some days, just hearing it out like a decent adult is the only thing you'll manage to borrow.'''),
 dict(id='a08', half='A', where="Borrow Hindsight P1", tries='third try',
      windows="Low 83, all of it with P2's start",
      tells="a reassuring gloss (\"makes the whole thing feel less lonely\") and a wry follow-up (\"They've only lived a little longer than you.\")",
      change="Both are cut, and the gospel point joins the gloss; his question is unchanged.",
      old='''It's a question borrowed from your future self, and sometimes just asking it makes the whole thing feel less lonely. I wouldn't take their answer as gospel, though. They've only lived a little longer than you.''',
      new='''It's a question borrowed from your future self, and I wouldn't take their answer as gospel.'''),
 dict(id='a09', half='A', where="Borrow Hindsight P2", tries='third try',
      windows="High 16, Medium 6 and Low 13",
      tells="an either-or pair (\"kind about it, or maybe they'd just\") and a rhetorical question opening the next step (\"Can't picture them at all?\")",
      change="One option; the question is a plain \"if\".",
      old='''Maybe they'd be kind about it, or maybe they'd just make you some food. Can't picture them at all? Then make the food yourself, and don't bother faking a feeling first.''',
      new='''Maybe they'd just make you some food. If you can't picture them, make the food yourself, without faking a feeling first.'''),
 dict(id='a10', half='A', where="Just Like Me P1", tries='first try',
      windows="Low 26, Low 2 and Low 21, its first four sentences",
      tells="a script's step-by-step beat (\"Name the feeling plainly. Lonely, say. Then think...\", E64)",
      change="The steps are one sentence.",
      old='''This one works best on a steadier day, when thinking about other people won't pull you out of your own shoes. Name the feeling plainly. Lonely, say. Then think of how many people are feeling that exact thing right now, and wanting it to stop, just like you.''',
      new='''On a steadier day, when thinking about other people won't pull you out of your own shoes, name the feeling plainly (lonely, say) and think of how many people are feeling that exact thing right now, and wanting it to stop, just like you.'''),
 dict(id='a11', half='A', where="Just Like Me P2", tries='first try',
      windows="Low 8 and Low 29, its last three sentences",
      tells="a parallel negation (\"isn't part of it, and neither is\") and a wry closer (\"if it ever comes\")",
      change="One plain sentence, and the closer is cut.",
      old='''Forgiving them isn't part of it, and neither is picturing their childhood. Getting in touch is a separate decision, for a much calmer day, if it ever comes.''',
      new='''You don't have to forgive them or picture their childhood. Getting in touch is a separate decision, for a much calmer day.'''),
 dict(id='a12', half='A', where="The Parent You Inherited P4", tries='first try',
      windows="Low 85, all but its last sentence",
      tells="a stock frame (\"it helps to\") and a wry aside (\"(it doesn't have to be a flattering name)\")",
      change="Both are out.",
      old='''If answering the voice feels disloyal, it helps to give it a name of its own, like the Critic (it doesn't have to be a flattering name), so you're arguing with what it says and leaving your parents out of it.''',
      new='''If answering the voice feels disloyal, give it a name of its own, like the Critic, so you're arguing with what it says and leaving your parents out of it.'''),
 dict(id='a13', half='A', where="Start With Whatever Showed Up P8", tries='third try',
      windows="Low 22, High 27 and Medium 36, from \"Roughly\" on",
      tells="a signposted checklist (\"they'd ask two things.\" and two questions), a two-step instruction (\"so listen to it, and then let your head check it\") and a balancing closer (\"I wouldn't let either one decide by itself\")",
      change="Kahneman and Klein's two conditions are one sentence, and the tired head now says why neither decides alone.",
      old='''Roughly, they'd ask two things. Is this the kind of situation that's predictable at all? And have you been in it enough times to learn it? A hunch might be catching something real that your head hasn't put into words yet, so listen to it, and then let your head check it. I wouldn't let either one decide by itself, though. Your head can get tired of not knowing and be glad to hand the whole thing over, to a hunch or to somebody who sounds sure.''',
      new='''Roughly, they'd ask whether the situation is predictable at all, and whether you've been in it enough times to learn it. A hunch might be catching something real that your head hasn't put into words yet, and your head can check it, unless it's tired of not knowing and glad to hand the whole thing over, to a hunch or to somebody who sounds sure.'''),
 dict(id='a14', half='A', where="Start With Whatever Showed Up P9", tries='first try',
      windows="Low 7, High 37, Low 18, Medium 27, High 21 and Medium 39, all of it",
      tells="a signpost opener (\"the same kind of listening\"), a colon list, two-step advice (\"hear it out and then go see\"), a quip (\"(Or they do, and you survive it.)\") and a balanced pair (\"and find out how right it was later\")",
      change="Each is cut, with one example of the guess.",
      old='''Anxiety deserves the same kind of listening. A lot of the time it's a part of you that's trying to protect you, making a guess about what's coming: that you'll get overwhelmed, maybe, or that people will laugh at you. It can be right! It's probably been wrong before too, and you know some of those times. So when it's safe to find out, I'd hear it out and then go see. Maybe nobody laughs. (Or they do, and you survive it.) If it might be real danger, though, I'd get some distance first, and find out how right it was later. Same with something a doctor should look at.''',
      new='''Anxiety is often a part of you that's trying to protect you, making a guess about what's coming, like that people will laugh at you. It can be right! It's probably been wrong before too, and you know some of those times. When it's safe to find out, I'd go see. Maybe nobody laughs. If it might be real danger, though, I'd get some distance first. Same with something a doctor should look at.'''),
 dict(id='a15', half='A', where="Start With Whatever Showed Up P10", tries='first try',
      windows="Medium 39, High 21 and Medium 23, all of it",
      tells="two parallel conditionals (\"If ..., that's enough to stop. And if ..., I'd stop there too.\") and a tidy follow-up",
      change="They're one sentence.",
      old='''If a part hesitates about being touched or about sex, that's enough to stop. And if it says no to going deeper in this work, or to an altered state, I'd stop there too. It might not be able to tell you why.''',
      new='''When a part hesitates about being touched or about sex, or says no to going deeper in this work or to an altered state, I'd stop, even if it can't tell you why.'''),
 dict(id='a16', half='A', where="Two Common Guarding Patterns P1", tries='third try',
      windows="Medium 23 and High 95, all of it, into P2 (turn 92 reported it fixed; that was wrong)",
      tells="an enumeration signpost that repeats the heading (\"Two kinds of reaction...\", \"The first one\") and a doubled \"again, or ... again\"",
      change="The first sentence is cut, and it starts \"One is a skeptic\".",
      old='''Two kinds of reaction really are trying to protect you, more often than not. The first one is on duty all the time, and it can sound like a skeptic: "You're just making this up." It may have spent years keeping you from being humiliated again, or left again,''',
      new='''One is a skeptic, on duty all the time: "You're just making this up." It may have spent years keeping you from being humiliated or left again,'''),
 dict(id='a17', half='A', where="Two Common Guarding Patterns P2", tries='third try',
      windows="High 95 (its start), Medium 17, Low 5, Low 11, Low 15, High 23 and Medium 21",
      tells="a short empathic knock-down (\"I'd want out too.\") and a \"like X, or like Y\" pair",
      change="Both are cut; his yawn and Re-evaluation Counseling, \"The skeptic and the pull both\" and the part's \"See? I knew it\" stay.",
      old='''Maybe it doesn't believe there's a grown-up around who could handle what's coming. I'd want out too. That yawn''',
      new='''Maybe it doesn't believe there's a grown-up around who could handle what's coming. That yawn''',
      old2='''If you treat either one like an enemy, or like proof that something's wrong with you, it'll probably just think "See? I knew it," and stay in charge.''',
      new2='''If you treat either one like an enemy, it'll probably just think "See? I knew it," and stay in charge.'''),
 dict(id='a18', half='A', where="Two Common Guarding Patterns P3", tries='third try',
      windows="Medium 21, High 68 and Medium 22, all but its last line",
      tells="a follow-up that restates (\"You just expect it\") and a summary signpost (\"So with any of these\")",
      change="Both are cut. The three ways of handling the expectation stay (his 77.3).",
      old='''You probably never said it to yourself in words. You just expect it, and it steers you before you know why.''',
      new='''You probably never said it to yourself in words, but it steers you before you know why.''',
      old2='''So with any of these, I'd ask what it's protecting you from''',
      new2='''With any of these, I'd ask what it's protecting you from'''),
 dict(id='a19', half='A', where="Two Common Guarding Patterns P4", tries='third try',
      windows="Low 52, from \"Then nobody offers\" on",
      tells="a reassuring reframe and a tidy closer (\"I'd just notice whether that's still true now.\")",
      change="One sentence says what keeping quiet costs now.",
      old='''Keeping quiet might have been the smartest thing you could do back then, with nobody safe to tell. I'd just notice whether that's still true now.''',
      new='''Keeping quiet might have been the smartest thing you could do back then, with nobody safe to tell, but now it can keep help away.'''),
 dict(id='b01', half='B', where="Untangling the Belonging Bargains P4", tries='second try',
      windows="High 46, Medium 16 and Low 13, all of it",
      tells="a word on the risk list (\"quieter\"), a concession (\"and that's worth sorting out\"), a balanced contrast (\"isn't help, though it can feel like loyalty\") and a hedge (\"doesn't by itself mean\", O43)",
      change="The paragraph is the bargain itself, so his 82a paragraph after it has its \"That's exactly why\" pointing at the bargain; the small good thing is one sentence after his paragraph.",
      old='''Some families run on a quieter bargain: "If I'm happy while someone I love is suffering, I'm abandoning them." You might really owe them help, and that's worth sorting out. Being miserable alongside them isn't help, though it can feel like loyalty. I'd try a small good thing, like a nice meal, and see what actually happens. Someone getting upset about it doesn't by itself mean you hurt them.''',
      new='''Some families run on a bargain like "If I'm happy while someone I love is suffering, I'm abandoning them."'''),
 dict(id='b02', half='B', where="Let the Child Be Bad at Things P3", tries='first try',
      windows="Low 56, from \"Either way\" into The Inner Guide P1",
      tells="a wry closer (\"You might catch yourself wondering when you became someone who does this.\")",
      change="It's cut.",
      old='''Either way, that's pl/ork in its most literal form: play becomes part of forming your identity. You might catch yourself wondering when you became someone who does this.''',
      new='''Either way, that's pl/ork in its most literal form: play becomes part of forming your identity.'''),
 dict(id='b03', half='B', where="The Inner Guide P1", tries='first try',
      windows="Low 56, Low 27 and Low 14, to \"at its own pace\"",
      tells="a balanced maxim (\"keep the standard and drop the tone\")",
      change="It's cut; the sentence before it says it.",
      old='''Your parent's harsh tone doesn't come with the job, though. If you hear it coming out of you, keep the standard and drop the tone.''',
      new='''Your parent's harsh tone doesn't come with the job, though.'''),
 dict(id='b04', half='B', where="The Inner Guide P4", tries='third try',
      windows="Medium 65, its last three sentences",
      tells="a second offered example (\"Or maybe, ...\") and a second instruction nested in the last one (\"and if you need a minute, say when you'll be back\")",
      change="Both are cut.",
      old='''I'd try croaking to someone you trust, "Could you pick up some soup?" Or maybe, "I'd really like to just watch a movie with you." If you keep swinging between spoiling and clamping down, try staying warm while you say what happens next, like "Not now, we'll go after lunch," and if you need a minute, say when you'll be back.''',
      new='''I'd try croaking to someone you trust, "Could you pick up some soup?" If you keep swinging between spoiling and clamping down, try staying warm while you say what happens next, like "Not now, we'll go after lunch."'''),
 dict(id='b05', half='B', where="How Much Happiness Do You Know Is Possible? P3", tries='third try',
      windows="Medium 39, its last sentence",
      tells="three instructions chained in one sentence",
      change="Two sentences, with \"If you meet\".",
      old='''Read people from different traditions, and if you get the chance, spend time around someone who's happy in a way that doesn't add up, and see how they treat people when their own day is going badly.''',
      new='''Read people from different traditions. If you meet someone who's happy in a way that doesn't add up, see how they treat people when their own day is going badly.'''),
 dict(id='b06', half='B', where="How Much Happiness Do You Know Is Possible? P5", tries='first try',
      windows="Low 28, its last two sentences",
      tells="an aphorism closer that repeats the quote (\"the limits ... are the limits\")",
      change="It's cut.",
      old='''But what if the experience is possible for me?" Don't assume the limits of what you've felt so far are the limits of what's possible.''',
      new='''But what if the experience is possible for me?"'''),
 dict(id='b07', half='B', where="Somatic Heart Opening P1", tries='first try',
      windows="Low 13, Low 30, High 32 and Low 10, to \"stay with it\"",
      tells="an aphoristic turn (\"from the other side\") and a reassuring negation (\"and that doesn't mean the love failed\")",
      change="Both are cut; the guide's Rumi line stays.",
      old='''Being loved can open grief from the other side, too. Someone takes care of you, and you think, "Why does this make me sad?" It can be sadness for the care that was missing, and that doesn't mean the love failed.''',
      new='''Being loved can open grief, too. Someone takes care of you, and you think, "Why does this make me sad?" It can be sadness for the care that was missing.'''),
 dict(id='b08', half='B', where="When the Practice Feels Real but Stays Shallow P1", tries='first try',
      windows="Low 47, its last two sentences",
      tells="a tidy closer (\"before you write off the whole thing\")",
      change="It's cut; his night line is unchanged.",
      old='''And if nightmares start wrecking your sleep, do less of the practice, earlier in the day or for a shorter time, before you write off the whole thing.''',
      new='''If nightmares start wrecking your sleep, do less of the practice, earlier in the day or for a shorter time.'''),
 dict(id='b09', half='B', where="Write It. Don't Send It Yet. P7", tries='second try',
      windows="Low 18, Low 15 and Low 18, all of it",
      tells="a hedged closer (\"I still won't know how they'll take it, but it might change a word or two.\")",
      change="It's cut.",
      old='''What felt scared when I wrote it can read like a threat from over there. I still won't know how they'll take it, but it might change a word or two.''',
      new='''What felt scared when I wrote it can read like a threat from over there.'''),
 dict(id='b10', half='B', where="How This Relates to IFS P7", tries='first try',
      windows="Low 65, its last two sentences, into Related Clinical Work",
      tells="a wry fragment tacked on (\"Or safer, for that matter.\")",
      change="One clause.",
      old='''Having a big institute with certifications behind it doesn't make a model any truer, either. Or safer, for that matter.''',
      new='''Having a big institute with certifications behind it doesn't make a model any truer or safer.'''),
]

AFTER_82A = dict(id='b01b', anchor="That's exactly why I was crying for 14 years.",
                 text='''I'd still try a small good thing, like a nice meal, and see what actually happens.''',
                 note=('Turn 93 (experiments/t93-tells/TELLS-ROUND2.md, item b01): the small good thing from the turn-90 loyalty-bargain '
                       'paragraph (GPT\'s advice on the Schema Hacks material, Joel 2026-10-22 18:03 UTC), moved after his 82a paragraph '
                       'so his "That\'s exactly why" follows the bargain itself. GPT\'s two corrections (real responsibilities; someone '
                       'upset isn\'t proof you hurt them) are out with the hedge. Lint %s. Not yet checked in Pangram.'))


def para_index(lines, frag):
    hits = [i for i, l in enumerate(lines) if frag in l and not l.startswith('<!--')]
    assert len(hits) == 1, (frag[:60], hits)
    return hits[0]


def main(lint=None):
    lint = lint or {}
    art = ART.read_text(encoding='utf-8')
    for it in ITEMS:
        for o, n in ((it['old'], it['new']), (it.get('old2'), it.get('new2'))):
            if o is None:
                continue
            assert art.count(o) == 1, (it['id'], art.count(o))
            art = art.replace(o, n)
    lines = art.split('\n')
    drafts = HERE / 'drafts'
    drafts.mkdir(exist_ok=True)
    for it in ITEMS:
        i = para_index(lines, it['new'][:70])
        (drafts / ('%s.txt' % it['id'])).write_text(lines[i] + '\n', encoding='utf-8')
        note = '<!-- ' + HEAD % (it['id'], it['half'], it['tries'], it['windows'], it['tells'], it['change'],
                                 lint.get(it['id'], 'pending')) + ' -->'
        lines[i:i] = [note, '']
    i = para_index(lines, AFTER_82A['anchor'])
    note = '<!-- ' + AFTER_82A['note'] % lint.get('b01b', 'pending') + ' -->'
    lines[i + 1:i + 1] = ['', note, '', AFTER_82A['text']]
    (drafts / 'b01b.txt').write_text(AFTER_82A['text'] + '\n', encoding='utf-8')
    ART.write_text('\n'.join(lines), encoding='utf-8')
    (HERE / 'FIXES.json').write_text(json.dumps({'items': ITEMS, 'after_82a': AFTER_82A}, ensure_ascii=False, indent=1) + '\n',
                                     encoding='utf-8')
    print('applied %d items, plus the sentence after 82a' % len(ITEMS))


if __name__ == '__main__':
    import sys
    main(json.loads(sys.argv[1]) if len(sys.argv) > 1 else None)
