const items0 = [["t69i_secks2", () => "# If You Want to Kill Yourself\n\nI try not to proselytize about spirituality, because I've made that mistake before, and I now see that it's better to let folks find it when they are ready. But when someone tells me they want to kill themself, I consider the topic to be brutally opened by default, regardless of whether they meant to do that, because if they actually do kill their body (which they might mistake to be their self), that's a very powerful spiritual challenge right there, even if they didn't realize it would be.\n\nMaybe you're reading this about to act, or with the means close by. Then before anything else, get another human being involved, and put some distance between you and the means. A crisis line or an emergency number counts, and the person on the other end can be a total stranger. Do the same if you can't stop yourself, or you're badly disoriented or intoxicated. Can't tell if that's you? Treat it like it is. None of that is me answering whether life is worth living. It just keeps the question open long enough to look at.\n\nThen, before getting all philosophical, make sure there's a real, live grown-up in the room or on the phone, if that's possible. And as for the internal psychology of it, when the part that wants to die feels like all of you, go ahead and notice who's doing the noticing (as we discussed in Noticing Counts), or borrow an adult from the adult lending library in your head :). Any part of you that can help keep your body safe, or would rather wait on a decision you can't undo, is welcome. And if none of them shows up yet? No problem, the questions can wait.\n\nThen ask: what is the self you want to kill? Is that self the same thing as your body? Why? Do you have the same body in dreams? What exactly do you expect your body's death to accomplish? If the problem is a state of mind, like self-hatred or despair, shame or loneliness, what makes you so sure that destroying the body ends it?\n\nIn Buddhism, death isn't an off switch, and it isn't a free new-age get-out-of-jail card back to the source. Repeated thought and intention shape the mind, and that keeps going through death and rebirth. Yes, that can include hell realms. A human birth is a rare chance to understand suffering and end its causes. You don't have to believe that, of course.\n\nBut if you're still thinking of staking your life on the opposite claim, that death is just nothing, look into that claim first (and if you're at the edge right now, the first step above comes before any of this). Near-death experiences and seriously studied rebirth reports can't give you reliable odds about death itself. They can still put a dent in the certainty that destroying the body means nothing comes after.\n\nAnd you can watch the mind pick up momentum inside this one life, too. Rumination feeds rumination, and the more you hate yourself, the better your mind gets at it (isolation tends to deepen despair, too). Physical life keeps handing you redirections, though, like other people and things you have to do, and help when you reach for it. If the many traditions and the accumulating scientific evidence are right that the mind's causal process goes on after the body dies, killing the body may take away some of those redirections and leave the suffering right where it was.\n\nMy father used to tell suicidal people, \"Oh, you want to kill yourself? That's wonderful. Now you can change what you've always been too afraid to change in your life, and then see if you still want to end it!\" His point wasn't that dying is wonderful. If everything's already on the table, what's the change you still can't bring yourself to make? Leaving? Quitting? Moving? Telling your family who you really are? Those aren't free, and you can't always take them back, but they're smaller than dying, and they can wait until you're calmer and have some help. Look at that life you've been afraid to change while you still have a human body, and people around to help redirect the path.", "9dd3c6f3fb85f153fbfda9e6f35e752edc4013912c24cdded76b0266aa5f1923"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t69i" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t69i = [];
const log = m => { window.__t69i.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t69i)); } catch (e) {} };
const other = () => { try { return JSON.parse(localStorage.getItem(lane(rev ? 'fwd' : 'rev')) || '[]').filter(m => / (clicked|taking)$/.test(m)).map(m => order0.indexOf(m.split(':')[0])); } catch (e) { return []; } };
const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const button = () => [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText));
const wait = ms => new Promise(r => setTimeout(r, ms));
async function run() {
  for (const [k, mk, want] of items) {
    const o = other(), i = order0.indexOf(k);
    if (o.length && (rev ? i <= Math.max(...o) : i >= Math.min(...o))) { log('stop at ' + k + ': the other tab has the rest'); break; }
    log(k + ': taking');  // claimed before the work, so the other tab never takes it too (turn 65: with a margin
                          // of one instead, both tabs stopped short of the last check)
    const T = mk();  // built when its turn comes, so it can use texts stored earlier in this batch
    for (let j = 0; j < 20 && !(button() && document.querySelector('textarea')); j++) await wait(500);
    const ta = document.querySelector('textarea');
    if (!ta) { log(k + ': no textarea'); break; }
    setter.call(ta, T); ta.dispatchEvent(new Event('input', {bubbles: true}));
    let b = null;
    for (let j = 0; j < 30; j++) { await wait(500); b = button(); if (b && !b.disabled) break; }
    const h = await sha(ta.value);
    if (h !== want) { log(k + ': hash mismatch ' + h + ' (is its prefix in sessionStorage?)'); break; }
    if (!b || b.disabled) { log(k + ': button not ready'); break; }
    try { sessionStorage.setItem(k, T); } catch (e) {}
    b.click(); log(k + ': clicked');
    await wait(10000);
  }
  log('end');
}
run(); 'started'
