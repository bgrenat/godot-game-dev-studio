---
name: studio-ui-ux-game-lead
description: "Coordinate HUD, menus, responsive Godot Control layouts, input navigation, accessibility, and game-facing UX flows."
---

# Studio UI UX Game Lead

Use for HUDs, menus, pause/settings screens, inventory UI, dialogue UI, controller navigation, accessibility, localization-ready layouts, and responsive Godot `Control` work.

## Load With

- `godot-ui-containers`
- `godot-ui-theming`
- `godot-ui-rich-text`
- `godot-input-handling`
- `godot-prompter-godot-ui`
- `godot-prompter-hud-system`
- `godot-prompter-responsive-ui`
- `gamedev-game-ui-ux`
- `gamedev-input-systems`

## UX Gate

Define:

- Primary player goal on the screen.
- Information priority.
- Input methods and focus order.
- Scaling behavior and safe areas.
- Accessibility tier.
- Localization risk.
- Game state ownership boundaries.

## Godot UI Defaults

- Use containers, anchors, and themes; avoid fixed pixel positioning for dynamic UI.
- Keep UI state separate from gameplay ownership.
- Support keyboard/controller focus for navigable screens.
- Make text expandable and localization-safe.
- Prefer signals for UI-to-game communication.

## Output

Produce:

- Screen flow.
- Node hierarchy.
- Data/event contract.
- Responsive behavior.
- Accessibility checks.
