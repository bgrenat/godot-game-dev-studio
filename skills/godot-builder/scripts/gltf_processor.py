import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to project")
    parser.add_argument("gltf", help="GLTF/GLB path")
    parser.add_argument("out", help="Output .tscn path")
    args = parser.parse_args()
    
    gb = GodotBase()
    code = f"""extends SceneTree
func _init():
    var doc = GLTFDocument.new()
    var state = GLTFState.new()
    var err = doc.append_from_file("{args.gltf}", state)
    if err == OK:
        var root = doc.generate_scene(state)
        var packed = PackedScene.new()
        packed.pack(root)
        ResourceSaver.save(packed, "{args.out}")
        print("Converted glTF to tscn")
    quit()"""
    script = gb.write_worker(args.project, code)
    res = gb.run(["-s", gb.normalize(script)], project=args.project)
    print(res.stdout); print(res.stderr)
    os.remove(script)

if __name__ == "__main__": main()
