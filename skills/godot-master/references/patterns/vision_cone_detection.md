# Pattern: Vision Cone Detection

Expert pattern for NPC vision using dot products for angle checks and low-level raycasts for line-of-sight.

```gdscript
class_name StealthNPC extends CharacterBody3D

@export var fov_degrees: float = 90.0
@export var vision_range: float = 20.0
@export var detection_time: float = 2.0 # Seconds to fully detect at point-blank

var detection_meter: float = 0.0
@onready var head: Node3D = $Head

func _physics_process(delta: float) -> void:
    var player = get_tree().get_first_node_in_group("player")
    if not player: return
    
    if _can_see_target(player):
        var distance = global_position.distance_to(player.global_position)
        var distance_factor = clampf(1.0 - (distance / vision_range), 0.1, 1.0)
        
        detection_meter += (delta / detection_time) * distance_factor
        if detection_meter >= 1.0:
            print("Player Detected!")
    else:
        detection_meter = maxf(0.0, detection_meter - delta * 0.5)

func _can_see_target(target: Node3D) -> bool:
    var eyes_pos = head.global_position
    var target_pos = target.global_position + Vector3(0, 1, 0) # Aim for chest/head
    
    # 1. Distance Check
    if eyes_pos.distance_squared_to(target_pos) > vision_range * vision_range:
        return false
        
    # 2. Dot Product (Angle) Check
    var forward_dir = -head.global_transform.basis.z.normalized()
    var dir_to_target = eyes_pos.direction_to(target_pos)
    
    var fov_radians = deg_to_rad(fov_degrees)
    if forward_dir.dot(dir_to_target) < cos(fov_radians / 2.0):
        return false 
        
    # 3. Raycast (Line of Sight) Check
    var space_state = get_world_3d().direct_space_state
    var query = PhysicsRayQueryParameters3D.create(eyes_pos, target_pos)
    query.collision_mask = 1 | 2 # e.g., World and Player layers
    
    var result = space_state.intersect_ray(query)
    
    if result and result.collider == target:
        return true 
        
    return false
```
