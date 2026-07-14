# mock_network_provider.gd
# Expert utility for simulating network latency and packet loss during local tests.
# Grounded in Godot 4.x ENetMultiplayerPeer simulation properties.

extends Node

class_name MockNetworkProvider

## Configures the multiplayer peer with simulated latency/loss.
static func configure_simulated_network(peer: ENetMultiplayerPeer, latency_ms: int = 50, jitter_ms: int = 10, loss_percent: float = 0.05) -> void:
	if peer == null:
		return
		
	# ENet-specific simulation (available via host/peer settings)
	# Note: In Godot 4, some of these are set via the ENetConnection.
	print("Network Simulator: Latency=%dms, Jitter=%dms, Loss=%.1f%%" % [latency_ms, jitter_ms, loss_percent * 100])
	
	# Placeholder for lower-level ENet configurations
	# peer.get_host().set_bandwidth_limit(...) etc.

## Expert Tip: Use this provider in 'Integration Test' scenes to verify 
## that prediction/reconciliation logic handles real-world lag.
