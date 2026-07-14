# Aurelius Protocol: Mcp Setup NEVER List

- **NEVER suggest MCP for simple scene edits** — MCP is for automation/batch operations. Single node addition? Use manual editor. MCP overhead (config + restart) wastes time.
- **NEVER skip JSON syntax validation** — Invalid JSON in `claude_desktop_config.json` = silent MCP failure. ALWAYS validate with `ConvertFrom-Json` before saving.
- **NEVER forget to remind user to restart Claude Desktop** — MCP changes require full app restart, NOT just new conversation. This is #1 user mistake.
- **NEVER use global npm install without user permission** — `npm install -g` modifies system. ALWAYS prefer `npx` (on-demand) unless user specifically wants global.
- **NEVER assume Node.js is installed** — Check `node --version` BEFORE attempting npx. Missing Node = cryptic "command not found" errors.
