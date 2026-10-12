# autoload_reference_checker.gd
# Validating singleton availability before access
extends Node

# EXPERT NOTE: In game code, reference an Autoload directly by its global name.
# Only use this optional lookup in addons/packages that must run even when the
# Autoload is not registered (the global name would fail to parse there).

static func get_events(tree: SceneTree) -> Node:
	var path := NodePath("/root/GlobalEvents")
	if tree.root.has_node(path):
		return tree.root.get_node(path)
	push_warning("GlobalEvents Autoload not found!")
	return null
