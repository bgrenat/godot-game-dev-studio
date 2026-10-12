# persistent_character_stats.gd
# Saving and loading character progression
extends Node

@export var stats: CharacterStats # Custom Resource

func save_stats() -> void:
	ResourceSaver.save(stats, "user://player_stats.tres")

func load_stats() -> void:
	if ResourceLoader.exists("user://player_stats.tres"):
		stats = load("user://player_stats.tres")
