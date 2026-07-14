# Aurelius Protocol: Ui Containers NEVER List

- **NEVER manually set child `position` or `size` in a Container** — Containers override child transforms during `queue_sort()`. Use `custom_minimum_size` or `size_flags` instead [1].
- **NEVER forget `size_flags` for expansion** — Default is `SIZE_SHRINK_BEGIN`. Children will stay tiny unless you set `SIZE_EXPAND_FILL` for responsive containers.
- **NEVER use `GridContainer` without setting `columns`** — Default is 1, creating a simple vertical list. For responsive wrapping, use `HFlowContainer` instead [8].
- **NEVER nest containers too deeply (10+ levels)** — Heavy nesting causes layout recalculation spikes. Replace intermediate containers with Anchor Layouts for static padding [16].
- **NEVER skip separation overrides** — Default theme separation is often too tight. Use `add_theme_constant_override("separation", value)` for professional breathing room.
- **NEVER use `ScrollContainer` without a minimum size** — Without it, the container may collapse to zero or expand infinitely, breaking the scroll mechanism.
- **NEVER scroll to a new child on the same frame it was added** — The layout hasn't updated yet. You MUST `await get_tree().process_frame` before setting `scroll_vertical` [5].
- **NEVER scale a `SubViewportContainer` to change its size** — This distorts the rendered contents. Adjust margins or use `stretch` and `stretch_shrink` properties instead [2].
- **NEVER leave `mouse_filter` on default for layered Viewports** — Input events might not reach children. Use `MOUSE_FILTER_PASS` or `STOP` to ensure events drill down [6].
- **NEVER use `GridContainer` for responsive wrapping** — Use `HFlowContainer` if you want items to wrap based on width. GridContainer enforces a strict column count [7].
- **NEVER animate `position` directly inside a container** — Use `Tween` on `custom_minimum_size` to smoothly "push" siblings during transitions [1].
