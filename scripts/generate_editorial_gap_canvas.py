#!/usr/bin/env python3
"""Generate an Obsidian JSON Canvas from a diagnostic editorial reader-gap register.

This tool is deliberately non-authoritative. It visualizes section nodes and
material reader-question objects; it never edits article prose or article
authority files.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


VALID_KINDS = {"gap-candidate", "coverage-control"}


def validate_register(register: dict[str, Any]) -> None:
    if register.get("schema_version") != 1:
        raise ValueError("schema_version must be 1")

    article = register.get("article") or {}
    if not article.get("id") or not article.get("master_path"):
        raise ValueError("article.id and article.master_path are required")

    sections = register.get("sections")
    questions = register.get("questions")
    if not isinstance(sections, list) or not sections:
        raise ValueError("sections must be a non-empty list")
    if not isinstance(questions, list):
        raise ValueError("questions must be a list")

    section_ids: set[str] = set()
    for section in sections:
        section_id = section.get("id")
        if not section_id:
            raise ValueError("every section needs an id")
        if section_id in section_ids:
            raise ValueError(f"duplicate section id: {section_id}")
        section_ids.add(section_id)

    question_ids: set[str] = set()
    for question in questions:
        question_id = question.get("id")
        if not question_id:
            raise ValueError("every question needs an id")
        if question_id in question_ids:
            raise ValueError(f"duplicate question id: {question_id}")
        question_ids.add(question_id)

        kind = question.get("kind")
        if kind not in VALID_KINDS:
            raise ValueError(f"{question_id}: invalid kind {kind!r}")

        trigger = question.get("trigger_section")
        if trigger not in section_ids:
            raise ValueError(f"{question_id}: unknown trigger_section {trigger!r}")

        for answer in question.get("answer_sections", []):
            if answer not in section_ids:
                raise ValueError(f"{question_id}: unknown answer section {answer!r}")

    for probe in register.get("prefix_probes", []):
        probe_id = probe.get("id", "<unnamed probe>")
        after = probe.get("after_section")
        if after not in section_ids:
            raise ValueError(f"{probe_id}: unknown after_section {after!r}")
        for answer in probe.get("answer_sections", []):
            if answer not in section_ids:
                raise ValueError(f"{probe_id}: unknown answer section {answer!r}")


def _question_text(question: dict[str, Any]) -> str:
    lines = [
        f"## {question['id']} — {question.get('coverage', 'unclassified')}",
        "",
        question.get("question", "").strip(),
        "",
        f"**Importance:** {question.get('importance', 'unclassified')}  ",
        f"**Disposition:** {question.get('disposition', 'review')}",
    ]
    if question.get("gap_classes"):
        lines.append(f"**Gap class:** {', '.join(question['gap_classes'])}")
    note = question.get("note")
    if note:
        lines.extend(["", note.strip()])
    return "\n".join(lines)


def generate_canvas(register: dict[str, Any]) -> dict[str, Any]:
    """Return deterministic JSON Canvas data for a validated register."""
    validate_register(register)

    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    section_y: dict[str, int] = {}

    master_path = register["article"]["master_path"]

    for index, section in enumerate(register["sections"]):
        y = index * 260
        section_y[section["id"]] = y
        node: dict[str, Any] = {
            "id": f"sec-{section['id']}",
            "type": "file",
            "file": master_path,
            "x": 0,
            "y": y,
            "width": 420,
            "height": 180,
        }
        if section.get("subpath"):
            node["subpath"] = section["subpath"]
        nodes.append(node)

    for left, right in zip(register["sections"], register["sections"][1:]):
        edges.append(
            {
                "id": f"edge-flow-{left['id']}-{right['id']}",
                "fromNode": f"sec-{left['id']}",
                "fromSide": "bottom",
                "toNode": f"sec-{right['id']}",
                "toSide": "top",
                "label": "article flow",
            }
        )

    trigger_counts: defaultdict[str, int] = defaultdict(int)
    for question in register["questions"]:
        trigger = question["trigger_section"]
        y = section_y[trigger] + trigger_counts[trigger] * 210
        trigger_counts[trigger] += 1
        x = 620 if question["kind"] == "gap-candidate" else 1260

        nodes.append(
            {
                "id": f"q-{question['id']}",
                "type": "text",
                "text": _question_text(question),
                "x": x,
                "y": y,
                "width": 520,
                "height": 190,
            }
        )
        edges.append(
            {
                "id": f"edge-raise-{question['id']}",
                "fromNode": f"sec-{trigger}",
                "fromSide": "right",
                "toNode": f"q-{question['id']}",
                "toSide": "left",
                "label": "raises / exposes",
            }
        )

        answer_label = (
            "covers"
            if str(question.get("coverage", "")).startswith("answered")
            else "partial coverage"
        )
        for index, answer in enumerate(question.get("answer_sections", [])):
            edges.append(
                {
                    "id": f"edge-answer-{question['id']}-{index}",
                    "fromNode": f"sec-{answer}",
                    "fromSide": "right",
                    "toNode": f"q-{question['id']}",
                    "toSide": "left",
                    "label": answer_label,
                }
            )

    return {"nodes": nodes, "edges": edges}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("register", type=Path, help="Reader-gap register JSON")
    parser.add_argument(
        "--out",
        type=Path,
        help="Output .canvas path. Defaults beside register.",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate register without writing a Canvas.",
    )
    args = parser.parse_args()

    register = json.loads(args.register.read_text(encoding="utf-8"))
    validate_register(register)

    if args.check_only:
        print("reader-gap register: PASS")
        return 0

    output = args.out or args.register.with_suffix(".canvas")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(generate_canvas(register), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
