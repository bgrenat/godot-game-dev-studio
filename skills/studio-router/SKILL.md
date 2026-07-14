---
name: studio-router
description: "Route broad Godot and game-development requests to the right GD Agentic Skills studio orchestrator, specialist skills, and quality gates."
---

# Studio Router

Use this first when a request is broad, ambiguous, multi-disciplinary, or project-stage oriented: concept, prototype, feature planning, architecture, implementation, review, polish, release, or rescue work.

## Routing Pass

1. Detect the project stage:
   - concept: no game loop, vague idea, genre exploration.
   - systems design: mechanics, progression, economy, content, UX, or level rules are being defined.
   - technical setup: scene architecture, save/load, input, resources, autoloads, networking, build/export, addons.
   - production: concrete feature implementation or refactor.
   - polish: performance, feel, balance, UX, bugs, accessibility.
   - release: export, platform readiness, patch notes, launch checklist.

2. Select the lead orchestrator:
   - concept or direction: `studio-game-director`
   - architecture or engine choice: `studio-godot-technical-director`
   - feature planning or schedule: `studio-producer`
   - player mechanics/combat/abilities: `studio-gameplay-lead`
   - economy/inventory/progression/save: `studio-systems-designer`
   - levels/maps/world/skill tree screens: `studio-level-design-lead`
   - HUD/menus/input/accessibility: `studio-ui-ux-game-lead`
   - narrative/dialogue/localization: `studio-narrative-content-lead`
   - addon/plugin/tool integration: `studio-godot-addon-integrator`
   - QA, playtest, regression: `studio-qa-playtest-lead`
   - profiling, export, launch: `studio-performance-release-lead`

3. Load only the specialist skills needed for the current request.

## Specialist Skill Families

- Core Godot: `godot-project-foundations`, `godot-scene-management`, `godot-gdscript-mastery`, `godot-signal-architecture`, `godot-resource-data-patterns`, `godot-autoload-architecture`.
- GodotPrompter depth: `godot-prompter-godot-project-setup`, `godot-prompter-gdscript-patterns`, `godot-prompter-gdscript-advanced`, `godot-prompter-godot-code-review`.
- Gameplay: `godot-characterbody-2d`, `godot-input-handling`, `godot-state-machine-advanced`, `godot-ability-system`, `godot-combat-system`, `godot-ai-navigation`, `gamedev-game-feel`.
- Systems: `godot-inventory-system`, `godot-rpg-stats`, `godot-quest-system`, `godot-economy-system`, `godot-save-load-systems`, `gamedev-save-systems`.
- World and levels: `godot-tilemap-mastery`, `godot-3d-world-building`, `godot-camera-systems`, `gamedev-level-design`, `gamedev-procedural-gen`.
- UI and UX: `godot-ui-containers`, `godot-ui-theming`, `godot-ui-rich-text`, `godot-prompter-responsive-ui`, `gamedev-game-ui-ux`.
- Tech and release: `godot-performance-optimization`, `godot-debugging-profiling`, `godot-testing-patterns`, `godot-export-builds`, `godot-platform-web`, `godot-platform-mobile`, `gamedev-itch-publish`, `gamedev-steam-publish`.

## Coordination Rules

- Keep one lead orchestrator for the decision.
- Use additional orchestrators only for cross-domain impact.
- Present trade-offs when a choice changes architecture, scope, player experience, or release risk.
- Implement directly when the request is concrete and safe; ask only when missing context would materially change the result.
- End with the next useful validation step: run, inspect, test, profile, export, or playtest.

## Output

For broad requests, return:

1. Lead orchestrator.
2. Skills to load, in order.
3. Decision gates to apply.
4. Implementation or review plan.
5. Verification target.
