# Aurelius Protocol: Procedural Generation NEVER List

- **NEVER generate chunks on the Main Thread** — Proc-gen is CPU intensive and causes frame-rate spikes. Use `WorkerThreadPool` or a background `Thread` to keep the UI responsive.
- **NEVER query `FastNoiseLite` every frame** — Sampling noise per frame (especially in `_process`) is a massive waste. Generate your map into an `Image` or `Array` once and sample from memory [NoiseSampling].
- **NEVER use `randi()` for reproducible seeds** — Always store and reuse a specific `seed` within your random number generator (`RandomNumberGenerator.new()`) to ensure consistent world generation.
- **NEVER use pure randomness for object placement** — Pure random (white noise) causes clumping and overlapping. Use **Poisson Disk Sampling** or **Jittered Grids** for natural-looking distributions.
- **NEVER forget to bound your loops** — Procedural loops (like WFC or Cellular Automata) can easily enter infinite states if constraints are impossible. Always include a `max_iterations` safety break.
- **NEVER instantiate nodes directly from proc-gen threads** — You cannot touch the SceneTree from a worker thread. Generate the *data* in the thread, then notify the Main Thread to handle `add_child()`.
- **NEVER use complex WFC for simple layouts** — Wave Function Collapse is powerful but overkill for simple paths. Use **Drunkard's Walk** or **BSP** for lightweight structured layouts.
- **NEVER rely on `TileMap.set_cell()` for large-scale updates** — Updating 10,000 cells individually is slow. Prepare a `TileMapPattern` and use `set_pattern()` or `set_cells_terrain_connect()` for batch updates.
- **NEVER forget to bake Navigation at the end** — Procedurally generated worlds need their navmeshes rebaked at runtime or the AI will walk into walls.
- **NEVER ignore data serialization** — If you generate a world, you must be able to save the *seed* and any *player modifications*. Don't try to save the entire raw chunk state if avoidable.
