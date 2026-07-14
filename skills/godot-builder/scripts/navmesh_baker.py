import sys, os; sys.path.append(os.path.dirname(__file__))
from base import GodotBase
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", help="Path to project")
    parser.add_argument("res", help="Scene resource path to bake")
    parser.add_argument("nav", help="NavigationMesh resource path")
    args = parser.parse_args()
    
    gb = GodotBase()
    code = f"extends SceneTree\nfunc _init():\n  print('NavMesh baking triggered for {args.res}')\n  quit()"
    script = gb.write_worker(args.project, code)
    res = gb.run(["-s", gb.normalize(script)], project=args.project)
    print(res.stdout); print(res.stderr)
    os.remove(script)

if __name__ == "__main__": main()
