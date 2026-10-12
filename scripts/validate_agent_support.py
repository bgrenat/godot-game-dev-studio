#!/usr/bin/env python3
"""Validate generated multi-agent entrypoints and portable repository references."""
from pathlib import Path
import sys
import json
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / ".cursor" / "rules" / "godot-game-dev-studio.mdc",
    ROOT / ".github" / "copilot-instructions.md",
    ROOT / ".claude" / "skills" / "godot-game-dev-studio" / "SKILL.md",
]
TEXT_SUFFIXES = {".md", ".mdc", ".gd", ".gdshader", ".json", ".py", ".ps1", ".toml", ".yml", ".yaml",
                 ".tscn", ".tres", ".cfg", ".txt", ".godot"}
# Absolute user-specific paths that must never be committed.
# Placeholder names used in documentation examples are allowed.
PERSONAL_PATH = re.compile(
    r"[A-Za-z]:[\\/]Users[\\/](?!\.\.\.)(?!(?:Player|username|user|you|USER|<user>)[\\/])[^\\/\s]+"
    r"|/Users/(?!(?:Player|username|user|you|USER|<user>)/)[^/\s]+/|/home/(?!(?:user|username|<user>)/)[^/\s]+/|file://"
)
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
errors = []


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def frontmatter(path: Path) -> str | None:
    match = FRONTMATTER.match(read(path))
    return match.group(1) if match else None


for path in required:
    if not path.is_file() or not read(path).strip():
        errors.append(f"missing or empty: {path.relative_to(ROOT)}")
claude_entry = required[2]
if claude_entry.is_file():
    header = frontmatter(claude_entry) or ""
    if not re.search(r"^name:\s*\S", header, re.M) or not re.search(r"^description:\s*\S", header, re.M):
        errors.append(f"missing name/description frontmatter: {claude_entry.relative_to(ROOT)}")

this_file = Path(__file__).resolve()
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES or path.resolve() == this_file:
        continue
    if ".git" in path.parts or "__pycache__" in path.parts:
        continue
    match = PERSONAL_PATH.search(read(path))
    if match:
        errors.append(f"personal path {match.group(0)!r}: {path.relative_to(ROOT)}")

skills_root = ROOT / "skills"
skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
for path in skill_dirs:
    skill_md = path / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"skill directory missing SKILL.md: {path.relative_to(ROOT)}")
        continue
    header = frontmatter(skill_md)
    if header is None:
        errors.append(f"missing frontmatter: {skill_md.relative_to(ROOT)}")
        continue
    name = re.search(r"^name:\s*([^\r\n]+)$", header, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", header, re.MULTILINE)
    if name and name.group(1).strip().strip('"') != path.name:
        errors.append(f"frontmatter name {name.group(1).strip()!r} does not match directory: {skill_md.relative_to(ROOT)}")
    if not name or not name.group(1).strip():
        errors.append(f"missing frontmatter name: {skill_md.relative_to(ROOT)}")
    if not description or not description.group(1).strip():
        errors.append(f"missing frontmatter description: {skill_md.relative_to(ROOT)}")

index_path = ROOT / "skills_index.json"
try:
    index = json.loads(read(index_path))
    names = [item.get("name") for item in index if isinstance(item, dict)]
    indexed_names = set(names)
    for name in sorted({n for n in names if names.count(n) > 1}):
        errors.append(f"duplicate skill name in skills_index.json: {name}")
    for name in sorted(indexed_names - {None}):
        if not (skills_root / name / "SKILL.md").is_file():
            errors.append(f"indexed skill missing from filesystem: {name}")
    for path in skill_dirs:
        if path.name not in indexed_names:
            errors.append(f"skill missing from skills_index.json (run update_skills_index.py): {path.name}")
except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"invalid skills_index.json: {exc}")

# godot-master/scripts mirrors every godot-* skill script as <skill-without-godot-, _>_<file>.
# Mirrors must stay identical to their source (line endings ignored).
master_scripts = skills_root / "godot-master" / "scripts"
mirrored = 0
if master_scripts.is_dir():
    for skill in skill_dirs:
        if not skill.name.startswith("godot-") or skill.name == "godot-master":
            continue
        prefix = skill.name[len("godot-"):].replace("-", "_") + "_"
        for source in sorted((skill / "scripts").glob("*")) if (skill / "scripts").is_dir() else []:
            mirror = master_scripts / (prefix + source.name)
            if source.is_file() and mirror.is_file():
                mirrored += 1
                if source.read_bytes().replace(b"\r\n", b"\n") != mirror.read_bytes().replace(b"\r\n", b"\n"):
                    errors.append(f"godot-master mirror out of sync: {mirror.relative_to(ROOT)} != {source.relative_to(ROOT)}")

# Relative Markdown links must resolve (fenced code blocks are ignored).
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
FENCE = re.compile(r"```.*?```", re.DOTALL)
link_count = 0
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    for match in LINK.finditer(FENCE.sub("", read(md))):
        target = match.group(2).split("#", 1)[0]
        if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target):
            continue
        link_count += 1
        if not (md.parent / unquote(target)).exists():
            errors.append(f"broken link {match.group(2)!r}: {md.relative_to(ROOT)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(required)} agent entrypoints, {len(skill_dirs)} skills, {mirrored} mirrored scripts, {link_count} Markdown links, and portable references validated")
