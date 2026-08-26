#!/usr/bin/env python3
"""Apply Joel's 2026-08-26 Inner Child guide edits to raw Substack editor HTML.

This is an owner-authorized, exact-anchor transformation for an article that is not yet
registered as canonical in joel-articles. It deliberately does NOT infer a master from Git.
The raw Substack editor HTML supplied at runtime remains the source authority.

After the article edit, this script invokes the repository's canonical
project-sources/substack_transfer_helper.py.txt in the required init -> build -> verify
sequence. It never reimplements the clipboard helper.
"""
from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
import sys
from pathlib import Path

DATE = "20260826"


def p(value: str) -> str:
    return f"<p>{value}</p>"


def read_clipboard() -> str:
    commands = [
        ["wl-paste", "--no-newline"],
        ["xclip", "-selection", "clipboard", "-o"],
        ["xsel", "--clipboard", "--output"],
    ]
    errors: list[str] = []
    for cmd in commands:
        if shutil.which(cmd[0]) is None:
            continue
        try:
            proc = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as exc:
            errors.append(f"{cmd[0]}: exit {exc.returncode}")
            continue
        value = proc.stdout.decode("utf-8")
        if value.strip():
            return value
    detail = "; ".join(errors) if errors else "no supported clipboard reader found"
    raise RuntimeError(
        "Could not read the clipboard (" + detail + "). Install/use wl-paste, xclip, or xsel, "
        "or rerun with --input /path/to/raw-editor.html."
    )


def normalize_chat_escaped_html(text: str) -> str:
    # If an editor-HTML blob was copied through a surface that escaped angle brackets as \<...\>,
    # normalize only that recognizable representation. Normal raw editor HTML is left untouched.
    if '<div contenteditable="true"' not in text and '\\<div contenteditable="true"' in text:
        text = text.replace("\\<", "<").replace("\\>", ">")
    return text.strip()


class Editor:
    def __init__(self, source: str) -> None:
        self.text = source
        self.ops: list[str] = []

    def _count(self, needle: str) -> int:
        return self.text.count(needle)

    def require_once(self, needle: str, label: str) -> None:
        count = self._count(needle)
        if count != 1:
            raise ValueError(f"{label}: expected exactly 1 anchor, found {count}")

    def replace_once(self, old: str, new: str, label: str) -> None:
        self.require_once(old, label)
        self.text = self.text.replace(old, new, 1)
        self.ops.append(label)

    def insert_after(self, anchor: str, addition: str, label: str) -> None:
        self.require_once(anchor, label)
        self.text = self.text.replace(anchor, anchor + addition, 1)
        self.ops.append(label)

    def replace_section(self, start: str, end: str, replacement: str, label: str) -> None:
        self.require_once(start, label + " start")
        self.require_once(end, label + " end")
        a = self.text.index(start)
        b = self.text.index(end, a + len(start))
        if b <= a:
            raise ValueError(f"{label}: invalid section order")
        self.text = self.text[:a] + replacement + self.text[b:]
        self.ops.append(label)


