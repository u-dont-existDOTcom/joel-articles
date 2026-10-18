const items0 = [["t71iii_tf89b", () => "Once you're the grown-up, your little one stays in the picture, and they bring the stuff adults tend to lose. Silliness and irreverence, rawness, creativity, that kind of thing, and maybe a connection to the Great Mystery from before any path gave it a name. You draw on that, and give back, more communion than command. My post [Treasuring the Inner Child's Gift](https://ibogaqueen.substack.com/p/treasuring-the-inner-childs-gift) is one example (its subtitle: \"Reparenting is often more Play than Work!\").", "a9fa719fa65b61067c0bb0c8c26259a4d0f154c6853cb78853727f5f47f4e7b3"], ["t71iii_tf89c", () => "Being the grown-up doesn't mean your little one has to leave the room. They carry a lot of what adults tend to lose, like the silliness and the irreverence, the rawness, the creativity, all that, and maybe a connection to the Great Mystery from before any path gave it a name. That's the spark of life they bring, and you get to draw on it and give back, so it's more communion than command. For one example of the spark, there's my post [Treasuring the Inner Child's Gift](https://ibogaqueen.substack.com/p/treasuring-the-inner-childs-gift).", "dac5661aee94538156fab1c113b7365f469fa5d7b3cc8ad0b13e92ee7f42ab2f"], ["t71iii_tf11b", () => "Intuition is great at catching a pattern before you can explain it. Checking is a different job: does it contradict itself, how has it done before, does the conclusion actually follow? And the part of you that does the checking can get tired of not knowing, and be pretty relieved to hand the job off, to a hunch or to somebody else. I wouldn't let either one take over. A strong intuitive click is real information, and it still has to check out.", "6ec24b6c5685549c6a2147487715777c1a8e394964fd3ca2c9fe8d0ac3faa83b"], ["t71iii_tf11c", () => "A hunch can be onto something before you can say why, since it can pick up on a pattern before your head has the words for it. Then let your head check it, for holes in the story and for how hunches like it have done before. Does the conclusion follow from it? Watch for getting tired of not knowing, too, because it can be a relief to hand the whole question over to a hunch, or to somebody else. I wouldn't let either one run the show alone. A really strong click is still just something to weigh.", "020e980cebd98e36aeb7919ebc1e3a2fa379393bb2628ec4ce555047eff3b1c3"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71iii" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71iii = [];
const log = m => { window.__t71iii.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71iii)); } catch (e) {} };
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
