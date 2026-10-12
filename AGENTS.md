# Agent instructions for Godot Game Dev Studio

This repository is a multi-tool AI skill library for Godot 4.7+ game development.

When helping with a Godot or game-development task:

1. Inspect [SKILL_CATALOG.md](SKILL_CATALOG.md) or [skills_index.json](skills_index.json).
2. Choose the smallest relevant skill family:
   - `studio-*` for orchestration, planning, production, QA, and role routing.
   - `godot-*` for core Godot expert guidance.
   - `godot-prompter-*` for GodotPrompter-style implementation workflows.
   - `gamedev-*` for broader game-design and game-development workflows.
3. Read the selected `skills/<skill-name>/SKILL.md`.
4. Read referenced files only when they are needed.
5. Prefer Godot 4.7+ APIs and GDScript with static typing.
6. Preserve upstream credits and license notices from [NOTICE.md](NOTICE.md) and [LICENSE](LICENSE).

Do not load all 188 skills into context at once. Route first, then read narrowly.
