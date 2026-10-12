#!/usr/bin/env python3
"""Compile every GDScript file of the library with a real Godot binary.

Usage: python scripts/check_gdscript.py --godot /path/to/godot [--update-baseline]

Skill scripts are copied into a throw-away project (godot-master/scripts mirrors are
skipped: validate_agent_support.py guarantees they match their sources). The
worldmap_builder addon is installed under res://addons/ as in a real project.
Scripts listed in scripts/gdscript_known_failures.txt depend on context that the
library cannot provide (user autoloads, third-party addons, game assets); any other
failure, or a listed script that now compiles, makes the check fail.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "scripts" / "gdscript_known_failures.txt"
WORLDMAP = ROOT / "assets" / "godot-worldmap-builder"
CHECKER = """extends SceneTree
func _init() -> void:
\tvar files: PackedStringArray = []
\t_walk("res://", files)
\tfor f in files:
\t\tvar s: Script = ResourceLoader.load(f, "", ResourceLoader.CACHE_MODE_IGNORE)
\t\tif s == null or not s.can_instantiate():
\t\t\tprint("BAD ", f)
\tprint("CHECKED ", files.size())
\tquit()
func _walk(dir: String, out: PackedStringArray) -> void:
\tfor d in DirAccess.get_directories_at(dir):
\t\tif not d.begins_with("."):
\t\t\t_walk(dir.path_join(d), out)
\tfor f in DirAccess.get_files_at(dir):
\t\tif f.ends_with(".gd") and dir != "res://":
\t\t\tout.append(dir.path_join(f))
"""


def build_project(dest: Path) -> dict[str, str]:
    """Copy scripts into dest and return {res:// path: repository path}."""
    mapping: dict[str, str] = {}
    (dest / "project.godot").write_text('config_version=5\n[application]\nconfig/name="library-check"\n', encoding="utf-8")
    (dest / "check.gd").write_text(CHECKER, encoding="utf-8")
    for source in sorted((ROOT / "skills").rglob("*.gd")):
        rel = source.relative_to(ROOT)
        if rel.parts[1] == "godot-master" and rel.parts[2] == "scripts":
            continue
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        mapping["res://" + rel.as_posix()] = rel.as_posix()
    for sub in ("addons", "example"):
        for source in sorted((WORLDMAP / sub).rglob("*")):
            if source.is_file():
                target = dest / source.relative_to(WORLDMAP)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
                if source.suffix == ".gd":
                    mapping["res://" + source.relative_to(WORLDMAP).as_posix()] = source.relative_to(ROOT).as_posix()
    return mapping


def run(godot: str) -> tuple[set[str], int]:
    with tempfile.TemporaryDirectory(prefix="gdcheck-") as tmp:
        project = Path(tmp)
        mapping = build_project(project)
        env = dict(os.environ)
        # First pass imports resources and builds the global class cache.
        subprocess.run([godot, "--headless", "--editor", "--quit"], cwd=project, env=env,
                       capture_output=True, timeout=1800, check=False)
        result = subprocess.run([godot, "--headless", "-s", "res://check.gd"], cwd=project, env=env,
                                capture_output=True, text=True, timeout=1800, check=False)
        output = result.stdout + result.stderr
        if "CHECKED " not in output:
            sys.exit("Godot did not run the checker:\n" + output[-4000:])
        bad = {mapping.get(line[4:].strip(), line[4:].strip()) for line in output.splitlines() if line.startswith("BAD ")}
        return bad, len(mapping)


def read_baseline() -> set[str]:
    if not BASELINE.is_file():
        return set()
    return {line.split("#", 1)[0].strip() for line in BASELINE.read_text(encoding="utf-8").splitlines()} - {""}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--godot", default=os.environ.get("GODOT", "godot"), help="Godot 4.7+ executable")
    parser.add_argument("--update-baseline", action="store_true", help="rewrite gdscript_known_failures.txt")
    args = parser.parse_args()
    bad, total = run(args.godot)
    if args.update_baseline:
        header = [line for line in BASELINE.read_text(encoding="utf-8").splitlines() if line.startswith("#")] if BASELINE.is_file() else []
        BASELINE.write_text("\n".join(header + sorted(bad)) + "\n", encoding="utf-8", newline="\n")
        print(f"Baseline updated: {len(bad)} known failures out of {total} scripts")
        return
    known = read_baseline()
    new, fixed = sorted(bad - known), sorted(known - bad)
    for path in new:
        print(f"NEW FAILURE: {path}")
    for path in fixed:
        print(f"NOW COMPILES (remove from {BASELINE.name}): {path}")
    if new or fixed:
        sys.exit(1)
    print(f"PASS: {total - len(bad)}/{total} scripts compile; {len(bad)} known context-dependent failures")


if __name__ == "__main__":
    main()
