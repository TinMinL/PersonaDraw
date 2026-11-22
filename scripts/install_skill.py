"""Install the repository's PersonaDraw skill in a target agent workspace."""

import argparse
from pathlib import Path
import tempfile


def install(host, project):
    project = project.expanduser().resolve(strict=True)
    if not project.is_dir():
        raise ValueError(f"Expected a project directory: {project}")
    if host == "dsh":
        project = next((p for p in (project, *project.parents) if (p / ".git").exists()), project)

    source = Path(__file__).resolve().parents[1] / "plugins/persona-draw/skills/persona-draw/SKILL.md"
    body = source.read_bytes()
    base = project / (".claude" if host == "claude" else ".agents") / "skills"
    target = base / "persona-draw"
    if base.resolve() != base or target.is_symlink():
        raise ValueError(f"Inspect this linked skills path before installing manually: {target}")
    if host == "dsh":
        native = project / ".dsh/skills"
        for path in (native / "persona-draw/SKILL.md", native / "persona-draw.md", base / "persona-draw.md"):
            if path.exists() or path.is_symlink():
                raise ValueError(f"Existing DSH candidate: {path}. Compare and consolidate copies before installing.")

    def existing():
        entry = target / "SKILL.md"
        if entry.is_file() and not entry.is_symlink() and entry.read_bytes() == body:
            return f"Already installed: {entry}"
        raise ValueError(f"Existing skill differs or is incomplete. Compare with {source} before updating {target}.")

    if target.exists():
        return existing()
    base.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=base) as temp:
        # Stage below a second level so skill discovery never sees a partial copy.
        staged = Path(temp) / "persona-draw"
        staged.mkdir()
        (staged / "SKILL.md").write_bytes(body)
        try:
            staged.rename(target)
        except OSError:
            if target.is_dir() and not target.is_symlink():
                return existing()
            raise
    return f"Installed: {target / 'SKILL.md'}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host", choices=("dsh", "agy", "codex", "gemini", "claude"))
    parser.add_argument("project", type=Path, help="existing target project directory")
    args = parser.parse_args()
    try:
        print(install(args.host, args.project))
    except (ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    main()
