from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "content-integrity.yml"


def _on_block(text: str) -> str:
    lines = text.splitlines()
    start = lines.index("on:")
    block = []
    for line in lines[start + 1 :]:
        if line and not line.startswith((" ", "\t")):
            break
        block.append(line)
    return "\n".join(block)


def test_content_integrity_is_pr_only_unless_manually_dispatched():
    text = WORKFLOW.read_text(encoding="utf-8")
    triggers = _on_block(text)
    assert "pull_request:" in triggers
    assert "workflow_dispatch:" in triggers
    assert "push:" not in triggers
    assert "schedule:" not in triggers
    assert "cancel-in-progress: true" in text
