class_name WaveWeightedSpawner
extends Marker3D

## Wave spawner with weighted random enemy selection.
## Ensures wave variety by controlling spawn probabilities.

@export var enemy_scenes: Array[PackedScene] = []
## Parallel array to enemy_scenes. Higher values = higher probability.
@export var spawn_weights: PackedFloat32Array = []
@export var spawn_radius: float = 2.0

var _rng := RandomNumberGenerator.new()

func _ready() -> void:
	_rng.randomize()

## Spawns a randomly selected enemy based on weights.
func spawn_enemy() -> Node3D:
	if enemy_scenes.is_empty() or spawn_weights.size() != enemy_scenes.size():
		push_error("WaveWeightedSpawner: enemy_scenes and spawn_weights must match in size.")
		return null
	
	# Expert weighted selection using RNG.rand_weighted
	var index = _rng.rand_weighted(spawn_weights)
	var enemy = enemy_scenes[index].instantiate() as Node3D
	
	add_child(enemy)
	enemy.global_position = _get_random_pos()
	
	return enemy

func _get_random_pos() -> Vector3:
	var angle = randf() * TAU
	var distance = randf() * spawn_radius
	return global_position + Vector3(cos(angle) * distance, 0, sin(angle) * distance)
