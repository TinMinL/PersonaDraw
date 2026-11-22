import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/install_skill.py"
SOURCE = ROOT / "plugins/persona-draw/skills/persona-draw/SKILL.md"


class ProjectInstallTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="persona draw ")
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name)
        self.entry = self.project / ".agents/skills/persona-draw/SKILL.md"

    def install(self, host, project=None):
        return subprocess.run([sys.executable, str(SCRIPT), host, str(project or self.project)],
                              capture_output=True, text=True)

    def test_project_layouts_and_repeat_install(self):
        for host in ("dsh", "agy", "gemini", "codex", "claude"):
            with self.subTest(host=host):
                result = self.install(host)
                self.assertEqual(result.returncode, 0, result.stderr)
                target = self.project / ".claude/skills/persona-draw/SKILL.md" if host == "claude" else self.entry
                self.assertEqual(target.read_bytes(), SOURCE.read_bytes())
                self.assertIn("Already installed", self.install(host).stdout)

    def test_dsh_uses_git_root(self):
        (self.project / ".git").mkdir()
        sub = self.project / "sub"
        sub.mkdir()
        self.assertEqual(self.install("dsh", sub).returncode, 0)
        self.assertTrue(self.entry.exists())
        self.assertFalse((sub / ".agents").exists())

    def test_preserves_customized_skill_and_rules(self):
        self.entry.parent.mkdir(parents=True)
        self.entry.write_bytes(b"custom")
        rules = self.project / "AGENTS.md"
        rules.write_bytes(b"existing instructions")
        self.assertNotEqual(self.install("agy").returncode, 0)
        self.assertEqual(self.entry.read_bytes(), b"custom")
        self.assertEqual(rules.read_bytes(), b"existing instructions")

    def test_dsh_shadow_candidates(self):
        for relative in (".dsh/skills/persona-draw.md", ".dsh/skills/persona-draw/SKILL.md", ".agents/skills/persona-draw.md"):
            with self.subTest(path=relative):
                old = self.project / relative
                old.parent.mkdir(parents=True, exist_ok=True)
                old.write_bytes(b"older skill")
                self.assertNotEqual(self.install("dsh").returncode, 0)
                self.assertFalse(self.entry.exists())
                self.assertEqual(old.read_bytes(), b"older skill")
                old.unlink()

    def test_simultaneous_installs(self):
        with ThreadPoolExecutor(4) as pool:
            for result in pool.map(self.install, ("dsh", "agy", "codex", "gemini")):
                self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.entry.read_bytes(), SOURCE.read_bytes())


if __name__ == "__main__":
    unittest.main()
