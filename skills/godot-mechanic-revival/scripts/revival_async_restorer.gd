class_name RevivalAsyncRestorer
extends Node

## Expert Asynchronous Restoration logic.
## Smoothly refills actor stats (Health, Mana, Energy) over time using Tweens.

@export var restoration_duration: float = 3.0

## Begins a smooth restoration of a specific property.
func restore_property(target: Node, property: String, target_value: float) -> void:
	if not target or not property in target:
		return
		
	var tween = create_tween().bind_node(self)
	
	# Organic S-curve restoration
	tween.set_trans(Tween.TRANS_SINE)
	tween.set_ease(Tween.EASE_IN_OUT)
	
	tween.tween_property(target, property, target_value, restoration_duration)

## Convenience for full health/mana recovery
func full_revive(actor: Node, max_hp: float, max_mp: float) -> void:
	restore_property(actor, "health", max_hp)
	restore_property(actor, "mana", max_mp)
