import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to project")
    parser.add_argument("layer", help="TileMapLayer resource path")
    parser.add_argument("json", help="JSON string of cell coordinates")
    args = parser.parse_args()
    
    gb = GodotBase()
    code = f"""extends SceneTree
func _init():
    print("TileMap generation started with data: {args.json}")
    quit()"""
    script = gb.write_worker(args.project, code)
    res = gb.run(["-s", gb.normalize(script)], project=args.project)
    print(res.stdout); print(res.stderr)
    os.remove(script)

if __name__ == "__main__": main()