def apply_edits(raw: str) -> tuple[str, list[str]]:
    e = Editor(raw)

    # Identity / stale-source gate. These anchors should all exist in the source supplied by Joel.
    for needle, label in [
        ("<h1>The Chicken-and-Egg Problem</h1>", "article identity: chicken-and-egg"),
        ("<h1>Borrow the Adult Before You Can Be the Adult</h1>", "article identity: borrowed adulthood"),
        ("<h2>When Love Is There but Doesn’t Feel Safe</h2>", "article identity: credibility section"),
        ("<h1>How to Forgive Without Forgetting</h1>", "article identity: forgiveness"),
    ]:
        e.require_once(needle, label)

    # 1. Don't Give the Inner Adult Away.
    my_journey_anchor = p(
        "Spiritual practice can continue while trauma heals. Divine love can help heal the wounded inner child when you direct it there. "
        "When the love stays above the wound, it reinforces the split."
    )
    guru = (
        "<h3>Don't Give the Inner Adult Away</h3>"
        + p("In my experience, most people do not start by becoming their own loving parent. They go looking for one. Sometimes it is a spiritual guru; sometimes a therapist, coach, partner, community, or ideology. That can be a healthy first stage. I call it borrowed adulthood. The helper lends a function you cannot yet hold alone. The trouble begins when the helper keeps it.")
        + p("A spiritual practice can change your relationship to pain. It cannot make an abusive person safe, repair a house, treat an infection, pay a debt, or leave a coercive relationship. Sometimes the adult move is to sit and feel. Sometimes it is to lock the door, call somebody, go to a doctor, get legal advice, or leave. A teaching that turns actual danger into merely ‘your story’ has stopped protecting the child.")
        + p("No-self teachings can also arrive out of order. If you were never allowed to discover what you like, believe, want, or refuse, you may need to build a self before you start dissolving it. Enough selfhood to stand; then enough flexibility not to become imprisoned by it. Using emptiness to erase an undeveloped self is spiritual bypass wearing very advanced clothes.")
        + p("The same problem appears with therapist-gurus. A helper may see a blind spot, challenge you, or model a missing adult function. They do not get final authority over your memories, relationships, body, medicine, conscience, or future. Even <a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://pemachodronfoundation.org/product/taking-the-leap-book/\">Pema Chödrön</a>, writing from a tradition that emphasizes devotion, says the teacher should “wean us from dependency altogether” and help us grow up. That is the test I keep. Are you becoming more able to think, disagree, protect yourself, and act without the helper?")
        + p("Borrow adulthood. Do not surrender it. The right helper stands beside you, teaches what they can, and gradually hands your life back.")
    )
    e.insert_after(my_journey_anchor, guru, "insert guru/helper authority section")

    # 2. Catch the hook before parts interpretation.
    regulation_anchor = p(
        "Use an eyes-open, present-focused version when imagery pulls you away from the room, time, or body you are actually in. "
        "If a session leaves you less able to function, more compulsive, or less oriented to the present, shorten it and bring in grounded support rather than trying to win a contest with your own nervous system."
    )
    hook = (
        "<h3>Catch the Hook Before You Interpret It</h3>"
        + p("Sometimes the first useful move is not to identify the child, the protector, or the origin of the reaction. Catch the moment the system gets hooked.")
        + p("The jaw tightens. The belly contracts. Heat rises. Something pulls back. Suddenly you want to attack, explain, text, scroll, drink, disappear, make a dramatic promise, or decide what the whole relationship means.")
        + p("<a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://pemachodronfoundation.org/product/taking-the-leap-book/\">Pema Chödrön</a> uses the Tibetan word <em>shenpa</em> for this hook: the tightening and urge that arrive before the complete storyline. Try this:")
        + "<ol>"
        + "<li><p>Look around the room and notice: “I am hooked.”</p></li>"
        + "<li><p>Unless immediate safety requires action, do not speak or act for one to three breaths.</p></li>"
        + "<li><p>Feel the bodily charge without deciding what it proves.</p></li>"
        + "<li><p>Ask which adult function is needed now: warmth, protection, or direction.</p></li>"
        + "<li><p>Take one small adult action, or relax and continue with the day.</p></li>"
        + "</ol>"
        + p("The story arising in that moment may be true, partly true, mistaken, or mixed with older material. The hook is not a truth detector. Pausing does not invalidate the story; it keeps an activated state from deciding the entire case.")
        + p("Acute work asks: What will prevent harm in the next ten minutes? What should I not say, send, consume, promise, or decide yet?")
        + p("Meaning work can come later: Which younger state or protector was involved? What present grievance is valid? What history does this resemble? What boundary, grief, repair, or developmental need remains?")
        + p("This is not an endurance test. One breath may be enough. If turning inward makes you less oriented, less functional, or more compelled, stop and use external support.")
    )
    e.insert_after(regulation_anchor, hook, "insert conditional hook practice")

    # 3. Caring-proxy / self-distancing section, replacing the old best-friend-only section.
    caring_proxy = (
        "<h2>Borrow Love—or Borrow the Perspective of Care</h2>"
        + p("Sometimes the missing capacity is not love itself. You can love other people or animals easily, but the feeling becomes inaccessible or unsafe when the recipient is you.")
        + p("Think of a pet, a baby, a friend, your own child, a partner, or anyone you naturally love. Feel the actual love first, without immediately trying to turn it into self-love. Let the body remember what the feeling is like. Then see whether a little of it can move toward the younger self.")
        + p("Don’t force the transfer. Even recognizing that the capacity exists somewhere in you is useful. You are borrowing a familiar pathway rather than manufacturing a feeling on command.")
        + p("Don’t make this exercise depend on a lucky biography. Some people can’t think of a best friend, loving parent, partner, child, or pet who feels usable as a proxy. In that case, imagine somebody whose intention is simply to take good care of you: an ideal parent, wise aunt, decent therapist, fictional character, future self, or an adult you invent for the purpose. If even that feels fake or threatening, begin with the least cruel, most sane response a minimally decent adult could give. The point is to borrow a caring function, not to prove that somebody like this existed in your past.")
        + p("Another shortcut is to ask:")
        + p("<strong>“If somebody I cared about had my actual history, limitations, and bad options, what would I say to them?”</strong>")
        + p("If nobody usable comes to mind, ask:")
        + p("<strong>“What would somebody who genuinely wanted to take good care of me say or do next?”</strong>")
        + p("Let this person have your actual history and constraints, not a tidier life where every sensible option was available. What would you say? What would you protect them from? What would you ask them to stop doing today? What small action would you advise next?")
        + p("It is amazing how much people wisen up when they ask this. Psychologists sometimes call the wider pattern <a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://pubmed.ncbi.nlm.nih.gov/24916084/\">self-distancing or Solomon’s paradox</a>: people often reason more wisely about another person’s conflict than their own, and taking a <a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://pubmed.ncbi.nlm.nih.gov/21728454/\">more distanced perspective</a> can narrow that gap. The exact prompt is my practical version of that idea.")
        + p("Do not borrow advice merely because it sounds generous. Advice to other people can become <a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://pubmed.ncbi.nlm.nih.gov/22268816/\">too idealistic</a> because the adviser does not have to pay the cost. Keep the part that is compassionate, sane, realistic, and based on the person’s actual options.")
        + p("Which adult function is speaking—the Nurturer, Protector, or Guide? Borrow one sentence or one action and do five percent of it for yourself. You do not have to feel fully convinced.")
        + p("Then imagine that the person shrugs, rejects the advice, or says, “Big whoop.” Which part remains true without requiring their gratitude, trust, or agreement? That is often the part your inner adult can borrow without turning care into a demand.")
        + p("Once you find one usable sentence or action, stop repeating the thought experiment in different words. Try the sentence or do the action.")
    )
    e.replace_section(
        "<h2>Borrow Love and Perspective You Already Have</h2>",
        "<h2>Become the Adult Apprentice</h2>",
        caring_proxy,
        "replace best-friend-only section with caring-proxy section",
    )

    # 4. Clarify three adult functions and worth vs capacity.
    old_functions = (
        "<ul><li><p><strong>Nurturer:</strong> receives pain with warmth. “It’s okay to feel this. You don’t have to do anything. I’m here.” The feeling is welcomed rather than forced away.</p></li>"
        "<li><p><strong>Protector:</strong> makes the warmth believable through boundaries, competence, and ordinary action.</p></li>"
        "<li><p><strong>Leader, Guide, or Guru:</strong> holds standards, chooses direction, and helps the child grow toward a whole life. I consider this the most important and most easily misread function.</p></li></ul>"
    )
    new_functions = (
        "<ul><li><p><strong>Nurturer:</strong> receives pain with warmth. “It is okay to feel this. You do not have to perform, solve it, or reassure me. I am here.” The Nurturer makes room for what is true without attacking the person who feels it.</p></li>"
        "<li><p><strong>Protector:</strong> makes the warmth believable through boundaries, competence, and ordinary action. The Protector works outside and inside: locking the door, ending the conversation, making the appointment, and also preventing a surge of fear, rage, craving, or shame from controlling speech, messages, spending, substances, sex, or relationship decisions.</p></li>"
        "<li><p><strong>Leader, Guide, or Guru:</strong> holds standards, chooses direction, and helps the child grow toward a whole life. The Guide does not need certainty. It chooses the next sane, value-consistent action while the future remains unknown. I consider this the most important and most easily misread function.</p></li></ul>"
        + p("Worth and adult capacity are different. The child did not become worthy when a reliable adult finally appeared. Worth was never the missing skill. What may be missing or inaccessible are adult capacities: pausing, regulating, protecting, choosing, staying, repairing, and acting consistently. Reparenting does not manufacture a better human being. It builds reliable functions around a life that was already worthy of care.")
    )
    e.replace_once(old_functions, new_functions, "clarify adult functions and worth/capacity")

    # Additional relational Protector evidence.
    protector_anchor = p("These acts accumulate into trust because internal soothing without external competence can sound like the same unreliability that wounded the child.")
    protector_relational = p("Some protective acts happen inside the relationship. Hearing “big whoop” without retaliating, allowing distrust without demanding reassurance, admitting that a complaint is true, and repairing after an internal attack can be as visible to the child as cleaning a room or keeping an appointment. Non-retaliation is evidence of love; it is not a substitute for love.")
    e.insert_after(protector_anchor, protector_relational, "add relational Protector evidence")

    # 5. Replace action-first credibility section with love/trust distinction, no blame trial.
    love_trust = (
        "<h2>Love Doesn’t Have to Wait for Trust</h2>"
        + p("Sometimes love is available and still feels unsafe because love and trust have become tied together as though one has to validate the other. They don’t.")
        + p("The younger state can look at the grown-up life and say, “I don’t trust you.” The adult can answer, “I believe you. And I love you.” Trust is allowed to examine old promises, continuing self-attack, and failures of protection. Love does not have to wait for trust to issue a favorable verdict.")
        + p("When I was about five, my mother told me it was time for bed—or something equally outrageous to a five-year-old. I cried and screamed, “I HATE YOU!” She answered, “But I love you!”")
        + p("That completely threw me. Her answer did argue with the emotional logic of the moment, and that may be exactly why it reached me. She did not tell me I wasn’t angry. She introduced a second truth: my hatred did not determine her love. I could hate somebody who loved me. The relationship did not have to mirror my current emotion to remain real.")
        + p("Don’t turn the sentence into a formula. “But I love you” can become dismissive when it means, “Therefore stop being angry.” The useful test is whether the love can remain alive, hear the anger, and take whatever is true in it seriously. Non-retaliation is one expression of love; it is not a colder substitute for love.")
        + p("The younger position may say:")
        + "<blockquote><p>“Big fuckity whoopty doo. I don’t believe you.”</p></blockquote>"
        + p("The adult can answer:")
        + "<blockquote><p>“Okay. I believe that you don’t believe me. I still love you. You don’t have to love me back. Tell me what feels unsafe.”</p></blockquote>"
        + p("The adult does not have to accept every conclusion. Listen for the concrete complaint without fighting the heat around it. If the criticism identifies something serious, answer it seriously.")
        + p("A <a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://www.springfieldspringfield.co.uk/movie_script.php?movie=a-beautiful-day-in-the-neighborhood\">dramatized scene</a> in <a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://www.sonypictures.com/movies/abeautifuldayintheneighborhood\"><em>A Beautiful Day in the Neighborhood</em></a> illustrates the same move. A cynical reporter suggests that it could not have been easy for Fred Rogers’s children to grow up with him. Rogers pauses, accepts that there may be truth in the criticism, and thanks him for the perspective. He neither collapses under the provocation nor fights it. He answers what is worth answering.")
        + p("Also notice what happens between the internal positions. If distrust is followed by accusation, the younger state may learn that love remains available only while it is received correctly. The resentful voice and the vow-making voice may be the same position, different positions, or a blend. Don’t merge them simply because both appear through the grown-up mind.")
        + p("When life has gone badly, the internal system may try to recover control by finding a defendant: some younger version must be guilty for failing to grow into the adult who was supposed to save everybody. But identifying the guilty age does not create the missing capacity.")
        + p("A five-year-old, an adolescent, a younger adult, and the person you were last year each acted from the awareness, conditioning, fear, support, and options they could actually access then. That does not make every choice harmless. Choices can hurt people, damage a life, and require repair. It means punishment cannot retroactively manufacture the awareness or capacity that was missing.")
        + p("Instead of asking which version deserves blame, ask:")
        + "<ul>"
        + "<li><p>What was that version trying to accomplish or avoid?</p></li>"
        + "<li><p>What did they understand at the time?</p></li>"
        + "<li><p>What options could they actually see and tolerate?</p></li>"
        + "<li><p>What happened because of the choice?</p></li>"
        + "<li><p>What capacity, support, or protection was missing?</p></li>"
        + "<li><p>What can the present adult learn, repair, or do differently now?</p></li>"
        + "</ul>"
        + p("“Big fuckity whoopty doo—what are you gonna do for me?” is still a literal question. But the first answer may be relational rather than practical: the love remains even when it is not believed. Trust can then update from both relational and ordinary-life evidence—being heard without retaliation, admitting where a complaint is true, repairing after an internal attack, keeping a boundary, attending an appointment, or handling one neglected problem.")
        + p("Relaxation may help you remain present for this conversation. It cannot decide whether the complaint is true, assign guilt, or create trust by itself.")
    )
    e.replace_section(
        "<h2>When Love Is There but Doesn’t Feel Safe</h2>",
        "<h2>Make a Simple Vow</h2>",
        love_trust,
        "replace credibility section with love/trust section",
    )

    # 6. Realistic loving vow and relational/practical credibility.
    old_vow = (
        "<blockquote><p>“I know you’re in there. I know I’ve ignored you, and I know you don’t trust me. That’s okay. You don’t have to do anything. My job, starting today, is to build a life that is safe for you. I will start listening. I will start protecting us.”</p></blockquote>"
        + p("If the child already sees a negative track record, don’t use the vow to argue with that judgment. You can say, <em>“You’re right that words aren’t enough. You don’t have to trust this. Watch what I do.”</em> Then begin with one action small enough to repeat.")
    )
    new_vow = (
        "<blockquote><p>“I know you are in there. I love you. You do not have to love me back or trust me yet. I cannot promise that nothing painful will happen, that I will always know what to do, or that I will never react badly. I can promise to tell you the truth, listen when you are angry, make our life safer where I can, take the next protective step I can see, and come back to repair when I fail. You do not have to believe these words. Watch what I do.”</p></blockquote>"
        + p("Trust may still answer, “Big whoop.” That is allowed. Choose one response small enough to repeat. It may be practical—keeping an appointment, ending an unsafe exchange, eating, sleeping, or handling one neglected task—or relational: listening without retaliation, admitting where the complaint is true, or repairing after you attack yourself. The vow becomes credible through repetition, not one beautiful session.")
    )
    e.replace_once(old_vow, new_vow, "replace overpromising vow")

    # 7. Least-elaborate model + relationship insight in Start With Whatever Showed Up.
    start_anchor = p("The cynical voice, numbness, urge to scroll, anger, dissociation, or sudden need to do something else all belong inside the pl/ork. The response may be a protector, the child speaking directly, an inherited critic, a present-day grievance, or a blend. Start with what it is trying to prevent, accomplish, or communicate before deciding who is speaking.")
    anti_reify = (
        p("Sometimes it is only a thought. Do not create a new inner person every time the mind produces a sentence. Use the least elaborate model that helps. A thought can be labeled “thinking,” allowed to pass, and followed by a return to the room. If it keeps returning with a coherent fear, strategy, age, or demand, a parts dialogue may help. The model serves the person, not the other way around.")
        + p("Once you have a tentative sense of what is present, don’t stop at naming the voices. Notice what each response teaches the others. A loving vow followed by blame when it is doubted teaches something very different from the same vow followed by curiosity. A protector who warns and is heard behaves differently from one that has to become louder because nobody listens. Often the useful insight is in the relationship between the positions, not in the label you give each one.")
    )
    e.insert_after(start_anchor, anti_reify, "add anti-reification and relational-insight paragraphs")

    # 8A. Pema's four hook pairs.
    belonging_anchor = p("The unparented child takes those bargains because belonging feels like life or death. Self-differentiation means noticing where belonging is being purchased with self-betrayal and learning to keep your own ground.")
    pairs = (
        "<h3>Four Pairs That Commonly Hook the Child</h3>"
        + p("<a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://pemachodronfoundation.org/product/taking-the-leap-book/\">Pema Chödrön</a> gives a quick map for finding the bargain: pleasure and pain, gain and loss, praise and blame, good reputation and disgrace. The child can panic not only when something hurts, but when praise, romance, money, status, belonging, or a spiritual high might disappear.")
        + p("Ask:")
        + "<ul><li><p>What do I think I am about to gain or lose?</p></li><li><p>Whose approval suddenly feels like survival?</p></li><li><p>Am I protecting a real value, or trying to preserve a high?</p></li><li><p>What would remain worth doing if nobody praised me for it?</p></li></ul>"
        + p("The aim is not to stop enjoying pleasure, praise, gain, or belonging. Notice when they have become conditions for having a self.")
    )
    e.insert_after(belonging_anchor, pairs, "insert four hook pairs")

    # 8B. Positive-hook warning.
    altered_anchor = p("The gate matters. Altered states can get past the guards before the adult functions are ready to hold what appears. Build sober Nurturer and Protector capacity first, or borrow those capacities from grounded support that does not seize authority over the experience.")
    positive_hook = p("The beautiful state can become a hook too. A psychedelic opening, dream, hypnosis session, meditation high, or sudden flood of love can become the new standard, and ordinary life then feels like failure. Intensity, relief, beauty, or a sense of revelation does not prove historical truth or completed healing. Look for what becomes more honest, protective, and reliable after the state ends.")
    e.insert_after(altered_anchor, positive_hook, "insert positive-hook warning")

    # 9A + 9B. Morning/evening review and common humanity.
    journal_anchor = p("This can bypass the silence people hit with speech or visualization. If the protector is what appears, let that part use the non-dominant hand first. Don’t demand the child before the guard has spoken.")
    practices = (
        "<h3>One Intention in the Morning, One Review at Night</h3>"
        + p("In the morning, choose one modest intention:")
        + "<blockquote><p>“Today I will notice one hook before I act from it.”</p></blockquote>"
        + p("At night, review the day without conducting a trial:")
        + "<ul><li><p>Where did I notice the hook?</p></li><li><p>Where did it run the sequence anyway?</p></li><li><p>What small repair or protective act comes next?</p></li><li><p>What moment of warmth, pleasure, courage, or connection did I actually receive?</p></li></ul>"
        + p("Count recognition as progress, even when it arrived afterward. If you interrupted the pattern, notice that too. Repair what can be repaired, renew the intention, and go to sleep.")
        + "<h3>Just Like Me</h3>"
        + p("Use this only when you are oriented enough that widening the circle does not pull you away from yourself.")
        + p("Name one feeling plainly: fear, shame, loneliness, craving, grief, anger, or confusion. Then say:")
        + "<blockquote><p>“Other people know this feeling too. Just like me, they want relief. Just like me, they sometimes make it worse while trying to escape it. May all of us find enough support to stay present and not pass the pain forward.”</p></blockquote>"
        + p("You can breathe normally and let the wish include yourself first, then anybody else who comes to mind. This is not a demand to forgive an abuser, imagine their childhood, or open contact while you are flooded. It is a way to stop carrying a universal human feeling as proof that you alone are defective.")
    )
    e.insert_after(journal_anchor, practices, "insert morning/evening and Just Like Me practices")

    # 9C. Deliberate close after photograph practice.
    photo_anchor = p("Put the photograph away when the practice is done. If it starts pulling you into compulsive searching, certainty, or dysregulation, stop using it for now and return to present-day regulation.")
    close = (
        "<h3>Close the Session and Return to Life</h3>"
        + p("Give every inner-child session a definite ending. Endless processing can become another way to avoid living.")
        + "<ol><li><p>Look around and name where you are.</p></li><li><p>Feel your feet, the chair, or another external contact point.</p></li><li><p>Relax your jaw and hands.</p></li><li><p>Name one ordinary action that comes next.</p></li><li><p>Say: “That is enough for today. We are returning to the life we are building.”</p></li></ol>"
        + p("The session does not have to resolve every feeling before you make food, answer a message, take a walk, or go to sleep. Returning to life is part of integration.")
    )
    e.insert_after(photo_anchor, close, "insert deliberate session close")

    # Missing-love fallback / witness logic.
    old_love_bullet = (
        "<li><p><strong>Love may already be familiar in another form.</strong> Most people have felt some form of it: warmth with a friend, care for a pet, or deep appreciation of beauty. Self-love can begin by turning an existing capacity inward.</p></li>"
    )
    new_love_bullet = (
        "<li><p><strong>Love may already be familiar in another form—or only imaginable as a direction.</strong> If care for a friend, child, animal, place, or beauty feels real, borrow from that. If nobody usable comes to mind, imagine somebody whose intention is simply to take good care of you: an ideal adult, fictional figure, future self, or other caring presence. If even that increases threat or loneliness, begin with the least cruel response a decent adult could offer. The exercise is a scaffold, not a test of whether you were loved enough.</p></li>"
    )
    e.replace_once(old_love_bullet, new_love_bullet, "broaden missing-love proxy fallback")
    old_witness_bullet = "<li><p><strong>Witness love in other people.</strong> Therapy, friendship, community, books, and stories can teach the logic of love until you begin to internalize it.</p></li>"
    new_witness_bullet = "<li><p><strong>Witness the logic of care wherever you can find it.</strong> Therapy, friendship, community, books, stories, fictional characters, and imagined caregivers can model warmth, protection, and repair until you begin to internalize those functions.</p></li>"
    e.replace_once(old_witness_bullet, new_witness_bullet, "broaden witnessed-care sources")

    # 10 + causal-compassion refinement in forgiveness.
    causal_anchor = p("The understanding that helps me is seeing how a person’s conditioning, history, pain, and capacity shaped the harmful move they made. Given the total person they had become by that moment, the harmful move was the only one their accumulated nature had available. Hurt people often pass forward pain they never processed. When that becomes something you can actually see rather than a moral instruction, forgiveness may arise by itself, and the rage that held the person as uniquely culpable can soften into something more accurate.")
    causal_insert = p("That does not mean the action was harmless or that no different option existed in the abstract. It means punishment cannot retroactively create the awareness, support, or capacity that was not available enough to guide the choice. The useful work is to repair what can be repaired and make a different response more available now.")
    e.insert_after(causal_anchor, causal_insert, "clarify causal compassion vs consequences")

    old_self_forgiveness = "Let remorse register the inner adult’s recognition that the action violated your values and used the child to do something the child wouldn’t freely choose."
    new_self_forgiveness = "Let remorse register that the action violated your values or caused harm. Remorse can guide repair and changed behavior without turning the person who acted into a permanent criminal."
    e.replace_once(old_self_forgiveness, new_self_forgiveness, "remove self-forgiveness prosecution frame")

    forgiveness_anchor = p("Some harms take years. Premature forgiveness is one trap; permanent residence inside resentment is another. Don’t push or bypass. Stay with the inquiry until the understanding becomes real enough to change the emotional relationship.")
    bardo = (
        "<h1>When One Life Has Ended and the Next Hasn’t Begun</h1>"
        + p("The inner child often becomes loudest in the gap after one life has ended and before the next has formed: after a breakup, migration, illness, loss of faith, loss of a role, a child leaving home, or the decision to leave a family or community on different terms.")
        + p("Tibetan Buddhism calls an in-between state a <a target=\"_blank\" rel=\"noopener noreferrer nofollow\" href=\"https://pemachodronfoundation.org/product/how-we-live-is-how-we-die-book/\"><em>bardo</em></a>. You do not have to accept its teachings about death or rebirth to use the ordinary-life insight: endings create a period with no familiar identity and no clear replacement.")
        + p("Ask:")
        + "<ul><li><p>What has actually ended?</p></li><li><p>What am I still trying to make continue?</p></li><li><p>What is not known yet?</p></li><li><p>What does the child fear will happen in the gap?</p></li><li><p>What practical act or small ritual would mark the ending without pretending I know the next beginning?</p></li></ul>"
        + p("Do not force a new identity because uncertainty feels unbearable. The adult can keep routines, protect the body, grieve what ended, and remain with the child while the next life takes shape.")
    )
    e.insert_after(forgiveness_anchor, "<hr contenteditable=\"false\">" + bardo, "insert endings/transitions practice")

    # Conclusion echo: love is unconditional, trust is evidence-sensitive.
    conclusion_sentence = "Love precedes anything you could earn."
    conclusion_replacement = conclusion_sentence + " Trust is different. It is allowed to grow slowly from truth, protection, repair, and what you repeatedly do. You do not have to withhold love until trust catches up."
    e.replace_once(conclusion_sentence, conclusion_replacement, "echo love/trust distinction in conclusion")

    return e.text, e.ops


