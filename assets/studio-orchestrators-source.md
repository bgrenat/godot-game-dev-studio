# Studio Orchestrators Source Notes

The `studio-*` orchestrator skills are a Codex/Godot adaptation inspired by:

- Donchitos/Claude-Code-Game-Studios
- https://github.com/Donchitos/Claude-Code-Game-Studios

The adaptation keeps the useful studio concepts:

- director and lead roles;
- vertical delegation;
- horizontal consultation;
- conflict escalation;
- phase gates from concept through release;
- team workflows for gameplay, UI, QA, release, polish, and level design.

It intentionally does not copy the Claude-specific runtime shape:

- no `.claude/settings.json`;
- no Claude hooks;
- no automatic subagent spawning;
- no Claude slash-command dependency;
- no forced approval protocol beyond normal Codex task safety.

In this plugin, orchestrators are plain Codex skills. They route requests to the existing `godot-*`, `godot-prompter-*`, and `gamedev-*` skill families and provide a lightweight studio coordination layer.
