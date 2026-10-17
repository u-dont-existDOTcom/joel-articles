const items0 = [["t69g_sp5p1x1", () => "My ex, Xandria, taught me to append \u201cAnd so that\u2019s the way it happened!\u201d to a difficult memory. Say it the way a grandpa would finish a story on the porch. (\"Once upon a time\u2026\" helps if the start is where you get stuck.) Somehow it moves the whole thing out of the courtroom, where the case was still being argued, and into your life story. Pick a memory you can handle for the first few tries.", "ce50ed59b612585da2027da113474736ededd1d86ce373269e04dcc5ace71ec6"], ["t69g_sp5p1x2", () => "My ex, Xandria, taught me to append \u201cAnd so that\u2019s the way it happened!\u201d to a difficult memory. (\"Once upon a time\u2026\" helps too, if the start is where you get stuck.) Somehow it moves the whole thing out of the courtroom, where the case was still being argued, and into your life story, like something a grandpa tells on the porch. Pick a memory you can handle for the first few tries.", "eb5367c064c89a220ca1a3068bea3526bd8eb7f5b8e23eaefee78195380755c4"], ["t69g_sp5p2x1", () => "You might wonder if that makes it fiction. It doesn't, and it doesn't prove every detail is right, either. And if someone hurt you, they're not off the hook just because the trial's over (same goes for you, if you were the one who did it): any repair that's owed is still owed. If the line helps, let it stay one line, no sequel.", "52e11f8bc6a736183a3f78c614b896223916198c03bb5c20b3213451d9e11864"], ["t69g_secsp5x1", () => "## \u201cAnd So That\u2019s the Way It Happened!\u201d\n\nMy ex, Xandria, taught me to append \u201cAnd so that\u2019s the way it happened!\u201d to a difficult memory. Say it the way a grandpa would finish a story on the porch. (\"Once upon a time\u2026\" helps if the start is where you get stuck.) Somehow it moves the whole thing out of the courtroom, where the case was still being argued, and into your life story. Pick a memory you can handle for the first few tries.\n\nYou might wonder if that makes it fiction. It doesn't, and it doesn't prove every detail is right, either. And if someone hurt you, they're not off the hook just because the trial's over (same goes for you, if you were the one who did it): any repair that's owed is still owed. If the line helps, let it stay one line, no sequel.\n\nKeep an ear on the narrator, though. If they start to sneer, stop. Stop too if you feel more ashamed, or kind of unreal, because telling it colder won't help with that. When it does help, you can ask what the younger you in that story needs from you now, and maybe give them a bit of it.", "dfbe0bf30ae5db618ef8b2d8cc3fcb22b051427f8692fa99b255d8d08190c867"], ["t69g_secsp5x2", () => "## \u201cAnd So That\u2019s the Way It Happened!\u201d\n\nMy ex, Xandria, taught me to append \u201cAnd so that\u2019s the way it happened!\u201d to a difficult memory. (\"Once upon a time\u2026\" helps too, if the start is where you get stuck.) Somehow it moves the whole thing out of the courtroom, where the case was still being argued, and into your life story, like something a grandpa tells on the porch. Pick a memory you can handle for the first few tries.\n\nYou might wonder if that makes it fiction. It doesn't, and it doesn't prove every detail is right, either. And if someone hurt you, they're not off the hook just because the trial's over (same goes for you, if you were the one who did it): any repair that's owed is still owed. If the line helps, let it stay one line, no sequel.\n\nKeep an ear on the narrator, though. If they start to sneer, stop. Stop too if you feel more ashamed, or kind of unreal, because telling it colder won't help with that. When it does help, you can ask what the younger you in that story needs from you now, and maybe give them a bit of it.", "f003a71c2800b79197a0ed4dd029fb67034255119ca652351d6dd351fb9f61a2"]];
const rev = !!window.__reverse;
const items = rev ? items0.slice().reverse() : items0;
const order0 = items0.map(x => x[0]);
const lane = k => "t69g" + '_' + k;
try { localStorage.removeItem(lane(rev ? 'rev' : 'fwd')); } catch (e) {}
window.__t69g = [];
const log = m => { window.__t69g.push(m); try { localStorage.setItem(lane(rev ? 'rev' : 'fwd'), JSON.stringify(window.__t69g)); } catch (e) {} };
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
