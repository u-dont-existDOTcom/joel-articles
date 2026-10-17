const items0 = [["t65z7_sh1w7p1", () => "Some people have the opposite problem: it feels like you're connecting with your little one, but the contact stays near the surface. Meditating for a long time and then sleeping, especially a second sleep, after you've already slept once, can open up much more emotionally direct material. Then the dream that night hits harder than the whole session did, with way more feeling and need in it, and you wake up wondering where all that was during the day. That's the sign this is you (a session that was good and just didn't stick around is something else). Whatever came up, what's available to you now that wasn't before, and how do you see it? And if nightmares start wrecking your sleep, try a smaller dose, earlier in the day or shorter, before you write off the whole thing.", "3c8eb7b2d896cc85ad2c6302017d1d366eee99e7367e846d169aeaa06de9834a"], ["t65z7_sh1w6p1", () => "Some people have the opposite problem. It feels like you're connecting with your little one, but the contact is staying near the surface. Meditating for a long time and then sleeping can open up much more emotionally direct stuff, especially in a second sleep, after you've already slept once. So say the dream that night carries far more feeling and need than the session came anywhere near. That's the sign this is you (a session that was good and just didn't stick around is something else). Whatever came up, what's available to you now that wasn't before, and how do you see it? And if nightmares start wrecking your sleep, try a smaller dose, earlier in the day or shorter, before you write off the whole thing.", "a40d0403273e4c07eaf7c7e0efee79813c8a5ebdd9385f9b371fe0742829bc1d"], ["t65z7_secsh1w6", () => "# When the Practice Feels Real but Stays Shallow\n\nSome people have the opposite problem. It feels like you're connecting with your little one, but the contact is staying near the surface. Meditating for a long time and then sleeping can open up much more emotionally direct stuff, especially in a second sleep, after you've already slept once. So say the dream that night carries far more feeling and need than the session came anywhere near. That's the sign this is you (a session that was good and just didn't stick around is something else). Whatever came up, what's available to you now that wasn't before, and how do you see it? And if nightmares start wrecking your sleep, try a smaller dose, earlier in the day or shorter, before you write off the whole thing.", "788cc1b0418c23bb1f020a8320b47f0591e84ddc89305ce67556d4a06b0c64f0"], ["t65z7_secsh1w7", () => "# When the Practice Feels Real but Stays Shallow\n\nSome people have the opposite problem: it feels like you're connecting with your little one, but the contact stays near the surface. Meditating for a long time and then sleeping, especially a second sleep, after you've already slept once, can open up much more emotionally direct material. Then the dream that night hits harder than the whole session did, with way more feeling and need in it, and you wake up wondering where all that was during the day. That's the sign this is you (a session that was good and just didn't stick around is something else). Whatever came up, what's available to you now that wasn't before, and how do you see it? And if nightmares start wrecking your sleep, try a smaller dose, earlier in the day or shorter, before you write off the whole thing.", "f6d549e7a08c8a0bf8cd25074f3480c4f8275978531fcf4768cc5c399be55ef8"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t65z7" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t65z7 = [];
const log = m => { window.__t65z7.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t65z7)); } catch (e) {} };
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
