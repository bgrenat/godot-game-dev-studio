class_name VRSafetyGuardianWarner
extends Node

## Expert guardian/chaperone proximity warner.
## Uses the XRServer to fetch reference bounds and warns if player is too close.

@export var camera: XRCamera3D

func _process(_delta: float) -> void:
	# The play area is a polygon in the XR reference frame (empty if no boundary is set).
	var interface := XRServer.primary_interface
	if interface == null: return
	var area := interface.get_play_area()
	if area.is_empty(): return
	var polygon := PackedVector2Array()
	for p in area: polygon.append(Vector2(p.x, p.z))
	var cam_pos_2d := Vector2(camera.position.x, camera.position.z)
	if not Geometry2D.is_point_in_polygon(cam_pos_2d, polygon):
		_warn_player_out_of_bounds()

func _warn_player_out_of_bounds() -> void:
	# Trigger visual/haptic warning
	pass

## Rule: Respecting real-world physical space is a safety requirement for VR.
