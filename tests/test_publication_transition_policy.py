import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / ".github" / "codex-repository.json"
SCRIPT = ROOT / "scripts" / "audit-publication-secrets.sh"


def test_profile_records_confirmed_public_visibility():
    data = json.loads(PROFILE.read_text(encoding="utf-8"))
    assert data["visibility"] == "public"
    transition = data["publication_transition"]
    assert transition["status"] == "public_readback_confirmed"
    assert transition["hosted_readback_visibility"] == "public"
    assert transition["excluded_repository"] == "u-dont-existDOTcom/AskRigor-lessons"


def test_publication_audit_uses_nonconflicting_pr_head_namespace():
    text = SCRIPT.read_text(encoding="utf-8")
    assert "+refs/pull/*/head:refs/remotes/pull-heads/*" in text
    assert "+refs/pull/*/head:refs/remotes/pull/*" not in text
    assert "--redact=100" in text