def run_helper(repo: Path, source: Path, output_dir: Path) -> dict[str, Path]:
    helper_script = repo / "project-sources" / "substack_transfer_helper.py.txt"
    compat = repo / "project-sources" / "CONFIRMED-SUBSTACK-HELPER.json"
    islands = repo / "project-sources" / "html_islands.py.txt"
    for required in (helper_script, compat, islands):
        if not required.is_file():
            raise FileNotFoundError(f"Required canonical helper authority missing: {required}")

    output_dir.mkdir(parents=True, exist_ok=True)
    plan = output_dir / "inner-child-guide-transfer-plan.json"
    inventory = output_dir / "inner-child-guide-native-object-inventory.json"
    helper = output_dir / "inner-child-guide-substack-transfer-helper.html"
    report = output_dir / "inner-child-guide-substack-transfer-report.md"
    compat_report = output_dir / "inner-child-guide-substack-compatibility-report.md"

    base = [sys.executable, str(helper_script)]
    subprocess.run(base + ["selftest"], check=True)
    subprocess.run(base + ["init", str(source), "--plan", str(plan), "--inventory", str(inventory), "--compat-profile", str(compat)], check=True)
    subprocess.run(base + ["build", str(source), "--plan", str(plan), "--compat-profile", str(compat), "--out", str(helper), "--report", str(report), "--compat-report", str(compat_report)], check=True)
    subprocess.run(base + ["verify", str(source), "--plan", str(plan), "--compat-profile", str(compat), "--helper", str(helper), "--compat-report", str(compat_report)], check=True)
    return {
        "plan": plan,
        "inventory": inventory,
        "helper": helper,
        "report": report,
        "compat_report": compat_report,
    }


