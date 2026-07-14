# Physics Tuning

Reference for `skills/godot-optimization/SKILL.md` — collision layers, simplified shapes, tick rate, and Area-vs-raycast trade-offs.

> ← Back to [SKILL.md](../SKILL.md)

---

### Collision Layers and Masks

Every physics body checks for collisions against bodies whose layer is included in its mask. Unnecessary mask bits cause wasted broadphase work.

```gdscript
# Project Settings > Layer Names > 3D Physics defines readable names.
# Assign layers so bodies only collide with what they need to.

# Example layer assignments (set in Inspector or via code):
# Layer 1 — Player
# Layer 2 — Enemies
# Layer 3 — Environment
# Layer 4 — Projectiles
# Layer 5 — Triggers / Sensors

# Player: layer = 1, mask = 2 | 3          (collides with enemies and environment)
# Enemy:  layer = 2, mask = 1 | 3          (collides with player and environment)
# Bullet: layer = 4, mask = 2 | 3          (hits enemies and environment only)
# Sensor: layer = 5, mask = 1              (detects player only)

func _ready() -> void:
    # Set via code (bit index is layer number minus 1)
    collision_layer = 1 << 3   # this body is on layer 4 (Projectiles)
    collision_mask  = (1 << 1) | (1 << 2)  # checks layers 2 and 3
```

### Simplified Collision Shapes

Mesh colliders (`ConcavePolygonShape3D`) are extremely expensive. Replace with primitives wherever possible.

| Shape | Cost | Use for |
|---|---|---|
| `SphereShape3D` | Cheapest | Projectiles, pickups, rolling objects |
| `CapsuleShape3D` | Cheap | Characters, pillars |
| `BoxShape3D` | Cheap | Walls, crates, platforms |
| `ConvexPolygonShape3D` | Moderate | Irregular convex geometry |
| `ConcavePolygonShape3D` | Expensive | Static-only complex terrain (never on moving bodies) |

```gdscript
# WRONG — mesh collider on a moving character body
# CollisionShape3D with ConcavePolygonShape3D on CharacterBody3D

# RIGHT — capsule approximates the character with minimal cost
# CollisionShape3D with CapsuleShape3D

# For static terrain that must be exact: ConcavePolygonShape3D is acceptable
# on StaticBody3D only, and only if the mesh is not overly dense.
```

### Physics Tick Rate Tuning

The default physics tick is 60 Hz (`Engine.physics_ticks_per_second`). Lowering it reduces CPU load at the cost of simulation fidelity.

```gdscript
# Lower the physics tick rate at runtime (e.g. for a top-down game that
# does not need 60 Hz physics accuracy)
func _ready() -> void:
    Engine.physics_ticks_per_second = 30

# Use max_physics_steps_per_frame to prevent the spiral-of-death
# (physics trying to catch up when the frame takes too long)
Engine.max_physics_steps_per_frame = 4
```

**C#:**

```csharp
public override void _Ready()
{
    Engine.PhysicsTicksPerSecond = 30;
    Engine.MaxPhysicsStepsPerFrame = 4;
}
```

Change project-wide defaults in **Project Settings > Physics > Common > Physics Ticks Per Second** and **Max Physics Steps Per Frame**.

### Area2D for Detection vs Raycasts

For detecting whether something enters a region, `Area2D`/`Area3D` is cheaper than running a raycast or shape query every frame because the engine maintains the overlap state incrementally.

```gdscript
# PREFER Area2D for "is the player in range?" checks
extends Area2D

func _ready() -> void:
    body_entered.connect(_on_body_entered)
    body_exited.connect(_on_body_exited)

func _on_body_entered(body: Node2D) -> void:
    if body.is_in_group("player"):
        _begin_aggro(body)

func _on_body_exited(body: Node2D) -> void:
    if body.is_in_group("player"):
        _end_aggro()
```

**C#:**

```csharp
// PREFER Area2D for "is the player in range?" checks
public partial class AggroZone : Area2D
{
    public override void _Ready()
    {
        BodyEntered += OnBodyEntered;
        BodyExited += OnBodyExited;
    }

    private void OnBodyEntered(Node2D body)
    {
        if (body.IsInGroup("player"))
            BeginAggro(body);
    }

    private void OnBodyExited(Node2D body)
    {
        if (body.IsInGroup("player"))
            EndAggro();
    }
}
```

```gdscript
# Use raycasts only when you need directionality or line-of-sight checks,
# and cache the RayCast2D/3D node — do NOT create PhysicsRayQueryParameters
# every frame unless necessary.
@onready var _ray: RayCast3D = $RayCast3D

func _physics_process(_delta: float) -> void:
    if _ray.is_colliding():
        _handle_hit(_ray.get_collider())
```

**C#:**

```csharp
// Cache the RayCast3D node — do NOT create PhysicsRayQueryParameters every frame
private RayCast3D _ray;

public override void _Ready()
{
    _ray = GetNode<RayCast3D>("RayCast3D");
}

public override void _PhysicsProcess(double delta)
{
    if (_ray.IsColliding())
        HandleHit(_ray.GetCollider());
}
```
