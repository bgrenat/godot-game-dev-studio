---
name: studio-gameplay-lead
description: "Coordinate player movement, combat, abilities, camera, enemies, input, game feel, and moment-to-moment Godot gameplay implementation."
---

# Studio Gameplay Lead

Use for playable mechanics: movement, combat, abilities, enemies, interaction, camera, controls, feedback, and core loop implementation.

## Load With

- `godot-characterbody-2d`
- `godot-input-handling`
- `godot-state-machine-advanced`
- `godot-ability-system`
- `godot-combat-system`
- `godot-camera-systems`
- `godot-ai-navigation`
- `godot-prompter-player-controller`
- `godot-prompter-input-handling`
- `gamedev-game-feel`
- Genre skills matching the project.

## Gameplay Gate

Before changing code, clarify:

- Player verb and expected feel.
- Input device and buffering needs.
- State ownership.
- Failure states and recovery.
- Camera relationship.
- Required feedback: animation, sound, particles, shake, pause, UI.

## Implementation Bias

- Keep controller logic explicit and testable.
- Separate input collection from movement resolution.
- Use state machines when behavior has clear modes.
- Keep tuning values exported or resource-backed.
- Add debug visibility for complex mechanics.

## Output

Provide:

- Mechanic contract.
- Scene/node structure.
- State/data flow.
- Skills used.
- Playtest checklist.
