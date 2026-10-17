const items0 = [["t65z19_st1p6w5p1", () => "Love moves in a loop. It goes from spiritual experience to your little one, on into the grown-up relationship, from you into other people, and back again. Maybe you're not sure which door you came in through. The loop matters more than the door. Community can work in both directions. Sometimes it's the people who come first: they love you, you feel safe and like you belong, and something deeper gets room to open. Other times the opening comes first, and afterward different people and relationships start turning up (you \"manifest\" them, if you like that word). Then community helps make the opening practical and real, something your body knows and not just your head.", "c5d7a0dad84d72ff8849ac48291481b517da5f77681623afaf121d9f39317bf0"], ["t65z19_st1p6w6p1", () => "Love moves in a loop. It goes from spiritual experience to your little one, on into the grown-up relationship, from you into other people, and back again. Maybe you're not sure which door you came in through. The loop matters more than the door. Community can work in both directions. Loving people can make you feel safe enough, and like you belong enough, for a deeper opening to happen. Or the opening happens first and changes who and what you can \"manifest.\" Then the people around you help make it practical and real, and help you live it in your body instead of only thinking about it.", "c070f0f93106c7508b3eef28ffe8e9d9b2d54f4eccc64bafbe3c402a55367d49"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t65z19" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t65z19 = [];
const log = m => { window.__t65z19.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t65z19)); } catch (e) {} };
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
