class_name HarvestAutoSaveManager
extends Node

## Manages interval-based auto-saving for harvest progress.
## Uses FileAccess and JSON for serialization to user://.

@export var save_interval: float = 60.0 # Seconds
@export var save_path: String = "user://harvest_progress.json"

var _timer: Timer

func _ready() -> void:
	_timer = Timer.new()
	_timer.wait_time = save_interval
	_timer.autostart = true
	add_child(_timer)
	_timer.timeout.connect(execute_save)

## Collects data from the game and saves to disk.
func execute_save() -> void:
	# Note: In a real project, pull this from a global Inventory or Stats manager
	var data_to_save = _gather_harvest_data()
	
	var file = FileAccess.open(save_path, FileAccess.WRITE)
	if file:
		var json_string = JSON.stringify(data_to_save)
		file.store_line(json_string)
		print_rich("[color=cyan][Harvest] Progress auto-saved to %s[/color]" % save_path)
	else:
		push_error("Failed to open save file at %s" % save_path)

func _gather_harvest_data() -> Dictionary:
	# Placeholder for actual data gathering logic
	return {
		"timestamp": Time.get_datetime_dict_from_system(),
		"resources": {} # Populate with actual inventory counts
	}
