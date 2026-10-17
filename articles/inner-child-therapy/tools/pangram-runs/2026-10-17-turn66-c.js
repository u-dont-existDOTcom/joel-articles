const items0 = [["t66c_fg1p4w7p1", () => "Forgiving yourself works the same way. Own what you did (only what was yours), and let yourself feel the remorse. Repair what you can, by apologizing or making amends. Changing the behavior counts too. Then you're allowed to stop holding yourself hostage, and the responsibility stays. If you're thinking \"not me, not after what I did,\" forgiving other people tends to be harder too. Some harms take years, so don't push it. Forgive too soon and it's only a show; stay in the resentment and you end up living there. Every so often, come back to how whoever did it got to be someone who could do that, until you understand it well enough that it changes how you feel.", "9118cbbb10a57d0b5e6eeaabf06d5417b6ce554ca0ced59c9d69348b8402d2b0"], ["t66c_secfgall4w7", () => "# How to Forgive Without Forgetting\n\nFor many people, healing does get around to some forgiveness eventually, or at least to not being run by the resentment anymore. It can't be put on a schedule (nobody gets a gold star for forgiving fastest). And you don't have to forgive first to get safe, set boundaries, hold someone accountable, get justice or get better. Then again, active resentment narrows what you see, and your little one stays organized around the injury. And if someone pressures you into forgiving early, what you get is an enlightened-looking act, with the wound gone underground.\n\nWhat can help is seeing how they got there. Picture everything that had made them who they were by that moment, what happened to them and what they learned, the pain they carried and what they could and couldn't handle. From in there, it was the only move they had. Hurt people often pass on pain they never worked through. You may have heard that from somebody telling you to forgive. When you see it for yourself, though, you might find yourself forgiving them, and if you've held them uniquely to blame, the rage can soften into something more accurate.\n\nThey still have to answer for what they did, and it still hurt. Seeing how they got there doesn't make it okay, and in theory they could have done something else. It's just that punishing them now can't reach back and give them what they were missing then, the sense to see it or the help. Or the skills. What's left is fixing what can be fixed, and making it easier for something different to happen now. So a boundary can still be right. So can the law, if it comes to that, or telling them plainly it was wrong (or telling yourself, if they'd never hear it). Keeping away from them for good can be right too, and you can still forgive them from over there. \"I understand how you became this way\" can sit right next to \"I now understand why I shouldn't rely on you for this.\"\n\nForgiving yourself works the same way. Own what you did (only what was yours), and let yourself feel the remorse. Repair what you can, by apologizing or making amends. Changing the behavior counts too. Then you're allowed to stop holding yourself hostage, and the responsibility stays. If you're thinking \"not me, not after what I did,\" forgiving other people tends to be harder too. Some harms take years, so don't push it. Forgive too soon and it's only a show; stay in the resentment and you end up living there. Every so often, come back to how whoever did it got to be someone who could do that, until you understand it well enough that it changes how you feel.", "2c0901382a5fb4754a5c2060c04ce3af6127be52aef2d7b788b581dfe0387819"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t66c" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t66c = [];
const log = m => { window.__t66c.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t66c)); } catch (e) {} };
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
