class_name ProcGenMarchingCubesBase
extends MeshInstance3D

## Base class for 3D terrain generation using ArrayMesh.
## Provides the foundation for Marching Cubes or Voxel geometry.

func update_geometry(vertices: PackedVector3Array, normals: PackedVector3Array, indices: PackedInt32Array) -> void:
	var surface_array = []
	surface_array.resize(Mesh.ARRAY_MAX)
	
	surface_array[Mesh.ARRAY_VERTEX] = vertices
	surface_array[Mesh.ARRAY_NORMAL] = normals
	surface_array[Mesh.ARRAY_INDEX] = indices
	
	var arr_mesh = ArrayMesh.new()
	# PRIMITIVE_TRIANGLES is the standard for 3D surfaces
	arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, surface_array)
	
	self.mesh = arr_mesh
	
	# Optimization: Generate collision if needed
	# create_trimesh_collision() 
