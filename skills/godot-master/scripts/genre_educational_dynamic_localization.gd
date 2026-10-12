# dynamic_localization.gd
# Transitioning between languages at runtime using tr()
extends Node

# EXPERT NOTE: tr() and atr() allow for dynamic localization
# without restarting the application.

func update_language(locale: String) -> void:
	TranslationServer.set_locale(locale)
	_refresh_ui_text()

func _refresh_ui_text() -> void:
	# Example for a button tag
	# get_node("StartButton").text = tr("KEY_START")
	pass

func get_apples_text(count: int) -> String:
	# EXPERT: Pluralization support via TranslationServer
	return atr_n("APPLE_COUNT_ONE", "APPLE_COUNT_MANY", count)
