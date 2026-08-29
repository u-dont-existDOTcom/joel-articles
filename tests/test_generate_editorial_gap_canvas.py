import unittest

from scripts.generate_editorial_gap_canvas import generate_canvas, validate_register


class EditorialGapCanvasTests(unittest.TestCase):
    def sample_register(self):
        return {
            "schema_version": 1,
            "article": {
                "id": "sample",
                "master_path": "articles/sample/master.md",
            },
            "sections": [
                {"id": "opening", "label": "Opening"},
                {"id": "body", "label": "Body", "subpath": "#Body"},
            ],
            "questions": [
                {
                    "id": "G001",
                    "kind": "gap-candidate",
                    "question": "What is missing?",
                    "trigger_section": "opening",
                    "answer_sections": ["body"],
                    "coverage": "partial",
                    "importance": "high",
                    "disposition": "review",
                    "gap_classes": ["promise-gap"],
                    "note": "Diagnostic only.",
                },
                {
                    "id": "C001",
                    "kind": "coverage-control",
                    "question": "What is already answered?",
                    "trigger_section": "body",
                    "answer_sections": ["body"],
                    "coverage": "answered",
                    "importance": "medium",
                    "disposition": "no-gap",
                },
            ],
            "prefix_probes": [
                {
                    "id": "P001",
                    "after_section": "opening",
                    "answer_sections": ["body"],
                }
            ],
        }

    def test_generates_file_and_question_nodes(self):
        canvas = generate_canvas(self.sample_register())
        node_ids = {node["id"] for node in canvas["nodes"]}
        self.assertIn("sec-opening", node_ids)
        self.assertIn("sec-body", node_ids)
        self.assertIn("q-G001", node_ids)
        self.assertIn("q-C001", node_ids)

    def test_question_columns_separate_candidates_and_controls(self):
        canvas = generate_canvas(self.sample_register())
        nodes = {node["id"]: node for node in canvas["nodes"]}
        self.assertEqual(nodes["q-G001"]["x"], 620)
        self.assertEqual(nodes["q-C001"]["x"], 1260)

    def test_unknown_section_fails_closed(self):
        register = self.sample_register()
        register["questions"][0]["trigger_section"] = "missing"
        with self.assertRaises(ValueError):
            validate_register(register)

    def test_duplicate_question_id_fails_closed(self):
        register = self.sample_register()
        register["questions"][1]["id"] = "G001"
        with self.assertRaises(ValueError):
            validate_register(register)

    def test_canvas_references_existing_nodes(self):
        canvas = generate_canvas(self.sample_register())
        node_ids = {node["id"] for node in canvas["nodes"]}
        for edge in canvas["edges"]:
            self.assertIn(edge["fromNode"], node_ids)
            self.assertIn(edge["toNode"], node_ids)


if __name__ == "__main__":
    unittest.main()
