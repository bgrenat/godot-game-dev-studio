# marking_rubrics_atlas.gd
# Centralized registry for genre-specific benchmarks and architectural rubrics.
# Grounded in expert Godot 4.x performance and structure standards.

extends RefCounted

class_name MarkingRubricsAtlas

## Benchmarks for different genres.
const RUBRICS := {
	"RPG": {
		"max_autoload_count": 8,
		"max_nested_systems": 3,
		"forced_layering": true, # Domain/Infrastructure separation
		"performance": {
			"static_memory_cap": 256 * 1024 * 1024, # 256MB
			"target_fps": 60
		}
	},
	"FPS": {
		"max_autoload_count": 5,
		"max_nested_systems": 2,
		"forced_layering": true,
		"performance": {
			"static_memory_cap": 512 * 1024 * 1024, # 512MB
			"target_fps": 144
		}
	}
}

## Validates a project configuration against a genre rubric.
static func validate_project_config(genre: String, current_config: Dictionary) -> Dictionary:
	if not RUBRICS.has(genre):
		return {"error": "Genre %s not found in atlas." % genre}
		
	var rubric = RUBRICS[genre]
	var issues := []
	
	if current_config.get("autoload_count", 0) > rubric["max_autoload_count"]:
		issues.append("EXCESSIVE_AUTOLOADS: %d vs %d allowed" % [current_config["autoload_count"], rubric["max_autoload_count"]])
		
	return {
		"passed": issues.is_empty(),
		"issues": issues
	}
