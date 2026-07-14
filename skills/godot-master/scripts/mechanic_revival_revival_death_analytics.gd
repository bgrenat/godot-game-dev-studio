class_name RevivalDeathAnalytics
extends Node

## Bridge for logging death events to a local JSON file.
## Essential for difficulty balancing and heatmap generation.

const LOG_PATH = "user://death_analytics.json"

## Logs a death event with context.
static func log_death(peer_id: int, position: Vector3, cause: String) -> void:
	var time = Time.get_datetime_dict_from_system()
	var timestamp = "%04d-%02d-%02d %02d:%02d:%02d" % [
		time.year, time.month, time.day,
		time.hour, time.minute, time.second
	]
	
	var entry = {
		"timestamp": timestamp,
		"peer_id": peer_id,
		"x": snappedf(position.x, 0.01),
		"y": snappedf(position.y, 0.01),
		"z": snappedf(position.z, 0.01),
		"cause": cause
	}
	
	var file = FileAccess.open(LOG_PATH, FileAccess.READ_WRITE)
	if not file:
		file = FileAccess.open(LOG_PATH, FileAccess.WRITE)
	
	if file:
		file.seek_end()
		file.store_line(JSON.stringify(entry))
		file.close()
