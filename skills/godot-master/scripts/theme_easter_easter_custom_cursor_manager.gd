extends Node
## Expert logic for swapping system mouse cursors with themed Easter icons.

func _ready() -> void:
    _apply_easter_cursor()

func _apply_easter_cursor() -> void:
    # Example implementation from reference
    var cursor_img = preload("res://ui/easter/cursor_bunny.png")
    if cursor_img:
        Input.set_custom_mouse_cursor(cursor_img, Input.CURSOR_ARROW, Vector2(16, 16))
    else:
        push_warning("Easter cursor image not found.")
