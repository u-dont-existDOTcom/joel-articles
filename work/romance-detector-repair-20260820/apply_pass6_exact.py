#!/usr/bin/env python3
from __future__ import annotations

import apply_pass6 as base


def stable_audit(source: str, candidate: str) -> dict[str, object]:
    missing_protected = [
        name for name, anchor in base.helper.PROTECTED_ANCHORS.items() if anchor not in candidate
    ]
    missing_pass6 = [
        name for name, anchor in base.PASS6_REQUIRED.items() if anchor not in candidate
    ]
    checks: dict[str, object] = {
        "headings_identical": base.helper.headings(source) == base.helper.headings(candidate),
        "native_markers_identical": base.helper.native_markers(source) == base.helper.native_markers(candidate),
        "markdown_link_destinations_identical": base.helper.markdown_links(source) == base.helper.markdown_links(candidate),
        "protected_anchors_missing": missing_protected,
        "pass6_required_missing": missing_pass6,
    }
    checks["passed"] = (
        bool(checks["headings_identical"])
        and bool(checks["native_markers_identical"])
        and bool(checks["markdown_link_destinations_identical"])
        and not missing_protected
        and not missing_pass6
    )
    return checks


base.audit = stable_audit

if __name__ == "__main__":
    raise SystemExit(base.main())
