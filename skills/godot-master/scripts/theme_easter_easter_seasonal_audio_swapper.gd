extends Node
## Dynamic audio resource loader that replaces standard UI sounds with seasonal variants.

@export var sound_overrides: Dictionary # String -> AudioStream
@onready var sfx_player: AudioStreamPlayer = AudioStreamPlayer.new()

var default_sounds: Dictionary = {}

func _ready() -> void:
    add_child(sfx_player)

func play_seasonal_sfx(original_name: String) -> void:
    var stream = sound_overrides.get(original_name, default_sounds.get(original_name))
    if stream:
        sfx_player.stream = stream
        sfx_player.play()
    else:
        push_warning("Sound not found for: " + original_name)
