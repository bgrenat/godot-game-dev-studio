# low_level_physics_query.gd
# Direct PhysicsServer queries for high performance
extends Node3D

# EXPERT NOTE: Direct space queries via DirectSpaceState
# are faster than RayCast nodes when doing hundreds of checks
# per frame (e.g. for AI vision or custom particles).

func _physics_process(_delta) -> void:
	var space_state = get_world_3d().direct_space_state
	var query = PhysicsRayQueryParameters3D.create(global_position, global_position + Vector3.FORWARD * 10)
	query.exclude = _self_exclusion()

	var result = space_state.intersect_ray(query)
	if result:
		# Handle hit
		pass

## Excludes the parent physics body (this helper node has no RID of its own).
func _self_exclusion() -> Array[RID]:
	var body := get_parent() as CollisionObject3D
	return [body.get_rid()] if body else []
