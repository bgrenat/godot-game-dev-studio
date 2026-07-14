# Pattern: Dead Instance Safe Signal Handler

Ensures that signals don't attempt to access objects that are queued for deletion or already freed.

```gdscript
func _on_damage_dealt(target: Node, amount: int) -> void:
    if not is_instance_valid(target): return
    if target.is_queued_for_deletion(): return
    target.get_component(&"health").apply_damage(amount)
```
