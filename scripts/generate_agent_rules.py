#!/usr/bin/env python3
"""Generate small, portable agent instruction entrypoints from the skills library."""
from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "skills" / "godot-master" / "SKILL.md"


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip('"') if match else "Godot 4 development guidance"


def render(target: str) -> str:
    master = MASTER.read_text(encoding="utf-8")
    description = frontmatter_value(master, "description")
    common = (
        "# Godot Game Dev Studio\n\n"
        "This repository provides portable Godot 4.7+ agent skills.\n\n"
        f"Primary orchestrator: `skills/godot-master/SKILL.md`\n\n"
        f"Description: {description}\n\n"
        "Use the smallest relevant skill first. Do not load the entire skills directory. "
        "Inspect the target Godot project before editing, use Godot 4 APIs, and validate "
        "with the Godot CLI when available.\n\n"
        "For focused guidance, consult the matching `skills/<skill-name>/SKILL.md`.\n"
    )
    if target == "cursor":
        return "---\ndescription: Godot 4.7+ game-development guidance\nglobs: **/*.gd,**/*.tscn,**/*.tres,project.godot\nalwaysApply: false\n---\n\n" + common
    if target == "copilot":
        return common + "\nWhen a request is specific, identify and read the matching skill before proposing code.\n"
    if target == "claude":
        return common + "\nClaude Code should read this file and then the relevant skill before implementing changes.\n"
    raise ValueError(target)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("cursor", "copilot", "claude", "all"), default="all")
    args = parser.parse_args()
    targets = ("cursor", "copilot", "claude") if args.target == "all" else (args.target,)
    paths = {
        "cursor": ROOT / ".cursor" / "rules" / "godot-game-dev-studio.mdc",
        "copilot": ROOT / ".github" / "copilot-instructions.md",
        "claude": ROOT / ".claude" / "skills" / "godot-game-dev-studio" / "SKILL.md",
    }
    for target in targets:
        path = paths[target]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(target), encoding="utf-8", newline="\n")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
