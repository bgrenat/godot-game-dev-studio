# skills/ability-system/scripts/ability.gd
class_name Ability
extends Node

## Base node for abilities managed by AbilityContainer.
## Scenes listed in AbilityContainer.initial_abilities must have this script (or a subclass) on their root.

@export var ability_name: StringName
@export var cooldown: float = 0.0

## Override to gate activation (resources, state, targeting...).
func can_activate(_context: Dictionary) -> bool:
	return true

## Override with the ability's effect.
func activate(_context: Dictionary) -> void:
	pass
