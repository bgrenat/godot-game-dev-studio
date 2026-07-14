# Aurelius Protocol: Mcp Scene Builder NEVER List

- **NEVER skip design phase** — Jumping straight to `mcp_godot_add_node` without planning hierarchy = spaghetti scenes. ALWAYS draft node tree first.
- **NEVER assume scene exists before adding nodes** — `mcp_godot_add_node` on non-existent scene = error. Must call `mcp_godot_create_scene` FIRST.
- **NEVER use absolute paths in MCP calls** — `texturePath="C:/Users/..."` breaks on other machines. Use `res://` paths only.
- **NEVER skip verification step** — MCP creates .tscn files but doesn't validate. ALWAYS call `mcp_godot_run_project` or `mcp_godot_launch_editor` to verify no errors.
- **NEVER add CollisionShape2D without setting shape** — MCP adds node but `shape` property is null by default. Must manually set or scene is broken.
