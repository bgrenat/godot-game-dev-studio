# Agent compatibility

The `SKILL.md` files are the portable source of truth. The repository also ships small entrypoints for each editor/agent so that the full library is not loaded into context automatically.

## Supported integrations

| Tool | Integration | Entry point |
| --- | --- | --- |
| Codex | Native plugin manifest | `.codex-plugin/plugin.json` |
| Claude Code | Project skill | `.claude/skills/godot-game-dev-studio/SKILL.md` |
| Cursor | Project rule | `.cursor/rules/godot-game-dev-studio.mdc` |
| VS Code + Copilot | Repository instructions | `.github/copilot-instructions.md` |

Regenerate the entrypoints after changing the master skill:

```bash
python scripts/generate_agent_rules.py --target all
python scripts/validate_agent_support.py
```

Use the smallest matching skill under `skills/` for a focused task. The generated files are orientation layers; they do not replace the detailed skills.
