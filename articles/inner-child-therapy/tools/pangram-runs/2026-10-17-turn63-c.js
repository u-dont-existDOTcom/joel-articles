const items = [["t63c_p10k", () => "A guru who demands surrender points you at themselves instead (so, more or less, they'd like to be your God). And sometimes they never have to ask. Ever met someone who seemed to get you better than you get yourself, and gave you more attention than you'd ever had? Your little one might just hand itself over, on its own.", "dcdaa9c4cfcb36506a19fc839f04446c9edf6c6753d5587e203f9eabe44c7e39"], ["t63c_p10l", () => "Some gurus really do demand surrender, and they're the opposite of the Guide: they point you at themselves (so, more or less, they'd like to be your God). And sometimes they never have to ask. Somebody seems to get your little one better than anyone ever has, or gives it the attention it's been starving for, and it hands itself right over.", "1848313a41f78e9eec256a1eab2d6e26fa3cace1e18bc3c9a6cca6bcbf945055"], ["t63c_p10o", () => "A guru who demands surrender points you at themselves instead (so, more or less, they'd like to be your God). Sometimes they never have to ask. Someone seems to get your little one like nobody ever has, or treats it like it's special, and it starts thinking, \"They know me better than I know myself.\"", "18056321ae85d3d20ace4a7c53ba936d392cd4a12d05fcd5842d2ffaf2f1d7aa"], ["t63c_p10p", () => "A guru who demands that you hand yourself over points you at themselves instead (so, more or less, they'd like to be your God). Sometimes they never have to ask. Someone seems to get your little one like nobody ever has, or treats it like it's special, and it starts thinking, \"They know me better than I know myself.\"", "b52245fbcc887a6bec7c9e5bcc40ffb960564f34cefe141346d48b8f63e1bece"]];
window.__t63c = [];
const log = m => window.__t63c.push(m);
const setter = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
const sha = async t => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))).map(b => b.toString(16).padStart(2, '0')).join('');
const button = () => [...document.querySelectorAll('button[type=submit]')].find(b => /check for ai/i.test(b.innerText));
const wait = ms => new Promise(r => setTimeout(r, ms));
async function run() {
  for (const [k, mk, want] of items) {
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
