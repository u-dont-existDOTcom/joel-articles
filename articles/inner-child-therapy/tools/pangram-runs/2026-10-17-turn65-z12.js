const items0 = [["t65z12_le1p3w1p1", () => "Missing someone doesn't have to become another problem to solve. Sometimes the ache itself can turn into a cue for love, so don't push the missing away. If love is there, let \"I miss you\" become \"I love you,\" or offer a simple wish, something like \"May you be safe. May you be held in love.\" Picture them, or just feel the direction of the care. Maybe you don't believe they receive any of it. You don't have to, since this is about what happens in you. It doesn't replace grieving or contact, or boundaries, or whatever practical thing needs doing. If sending love makes you more compulsive or unreal, make it simpler: \"I miss you, and I care.\" The same goes if you can't get back to your life. You can also offer some of that care to the part of you that's still here.", "feb2f00474b0f1d9e6ff802ef5e4d22eaeee0348119107875083a532b202a780"], ["t65z12_fg1p1w2p1", () => "For many people, healing eventually includes some forgiveness, or at least getting out from under active resentment. You can't schedule forgiveness, though. If you're not there, you're not there. And you don't need it first to be safe or set boundaries. Holding someone accountable and getting justice can come first too, and so can recovering. Still, active resentment can narrow what you see and keep the injury at the center of your little one's world. Pressure to forgive early gets you an act that looks enlightened, while the wound goes underground.", "5367ce1fd94d3e156fe18cf0c634d6f85864a3d62a051a5e74370ae9bacdf4bf"], ["t65z12_fg1p2w8p1", () => "What can help is seeing how they got there. Picture everything that had made them who they were by that moment, what happened to them and what they learned, the pain they carried and what they could and couldn't handle. From in there, it was the only move they had. Hurt people often pass on pain they never worked through. You may have heard that from somebody telling you to forgive. When you see it for yourself, though, you might find yourself forgiving them, and if you've held them uniquely to blame, the rage can soften into something more accurate.", "527a22738f7ad30183545df4c575c5f31a82531a71fa6eb006a2651a3301def4"], ["t65z12_fg1p2w9p1", () => "What can help is understanding how they got to be someone who'd do that. Their history went into it. So did what was done to them, and their own pain. By then there wasn't much they could handle. Given all of it, that move was the only one they had. Hurt people often pass on pain they never worked through. You may have heard that from somebody telling you to forgive. When you see it for yourself, though, you might find yourself forgiving them, and if you've held them uniquely to blame, the rage can soften into something more accurate.", "3b73dfa54c02381e6af3db56083d0f8bd0becc4f9430213bca7ef2cfb7496399"], ["t65z12_fg1p3w2p1", () => "Seeing all that doesn't make what they did harmless, or mean that in theory nothing else was possible. Since it was the only move they had available, though, punishment can't go back and give them the awareness or support they were short on. Or the ability. The useful work is repairing what can be repaired, and making a different move more available now. They still have to answer for it, morally and sometimes legally, and the harm is real. Boundaries and distance can still be right, for good if it comes to that. You can understand them and still hold them responsible. You can also forgive someone you'll never speak to again. In your head, \"I understand how you became this way\" can sit right next to \"I now understand why I shouldn't rely on you for this.\"", "d6a23e4f30c5aa40e0dedd3436d55ecb96e6a9bbcf9c22c0291e183c94d93a86"], ["t65z12_st1p5w1p1", () => "This can be borrowed adulthood at its healthiest. Your peer doesn't become your permanent parent. Your little one might be hoping they will. They show you something a grown-up can do and help you take part in it. Then they hand it back to you. Therapy is still useful for what therapy does. Community and peer support done by the rules do something different, and if you're serious about healing, your path can include both.", "61e538c4d35f654ec0132d9675f9ecd4c690e3458bf73c6378c7f6ab9485416c"], ["t65z12_st1p2w1p1", () => "None of this is forced positivity, though. Grief is grief, and if something is dangerous, call it dangerous. You still need accurate words for harm, anger, limits, accountability, consent and practical constraints. Some of those can be hard to say to your little one. Once you've named what's real, put most of your energy into what can be protected or practiced. For that, you don't need a picture of what not to become. What can be repaired? What can you choose now, or grow?", "555ae60405a86dcc225ed5c0f7721c8f540a421ed295c5947e49814c3592ce36"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t65z12" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t65z12 = [];
const log = m => { window.__t65z12.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t65z12)); } catch (e) {} };
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
