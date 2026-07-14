import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to project")
    parser.add_argument("json", help="JSON layout string")
    parser.add_argument("out", help="Output .tscn path")
    args = parser.parse_args()
    
    gb = GodotBase()
    code = f"""extends SceneTree\nfunc _init():\n  var root = Control.new()\n  var packed = PackedScene.new()\n  packed.pack(root)\n  ResourceSaver.save(packed, "{args.out}")\n  quit()"""
    script = gb.write_worker(args.project, code)
    res = gb.run(["-s", gb.normalize(script)], project=args.project)
    print(res.stdout); print(res.stderr)
    os.remove(script)

if __name__ == "__main__": main()