def maybe_open(path: Path) -> None:
    candidates = [
        ["opera", path.as_uri()],
        ["opera-stable", path.as_uri()],
        ["xdg-open", str(path)],
    ]
    for cmd in candidates:
        if shutil.which(cmd[0]):
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Opened helper with: {cmd[0]}")
            return
    print(f"Helper is ready but no browser opener was found: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    src = parser.add_mutually_exclusive_group()
    src.add_argument("--input", type=Path, help="Raw Substack editor HTML file instead of clipboard")
    src.add_argument("--clipboard", action="store_true", help="Read raw Substack editor HTML from desktop clipboard (default)")
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Local joel-articles checkout containing project-sources")
    parser.add_argument("--output", type=Path, default=Path.home() / "Téléchargements" / f"inner-child-guide-updated-{DATE}.html")
    parser.add_argument("--helper-dir", type=Path, default=Path.home() / "Téléchargements" / f"inner-child-guide-transfer-{DATE}")
    parser.add_argument("--open", action="store_true", help="Open the verified canonical helper in Opera/desktop browser")
    args = parser.parse_args()

    repo = args.repo.expanduser().resolve()
    if args.input:
        raw = args.input.expanduser().read_text(encoding="utf-8")
        source_label = str(args.input)
    else:
        raw = read_clipboard()
        source_label = "clipboard"
    raw = normalize_chat_escaped_html(raw)

    updated, operations = apply_edits(raw)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(updated, encoding="utf-8")

    helper_paths = run_helper(repo, args.output, args.helper_dir.expanduser())
    patch_report = args.helper_dir.expanduser() / "inner-child-guide-update-report.json"
    patch_report.write_text(
        json.dumps(
            {
                "format": "joel-inner-child-guide-update-20260826",
                "source": source_label,
                "operation_count": len(operations),
                "operations": operations,
                "updated_html": str(args.output),
                "canonical_helper": str(helper_paths["helper"]),
                "transfer_report": str(helper_paths["report"]),
                "note": "Article is not registered in joel-articles; runtime raw editor HTML was the source authority for this owner-authorized update.",
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Applied {len(operations)} exact owner-authorized article operations.")
    print(f"Updated archival HTML: {args.output}")
    print(f"Verified Substack helper: {helper_paths['helper']}")
    print(f"Update report: {patch_report}")
    print("The helper will expose ordered Copy Part controls and manual native-video insertion steps when required by the source.")
    if args.open:
        maybe_open(helper_paths["helper"].resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
