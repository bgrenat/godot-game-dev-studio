# Changelog

## 0.3.0 — Validated library

### Skills and index

- Index all 188 skills in `skills_index.json` (previously 96) and require a `Use when` clause in every description; the 93 imported skills that lacked one now describe when to use them.
- Remove `godot-ai-navigation`, a truncated duplicate of `godot-navigation-pathfinding`, and the unreferenced `godot-composition/resources/` duplicates.
- Fix 958 broken relative Markdown links (mostly in `godot-master` and `godot-auditor` reference copies); unlink 31 references to documents that never existed.

### GDScript

- Fix 88 scripts that did not compile with Godot 4.7: Godot 3 or non-existent APIs, wrong call signatures, Python-style syntax, `Node` scripts using 3D APIs, missing helper functions, a missing `Ability` base class, and strict-typing errors.
- Rename class names that collided inside a skill or with Godot 4.7 native classes (`VirtualJoystick` → `CustomVirtualJoystick`).
- Fix `worldmap_builder` for Godot 4.7 (`_property_can_revert` must always return a bool).
- Add static types to library scripts: untyped variables drop from 1,284 to 579 and untyped functions from 389 to 57, with no new compile failure.
- Rename `ortho_to_perspective_fx` to `.gdshader` (it is a shader, not GDScript).

### Tooling and CI

- `scripts/check_gdscript.py` compiles every library script with Godot 4.7; CI runs it, with documented context-dependent exceptions in `scripts/gdscript_known_failures.txt`.
- `validate_agent_support.py` now checks index completeness and duplicates, frontmatter names, `godot-master` mirror sync, Markdown links, and personal paths, and only reads text files.
- `update_skills_index.py` produces deterministic output, strips quoted descriptions, and exits non-zero on `--validate` warnings; CI checks the committed index is current.
- The generated Claude Code entrypoint now has `name`/`description` frontmatter.
- Add native Claude Code project skills for routing and library validation, and read-only subagents for skill routing and Godot quality review.

## 0.2.0 — Multi-agent integrations

- Add portable entrypoints for Claude Code, Cursor, and VS Code + Copilot.
- Add generated agent-rule tooling and validation for all 189 skills.
- Add contributor documentation for agent integrations and MCP.
- Add GitHub Actions validation for manifests, skills, and generated files.
- Update the plugin description to present the project as a multi-agent Godot toolkit.


## 0.1.0 — Initial Codex plugin distribution

Initial public release of **Godot Game Dev Studio** as a Codex plugin assembled by **[Powehi](https://powehi.eu)**.

### Added

- Codex plugin manifest in `.codex-plugin/plugin.json`
- plugin icon and presentation metadata
- Powehi credit links in plugin metadata
- packaged Godot/game-development skill library
- studio-style orchestration skills
- machine-readable `skills_index.json`
- supporting assets and examples

### Provenance

This release curates and adapts open Godot/game-development skill resources, including material from **Divergent AI / GD Agentic Skills**, **awesome-gamedev-agent-skills**, **GodotPrompter**, **Claude-Code-Game-Studios**, and **godot-worldmap-builder**. See [NOTICE.md](NOTICE.md).

## Upstream history

Earlier GD Agentic Skills history belongs to the upstream project:

- [thedivergentai/gd-agentic-skills](https://github.com/thedivergentai/gd-agentic-skills)
