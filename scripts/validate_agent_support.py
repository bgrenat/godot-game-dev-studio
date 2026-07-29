#!/usr/bin/env python3
"""Validate generated multi-agent entrypoints and portable repository references."""
from pathlib import Path
import sys
import json
import re

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / ".cursor" / "rules" / "godot-game-dev-studio.mdc",
    ROOT / ".github" / "copilot-instructions.md",
    ROOT / ".claude" / "skills" / "godot-game-dev-studio" / "SKILL.md",
]
bad_tokens = ("C:\\Users\\x-v-i", "/Users/x-v-i", "H:\\Agrici", "file://")
errors = []
for path in required:
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"missing or empty: {path.relative_to(ROOT)}")
text_files = [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts and "__pycache__" not in path.parts]
for path in text_files:
    if path == Path(__file__).resolve():
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for token in bad_tokens:
        if token in text:
            errors.append(f"personal path token {token!r}: {path.relative_to(ROOT)}")

skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
skill_dirs = [path for path in (ROOT / "skills").iterdir() if path.is_dir()]
for path in skill_dirs:
    if not (path / "SKILL.md").is_file():
        errors.append(f"skill directory missing SKILL.md: {path.relative_to(ROOT)}")
for path in skill_files:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        errors.append(f"missing frontmatter: {path.relative_to(ROOT)}")
        continue
    header = text[4:text.find("\n---\n", 4)]
    name = re.search(r"^name:\s*([^\n]+)$", header, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", header, re.MULTILINE)
    if not name or not name.group(1).strip():
        errors.append(f"missing frontmatter name: {path.relative_to(ROOT)}")
    if not description or not description.group(1).strip():
        errors.append(f"missing frontmatter description: {path.relative_to(ROOT)}")

index_path = ROOT / "skills_index.json"
try:
    index = json.loads(index_path.read_text(encoding="utf-8"))
    indexed_names = {item.get("name") for item in index if isinstance(item, dict)}
    for name in indexed_names:
        if not (ROOT / "skills" / name / "SKILL.md").is_file():
            errors.append(f"indexed skill missing from filesystem: {name}")
except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"invalid skills_index.json: {exc}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(required)} agent entrypoints, {len(skill_files)} skills, and portable references validated")
