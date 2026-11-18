import json
import tempfile
import unittest
from pathlib import Path

from update_visitor_counter import merge_metrics, update_files


class VisitorCounterTests(unittest.TestCase):
    def test_merging_replaces_overlaps_and_preserves_history(self):
        existing = [
            {"date": "2026-10-01", "count": 10, "uniques": 2},
            {"date": "2026-11-17", "count": 3, "uniques": 1},
        ]
        views = [
            {"timestamp": "2026-11-18T00:00:00Z", "count": 2, "uniques": 1},
            {"timestamp": "2026-11-17T00:00:00Z", "count": 5, "uniques": 2},
        ]
        merged = merge_metrics(existing, views)
        self.assertEqual([entry["count"] for entry in merged], [10, 5, 2])
        self.assertEqual(merge_metrics(merged, views), merged)

    def test_corrupt_history_is_rejected(self):
        for history in ({}, [{"date": "2026-11-17", "count": -1, "uniques": 0}]):
            with self.subTest(history=history), self.assertRaises(ValueError):
                merge_metrics(history, [])

    def test_badges_update_and_missing_marker_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            partials = root / "docs" / "overrides" / "partials"
            partials.mkdir(parents=True)
            metrics = root / "metrics.json"
            metrics.write_text("[]\n", encoding="utf-8")
            content = "Keep this.\n<!-- START BADGE -->old<!-- END BADGE -->\n"
            readme = root / "README.md"
            page = partials / "visitor-counter.html"
            readme.write_text(content, encoding="utf-8")
            page.write_text("Missing badge.", encoding="utf-8")
            traffic = {"views": [
                {"timestamp": "2026-11-18T00:00:00Z", "count": 7, "uniques": 2}
            ]}
            with self.assertRaisesRegex(ValueError, "exactly one"):
                update_files(root, traffic, "2026-11-18")
            self.assertEqual(readme.read_text(encoding="utf-8"), content)
            self.assertEqual(json.loads(metrics.read_text(encoding="utf-8")), [])

            page.write_text(content, encoding="utf-8")
            lesson = root / "docs" / "lesson.md"
            lesson.write_text("# A lesson without a counter block\n", encoding="utf-8")
            update_files(root, traffic, "2026-11-18")
            for path in (readme, page):
                updated = path.read_text(encoding="utf-8")
                self.assertTrue(updated.startswith("Keep this.\n"))
                self.assertIn("Total%20views-7-limegreen", updated)
                self.assertIn("Refresh Date: 2026-11-18", updated)
                self.assertNotIn("not website visits", updated)
            self.assertEqual(json.loads(metrics.read_text(encoding="utf-8"))[0]["count"], 7)
            self.assertEqual(
                lesson.read_text(encoding="utf-8"),
                "# A lesson without a counter block\n",
            )


if __name__ == "__main__":
    unittest.main()
