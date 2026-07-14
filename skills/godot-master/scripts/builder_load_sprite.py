import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to project")
    parser.add_argument("res", help="Scene resource path")
    parser.add_argument("name", help="Node name to target")
    parser.add_argument("sprite", help="Sprite resource path (res://...)")
    args = parser.parse_args()
    
    gb = GodotBase()
    code = f"extends SceneTree\nfunc _init():\n  var s = load('{args.res}')\n  if s:\n    var r = s.instantiate()\n    var n = r.find_child('{args.name}', true, false)\n    if n and n is Sprite2D:\n      n.texture = load('{args.sprite}')\n      var p = PackedScene.new()\n      p.pack(r)\n      ResourceSaver.save(p, '{args.res}')\n  quit()"
    script = gb.write_worker(args.project, code)
    res = gb.run(["-s", gb.normalize(script)], project=args.project)
    print(res.stdout); print(res.stderr)
    os.remove(script)

if __name__ == "__main__": main()
