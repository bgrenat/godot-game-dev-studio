# Aurelius Protocol: Project Templates NEVER List

- **NEVER hardcode scene paths** — `get_tree().change_scene_to_file("res://levels/level_1.tscn")` in 20 places? Nightmare refactoring. Use AutoLoad + constants OR scene registry.
- **NEVER skip .gdignore for asset folders** — Designer internal project files should never be imported into res:// directly.
- **NEVER use `get_tree().paused` without groups** — Pausing entire tree = pause menu freezes. Use process mode `PROCESS_MODE_ALWAYS` on UI.
- **NEVER skip virtual lifecycle hooks** — In base classes, always provide `_initialize_X()` hooks instead of just `_ready()` to allow child overrides without breaking parents.
- **NEVER rely on monolithic "God" singletons** — Decouple systems using a **Signal Bus** or **Subsystem Locator**.
- **NEVER skip Input.MOUSE_MODE_CAPTURED in FPS** — Set in player `_ready()` to ensure focus.
- **NEVER use floating point constants for UI layout** — Leads to drift. Use anchors and containers.
- **NEVER ignore i18n Translation Context** — "Lead" (Metal) vs "Lead" (Action). Strictly use contexts in `translate()`.
- **NEVER load massive levels synchronously** — Causes frame freezes. Strictly use `ResourceLoader.load_threaded_request()`.
- **NEVER copy-paste templates as-is** — Using platformer template for RPG? Leads to debt. UNDERSTAND the structure, then adapt.
