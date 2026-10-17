const items = [["t62g_p9k", () => "With that under you, belonging with people can get a lot less desperate. Not all at once, but the Guide keeps watching for the moment your little one starts thinking, \"If they stop liking me, I won't belong anywhere,\" and keeps reminding it that a group's approval isn't the deepest belonging there is. By the way, this job doesn't have to be called the Guide. The Wise One works, or your Inner Teacher, and \"Guru\" does for some people, though for cult survivors it can be a trigger word, which is understandable.", "f9548be61f54a9db3f3657d423b7a9a4e2016f28b659d503f8f46abe95e69fd0"], ["t62g_p9l", () => "With that under you, belonging with people can get a lot less desperate. Not all at once, but the Guide keeps watching for the moment your little one starts thinking, \"If they stop liking me, I won't belong anywhere,\" and keeps reminding it that a group's approval isn't the deepest belonging there is. (If \"Guide\" doesn't sit right, any name for this job works, the Wise One or your Inner Teacher, say. \"Guru\" carries real spiritual weight for some readers, but for cult survivors it can be a trigger word.)", "99a0fbeb47299239ee9a6d3882a2205c0a1306cd050d8fa64c6295abc0a820ca"], ["t62g_p9m", () => "With that under you, belonging with people can get a lot less desperate. Not all at once, but the Guide keeps watching for the moment your little one starts thinking, \"If they stop liking me, I won't belong anywhere,\" and keeps reminding it that a group's approval isn't the deepest belonging there is.", "f99a62f8504d33cc527f395ac04cb72038ea1bd1f13d8cf9f16b07173c93edea"], ["t62g_p8r", () => "The Guide (or the Wise One, or your Inner Teacher, whatever you'd call this job; \"Guru\" too, though for cult survivors that word can be a trigger) also points beyond itself, toward a belonging deeper than any group. That might be nature, or existence itself. It might be whatever your tradition sees as ultimate (that part is optional, and maybe your life already gives you enough love and meaning without it). Love can come from any of these places, and you also belong there, which is a little different. Maybe you've felt that outside somewhere, like you didn't need anybody's okay to be there. The way in is time in nature and contemplative practice, like meditation.", "6e93780871bd1f1233ae3e3cc303fccedca9a2ed58c184f4822aa60400197f69"]];
window.__t62g = [];
const log = m => window.__t62g.push(m);
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
