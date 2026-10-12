# currency_pickup_effect.gd
# Visual feedback for financial gains
extends GPUParticles2D

# EXPERT NOTE: Trigger visual effects via balance signals
# to ensure the world "feels" the impact of economic changes.

func _ready() -> void:
	WalletManager.balance_changed.connect(_on_balance_changed)

func _on_balance_changed(id: String, _amount: int) -> void:
	if id == "gold":
		restart()
