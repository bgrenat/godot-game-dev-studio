---
description: Validate Godot Game Dev Studio library metadata and packaging after editing skills, catalog entries, or compatibility files. Invoke with /godot-library-check.
disable-model-invocation: true
allowed-tools: Bash(python update_skills_index.py --validate), Bash(python C:/Users/x-v-i/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .), Read, Glob, Grep
---

Validate repository changes without altering generated files unless the user explicitly asks to regenerate them.

1. Run `python update_skills_index.py --validate`.
2. Run `python C:/Users/x-v-i/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .` if that script exists; otherwise report that validation unavailable.
3. Inspect `git diff --check`.
4. Report commands, pass/fail result, and exact warnings or failures. Do not hide pre-existing warnings.
5. If skill names or descriptions changed, tell user `python update_skills_index.py` must be run, but do not run it automatically.
