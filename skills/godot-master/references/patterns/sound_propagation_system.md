# Pattern: Sound Propagation System

Centralized manager for gameplay sound events with raycast-based occlusion.

```gdscript
# sound_manager.gd (Autoload)
extends Node

@export var wall_occlusion_multiplier: float = 0.4 # Walls block 60% of sound

func emit_noise(origin: Vector3, base_radius: float) -> void:
    var listeners = get_tree().get_nodes_in_group("listeners")
    var space_state = get_viewport().find_world_3d().direct_space_state
    
    for npc in listeners:
        var dist_sq = origin.distance_squared_to(npc.global_position)
        
        if dist_sq > base_radius * base_radius:
            continue
            
        var effective_radius = base_radius
        
        # Check for occlusion
        var query = PhysicsRayQueryParameters3D.create(origin, npc.global_position)
        query.collision_mask = 1 # Layer 1: World/Walls only
        
        var result = space_state.intersect_ray(query)
        if result:
            effective_radius *= wall_occlusion_multiplier
            
        if dist_sq <= effective_radius * effective_radius:
            if npc.has_method("investigate_sound"):
                npc.investigate_sound(origin)
```
