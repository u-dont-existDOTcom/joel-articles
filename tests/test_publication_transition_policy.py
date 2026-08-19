import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / ".github" / "codex-repository.json"
SCRIPT = ROOT / "scripts" / "audit-publication-secrets.sh"
WORKFLOW = ROOT / ".github" / "workflows" / "publication-secret-audit.yml"


def test_profile_records_confirmed_public_visibility():
    data = json.loads(PROFILE.read_text(encoding="utf-8"))
    assert data["visibility"] == "public"
    transition = data["publication_transition"]
    assert transition["status"] == "public_readback_confirmed"
    assert transition["hosted_readback_visibility"] == "public"
    assert transition["excluded_repository"] == "u-dont-existDOTcom/AskRigor-lessons"


def test_publication_audit_uses_nonconflicting_pr_head_namespace_and_skips_self():
    text = SCRIPT.read_text(encoding="utf-8")
    assert "+refs/pull/*/head:refs/remotes/pull-heads/*" in text
    assert "+refs/pull/*/head:refs/remotes/pull/*" not in text
    assert 'current_run_id="${GITHUB_RUN_ID:-}"' in text
    assert '"$run_id" == "$current_run_id"' in text
    assert "--redact=100" in text


def test_completed_publication_audit_is_archival_manual_only():
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "workflow_dispatch:" in text
    assert "pull_request:" not in text
    assert "push:" not in text
    assert "schedule:" not in text
