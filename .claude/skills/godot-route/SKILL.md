---
description: Route a Godot or game-development task to the smallest relevant Godot Game Dev Studio skill set. Use when planning, implementing, reviewing, debugging, or when the user asks which skill to use.
disable-model-invocation: true
---

Route this task through the library before doing any implementation.

1. Read `skills_index.json`; use `SKILL_CATALOG.md` only if needed.
2. Choose the smallest relevant skill set, normally one skill and never more than three.
3. Read every selected `skills/<skill-name>/SKILL.md` fully.
4. Read only files directly required by those skill instructions.
5. State selected skills and proceed with requested work.

Prefer skill families as follows:

- `studio-*`: orchestration, production, QA, planning, multi-role routing.
- `godot-*`: Godot systems, architecture, APIs, debugging, optimization.
- `godot-prompter-*`: guided implementation workflows.
- `gamedev-*`: genre, design, and broad game-development workflows.

Keep Godot guidance at 4.7+ and GDScript statically typed. Preserve attribution in `NOTICE.md` and `LICENSE`.
