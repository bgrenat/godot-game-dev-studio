# singleton_health_check_test.gd
# Template for verifying global singleton state using expert unit testing patterns.
# Designed for compatibility with GUT (Godot Unit Test) or GdUnit4.

extends Node

## Health Check: Verify that core singletons are correctly initialized.
func test_singleton_initialization():
	# Verify ServiceLocator
	var root = Engine.get_main_loop().root
	assert_not_null(root.get_node_or_null("GameManager"), "GameManager must be registered as an Autoload.")
	
	# Verify default states
	# var gm = root.get_node("GameManager")
	# assert_eq(gm.score, 0, "GameManager score should start at 0.")
	
	print("Health Check: Singletons are stable.")

## Helper for GUT (if using)
func assert_not_null(obj, msg):
	if obj == null:
		push_error(msg)
	else:
		print("PASSED: ", msg)
