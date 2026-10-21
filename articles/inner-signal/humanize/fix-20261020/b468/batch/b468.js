const items0 = [["HG15-p9e2", () => "What is the difference between a human doer and a human being? If you don\u2019t feel good enough as a human being, you will try to become good enough as a human doer by for example being beautiful, doing something well, being smart, having a certain status, being spiritual, etc. I\u2019m not saying those can\u2019t be real gifts, but if failing at one of them feels like losing yourself, then you\u2019re using it to buy belonging.", "e2a7669aff449e5d463753aa9ad6f80870b1784115def239129bdebf913b081e"], ["HG35-forgive-e3", () => "We can not \u2018force\u2019 forgiveness on ourselves, it has to come from a place of understanding otherwise it can be bypassing. However, if we remain in the anger forever, we are allowing the injury to dictate how we live our lives in the present. So how do we hold all of this? We just remember that it can all be true at once. They really did hurt us and they still have to answer for it, and our boundary with them still matters, but one day we may find that we have forgiven them.", "31582ab9a89a16868a4577a8265ef380b5510e848cfe2752a8ccabf64ccf3092"], ["HG35-quote-e", () => "A helpful understanding to come to, is that while their actions were harmful, in a sense, they could only make the moves they made, given their accumulated nature at the time (conditioning, history, pain, capacity, etc). This doesn\u2019t negate that harm was caused, holding someone accountable, allowing for consequences, working on making different moves now, etc. It simply helps us come to a place where we aren\u2019t expecting something from someone that they can\u2019t give. It doesn\u2019t make their limitations matter any less.\n\n\u201cYou don\u2019t have to forgive before you\u2019re ready. I\u2019m not going to use spirituality to silence your pain, and I also won\u2019t build our whole life around this wound forever.\u201d", "cb0282de1860800f941859289d9db11a9fa3b99b3cc51172d4563ddbcc36516b"], ["HG35-selfforgive-e", () => "For self-forgiveness, name what you did, but don't take responsibility for what wasn't yours. Let yourself feel the remorse and take in the harm, or how it went against your values, and stop short of making yourself a permanent criminal.\n\nTake responsibility, feel the remorse, then rectify if you can, and then let it go. Be specific about the action you took, and the impact it had, feel the remorse, do what you can to rectify or keep it from happening again, and then stop holding yourself hostage.", "b40c41265c9f6fe8f707c8abfc54b5368aa0a53213d8284417b0238d41aa1f5b"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "B468log" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__B468log = [];
const log = m => { window.__B468log.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__B468log)); } catch (e) {} };
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
