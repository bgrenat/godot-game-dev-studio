extends Node

class_name SubtitleSyncSystem

signal subtitle_show(text: String)
signal subtitle_hide()

@export var audio_player: AudioStreamPlayer

# Array of dictionaries: {"time": float, "text": String}
var _subtitle_track: Array[Dictionary] = []
var _current_index: int = -1

func start_dialogue(track: Array[Dictionary]) -> void:
	_subtitle_track = track
	_current_index = -1
	subtitle_hide.emit()

func _process(_delta: float) -> void:
	if not audio_player.playing or _subtitle_track.is_empty():
		return
	
	# Elite Pattern: Latency-Compensated Playback Position
	# get_playback_position() is chunked; adding time_since_last_mix and 
	# subtracting output_latency gives the true hardware-synced time.
	var time := audio_player.get_playback_position() + AudioServer.get_time_since_last_mix()
	time -= AudioServer.get_output_latency()
	
	_update_subtitles(time)

func _update_subtitles(current_time: float) -> void:
	var target_index = -1
	
	# Find the latest subtitle that should be visible
	for i in range(_subtitle_track.size()):
		if current_time >= _subtitle_track[i].time:
			target_index = i
		else:
			break
			
	if target_index != _current_index:
		_current_index = target_index
		if _current_index != -1:
			subtitle_show.emit(_subtitle_track[_current_index].text)
		else:
			subtitle_hide.emit()
