# Aurelius Protocol: Tilemap Mastery NEVER List

- **NEVER use set_cell() in loops without batching** — 1000 tiles × `set_cell()` = 1000 individual function calls = slow. Use `set_cells_terrain_connect()` for bulk OR cache changes, apply once.
- **NEVER forget source_id parameter** — `set_cell(pos, atlas_coords)` without source_id? Wrong overload = crash OR silent failure. Use `set_cell(pos, source_id, atlas_coords)`.
- **NEVER mix tile coordinates with world coordinates** — `set_cell(mouse_position)` without `local_to_map()`? Wrong grid position. ALWAYS convert: `local_to_map(global_pos)`.
- **NEVER skip terrain set configuration** — Manual tile assignment for organic shapes? 100+ tiles for grass patch. Use `set_cells_terrain_connect()` with terrain sets for autotiling.
- **NEVER use TileMap for dynamic entities** — Enemies/pickups as tiles? No signals, physics, scripts. Use Node2D/CharacterBody2D, reserve TileMap for static/destructible geometry.
- **NEVER query get_cell_tile_data() in _physics_process** — Every frame tile data lookup? Performance tank. Cache tile data in dictionary: `tile_cache[pos] = get_cell_tile_data(pos)`.
