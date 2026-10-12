class_name RevivalDeathTimer
extends Timer

## Expert Respawn Timer.
## Manages transition duration and UI callbacks for game-over screens.

@export var respawn_time: float = 3.0

func start_death_timer() -> void:
	wait_time = respawn_time
	one_shot = true
	start()
	# Trigger UI 'YOU DIED' here
	timeout.connect(_on_timeout)

func _on_timeout() -> void:
	_revival().trigger_death()

## Tip: Use 'one_shot' timers for death logic to avoid recursive respawns if dying during the timer.

## Autoload registered as "Revival" (an autoload cannot share the RevivalGlobalManager class_name).
func _revival() -> RevivalGlobalManager:
	return get_node(^"/root/Revival") as RevivalGlobalManager
