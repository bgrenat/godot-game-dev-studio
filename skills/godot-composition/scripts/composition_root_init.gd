# composition_root_init.gd
# The "Smart Parent" pattern for wiring components
extends CharacterBody2D

# EXPERT NOTE: The parent node acts as the 'orchestrator' or
# 'composition root' that connects disparate components.

@onready var health := $HealthComponent
@onready var hitbox := $HitBoxComponent
@onready var velocity_comp := $VelocityComponent

func _ready() -> void:
	# Wire components together
	hitbox.health_component = health

	# Respond to component signals
	health.health_depleted.connect(_on_death)

func _physics_process(delta) -> void:
	# Delegation
	velocity_comp.accelerate_in_direction(Input.get_vector("left", "right", "up", "down"), delta)
	velocity_comp.apply_velocity(self)

func _on_death() -> void:
	queue_free()
