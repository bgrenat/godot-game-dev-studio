class_name ProcGenGraphLayout
extends Node

## Expert pattern for managing dungeon layouts using AStar data structures.
## Decouples logical connections (rooms/hallways) from physical geometry.

var layout_graph := AStar2D.new()

## Adds a room node to the layout.
func add_room(id: int, pos: Vector2) -> void:
	layout_graph.add_point(id, pos)

## Connects two rooms with a hallway.
func connect_rooms(id_a: int, id_b: int, bidirectional: bool = true) -> void:
	layout_graph.connect_points(id_a, id_b, bidirectional)

## Returns all rooms in the layout.
func get_all_rooms() -> PackedInt64Array:
	return layout_graph.get_point_ids()

## Returns connections for a specific room (e.g. to determine where doors should be).
func get_room_connections(id: int) -> PackedInt64Array:
	return layout_graph.get_point_connections(id)

## Returns the spatial distance between two connected rooms.
func get_hallway_length(id_a: int, id_b: int) -> float:
	return layout_graph.get_point_position(id_a).distance_to(layout_graph.get_point_position(id_b))
