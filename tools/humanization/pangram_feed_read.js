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
(() => {
  const span = document.querySelector('span[class*="text-segm"]');
  if (!span) return JSON.stringify({error: 'no text segments on this page: open the full analysis first'});
  const key = Object.keys(span).find(k => k.startsWith('__reactFiber$'));
  let f = span[key], q = null;
  for (let d = 0; f && d < 80; d++, f = f.return) {
    if (f.memoizedProps && f.memoizedProps.textQueryData) { q = f.memoizedProps.textQueryData; break; }
  }
  if (!q) return JSON.stringify({error: 'no textQueryData in the page props'});
  const rp = q.response_payload;
  const uuid = (location.pathname.match(/feed\/([0-9a-f-]{36})/) || [])[1] || null;
  return JSON.stringify({
    feed_uuid: uuid, link: uuid ? 'https://www.pangram.com/feed/' + uuid : location.href, created_at: q.created_at,
    domain: q.domain, content_type: q.content_type, prediction_short: rp.prediction_short, headline: rp.headline,
    version: rp.version, confidence_policy_id: rp.confidence_policy_id, readout_policy_id: rp.readout_policy_id || null,
    fraction_ai: rp.fraction_ai, fraction_human: rp.fraction_human, fraction_breakdown: rp.fraction_breakdown,
    document_confidence: rp.document_confidence, verdict_support: rp.verdict_support, ai_distribution: rp.ai_distribution,
    num_ai_segments: rp.num_ai_segments, num_human_segments: rp.num_human_segments, word_count: rp.word_count,
    task_id: rp.task_id,
    windows: rp.windows.map(w => ({label: w.label, confidence: w.confidence, ai_likelihood: w.ai_likelihood,
      word_count: w.word_count, start_index: w.start_index, end_index: w.end_index, is_humanized: w.is_humanized,
      calibrated_confidence: w.calibrated_confidence, uncertainty_highlighting: w.uncertainty_highlighting})),
    text: rp.text});
})()
