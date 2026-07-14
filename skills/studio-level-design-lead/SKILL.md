---
name: studio-level-design-lead
description: "Coordinate levels, maps, tiles, world building, progression paths, procedural generation, encounters, and Godot worldmap/skill-tree screens."
---

# Studio Level Design Lead

Use for maps, levels, rooms, encounter pacing, tilemaps, 3D spaces, world maps, skill trees, route graphs, procedural generation, and level-select screens.

## Load With

- `godot-tilemap-mastery`
- `godot-3d-world-building`
- `godot-camera-systems`
- `godot-navigation-pathfinding`
- `godot-procedural-generation`
- `godot-prompter-2d-essentials`
- `godot-prompter-3d-essentials`
- `gamedev-level-design`
- `gamedev-procedural-gen`

## Worldmap Builder Asset

For skill trees, level selection screens, and branching world maps, inspect `assets/godot-worldmap-builder` in this plugin. Treat it as a candidate addon, not a default dependency. Ask the technical director gate before adopting it into a project.

## Level Gate

Define:

- Player route and possible branches.
- Critical path vs optional content.
- Camera constraints.
- Navigation and collision needs.
- Encounter rhythm.
- Progression locks/unlocks.
- Authoring workflow for designers.

## Output

Produce:

- Layout model.
- Tile/scene/addon approach.
- Progression graph.
- Validation pass: traversal, camera, collision, pacing.
