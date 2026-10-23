// pangram_feed_read.js - read every window of a Pangram check of a Substack post, from its result page (2026-10-20).
//
// A check of a Substack post made by Pangram's extension (the label next to the author's name on a post or a secret draft
// link, then "View Full Analysis") opens https://www.pangram.com/feed/<uuid>. That page isn't in the History list and its
// API wants a token the page holds, but the page's own React props carry the whole result: textQueryData.response_payload,
// with the checked text and every window (label, confidence, AI likelihood, word count, start and end index). Paste this
// into the page (the built-in browser's javascript tool) and save what it returns as the lane's RESULT-*.json.
//
// Limits seen on 2026-10-20 (the hypnosis guide): the check reads at most the first 99,999 characters of the post's text
// (headings and buttons left out), so a longer post is checked in parts; set the draft's preview to "Paid subscriber view"
// first, or a paywall cuts the text.
//
// Two modes. By default it returns everything, the checked text included (about 25,000 tokens for half of a long guide).
// With window.__feedMode = 'compact' set first, it returns the result's fields, the SHA-256 of the checked text and of the
// compact windows line, and the windows' sums, and leaves the line itself in window.__compact (one entry a window,
// "label,confidence,start,end,words,ai_likelihood,is_humanized,calibrated_confidence,uncertainty", label H or A and
// confidence H, M or L, separated by ";"), to be read out in pieces and saved as the lane's WINDOWS.txt; the text is then
// rebuilt from the pasted payload (tools/humanization/substack_check_text.py result), which checks it against that SHA-256.
//
// 2026-10-23 (the hypnosis guide's recheck A3 and Nibbāna's third recheck): the page no longer had any
// span[class*="text-segm"] element, the one this script started its search from, so it found nothing. It now looks for
// the props from that span when there is one, and otherwise from every element of the page's main part (then of the
// whole body), walking up each element's React fibers until one holds textQueryData.
(async () => {
  const fiberOf = el => { const k = Object.keys(el).find(k => k.startsWith('__reactFiber$')); return k ? el[k] : null; };
  const propsFrom = el => {
    let f = fiberOf(el);
    for (let d = 0; f && d < 80; d++, f = f.return) {
      if (f.memoizedProps && f.memoizedProps.textQueryData) return f.memoizedProps.textQueryData;
    }
    return null;
  };
  let q = null;
  const span = document.querySelector('span[class*="text-segm"]');
  if (span) q = propsFrom(span);
  for (const sel of ['main *', 'body *']) {
    if (q) break;
    for (const el of document.querySelectorAll(sel)) { q = propsFrom(el); if (q) break; }
  }
  if (!q) return JSON.stringify({error: 'no textQueryData in the page props: open the full analysis first'});
  const rp = q.response_payload;
  const uuid = (location.pathname.match(/feed\/([0-9a-f-]{36})/) || [])[1] || null;
  const meta = {
    feed_uuid: uuid, link: uuid ? 'https://www.pangram.com/feed/' + uuid : location.href, created_at: q.created_at,
    domain: q.domain, content_type: q.content_type, prediction_short: rp.prediction_short, headline: rp.headline,
    version: rp.version, confidence_policy_id: rp.confidence_policy_id, readout_policy_id: rp.readout_policy_id || null,
    fraction_ai: rp.fraction_ai, fraction_human: rp.fraction_human, fraction_breakdown: rp.fraction_breakdown,
    document_confidence: rp.document_confidence, verdict_support: rp.verdict_support, ai_distribution: rp.ai_distribution,
    num_ai_segments: rp.num_ai_segments, num_human_segments: rp.num_human_segments, word_count: rp.word_count,
    task_id: rp.task_id};
  const windows = rp.windows.map(w => ({label: w.label, confidence: w.confidence, ai_likelihood: w.ai_likelihood,
    word_count: w.word_count, start_index: w.start_index, end_index: w.end_index, is_humanized: w.is_humanized,
    calibrated_confidence: w.calibrated_confidence, uncertainty_highlighting: w.uncertainty_highlighting}));
  if (window.__feedMode !== 'compact') return JSON.stringify(Object.assign(meta, {windows, text: rp.text}));
  const hex = async s => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s))))
    .map(b => b.toString(16).padStart(2, '0')).join('');
  const labels = new Set(windows.map(w => w.label));
  window.__compact = windows.map(w => [String(w.label).startsWith('AI') ? 'A' : 'H', String(w.confidence)[0], w.start_index,
    w.end_index, w.word_count, w.ai_likelihood, w.is_humanized ? 1 : 0, w.calibrated_confidence,
    w.uncertainty_highlighting ? 1 : 0].join(',')).join(';');
  return JSON.stringify(Object.assign(meta, {
    text_sha256: await hex(rp.text), text_chars_js: rp.text.length, compact_sha256: await hex(window.__compact),
    compact_chars: window.__compact.length, windows_word_sum: windows.reduce((s, w) => s + w.word_count, 0),
    windows_ai: windows.filter(w => String(w.label).startsWith('AI')).length,
    windows_human: windows.filter(w => !String(w.label).startsWith('AI')).length,
    labels: Array.from(labels), note: labels.size > 2 ? 'more than two labels: the compact line writes every AI label as A' : undefined}));
})()
