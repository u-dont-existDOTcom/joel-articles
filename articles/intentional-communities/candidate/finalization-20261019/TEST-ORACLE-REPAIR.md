# Exact selected-quote browser regression repair

The initial canonical browser test failed for the selection `e East Wind `, which contains a trailing space. The UI stores and displays the selection through textContent; the test compared it with rendered innerText, which can collapse the boundary whitespace. The repair changes the assertion’s read to text_content(), preserving the exact selected string rather than weakening it with strip/normalization.

No review-interface controls or storage behavior were changed. Both exact final review files passed the complete browser test after the oracle repair. The source patch is preserved in project-sources/review_interface_browser_test.py.txt and the repository regression requires the exact-whitespace comparison. Clipboard destination behavior is unrelated and remains untested.
