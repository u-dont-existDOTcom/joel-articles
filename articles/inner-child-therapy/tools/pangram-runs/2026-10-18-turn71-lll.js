const items0 = [["t71lll_wlu1", () => "The love in the title is the universal kind. Whether you'd say it comes from God or the universe itself or whatever, it was there before you could earn anything. Love from a person is more conditional than that, even a good person's, so somebody's love running out on you was never the measure of what you're worth.", "e5fe9afc583f0b67030748f8be133ed99bc93ce23e85176714988598140c56c1"], ["t71lll_wlu2", () => "Even if the love you got from people always seemed to come with strings? The love in the title is the universal kind, whether you'd say it comes from God or the universe itself or whatever, and it was there before you could earn anything. Love from a person is more conditional than that. Trust is slower still, and it can grow out of what somebody keeps doing, you included.", "f68f1eceba9a08ccd65342ebebe48faf6e1b1492e9d26975872ec10036633512"], ["t71lll_h1wl1", () => "# You Are Worthy of Love. Always.\n\nThe love in the title is the universal kind. Whether you'd say it comes from God or the universe itself or whatever, it was there before you could earn anything. Love from a person is more conditional than that, even a good person's, so somebody's love running out on you was never the measure of what you're worth.\n\nBe patient with yourself, and gentle, including with the part of you that thinks you should be over it by now. You are more than your pain and your past. That's easy to lose sight of when you've spent so long looking at them. And you aren't alone. There's help, and lots of other people are out there learning to look after their own little ones.", "32cef355dcd2050fc6633f5cd0ae4409330313381b03fbb2b67d67ecfcc3f76c"], ["t71lll_h1wl2", () => "# You Are Worthy of Love. Always.\n\nEven if the love you got from people always seemed to come with strings? The love in the title is the universal kind, whether you'd say it comes from God or the universe itself or whatever, and it was there before you could earn anything. Love from a person is more conditional than that. Trust is slower still, and it can grow out of what somebody keeps doing, you included.\n\nBe patient with yourself, and gentle, including with the part of you that thinks you should be over it by now. You are more than your pain and your past. That's easy to lose sight of when you've spent so long looking at them. And you aren't alone. There's help, and lots of other people are out there learning to look after their own little ones.", "4cba89e879541e4f35f938234194697a1b4ec392451f96dc814c0f482e6e1289"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t71lll" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t71lll = [];
const log = m => { window.__t71lll.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t71lll)); } catch (e) {} };
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
