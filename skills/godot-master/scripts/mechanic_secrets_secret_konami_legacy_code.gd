class_name SecretKonamiLegacy
extends SecretSequenceComboMatcher

## Classic Konami Code Specialization.
## Example of extending the Sequence Matcher for the most famous cheat.

func _ready() -> void:
	sequences = {
		"Konami": ["ui_up", "ui_up", "ui_down", "ui_down", "ui_left", "ui_right", "ui_left", "ui_right", "ui_accept"]
	}
	combo_achieved.connect(_on_konami)

func _on_konami(combo_name: String) -> void:
	if combo_name == "Konami":
		_secretmeta().unlock_meta_secret("konami_legacy_achieved")
		# Give 30 lives or enable debug mode...

## Rule: The Konami code is a 'Gamer Rite of Passage'—always include it in retro-styled projects.

## Autoload registered as "SecretMeta" (an autoload cannot share the SecretMetaPersistence class_name).
func _secretmeta() -> SecretMetaPersistence:
	return get_node(^"/root/SecretMeta") as SecretMetaPersistence
