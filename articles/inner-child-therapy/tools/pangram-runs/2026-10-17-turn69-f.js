const items0 = [["t69f_st1k", () => "If you keep telling yourself \"I'm not dependent,\" your mind still lands on \"dependent,\" since whatever you put into words is where your attention goes. So unless the painful thing itself needs naming, talk about what you'd like more of, like being able to ask for help, or a relationship you're growing. Something like \"Let's find you more ways to feel looked after\" gives your mind somewhere to go. With your little one, and in hypnosis especially, make it something they can picture (a warm kitchen, a door that locks, whatever they really need).", "6ff7a1e4bdd2f9b5903277005f3777488f58b9178695d4fece6b8da396058bc3"], ["t69f_st2q", () => "Partway through all that steering, you might think, \"But it really was dangerous,\" and if it was, it should be called dangerous. Nobody's asking you to be positive about a loss either, that gets called grief. If your little one says \"he hurt me,\" that's harm, and it gets called harm. Same for anger, a no, who's responsible, what's possible in practice, all that. After that, most of the talking can go to what can be protected or fixed from here, or practiced, or chosen, or grown, whatever's in reach.", "186ba053e6f96d1e934af95ffe54b4c77b6b8829d7fb3910645a3fc14f32e81c"], ["t69f_st5k", () => "The peer isn't there to become your permanent parent. They show you how something's done and you try it with them there. After that it goes back to you, which is about as healthy as borrowed adulthood gets. It doesn't replace therapy either. Peers and community are a different kind of help, and a serious healing path can include both, in whatever mix works for you.", "545c2e54448278b592eea083b145b1ff4e1ff9a03be973bbd7965cdce17ac8a4"], ["t69f_st5l", () => "Will they end up being your parent forever? Hopefully not. They show you how something's done and let you try it with them, and after that it's yours, which is about as healthy as borrowed adulthood gets. None of this replaces therapy, it's just a different kind of help, so a serious healing path can include both, in whatever mix works for you.", "7ccab663debcd1e9fa238dcfbc2c31ea46cb8af9cd91ba93c37a3a3c66428c02"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t69f" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t69f = [];
const log = m => { window.__t69f.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t69f)); } catch (e) {} };
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
