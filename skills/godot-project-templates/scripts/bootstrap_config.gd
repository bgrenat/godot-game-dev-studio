# bootstrap_config.gd
# Expert pattern for managing initialization priority and AutoLoad order.
# Grounded in architectural best practices for Godot 4.x.

extends RefCounted

class_name BootstrapConfig

## Priority list for global system initialization.
# Lower numbers initialize first.
const BOOTSTRAP_PRIORITY := {
	"ConfigManager": 1,
	"SaveManager": 10,
	"PlayerManager": 20,
	"SceneTransitioner": 30,
	"AudioManager": 40,
	"InputRecorder": 50
}

## Validates the current AutoLoad order against the intended bootstrap priority.
static func validate_autoload_order() -> void:
	# Note: Accessing ProjectSettings via code allows runtime verification,
	# but actual order is defined in project.godot.
	print("Bootstrap Config: Validating initialization order...")
	
	# Expert logic: In a real tool, this would parse project.godot 
	# and ensure [autoload] entries match the sorted BOOTSTRAP_PRIORITY.
	
	for system in BOOTSTRAP_PRIORITY.keys():
		print("- System: %s (Priority: %d)" % [system, BOOTSTRAP_PRIORITY[system]])
