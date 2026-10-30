# The marking page's Previous button (2026-10-30)

Joel, 2026-10-30 14:35 UTC, after marking every card of Hypnosis Guide Cards in order: "your "pevious" button brouught me
to the bottom of the page btw so that needs fixing".

**The cause.** In `tools/humanization/suggestion_review_template.html`, Previous went to the last *undecided* card above
the bar, and when there was none it wrapped round to the last undecided card on the page. Going through the cards in
order, every card above is decided, so Previous always jumped to the bottom.

**The fix** (suggestion_review.py 1.4): Previous goes to the card before the one you're on, decided or not. Inside a long
card it goes back to that card's start first. At the first card it stays and says "this is the first card". Next
undecided is unchanged. The test is `tests/test_suggestion_review.py`
(`test_previous_goes_to_the_card_before_and_never_wraps_to_the_bottom`).

**The browser check** (`previous_button_check.js`, run with Node and Playwright on a page built from REVIEW-483.json and
the guide as it was): Next to T1, approve it, Next to J5, approve it, then Previous, Previous again; then 300px into the
audit card, Previous twice.

| step | the old button | the fixed button |
|---|---|---|
| approve J5, Previous | the bottom of the page (scrollY 95514) | T1 |
| Previous again | R-755 | T1, "this is the first card" |
| inside the audit card, Previous | the audit card's start | the audit card's start |
| Previous again | the audit card again | T13, the card before it |

(Clicks are sent with the button's own `click()`: Playwright's own click scrolled the page before clicking, which moved
the card under the bar and hid the case being tested.)
