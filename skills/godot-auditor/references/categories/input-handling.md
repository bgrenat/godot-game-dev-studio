# Aurelius Protocol: Input Handling NEVER List

- **NEVER poll input in `_process()` for gameplay actions** — Use `_physics_process()` or `_unhandled_input()`. `_process()` is frame-rate dependent, causing dropped inputs at low FPS [22].
- **NEVER use hardcoded key checks (e.g., `KEY_W`)** — Always use `InputMap` actions. Hardcoded keys prevent rebinding and break compatibility with non-QWERTY layouts [23].
- **NEVER ignore analog stick deadzones** — Drifting sticks at 0.05 magnitude will cause unintended movement. Implement a radial deadzone (not axial) in code or settings [24].
- **NEVER assume a single input device** — Players may switch between Keyboard and Controller mid-session. Use `Input.joy_connection_changed` to update UI prompts dynamically [25].
- **NEVER use `_input()` for gameplay actions** — `_input()` fires for ALL events (including UI). Use `_unhandled_input()` so gameplay logic doesn't trigger while clicking menus [26].
- **NEVER omit input buffering in fast-paced games** — If a player presses jump 50ms before landing, the input is lost without a buffer. Implement a 100-150ms buffer for a "tight" feel [27].
- **NEVER use `Input.is_action_pressed()` for one-time triggers** — It returns true every frame the key is held. Use `_just_pressed` for jumps, attacks, and toggles to avoid logic spam.
- **NEVER implement manual 'Hold vs Toggle' logic in multiple places** — Centralize it in a setting or input wrapper to ensure accessibility consistency across the whole game.
- **NEVER forget to handle `InputEvent.is_echo()` in UI navigation** — Echo events (keyboard repeat) should move menus but rarely should they trigger "Confirm" or "Back" actions.
- **NEVER capture the mouse without a 'Release' shortcut** — If your game crashes or blocks `ui_cancel`, the user is trapped. Always provide a fallback escape for mouse capture.
