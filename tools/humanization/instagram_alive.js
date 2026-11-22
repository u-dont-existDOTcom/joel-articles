// instagram_alive.js - which Instagram posts can still be embedded (lesson embeds-2026-11-21a).
//
// Substack builds an Instagram embed itself from the post's id. When the post is deleted, made private or restricted,
// Instagram's embed page never reports a size, so Substack's frame stays at its 520px start with nothing in it: a blank
// box with no link, for every reader. On 2026-11-21 three of the 18 Instagram embeds in Joel's posts were like that.
//
// Run it on any https://www.instagram.com/ page, in the desktop app's browser pane or Claude in Chrome, signed in or not:
// paste this file, then the line `post_embeds.py POST.html --instagram` printed, for example
//   await instagramAlive(["DQ_V5uZje4f", "DP464qoCoND"])
// Each answer is {id, state, status}: state "dead" is Instagram's own "the link may be broken or the post removed" page
// (class EmbedBrokenMedia), "live" a rendered post (class EmbeddedMedia), "unknown" anything else (look at it yourself).
// It asks without cookies, as a reader who isn't signed in to Instagram, since an embed only shows posts anyone can see.
async function instagramAlive(ids) {
  const one = async (id) => {
    const r = await fetch('/p/' + encodeURIComponent(id) + '/embed/captioned/', {credentials: 'omit', cache: 'no-store'});
    const page = await r.text();
    const dead = /class="[^"]*\bEmbedBrokenMedia\b/.test(page);
    const live = /class="[^"]*\bEmbeddedMedia\b/.test(page);
    return {id, state: dead ? 'dead' : live ? 'live' : 'unknown', status: r.status};
  };
  const out = [];
  for (let i = 0; i < ids.length; i += 4) out.push(...(await Promise.all(ids.slice(i, i + 4).map(one))));
  return out;
}
