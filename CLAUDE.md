# Claude Code instructions

Use this repository as a Godot 4.7+ game-development skill library.

Before implementing or reviewing Godot code:

1. Read [SKILL_CATALOG.md](SKILL_CATALOG.md) or [skills_index.json](skills_index.json).
2. Select the most relevant `skills/<skill-name>/SKILL.md`.
3. Read that skill and only the references it requires.
4. Apply Godot 4.7+ patterns, static typing, and the anti-patterns documented by the selected skill.
5. If the task is broad, start with `skills/studio-router/SKILL.md` or `skills/godot-master/SKILL.md`.

Never ingest all skills blindly. This repository contains 188 skills.

## Native Claude Code integration

- Use `/godot-route` before broad Godot, game-design, or GDScript work. It selects and loads smallest relevant skill set.
- Delegate focused catalog discovery to `godot-skill-router` when exploration would crowd main task context.
- Delegate read-only implementation review to `godot-quality-reviewer` after non-trivial Godot changes.
- Use `/godot-library-check` after editing skills, skill metadata, or compatibility files.
- `.claude/settings.local.json` is per-developer and ignored. Never add secrets or machine-specific paths to tracked configuration.

Preserve Powehi and upstream attribution from [NOTICE.md](NOTICE.md).
