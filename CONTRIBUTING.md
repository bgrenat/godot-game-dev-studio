# Contributing to Godot Game Dev Studio

Thank you for helping improve **Godot Game Dev Studio**, the Codex plugin distribution assembled and maintained by **[Powehi](https://powehi.eu)**.

This project builds on open Godot/game-development agentic skill resources, including work from **[Divergent AI / GD Agentic Skills](https://github.com/thedivergentai/gd-agentic-skills)**, **[awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills)**, **[GodotPrompter](https://github.com/jame581/GodotPrompter)**, **[Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)**, and **[godot-worldmap-builder](https://github.com/don-tnowe/godot-worldmap-builder)**. Contributions should preserve upstream attribution and license notices.

## Contribution principles

We are not building a beginner tutorial collection. We are building a practical, agent-first knowledge base for Godot and game-development work.

Every new or edited skill should add an expert knowledge delta:

- explain practical tradeoffs, not generic syntax
- include Godot 4.7+ specific guidance when relevant
- name anti-patterns and failure modes
- prefer reusable, production-shaped examples
- keep instructions concise enough for agent use

## Skill structure

Each skill lives in:

```text
skills/<skill-name>/
├── SKILL.md
├── references/
└── scripts/
```

`SKILL.md` must include YAML frontmatter:

```yaml
---
name: my-skill
description: What this skill does and when Codex should use it.
---
```

## Code and asset standards

- Use Godot 4.7+ idioms where possible.
- Keep GDScript statically typed when scripts are included.
- Avoid adding editor caches, build exports, or generated local state.
- Do not remove third-party license notices.
- Add attribution to [NOTICE.md](NOTICE.md) when importing or adapting external material.
- If a contribution is derived from another repository, name the source repository and its license in the PR.

## Validation

Before publishing a change, run:

```powershell
python C:\Users\x-v-i\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\x-v-i\plugins\godot-game-dev-studio
```

If you modify skill names or descriptions, regenerate or update `skills_index.json` as needed.

## License

By contributing, you agree that your contribution is licensed under the project license, **GNU Lesser General Public License v3.0 (LGPLv3)**, unless a file explicitly states a different compatible license.
