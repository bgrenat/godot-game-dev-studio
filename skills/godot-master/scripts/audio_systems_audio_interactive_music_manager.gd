class_name InteractiveMusicManager
extends Node

## Expert manager for vertical music layering using AudioStreamSynchronized.
## Allows seamless crossfading between musical stems based on game intensity.

@export var music_player: AudioStreamPlayer

var _sync_stream: AudioStreamSynchronized

func _ready() -> void:
	if not music_player: return
	
	_sync_stream = music_player.stream as AudioStreamSynchronized
	if not _sync_stream:
		push_error("InteractiveMusicManager: AudioStreamPlayer must use an AudioStreamSynchronized resource.")
		return

## Fades a specific stem index to a target volume.
## stem_index matches the order in the AudioStreamSynchronized resource.
func fade_stem(index: int, target_db: float, duration: float = 2.0) -> void:
	if index >= _sync_stream.stream_count: return
	
	var current_vol = _sync_stream.get_sync_stream_volume(index)
	var tween = create_tween()
	
	tween.tween_method(
		func(v): _sync_stream.set_sync_stream_volume(index, v),
		current_vol,
		target_db,
		duration
	).set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_IN_OUT)

## Convenience method to mute all layers except the base.
func reset_to_base(base_index: int = 0) -> void:
	for i in range(_sync_stream.stream_count):
		var vol = 0.0 if i == base_index else -60.0
		fade_stem(i, vol, 1.0)
