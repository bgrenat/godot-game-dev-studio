---
name: studio-godot-addon-integrator
description: "Evaluate, integrate, isolate, and document Godot addons, editor plugins, tools, and third-party dependencies."
---

# Studio Godot Addon Integrator

Use when adding or evaluating a Godot addon, editor plugin, tool script, native extension, asset pipeline helper, or repository-provided addon such as Worldmap Builder.

## Load With

- `godot-project-foundations`
- `godot-scene-management`
- `godot-export-builds`
- `godot-testing-patterns`
- `godot-prompter-addon-development`
- `godot-prompter-assets-pipeline`
- `godot-prompter-gdextension`

## Addon Gate

Before adoption, check:

- License compatibility.
- Godot version compatibility.
- Files installed under `addons/`.
- Runtime vs editor-only code.
- Export/platform impact.
- Maintenance risk.
- How hard removal would be.

## Worldmap Builder Note

The plugin includes `assets/godot-worldmap-builder` as a reference addon for branching world maps, level selection, and skill trees. Prefer a small integration spike before committing a production dependency.

## Output

Produce:

- Adopt, spike, fork, or reject recommendation.
- Install path.
- Scene/API usage.
- Risks.
- Test/export checklist.
