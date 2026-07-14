---
name: studio-systems-designer
description: "Coordinate inventory, stats, economy, quests, progression, save/load, resources, and data-driven Godot systems."
---

# Studio Systems Designer

Use for game systems that persist, balance, interact, or drive progression: inventory, items, stats, economy, crafting, quests, rewards, abilities, unlocks, and save/load.

## Load With

- `godot-resource-data-patterns`
- `godot-inventory-system`
- `godot-rpg-stats`
- `godot-quest-system`
- `godot-economy-system`
- `godot-save-load-systems`
- `godot-ability-system`
- `godot-prompter-resource-pattern`
- `godot-prompter-save-load`
- `gamedev-save-systems`
- `gamedev-rpg`
- `gamedev-survival-crafting`

## Systems Gate

Define:

- Entities and resources.
- State that persists.
- Rules and formulas.
- Versioning/migration needs.
- UI touchpoints.
- Balance knobs.
- Failure cases and exploits.

## Defaults

- Prefer custom `Resource` types for definitions.
- Keep runtime state separate from static definitions.
- Version save data from day one.
- Make formulas visible and editable.
- Test edge cases before adding content volume.

## Output

Produce:

- Data model.
- Runtime state model.
- Save/load impact.
- UI and gameplay integrations.
- Balance/test checklist.
