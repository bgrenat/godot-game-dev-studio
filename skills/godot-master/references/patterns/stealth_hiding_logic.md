# Pattern: Stealth Hiding Logic

Global visibility management using Area3D zones and concealment modifiers.

```gdscript
# hiding_zone.gd (Attached to an Area3D)
extends Area3D

enum CoverType { BUSH, SHADOW, LOCKER }
@export var cover_type: CoverType = CoverType.BUSH

func _ready() -> void:
    body_entered.connect(_on_body_entered)
    body_exited.connect(_on_body_exited)

func _on_body_entered(body: Node3D) -> void:
    if body.is_in_group("player"):
        VisibilityManager.add_cover(cover_type)

func _on_body_exited(body: Node3D) -> void:
    if body.is_in_group("player"):
        VisibilityManager.remove_cover(cover_type)

# visibility_manager.gd (Autoload)
extends Node

var active_covers: Array = []

func add_cover(cover) -> void:
    if not active_covers.has(cover):
        active_covers.append(cover)

func remove_cover(cover) -> void:
    active_covers.erase(cover)

func get_visibility_multiplier() -> float:
    if active_covers.has(CoverType.LOCKER):
        return 0.0 
    elif active_covers.has(CoverType.BUSH):
        return 0.2 
    elif active_covers.has(CoverType.SHADOW):
        return 0.5 
    return 1.0 
```
