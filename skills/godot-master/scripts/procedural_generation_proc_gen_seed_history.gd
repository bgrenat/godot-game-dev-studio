class_name ProcGenSeedHistory
extends Node

## Expert Seed & State History Manager.
## Ensures deterministic procedural generation and allows "undo/redo" of random sequences.

var rng := RandomNumberGenerator.new()
var state_history: Array[int] = []

func _ready() -> void:
	rng.randomize()

## Seeds the generator and clears history.
func initialize_seed(new_seed: int) -> void:
	rng.seed = new_seed
	state_history.clear()

## Records the current RNG state before a generation step.
func push_state() -> void:
	state_history.append(rng.state)

## Restores the RNG to a previous state.
func pop_state() -> void:
	if state_history.is_empty(): return
	rng.state = state_history.pop_back()

## Returns the current seed string (useful for sharing).
func get_seed_string() -> String:
	return str(rng.seed)
