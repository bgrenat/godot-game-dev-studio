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
description: What this skill does. Use when <the situations that should trigger it>.
---
```

- `name` must match the folder name.
- `description` must contain a `Use when` clause (or `Keywords:`); `update_skills_index.py --validate` enforces it.
- Relative links in Markdown must resolve; the validator checks every link.

## Code and asset standards

- Use Godot 4.7+ idioms where possible.
- Keep GDScript statically typed when scripts are included.
- Scripts must compile with Godot 4.7. A snippet that needs game context (an autoload, an addon, an asset) may be listed in `scripts/gdscript_known_failures.txt`; document that dependency in the script header.
- Do not reuse a `class_name` already declared by another script of the same skill, and never shadow a native Godot class.
- Edit `godot-*` scripts in their own skill, then copy them to their `skills/godot-master/scripts/` mirror.
- Avoid adding editor caches, build exports, or generated local state.
- Do not remove third-party license notices.
- Add attribution to [NOTICE.md](NOTICE.md) when importing or adapting external material.
- If a contribution is derived from another repository, name the source repository and its license in the PR.

## Validation

Before publishing a change, run:

```bash
python update_skills_index.py            # regenerate skills_index.json after adding/renaming a skill or editing a description
python update_skills_index.py --validate # every description needs a "Use when" clause or keywords
python scripts/generate_agent_rules.py --target all
python scripts/validate_agent_support.py # entrypoints, frontmatter, index completeness, godot-master mirrors, Markdown links, personal paths
python scripts/check_gdscript.py --godot <path-to-godot-4.7>  # compiles every library script
```

Also run the Codex plugin validator if it is installed (`python <codex-plugin-validator>/validate_plugin.py .`). GitHub Actions runs all checks above, including the Godot 4.7 compile step.

## License

By contributing, you agree that your contribution is licensed under the project license, **GNU Lesser General Public License v3.0 (LGPLv3)**, unless a file explicitly states a different compatible license.
