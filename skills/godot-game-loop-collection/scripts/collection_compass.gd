class_name CollectionCompass
extends Sprite2D

## Spatial Radar/Compass for tracking collectibles.
## Rotates the sprite to point towards the nearest or targeted collectible.

@export var search_group: StringName = &"collectible"
@export var rotation_speed: float = 10.0

var target_collectible: Node2D

func _process(delta: float) -> void:
	# Find nearest collectible if we don't have a target
	if not is_instance_valid(target_collectible):
		target_collectible = _find_nearest_collectible()
	
	if is_instance_valid(target_collectible):
		# Calculate the target rotation using look_at or direction_to
		var target_pos = target_collectible.global_position
		var angle_to_target = get_angle_to(target_pos)
		
		# Smoothly rotate towards the target
		rotation += angle_to_target * rotation_speed * delta

func _find_nearest_collectible() -> Node2D:
	var collectibles = get_tree().get_nodes_in_group(search_group)
	var nearest: Node2D = null
	var min_dist = INF
	
	for c in collectibles:
		if c is Node2D:
			var dist = global_position.distance_to(c.global_position)
			if dist < min_dist:
				min_dist = dist
				nearest = c
	
	return nearest
