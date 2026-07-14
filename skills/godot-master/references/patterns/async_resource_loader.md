# Pattern: Async Resource Loader

Uses `ResourceLoader`'s threaded loading to prevent main-thread stalls during asset ingestion.

```gdscript
func _load_level_async(path: String) -> void:
    ResourceLoader.load_threaded_request(path)
    while ResourceLoader.load_threaded_get_status(path) == ResourceLoader.THREAD_LOAD_IN_PROGRESS:
        await get_tree().process_frame
    var scene: PackedScene = ResourceLoader.load_threaded_get(path)
    add_child(scene.instantiate())
```
