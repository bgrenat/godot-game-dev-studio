# manual_culling_logic.gd
# Disabling off-screen logic manually
extends VisibleOnScreenNotifier2D

# EXPERT NOTE: VisibilityNotifiers are the most efficient
# way to cull heavy _process or _physics_process logic
# when nodes are not visible to the camera.

func _ready() -> void:
	screen_entered.connect(_on_screen_entered)
	screen_exited.connect(_on_screen_exited)

func _on_screen_entered() -> void:
	set_process(true)
	set_physics_process(true)

func _on_screen_exited() -> void:
	set_process(false)
	set_physics_process(false)
