const items0 = [["t71hh_jwp", () => "Lucia Capacchione, an art therapist, has been teaching this one for decades (it's in her book [Recovery of Your Inner Child](https://www.luciac.com/)). Sounds almost too simple, I know. Your non-dominant hand writes down whatever scared or hurt feelings are really there (nothing made up). It writes like a first grader anyway, so it's a natural fit. Then your usual hand writes back as the grown-up. If talking or picturing has only gotten you silence, give the clumsy hand a try. A protective part might grab the pen first, and then it gets that hand until it's had its say.", "8dcf58cc292de1a7a8f8319d5c1c676a5d403caa228711f8593986314e064549"], ["t71hh_oiu", () => "The night half of this is a lot like the [Examen](https://www.ignatianspirituality.com/ignatian-prayer/the-examen/), the evening review Jesuits have done for centuries, just aimed at hooks. Not bad company, honestly. In the morning you pick one small intention, like \"Today I'll notice one hook before I act on it.\" At night you look back over the day. Where did you catch the hook, and where did it run its routine anyway? What's the next small repair, or something that'd protect your little one?", "2f1c13cb130d95993a1906dc63a1afe190128540ae6313eb9976da45192280d9"], ["t71hh_secjwp", () => "## Journal With Each Hand\n\nLucia Capacchione, an art therapist, has been teaching this one for decades (it's in her book [Recovery of Your Inner Child](https://www.luciac.com/)). Sounds almost too simple, I know. Your non-dominant hand writes down whatever scared or hurt feelings are really there (nothing made up). It writes like a first grader anyway, so it's a natural fit. Then your usual hand writes back as the grown-up. If talking or picturing has only gotten you silence, give the clumsy hand a try. A protective part might grab the pen first, and then it gets that hand until it's had its say.\n\nIf thinking things through on paper leaves you more confused, a simpler memory aid is fine. It keeps track of things without you having to work out what they mean at the same time. Looking for patterns can come later, if it's useful at all. A memory aid doesn't have to explain your life. It could be a short note of what happened, with the date, or a note of what helped. A reminder or a next step works too. Or you can leave yourself a voice note.", "4c07595d3ba83e0be5b7e05eead4ebf57ac36687110b6ee5bfcecc0b4af7880f"], ["t71hh_secoiu", () => "## One Intention in the Morning, One Review at Night\n\nThe night half of this is a lot like the [Examen](https://www.ignatianspirituality.com/ignatian-prayer/the-examen/), the evening review Jesuits have done for centuries, just aimed at hooks. Not bad company, honestly. In the morning you pick one small intention, like \"Today I'll notice one hook before I act on it.\" At night you look back over the day. Where did you catch the hook, and where did it run its routine anyway? What's the next small repair, or something that'd protect your little one?\n\nAnd what good did you get today? Count the small stuff, like a warm moment, or some nerve you didn't know you had. Noticing the hook counts too, and it counts if you're only seeing it now, in the review. Same if you broke the pattern somewhere. Then repair what you can, and that's the day. Same intention tomorrow. Bed.", "ed601c2994e47459949881c59d8aafc8bcd3c0e2d7bdff79da0aeba0970dbde3"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71hh" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71hh = [];
const log = m => { window.__t71hh.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71hh)); } catch (e) {} };
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
