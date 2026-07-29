# Compatibility with AI coding tools

Godot Game Dev Studio is packaged as a Codex plugin, but the skill files are plain Markdown and can be used by other AI coding tools.

The important rule for every tool is the same:

1. Start with [skills_index.json](skills_index.json) or [SKILL_CATALOG.md](SKILL_CATALOG.md).
2. Select the smallest relevant skill set.
3. Read the selected `skills/<name>/SKILL.md`.
4. Read only the referenced files required by that skill.
5. Preserve [NOTICE.md](NOTICE.md), [LICENSE](LICENSE), and upstream attribution when copying or adapting content.

## Supported instruction files in this repository

| Tool | File added | Purpose |
| --- | --- | --- |
| Codex and generic agents | [AGENTS.md](AGENTS.md) | Repository-level agent instructions |
| Claude Code | [CLAUDE.md](CLAUDE.md) | Claude Code project memory/instructions |
| VS Code GitHub Copilot | [.github/copilot-instructions.md](.github/copilot-instructions.md) | Copilot Chat workspace instructions |
| Cursor | [.cursor/rules/godot-game-dev-studio.mdc](.cursor/rules/godot-game-dev-studio.mdc) | Cursor project rule |
| Gemini CLI | [GEMINI.md](GEMINI.md) | Gemini project instructions |

## Claude Code

Claude Code can use this repository through `CLAUDE.md` and native project configuration in `.claude/`:

- `.claude/skills/godot-route/`: explicit routing command, `/godot-route`.
- `.claude/skills/godot-library-check/`: explicit metadata and packaging validation, `/godot-library-check`.
- `.claude/agents/godot-skill-router.md`: read-only catalog-routing subagent.
- `.claude/agents/godot-quality-reviewer.md`: read-only Godot review subagent.

These files are versioned project configuration. Local Claude Code preferences belong in `.claude/settings.local.json`, which is ignored.

Recommended workflow:

```bash
git clone https://github.com/powehi-eu/godot-game-dev-studio.git
cd godot-game-dev-studio
claude
```

Start work with `/godot-route`, then ask Claude Code to use only selected skill references. After library edits, run `/godot-library-check`. Claude Code discovers project skills and subagents from `.claude/`; restart once if this is the first `.claude/` directory seen by an already-running session.

## VS Code / GitHub Copilot

GitHub Copilot Chat in VS Code can use `.github/copilot-instructions.md` as workspace instructions.

Recommended workflow:

```bash
git clone https://github.com/powehi-eu/godot-game-dev-studio.git
code godot-game-dev-studio
```

In Copilot Chat, ask for Godot help while referencing the repository. The instructions tell Copilot to route through `skills_index.json`, `SKILL_CATALOG.md`, and the relevant `SKILL.md` files.

## Cursor

Cursor can use `.cursor/rules/godot-game-dev-studio.mdc`.

Recommended workflow:

```bash
git clone https://github.com/powehi-eu/godot-game-dev-studio.git
cursor godot-game-dev-studio
```

The rule is always applied inside this repository and tells Cursor to use the skill catalog instead of improvising from generic Godot knowledge.

## Gemini CLI

Gemini CLI can use `GEMINI.md`.

Recommended workflow:

```bash
git clone https://github.com/powehi-eu/godot-game-dev-studio.git
cd godot-game-dev-studio
gemini
```

Ask Gemini to route tasks through `skills_index.json` and the appropriate `SKILL.md`.

## Other useful CLI/agent integrations

These tools can also consume the repository as plain Markdown:

- **OpenAI Codex CLI / Codex app**: use this as the native Codex plugin or as a cloned skill reference repository.
- **Aider**: add a short project note pointing to `AGENTS.md`, `SKILL_CATALOG.md`, and `skills_index.json`.
- **Cline / Roo Code**: add the repository as workspace context and ask the agent to follow `AGENTS.md`.
- **Continue.dev**: index the repository or pin `SKILL_CATALOG.md` plus the needed `SKILL.md` files.

For all tools, avoid loading every skill at once. This plugin contains 189 skills; use the catalog to choose the smallest useful subset.
