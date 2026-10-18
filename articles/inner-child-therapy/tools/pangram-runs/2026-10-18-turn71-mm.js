const items0 = [["t71mm_jw2e", () => "And what if all that writing leaves you more confused than when you started? Then skip the meaning-making for now and just keep track; the patterns can wait, if they matter at all. A memory aid doesn't have to explain your life. It could be a dated note of what happened, or of what helped. A reminder or a next step works too, or you can skip the pen and leave yourself a voice note.", "99556515870fc13b979282b250d8d1fcaada127a9ac5b44367011781a0de6875"], ["t71mm_jw2f", () => "And what if all that writing leaves you more confused than when you started, both hands included? Then skip the meaning-making for now and just keep track. The patterns can wait, if they matter at all. A memory aid doesn't have to explain your life. It could be a dated note of what happened, or of what helped. A reminder or a next step works too. Or skip the pen and leave yourself a voice note.", "b8714e14b4f95365df2f1f18dca5f93f2a82755940033813e3ee8f4d0e0a8ca6"], ["t71mm_secjwse", () => "## Journal With Each Hand\n\nLucia Capacchione, an art therapist, wrote a whole book on this one, [The Power of Your Other Hand](https://www.luciac.com/). As titles go, it's pretty literal. Your other hand, the clumsy one, writes like a first grader anyway, so it gets the scared or hurt feelings (nothing made up). The usual hand answers, as the grown-up. Some people who get nothing but silence from their little one are surprised by what the other hand comes up with. A protective part might grab the pen first, and then it gets that hand until it's had its say.\n\nAnd what if all that writing leaves you more confused than when you started? Then skip the meaning-making for now and just keep track; the patterns can wait, if they matter at all. A memory aid doesn't have to explain your life. It could be a dated note of what happened, or of what helped. A reminder or a next step works too, or you can skip the pen and leave yourself a voice note.", "0c3cdd486d6dd4c3dece4aeedeec590f3d9dcdc05393d57e854de8c20ac7e910"], ["t71mm_secjwsf", () => "## Journal With Each Hand\n\nLucia Capacchione, an art therapist, wrote a whole book on this one, [The Power of Your Other Hand](https://www.luciac.com/). As titles go, it's pretty literal. Your other hand, the clumsy one, writes like a first grader anyway, so it gets the scared or hurt feelings (nothing made up). The usual hand answers, as the grown-up. Some people who get nothing but silence from their little one are surprised by what the other hand comes up with. A protective part might grab the pen first, and then it gets that hand until it's had its say.\n\nAnd what if all that writing leaves you more confused than when you started, both hands included? Then skip the meaning-making for now and just keep track. The patterns can wait, if they matter at all. A memory aid doesn't have to explain your life. It could be a dated note of what happened, or of what helped. A reminder or a next step works too. Or skip the pen and leave yourself a voice note.", "9f30098cfb8972a1cef9a78604d61355ca94e6a23807ed6209566c1c2ea73603"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71mm" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71mm = [];
const log = m => { window.__t71mm.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71mm)); } catch (e) {} };
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
