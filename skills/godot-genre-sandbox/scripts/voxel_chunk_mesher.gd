extends MeshInstance3D
class_name VoxelChunkMesher

## Expert Voxel Meshing (Godot 4.7).
## Uses SurfaceTool with background threading (WorkerThreadPool).

const CHUNK_SIZE = 16
var _voxels: PackedByteArray # 16x16x16 = 4096 bytes

func regenerate_mesh() -> void:
	# Expert Pattern: Offload generation to save frame budget
	WorkerThreadPool.add_task(_build_surface)

func _build_surface() -> void:
	var st = SurfaceTool.new()
	st.begin(Mesh.PRIMITIVE_TRIANGLES)

	for x in CHUNK_SIZE:
		for y in CHUNK_SIZE:
			for z in CHUNK_SIZE:
				if _get_voxel(x, y, z) > 0:
					_add_visible_faces(st, x, y, z)

	st.index()
	st.generate_normals()
	var final_mesh = st.commit()

	# Thread-safe assignment
	call_deferred("set_mesh", final_mesh)

func _add_visible_faces(st: SurfaceTool, x: int, y: int, z: int) -> void:
	# Face Culling: Only add faces if the neighbor is transparent/air
	if _get_voxel(x, y + 1, z) == 0:
		_add_face(st, Vector3(x, y + 1, z), Vector3.UP)

func _get_voxel(x, y, z) -> int:
	if x < 0 or x >= CHUNK_SIZE or y < 0 or y >= CHUNK_SIZE or z < 0 or z >= CHUNK_SIZE:
		return 0
	return _voxels[x + (y * CHUNK_SIZE) + (z * CHUNK_SIZE * CHUNK_SIZE)]

## [SKILL NOTICE]: Use 'WorkerThreadPool' to generate voxel meshes.
## This prevents frame drops when players modify large chunks of the world.

## Emits one unit quad for the voxel face pointing along `normal`.
func _add_face(st: SurfaceTool, pos: Vector3, normal: Vector3) -> void:
	var u := Vector3(normal.y, normal.z, normal.x) * 0.5 # first tangent
	var v := normal.cross(u) # second tangent
	var center := pos + Vector3(0.5, 0.5, 0.5) + normal * 0.5
	var corners := [center - u - v, center + u - v, center + u + v, center - u + v]
	st.set_normal(normal)
	for idx in [0, 1, 2, 0, 2, 3]:
		st.add_vertex(corners[idx])
