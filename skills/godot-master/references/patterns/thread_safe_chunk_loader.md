# Pattern: Thread-Safe Chunk Loader (Server API Pattern)

Bypass the scene tree for safe off-thread construction of scene chunks, attaching them only on the main thread.

```gdscript
func _load_chunk_threaded(chunk_pos: Vector2i) -> void:
    # Build scene chunk OFF the active tree (thread-safe)
    var chunk := _generate_chunk(chunk_pos)
    # Attach to live tree from main thread ONLY
    _world_root.add_child.call_deferred(chunk)
```
