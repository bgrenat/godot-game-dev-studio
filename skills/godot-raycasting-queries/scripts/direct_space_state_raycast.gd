# direct_space_state_raycast.gd
# Querying physics state directly via PhysicsServer for max speed
extends Node3D

func fire_laser(origin: Vector3, end: Vector3) -> void:
	var space_state = get_world_3d().direct_space_state

	# create() is a fast helper to initialize the query parameters
	var query = PhysicsRayQueryParameters3D.create(origin, end)
	query.exclude = _self_exclusion() # Expert: Use RID for faster exclusion

	var result = space_state.intersect_ray(query)

	if result:
		print("Hit at point: ", result.position)
		print("Collider: ", result.collider)

## Excludes the parent physics body (this helper node has no RID of its own).
func _self_exclusion() -> Array[RID]:
	var body := get_parent() as CollisionObject3D
	return [body.get_rid()] if body else []
