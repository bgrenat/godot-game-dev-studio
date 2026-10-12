# threaded_ai_manager.gd
# Offloading server-side AI to worker threads
extends Node

# EXPERT NOTE: Server CPUs are often the bottleneck.
# Move bot behavior logic to the WorkerThreadPool.

func process_bots() -> void:
	var bot_ids := range(bots.size())
	WorkerThreadPool.add_group_task(_tick_bot, bot_ids.size())

func _tick_bot(index: int) -> void:
	# Bot logic running on secondary thread
	# CAUTION: Physics access must be synchronized!
	pass

var bots: Array = []
