# dialogue_portrait_manager.gd
# Handling speaker expressions visually
extends TextureRect

func _ready() -> void:
	DialogueManager.line_started.connect(_on_line_started)

func _on_line_started(node: DialogueNode) -> void:
	if node.portrait:
		texture = node.portrait
		# Add tween for "entry" animation
