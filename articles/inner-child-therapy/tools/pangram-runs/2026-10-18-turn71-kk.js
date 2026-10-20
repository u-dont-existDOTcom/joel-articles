const items0 = [["t71kk_jwr", () => "Lucia Capacchione, an art therapist, wrote a whole book on this one, [The Power of Your Other Hand](https://www.luciac.com/). As titles go, it's pretty literal. Your other hand, the clumsy one, writes like a first grader anyway, so it gets the scared or hurt feelings (nothing made up). Your usual hand gets the grown-up's part and writes back. If talking or picturing has only gotten you silence, see what the other hand does with a pen. And if a protective part grabs it first? Then it gets that hand until it's had its say.", "03ba4e166ba002a16894aadff9a362985b539793981adbe143610bef031e438a"], ["t71kk_jws", () => "Lucia Capacchione, an art therapist, wrote a whole book on this one, [The Power of Your Other Hand](https://www.luciac.com/). As titles go, it's pretty literal. Your other hand, the clumsy one, writes like a first grader anyway, so it gets the scared or hurt feelings (nothing made up). The usual hand answers, as the grown-up. Some people who get nothing but silence from their little one are surprised by what the other hand comes up with. A protective part might grab the pen first, and then it gets that hand until it's had its say.", "02ccd0b44d374659f7585d1fb7d36f7d801dfe6fe857a48b64b8349d58c13e7b"], ["t71kk_secjwr", () => "## Journal With Each Hand\n\nLucia Capacchione, an art therapist, wrote a whole book on this one, [The Power of Your Other Hand](https://www.luciac.com/). As titles go, it's pretty literal. Your other hand, the clumsy one, writes like a first grader anyway, so it gets the scared or hurt feelings (nothing made up). Your usual hand gets the grown-up's part and writes back. If talking or picturing has only gotten you silence, see what the other hand does with a pen. And if a protective part grabs it first? Then it gets that hand until it's had its say.\n\nIf thinking things through on paper leaves you more confused, a simpler memory aid is fine. It keeps track of things without you having to work out what they mean at the same time. Looking for patterns can come later, if it's useful at all. A memory aid doesn't have to explain your life. It could be a short note of what happened, with the date, or a note of what helped. A reminder or a next step works too. Or you can leave yourself a voice note.", "66adecaf52c029e21cad49461acb6ef44c21c406f25873e4ee58b7984911f959"], ["t71kk_secjws", () => "## Journal With Each Hand\n\nLucia Capacchione, an art therapist, wrote a whole book on this one, [The Power of Your Other Hand](https://www.luciac.com/). As titles go, it's pretty literal. Your other hand, the clumsy one, writes like a first grader anyway, so it gets the scared or hurt feelings (nothing made up). The usual hand answers, as the grown-up. Some people who get nothing but silence from their little one are surprised by what the other hand comes up with. A protective part might grab the pen first, and then it gets that hand until it's had its say.\n\nIf thinking things through on paper leaves you more confused, a simpler memory aid is fine. It keeps track of things without you having to work out what they mean at the same time. Looking for patterns can come later, if it's useful at all. A memory aid doesn't have to explain your life. It could be a short note of what happened, with the date, or a note of what helped. A reminder or a next step works too. Or you can leave yourself a voice note.", "40d3e54ecef28049be55238c58f4e177e6fd5255184cf98ce469294a14574a58"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71kk" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71kk = [];
const log = m => { window.__t71kk.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71kk)); } catch (e) {} };
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
