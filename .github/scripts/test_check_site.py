import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class SiteCheckerTests(unittest.TestCase):
    def run_checker(self, directory, html):
        root = Path(directory)
        scripts = root / ".github" / "scripts"
        scripts.mkdir(parents=True)
        script = scripts / "check_site.py"
        shutil.copyfile(Path(__file__).with_name("check_site.py"), script)
        (root / "site" / "nested").mkdir(parents=True)
        (root / "docs").mkdir()
        (root / "site" / "index.html").write_text("<h1>Home</h1>", encoding="utf-8")
        (root / "site" / "nested" / "lesson.html").write_text(html, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_fragment_only_links_use_the_current_page(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_checker(
                directory,
                '<h1 id="lesson">Lesson</h1><a href="#lesson">Jump</a>',
            )
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_fragment_and_file_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_checker(
                directory,
                '<a href="#missing">Jump</a><a href="missing.html">File</a>',
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing anchor #missing", result.stderr)
            self.assertIn("missing target missing.html", result.stderr)
