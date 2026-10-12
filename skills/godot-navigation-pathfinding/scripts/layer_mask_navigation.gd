# layer_mask_navigation.gd
# Toggling agent capabilities (e.g. Flying vs Walking) using bitmasks
extends Node

enum NavLayers {
	WALK = 1,
	JUMP = 2,
	FLY = 4,
	SWIM = 8
}

func set_agent_capability(agent: NavigationAgent3D, layers: int) -> void:
	# Navigation layers use a 32-bit integer bitmask.
	# This allows one agent to only use specific regions/links.
	agent.navigation_layers = layers

func unlock_swimming(agent: NavigationAgent3D) -> void:
	agent.navigation_layers |= NavLayers.SWIM # Add swim bit
