---
description: Validate Godot Game Dev Studio library metadata and packaging after editing skills, catalog entries, or compatibility files. Invoke with /godot-library-check.
disable-model-invocation: true
allowed-tools: Bash(python update_skills_index.py --validate), Bash(python scripts/validate_agent_support.py), Bash(python scripts/check_gdscript.py:*), Read, Glob, Grep
---

Validate repository changes without altering generated files unless the user explicitly asks to regenerate them.

1. Run `python update_skills_index.py --validate`.
2. Run `python scripts/validate_agent_support.py` (entrypoints, frontmatter, index completeness, godot-master mirrors, Markdown links, personal paths).
3. If a Godot 4.7+ executable is available (`GODOT` environment variable or `godot` on PATH), run `python scripts/check_gdscript.py`. Otherwise report that the compile check was skipped.
4. Run the standard Codex plugin validator configured in the current environment. If unavailable, report that validation unavailable.
5. Inspect `git diff --check`.
6. Report commands, pass/fail result, and exact warnings or failures. Do not hide pre-existing warnings.
7. If skill names or descriptions changed, tell user `python update_skills_index.py` must be run, but do not run it automatically.
