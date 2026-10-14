const T="The two failures mirror each other. Secular groups distribute power but leave the inner life largely private or ignored. Spiritual groups attempt to address the inner life, but because it's the inner being shaped by the outer as a condition of membership, we tend to find both real-world and spiritual power concentrating around whoever defines the path.";
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
await sleep(2500);
const cred=()=>Number((document.body.innerText.match(/(\d+)\s*left/)||[])[1]);
let res={};
if(!/dashboard/.test(location.href)){res={error:'not on dashboard'};} else {
 let ta=document.querySelector('textarea');
 const before=cred();
 Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype,'value').set.call(ta,T);
 ta.dispatchEvent(new Event('input',{bubbles:true}));
 await sleep(800);
 if(ta.value!==T){res={error:'box mismatch'};} else {
  const btn=[...document.querySelectorAll('button')].filter(b=>/Check for AI/.test(b.innerText)&&!b.disabled&&b.offsetParent)[0];
  btn.click(); window.__pgBefore=before; window.__pgTail=T.split(/\s+/).slice(-6).join(' ');
  res={submitted:true,before,words:T.split(/\s+/).length};
 }}
res